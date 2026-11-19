---
name: AI Study Buddy
status: draft
created: 2026-11-14
updated: 2026-11-19
concept: selected
sources:
  - ../../prds/prd-G89-halvorsen-2026-11-03/prd.md
  - ../../prds/prd-G89-halvorsen-2026-11-03/addendum.md
  - decisions.md
---

# AI Study Buddy — Experience (draft)

## Foundation

The v1 interface is English throughout, with no interface-language switch. This includes navigation, actions, help, status, validation, confirmation text and accessible labels.

The latest Home, Summary, Flashcards and Quiz form the **selected concept**, confirmed by the user on 19 November 2026. Minor refinements remain possible. The UX phase is open and this document remains a draft; selection is not a claim that all states or journeys are complete. Continue from [the current prototype](.working/study-preview.html), using [DESIGN.md](DESIGN.md) for visual identity and [README.md](README.md) for current versus historical artifacts. Laptop/PC is the priority; the same web application responds to mobile.

The **study material language** is a separate startup choice: **Norwegian Bokmål** or **English**. It applies to generated Summary, Flashcards and Quiz content and stays fixed for the study session under PRD FR-4/FR-21. **Brief** and **Detailed** apply only to Summary under FR-5. These choices do not change the interface language.

Original source excerpts and filenames retain their original wording. The PRD and addendum remain authoritative for product behaviour; this update introduces no functionality or production implementation.

## Information Architecture

**Prototype navigation:** The selected concept preview has one clickable Home / Summary / Flashcards / Quiz menu inside the app on all four screens. Home opens the startup screen for inspection; it is not Clear or New session and does not discard example practice state. The learning links display saved example content, without PDF processing or AI calls. Returning to Flashcards retains its position and shows its front; Quiz answers remain intact. Closing View source preserves the current view and revealed answer.

**Production boundary:** The existing PRD still governs real sessions. Changing PDF, study-material language or Summary detail requires confirmed New session and fresh startup under FR-15/FR-21. Clear requires confirmation under FR-16. Navigation alone never generates content. External transfer remains blocked until the current upload's active acknowledgement. The prototype screen menu does not add production functionality or replace these rules.

## Voice and Tone

Use concise, direct English instructions and sentence case. Keep the product labels **Summary**, **Flashcards**, **Quiz**, **Norwegian Bokmål**, **English**, **Brief** and **Detailed** consistent.

Separate English interface feedback labels from generated explanations in the selected study language. Keep essential external-processing, sharing-restriction, acknowledgement and temporary-session information visible when shortening startup copy. The PRD remains authoritative for product behaviour.

Use **concept** for preliminary sketches and variants. Required BMAD filenames such as `DESIGN.md` remain unchanged.

## Component Patterns

| Surface | Captured interaction and scope |
|---|---|
| Home | Choose PDF metadata, Norwegian Bokmål/English and Brief/Detailed; Generate Summary stays disabled until all choices and acknowledgement are present. The preview uses saved examples and reads no PDF text. |
| Summary | Show the session-selected level; keep the reading measure and rhythm defined in DESIGN.md. Navigation to Quiz opens the existing attempt. |
| Flashcards | Flip one card; sources appear on the back. Previous/Next changes card, actual count is visible, and newly shown cards start on the front. Function return preserves card position and hides its answer. |
| Quiz | Select among four alternatives, then explicitly confirm. Feedback follows confirmation; confirmed answers are locked. The one-question example illustrates feedback/result but does not cover the PRD's complete multi-question flow. |
| View source | Show filename, physical page and highlighted original-language excerpt; close without losing current view, practice position or revealed answer. A matching location does not prove factual support. |

Shared controls follow the function-canvas tokens `{colors.summary-canvas}`, `{colors.flashcards-canvas}` and `{colors.quiz-canvas}` in DESIGN.md. Home uses `{colors.home-canvas}` and a neutral active tab. Colours supplement labels, borders and active-state semantics.

## State Patterns

The current concept illustrates startup gating, empty/example-ready learning views, card front/back, Quiz selection/confirmation/feedback and source open/closed. The three-card and one-question sets are illustrative, not product limits or the final key-free demo.

Still to detail and review: actual processing states, unsupported/password/damaged/unreadable PDF errors, uncertain/partial coverage, reduced or invalid source sets, manual Try again, service/setup failures and preservation of valid active-session content. Complete confirmed/cancelled New session and Clear flows under the PRD, including late-result isolation. No automatic regeneration or repair is introduced.

## Interaction Primitives

Use labelled native controls, visible keyboard focus and explicit answer confirmation. Keep one shared menu and preserve practice state on function switches. The existing short canvas-colour transition respects reduced-motion preferences. Source closing restores the invoking control and current example state. Full keyboard and state coverage remains open.

## Accessibility Floor

Keep meaningful labels, associated instructions, status feedback and sufficient text/control contrast. Decorative logo/illustrations/icons are hidden from assistive technology and supported by visible text; do not use colour alone to communicate location or answer state. Maintain clear focus and readable responsive content. Targeted browser checks are recorded in the artifact guide; they do not constitute a complete accessibility or usability audit.

## Key Flows

| Flow | Current coverage / next work |
|---|---|
| First startup → Summary | Example path covers PDF metadata, output choices and acknowledgement; real PDF checks, processing and failure states remain UX work. |
| Summary ↔ Flashcards ↔ Quiz | Example menu and practice-state preservation are present; complete multi-question review/result flows still need coverage. |
| Learning → View source → learning | Example panel and return state are present; multiple references and source-failure/coverage notices still need detail. |
| New session / Clear | PRD rules are retained; confirmations, cancellation and empty restart require completed UX representation and review. |

Named-protagonist journeys and actual user walkthroughs remain to be captured from user input; none are invented by this documentation update. Do not mark UX complete or start the next BMAD phase.

## Responsive & Platform

The selected concept is desktop-first and responsive, with no separate mobile app. Preserve current wrapping navigation, stacked startup fields and simplified/hidden mobile decoration. Broader keyboard/state and usability checks across both sizes remain open; minor visual refinements may follow review.
