# AI Study Buddy — browser concept preview

**UX planning complete, 24 November 2026.** The user-selected concept and full interaction references are documented in [DESIGN.md](../../DESIGN.md), [EXPERIENCE.md](../../EXPERIENCE.md) and [the final report](../../validation-report.md). Minor refinements remain possible. No production app, architecture work, commit or push is implied.

From the project root, run:

```sh
python3 _bmad-output/planning-artifacts/ux-designs/ux-G89-halvorsen-2026-11-14/.working/browser-preview/serve_preview.py
```

Open the printed local URL, normally `http://127.0.0.1:8765/`. If occupied, the server selects another port. Stop with Ctrl+C.

| Entry | Selected scope |
| --- | --- |
| [remaining-ux.html](remaining-ux.html) | Combined complete learning, reliability and processing references, with desktop/mobile inspection controls. |
| [index.html](index.html) | Illustrated empty/active Home and shared menu/basic sample. Its one-question Quiz is intentionally partial; use the complete flow for the full contract. |
| [learning-flows.html](learning-flows.html) | Full upload/settings/acknowledgement sample → Summary/cards/Quiz → sources/results/review/restart → New session. |
| [reliability.html](reliability.html) | 17 supplied cases grouped as errors, usable-content notices and demo information; four outcome patterns plus pending. |
| [statuses-r20.html](statuses-r20.html) | Shared processing, password rejection and AI-failure patterns with Round 21 copy/mobile refinement. |

The English UI is separate from fixed Norwegian Bokmål/English generated material and Brief/Detailed Summary. Empty Home requires PDF/settings/active acknowledgement; active Home locks those choices and provides Continue studying/New session. Continue returns to the last learning tab with progress. New session Cancel/Escape preserves work; confirmation empties Home, blocks ended-state revival and requires fresh later choices/acknowledgement. The original device file is unaffected.

Uploads are metadata-only and all material/passages are saved synthetic examples. No PDF text, AI/API call or automatic successful generation is represented. The basic shell's initial learning-tab shortcut and outside-app scenario/sample controls are prototype inspection aids; real app navigation requires an active session and never generates content itself. Reload starts fixtures again, not recovered student data. Review pending does not finish automatically.

Editable fragments/builders remain one directory above. [Promoted snapshots](../../mockups/) are unchanged copies of these current exports, with their roles and refresh instructions in [the artifact guide](../../README.md). [Final evidence](../review-final-ux/inspection.json) and [Round 21 evidence](../review-v1-error-simplification/inspection.json) state the exact tested scope. Real extraction, generation, cleanup, source quality and full accessibility/user testing remain implementation/evaluation work.

Earlier active Home, status comparison, visible-button/session-menu, neutral/warm Home and colour comparisons remain historical. Their original sources/exports and [the prior guide](../round-21-before-finalization/browser-README.md) are preserved; they do not override the selected concept. Private PDFs and temporary files must remain outside tracked UX evidence.
