# Research brief: PDF source reliability

Date: 2026-10-29. Intent: Run. Type: technical. Shape: explore.

## Decision

Identify feasible, testable PDF and citation behaviour for AI Study Buddy's PRD, without selecting the final architecture or changing the Product Brief.

## Authorized scope and plan

The user's explicit request authorizes this focused plan: research page-wise extraction, preservation of physical PDF page positions, generated filename/page/excerpt citations, excerpt matching on the cited page, and understandable handling of unreadable PDFs. Keep recommendations achievable for a beginner IBE160 project.

- Breadth-first research: extraction/page mapping; citation generation/validation; unreadable-file handling.
- Standard preset: up to three assistants, eight sources per dimension per round, two rounds maximum; stop when covered. Normal verification; no additional red-team or workflow orchestration.
- Sources: official library documentation, relevant standards, official model documentation; retrieved through available web search/open tools. No performance benchmark or current version ranking is intended.
- Expected duration: several minutes. Markdown output because this is a skill-invoked run. Research helpers and quality-review assistants may be used as specified by Deep Recon.
- Language: English artifacts, Norwegian conversation, following the latest project convention.

## Project context (requirements, not external evidence)

Inputs read: current product-brief.md, addendum.md and .memlog.md under ../../briefs/brief-G89-halvorsen-2026-09-26/, plus the previous session log and issues.md.

V1 supports text-based PDFs only; OCR and other upload formats are excluded. References show filename, physical page position starting at 1, and a short excerpt through View source. Excerpt checking warns on failure but cannot prove factual support. Bokmål/English output is independent of source language. No concrete T1–T3 PDFs are selected; their page ranges are test categories, not upload limits. Final library/model selection belongs to Architecture.

## Deliverables

research.md: concise findings, possible solutions, recommendations and PRD decisions, with source appendix and limitations. digests/: retrieved evidence and provenance. .memlog.md: decisions and claim status. No application implementation, Product Brief edit or PRD creation.
