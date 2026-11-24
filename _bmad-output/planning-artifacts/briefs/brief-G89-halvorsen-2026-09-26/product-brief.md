---
title: Product Brief — AI Study Buddy
status: draft
created: 2026-09-26
updated: 2026-11-19
---

# Product Brief: AI Study Buddy

## Executive summary

AI Study Buddy is a simple web application that turns one text-based course PDF into summaries, flashcards, and multiple-choice quizzes. Students choose one output language and one summary detail level per temporary study session, and inspect source references to check generated content.

The goal is to spend less time preparing study material and more time understanding and practising it. This solo IBE160 Programming with AI project is evaluated using the developer’s own material, with time reserved for testing, documentation, and reflection on AI-assisted development.

## The Problem

Course content is spread across lecture notes, slides, and readings. Preparing study aids takes time away from understanding and practising that content.

For example, a student revising approximately 40 lecture slides before an exam must identify the important information, write a useful summary, and create questions to test their knowledge. When an answer is unclear, they need to find the supporting passage in the slides. This is an illustrative study situation, not an observed test result.

Students need to locate the source supporting a generated summary or answer. Usefulness and expected time savings will be explored through the developer’s own study tasks; they are not established results.

## The Solution

Students choose a PDF, Norwegian Bokmål or English independently of source language, and a summary level before generation. The selected language applies to all generated aids in that session. Summaries support understanding, flashcards recall, and quizzes self-assessment; navigation preserves generated content and practice progress.

**Brief** covers main points and key concepts; **Detailed** adds fuller explanations and relevant source-grounded examples. The chosen level applies only to summaries, not cards, quizzes, or incorrect-answer explanations.

**New session** is the single explicit action for ending the current session, whether the student is finished or wants to change document, language, or level. Changing any of those choices requires this confirmed flow. Confirmation removes the old PDF, aids, progress, and external-processing acknowledgement, leaving ordinary empty startup; the original device file is unaffected. The student can stop there. Starting again requires a new file selection, even for the same PDF, new choices, and acknowledgement. Cancelling the confirmation preserves the current session; cancelled file selection or a rejected file after confirmation leaves startup empty. Reload or closing ends the session without recovery.

From a summary, students can enter the existing quiz. Wrong answers show the correct alternative, a short explanation, and source access. **View source** opens a simple sidepanel showing filename, physical PDF page counted from 1, and an original-language excerpt. A page-and-excerpt match establishes location, not factual correctness or semantic support.

Invalid references withhold the whole new summary. In otherwise structurally valid card/quiz sets, omit each item with any invalid reference and deliver the valid subset with its actual count and a notice; zero usable items means an error. Malformed replies are rejected as a whole. There is no automatic AI regeneration or repair: **Try again** is manual, and failure preserves valid content and progress in the active session.

Before any extracted text goes to external AI, show a short material-handling notice and require active acknowledgement for the current upload. Discourage sensitive, confidential, or externally restricted material. Keep credentials private, render untrusted content inertly, validate model replies, and make only verified provider-retention claims. App cleanup does not imply provider deletion.

A labelled demo uses one shareable PDF, still to be selected, with saved Brief/Detailed summaries and card/quiz sets in both languages. Only the selected language/level combination is active per session; changed choices use New session. It runs without private keys or paid accounts. Live integration is validated separately.

## What Makes This Different

The project emphasizes a simple workflow using the student’s own material, with inspectable sources and feedback. Evaluation considers usefulness and ease of verification in actual study tasks.

