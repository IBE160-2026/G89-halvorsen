#!/usr/bin/env python3
"""Build an isolated learning-flow UX review from frozen Round 19.

Only adjacent learning-flows-* outputs are written. All passages are authored
synthetic examples; no PDF, API, persistent browser state or production code.
"""
from pathlib import Path
import hashlib
import re

HERE = Path(__file__).resolve().parent


def once(source, old, new):
    assert source.count(old) == 1, f'Expected exactly one insertion point: {old[:90]}'
    return source.replace(old, new, 1)


def between(source, start, end, replacement):
    assert source.count(start) == 1 and source.count(end) == 1
    first, last = source.index(start), source.index(end)
    assert first < last
    return source[:first] + replacement + source[last:]


def part(parts, name):
    match = re.search(rf'<!-- BEGIN {name} -->\n(.*?)\n<!-- END {name} -->', parts, re.S)
    assert match, name
    return match.group(1)


def namespace(source):
    ids = set(re.findall(r'\bid="([^"]+)"', source))
    replacements = {}
    for index, old in enumerate(sorted(ids, key=len, reverse=True)):
        placeholder = f'__LEARNING_ID_{index}__'
        replacements[placeholder] = 'learning-flows-preview' if old == 'study-preview' else f'learning-{old}'
        source = source.replace(old, placeholder)
    for placeholder, new in replacements.items():
        source = source.replace(placeholder, new)
    return source


def main():
    frozen = HERE / 'study-preview-round-19.html'
    frozen_bytes = frozen.read_bytes()
    source = frozen_bytes.decode()
    parts = (HERE / 'learning-flows-parts.html').read_text()
    source = once(source, '  </style>', (HERE / 'learning-flows-styles.css').read_text() + '  </style>')
    source = once(source, 'Selected concept preview for AI Study Buddy', 'Learning-flow review concept for AI Study Buddy')
    source = once(source, '  <div class="app-frame">', '  <p class="learning-review-note">Learning-flow concept for review · 8 sample questions and 3 sample cards, not product limits. All content and source passages are synthetic. No PDF processing or AI calls. Choose the sample PDF and session settings to begin.</p>\n  <div class="app-frame">')
    source = once(source, '              <p class="selected-file"', '              <button class="source-link sample-file-action cursor-interaction" type="button" data-use-learning-sample>Use synthetic sample PDF</button>\n              <p class="selected-file"')
    source = once(source, '<span>Generate Summary</span>', '<span>Open sample Summary</span>')
    source = once(source, '<div class="summary-sources"><button class="source-link cursor-interaction" type="button" data-source="summary" aria-controls="study-source-panel" aria-expanded="false">Source · page 2</button><button class="source-link cursor-interaction" type="button" data-source="summary-repetition" aria-controls="study-source-panel" aria-expanded="false">Source · page 3</button></div>', '<div class="summary-sources"><button class="source-link cursor-interaction" type="button" data-source="summary" aria-controls="study-source-panel" aria-expanded="false">View sources · recall and checking</button><button class="source-link cursor-interaction" type="button" data-source="summary-repetition" aria-controls="study-source-panel" aria-expanded="false">View sources · further study</button></div>')
    source = between(source, '        <section class="learning-view" id="preview-flashcards"', '      </main>', part(parts, 'FLASHCARDS') + '\n' + part(parts, 'QUIZ') + '\n')
    source = between(source, '      <aside class="source-panel"', '      <div class="session-modal-layer"', part(parts, 'SOURCES') + '\n')
    source = once(source, '      function appendText(parent, tag, text)', (HERE / 'learning-flows-data.js').read_text() + '\n' + (HERE / 'learning-flows-logic.js').read_text() + '\n      function appendText(parent, tag, text)')
    source = between(source, '      function sourceItem() {', '      function render() {', '')
    source = between(source, '        const card = text.cards[state.card];', '        renderForm();', '        renderCards();\n        renderQuiz();\n        renderLearningSources();\n')
    source = once(source, "if (view === 'flashcards' && state.view !== view) state.flipped = false;", "if (view === 'flashcards' && state.view !== view) { state.flipped = false; state.cardComplete = false; }")
    source = once(source, "        state.card = 0; state.flipped = false; state.answer = null; state.confirmed = false; state.ready = { summary: true, flashcards: false, quiz: false };", "        resetLearningFlows();\n        state.card = 0; state.flipped = false; state.answer = null; state.confirmed = false; state.ready = { summary: true, flashcards: false, quiz: false };")
    source = between(source, "      root.addEventListener('click', event => {\n        const button = event.target.closest('button'); if (!button", '      let exampleEnded = false;', (HERE / 'learning-flows-events.js').read_text() + '\n')
    source = once(source, '        exampleEnded = true;', '        exampleEnded = true;\n        resetLearningFlows();')
    source = once(source, "          root.querySelector('[data-excerpt]').textContent = '';", "          root.querySelector('[data-source-reference-list]').replaceChildren();")
    source = between(source, "        if (!state.active && view !== 'startup') {", '        closeSessionPopup();\n        sessionBaseSetView(view, false);', "        if (!state.active && view !== 'startup') return; // Startup fixes the session language/detail.\n")
    source = once(source, "button.disabled = button.dataset.preview !== 'startup' && exampleEnded && !state.active", "button.disabled = button.dataset.preview !== 'startup' && !state.active")
    source = once(source, "root.querySelector('.sample-note').textContent = 'Saved example content · no PDF processing or AI calls.';", "root.querySelector('.sample-note').textContent = 'Synthetic saved samples · 8 quiz questions and 3 cards are illustrative, not limits · no PDF processing or AI calls.';")
    source = once(source, "root.querySelector('.active-session-example').textContent = 'Saved example content · no PDF processing';", "root.querySelector('.active-session-example').textContent = 'Synthetic saved sample · no PDF processing';")
    source = once(source, 'Concept preview · sample content · no PDF processing or AI calls', 'Learning-flow review concept · synthetic sample content · no PDF processing or AI calls')
    source = once(source, "        const result = window.openai?.setWidgetState?.({ privateContent: { kind: 'study-preview-presentation', screen: state.view, origin: presentationOrigin }, modelContent: null });\n        result?.catch?.(() => {});", '        // Isolated review: no persistent browser or host state is written.')
    source = once(source, '      restorePresentation(window.openai?.widgetState?.privateContent);\n', '')
    source = once(source, "      window.addEventListener('openai:set_globals', event => restorePresentation(event.detail?.globals?.widgetState?.privateContent));\n", '')
    source = once(source, '  </style>', (HERE / 'mobile-study-alignment.css').read_text() + '  </style>')
    source = namespace(source)
    review = once((HERE / 'learning-flows-shell.html').read_text(), '<!-- LEARNING_FLOW_FRAGMENT -->', source)
    destination = HERE / 'learning-flows-review.html'
    destination.write_text(review)
    assert frozen.read_bytes() == frozen_bytes, 'Frozen Round 19 changed during build'
    print(f'Built {destination.name}; frozen SHA-256 {hashlib.sha256(frozen_bytes).hexdigest()}')


if __name__ == '__main__':
    main()
