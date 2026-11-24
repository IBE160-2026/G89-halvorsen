---
name: AI Study Buddy
status: draft
created: 2026-11-14
updated: 2026-11-24
concept: selected
sources:
  - ../../prds/prd-G89-halvorsen-2026-11-03/prd.md
  - ../../prds/prd-G89-halvorsen-2026-11-03/addendum.md
  - decisions.md
---

# AI Study Buddy — Experience (draft)

## Foundation

The v1 interface is English throughout, with no interface-language switch. This includes navigation, actions, help, status, validation, confirmation text and accessible labels.

The latest Home, Summary, Flashcards and Quiz form the **selected concept**, confirmed by the user on 19 November 2026. Round 18 on 20 November adopts active Home and approves Continue studying and New session flows. On 24 November, the user approves all three Round 19 processing/PDF/AI presentations on desktop and mobile; Round 20 adopts those patterns and continues the remaining UX. Round 21 refines shared reliability feedback, state preservation and mobile alignment. The UX phase is open and this document remains a draft; selection is not a claim that all states or journeys are complete. Continue from [the current prototype](.working/study-preview.html), using [DESIGN.md](DESIGN.md) for visual identity and [README.md](README.md) for current versus historical artifacts. Laptop/PC is the priority; the same web application responds to mobile.

The **study material language** is a separate startup choice: **Norwegian Bokmål** or **English**. It applies to generated Summary, Flashcards and Quiz content and stays fixed for the study session under PRD FR-4/FR-21. **Brief** and **Detailed** apply only to Summary under FR-5. These choices do not change the interface language.

Original source excerpts and filenames retain their original wording. The PRD and addendum remain authoritative for product behaviour; this update introduces no functionality or production implementation.

## Information Architecture

**Prototype navigation:** The selected concept preview has one clickable Home / Summary / Flashcards / Quiz menu inside the app on all four screens. It initially opens the existing illustrated empty Home. Before the first startup/reset, learning tabs may load labelled prewritten examples for inspection; this does not process a PDF or call AI. With an active example/session, Home shows read-only document/settings information and the approved Continue studying and New session actions. Home inspection preserves the session and keeps its settings locked. Continue studying returns to the last visited learning tab, initially Summary if none has been visited, preserving content and practice progress. Returning to Flashcards retains its position and shows its front; Quiz answers remain intact. Closing View source preserves the current view and revealed answer. After confirmed New session, the learning links stay disabled until fresh PDF/settings/acknowledgement startup; neither navigation nor restored host presentation choices may revive the ended example.

**Production boundary:** The revised PRD governs real sessions. **New session is the single explicit session-ending action**, whether the student is finished or wants a different PDF, study-material language or Summary detail. The separate Clear action is removed and FR-16 is retired; FR-15/FR-21 and shared rules retain confirmation and cleanup protections. Cancel preserves the entire current session. Confirmation returns to empty ordinary Home; starting again is optional. A new study session requires fresh PDF/settings selection and active acknowledgement. Navigation alone never generates content or ends the session, and the original device file is unaffected.

## Voice and Tone

Use concise, direct English instructions and sentence case. Keep the product labels **Summary**, **Flashcards**, **Quiz**, **Norwegian Bokmål**, **English**, **Brief** and **Detailed** consistent.

Explain failures through the student's task: what could not be created or read, what remains available and the next action. Keep schema/structure errors, reason codes and source-validation mechanics in internal review/development evidence. For example, say **We couldn't create your flashcards** with manual **Try again**, rather than asking the student to understand an invalid response structure. Distinct internal causes can reuse the same concise message when their recovery is the same. Describe only a detected PDF condition; do not infer that every textless PDF is scanned or claim complete/factually verified coverage.

Separate English interface feedback labels from generated explanations in the selected study language. Keep essential external-processing, sharing-restriction, acknowledgement and temporary-session information visible when shortening startup copy. The PRD remains authoritative for product behaviour.

Use **concept** for preliminary sketches and variants. Required BMAD filenames such as `DESIGN.md` remain unchanged.

## Component Patterns

