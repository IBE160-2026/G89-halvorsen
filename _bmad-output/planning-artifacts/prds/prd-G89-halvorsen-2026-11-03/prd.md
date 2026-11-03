---
title: AI Study Buddy — Product Requirements Document
status: final
created: 2026-11-03
updated: 2026-11-03
---

# AI Study Buddy — Product Requirements Document

This PRD defines AI Study Buddy's confirmed v1 requirements and acceptance criteria. Later decisions recorded here supersede the product brief; staged technical and evaluation work appears under Handoff conditions.

## Product purpose

AI Study Buddy helps students spend less time extracting key information and preparing study aids, leaving more time to understand and practise course material. It is a simple browser application for independent study, built as a solo IBE160 project and evaluated first with Camilla's own course material.

The app supports study material across disciplines; IBE110 Information Technology is an illustrative situation, not a subject restriction. This intended scope does not establish general learning gains or universal PDF coverage.

## Confirmed direction

V1 turns one text-based academic PDF into summaries, flashcards and a multiple-choice quiz in Bokmål or English, independently of the source language. Students inspect original passages through page-and-excerpt references and move among learning functions without repeated uploads.

The defining tradeoffs are a temporary study session without recovery after reload, source-grounded quality over item count, and conservative failure when content cannot be read or referenced reliably. A labelled saved-data demo demonstrates the core flows without private credentials; live generation is validated separately. There is no public launch in v1.

## V1 boundaries

Excluded: non-PDF input such as `.txt`, accounts/login, cross-device synchronization, automatic permanent study history, learning plans, written-answer assessment, OCR/advanced PDF repair, advanced diagram/complex-table interpretation, advanced statistics, gamified scoring, adaptive learning, spaced repetition and mastery ratings. Browser-saved progress is only a possible later extension after the tested core.

## User journey

### UJ-1: Camilla understands and revises course material before an exam

Camilla is preparing for an IBE110 exam in this example. She uploads a text-based PDF readable without a password. Before first generation for that upload, she actively acknowledges the visible notice about external AI processing and material restrictions.

1. She chooses Bokmål or English and a summary level. She starts with Detailed for understanding, reading headings, key concepts and explanations with source references.
2. She practises concepts and relationships with flashcards, attempting each answer before flipping to its answer and source. She moves forward/back through the set and follows its current/total counter. Returning from Summary or Quiz keeps her card position but hides the answer. She can repeat the same set.
3. From Summary she enters the existing quiz. For each four-option question, she selects and confirms an answer before immediate feedback. Incorrect answers show the correct option, an explanation and source access. She advances with Next question or reviews earlier locked answers. Completion shows her correct count, percentage and list of incorrectly answered questions; she can review explanations/sources and restart the same questions.
4. When uncertain, she opens View source: a sidepanel with filename, physical page and highlighted original excerpt, with multiple references when needed. Closing it preserves her place and progress.
5. She switches among learning functions without re-uploading or losing generated content. An unfinished quiz resumes with its position and previous answers. Later she generates Brief for revision; both summary levels then remain available without regeneration.

Cards and quizzes normally contain ten items, fewer with a notice when source-supported quality limits the set. Language changes follow FR-20–FR-23 and FR-31: confirmation and successful generation commit replacement; failure preserves prior work. Camilla moves from reading to understanding, recall and self-assessment using the same document.

## Features and functional requirements

### Document session and navigation

