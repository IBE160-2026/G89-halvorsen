---
name: AI Study Buddy
status: final
planning_status: complete
created: 2026-11-14
updated: 2026-11-24
finalized: 2026-11-24
concept: selected
sources:
  - ../../prds/prd-G89-halvorsen-2026-11-03/prd.md
  - ../../prds/prd-G89-halvorsen-2026-11-03/addendum.md
  - decisions.md
---

# AI Study Buddy — Experience

## Foundation

**Complete for UX planning, 24 November 2026**, following user acceptance and the consolidated PRD/flow check. The selected concept includes empty/active Home, Summary, complete Flashcards/Quiz/source flows, shared processing/error/notice patterns and the Round 21 mobile treatment. Minor implementation refinements are allowed. [DESIGN.md](DESIGN.md) owns visual identity; the PRD/addendum govern product behaviour. [The final report](validation-report.md) records closure, evidence and nonblocking follow-up. This is no claim of a production-ready app or completed user study.

The desktop-first responsive web application has an **English interface throughout**, with no interface-language switch. Startup separately fixes **Norwegian Bokmål** or **English** for all generated study material and **Brief** or **Detailed** for Summary only. Original filenames/source excerpts keep their original language. PDF, language and detail cannot change within the active session.

## Information Architecture

One shared top menu contains Home, Summary, Flashcards and Quiz. Without an active session, Home has upload/settings and learning tabs are unavailable in the actual app. With an active session, Home has document/settings information, Continue studying and New session. Navigation preserves content/progress and never generates content on its own. Continue returns to the last learning tab, initially Summary; Flashcards returns to its existing position with the answer hidden, while Quiz keeps position, draft selections and confirmed answers.

[Promoted references](mockups/ux-overview.html) cover the full planned interaction. [Selected shell](mockups/selected-shell.html) preserves the illustrated Home/basic one-question sample. [Complete learning flow](mockups/complete-learning-flow.html) is the reference for full practice, result/review/restart and multiple sources; [reliability states](mockups/reliability-states.html) and [processing states](mockups/processing-states.html) define the other outcomes. These are complementary parts of one concept. Review tools and prewritten samples remain labelled outside normal product flows. The basic shell can open an inspection example before first startup; that is a prototype shortcut, not a production permission to study without a session. Ended examples cannot be revived by navigation/host state.

## Voice and Tone

Use concise, direct English and sentence case. Keep **Summary**, **Flashcards**, **Quiz**, **Norwegian Bokmål**, **English**, **Brief** and **Detailed** consistent. Interface feedback labels stay English; generated explanations use the fixed study language.

Explain what could not be read/created, what remains available and the next action. Use **Flashcards could not be created** / **Quiz could not be created**, a short explanation and **Try again** where retry can help. Technical schemas, reason codes, provider keys and source-validation mechanics remain internal. Name only a known PDF condition; no usable extracted text does not establish that a PDF is scanned. A located source does not verify factual support or complete coverage.

Keep essential external-processing information, sharing restrictions, active acknowledgement and temporary-session explanation visible. Make no unsupported provider-storage/deletion/training promise. Use “concept” for preliminary variants, retaining BMAD filenames.

## Component Patterns

