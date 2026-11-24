#!/usr/bin/env python3
"""Build a synthetic reliability review from the frozen pre-adoption Round 19.

This helper never changes the selected main or the approved Round 19 sketches.
"""
from pathlib import Path
import hashlib
import re

HERE = Path(__file__).resolve().parent


def once(source, old, new):
    assert source.count(old) == 1, f'Expected one insertion point: {old[:80]}'
    return source.replace(old, new, 1)


def part(source, name):
    match = re.search(rf'<!-- BEGIN {name} -->\n(.*?)\n<!-- END {name} -->', source, re.S)
    assert match, f'Missing literal part: {name}'
    return match.group(1)


def main():
    frozen = HERE / 'study-preview-round-19.html'
    frozen_bytes = frozen.read_bytes()
    source = frozen_bytes.decode('utf-8')
    parts = (HERE / 'reliability-parts.html').read_text()
    # Reuse the reviewed Round 19 status geometry and language hierarchy.
    styles = (HERE / 'processing-states-styles.css').read_text() + '\n' + (HERE / 'reliability-styles.css').read_text()
    logic = (HERE / 'reliability-logic.js').read_text()
    source = once(source, '  </style>', styles + '  </style>')
    source = once(source, '  <div class="app-frame">', part(parts, 'REVIEW_CONTROLS') + '\n  <div class="app-frame">')
    source = once(source, '        <section class="learning-view" id="preview-summary"', part(parts, 'DEMO_NOTICE') + '\n' + part(parts, 'STATUS_CARD') + '\n        <section class="learning-view" id="preview-summary"')
    source = once(source, '          <article class="summary-copy"', part(parts, 'SUMMARY_NOTICE') + '\n          <article class="summary-copy"')
    source = once(source, '            <p class="item-count" data-card-count', part(parts, 'CARDS_NOTICE') + '\n            <p class="item-count" data-card-count')
    source = once(source, '            <p class="item-count">Question 1 of 1', part(parts, 'QUIZ_NOTICE') + '\n            <p class="item-count">Question 1 of 1')
    source = once(source, '      render();\n      restorePresentation', logic + '\n\n      render();\n      restorePresentation')
    source = once(source, '      restorePresentation(window.openai?.widgetState?.privateContent);\n', '')
    source = once(source, "      window.addEventListener('openai:set_globals', event => restorePresentation(event.detail?.globals?.widgetState?.privateContent));\n", '')
    source = once(source, "const result = window.openai?.setWidgetState?.({ privateContent: { kind: 'study-preview-presentation', screen: state.view, origin: presentationOrigin }, modelContent: null });\n        result?.catch?.(() => {});", '// Reliability review does not read or write host presentation state.')
    source = once(source, 'Selected concept preview for AI Study Buddy', 'Reliability concept review for AI Study Buddy')
    source = once(source, 'Concept preview · sample content · no PDF processing or AI calls', 'Reliability concept review · synthetic fixtures · no PDF processing or AI calls')
    source = once(source, '  </style>', (HERE / 'mobile-study-alignment.css').read_text() + '  </style>')
    # Keep new review IDs stable; namespace the inherited product fragment IDs.
    ids = sorted(set(re.findall(r'\bid="([^"]+)"', source)), key=len, reverse=True)
    mapping = {}
    for index, old in enumerate(ids):
        if old.startswith('reliability-'):
            continue
        marker = f'__RELIABILITY_ID_{index}__'
        mapping[marker] = 'reliability-preview' if old == 'study-preview' else f'reliability-{old}'
        source = source.replace(old, marker)
    for marker, new in mapping.items():
        source = source.replace(marker, new)
    source = source.replace('study-preview-app', 'reliability-preview-app')
    source = source.replace('status-pending-turn', 'reliability-pending-turn')
    source = source.replace('preview-quiz-answer', 'reliability-quiz-answer')
    (HERE / 'reliability-review.html').write_text(source)
    assert frozen.read_bytes() == frozen_bytes, 'Frozen Round 19 changed during build'
    print('Built reliability-review.html from frozen Round 19')
    print(f'Frozen base SHA-256: {hashlib.sha256(frozen_bytes).hexdigest()}')


if __name__ == '__main__':
    main()
