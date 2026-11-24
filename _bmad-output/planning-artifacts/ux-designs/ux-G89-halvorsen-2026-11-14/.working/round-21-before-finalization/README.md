# AI Study Buddy — UX concept guide

**Selected concept — UX in progress, 24 November 2026.** The latest Home, Summary, Flashcards and Quiz are the selected concept for continued work. Round 18 adopts active Home and the approved Continue studying and New session flows. Round 20 adopts the three approved status presentations and proposes the remaining reliability and learning/source presentations separately. Round 21 refines reliability feedback/state handling and shared mobile alignment within the existing system. `DESIGN.md` and `EXPERIENCE.md` remain drafts; no next BMAD phase or UX completion is implied.

## Current concept

| Artifact | Purpose |
|---|---|
| [DESIGN.md](DESIGN.md) | Selected appearance, colour roles and outstanding visual work. Required BMAD filename is retained. |
| [EXPERIENCE.md](EXPERIENCE.md) | Interaction rules, prototype/production boundary and outstanding UX states/flows. |
| [decisions.md](decisions.md) | Current selection followed by the chronological concept/preference history. |
| [.memlog.md](.memlog.md) | Append-only BMAD decision/event record, maintained with the BMAD helper. |
| [.working/study-preview.html](.working/study-preview.html) | Editable selected concept, initially empty Home; active sessions show the selected session-information card and actions. |
| [.working/study-preview-status-r20.html](.working/study-preview-status-r20.html) | Current selected-status entry, with shared Round 21 copy/mobile refinements; scenario controls stay outside the app. [Browser entry](.working/browser-preview/statuses-r20.html). |
| [.working/remaining-ux-review-r21.html](.working/remaining-ux-review-r21.html) | Fresh Round 21 combined chat-review entry for the refined reliability and learning/source concepts. Additional presentations await review. [Stable browser entry](.working/browser-preview/remaining-ux.html). |
| [.working/remaining-ux-review.html](.working/remaining-ux-review.html) | Stable editable combined entry, rebuilt alongside the fresh Round 21 path. |
| [.working/reliability-review.html](.working/reliability-review.html) | Proposed additional PDF/coverage, source-validity, setup and service outcomes. [Browser entry](.working/browser-preview/reliability.html). |
| [.working/learning-flows-review.html](.working/learning-flows-review.html) | Proposed complete card/Quiz and source-panel flows. [Browser entry](.working/browser-preview/learning-flows.html). |
| [.working/ux-coverage-review.md](.working/ux-coverage-review.md) | PRD-to-concept coverage matrix, outstanding actual usability work and production/evaluation limits. |
| [.working/reliability-scenarios.md](.working/reliability-scenarios.md) | Internal mapping of all 17 PRD-relevant fixtures to shared patterns, retained state/publication rules and actual verification prerequisites. Technical IDs are not student controls. |
| [.working/round-20-before-simplification/](.working/round-20-before-simplification/) | Preserved Round 20 browser exports of main, selected statuses, reliability, learning and combined review before Round 21 refinements. |
| [.working/study-preview-active-home-r18.html](.working/study-preview-active-home-r18.html) | Preserved Round 18 active Home review. [Browser entry](.working/browser-preview/active-home-r18.html). |
| [.working/browser-preview/index.html](.working/browser-preview/index.html) | Standalone browser export of that source. [Local preview instructions](.working/browser-preview/README.md). |
| [imports/front-page-reference.png](imports/front-page-reference.png) | User-supplied visual reference, retained as a source rather than a product requirement. |
| [.working/review-v1-error-simplification/](.working/review-v1-error-simplification/) | Current Round 21 targeted browser/static checks, 22 captures and [inspection report](.working/review-v1-error-simplification/inspection.json). Synthetic prototype evidence only. |
| [.working/review-ux-continuation/](.working/review-ux-continuation/) | Round 20 targeted browser/static checks and 22 captures. [Inspection report](.working/review-ux-continuation/inspection.json) covers selected status integration, 17 reliability scenarios, complete learning/source flows and the combined review. It is not an actual user study or full accessibility audit. |
| [.working/review-processing-states/](.working/review-processing-states/) | Historical Round 19 captures/checks for the three status sketches, before their Round 20 selection. Targeted prototype evidence, not validation of the current integration. |
| [.working/review-active-home-selected/](.working/review-active-home-selected/) | Round 18 main/review checks and desktop/mobile captures: six widths, selected session flows, focus/reset guards and static/export/build integrity. Targeted prototype evidence, not production validation or a full audit. |
| [.working/review-selected-concept/](.working/review-selected-concept/) | Historical Round 11 baseline checks and screen captures. |
| [.working/prd-ux-constraints.md](.working/prd-ux-constraints.md) | Derived PRD constraint extract; the original PRD/addendum remain authoritative. |
| [.working/impeccable-context/PRODUCT.md](.working/impeccable-context/PRODUCT.md) | Derived supporting context, not a separate product specification. |


