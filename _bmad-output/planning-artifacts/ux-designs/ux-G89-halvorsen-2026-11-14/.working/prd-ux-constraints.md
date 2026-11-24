# AI Study Buddy — PRD constraints for UX concept exploration

Sources: [final PRD, updated 2026-11-19](../../../prds/prd-G89-halvorsen-2026-11-03/prd.md) and [final addendum](../../../prds/prd-G89-halvorsen-2026-11-03/addendum.md).
This is an extraction for this existing UX run, not a new specification or adopted visual direction. The PRD governs product behaviour; earlier research and retired requirements do not override it.

## Session and startup — required behaviour

- **FR-1, FR-14:** One text-based academic PDF per temporary session. Accept notes, slides, articles and compendia in that format; no multiple-document workspace.
- **FR-4:** Select one output language, Bokmål or English, before generation. It applies to all learning functions independently of the PDF language. Original excerpts keep their original language. This does not prescribe the UI's language.
- **FR-5, FR-6:** Select one summary level, Brief or Detailed, before generation. Only one summary variant exists in that session. The level does not change cards, quiz questions or wrong-answer explanations.
- **FR-44, FR-45:** Before external processing, visibly explain that extracted PDF text goes to an external AI service; exclude sensitive, confidential or externally unshareable material. Active acknowledgement is required for each accepted upload before any external transfer, including checks. Same-session navigation/retries reuse it.
- **FR-46:** No unsupported promises about provider storage, training or deletion. App cleanup does not imply provider deletion.
- **FR-17:** Explain that reload/closing ends the session and restores no PDF, content or progress. A guaranteed browser-leave warning is not required.
- **FR-15, FR-21:** New session is the sole explicit session-ending action and requires confirmation explaining loss of the PDF, generated content and progress. Confirmation gives empty ordinary Home; the student may stop there. Changing PDF, language or level requires starting again with fresh PDF/settings selection and acknowledgement, even for the same file. FR-16, the duplicate separate Clear action, is retired.
- **Shared acceptance rules:** Cancelling confirmation preserves the entire active session. Confirming empties it; cancelled/rejected subsequent file selection leaves startup empty, without restoring the ended session. The original device file is unaffected.
- **FR-18:** Late results from an ended session cannot repopulate it or enter another session.

## Navigation and learning functions — required behaviour

- **FR-2, FR-3:** Summary, Flashcards and Quiz reuse the PDF, generated content and practice progress. Navigation does not upload or generate again.
- **FR-6:** Summary uses headings, key concepts and explanations at the session's chosen level; Detailed may contain fuller source-grounded explanations/examples.
- **FR-19, FR-13:** Summary provides a route to the existing Quiz, preserving any current attempt. No additional post-summary question set or mode.
- **FR-7:** Show one flashcard at a time; front has a term/question and back has its answer. Clicking flips it. Every newly displayed card starts on its front.
- **FR-30, FR-31:** Normally ten source-grounded, nonrepetitive cards; fewer with a notice if necessary. Provide back/forward and current/actual-total count. Returning from Summary/Quiz retains card position and shows the front.
- **FR-32:** Flashcard references appear only on the back with the answer; do not disclose them on the front.
- **FR-33:** Restart repeats the same set at the first front without generation; no mastery ratings or advanced tracking.
- **FR-8, FR-24:** One quiz question at a time, four alternatives and one correct answer. Selecting an option reveals no feedback until explicit confirmation. Confirmed answers stay locked for that attempt.
- **FR-9:** After confirmation, show immediate correct/incorrect feedback. Wrong answers reveal the correct option, a short explanation and source access.
- **FR-25, FR-13:** Next question follows feedback. Show current/actual-total count. Earlier questions/confirmed answers remain reviewable and locked; function switches and closing View source retain position and prior answers.
- **FR-10, FR-26:** Completion with N >= 1 shows correct count C, percentage 100*C/N and incorrectly answered questions. Questions, answers, explanations and sources remain reviewable; review does not change the result.
- **FR-27:** Restart repeats the same questions without generation and clears the current attempt's answers/progress/result; no earlier-attempt history is required.
- **FR-28, FR-29:** Normally ten varied questions; fewer with a notice when needed. Use factual, understanding and simple-application questions where supported; no fixed mixture or extra modes.

## View source — required behaviour

