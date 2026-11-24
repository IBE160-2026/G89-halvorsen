# AI Study Buddy — Supporting Context

## User-provided assessment requirements

- Original product brief deadline: 2026-09-27, retained as historical context.
- Final project submission: mid December 2026; exact date unconfirmed.
- Project code and functionality: 70% of the assessment.
- Required application deliverable: an AI-generated application, with documentation explaining how AI was used and how the code was quality-assured.
- Reflection report: 30% of the assessment; describes the development process, challenges, and solutions.

These requirements were provided by the user. The teacher’s feedback dated 2026-10-06 is available in `tilbakemelding-product-brief.md`; the original assignment specification and full grading rubric have not been supplied. This context is retained for downstream implementation and reporting work.

## Project conventions

The product name is AI Study Buddy; the project folder remains G89-halvorsen. Current communication is in Norwegian and project documents are in English, superseding the earlier English-only response convention. Brief development follows the coaching path so the user can understand and shape the decisions.

## Current decisions

The brief summarizes scope; the [PRD](../../prds/prd-G89-halvorsen-2026-11-03/prd.md) is the current detailed requirements source. Earlier decisions remain historical; research proposals apply only when adopted there.

- **Users and scope:** students studying independently from text-based PDFs. Summaries, flashcards, quizzes, and inspectable sources remain core. OCR/PDF repair, advanced diagrams/tables, accounts, synchronization, and permanent history are excluded; browser-saved progress is only a later possibility.
- **Session and choices:** choose one PDF, Bokmål/English, and Brief/Detailed before generation. Language applies to all aids; level only to summaries. New session is the single explicit action for ending the session, whether finished or changing document/language/level. Changing those choices requires this confirmed flow. Confirmation removes the old PDF, aids, progress, and acknowledgement, returning to empty startup without affecting the original device file. Starting again is optional and requires file selection, even for the same PDF, choices, and fresh acknowledgement. Cancelling the confirmation preserves state; cancelled file selection or rejected input after confirmation leaves startup empty. Reload/closing has no recovery.
- **References and failures:** View source shows filename, physical page from 1, and original excerpt. A match establishes location, not factual support. Invalid references withhold the new summary or remove whole invalid items from otherwise valid sets; deliver a nonempty valid subset with count/notice. Malformed replies or zero usable items fail. Try again is manual; no automatic AI regeneration/repair. Failures preserve valid active-session content/progress.
- **Evaluation:** local ignored files `test-data/pdfs/T1.pdf` (English IBE321 cybersecurity slides, 10 pages), `T2.pdf` (own Norwegian strategy notes, 24), and `T3.pdf` (own English IT notes, 40). Planned matrix: 12 summary, six card, six quiz cases; summary levels use separate sessions. Known figure omissions require coverage checks. Stop on material/uncertain loss; a correct stop can pass a failure test but cannot pass content quality. Report blocked quality cases separately.
- **Acceptance:** retain 9/10 correctness and supporting-reference thresholds per case, with joint answer/source passes on the same card/quiz items; all pass if fewer than ten. No unresolved known errors pass. Preserve first outputs, failures, corrections, and retests. No completed results or time savings are claimed.
- **AI, privacy, and demo:** require a visible notice and active upload acknowledgement before external text transfer; keep credentials private and untrusted content inert. Verify provider claims; app cleanup does not imply provider deletion. Select a separate shareable demo PDF with saved variants for both languages/levels; only the selected combination is active per session. Demo works without private keys or paid accounts; validate live integration separately.

## Open questions and downstream work

- **Before evaluation:** verify extraction/coverage of selected files, pilot T1, and freeze mapped points, sampling, and timing tasks before full scoring. Select a shareable demo PDF and confirm rights for deliberately saved evidence.
- **Architecture and README:** select provider/PDF processing; define and verify resource, cost, time, and cleanup bounds before implementation relies on them. Verify provider terms/configuration before real transfer. Document key setup through `.env.example`, local running, and truthful demo limits.
- **Later scope:** decide whether to implement optional phase-2 browser-local progress tracking only after the core is implemented and tested.
- **Schedule:** confirm the final submission date when announced.

## Preliminary comparison sources

A preliminary check on 2026-09-26 found overlapping features in [NotebookLM](https://notebook.google/students?hl=en-US) and [Quizlet](https://quizlet.com/features/ai-study-tools). These are vendor descriptions, not independently tested results. No unique differentiator has been established.
