---
name: AI Study Buddy
status: draft
created: 2026-11-14
updated: 2026-11-24
concept: selected
description: Selected Notatkort-based concept with Atlas-inspired Quiz options; UX remains open.
colors:
  home-canvas: '#edeef2'
  summary-canvas: '#eef5ef'
  flashcards-canvas: '#fbf7e5'
  quiz-canvas: '#edf4fc'
  surface: '#ffffff'
  brand-ink: '#343a40'
  headline: '#171a19'
  brand-summary: '#4f9f6f'
  brand-flashcards: '#e0ae26'
  brand-quiz: '#4b9bc8'
typography:
  body:
    fontFamily: '"Avenir Next", Avenir, "Segoe UI", system-ui, sans-serif'
    fontSize: 16px
    lineHeight: '1.6'
  summary:
    fontSize: 17px
    lineHeight: '1.8'
rounded:
  md: 14px
  lg: 16px
  home-card: 34px
components:
  upload-cloud:
    color: '{colors.brand-flashcards}'
  pdf-arrow:
    color: '{colors.brand-ink}'
sources:
  - ../../prds/prd-G89-halvorsen-2026-11-03/prd.md
  - ../../prds/prd-G89-halvorsen-2026-11-03/addendum.md
  - decisions.md
  - imports/front-page-reference.png
---

# AI Study Buddy — Selected UX concept (draft)

## Brand & Style

On 19 November 2026, the user selected the latest **Home, Summary, Flashcards and Quiz** in [.working/study-preview.html](.working/study-preview.html) as the concept to continue. This includes Round 10's Home colours and the existing learning screens. On 20 November, Round 18 adopts the active Home state and both session flows, retaining the approved Round 17 action treatment. On 24 November, the user approves all three Round 19 status presentations on desktop and mobile; Round 20 carries these into the selected concept and continues the remaining UX review. Round 21 refines plain-English reliability feedback, shared presentation/state rules and mobile alignment within that visual system. The concept is selected; these contracts remain drafts and the UX phase is open. See the current decision in [decisions.md](decisions.md) and the [artifact guide](README.md).

Keep Notatkort's soft, minimal, professional character with rounded forms, readable typography and Atlas-inspired separate Quiz answer boxes. The [supplied visual reference](imports/front-page-reference.png) informs the illustrated Home composition. Earlier neutral and warm Home variants are historical alternatives, not competing defaults.

The v1 interface stays English. Generated study material uses the separate **Norwegian Bokmål** / **English** choice; [EXPERIENCE.md](EXPERIENCE.md) defines this distinction. PRD requirements govern behaviour. These peer UX documents record the selected concept; historical sketches and imports do not override them.

## Colors

| Surface or role | Selected concept |
|---|---|
| Home canvas | `{colors.home-canvas}` — light neutral grey |
| Summary canvas | `{colors.summary-canvas}` — very light sage green |
| Flashcards canvas | `{colors.flashcards-canvas}` — very light warm yellow |
| Quiz canvas | `{colors.quiz-canvas}` — very light blue |
| Content cards and answer boxes | `{colors.surface}` |
| Wordmark, Upload your PDF and decorative PDF arrow | `{colors.brand-ink}` |
| Upload cloud and middle logo layer | `{colors.brand-flashcards}` — exact shared golden yellow |
| Upper / lower logo layers | `{colors.brand-summary}` / `{colors.brand-quiz}` |

The logo's three original layers, strokes and existing responsive sizes stay fixed across all four screens. Home's active tab is neutral grey (`#e1e5e9`, border `#737e8b`), with a neutral `#526173` keyboard-focus ring. Learning tabs and enabled primary actions follow their green/yellow/blue function themes; secondary controls are white with coordinated borders, and disabled controls are neutral. The existing pastel illustration cards and corner forms remain unchanged.

## Typography

