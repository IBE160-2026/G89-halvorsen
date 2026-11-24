#!/usr/bin/env python3
"""Build isolated status sketches from the selected, unmodified UX prototype.

Literal markup, CSS and JavaScript live in adjacent source files. These are
presentation-only fixtures; the selected prototype and its builders stay intact.
"""
from pathlib import Path
import hashlib
import re

HERE = Path(__file__).resolve().parent


def replace_once(source, old, new):
    assert source.count(old) == 1, f'Expected one insertion point: {old[:80]}'
    return source.replace(old, new, 1)


def part(source, name):
    found = re.search(rf'<!-- BEGIN {name} -->\n(.*?)\n<!-- END {name} -->', source, re.S)
    assert found, f'Missing literal part: {name}'
    return found.group(1)


def namespace(source, concept):
    root = f'status-{concept}-preview'
    ids = set(re.findall(r'\bid="([^"]+)"', source))
    replacements = {}
    for index, old in enumerate(sorted(ids, key=len, reverse=True)):
        placeholder = f'__STATUS_ID_{index}__'
        replacements[placeholder] = root if old == 'study-preview' else f'{concept}-{old}'
        source = source.replace(old, placeholder)
    for placeholder, new in replacements.items():
        source = source.replace(placeholder, new)
    source = source.replace('name="preview-quiz-answer"', f'name="{concept}-preview-quiz-answer"')
    source = source.replace('name="preview-quiz-answer"]', f'name="{concept}-preview-quiz-answer"]')
    # Container and keyframe names must also be independent when embedded together.
    source = source.replace('study-preview-app', f'status-{concept}-app')
    source = source.replace('status-pending-turn', f'status-{concept}-pending-turn')
    return replace_once(source, f'<div id="{root}" lang="en"', f'<div id="{root}" data-concept="status-{concept}" data-status-concept="{concept}" lang="en"')


def main():
    chosen = HERE / 'study-preview-round-19.html'
    chosen_bytes = chosen.read_bytes()
    base = chosen_bytes.decode('utf-8')
    parts = (HERE / 'processing-states-parts.html').read_text()
    styles = (HERE / 'processing-states-styles.css').read_text()
    logic = (HERE / 'processing-states-logic.js').read_text()
    initial = "view: 'startup', language: 'nb', level: 'detailed', file: null, active: false, selectedName: ''"
    all_ready = 'ready: { summary: true, flashcards: true, quiz: true }'
    fragments = {}
    for concept in ('loading', 'pdf-problem', 'ai-error'):
        source = base
        view = 'flashcards' if concept == 'ai-error' else 'startup' if concept == 'pdf-problem' else 'summary'
        filename = 'Forelesningsnotater.pdf' if concept == 'pdf-problem' else 'Studieteknikk.pdf'
        fixture = f"view: '{view}', language: 'nb', level: 'detailed', file: {{ name: '{filename}', pdf: true, example: true }}, active: true, selectedName: '{filename}'"
        source = replace_once(source, initial, fixture)
        source = replace_once(source, all_ready, 'ready: { summary: ' + ('true' if concept == 'ai-error' else 'false') + ', flashcards: false, quiz: false }')
        source = replace_once(source, '  </style>', styles + '  </style>')
        source = replace_once(source, '        <section class="learning-view" id="preview-summary"', part(parts, 'STATUS_CARD') + '\n        <section class="learning-view" id="preview-summary"')
        if concept == 'loading':
            source = replace_once(source, '  <p class="text-small text-muted preview-note">', part(parts, 'LOADING_CONTROLS') + '\n  <p class="text-small text-muted preview-note">')
        source = replace_once(source, '      render();\n      restorePresentation', logic + '\n\n      render();\n      restorePresentation')
        source = replace_once(source, '      restorePresentation(window.openai?.widgetState?.privateContent);\n', '')
        source = replace_once(source, "      window.addEventListener('openai:set_globals', event => restorePresentation(event.detail?.globals?.widgetState?.privateContent));\n", '')
        source = replace_once(source, "const result = window.openai?.setWidgetState?.({ privateContent: { kind: 'study-preview-presentation', screen: state.view, origin: presentationOrigin }, modelContent: null });\n        result?.catch?.(() => {});", '// Isolated status concept; no host presentation state is written.')
        source = replace_once(source, 'Selected concept preview for AI Study Buddy', f'{concept.replace("-", " ").capitalize()} state concept for AI Study Buddy')
        source = replace_once(source, 'Concept preview · sample content · no PDF processing or AI calls', 'Synthetic status sketch · no PDF processing or AI calls')
        source = namespace(source, concept)
        fragments[concept] = source
        destination = HERE / f'status-{concept}.html'
        destination.write_text(source)
        print(f'Built {destination.name}')
    shell_path = HERE / 'processing-states-comparison-shell.html'
    if shell_path.exists():
        comparison = shell_path.read_text()
        for marker, concept in (('STATUS_LOADING_FRAGMENT', 'loading'), ('STATUS_PDF_FRAGMENT', 'pdf-problem'), ('STATUS_AI_FRAGMENT', 'ai-error')):
            comparison = replace_once(comparison, f'<!-- {marker} -->', fragments[concept])
        (HERE / 'processing-states-comparison.html').write_text(comparison)
        print('Built processing-states-comparison.html')
    assert chosen.read_bytes() == chosen_bytes, 'The selected prototype changed during build'
    print(f'Selected prototype unchanged; SHA-256 {hashlib.sha256(chosen_bytes).hexdigest()}')


if __name__ == '__main__':
    main()
