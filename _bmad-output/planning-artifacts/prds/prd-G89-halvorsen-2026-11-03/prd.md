---
title: AI Study Buddy — Product Requirements Document
status: final
created: 2026-11-03
updated: 2026-11-14
---

# AI Study Buddy — Product Requirements Document

This PRD defines confirmed v1 requirements. It supersedes earlier product behaviour in the brief and historical research/reviews. Unresolved technical choices appear under Handoff conditions.

## Product purpose

AI Study Buddy helps students reduce study-material preparation and spend more time understanding and practising course content. It is a browser application built as a solo IBE160 project, initially evaluated with the developer's own course material. IBE110 Information Technology is illustrative, not a subject restriction or evidence of usefulness across disciplines.

## Confirmed direction

One temporary study session uses one text-based PDF, one output language (Bokmål or English) and one summary level (Brief or Detailed), chosen before generation. Students request a summary, flashcards or a multiple-choice quiz and inspect original supporting passages. Navigation reuses generated content; changing the PDF, language or level requires a confirmed new session and ordinary startup again.

Source-supported quality takes priority over item count. Unreliable or uncertain main-text coverage stops generation. A labelled saved-content demo runs without private credentials; live generation is evaluated separately. V1 has no public launch or recovery after reload/closing.

## V1 boundaries

All active FRs below are core v1 requirements. Excluded: non-PDF input, accounts/login, cross-device synchronization, permanent study history, learning plans, written-answer assessment, OCR/PDF repair, advanced diagram/complex-table interpretation, advanced statistics, gamified scoring, adaptive learning, spaced repetition and mastery ratings. Failed generation is retried manually, without automatic regeneration or repair calls.

Possible later extensions: language/level changes within an active session, coexisting content variants and browser-saved progress. These are not delivery commitments.

## Glossary

| Term | Meaning |
| --- | --- |
| Study session | Temporary state for one PDF and fixed language/summary level, including acknowledgement, generated content and practice progress. |
| Learning function | Summary, Flashcards or Quiz. |
| Generated content | A summary or a flashcard/quiz set. |
| Set | The ordered cards or questions produced for one learning function. |
| Item | One flashcard or one quiz question. |
| Source reference | PDF filename, physical page and original excerpt associated with generated content. |
| Physical page | File-order position counted from 1, regardless of printed labels. |
| Excerpt | Original text extracted from the uploaded PDF, used to locate and verify supporting information. |

## User journey

### UJ-1: A student understands and revises course material

| Step | Student action | Requirements |
| --- | --- | --- |
| Start | Select a PDF, language and level; acknowledge external processing before generation. | FR-1, FR-4–FR-5, FR-14, FR-43–FR-46 |
| Learn and practise | Request a summary, recall card answers and confirm quiz answers before feedback. | FR-6–FR-10, FR-19, FR-24–FR-33 |
| Verify | Inspect original passages when checking generated content. | FR-11–FR-12, FR-34–FR-37 |
| Continue | Switch functions and resume practice without uploading or generating again. | FR-2–FR-3, FR-13, FR-31 |
| Finish or start again | Confirm Clear or New session; choose a PDF and settings again for another session. | FR-15–FR-18, FR-21 |

## Features and functional requirements

Existing IDs are retained. Shared acceptance rules below apply across learning functions.

### Document input and navigation

- **FR-1 — Upload a study document:** Accept text-based academic PDFs, such as notes, slides, articles and compendia. Reject unsupported formats, damaged files and files without usable text with a detected reason and next step. No-text errors must not claim every such file is a scan.
- **FR-2 — Reuse the uploaded PDF:** Switching learning functions requires no new upload.
- **FR-3 — Retain content and progress:** Function switches preserve generated content and practice progress. Quiz resumption follows FR-13; card answer visibility follows FR-31.
- **FR-38 — Use reliable extracted material:** Use ordinary text and simple table/figure content only when reliably extracted and interpretable with source support. Never reconstruct information available only in an unreadable image.
- **FR-39 — Show processing and failure status:** Display a loading indicator and the operation actually running: Checking PDF, Extracting text, Generating summary, Generating flashcards or Generating quiz. End the indicator on completion/failure. Use no artificial percentage or implication that all functions generate automatically.
- **FR-40 — Disclose incidental omissions:** When unreadable elements are incidental to reliable main text, identify excluded parts in a coverage notice and generate only from readable, verifiable content.
- **FR-41 — Stop on material or uncertain loss:** Stop generation if central/substantial content is unreadable or reliable main-text coverage cannot be established. Explain the detected loss/uncertainty and offer manual retry or another PDF through New session. Observable stop criteria require Architecture verification; detection of every omission is not promised.
- **FR-43 — Reject password-required PDFs:** Reject before generation with a message naming the password problem and suggesting another file. Provide no password-entry or unlocking workflow.

