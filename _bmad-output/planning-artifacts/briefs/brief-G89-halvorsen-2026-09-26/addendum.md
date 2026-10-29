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

The updated `product-brief.md` defines the current product scope and acceptance criteria. Earlier decisions remain in `.memlog.md`; later overrides take precedence.

- **Users and scope:** the primary user is a bachelor’s student at Molde University College studying IT-related subjects; other students may also use the app. Version 1 supports only text-based PDFs, replacing the original PDF/text scope. Summaries, flashcards, multiple-choice quizzes, and source-based feedback remain core functions. Plain-text files and OCR are excluded. Browser-local progress tracking is optional phase 2; accounts, synchronization, and personal learning plans remain outside v1.
- **Output choices:** Norwegian Bokmål and English are selectable independently of source language for all three study-aid types. Brief and Detailed apply only to summaries, not incorrect-answer explanations.
- **References:** PDF filename, page position starting at 1, and a short excerpt, accessible through View source. An excerpt-presence check warns when verification fails; it does not establish factual correctness.
- **Evaluation:** initial evaluation uses the developer’s own study material. T1–T3 define planned PDF categories: short Norwegian lecture notes (1–10 pages), medium English lecture slides (11–25), and long English course reading (26–40). No concrete PDFs have been selected. These ranges organize testing and are not product limits. Both languages and summary levels give 12 summary combinations; flashcards and quizzes have separate cases.
- **Acceptance:** the brief now contains agreed planned thresholds, including 9 of 10 for flashcard answers, quiz answer keys, and supporting references. It also defines manual summary review, feedback, error handling, and sample rules. These are not completed tests or evidence of time savings.
- **AI and demo:** an external model API is planned. Gemini 2.5 Flash is provisional; final selection belongs to Architecture. A labelled demo with one example PDF and saved study aids must work without the developer’s private key; live API integration is evaluated separately.

## Open questions and downstream work

- **Before testing:** select the actual T1–T3 PDFs, a shareable demo PDF, and manual preparation tasks for comparison. Confirm sharing rights for any material committed to the repository.
- **PRD:** define detailed test cases, sampling and summary-review rules, simple quiz scoring, document limits, error and demo behaviour, and handling and retention of uploaded material. Planned error tests cover unsupported formats, invalid or damaged PDFs, and scanned PDFs without extractable text.
- **Review recommendations, not adopted requirements:** clarify whether answer correctness and supporting references must pass jointly on the same sampled items; whether excerpt checking must use the cited page; and whether questions after summaries reuse the quiz flow.
- **Architecture and README:** select the model and PDF-processing approach, plan API-key handling and demo implementation, and document local setup. The teacher recommends `.env.example`; the model choice must consider cost, availability, quality, and integration.
- **Later scope:** decide whether to implement optional phase-2 browser-local progress tracking only after the core is implemented and tested.
- **Schedule:** confirm the final submission date when announced.

## Preliminary comparison sources

A preliminary check on 2026-09-26 found overlapping features in [NotebookLM](https://notebook.google/students?hl=en-US) and [Quizlet](https://quizlet.com/features/ai-study-tools). These are vendor descriptions, not independently tested results. No unique differentiator has been established.