| Surface | Captured interaction and scope |
|---|---|
| Empty Home | Choose PDF metadata, Norwegian Bokmål/English and Brief/Detailed; Generate Summary stays disabled until all choices and acknowledgement are present. The preview uses saved examples and reads no PDF text. |
| Active Home | Show filename and fixed output choices. Continue studying returns to the last visited learning tab with content/progress preserved; New session opens the existing confirmation. |
| Summary | Show the session-selected level; keep the reading measure and rhythm defined in DESIGN.md. Navigation to Quiz opens the existing attempt. |
| Flashcards | Flip one card; sources appear on the back. Previous/Next changes card, actual count is visible, and newly shown cards start on the front. Function return preserves card position and hides its answer. |
| Quiz | Select among four alternatives, then explicitly confirm. Feedback follows confirmation; confirmed answers are locked. The selected main's one-question example is illustrative; the separate Round 20 learning review proposes the complete multi-question/review/result presentation. |
| View source | Show filename, physical page and highlighted original-language excerpt; close without losing current view, practice position or revealed answer. A matching location does not prove factual support. |

Shared controls follow the function-canvas tokens `{colors.summary-canvas}`, `{colors.flashcards-canvas}` and `{colors.quiz-canvas}` in DESIGN.md. Home uses `{colors.home-canvas}` and a neutral active tab. Colours supplement labels, borders and active-state semantics.

## State Patterns

The current concept illustrates empty/active Home, startup gating, empty/example-ready learning views, card front/back, Quiz selection/confirmation/feedback and source open/closed. The three-card and one-question sets are illustrative, not product limits or the final key-free demo.

The processing/password/AI-error presentations are selected in Round 20. Other PDF, coverage, source-validity, setup/service and complete learning/source presentations are proposed separately for review, as described below. Continue systematic keyboard/state review and actual user walkthroughs under the PRD. Real processing/cleanup and late-result isolation require implementation verification; no automatic regeneration or repair is introduced.

**Round 14 — Visible button selected:** New session is the single explicit session-ending action, and the user selects a **directly visible button beside the document context** on the learning screens. It is integrated in [the main prototype](.working/study-preview.html). Cancel/Escape preserves the session and practice state and returns focus to that button. Confirmation returns to empty Home without requiring another upload; the student may stop there. A later cancelled/rejected file selection cannot restore the ended example, and fresh generation still requires PDF/settings/acknowledgement. Active choices remain locked so Home inspection cannot bypass the confirmed reset. The [one-action placement comparison](.working/session-actions-comparison.html) and [two-action Round 12 archive](.working/session-actions-round-12/session-actions-comparison.html) are historical exploration, not competing defaults. Round 18 approves the existing dialog and its Cancel/confirm flows. Broader state coverage and actual user walkthrough remain open. No real PDF processing, late AI response, provider cleanup or production validation is represented.

**Selected active Home and session flows — Round 18:** Without an active session, retain the existing PDF/settings form. With a session, the selected main shows filename, locked output language and Summary detail, Continue studying, and direct New session with the approved Round 17 equal-sized actions. The [fresh review](.working/study-preview-active-home-r18.html) opens an explicitly labelled prewritten active example; the main opens empty Home.

Continue studying returns to the last visited learning function, initially Summary if none has been visited, preserving content and practice progress. Returning to Flashcards still shows the front of the retained card; Quiz answers and feedback remain intact. No settings can be edited during an active session.

New session uses the existing dialog. Cancel/Escape keeps all working session state and restores focus to the invoking Home or learning-screen button. Confirmation clears the working session and reveals empty Home; the original local file is unaffected and the student may stop there. A later start requires fresh PDF metadata, choices and acknowledgement. No real PDF is processed or session restored across reloads. These flows are approved; remaining production-state and usability work does not reopen this selection.


## Selected Processing and Failure Patterns — Round 20

The user approves all three states in the [Round 19 comparison](.working/processing-states-comparison.html) for desktop/mobile on 24 November. Round 20 carries the presentations into the main concept, with a [fresh status review](.working/study-preview-status-r20.html). A labelled preview-only scenario/operation selector stays outside the app; it is an inspection aid, not a product setting. Show exactly the represented operation: **Checking PDF**, **Extracting text**, **Generating summary**, **Generating flashcards** or **Generating quiz**. There is no invented percentage, elapsed-time promise or automatic completion.

The [PDF problem sketch](.working/status-pdf-problem.html) represents a password-required PDF before a Summary exists. It uses the neutral canvas and supplies no unlock or retry action. Recovery is the existing confirmed New session: Cancel preserves the current state; confirmation returns to empty Home.