| Component | Behavioural contract |
| --- | --- |
| Navigation | Switch among existing session views; preserve accepted material and practice. Learning links require an active session in production. No automatic generation. |
| Empty Home | Select one PDF and fixed output language/Summary detail. Generate Summary stays disabled until choices and active per-upload external-processing acknowledgement exist. No external checking/transfer before acknowledgement. |
| Active Home | Show filename and locked choices. Continue studying opens the last learning tab with progress; New session opens the shared confirmation. |
| Summary | Show the one selected level, clear headings/prose and inspectable references. The route to Quiz opens its existing attempt. Reading uses `{typography.summary.fontSize}` / `{typography.summary.lineHeight}` and the measure in DESIGN.md. |
| Flashcards | Show one front/back card and actual count. Source access only on its answer. Previous/Next changes the card and shows its front. Return from another function hides the answer; closing a source keeps the revealed answer. End/restart repeats the same accepted set without generation. |
| Quiz | Four alternatives with one correct answer. Selection alone gives no feedback. Explicit Confirm locks the answer and shows correctness; incorrect answers have a short generated explanation/source access. Next follows feedback; previous confirmed answers remain reviewable and immutable. Unconfirmed draft choices and current position survive navigation. |
| Quiz result/review | Use C/N and 100×C/N, where C is the number of correct answers and N is the accepted question count; list wrong questions. Review never changes confirmed answers or the result. Restart clears only this attempt, reusing the same questions with no generation. Never score an empty quiz. |
| View source | Show filename, physical page and highlighted original-language excerpt; separate contributing passages remain individually inspectable. Opening/closing preserves learning position, answer state and progress. Close/Escape returns focus to the invoking control. This is an excerpt reader, not a PDF viewer or factual verification badge. |
| New session dialog | The only explicit session-ending action, visible beside document information on learning tabs and on active Home. Cancel/Escape preserves all and restores trigger focus. Confirmation clears session data/progress, ignores ended-session results and returns to ordinary empty Home. The original device file is unaffected; starting again is optional. A later session requires fresh PDF/settings/acknowledgement. No separate Clear. |
| Processing / error card | One reusable status surface. Name the actual operation; show a short problem/recovery when failed. Manual retry targets the failed operation and retains accepted content/progress. Missing setup uses the same generation-error surface with an available-material route; retry cannot fix configuration. |
| Usable-content notice / demo information | A nonblocking notice accompanies accepted but limited material, with actual count or known omission. Demo information labels saved material and explains own-PDF/fresh-generation live requirements. Neither is presented as a blocking error or verified-quality claim. |

## State Patterns

| State | Planned outcome |
| --- | --- |
| Empty / incomplete startup | Clear upload and choices, unchecked acknowledgement, disabled Generate Summary; rejected input cannot restore an ended session. |
| Active session | One PDF and locked choices; navigation/active Home preserve valid material and progress. Reload/close ends the temporary session in production. |
| Processing | Use exactly Checking PDF, Extracting text, Generating summary, Generating flashcards or Generating quiz for the actual operation. No fake percentage, time estimate or automatic retry. End the indicator on real completion/failure. Review retries remain pending instead of fabricating success. |
| Document error | Reject unsupported/damaged/password/no-usable-text input before generation. Offer confirmed New session/another PDF; no password entry, unlocking, OCR or repair. Material loss/uncertain extraction stops generation and can offer manual retry. |
| Generation error | Reject the failed new response; preserve any accepted Summary, cards, Quiz and progress. Offer manual Try again where useful and access to other ready functions. Never clear accepted content merely because retry begins. |
| Usable limited content | Show a known nonessential omission only when main text is usable. For otherwise valid card/Quiz output, omit each whole item with any invalid reference; show a nonempty accepted subset and its actual count. No repair/refill. |
| Completely rejected output | Malformed structures reject the whole reply. Any invalid new Summary reference withholds the whole new Summary. Zero valid cards/questions produces a failure, not partial invalid content or an empty scored quiz. |
| Saved demo | Clearly labelled prewritten material works without private keys/paid accounts and matches the selected language/level. Own PDFs/fresh generation need live setup; explain this without adding an app mode switch or credential form. |
| Ended session | Empty Home, no old content/progress revival, new upload/choices/acknowledgement before starting again. Late results must not repopulate it. |

The 17 [internal scenarios](.working/reliability-scenarios.md) reuse four outcome patterns plus processing: 13 errors, three usable-content notices and one demo-information case. They are test inputs, not 17 product features. Source-location filtering only applies to otherwise valid structures; location matching does not establish factual support. PDF coverage examples supply known test signals, not a working universal detector. Observable extraction/stop rules and source matching remain technical implementation decisions; advanced figure interpretation is out of scope.

## Interaction Primitives

Use labelled native file/select/checkbox/radio/button controls and natural keyboard order. Keep visible function-themed focus, explicit answer confirmation, labelled status feedback and reduced-motion canvas transitions. New session and source dialogs contain focus while open, support Escape and return focus to their actual trigger; Continue moves focus to its visible destination. Do not hide required actions behind hover. Manual retry never repairs, refills or repeats automatically.