- **FR-1 — Upload a study document:** Accept text-based academic PDFs: lecture notes, syllabus articles, compendia and teaching material, primarily continuous text, headings, paragraphs and bullets. Simple tables/figures follow FR-38. For unsupported or non-PDF files, damaged files and files without usable text, show an understandable message explaining the problem and next step; rejected replacements follow FR-15.
- **FR-2 — Reuse the uploaded PDF:** Use the same PDF for summaries, flashcards and quizzes without another upload when switching functions.
- **FR-3 — Retain content and progress during navigation:** Preserve generated content and practice progress, including previous quiz answers, across function switches within the active session. Quiz resumption follows FR-13; card position/answer visibility follows FR-31.
- **FR-38 — Use only reliable extracted material:** Use ordinary text and only simple table/figure content that can be extracted and understood reliably with source support. Never invent information available only in an uninterpretable image. OCR, advanced diagrams/complex tables and PDF repair remain outside v1. Partial coverage follows FR-40–FR-41.
- **FR-39 — Show truthful processing status:** Show a visible loading indicator and a short status for the operation actually running: Checking PDF, Extracting text, Generating summary, Generating flashcards or Generating quiz, as applicable. Do not imply all aids generate automatically or show percentage progress without reliable measurement. Explain failures clearly.
- **FR-40 — Disclose incidental omissions:** Readable main text may support generation when unreadable elements, such as figures or complex tables, are incidental. Clearly disclose excluded parts and generate only from readable, verifiable content.
- **FR-41 — Stop on material or uncertain extraction loss:** Stop if substantial/central content is unreadable or adequate reliable main-text coverage cannot be established. Explain the problem/uncertainty and offer retry or another PDF. Never assume missing material is unimportant, reconstruct it or infer unavailable subject matter. FR-15 protects rejected replacements. Architecture defines observable stop criteria and tests representative cases without claiming detection of every omission.
- **FR-43 — Reject password-protected PDFs:** Accept only PDFs readable without a password. Explain password-required rejection and offer another file; do not remove protection or provide password/unlocking workflows. Preserve an existing session under FR-15.

Boundary checks: readable main text with incidental omissions can produce grounded aids with a coverage notice; uncertain main-text coverage must stop. Non-PDF, damaged, no-usable-text and password-required fixtures exercise controlled rejection without erasing prior work. No-text errors must not falsely identify every such document as a scan.

### Study-session lifecycle

An active study session contains the PDF, its external-processing acknowledgement, generated aids and practice progress. Accepted replacement, confirmed Clear, reload or closing ends it.

- **FR-14 — Use one active PDF:** Work with one PDF at a time; an accepted replacement starts a new session, not a second document.
- **FR-15 — Confirm document replacement:** Explain the loss of the current document, aids and practice progress before asking for confirmation. Cancellation or rejected replacement preserves the current session. Accepted replacement starts without old content/progress.
- **FR-16 — Confirm clearing a study session:** Explain what will be lost and require confirmation before Clear removes the active document, aids and practice progress. Cancellation preserves them. The original device file is unaffected.
- **FR-17 — Communicate temporary sessions:** Clearly explain that the session is not saved for recovery. Reload/closing ends it; a fresh load restores no PDF, aids or practice progress. A guaranteed closing/reload warning is not required.
- **FR-18 — Keep ended sessions ended:** Results arriving after replacement or Clear must not repopulate the ended session or appear in the new one.

App cleanup does not imply provider deletion; FR-46 governs that distinction.

### Material handling and external processing

- **FR-44 — Explain external processing before generation:** Before first generation for an upload, visibly explain in short, plain language that extracted PDF text goes to an external AI service for summaries, cards and quizzes. A privacy-policy-only notice is insufficient. Tell students not to upload sensitive personal data, confidential material or content not permitted for external sharing.
- **FR-45 — Require acknowledgement for the current upload:** Gate all extracted-content transfer to external AI, including external checks, on active acknowledgement of FR-44. Each accepted upload requires its own acknowledgement. Cancelled/rejected replacement retains it; same-upload function switches, language changes and retries reuse it. Clear/reload/closing ends it.
- **FR-46 — Make only supported provider claims:** Claims of no storage, no training use or automatic deletion must be documented and technically upheld in the actual service/configuration. Clear must not imply provider deletion. Architecture selects the provider; verify its terms, retention and configuration before real transfer.

Boundary checks: accepted replacement requires a new acknowledgement even when filenames match; cancelled/rejected replacement preserves the old one. Same-upload language retries retain acknowledgement but still require FR-21's separate replacement confirmation. Saved demo playback need not transfer PDF text and must not imply live generation.

### Output language and summaries

