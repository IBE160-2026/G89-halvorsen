"""Insert the selected status patterns into the UX main; no backend operation."""
import re


def integrate_statuses(source, folder):
    parts = (folder / 'processing-states-parts.html').read_text()
    card = re.search(r'<!-- BEGIN STATUS_CARD -->\n(.*?)\n<!-- END STATUS_CARD -->', parts, re.S).group(1)
    styles = (folder / 'processing-states-styles.css').read_text()
    logic = (folder / 'selected-status-logic.js').read_text()
    for anchor, replacement in [
        ('  </style>', styles + '  </style>'),
        ('        <section class="learning-view" id="preview-summary"', card + '\n        <section class="learning-view" id="preview-summary"'),
        ('      render();\n      restorePresentation', logic + '\n      render();\n      restorePresentation'),
    ]:
        assert source.count(anchor) == 1, anchor
        source = source.replace(anchor, replacement, 1)
    return source