## Accessibility Floor

Apply DESIGN.md contrast targets and role tokens: `{colors.ink}` / `{colors.secondary-ink}` on appropriate surfaces, labelled outcomes in addition to colour, and visible 3px focus. Keep effective touch targets at least 44×44px, native labels, status announcements and meaningful names. Decorative illustrations/logo icons are hidden from assistive technology. Preserve reading order, original excerpt language and usable reflow at 320px; verify zoom, long text and assistive technology in the built app.

Automated browser/keyboard and visual checks are recorded in [the final report](validation-report.md). Actual observed user research, a full screen-reader/accessibility audit and real-device checks have not been completed. They remain implementation/evaluation follow-up, not evidence invented for planning closure.

## Key Flows

### UJ-1: A student understands and revises course material

Camilla, a student preparing for revision, wants to turn one course PDF into readable material, practise recall and check an explanation against the original passage. Her reported preferred order is Summary → Quiz → Flashcards; the shared navigation also supports Summary → Flashcards → Quiz without losing progress.

1. On empty Home, Camilla selects one PDF, Norwegian Bokmål or English, and Brief or Detailed. She reads the external-AI/material/temporary-session information and actively acknowledges this upload before Generate Summary becomes available.
2. The app names the operation actually running. A document problem stops generation with a clear next action; material loss/uncertain main-text coverage also stops rather than presenting an uncertain result as complete. Known nonessential omissions can accompany usable material with a short notice.
3. Camilla reads the selected-level Summary. She opens its original-language source passage, checks the physical page/excerpt and closes it without losing her place. A page match helps locate evidence; she must still judge whether it supports the explanation.
4. She opens Quiz and requests it once for the session. She selects an answer, explicitly confirms it, then receives feedback. **The central verification moment:** after a wrong answer she opens the separate contributing source passages and compares them with the explanation, then resumes the same locked attempt. A failed generation offers manual retry without losing Summary or other progress.
5. She completes the accepted questions, sees actual C/N and percentage, reviews wrong answers without editing the result, and may restart the same set. An empty/invalid new set is withheld entirely; a valid reduced set uses its real denominator and a notice.
6. She practises Flashcards one at a time, recalls before flipping, inspects answer-side sources and moves through the same set. Function return keeps card position and shows the front; source close keeps a revealed answer. Completion can restart the same accepted cards without generation.
7. She visits Home to see the fixed document/settings, then Continue studying returns to her last learning tab with content/progress. Language/detail changes require New session rather than editing the active session.
8. When finished, she chooses New session. Cancel/Escape preserves her work; confirmation removes session content/progress and returns to empty Home, leaving her device file untouched. She may stop there or later select a fresh PDF/settings/acknowledgement.

This is a specified journey and automated prototype walkthrough, not a claim that Camilla performed an observed usability test. [Coverage inventory](.working/ux-coverage-review.md) connects each surface and applicable failure branch to its visual reference and evidence. Demo/live limitations follow the same startup/choice rules; permitted demo assets and their content evaluation remain to be prepared under FR-42.

## Inspiration & Anti-patterns

Keep Notatkort's calm reading/card structure, Atlas's separate rounded answers and [the supplied illustrated Home reference](imports/front-page-reference.png). Quizlet informs recall practice only. Avoid crowded screens, duplicate Clear/New session, gamification, excessive animation, technical error jargon and unsupported source/privacy claims. Preserve the app's selected identity.

## Responsive & Platform

Use the same responsive web application on desktop/mobile. Startup fields/actions stack and decoration simplifies on narrow screens. At app widths up to 540px centre Flashcards/Quiz boxes, notices/actions and short processing/error surfaces, while Summary reading/notices and source excerpts retain left alignment. Keep desktop placement. The selected canvas tokens `{colors.summary-canvas}`, `{colors.flashcards-canvas}` and `{colors.quiz-canvas}` identify function alongside text/active tabs.

Planning closure selects these rules and references. Actual generation/extraction, quality, permitted demo material, production cleanup/late-result isolation, full accessibility and observed usability remain required follow-up. No architecture phase, production implementation, commit or push is started here.
