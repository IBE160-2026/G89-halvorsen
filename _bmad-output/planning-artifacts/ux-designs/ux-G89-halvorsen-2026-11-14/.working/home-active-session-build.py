"""Build only the separate Home-with-active-session concept from the chosen source.

The shared source and its builders/exports remain unchanged. Literal new markup,
styles and logic live in adjacent reviewable helper files.
"""
from pathlib import Path
import hashlib
from home_active_session import integrate_home, replace_once

HERE = Path(__file__).resolve().parent
source_path = HERE / 'study-preview-round-17.html'
source_bytes = source_path.read_bytes()
source = source_bytes.decode('utf-8')
source = integrate_home(source, HERE, example=True)
source = replace_once(source, 'aria-label="Selected concept preview for AI Study Buddy"', 'aria-label="Home with active session concept for AI Study Buddy" data-home-concept="pending-review"')
source = source.replace('study-preview', 'home-active-preview')
destination = HERE / 'home-active-session.html'
destination.write_text(source)
shell = (HERE / 'home-active-session-shell.html').read_text()
review = replace_once(shell, '<!-- ACTIVE_HOME_CONCEPT -->', source)
(HERE / 'home-active-session-review.html').write_text(review)
(HERE / 'home-active-session-buttons-review.html').write_text(review)
assert source_path.read_bytes() == source_bytes, 'Chosen source was unexpectedly changed'
print(f'Built {destination.name} ({len(source.encode())} bytes); chosen source unchanged; SHA-256 {hashlib.sha256(source_bytes).hexdigest()}')
