#!/usr/bin/env python3
"""Generate owned local PDF fixtures and exercise parser/location boundaries.

The location matcher is a probe policy, not app implementation. All input/output
content is generated here and stays in /private/tmp. No decryption is attempted.
"""
from __future__ import annotations

import contextlib
import hashlib
import importlib.metadata
import io
import json
import logging
import platform
import unicodedata
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from pypdf import PdfReader, PdfWriter
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

from probe import location_match, normalized


ROOT = Path('/private/tmp/ai-study-buddy-pdf-probe/synthetic')
FONT_FILE = Path('/System/Library/Fonts/Supplemental/Arial.ttf')


def json_write(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def make_fixtures():
    ROOT.mkdir(parents=True, exist_ok=True)
    if not FONT_FILE.is_file():
        raise RuntimeError('A Unicode-capable local Arial.ttf is required for this probe')
    pdfmetrics.registerFont(TTFont('ProbeArial', str(FONT_FILE)))
    raster = Image.new('RGB', (1000, 280), 'white')
    draw = ImageDraw.Draw(raster)
    draw.text((30, 80), 'Raster only source 8391', fill='black', font=ImageFont.truetype(str(FONT_FILE), 58))
    raster.save(ROOT / 'image-only-source.png')

    c = canvas.Canvas(str(ROOT / 'numbering-blank-image.pdf'), pagesize=A4)
    c.setFont('ProbeArial', 16)
    c.drawString(60, 780, 'Unique physical one source')
    c.drawString(60, 55, 'Printed page iv')
    c.showPage()
    c.setFont('ProbeArial', 16)
    c.drawString(60, 780, 'Numbered page one on physical two')
    c.drawString(60, 55, 'Printed page 1')
    c.showPage()
    # Intentionally no visible objects on physical page 3.
    c.showPage()
    c.drawImage(ImageReader(raster), 45, 500, width=505, height=141)
    c.showPage()
    c.setFont('ProbeArial', 16)
    c.drawString(60, 780, 'After blank and image physical five')
    c.drawString(60, 55, 'Printed page 2')
    c.showPage()
    c.save()

    c = canvas.Canvas(str(ROOT / 'unicode-table.pdf'), pagesize=A4)
    c.setFont('ProbeArial', 16)
    lines = [
        'Nordic: æøå ÆØÅ; café; Ångström.',
        'Canonical: café / cafe\u0301',
        'Exact key: Alpha-Beta 42',
        'Whitespace: red    green',
        'blue',
    ]
    for index, line in enumerate(lines):
        c.drawString(60, 780 - index * 30, line)
    left, top, width, row_height, col_width = 60, 560, 360, 38, 220
    cells = [['Item', 'Value'], ['Alpha', '42'], ['Beta', '73']]
    c.setStrokeColor(colors.black)
    for row in range(4):
        y = top - row * row_height
        c.line(left, y, left + width, y)
    for x in (left, left + col_width, left + width):
        c.line(x, top, x, top - 3 * row_height)
    for row_index, row in enumerate(cells):
        for col_index, value in enumerate(row):
            c.drawString(left + (0 if col_index == 0 else col_width) + 10, top - 26 - row_index * row_height, value)
    c.showPage()
    c.save()

    # A deliberately password-required owned fixture; no opening password is
    # supplied to either parser during the checks below.
    writer = PdfWriter()
    writer.append(str(ROOT / 'unicode-table.pdf'))
    writer.encrypt(user_password='probe-password', owner_password='probe-owner', algorithm='RC4-128')
    with (ROOT / 'password-required.pdf').open('wb') as stream:
        writer.write(stream)
    writer.close()
    (ROOT / 'damaged.pdf').write_bytes(b'%PDF-1.7\nDeliberately incomplete probe file without xref/trailer/EOF.\n')


def check_library(library):
    result = {'library': library, 'version': importlib.metadata.version(library), 'checks': {}, 'private_outputs': True}
    checks = result['checks']
    out = ROOT / library
    out.mkdir(exist_ok=True)
    docs = {}
    table = None
    for filename in ('numbering-blank-image.pdf', 'unicode-table.pdf'):
        if library == 'pypdf':
            with PdfReader(ROOT / filename) as doc:
                pages = [page.extract_text() or '' for page in doc.pages]
                images = [len(page.images) for page in doc.pages]
        else:
            import pdfplumber
            with pdfplumber.open(ROOT / filename) as doc:
                pages = [page.extract_text() or '' for page in doc.pages]
                images = [len(page.images) for page in doc.pages]
                if filename == 'unicode-table.pdf':
                    table = doc.pages[0].extract_tables()
        docs[filename] = pages
        json_write(out / (filename + '.text.json'), {'pages': pages, 'images': images})
        if filename == 'numbering-blank-image.pdf':
            checks['physical_page_count_five'] = len(pages) == 5
            checks['physical_page_two_match'] = location_match(pages, 2, 'Numbered page one on physical two') is not None
            checks['printed_label_one_not_physical_one'] = location_match(pages, 1, 'Numbered page one on physical two') is None
            checks['blank_page_preserved_at_three'] = len(pages) >= 3 and not pages[2].strip() and images[2] == 0
            checks['image_only_preserved_at_four_without_ocr_text'] = len(pages) >= 4 and not pages[3].strip() and images[3] == 1
            checks['physical_page_five_after_gaps'] = location_match(pages, 5, 'After blank and image physical five') is not None
    pages = docs['unicode-table.pdf']
    checks['visible_nordic_text_preserved'] = location_match(pages, 1, 'Nordic: æøå ÆØÅ; café; Ångström.') is not None
    checks['canonical_unicode_equivalence'] = location_match(pages, 1, unicodedata.normalize('NFD', 'Nordic: æøå ÆØÅ; café; Ångström.')) is not None
    checks['canonical_line_preserved_under_nfc'] = normalized('Canonical: café / cafe\u0301') in normalized(pages[0])
    checks['whitespace_collapsing_match'] = location_match(pages, 1, 'Whitespace:\tred green\nblue') is not None
    checks['literal_case_number_hyphen_match'] = location_match(pages, 1, 'Exact key: Alpha-Beta 42') is not None
    for label, value in [('case', 'Exact key: alpha-Beta 42'), ('number', 'Exact key: Alpha-Beta 43'), ('removed_hyphen', 'Exact key: AlphaBeta 42'), ('changed_hyphen', 'Exact key: Alpha–Beta 42')]:
        checks[label + '_alteration_rejected'] = location_match(pages, 1, value) is None
    checks['native_table_cells_present'] = all(location_match(pages, 1, value) is not None for value in ('Item', 'Value', 'Alpha', '42', 'Beta', '73'))
    text = normalized(pages[0])
    checks['native_table_row_order_preserved_in_this_fixture'] = text.index('Item') < text.index('Value') < text.index('Alpha 42') < text.index('Beta 73') if 'Alpha 42' in text and 'Beta 73' in text else False
    if library == 'pdfplumber':
        expected = [['Item', 'Value'], ['Alpha', '42'], ['Beta', '73']]
        checks['native_table_structured_cells_match'] = expected in table
        json_write(out / 'native-table.json', table)

    with contextlib.redirect_stderr(io.StringIO()):
        if library == 'pypdf':
            doc = PdfReader(ROOT / 'password-required.pdf')
            # Policy checks encryption before any attempt to enumerate pages.
            checks['password_required_rejected_without_decryption'] = bool(doc.is_encrypted)
            result['password_rejection_mechanism'] = 'is_encrypted policy gate; no decrypt call'
            doc.close()
        else:
            import pdfplumber
            try:
                with pdfplumber.open(ROOT / 'password-required.pdf'):
                    checks['password_required_rejected_without_decryption'] = False
            except Exception as exc:
                result['password_exception'] = type(exc).__name__
                chain, seen, current = [], set(), exc
                while current is not None and id(current) not in seen:
                    seen.add(id(current))
                    chain.append(type(current).__name__)
                    current = current.__cause__ or current.__context__
                result['password_exception_chain'] = chain
                checks['password_required_rejected_without_decryption'] = 'PDFPasswordIncorrect' in chain
        try:
            if library == 'pypdf':
                doc = PdfReader(ROOT / 'damaged.pdf')
            else:
                import pdfplumber
                doc = pdfplumber.open(ROOT / 'damaged.pdf')
            try:
                len(doc.pages)
                checks['damaged_pdf_rejected'] = False
            finally:
                doc.close()
        except Exception as exc:
            checks['damaged_pdf_rejected'] = True
            result['damaged_exception'] = type(exc).__name__
    result['passed'] = sum(value is True for value in checks.values())
    result['total'] = len(checks)
    result['failed_checks'] = [key for key, value in checks.items() if value is not True]
    return result


def main():
    logging.getLogger('pypdf').addHandler(logging.NullHandler())
    logging.getLogger('pypdf').propagate = False
    if not all((ROOT / name).is_file() for name in ('numbering-blank-image.pdf', 'unicode-table.pdf', 'password-required.pdf', 'damaged.pdf')):
        make_fixtures()
    results = [check_library(library) for library in ('pypdf', 'pdfplumber')]
    summary = {
        'scope': 'owned synthetic fixtures and local parser/location checks; not app/security/semantic validation',
        'python': platform.python_version(),
        'versions': {name: importlib.metadata.version(name) for name in ('pypdf', 'pdfplumber', 'reportlab', 'pillow')},
        'font': FONT_FILE.name,
        'fixture_hashes': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(ROOT.glob('*.pdf'))},
        'libraries': results,
    }
    json_write(ROOT / 'summary.json', summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return int(any(r['failed_checks'] for r in results))


if __name__ == '__main__':
    raise SystemExit(main())