- **FR-4 — Choose output language:** Choose Bokmål or English before generation, independently of source language. Existing-content changes follow FR-21–FR-22.
- **FR-5 — Choose summary detail:** Brief covers main points/key concepts; Detailed adds fuller explanations and relevant source-grounded examples. Levels affect summaries only, not cards, quizzes or wrong-answer explanations. FR-20 governs retention.
- **FR-6 — Read a structured summary:** Present clear headings, key concepts and explanations for understanding/revision.
- **FR-19 — Continue from a summary to Quiz:** Navigate easily to the existing quiz using the active PDF, preserving any existing quiz under FR-3/FR-13. Provide no separate post-summary comprehension questions, set or quiz mode.
- **FR-20 — Keep both summary levels:** Once generated in the current summary language, Brief and Detailed coexist during the session; switching needs no generation. After a confirmed language change, the first successfully generated summary at the requested level replaces both old-language summaries. The other level can then be generated in the new language. Cards/quiz are unaffected.
- **FR-21 — Confirm replacement on language change:** Explicitly confirm before regenerating existing content in another language. Identify what will be replaced, including both summary levels. Only successful generation commits replacement; cancellation preserves content/progress and other functions are unaffected. Quiz reset follows FR-22; failure follows FR-23.
- **FR-23 — Preserve content when language regeneration fails:** Retain existing content and associated quiz answers/progress until successful generation. Failure shows an understandable error and retry, without replacement or quiz reset.

Boundary example: with both Bokmål summaries available, requesting English Brief keeps both until success. Success leaves English Brief, removes both old levels and changes neither cards nor quiz. Failure preserves both; a failed quiz-language change likewise preserves its old position/answers.

### Flashcard practice

- **FR-7 — Practise before revealing an answer:** Show one card with a term/question on its front and answer on its back. Allow an attempt before clicking to flip. Every newly displayed card starts front-first.
- **FR-30 — Prioritize flashcard quality over count:** Default to ten cards, fewer with a short notice when source material is insufficient. Cover central concepts, definitions and important relationships without unnecessary repetition; every answer is document-grounded and cited. Source-invalid/zero-usable outcomes follow FR-37.
- **FR-31 — Navigate and resume flashcards:** Provide forward/back navigation and a current/actual-total counter. Returning from Summary or Quiz retains position but shows the front, hiding answer/source. Successful language replacement starts at the front of the new set's first card, even for a shorter set; failure preserves the old set/position under FR-23.
- **FR-32 — Check flashcard sources after recall:** Sources appear only on the back with the answer, never on the front before recall.
- **FR-33 — Repeat the same flashcard set:** At the walkthrough's end, restart the same generated set at the first card's front without generation. No mastery ratings, advanced tracking or spaced repetition are required.

### Quiz and feedback

- **FR-8 — Test understanding:** Default to ten document-based multiple-choice questions, each with four alternatives and one correct answer. FR-28 governs reduced counts; FR-29 governs the mix.
- **FR-9 — Learn from an incorrect answer:** Immediately after confirmation, show correct/incorrect feedback. Wrong answers reveal the correct alternative and a short explanation of the mistake and correct answer, with page/excerpt source access. Summary level does not affect feedback.
- **FR-10 — Review the quiz result:** For a completed quiz of N ≥ 1 questions and C correct confirmed answers, show C, percentage 100 × C / N and the list of incorrectly answered questions. Use the actual question count and that attempt's confirmed answers, unaffected by later review/retry.
- **FR-13 — Resume an unfinished quiz:** Returning from Summary or View source within the session resumes the same quiz position and previous answers without restart or modification.
- **FR-22 — Reset quiz practice when its language changes:** Confirmation must explain that successful language replacement resets answers/progress for the new quiz. Cancellation/failure preserves the existing quiz, position and answers under FR-23.
- **FR-24 — Confirm a quiz answer:** Present one question at a time. Let the student select one alternative and require explicit confirmation before showing feedback. Confirmed answers cannot be edited within that attempt.
- **FR-25 — Navigate and follow progress:** After feedback, Next question advances. Show current/actual-total progress, including reduced sets. Allow earlier questions and the student's answers to be reviewed; confirmed answers stay locked.
- **FR-26 — Review the completed quiz:** Review questions, answers, explanations and sources after completion, including wrongly answered questions.
- **FR-27 — Restart the same quiz:** From the result, start a new attempt using the same generated questions without generation. Reset answers, progress and result; no history of earlier attempts is required.
- **FR-28 — Prioritize question quality over count:** Generate fewer than ten when source material cannot support ten correct, varied, source-backed questions. Explain the reduction briefly; never pad with unsupported content or unnecessary repetition. Source-invalid/zero-usable outcomes follow FR-37.
- **FR-29 — Mix question types according to the material:** Include factual definitions/key concepts, understanding of why/how/relationships, and simple application as the PDF supports. Adapt the mix without fixed percentages; all use the same four-option flow, without extra modes.

