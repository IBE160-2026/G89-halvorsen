#!/usr/bin/env python3
"""Promote the selected visible New session control onto the frozen Home baseline."""
from pathlib import Path
import re
from home_active_session import integrate_home
from selected_statuses import integrate_statuses


def replace_once(source, old, new):
    assert source.count(old) == 1, f"Expected one occurrence: {old[:80]}"
    return source.replace(old, new, 1)


def main():
    folder = Path(__file__).resolve().parent
    source = (folder / "study-preview-round-11.html").read_text()
    styles = (folder / "session-actions-styles.css").read_text()
    logic = (folder / "session-actions-logic.js").read_text()
    document = (folder / "session-actions-document.html").read_text()
    actions = (folder / "session-actions-buttons.html").read_text()
    dialog = (folder / "session-actions-dialog.html").read_text()

    # Keep all original markup/styles/IDs except the chosen document-context control.
    document = document.replace("Norwegian Bokmål · Brief · sample content", "Norwegian Bokmål · Detailed · sample content")
    source, count = re.subn(r'^        <div class="doc-context" hidden>.*?</div>$', lambda _: document.replace("<!-- SESSION_ACTIONS -->", actions.strip()), source, flags=re.M)
    assert count == 1
    source = replace_once(source, "  </style>", styles + "  </style>")
    aside_end = source.index("</aside>") + len("</aside>")
    source = source[:aside_end] + "\n" + dialog + source[aside_end:]

    # Main starts on the original empty Home. Initial learning navigation may
    # activate prewritten examples, but ended examples must never reappear.
    logic = "      let exampleEnded = false;\n" + logic
    logic = replace_once(logic, "        state.active = false;", "        exampleEnded = true;\n        state.active = false;")
    logic = replace_once(logic,
        "button.disabled = button.dataset.preview !== 'startup' && !state.active",
        "button.disabled = button.dataset.preview !== 'startup' && exampleEnded && !state.active")
    logic = replace_once(logic,
        "      setView = (view) => {\n        if (!state.active && view !== 'startup') return;\n        closeSessionPopup();\n        sessionBaseSetView(view, false);\n      };",
        """      setView = (view, direct = false) => {
        if (!screens.has(view)) return;
        if (!state.active && view !== 'startup') {
          if (exampleEnded || !direct) return;
          state.active = true;
          state.file = { name: 'Studieteknikk.pdf', pdf: true, example: true };
          state.selectedName = 'Studieteknikk.pdf';
          state.language = 'nb';
          state.level = 'detailed';
          state.ready = { summary: true, flashcards: true, quiz: true };
          languageInput.value = 'nb';
          levelInput.value = 'detailed';
          acknowledgement.checked = true;
        }
        closeSessionPopup();
        sessionBaseSetView(view, false);
      };""")
    logic = replace_once(logic, "      savePresentation = () => {};\n", "")
    logic = replace_once(logic,
        "      languageInput.value = 'nb';\n      levelInput.value = 'brief';\n      acknowledgement.checked = true;\n",
        "")
    logic = replace_once(logic,
        "        render();\n        root.querySelector('[data-choose-pdf]').focus({ preventScroll: true });",
        "        render();\n        savePresentation();\n        root.querySelector('[data-choose-pdf]').focus({ preventScroll: true });")
    first_render = source.rindex("      render();\n      restorePresentation")
    source = source[:first_render] + logic + "\n" + source[first_render:]
    # Fresh chat-review entry: same selected concept, with an independent
    # presentation-state key and Summary open so the chosen control is visible.
    review = source.replace("study-preview-presentation", "visible-button-review-r15")
    review = replace_once(review,
        "      render();\n      restorePresentation(window.openai?.widgetState?.privateContent);",
        "      render();\n      setView('summary', true);\n      restorePresentation(window.openai?.widgetState?.privateContent);")
    review = replace_once(review,
        '<div id="study-preview" lang="en"',
        '<div id="study-preview" data-preview-revision="visible-button-r15" lang="en"')
    (folder / "study-preview-visible-button-r15.html").write_text(review)
    print(folder / "study-preview-visible-button-r15.html")

    # Adopt the reviewed Home state, retaining the original empty entry point.
    source = integrate_home(source, folder)

    # Fresh review starts the labelled example on active Home. It does not
    # change the main entry point or persist any PDF/session content.
    selected = source.replace('study-preview', 'study-active-home-r18')
    selected = replace_once(selected,
        '      render();\n      restorePresentation(window.openai?.widgetState?.privateContent);',
        "      render();\n      setView('summary', true);\n      setView('startup');\n      restorePresentation(window.openai?.widgetState?.privateContent);")
    shell = (folder / 'home-active-session-shell.html').read_text()
    shell = shell.replace('active-home-review', 'active-home-review-r18')
    selected = replace_once(shell, '<!-- ACTIVE_HOME_CONCEPT -->', selected)
    (folder / 'study-preview-active-home-r18.html').write_text(selected)
    print(folder / 'study-preview-active-home-r18.html')

    source = integrate_statuses(source, folder)
    source = replace_once(source, '  </style>', (folder / 'mobile-study-alignment.css').read_text() + '  </style>')
    (folder / 'study-preview.html').write_text(source)
    print(folder / 'study-preview.html')
    review = source.replace('study-preview', 'study-selected-status-r20')
    shell = (folder / 'selected-status-review-shell.html').read_text()
    assert shell.count('<!-- SELECTED_STATUS_APP -->') == 1
    (folder / 'study-preview-status-r20.html').write_text(shell.replace('<!-- SELECTED_STATUS_APP -->', review))


if __name__ == "__main__":
    main()