Use the current Avenir/system stack in `{typography.body.fontFamily}`. Keep **Make studying easier** near black, with the existing responsive 56/48/35px scale. Detailed Summary uses `{typography.summary.fontSize}`, `{typography.summary.lineHeight}` and a maximum 68ch measure, distinct headings and generous paragraph spacing. Current type and layout are the baseline, not a new redesign.

## Layout & Spacing

Prioritise laptop/PC with a responsive single web application. Keep one in-app top menu: Home, Summary, Flashcards, Quiz. Home has a centred introduction and raised white card: upload/settings without a session, read-only session information and actions with an active session. A PDF illustration sits on the left and stacked learning cards on the right. Decorations stay clear of important text and controls and simplify or disappear on smaller screens; fields stack as needed. Preserve the existing spacing and responsive rules.

## Elevation & Depth

Keep restrained soft shadows on the Home upload card and illustrations. Learning content remains calm and readable. No added decorative animation; the existing 200ms function-canvas transition respects reduced motion.

## Shapes

Keep the existing rounded card, control and answer-box shapes. The selected prototype uses 16px learning cards, 14px separated Quiz answers and a 34px Home upload card. The logo form remains unchanged.

## Components

- **Empty Home:** obvious dashed rounded PDF selector, clear upload icon, output-language and Summary-detail choices, Generate Summary, concise external-AI/material restrictions, unchecked acknowledgement and temporary-session copy.
- **Active Home:** filename, read-only output language and Summary detail, Continue studying and a directly visible New session action. The card replaces the upload form only while the session is active.
- **Summary:** white reading card, Brief/Detailed selected at startup, readable headings/prose and a route to the existing Quiz.
- **Flashcards:** one white front/back card, actual count, Previous/Next, answer-side source link and repeat-same-set treatment.
- **Quiz:** four separate rounded white answer boxes, distinct selected state, Confirm answer, then feedback/source/result treatment.
- **View source:** the existing side panel illustrates filename, physical page and highlighted original excerpt. Full source/state coverage remains to be completed in UX.

**Selected New session placement — Round 14:** The user selects **Visible button**: one directly visible New session button beside the document context on Summary, Flashcards and Quiz. Keep the approved white rounded secondary-control treatment with the active function's border/hover colours. On desktop it sits beside the document information; on mobile it wraps beneath it. There is no Session disclosure or separate Clear command in the selected main prototype. [The earlier comparison](.working/session-actions-comparison.html) remains for traceability; the Session-menu option is not selected. Round 18 approves the existing dialog and its flows; broader state coverage and actual user walkthrough remain open without reopening the chosen placement.

**Selected active Home — Round 18:** The [main prototype](.working/study-preview.html) now uses the approved active-session card within the existing grey Home canvas, white surface, shared logo, typography, corner forms and side illustrations. Session values and actions stack on mobile, where decorative illustrations remain hidden. The empty Home form remains the initial and confirmed-reset state. [The fresh review entry](.working/study-preview-active-home-r18.html) opens the labelled active example; earlier separate concepts are historical.

The approved Round 17 actions use 16px text/500 weight, 56px height and 15px corners, with a 14px gap. They share equal columns on desktop and stack at equal full width on mobile. Continue retains green; New session uses a light neutral fill. Both flows are approved: Continue returns to the last learning tab with progress preserved, while the existing New session dialog preserves state on Cancel and clears to empty Home on confirmation. See EXPERIENCE.md for the Flashcards return rule and session boundaries.


## Selected Processing and Failure Patterns — Round 20

On 24 November, the user approves all three presentations from the [Round 19 comparison](.working/processing-states-comparison.html) for desktop and mobile. Retain their selected typography, rounded white surfaces, shared logo/navigation, responsive spacing and status hierarchy in the main concept. The [fresh Round 20 status review](.working/study-preview-status-r20.html) separates the current integrated presentation from earlier review entries. Any scenario/operation selector belongs outside the app as a labelled preview control.