### Study session and output choices

- **FR-14 — Use one active PDF:** A session contains one PDF and fixed output choices, not multiple documents or variants.
- **FR-15 — Confirm a new session:** Before changing the document, explain that the active PDF, content and progress will be lost and request confirmation. Apply the shared session rules below.
- **FR-16 — Confirm Clear:** Explain the same loss before Clear empties the session. Use shared confirmation/cleanup rules; the original device file is unaffected.
- **FR-17 — Explain temporary sessions:** State that reload/closing ends the session. A fresh load restores no PDF, generated content or practice progress. A guaranteed reload/closing warning is not required.
- **FR-18 — Ignore ended-session results:** Late results must neither repopulate an ended session nor appear in another session.
- **FR-4 — Choose output language:** Before generation, select Bokmål or English independently of source language. The choice applies to every learning function for this session; excerpts remain in their original language.
- **FR-5 — Choose summary detail:** Before generation, select Brief (main points/key concepts) or Detailed (fuller explanations and relevant source-grounded examples). Keep that level for the session; it affects neither cards, quiz questions nor wrong-answer explanations.
- **FR-21 — Start a new session for different choices:** Changing language or summary level uses the same confirmed New session flow as changing the document. Return to ordinary startup and select the PDF, language and level again, even for the same file.

Retired IDs: FR-20 (coexisting summary levels), FR-22 (quiz-language reset) and FR-23 (failed language replacement) are replaced by FR-4/FR-5/FR-21 and shared rules. Their former behaviour is not required in v1.

### Summaries

- **FR-6 — Read a structured summary:** Present headings, key concepts and explanations at the selected level. Keep one summary variant in the session.
- **FR-19 — Continue to Quiz:** Provide navigation from Summary to the existing Quiz function, preserving any current attempt. Do not create a separate post-summary question set or mode.

### Flashcard practice

- **FR-7 — Recall before revealing:** Show one card at a time with a term/question on the front and answer on the back. Clicking flips it; every newly displayed card starts on the front.
- **FR-30 — Prioritize card quality:** Normally produce ten cards, fewer with a notice when the source cannot support ten. Cover central concepts, definitions and relationships without unnecessary repetition; every answer is document-grounded and cited.
- **FR-31 — Navigate and resume cards:** Provide forward/back and current/actual-total counts. Returning from Summary or Quiz keeps the position and shows the front.
- **FR-32 — Show sources after recall:** Source references appear only on the back with the answer.
- **FR-33 — Repeat the same cards:** At the end, restart the same set at the first card's front without generation. No mastery ratings or advanced tracking are required.

### Quiz and feedback

- **FR-8 — Test understanding:** Normally produce ten document-based questions, each with four alternatives and one correct answer. Reduced counts follow FR-28/FR-37.
- **FR-24 — Confirm an answer:** Present one question at a time. Selection shows no feedback until explicit confirmation; confirmed answers stay locked for that attempt.
- **FR-9 — Explain incorrect answers:** After confirmation, show correct/incorrect feedback immediately. Wrong answers reveal the correct option, a short explanation of the mistake and correct answer, and source access.
- **FR-25 — Navigate and follow progress:** After feedback, Next question advances. Show current/actual-total progress; earlier questions and confirmed answers remain reviewable and locked.
- **FR-13 — Resume an unfinished quiz:** Returning from another function or closing View source preserves the same position and previous answers.
- **FR-10 — Report the result:** A completed quiz with N ≥ 1 questions and C correct answers shows C, 100 × C / N percent and its incorrectly answered questions. Use actual set size and that attempt's confirmed answers; reviewing does not change the result.
- **FR-26 — Review completion:** After completion, allow review of questions, answers, explanations and sources, including wrong answers.
- **FR-27 — Restart the same quiz:** Restart the same questions without generation, clearing answers/progress/result for a new attempt. No earlier-attempt history is required.
- **FR-28 — Prioritize question quality:** Produce fewer than ten with a notice when the source cannot support ten correct, varied questions. Do not pad with unsupported content or repetition.
- **FR-29 — Adapt the question mix:** Use factual, understanding and simple-application questions as the material supports, without fixed percentages or additional modes.

### Source verification

