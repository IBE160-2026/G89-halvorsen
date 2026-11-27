#!/usr/bin/env python3
"""Read-only, local parser probe. Full extracted content stays in a private tmp folder.

Location probes verify only page/excerpt lookup consistency; they do not establish
PDF fidelity, correct reading order, complete coverage, or factual support.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import io
import json
import logging
import platform
import re
import resource
import subprocess
import sys
import time
import unicodedata
import warnings
from pathlib import Path


DEFAULT_INPUT = Path.cwd() / 'test-data/pdfs'
DEFAULT_OUTPUT = Path('/private/tmp/ai-study-buddy-pdf-probe')


def digest(value: bytes | str) -> str:
    if isinstance(value, str):
        value = value.encode('utf-8', errors='replace')
    return hashlib.sha256(value).hexdigest()


def sanitized_error(exc: BaseException) -> dict:
    return {'type': type(exc).__name__, 'message_sha256': digest(str(exc))}


def normalized(value: str) -> str:
    return ' '.join(unicodedata.normalize('NFC', value).split())


def text_metrics(value: str) -> dict:
    return {
        'chars': len(value),
        'words': len(value.split()),
        'nonwhitespace_chars': sum(not c.isspace() for c in value),
        'replacement_chars': value.count('\ufffd'),
        'unexpected_controls': sum(
            unicodedata.category(c) in {'Cc', 'Cf'} and c not in '\t\r\n'
            for c in value
        ),
        'sha256': digest(value),
    }


class DiagnosticCapture(logging.Handler):
    def __init__(self):
        super().__init__()
        self.events = []

    def emit(self, record):
        self.events.append({
            'logger': record.name,
            'level': record.levelname,
            'message_sha256': digest(record.getMessage()),
        })


def location_match(pages: list[str], page_number, excerpt) -> str | None:
    if type(page_number) is not int or not 1 <= page_number <= len(pages):
        return None
    if not isinstance(excerpt, str) or not excerpt.strip():
        return None
    page = pages[page_number - 1]
    if excerpt in page:
        return 'exact'
    if normalized(excerpt) in normalized(page):
        return 'nfc_whitespace'
    return None


def candidate_excerpts(text: str) -> list[str]:
    """Return reproducible literal windows; never join/reorder source words."""
    spans = list(re.finditer(r'\S+', text))
    if len(spans) < 3:
        return []
    out = []
    for ratio in (0.15, 0.45, 0.75, 0.0):
        start = min(int(len(spans) * ratio), max(0, len(spans) - 3))
        end = min(start + 18, len(spans))
        excerpt = text[spans[start].start():spans[end - 1].end()]
        if len(excerpt.strip()) >= 20 and excerpt not in out:
            out.append(excerpt)
    return out


def citation_probes(pages: list[str]) -> tuple[dict, dict]:
    normalized_pages = [normalized(p) for p in pages]
    samples = []
    counts = {
        'sampled_pages': 0,
        'pages_without_unique_excerpt': 0,
        'exact_roundtrip_pass': 0,
        'normalized_roundtrip_pass': 0,
        'wrong_page_tests': 0,
        'wrong_page_rejections': 0,
        'altered_excerpt_rejections': 0,
        'empty_excerpt_rejections': 0,
        'invalid_page_rejections': 0,
        'unexpected_acceptances': 0,
    }
    for index, text in enumerate(pages):
        choices = candidate_excerpts(text)
        unique = [e for e in choices if sum(normalized(e) in p for p in normalized_pages) == 1]
        if not unique:
            counts['pages_without_unique_excerpt'] += 1
            continue
        excerpt = unique[0]
        number = index + 1
        counts['sampled_pages'] += 1
        exact = location_match(pages, number, excerpt) == 'exact'
        # Both canonical Unicode decomposition and changed whitespace must be
        # accepted only through the documented NFC + whitespace lookup path.
        changed = '\t  ' + '\n\t'.join(unicodedata.normalize('NFD', excerpt).split()) + '  '
        norm = location_match(pages, number, changed) is not None
        counts['exact_roundtrip_pass'] += int(exact)
        counts['normalized_roundtrip_pass'] += int(norm)
        wrong_accepted = []
        for wrong in range(1, len(pages) + 1):
            if wrong == number:
                continue
            counts['wrong_page_tests'] += 1
            rejected = location_match(pages, wrong, excerpt) is None
            counts['wrong_page_rejections'] += int(rejected)
            if not rejected:
                wrong_accepted.append(wrong)
                counts['unexpected_acceptances'] += 1
        absent = 'PDF_PROBE_ABSENT_' + digest(excerpt) + ' ' + excerpt
        rejected = location_match(pages, number, absent) is None
        counts['altered_excerpt_rejections'] += int(rejected)
        counts['unexpected_acceptances'] += int(not rejected)
        samples.append({
            'physical_page': number,
            'literal_excerpt': excerpt,
            'exact_pass': exact,
            'nfc_whitespace_pass': norm,
            'wrong_pages_accepted': wrong_accepted,
            'altered_rejected': rejected,
        })
    for value in ('', ' \n\t', None):
        rejected = location_match(pages, 1, value) is None
        counts['empty_excerpt_rejections'] += int(rejected)
        counts['unexpected_acceptances'] += int(not rejected)
    for number in (0, -1, len(pages) + 1, '1', 1.5, True):
        rejected = location_match(pages, number, 'PDF_PROBE') is None
        counts['invalid_page_rejections'] += int(rejected)
        counts['unexpected_acceptances'] += int(not rejected)
    return counts, {'scope': 'location consistency only; extracted-text-derived samples', 'samples': samples}


def peak_rss_bytes() -> int:
    value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return int(value if sys.platform == 'darwin' else value * 1024)


def write_json(path: Path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def probe_document(args) -> int:
    started = time.perf_counter()
    source = args.input_dir / (args.document + '.pdf')
    destination = args.output_dir / args.library / args.document
    destination.mkdir(parents=True, exist_ok=True)
    (destination / 'plain').mkdir(exist_ok=True)
    (destination / 'layout').mkdir(exist_ok=True)
    log_capture = DiagnosticCapture()
    log = logging.getLogger(args.library)
    old_handlers, old_propagate = log.handlers[:], log.propagate
    log.handlers, log.propagate = [log_capture], False
    pages = []
    extraction_elapsed = {'plain': 0.0, 'layout': 0.0, 'tables': 0.0}
    errors = []
    caught = []
    document = None
    parse_elapsed = None
    summary = {
        'document': args.document,
        'library': args.library,
        'library_version': importlib.metadata.version(args.library),
        'python': platform.python_version(),
        'platform': platform.platform(),
        'file_bytes': source.stat().st_size,
        'source_sha256': digest(source.read_bytes()),
        'content_output_is_private': True,
        'reading_order_and_coverage': 'require independent visual/manual review',
    }
    try:
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('always')
            parse_start = time.perf_counter()
            if args.library == 'pypdf':
                from pypdf import PdfReader
                document = PdfReader(source, strict=False)
                if document.is_encrypted:
                    summary['encrypted'] = True
                    summary['status'] = 'rejected_encrypted_without_decryption'
                    return finish(summary, pages, destination, log_capture.events, caught, errors, started, parse_elapsed, extraction_elapsed)
                summary['encrypted'] = False
            else:
                import pdfplumber
                document = pdfplumber.open(source)
            raw_pages = document.pages
            page_count = len(raw_pages)
            parse_elapsed = time.perf_counter() - parse_start
            for index, page in enumerate(raw_pages, 1):
                record = {'physical_page': index, 'plain': '', 'layout': '', 'errors': []}
                for mode in ('plain', 'layout'):
                    extraction_start = time.perf_counter()
                    try:
                        if args.library == 'pypdf':
                            value = page.extract_text() if mode == 'plain' else page.extract_text(extraction_mode='layout')
                        else:
                            value = page.extract_text(layout=(mode == 'layout'))
                        record[mode] = value or ''
                    except Exception as exc:
                        record['errors'].append({'operation': mode, **sanitized_error(exc)})
                    extraction_elapsed[mode] += time.perf_counter() - extraction_start
                    (destination / mode / f'page-{index:03d}.txt').write_text(record[mode], encoding='utf-8')
                try:
                    record['image_count'] = len(page.images)
                except Exception as exc:
                    record['image_count'] = None
                    record['errors'].append({'operation': 'image_count', **sanitized_error(exc)})
                if args.library == 'pdfplumber':
                    record['char_objects'] = len(page.chars)
                    record['line_objects'] = len(page.lines)
                    record['rect_objects'] = len(page.rects)
                    table_start = time.perf_counter()
                    try:
                        record['tables'] = page.extract_tables()
                        record['table_metrics'] = {
                            'detected_tables': len(record['tables']),
                            'rows': [len(table) for table in record['tables']],
                            'max_columns': [max((len(row) for row in table), default=0) for table in record['tables']],
                        }
                    except Exception as exc:
                        record['tables'] = []
                        record['table_metrics'] = {'detected_tables': None}
                        record['errors'].append({'operation': 'extract_tables', **sanitized_error(exc)})
                    extraction_elapsed['tables'] += time.perf_counter() - table_start
                record['plain_metrics'] = text_metrics(record['plain'])
                record['layout_metrics'] = text_metrics(record['layout'])
                pages.append(record)
                if args.library == 'pdfplumber':
                    page.close()
            summary['physical_page_count'] = page_count
            summary['status'] = 'extracted_with_page_errors' if any(p['errors'] for p in pages) else 'extracted'
    except Exception as exc:
        errors.append(sanitized_error(exc))
        summary['status'] = 'failed'
    finally:
        if document is not None and hasattr(document, 'close'):
            try:
                document.close()
            except Exception as exc:
                errors.append({'operation': 'close', **sanitized_error(exc)})
        log.handlers, log.propagate = old_handlers, old_propagate
    return finish(summary, pages, destination, log_capture.events, caught, errors, started, parse_elapsed, extraction_elapsed)


def finish(summary, pages, destination, diagnostics, caught, errors, started, parse_elapsed, extraction_elapsed):
    private = {'document': summary['document'], 'library': summary['library'], 'pages': pages}
    write_json(destination / 'pages.json', private)
    plain_pages = [p['plain'] for p in pages]
    location_summary, location_private = citation_probes(plain_pages) if pages else ({}, {'samples': []})
    write_json(destination / 'citation-samples.json', location_private)
    summary.update({
        'parse_seconds': parse_elapsed,
        'extract_seconds': extraction_elapsed,
        'total_seconds': time.perf_counter() - started,
        'peak_process_rss_bytes': peak_rss_bytes(),
        'page_positions': [p['physical_page'] for p in pages],
        'nonempty_plain_pages': sum(bool(p['plain'].strip()) for p in pages),
        'nonempty_layout_pages': sum(bool(p['layout'].strip()) for p in pages),
        'plain_chars': sum(len(p['plain']) for p in pages),
        'layout_chars': sum(len(p['layout']) for p in pages),
        'plain_words': sum(len(p['plain'].split()) for p in pages),
        'replacement_chars': sum(p['plain_metrics']['replacement_chars'] for p in pages),
        'unexpected_controls': sum(p['plain_metrics']['unexpected_controls'] for p in pages),
        'pages_with_images': [p['physical_page'] for p in pages if p['image_count']],
        'total_image_objects': sum(p['image_count'] or 0 for p in pages),
        'page_metrics': [{key: value for key, value in p.items() if key not in ('plain', 'layout', 'tables')} for p in pages],
        'location_probes': location_summary,
        'diagnostics': diagnostics,
        'python_warnings': [{'category': w.category.__name__, 'message_sha256': digest(str(w.message))} for w in caught],
        'document_errors': errors,
    })
    write_json(destination / 'summary.json', summary)
    print(json.dumps({k: summary.get(k) for k in ('document', 'library', 'library_version', 'status', 'physical_page_count', 'nonempty_plain_pages', 'plain_chars', 'total_seconds', 'peak_process_rss_bytes')}, ensure_ascii=False))
    return 1 if summary.get('status') == 'failed' else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--library', choices=('pypdf', 'pdfplumber'), required=True)
    parser.add_argument('--input-dir', type=Path, default=DEFAULT_INPUT)
    parser.add_argument('--output-dir', type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument('--documents', nargs='+', default=['T1', 'T2', 'T3'])
    parser.add_argument('--timeout', type=float, default=120)
    parser.add_argument('--document', help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.document:
        return probe_document(args)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    summaries = []
    failed = False
    for document in args.documents:
        command = [sys.executable, str(Path(__file__).resolve()), '--library', args.library, '--input-dir', str(args.input_dir), '--output-dir', str(args.output_dir), '--document', document]
        try:
            completed = subprocess.run(command, text=True, capture_output=True, timeout=args.timeout)
            if completed.stdout:
                print(completed.stdout.strip())
            if completed.stderr:
                print(json.dumps({'document': document, 'stderr_sha256': digest(completed.stderr), 'stderr_lines': len(completed.stderr.splitlines())}))
            failed = failed or completed.returncode != 0
            path = args.output_dir / args.library / document / 'summary.json'
            if path.exists():
                summaries.append(json.loads(path.read_text()))
        except subprocess.TimeoutExpired:
            failed = True
            summary = {'document': document, 'library': args.library, 'status': 'timeout', 'timeout_seconds': args.timeout}
            summaries.append(summary)
            print(json.dumps(summary))
    write_json(args.output_dir / args.library / 'summary-all.json', {'scope': 'local parser feasibility; not production or semantic verification', 'documents': summaries})
    return int(failed)


if __name__ == '__main__':
    raise SystemExit(main())