## Selected status patterns — Round 20

On 24 November, the user approves all three Round 19 concepts on desktop/mobile. Their processing, password-required PDF and Flashcards AI-failure presentations now form the selected status pattern. Use the [fresh main status review](.working/study-preview-status-r20.html) or [browser entry](.working/browser-preview/statuses-r20.html). The previous main is preserved as [.working/study-preview-round-19.html](.working/study-preview-round-19.html) and [main-before-statuses-r19.html](.working/browser-preview/main-before-statuses-r19.html).

Processing names exactly Checking PDF, Extracting text, Generating summary, Generating flashcards or Generating quiz, without invented progress or automatic completion. The password-required PDF example has no Summary, uses a neutral canvas and recovers through confirmed New session without unlock/retry. The yellow Flashcards AI error preserves valid Summary and locked settings; manual Try again shows pending Generating flashcards without an automatic outcome. All remain labelled examples, with no PDF reading or API calls. Preview-only scenario controls stay outside the app.

The [Round 19 comparison](.working/processing-states-comparison.html), [browser comparison](.working/browser-preview/processing-states.html) and individual [processing](.working/status-loading.html), [PDF problem](.working/status-pdf-problem.html) and [AI failure](.working/status-ai-error.html) sketches remain as review history. `processing-states-build.py` and its parts/styles/logic author those separate sketches; they do not update the selected main.

## Remaining UX — Round 20 Proposal, Refined in Round 21

Open the [combined review](.working/remaining-ux-review.html) or [browser entry](.working/browser-preview/remaining-ux.html), then inspect [reliability](.working/reliability-review.html) and [learning/source flows](.working/learning-flows-review.html). These extend the selected visual system and existing PRD behaviour. Their new presentations and copy are pending user review and are not adopted into the main.

The reliability review covers additional PDF/coverage problems, reduced/invalid source outcomes, setup/service failures and saved-demo/live-action explanation. The learning review covers complete card/Quiz practice, review/results/restart and source inspection. The [coverage matrix](.working/ux-coverage-review.md) records the requirements and limits; it does not claim live extraction, AI quality, complete accessibility or actual user-study results. Neither the examples nor preview scenario controls add product modes, settings or numeric upload limits.

[Round 20 inspection](.working/review-ux-continuation/inspection.json) records the earlier version's selected main/session flows at six widths, status/reliability/learning/combined layouts, manual retries, explicit Quiz confirmation/locking, both material languages with a 6/8 = 75% example, same-set restarts and source/focus return. Targeted keyboard checks include arrow-key answer selection without feedback and Cancel/Escape/focus return. Its product assertions/static checks passed with no script exceptions. This evidence remains scoped to Round 20 and does not verify the Round 21 refinements. New reliability/learning presentations remain pending user review, and broader keyboard/accessibility and actual usability work remain open.

## Reliability refinements — Round 21

Open the [fresh combined review](.working/remaining-ux-review-r21.html) or the stable [browser entry](.working/browser-preview/remaining-ux.html). This round retains all 17 relevant internal fixtures while reusing four outcome presentations: document error, generation error, usable-content notice and demo information, plus existing pending status. Thirteen fixtures are blocking errors, three are usable notices and one is demo information. They are test cases for existing PRD behaviour, not 17 new features or student-selectable modes.