### Source verification

- **FR-11 — Inspect source references:** Show filename, short original-document excerpt and physical PDF page counted from 1, irrespective of printed labels. Keep excerpts in original wording/language even when generated content is translated or paraphrased.
- **FR-12 — Check sources in a sidepanel:** View source shows filename, page and highlighted original excerpt in a simple sidepanel. Closing preserves place/progress. V1 does not require a PDF viewer, direct navigation to the original page or highlighting within the PDF.
- **FR-34 — Distinguish location from factual support:** An excerpt found on its cited page is not proof of correctness or support. Allow inspection of the original supporting text; invalid/unverifiable references follow FR-36.
- **FR-35 — Support explanations with original passages:** Generated interpretations, simplifications and paraphrases cite original supporting passages, not necessarily identical generated wording. Multiple contributing passages have multiple inspectable references with their locations/excerpts.
- **FR-36 — Recover from invalid sources without publishing them:** Invalid/missing pages, missing/empty excerpts and unverifiable excerpts must not appear as valid sources. Regenerate affected content within a finite limit. If any citation remains invalid, withhold the whole new summary and preserve any previous valid summary. Cards/quizzes follow FR-37. Unusable generation ends with an understandable error; failed generation/recovery preserves valid content/progress. Architecture/implementation defines and verifies retries and matching/normalization.
- **FR-37 — Deliver only usable quiz questions and cards:** After bounded recovery, omit an entire item if any reference remains unverifiable, even alongside valid references. Deliver remaining usable items with a brief source-verification notice and their actual count for navigation/results. Never pad to ten. Zero usable items means an error and retry, preserving prior valid content/progress. Filter only otherwise structurally valid sets; malformed replies follow NFR-3.

Boundary checks:

- A paraphrase cites and highlights original supporting wording, not an invented matching quotation. Finding it is not labelled factual verification.
- Opening/closing View source preserves quiz/card state and does not trigger FR-31's front reset for function switching.
- Nine usable items out of ten means deliver nine with a notice; several failures follow the same rule. None means error/retry, never an empty scored quiz.

### Demo and live validation

- **FR-42 — Run a clearly labelled key-free demo:** Provide one shareable predefined PDF with saved Brief/Detailed summaries and card/quiz sets in both Bokmål and English. Core learning/source flows run from the README without private keys or paid accounts. Language/detail actions load matching saved variants, truthfully labelled as demo. Own PDFs/fresh generation require live mode; unsupported demo actions explain the limit instead of fabricating output. Apply the same content/source/rubric checks to demo aids; validate live integration separately, since demo quality does not establish live quality.

## Cross-cutting security requirements

Implement these boundaries and their negative checks during Architecture and development.

- **NFR-1 — Keep study content separate from app authority:** PDF/model content is study data; embedded instructions authorize no app rule, setting or action changes. Give the model no shell, arbitrary-file or URL-fetch tools.
- **NFR-2 — Display untrusted content inertly:** Model text, excerpts and filenames must not execute HTML/scripts, automatically load remote images or trigger external requests through generated content. Safe headings, emphasis and lists are allowed; Architecture chooses rendering.
- **NFR-3 — Validate generated structures:** Validate required fields, types, lengths, four-option structure, answer keys and app-owned source locations. Reject structurally malformed replies as a whole with controlled failure and preserved valid state. FR-37's narrower filtering applies only to otherwise valid structure.
- **NFR-4 — Protect private credentials:** Exclude private credentials from model/PDF content, browser-delivered code and exposed errors/payloads. Apply the same content/rendering boundaries to demo aids; verify mechanisms during Architecture/implementation.
- **NFR-5 — Bound app-owned working data:** Ordinary PDFs, extracted text and generated aids are not permanent history. Clear/accepted replacement removes app-owned working copies; working copies from other ended sessions have a finite cleanup deadline, defined and tested in Architecture. Ordinary app/SDK/error logs exclude study material. Deliberately saved permitted test/demo evidence has separate owner, access and review/deletion conditions. Provider retention follows FR-46.

## Validation plan and success measures

These are planned checks, not completed results.

| Test band | Physical PDF pages |
| --- | --- |
| T1 — Short | 1–10 |
| T2 — Medium | 15–25 |
| T3 — Long | 30–40 |