The [AI failure sketch](.working/status-ai-error.html) represents Flashcards generation failing while a valid Summary remains available. Keep the yellow function canvas, Summary navigation and fixed session choices. **Try again** is manual and opens **Generating flashcards**, staying pending without an automatic outcome. Preserve valid session material; do not imply automatic regeneration or repair.

These selected presentations use labelled prewritten examples, read no PDF content and make no AI/API calls. They do not establish real processing, source validity, provider cleanup or late-result isolation; the PRD/addendum remain authoritative. Earlier Round 18 and separate Round 19 entries remain historical records of their review stages.

## Remaining Reliability and Learning Flows — Round 20 Proposal, Refined in Round 21

Use the [combined remaining UX review](.working/remaining-ux-review.html) to inspect the separate [reliability](.working/reliability-review.html) and [learning/source](.working/learning-flows-review.html) concepts. These new presentations and copy await review; they are not adopted into the main. The [coverage matrix](.working/ux-coverage-review.md) maps PRD requirements to selected and proposed examples and separates open usability work from technical handoff.

**Reliability:** Explain the detected unsupported, damaged or no-usable-text PDF condition without assuming that every textless file is scanned. Distinguish incidental excluded content with reliable main text from material loss or uncertain main-text coverage that stops generation. A usable reduced card/Quiz set shows its actual count and an omission notice; invalid references remove the entire affected item only from an otherwise valid structure. Zero usable items, malformed structures and any invalid new Summary reference are errors, not empty successful results. Withhold the whole invalid new Summary. Preserve existing valid session content/progress; retry is explicit and manual. Setup/service/timeout examples must offer the applicable next step without selecting a provider, inventing limits or claiming provider deletion.

**Flashcards:** Show one item, front first, with Previous/Next and current/actual total. Flipping reveals the answer and its sources; the front reveals neither. Newly displayed cards and function returns show the front, retaining the position on return. Closing View source preserves a revealed answer. At the end, repeat the same set at the first card's front without generation or mastery tracking.

**Quiz:** Selection alone gives no feedback; explicit Confirm answer locks the answer and reveals feedback. Wrong answers show the correct option, a short explanation and source access. Next question advances after feedback; earlier questions and confirmed answers remain reviewable and locked. Switching functions or closing View source preserves the same question and answers. Completion reports correct/actual total, its percentage and the incorrectly answered questions. Review can inspect questions, answers, explanations and sources without changing the result. Restart reuses the same questions and clears the attempt's answers/progress/result; it does not generate. A reduced example set is an illustrative count, not a new product target or limit.

**Sources:** Each reference exposes the filename, physical page counted from 1 in file order, and highlighted original-language excerpt. Separate contributing passages remain individually inspectable. Generated translation/paraphrase does not replace original wording. A location match does not establish factual support. Source close preserves learning position, feedback and a revealed card, with focus returned to its trigger. This is an excerpt sidepanel, without a PDF viewer or direct page-navigation requirement.

**Demo boundary:** The reliability review proposes a saved-demo notice that explains own PDFs/fresh generation require the live version, without adding a mode toggle or credential form. All new examples are visibly prewritten UX fixtures. They are not the FR-42 key-free demo or evidence that live processing/source validation succeeds. The final demo still needs a permitted shareable PDF and saved Brief/Detailed summaries plus card/Quiz sets in both study languages, matching fixed startup choices, with unsupported live actions explained. No actual user study or production quality pass is established by these concepts.

## Reliability Refinement — Round 21

The [fresh combined review](.working/remaining-ux-review-r21.html) refines the proposed reliability flow and reuses the complete learning/source review. The stable browser entry remains [remaining-ux.html](.working/browser-preview/remaining-ux.html). Additional reliability/learning presentations still await review; plain-English shared status copy and mobile alignment also refine the selected main. Earlier Round 20 checks describe that earlier version and do not verify this refinement.

All 17 internal cases are relevant v1 test fixtures, with four reusable outcome presentations and the existing pending presentation. The [internal mapping](.working/reliability-scenarios.md) retains technical triggers, publication/state rules and required verification. Students encounter the applicable state, not a scenario selector or technical reason code.