Student messages explain what could not be read/created, what remains available and what to do next. Technical structure/source-validation causes stay in the [internal mapping](.working/reliability-scenarios.md). Cards/Quiz failures and manual retries preserve valid Summary, other content and practice progress. Source locations do not prove factual support, and PDF coverage fixtures do not establish a detector; actual observable stop criteria remain technical handoff work. No advanced PDF interpretation is introduced.

One shared mobile rule centres Flashcards/Quiz content, notices and actions and the loading/error boxes at app widths up to 540px. Summary reading prose/notices, source excerpts and desktop styling retain the established treatment. Shared status copy/alignment also refine the selected main and Round 20 status entry. The separate Round 19 sketches and Round 18 entries remain historical. Additional reliability and complete learning/source presentations still await review; UX stays open/draft.

[Round 21 inspection and captures](.working/review-v1-error-simplification/) record passing targeted prototype checks: all 17 cases at 1280/390/320px, nine manual retries, valid Summary and locked Quiz answers retained across four Flashcards failures, and Flashcards position retained across three Quiz failures. Main-state preservation, both study-material languages, complete learning/source flows and the combined review also pass, with no script exceptions. The 22 captures and [report](.working/review-v1-error-simplification/inspection.json) bind evidence to current source hashes. Existing product CSS is unchanged except for one mobile-only rule; five exact exports, valid IDs/references/JavaScript and four reproducible builders pass. PRD, imported references, earlier frozen concepts and installed skills remain unchanged. These are synthetic prototype checks, not PDF-detector, live-AI, production-state or actual-user validation. UX remains open/draft.

## Selected session action and earlier exploration

**Selected placement — Round 14:** The user chooses **Visible button**. The [main prototype](.working/study-preview.html) now includes one directly visible New session button beside the document context on learning screens, with the existing confirmed reset flow. Its illustrated Home and visual identity are preserved. The separate [Session menu](.working/session-menu.html), [Visible button concept](.working/session-buttons.html) and [comparison](.working/session-actions-comparison.html) remain as exploration history. The menu is not the selected default, and Clear remains removed. See decisions.md and the [browser preview guide](.working/browser-preview/README.md).

**Historical diagnostic entry — Round 15:** [This frozen review copy](.working/study-preview-visible-button-r15.html) opens the Round 14 concept on Summary, with [its browser export](.working/browser-preview/visible-button-r15.html). Its separate path and presentation-state key helped inspect a reported missing button; the exact cause of that earlier display is not established. [Round 15 visibility evidence](.working/review-preview-visibility/) records the button on all three learning screens at desktop and mobile widths. This entry is preserved unchanged and is no longer the current review link.

The `session-actions-*` source parts and `session-actions-build.py` derive the earlier comparison from the preserved [pre-session-action baseline](.working/study-preview-round-11.html). `session-actions-promote.py` reproduces the frozen Round 15 and Round 18 entries before building the selected main; `home_active_session.py` applies the approved active Home snippets, and `selected_statuses.py` with `selected-status-logic.js` carries the approved status pattern into the main. The separate `home-active-session-build.py` uses the frozen Round 17 main, and `processing-states-build.py` uses the frozen Round 19 main to reproduce their historical concepts. These are concept-authoring helpers, not production application code.

Historical Round 12 captures and inspection are saved under [.working/review-session-actions/](.working/review-session-actions/); that round includes New session and Clear. Its sources and exports are preserved in [.working/session-actions-round-12/](.working/session-actions-round-12/). Round 13 one-action checks are under [.working/review-new-session/](.working/review-new-session/), and selected main-preview checks are under [.working/review-visible-button/](.working/review-visible-button/). Round 18 also approves the existing dialog flows; broader state coverage and actual usability review remain open.

## Selected active Home — Round 18

