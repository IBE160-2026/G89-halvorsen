# AI Study Buddy — browser concept preview

From the project root, run:

```sh
python3 _bmad-output/planning-artifacts/ux-designs/ux-G89-halvorsen-2026-11-14/.working/browser-preview/serve_preview.py
```

Open the local URL printed by the server. It normally uses `http://127.0.0.1:8765/`; if that port is occupied, it selects another free local port. Stop it with Ctrl+C.

The single menu inside the app exposes Home, Summary, Flashcards and Quiz using saved example content. Together these screens are the selected concept, confirmed on 19 November 2026; minor refinements remain possible and UX is still in progress. Home shows the startup screen for inspection and preserves example practice state; it does not represent Clear or New session. PDF selection is a visual interaction; the preview does not process PDF content or call an AI service. Real study sessions remain governed by the PRD.

The editable source is `../study-preview.html`. `index.html` is its standalone browser rendering. Existing PRD requirements remain authoritative.

The current `index.html` continues the original grey Home, with the shared green/yellow/blue logo, upload cloud in the logo's exact golden yellow `#e0ae26` and dark-grey PDF arrow `#343a40`. Summary, Flashcards and Quiz retain their selected green/yellow/blue pastel canvases and existing interactions. The earlier neutral Round 7 concept is archived at `neutral-home-round-7.html`.

The independent warm cream Home concept remains available at `home-warm-cream.html`; `home-comparison.html` preserves the earlier comparison between Round 7 and the warm concept. These are historical alternatives, not the selected default. The warm alternative changes Home only and retains its original learning screens. Its editable source is `../home-warm-cream.html`, with Home-only colour overrides in `../home-warm-cream.css`; the comparison source is `../home-colour-comparison.html`. Only preview terminology is refreshed; their visual treatments and behaviour are retained. See the [UX artifact guide](../../README.md) for current/historical roles and remaining UX work.