- **FR-11, FR-12:** Use a sidepanel showing PDF filename, physical page counted from 1 and a short original-language excerpt, with the excerpt highlighted. Closing preserves position/progress, including a revealed card answer.
- **FR-12:** A PDF viewer, direct PDF-page navigation and highlighting inside the PDF are not required. The panel's original excerpt is sufficient for the specified source-view interaction.
- **FR-34:** A matching page/excerpt establishes location, not factual correctness or semantic support. Avoid “fact verified” claims or equivalent certainty badges.
- **FR-35:** Where several passages contribute, each source reference must be inspectable. Generated translations/paraphrases do not replace original wording.

## Processing, errors and partial results — required behaviour

- **FR-39:** Show a loading indicator and the actual operation: Checking PDF, Extracting text, Generating summary, Generating flashcards or Generating quiz. End processing on success/failure. No fabricated percentage or implication that all functions generate automatically.
- **FR-1, FR-43:** Reject unsupported formats, damaged files, no-usable-text PDFs and password-required PDFs with the detected reason and a next action. No password-entry/unlocking flow; no claim that every no-text PDF is scanned.
- **FR-38, FR-40:** Use only reliably extracted/interpretable text and simple table/figure content. Incidental excluded elements require a coverage notice identifying omissions; never reconstruct unreadable image information.
- **FR-41:** Stop when central/substantial content is unreadable or reliable main-text coverage is uncertain. Explain the loss/uncertainty; offer manual retry or another PDF through New session. No promise to detect every omission.
- **FR-36:** Any invalid summary reference withholds the whole new summary; show an error and manual Try again.
- **FR-37, NFR-3:** In an otherwise structurally valid card/quiz set, omit a whole item if any reference is unverifiable. A nonempty valid subset is usable: show actual count and omission notice. Zero usable items is an error. Reject malformed model structures as a whole.
- **Shared acceptance rules, addendum:** Missing key, unavailable service, timeout or generation/validation failure ends processing with reason and setup/manual Try again/another-PDF action as appropriate. Preserve existing valid content/progress in the active session; never restore an ended one.
- **Shared acceptance rules:** No automatic regeneration, repair or item refill. Retry requires the student's action. Never show fabricated success or an empty scored quiz. Eight questions/six correct means 6/8, 75%, two wrong questions.

## Demo and security — required behaviour

- **FR-42:** A labelled key-free demo uses one separately shareable predefined PDF, saved summaries at both levels and card/quiz sets in both languages. Load only the startup-selected language/level; changing choices still requires New session.
- **FR-42:** Demo supports core learning/source flows without private keys or paid accounts. Own PDFs/fresh generation need live mode; explain unsupported demo actions. Saved playback must not pretend to be live AI generation.
- **NFR-1, NFR-2:** PDF/model content is study data, never app authority. Render text/excerpts/filenames inertly, with no script execution or automatic remote-image/external requests. Safe headings, emphasis and lists are allowed.
- **NFR-3, NFR-4:** Validate structures before publication and protect credentials from browser code, content, errors and exposed payloads. Apply the same boundaries to demo content.
- **NFR-5:** No permanent ordinary-PDF/content history. Confirmed New session removes app-owned working state; other cleanup deadlines are Architecture work. Keep study material out of ordinary logs. Provider retention is separate.

## Fixed boundaries and open choices

- **PRD V1 boundaries:** No non-PDF input, accounts/login, cross-device sync, permanent history, learning plans, written-answer assessment, OCR/PDF repair, advanced diagram/complex-table interpretation, advanced statistics, gamified scoring, adaptive learning, spaced repetition or mastery ratings. No public launch or reload recovery in v1.
- **Retired FR-20, FR-22, FR-23:** Do not reintroduce coexisting summary levels, in-session language replacement or its old recovery flows. FR-4/FR-5/FR-21 and shared rules replace them.
- **Addendum / Handoff conditions:** Stack, model/parser, provider configuration, resource/time/cost/upload bounds, cleanup deadline and extraction/matching algorithms are unresolved. T1–T3 are local test inputs, not public demo assets or numeric upload limits. Do not invent such limits in concepts.
- **Addendum UX follow-up:** Cover startup, navigation, source panel, warnings and wrong-answer flow; check keyboard use, readability and source-location/support wording. This extraction does not claim those checks passed.
- **Appearance is a UX decision:** The PRD does not select palette, fonts, radii, density, visual hierarchy, navigation topology, component library, imagery, animation or theme support. The user has now selected the latest Home/Summary/Flashcards/Quiz concept in [decisions.md](../decisions.md); UX planning is complete under the final peer contracts and Round 22, with minor implementation refinements possible without changing the required behaviours or exclusions.
- **Concept fidelity:** Concept content and simulated transitions are illustrations, not implementation, live-generation, source-quality or usability-test evidence. Existing UX decisions remain in this run's memlog; no concept is adopted merely by rendering it.
