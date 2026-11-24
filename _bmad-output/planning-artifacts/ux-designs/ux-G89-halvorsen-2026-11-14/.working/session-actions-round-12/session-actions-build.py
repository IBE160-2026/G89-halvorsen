#!/usr/bin/env python3
"""Derive two isolated UX concepts from the unchanged selected prototype."""
from pathlib import Path
import re


def main():
    folder = Path(__file__).resolve().parent
    base = (folder / "study-preview.html").read_text()
    styles = (folder / "session-actions-styles.css").read_text()
    logic = (folder / "session-actions-logic.js").read_text()
    document = (folder / "session-actions-document.html").read_text()
    dialog = (folder / "session-actions-dialog.html").read_text()
    for concept in ("menu", "buttons"):
        source = base
        actions = (folder / f"session-actions-{concept}.html").read_text()
        source, count = re.subn(r'^        <div class="doc-context" hidden>.*?</div>$', lambda _: document.replace("<!-- SESSION_ACTIONS -->", actions.strip()), source, flags=re.M)
        assert count == 1
        source = source.replace("  </style>", styles + "  </style>", 1)
        aside_end = source.index("</aside>") + len("</aside>")
        source = source[:aside_end] + "\n" + dialog + source[aside_end:]
        initial = "view: 'startup', language: 'nb', level: 'detailed', file: null, active: false, selectedName: ''"
        replacement = "view: 'summary', language: 'nb', level: 'brief', file: { name: 'Studieteknikk.pdf', pdf: true, example: true }, active: true, selectedName: 'Studieteknikk.pdf'"
        assert source.count(initial) == 1
        source = source.replace(initial, replacement, 1)
        first_render = source.rindex("      render();\n      restorePresentation")
        source = source[:first_render] + logic + "\n" + source[first_render:]
        source = source.replace("      restorePresentation(window.openai?.widgetState?.privateContent);\n", "")
        source = source.replace("      window.addEventListener('openai:set_globals', event => restorePresentation(event.detail?.globals?.widgetState?.privateContent));\n", "")
        # The cloned examples deliberately keep independent in-memory state.
        source = source.replace("const result = window.openai?.setWidgetState?.({ privateContent: { kind: 'study-preview-presentation', screen: state.view, origin: presentationOrigin }, modelContent: null });\n        result?.catch?.(() => {});", "// Independent concept instance; no host state is written.")
        root = f"session-{concept}-preview"
        ids = set(re.findall(r'\bid="([^"]+)"', source))
        replacements = {}
        for index, old in enumerate(sorted(ids, key=len, reverse=True)):
            placeholder = f"__SESSION_ID_{index}__"
            replacements[placeholder] = root if old == "study-preview" else f"{concept}-{old}"
            source = source.replace(old, placeholder)
        for placeholder, new in replacements.items():
            source = source.replace(placeholder, new)
        source = source.replace('name="preview-quiz-answer"', f'name="{concept}-preview-quiz-answer"')
        source = source.replace('name="preview-quiz-answer"]', f'name="{concept}-preview-quiz-answer"]')
        source = source.replace(f'<div id="{root}" lang="en"', f'<div id="{root}" data-concept="{concept}" lang="en"', 1)
        source = source.replace("Selected concept preview for AI Study Buddy", f"Session {concept} concept for AI Study Buddy", 1)
        (folder / f"session-{concept}.html").write_text(source)
        print(folder / f"session-{concept}.html")
    comparison = (folder / "session-actions-comparison-shell.html").read_text()
    comparison = comparison.replace("<!-- SESSION_MENU_FRAGMENT -->", (folder / "session-menu.html").read_text())
    comparison = comparison.replace("<!-- SESSION_BUTTONS_FRAGMENT -->", (folder / "session-buttons.html").read_text())
    (folder / "session-actions-comparison.html").write_text(comparison)
    print(folder / "session-actions-comparison.html")


if __name__ == "__main__":
    main()