- **FR-11 — Inspect references:** Display filename, physical page and a short original-language excerpt. Generated translations/paraphrases do not replace the original excerpt.
- **FR-12 — View sources in a sidepanel:** Show those fields and highlight the excerpt. Closing preserves position/progress, including a revealed card answer. No PDF viewer, direct page navigation or highlighting inside the PDF is required.
- **FR-34 — Separate location from support:** A page/excerpt match establishes location, not factual correctness or semantic support. Do not label it factual verification.
- **FR-35 — Cite supporting passages:** Interpretations, simplifications and paraphrases cite original supporting wording. Where several passages contribute, provide their separate inspectable references.
- **FR-36 — Withhold invalid summary references:** Check cited pages and excerpts. Missing/invalid pages, empty/missing excerpts and excerpts not verifiable on the cited page cannot be published as valid references. Any invalid reference withholds the entire new summary; show an error and manual Try again. Do not regenerate automatically.
- **FR-37 — Deliver usable items only:** In an otherwise structurally valid set, omit an entire card/question if any reference is unverifiable, even alongside valid references. Deliver a nonempty valid subset with a notice and actual count; this is a usable result. Zero usable items means error and manual Try again. Do not fill the set automatically. Malformed structures follow NFR-3.

### Material handling and external processing

- **FR-44 — Explain external processing:** Before first generation, visibly explain that extracted PDF text goes to an external AI service. Tell students to exclude sensitive personal data, confidential material and content not permitted for external sharing. A privacy-policy-only notice is insufficient.
- **FR-45 — Require current-upload acknowledgement:** Block every extracted-content transfer to external AI, including external checks, until active acknowledgement of FR-44. Each accepted upload requires it, even for the same file. Function switches and manual retries in the same session reuse it; an ended session does not.
- **FR-46 — Support provider claims:** Claim no storage, no training use or automatic deletion only when documented and upheld by the selected service/configuration. App cleanup does not imply provider deletion. Verify terms and configuration before real transfer.

### Demo and live validation

- **FR-42 — Run a labelled key-free demo:** Supply one shareable predefined PDF and saved summaries at both levels plus card/quiz sets in both languages. Startup selects the session's language/level; load only matching saved content. Different choices require New session. Core learning/source flows run from README without private keys or paid accounts. Label playback as demo; own PDFs/fresh generation require live mode. Explain unsupported actions. Apply the same content/source rubric to demo content and validate live integration separately.

### Shared acceptance rules

| Trigger | Required outcome |
| --- | --- |
| Cancel New session or Clear confirmation | Keep the active PDF, choices, acknowledgement, content and progress unchanged. |
| Confirm New session or Clear | Remove that session's working state and show ordinary startup. New session requires PDF/settings selection and fresh acknowledgement. Cancelled file selection or a rejected file after confirmation leaves startup empty; never restore the ended session. Original device files are unchanged. |
| Missing live key, unavailable AI service, timeout, failed generation, invalid structure or no usable content | End processing with a reason and next action: setup, manual Try again or another PDF as applicable. Preserve existing valid content/progress in the active session. Show neither fabricated success nor an empty scored quiz. |
| Valid reduced set | Show usable items, actual total and omission notice. Nine valid items out of ten means nine, without automatic refill. |

Failed attempts never trigger automatic regeneration/repair; another attempt requires the student's Try again action. Source/structure checks precede publication. Navigation and restarting an existing set do not generate content. With eight quiz questions and six correct answers, the result is 6/8 and 75%, with two wrong questions listed.

## Cross-cutting security requirements

Implement these boundaries and their negative checks during Architecture and development.

- **NFR-1 — Separate content from authority:** PDF/model content is study data and cannot change app rules, settings or actions. Give the model no shell, arbitrary-file or URL-fetch tools.
- **NFR-2 — Render untrusted content inertly:** Text, excerpts and filenames cannot execute HTML/scripts, load remote images automatically or trigger external requests. Safe headings, emphasis and lists are allowed.
- **NFR-3 — Validate generated structures:** Check required fields, types, lengths, four-option structure, answer keys and app-owned source locations. Reject malformed replies as a whole using shared failure rules. FR-37 filtering applies only to otherwise valid structure.
- **NFR-4 — Protect credentials:** Keep private credentials out of PDF/model content, browser-delivered code and exposed errors/payloads. Apply content/rendering boundaries to demo content too.
- **NFR-5 — Bound working data:** No permanent history of ordinary PDFs, extracted text or generated content. Clear/New session removes app-owned working copies; other ended sessions have an Architecture-defined/tested cleanup deadline. Exclude study material from ordinary app/SDK/error logs. Deliberately saved permitted evaluation/demo evidence has separate owner, access and review/deletion conditions. Provider retention follows FR-46.

## Validation plan and success measures

Selected files remain local under `test-data/pdfs/`, ignored by Git; paths below are relative to repository root.

| Test document | Physical pages | Material |
| --- | --- | --- |
| T1 — `test-data/pdfs/T1.pdf` | 10 | English cybersecurity lecture slides, labelled IBE321. |
| T2 — `test-data/pdfs/T2.pdf` | 24 | Own Norwegian strategic-management notes. |
| T3 — `test-data/pdfs/T3.pdf` | 40 | Own English Information Technology notes. |