Processing names only the operation represented: **Checking PDF**, **Extracting text**, **Generating summary**, **Generating flashcards** or **Generating quiz**, without invented percentages or automatic completion. The password-required [PDF problem](.working/status-pdf-problem.html) uses the neutral canvas and has no Summary available; its recovery uses the existing confirmed New session flow, without an unlock or retry control. The [AI failure](.working/status-ai-error.html) uses the yellow Flashcards canvas, preserves access to valid Summary and offers manual Try again. That action shows pending Generating flashcards only. Approval selects these presentations; it does not establish live processing or select every other error/coverage state.

## Remaining State and Learning Presentations — Round 20 Proposal, Refined in Round 21

The [remaining UX review](.working/remaining-ux-review.html) brings together separate [reliability](.working/reliability-review.html) and [learning/source](.working/learning-flows-review.html) concepts. Their presentation and copy await review before adoption into the main. Reuse the selected visual system; distinguish information, a usable reduced result and a blocking failure through explicit headings, explanations and actions as well as colour.

The reliability concepts extend the approved status pattern to other PDF/coverage, source-validity, setup/service outcomes and saved-demo/live-action explanation. Learning concepts extend the existing card/Quiz and source-panel presentation to complete sets, review/results and multiple supporting passages. Use actual example counts and keep source location distinct from factual support. The [PRD coverage review](.working/ux-coverage-review.md) records current versus proposed coverage and remaining usability/production limits. These are labelled prewritten examples, not new product requirements or a final demo.

## Reliability and Mobile Refinements — Round 21

Review the [fresh combined entry](.working/remaining-ux-review-r21.html), which avoids relying on an earlier embedded chat copy. The stable [browser review](.working/browser-preview/remaining-ux.html) remains available. The additional reliability and complete learning/source presentations still await review before adoption; the selected main also receives the shared status-copy and mobile refinements.

Reuse four outcome presentations: **document error**, **generation error**, **usable-content notice** and **demo information**, plus the existing operation-specific pending card. The 17 internal cases map to these patterns: 13 blocking errors, three usable notices and one demo-information fixture. A new technical reason changes the text/action as applicable, rather than creating another visual system. Keep the reason codes and validation details in the [internal mapping](.working/reliability-scenarios.md). Student-facing copy explains the problem, available material and next action in plain English; it does not name malformed response structures or reference-validation mechanisms.

At app widths up to 540px, centre Flashcards/Quiz card, question/option, help, feedback, result/end and count text; centre their notice and action content/groups as well. Empty-generation cards and the shared loading/error boxes use the same alignment; status icons sit above centred headings. Summary reading prose and Summary notices retain their reading alignment, and source excerpts, navigation and document information keep their existing treatment. Desktop styling remains the established baseline. Keep this mobile rule shared across current previews so equivalent states align consistently.

Errors block the rejected document or new output; usable notices accompany content that remains available. Demo information explains saved playback and unsupported live actions. Preserve valid Summary/other content and practice progress when Flashcards or Quiz creation fails or is pending. These refinements add no product modes, advanced PDF detection or new v1 features. Real extraction/coverage/source checks remain technical verification work; neither layout nor a fixture demonstrates detection or factual support.

[Round 21 checks and captures](.working/review-v1-error-simplification/) confirm centred mobile states and unchanged existing desktop CSS across the current previews. Targeted inspection covers 17 cases at three widths, complete learning/source flows and the combined review, without overflow or script exceptions. These checks do not establish a complete accessibility audit or user approval.

## Do's and Don'ts

Preserve the selected visual baseline and use **concept** for preliminary sketches and variants. Keep BMAD's `DESIGN.md`, directory names and references intact. Avoid crowded screens, childish/gamified styling, unnecessary motion and unsupported privacy claims.

Remaining UX work: review the new reliability and learning/source presentations on desktop/mobile, resolve any resulting interaction or copy issues, and complete systematic keyboard/state checks and an actual user walkthrough. Real extraction, generation, cleanup and source/quality evaluation remain implementation/evaluation work; open provider/parser/resource choices do not by themselves block this UX review. Reconcile both draft contracts after review before any separate UX-completion decision. This update starts no next BMAD phase.