Existing tools such as [NotebookLM](https://notebook.google/students?hl=en-US) and [Quizlet](https://quizlet.com/features/ai-study-tools) offer overlapping features. No uniqueness is claimed; the focus is an achievable beginner project with explainable, testable behaviour.

## Who This Serves

The primary user is a bachelor’s student at Molde University College studying IT-related subjects independently from text-based PDF slides, readings, and notes. Other students may also use the app; it is not restricted to one discipline.

Initial evidence concerns the developer’s selected tasks, without establishing usefulness across subjects or student groups.

## Success Criteria

These are planned checks, not completed results. The selected local evaluation files are:

| Test document | Length | Representative content |
|---|---|---|
| T1 — `test-data/pdfs/T1.pdf` | 10 pages | English IBE321 cybersecurity slides. |
| T2 — `test-data/pdfs/T2.pdf` | 24 pages | The developer’s Norwegian strategy notes. |
| T3 — `test-data/pdfs/T3.pdf` | 40 pages | The developer’s English IT notes. |

These files are ignored by Git and are not approved demo assets. Page counts are not upload limits. The planned matrix is **12 summary, six flashcard, and six quiz cases** across these PDFs and both languages. Summary levels use separate sessions. Known figure omissions require coverage checks: generation proceeds only with reliable main-text coverage. Material or uncertain loss must stop. A correct stop may pass a failure test but does not pass content-quality evaluation; record blocked quality cases explicitly.

All aids must follow the selected language. Review ten items per card/quiz case; inspect all and require all to pass for smaller sets.

- **Functional:** test all three PDFs. Supported input permits upload, generation, practice, and source inspection; unreliable input produces controlled rejection or stopping.
- **Summaries:** generated cases follow the selected level and the PRD’s manual coverage rubric. Check factual claims, explanations, and examples against the original PDF.
- **Flashcards:** at least 9 of 10 checked cards have factually correct answers in each document-and-output-language test case.
- **Quizzes:** at least 9 of 10 checked questions have a correct, unambiguous answer key in each document-and-output-language test case.
- **References:** at least 9/10 reviewed references per case support the associated content; all must pass if fewer than ten. Every displayed location and excerpt is verifiable. On the same sampled card/quiz items, at least 9/10 jointly pass answer correctness and source support, or all if fewer. Semantic support is reviewed manually against the original PDF.
- **Study feedback:** every tested incorrect quiz answer displays the correct answer, an understandable explanation, and a source reference.
- **Error handling:** test non-PDF, damaged, password-protected, no-usable-text, source, service, and coverage failures; explain the problem and next step. Test cancelled/confirmed New session, empty startup without a new upload, active-session preservation on generation failure, and rejection after confirmed restart.
- **Demo access:** following the README, the examiner can complete the demo workflow described above, including quiz feedback and source inspection, without a private API key or paid account. Live API generation will be tested separately.
- **Practical value:** compare like-for-like preparation time, including review, corrections, and failed attempts; record usefulness. Freeze tasks before evaluation. Time savings remain a goal.
- **Project learning and quality:** documentation explains how AI was used, how the code and application were checked, and what challenges and solutions arose during development.

Record first outputs, failures, corrections, and retests; no unresolved known error passes. Final sampling and timing tasks follow the T1 pilot. Wider student testing is not required.

## Scope

The first version is a simple web application designed to remain achievable as a beginner project. Scope must leave time for testing and documenting AI use and code quality assurance.

**In:**

One temporary PDF session, the three learning functions, per-session language/summary choices, source validation and inspection, quiz feedback, manual retries, controlled failures, and the labelled demo described above.

**Out:**

Non-PDF formats, accounts/login, synchronization, permanent study history, learning plans, adaptive learning, written-answer assessment, OCR/PDF repair, advanced diagram or complex-table interpretation, automatic AI repair, and in-session language/level changes. Browser-saved progress is only a possible later extension after the tested core.

The [PRD](../../prds/prd-G89-halvorsen-2026-11-03/prd.md) is the current detailed requirements source. Architecture selects the provider, PDF processing, resource/cost/time limits, credential handling, and cleanup mechanisms. Verify these with representative files before relying on them; README documents setup and demo access. Research and historical proposals are requirements only when adopted in the PRD.

## Vision

Future versions could add accounts, synchronized progress, and personal learning plans after a useful, verifiable first version. These are not commitments for the current project.
