---
title: Product Brief — AI Study Buddy
status: draft
created: 2026-09-26
updated: 2026-10-29
---

# Product Brief: AI Study Buddy

## Executive summary

AI Study Buddy is a simple web application that helps university and college students turn their course material into study aids. Students upload lecture notes, slides, or course readings as text-based PDF documents and generate summaries, flashcards, and multiple-choice quizzes with answers. They can choose the output language and summary detail level, and use source references to check the generated content against the uploaded material.

The goal is to spend less time preparing study material and more time understanding and practicing course content. Developed as an IBE160 Programming with AI project, the first version will have a manageable scope for a beginner and will be evaluated using the developer’s own courses and materials. The project also provides experience with AI text processing, AI-assisted development, and code quality assurance.

## The Problem

Course content is spread across lecture notes, slides, and readings. Preparing study aids takes time away from understanding and practising that content.

For example, a student revising approximately 40 lecture slides before an exam must identify the important information, write a useful summary, and create questions to test their knowledge. When an answer is unclear, they need to find the supporting passage in the slides. This is an illustrative study situation, not an observed test result.

AI-generated study aids need to be verifiable: students should be able to locate the source supporting a summary or answer. The initial problem and expected time savings will be explored through the developer’s own study tasks; they have not yet been validated with a wider student group.

## The Solution

AI Study Buddy provides a browser-based workflow for uploading text-based PDF course material and generating study aids. Students choose Norwegian Bokmål or English for summaries, flashcards, and quizzes, independently of the source language. An English document can produce Norwegian study material, and vice versa. Summaries help students review the content, flashcards support practice, and multiple-choice quizzes let them check their understanding.

Summary detail levels are **Brief**, covering main points and key concepts, and **Detailed**, adding fuller explanations and relevant examples from the source material. These levels apply only to summaries, not to explanations after incorrect quiz answers.

Comprehension questions can appear at the end of a summary. When a student answers incorrectly, the app directs them to the relevant passage in the uploaded source and offers a fuller explanation. References connect the generated content to the course material so the student can verify it and decide what to revisit.

Source references show the PDF filename, page number, and a short source excerpt. Page numbers follow the page order in the PDF file, starting at 1, regardless of any printed page labels. Students select **View source** to see the relevant passage. A simple check tests whether the quoted excerpt occurs in the source material and displays a warning if it cannot be verified. Finding the excerpt does not guarantee that the generated information is factually correct or supported by that passage.

The app is planned to use an external language model through an API. A clearly labelled demo mode uses one predefined example document with saved summaries, flashcards, and quiz questions, allowing the examiner to demonstrate the main functions without the developer’s private API key. Demo content is distinguished from live AI generation; the API integration will be tested separately during development.

## What Makes This Different

The project emphasizes a simple workflow built around the student’s own course material, with source references and feedback that leads back to that material. Its value will be evaluated through usefulness and ease of verification in actual study tasks.

These capabilities are not claimed to be unique. Existing tools such as [NotebookLM](https://notebook.google/students?hl=en-US) and [Quizlet](https://quizlet.com/features/ai-study-tools) offer overlapping study features. AI Study Buddy’s focus is a small, achievable implementation whose behavior and quality can be tested and explained as part of a beginner project.

## Who This Serves

The primary user is a bachelor’s student at Molde University College studying IT-related subjects. They study independently using PDF lecture slides, course readings, and their own notes, and want a more efficient way to understand and revise course content before exams. Material used in the app, including their own notes, must be available as text-based PDFs. Other university and college students can also use the app.

Initial testing will use the developer’s own courses and curriculum materials. This will provide evidence about the selected study tasks, without establishing usefulness across all subjects or student groups.

## Success Criteria

The following are planned acceptance criteria, not completed tests or reported results. Three text-based PDFs will be selected later:

| Test document | Length | Representative content |
|---|---|---|
| T1 — Short PDF | 1–10 pages | Norwegian lecture notes with key concepts and definitions. |
| T2 — Medium PDF | 11–25 pages | English lecture slides with technical terms, explanations, and models. |
| T3 — Long PDF | 26–40 pages | English course reading covering several topics with fuller explanations. |

These categories organize testing; they do not define supported PDF length limits. Each document will be tested with both output languages and both summary detail levels, giving **12 summary test combinations**. Flashcards and quizzes will have separate test cases in both output languages for each document; summary detail levels do not apply to them.

All generated study aids must follow the selected output language. For flashcards, quiz questions, and source references, samples will cover ten items per test case. If fewer are available, all will be checked and must meet the relevant criterion.

- **Functional:** all three PDFs support the complete workflow: upload, generate each study-aid type, and view answers and source references.
- **Summaries:** all 12 combinations follow the selected summary level. Manual review checks that factual statements are correct and supported by the document, including explanations and examples in Detailed summaries.
- **Flashcards:** at least 9 of 10 checked cards have factually correct answers in each document-and-output-language test case.
- **Quizzes:** at least 9 of 10 checked questions have a correct, unambiguous answer key in each document-and-output-language test case.
- **References:** at least 9 of 10 checked references lead to relevant source content that supports the associated statement or answer. Samples are checked separately for each study-aid type, document, and output language. Every displayed reference must identify an existing source location. The excerpt check warns when a quotation cannot be verified; factual support is assessed manually.
- **Study feedback:** every tested incorrect quiz answer displays the correct answer, an understandable explanation, and a source reference.
- **Error handling:** planned tests include unsupported file formats such as .txt, invalid or damaged PDF files, and scanned PDFs without extractable text. Files that cannot be processed must produce an understandable error message explaining the problem and a possible next step.
- **Demo access:** following the README, the examiner can complete the demo workflow described above, including quiz feedback and source inspection, without a private API key or paid account. Live API generation will be tested separately.
- **Practical value:** representative study tasks compare preparation time with manual preparation and record usefulness and necessary corrections. Time savings are a goal, not an established result.
- **Project learning and quality:** documentation explains how AI was used, how the code and application were checked, and what challenges and solutions arose during development.

Identified errors will be recorded, corrected, and retested; the thresholds do not justify retaining known errors. Exact documents, sampling procedures, and detailed test cases will be defined later. Wider student testing is not required for the initial evaluation.

## Scope

The first version is a simple web application designed to remain achievable as a beginner project. Scope must leave time for testing and documenting AI use and code quality assurance.

**In:** 

The first version supports text-based PDF uploads, summaries, flashcards, and multiple-choice quizzes with answers. It includes the language and summary-level choices, source references with an excerpt check, incorrect-answer feedback, understandable processing errors, and the predefined demo mode described above.

**Out:**

The first version does not support plain-text (.txt) files or other non-PDF formats. It does not include personal accounts, login, synchronization between devices, personal learning plans, adaptive study recommendations based on performance over time, written-answer assessment, or OCR for scanned documents. Browser-local progress tracking is reserved for an optional phase 2, after the core functions have been implemented and tested.

The PRD will define detailed acceptance tests, document limits, error behaviour, demo behaviour, and handling of uploaded material. Architecture will select the model, PDF processing approach, API-key handling, and demo implementation. Google Gemini 2.5 Flash is a provisional model candidate, not a final choice; selection will consider cost, availability, quality, and integration. API-key setup and local running instructions will be documented in the README.

## Vision

AI Study Buddy could grow into a study companion that supports continued practice across courses and devices. Future development could introduce personal accounts and login, synchronized progress, and a personal learning plan that uses practice results to suggest topics needing further work. These possibilities depend on a useful, verifiable first version and are not commitments for the current project.
