---
title: AI Study Buddy — PRD Addendum
status: final
created: 2026-11-03
updated: 2026-11-03
---

# AI Study Buddy — PRD Addendum

Technical considerations for downstream Architecture and implementation. Product behaviour is defined in [the PRD](prd.md); these notes do not select a library or add features.

## PDF extraction and coverage

Architecture must define observable signals for unreadable or unreliable extraction and verify them on representative PDFs. The product fallback in FR-41 is to stop when adequate reliable main-text coverage cannot be established. Do not claim that the importance of every omitted passage can be determined automatically. Keep the student's coverage notice distinct from a guarantee that all significant material was captured. Empty pages alone do not establish what meaningful content, if any, was missed; their treatment requires representative fixtures and an explicit rule.

Text extraction does not guarantee preservation of a PDF's structure or image content. The primary [pypdf extraction documentation](https://pypdf.readthedocs.io/en/stable/user/extract-text.html) describes positioned text, table/reading-order difficulties, image-only text and missing semantic structure. This is evidence of extraction limitations, not a selection of pypdf for the project or a test of AI Study Buddy.

## Resource and validation boundaries

- Choose and verify byte, page, extracted-text, processing-time and provider-context limits before implementation relies on them. The agreed document-size test bands do not themselves define upload limits.
- Define a finite source-recovery retry cap and source-excerpt matching/normalization rules against cited physical pages. Excerpt-location checks must remain separate from evaluation of factual support.
- Verify preservation of prior valid content and practice state when generation or replacement fails, including delayed results after Clear/document replacement and unsuccessful language changes.
- Use the planned short, medium and long documents alongside language/content coverage and explicit failure fixtures. Actual files, permissions, acceptance evidence and measured limits remain to be selected and collected.

## Evaluation and regression evidence

Camilla owns the test protocol before full scoring: choose permitted PDFs, map original-PDF key points, freeze item/reference sampling and counting, and define comparable timing tasks after the T1 pilot. Review original PDF pages separately from parser-produced text. For multi-reference items, record each location/excerpt check and the combined semantic support for the answer; a valid-looking location alone is not a passing support judgment.

Record model, prompt, extraction/library and relevant configuration versions with the evaluation evidence. Preserve initial failures, omitted items, corrections and retests. Revalidate affected cases when these inputs change. Apply the same quality/source rubric to saved demo aids while keeping demo playback evidence separate from live-integration evidence. The evidence register must state the owner, permitted uses, access permissions and conditions for review or deletion. Keep it separate from ordinary app logs and student history.

## Educational delivery follow-ups

The brief describes a solo IBE160 Programming with AI project, with 70% functionality and 30% reflection assessment. Before delivery planning, Camilla must confirm these assessment details against the original assignment and full rubric, and confirm the exact deadline.

- Architecture/README: justify stack, model and PDF-library choices; document costs and provider configuration, local startup, the key-free demo and separate live setup. Provide a credential-free `.env.example` when environment variables are used.
- Development/reflection: retain permitted evidence of AI use, prompt iteration, decisions, code-quality assurance, tests, challenges and solutions for the reflection report. Do not mistake planned checks for completed evidence.
- UX: sketch the learning navigation, source sidepanel, warnings and wrong-answer flow; check basic keyboard use, readability and understanding of source-location versus factual-support messages. Track findings and changes before final delivery.