| Presentation | Student outcome |
| --- | --- |
| Document error | Explain why this PDF cannot currently be used. Offer another PDF through confirmed New session; detected material loss/uncertain text extraction can also offer manual Try again. Password-required files retain no unlock/password workflow. |
| Generation error | Explain that the requested material could not be created. Offer manual Try again when retry can help; missing live setup instead explains this version's limitation and offers existing material. Preserve the active session. |
| Usable-content notice | Keep available material usable, show the actual item count and explain detected exclusions/limited output. No automatic refill or unsupported claim of complete coverage. |
| Demo information | Label saved material and explain own-PDF/fresh-generation restrictions. Saved playback is not an error. |
| Pending | Name only the operation actually running. End it on completion/failure; retries in the fixture stay pending without fabricating results. |

The case count is **13 blocking errors, three usable notices and one demo-information state**. Technical distinctions remain enforced before publication: malformed replies are rejected as a whole; any invalid new Summary reference withholds that whole Summary; reference-based filtering applies only to an otherwise valid card/Quiz set and removes each entire affected item. A nonempty subset is usable with a notice, while zero usable items is an error. No partial invalid Summary, automatic repair/refill or empty scored Quiz is shown.

Failure or pending generation in Flashcards/Quiz must retain valid Summary, other existing learning content and practice progress. Retrying the failed function must not clear another function's material, card position or Quiz answers. Function return still follows the existing card-front and locked-answer rules. Only confirmed New session clears the active session; Cancel preserves it. These synthetic retained-state fixtures are not production proof of all state combinations, request cancellation or late-result isolation.

The PDF coverage cases express PRD FR-40/FR-41 outcomes, not an implemented detector. Architecture must verify observable signals and explicit stop rules before claiming reliable main-text coverage or a specific detected omission. Empty/nonempty pages, a source location match and a synthetic figure example do not establish complete coverage or factual support. Advanced figure interpretation, OCR and repair remain outside v1.

[Round 21 evidence](.working/review-v1-error-simplification/inspection.json) verifies manual retry without loss of valid Summary, confirmed Quiz answers or Flashcards position, rejection/notice boundaries, actual reduced scoring and confirmed reset. Main, reliability, bilingual learning/source and combined-review checks pass with no script exceptions. This is prototype evidence; production request/session isolation and generated-content quality remain untested.

## Interaction Primitives

Use labelled native controls, visible keyboard focus and explicit answer confirmation. Keep one shared menu and preserve practice state on function switches. The existing short canvas-colour transition respects reduced-motion preferences. Source closing restores the invoking control and current example state. Full keyboard and state coverage remains open.

## Accessibility Floor

Keep meaningful labels, associated instructions, status feedback and sufficient text/control contrast. Decorative logo/illustrations/icons are hidden from assistive technology and supported by visible text; do not use colour alone to communicate location or answer state. Maintain clear focus and readable responsive content. Targeted browser checks are recorded in the artifact guide; they do not constitute a complete accessibility or usability audit.

## Key Flows

| Flow | Current coverage / next work |
|---|---|
| First startup → Summary | Selected metadata/choices/acknowledgement path and approved processing/password/AI status pattern; the refined additional reliability presentations await review. Real extraction/generation remain implementation work. |
| Summary ↔ Flashcards ↔ Quiz | Selected menu and practice-state preservation; complete card/Quiz/review/result presentations await review in the separate learning concept. |
| Learning → View source → learning | Selected panel and return rule; multiple-reference presentation and source/coverage outcomes await review in the separate concepts. |
| New session | The sole explicit session-ending action, directly visible on learning screens and active Home. Round 18 approves the existing dialog: Cancel preserves all; confirmation clears to empty Home without changing the original local file. Broader state coverage and user walkthrough remain open. |
| Active Home → continue / New session | Round 18 adopts the read-only session card and approved actions in the main. Continue preserves content/progress and returns to the last learning tab; the existing confirmed reset returns to empty Home. |

Use the PRD's existing **UJ-1: A student understands and revises course material** as the walkthrough scope. On 24 November, Camilla states her preferred study order is **Summary → Quiz → Flashcards**. Use that stated order for a proposed walkthrough after normal PDF/settings/acknowledgement startup, with source inspection and session ending as applicable. This is a reported preference, not an observed completed task or usability finding. Actual walkthroughs, findings and fixes remain to be recorded from observed use; prototype checks do not substitute for them. Do not mark UX complete or start the next BMAD phase.

## Responsive & Platform

The selected concept is desktop-first and responsive, with no separate mobile app. Preserve current wrapping navigation, stacked startup fields and simplified/hidden mobile decoration. Broader keyboard/state and usability checks across both sizes remain open; minor visual refinements may follow review.