Bands organize sampling; they are neither upload limits nor rejection rules for intervening lengths. Preserve language/content-type coverage alongside size. Actual PDFs, numeric byte/page/text/time limits and evidence remain pending.

- **SM-1 — Summary coverage:** Review 12 cases: T1–T3 × Bokmål/English × Brief/Detailed, using the manual accuracy/coverage protocol. Readable formatting alone does not pass. Validates FR-4–FR-6 and FR-20.
- **SM-2 — Flashcard answer quality:** Across six cases (T1–T3 × both languages), require at least 9/10 correct reviewed answers per case. If fewer than ten are available, inspect all and require all to pass. Validates FR-7/FR-30.
- **SM-3 — Quiz answer quality:** Across six cases (T1–T3 × both languages), require at least 9/10 correct, unambiguous reviewed keys per case; inspect all and require all to pass for smaller sets. Validates FR-8/FR-9/FR-29.
- **SM-4 — Reference support and location:** Per case, at least 9/10 reviewed references must be relevant to and support the associated content; inspect all and require all to pass if fewer. Every displayed location exists. On the same sampled card/quiz items, require joint answer-correctness/source-support passes for at least 9/10, or all if fewer. Report separate and joint results. FR-11/FR-34–FR-37 location checks do not replace human semantic review.
- **SM-5 — Functional and failure behaviour:** Check wrong-answer feedback in every tested case, navigation/results/restart, session/language replacement, source failures and unusable-PDF handling. Correct/retest known errors regardless of numerical passes. Validate labelled key-free demo and live integration separately.
- **SM-6 — Preparation effort and usefulness:** Compare like-for-like preparation with/without the app, including review/correction time and failed attempts. Record usefulness/corrections and disclose familiarity/order effects. Define timing tasks before full evaluation; no savings or learning-gain result is established.

Counterchecks: item count must not override correctness/source support (FR-28/FR-30/FR-37). Corrections and failures accompany timing/usefulness observations; faster raw generation alone is insufficient evidence of useful preparation.

### Manual evaluation protocol

1. Review every summary factual claim against the original PDF, not only extracted text. No unresolved factual error, unsupported addition or unclear assessment passes. Assess language, organization, relevance, repetition and selected level.
2. Before viewing outputs, map five Brief core points and ten Detailed eligible points to sources. Brief covers all five; Detailed covers those five plus at least three additional points. Fix smaller eligible lists/thresholds for short sources before scoring. Pilot T1 before full evaluation.
3. Apply SM-4 to the same sampled card/quiz items against the original PDF. For multiple references, check locations/excerpts and support for required claims; a found but irrelevant passage fails support. Record joint item and separate correctness/reference results. Freeze reference-selection/counting before scoring.
4. Retain first complete outputs, failures, omitted items, original defects, corrections and retests for permissioned evaluation files. Choose samples before quality review; report per-case results without pooling away failures. This evidence is separate from automatic study history.
5. Camilla freezes actual documents, mapped points, sampling/counting rules and SM-6 timing tasks after the T1 pilot and before full scoring.

## Handoff conditions

Product decisions are resolved. Architecture owns numeric upload/resource/time bounds, observable extraction stop criteria, matching/normalization and retry caps. Define and verify these with representative documents before implementation relies on them; flag limits changing the agreed test-size scope.

Camilla selects permissioned test/demo files before live testing and confirms the assignment rubric/exact deadline before final delivery planning. Planned checks are not completed evidence. See [the addendum](addendum.md) for technical considerations. Research proposals apply only when adopted here.

## Existing inputs

- [Product brief](../../briefs/brief-G89-halvorsen-2026-09-26/product-brief.md)
- [Brief addendum](../../briefs/brief-G89-halvorsen-2026-09-26/addendum.md)
- [Teacher feedback](../../briefs/brief-G89-halvorsen-2026-09-26/tilbakemelding-product-brief.md)
- [PDF source reliability research](../../research/technical-pdf-source-reliability-2026-10-29/research.md)
- [Quality and evaluation research](../../research/technical-quality-evaluation-2026-11-02/research.md)
- [Uploaded-material handling research](../../research/technical-uploaded-material-handling-2026-11-02/research.md)
- [AI security notes](../../research/ai-security-notes.md)
