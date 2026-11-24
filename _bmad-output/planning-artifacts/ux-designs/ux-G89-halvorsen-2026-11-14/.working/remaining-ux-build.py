"""Assemble separate UX reviews without changing their interaction state."""
from pathlib import Path

folder = Path(__file__).resolve().parent
source = (folder / 'remaining-ux-review-shell.html').read_text()
for marker, name in [
    ('RELIABILITY_REVIEW', 'reliability-review.html'),
    ('LEARNING_FLOWS_REVIEW', 'learning-flows-review.html'),
    ('SELECTED_STATUS_REVIEW', 'study-preview-status-r20.html'),
]:
    anchor = f'<!-- {marker} -->'
    assert source.count(anchor) == 1
    source = source.replace(anchor, (folder / name).read_text())
(folder / 'remaining-ux-review.html').write_text(source)
print('Built remaining-ux-review.html')
