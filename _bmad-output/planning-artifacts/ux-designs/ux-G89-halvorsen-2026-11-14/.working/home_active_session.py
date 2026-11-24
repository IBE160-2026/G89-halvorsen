"""Shared authoring transform for the selected Home state and earlier concept."""


def replace_once(source, old, new):
    if source.count(old) != 1:
        raise ValueError(f'Expected one insertion anchor: {old[:70]}')
    return source.replace(old, new, 1)


def integrate_home(source, folder, *, example=False):
    parts = (folder / 'home-active-session-parts.html').read_text()
    styles = (folder / 'home-active-session-styles.css').read_text()
    logic = (folder / 'home-active-session-logic.js').read_text()
    source = replace_once(source, '</form>\n        </section>', '</form>\n' + parts + '        </section>')
    source = replace_once(source, '  </style>', styles + '  </style>')
    if example:
        source = replace_once(source, "file: null, active: false, selectedName: '', card: 0", "file: { name: 'Studieteknikk.pdf', pdf: true, example: true }, active: true, selectedName: 'Studieteknikk.pdf', card: 0")
        source = replace_once(source, "      render();\n      restorePresentation(window.openai?.widgetState?.privateContent);\n      window.addEventListener('openai:set_globals', event => restorePresentation(event.detail?.globals?.widgetState?.privateContent));", logic + '\n      render();')
    else:
        logic = replace_once(logic, '      // Independent, prewritten fixture. No PDF content or real study session is restored.', '      // Selected Home state; session choices and practice remain in memory only.')
        logic = replace_once(logic, '      // Keep this concept isolated from presentation state belonging to the chosen concept.\n      savePresentation = () => {};\n', '')
        logic = replace_once(logic, "      languageInput.value = 'nb';\n      levelInput.value = 'detailed';\n      acknowledgement.checked = true;\n", '')
        source = replace_once(source, '      render();\n      restorePresentation', logic + '\n      render();\n      restorePresentation')
    return source