The user approves the active Home card and both flows. The [main source](.working/study-preview.html) and [browser index](.working/browser-preview/index.html) still open the illustrated empty Home. An active example or metadata-only session replaces the upload form with filename, read-only output language/Summary detail, and the approved Round 17 equal-sized Continue studying and New session actions. Continue returns to the last visited learning tab with content and progress preserved; returning to Flashcards shows the front of the same card. The existing New session dialog preserves all state on Cancel/Escape; confirmation clears the session to empty Home and leaves the original local file unaffected. Starting again is optional and requires fresh PDF/settings/acknowledgement.

The preserved [Round 18 active Home review](.working/study-preview-active-home-r18.html) and [browser entry](.working/browser-preview/active-home-r18.html) show the labelled prewritten active example before status integration. The earlier main is preserved as [.working/study-preview-round-17.html](.working/study-preview-round-17.html) and [home-before-active-r17.html](.working/browser-preview/home-before-active-r17.html). These entry points remain metadata-only previews with prewritten content; no real PDF processing, AI calls or session recovery across reloads is represented.

The [separate Round 16 concept](.working/home-active-session-review.html), [Round 17 action review](.working/home-active-session-buttons-review.html), [browser concept](.working/browser-preview/home-active-session.html) and [Round 16 archive](.working/home-active-session-round-16/) remain historical exploration. Their existing [active Home checks](.working/review-active-home/) and [button checks](.working/review-home-buttons/) document those rounds. `home-active-session-build.py` reproduces the separate concept from its source parts and preview-width shell; it is not the selected main's entry point.

## Historical concepts and evidence

- `navigation-options.html`, `visual-concepts.html`, `notatkort-atlas-refinement.html` and `function-backgrounds.html` preserve the earlier comparisons. `concept-parts/` contains their reusable source parts.
- `study-preview-round-4.html`, `-5.html`, `-6.html`, `-7.html` and `-9.html` preserve previous concept snapshots. `browser-preview/neutral-home-round-7.html` is the separately reviewable neutral Home archive.
- `home-warm-cream.html`, `home-warm-cream.css` and their browser export preserve the alternative warm Home. `home-colour-comparison.html` and `browser-preview/home-comparison.html` show the **historical Round 7 versus warm** comparison, not the current selected concept.
- `review-round-5/`, `-6/`, `-7/`, `-9/`, `-10/` and `review-home-warm-cream/` preserve dated screen captures and checks. Their appearance reflects the concept round they document; they are not duplicates of the current concept.

All paths above are under `.working/` unless otherwise stated. Historical approval/pending wording records the state at that time; the current selection in decisions.md supersedes it.

## Source Control review — 19 November 2026

The initial 54 changes were **52 UX files plus two log files**, about 5.59 MB in total. The read-only review classified them as 11 current/source/support/reference artifacts, 35 historical sketches/source parts/checks and six alternative/comparison artifacts. No exact byte duplicates or disposable temporary files were found. The six alternative/comparison artifacts can be regenerated but preserve an explicitly requested comparison, so they are retained. **No files were deleted or moved.**

That checkpoint added this guide and Round 11 selected-concept check evidence. Existing BMAD names, directories, configuration, installed skills and PRD sources remain intact. “Concept” is used for preliminary sketches/variants; historical decision substance and saved visual evidence are retained.

Private T1–T3 PDFs remain only in the ignored `/test-data/pdfs/` directory. Do not add them, PDF-derived private content, credentials, temporary browser profiles, tool caches or `.DS_Store` to the repository. All study content in this prototype and its captures is prewritten illustrative content; the imported reference is the user-supplied UI image.

## Continue here

Continue the same UX run from the selected main, active Home/session flows and approved status patterns. Review the Round 21 reliability refinements and complete learning/source presentations on desktop/mobile, resolve findings, complete systematic keyboard/state checks and record an actual user walkthrough of PRD UJ-1. Refine the draft peer contracts from those outcomes before a separate decision to finish UX. Parser/provider/resource/cleanup choices and live content-quality evaluation remain technical/evaluation handoff work. No production app implementation or next BMAD phase is part of this checkpoint.