These are test inputs, not upload limits or public demo assets. A limited local PDFKit inspection confirmed text on all 74 pages and physical page counts, but found omitted/fragmented figure content, including T2 page 12 and T3 page 30. It neither selects the app's parser nor establishes complete coverage or AI quality.

The following app checks remain planned. Set expected readable/omission/stop outcomes before testing. A controlled stop can pass failure handling, never content quality; record blocked/failed quality cases rather than claiming every PDF completes generation.

- **SM-1 — Summary coverage:** Plan 12 cases: T1–T3 × both languages × both levels, each in a separate session. Apply the manual accuracy/coverage protocol to generated summaries; formatting alone does not pass. Validates FR-4–FR-6.
- **SM-2 — Card quality:** Across six document/language cases, require at least 9/10 correct reviewed answers per case; inspect all and require all to pass for smaller sets. Validates FR-7/FR-30.
- **SM-3 — Quiz quality:** Across six document/language cases, require at least 9/10 correct, unambiguous keys per case; all must pass for smaller sets. Validates FR-8/FR-9/FR-29.
- **SM-4 — Reference support/location:** Per case, at least 9/10 reviewed references support associated content; all pass if fewer. Every displayed location exists. On the same sampled card/question, require joint answer-correctness/source-support passes for at least 9/10, or all if fewer. Report separate and joint results; location checks do not replace human support review.
- **SM-5 — Function/failure behaviour:** Check wrong-answer feedback in every tested case, navigation/results/restart, cancelled/confirmed New session and Clear, fresh acknowledgement, manual retry, late results, source/structure failures and unusable PDFs. Validate key-free demo and live integration separately. Correct/retest known defects regardless of numerical passes.
- **SM-6 — Preparation effort/usefulness:** Compare equivalent manual/app-assisted tasks, including review, correction and failed attempts. Record usefulness/corrections and familiarity/order effects. Fix the task and a provisional timing target before full evaluation; no achieved savings or learning gains are established.

### Manual evaluation protocol

1. Review every summary factual claim against the original PDF, not just extracted text. No unresolved factual error, unsupported addition or unclear judgment passes. Check language, organization, relevance, repetition and level.
2. Before viewing outputs, map five Brief core points and ten Detailed eligible points to sources. Brief covers all five; Detailed covers those five plus at least three additional points. Fix smaller lists/thresholds for short sources before scoring. Pilot before full evaluation.
3. Review the same card/question for correctness and SM-4 support. With multiple references, check each location/excerpt and combined support for required claims. Freeze item/reference sampling and counting before scoring.
4. Preserve first outputs, failed attempts, omitted items, original defects, corrections and retests for permitted files. Select samples before quality review; report per-case results without pooling away failures.
5. The developer freezes source points, sampling/counting and SM-6 tasks/target after the T1 evaluation pilot, before full scoring. The earlier extraction inspection does not replace that pilot.

## Handoff conditions

| Owner | Open work | Resolve before |
| --- | --- | --- |
| Architecture | Stack, model/PDF library, provider terms/configuration, input/context/resource/time/cost bounds and working-copy cleanup deadline. Flag limits excluding selected test files; preserve no automatic regeneration. | Implementation depends on each choice; provider verification before real transfer. |
| Architecture | Observable extraction stop criteria, page-local excerpt matching/normalization and negative fixtures, including missing figures, blank pages and unusable PDFs. No universal coverage detector is assumed. | Accepting the extraction/source pipeline. |
| Developer/evaluation | Separate shareable demo PDF; local/API/demo/repository permissions; source points, sampling/counting and timing task/target. | Relevant material use and full scoring. |
| Developer/delivery | Original assignment/full rubric and exact deadline; UX, README, reflection and test evidence. | Delivery planning and acceptance. |

See [the addendum](addendum.md) for technical/evidence follow-ups. Unadopted research proposals are not requirements.

## Existing inputs

- [Product brief](../../briefs/brief-G89-halvorsen-2026-09-26/product-brief.md)
- [Brief addendum](../../briefs/brief-G89-halvorsen-2026-09-26/addendum.md)
- [Brief feedback](../../briefs/brief-G89-halvorsen-2026-09-26/tilbakemelding-product-brief.md)
- [PRD feedback](tilbakemelding-prd.md)
- [PDF source reliability research](../../research/technical-pdf-source-reliability-2026-10-29/research.md)
- [Quality/evaluation research](../../research/technical-quality-evaluation-2026-11-02/research.md)
- [Uploaded-material handling research](../../research/technical-uploaded-material-handling-2026-11-02/research.md)
- [AI security notes](../../research/ai-security-notes.md)
