---
title: AI Study Buddy — PRD Addendum
status: final
created: 2026-11-03
updated: 2026-11-26
---

# AI Study Buddy — PRD Addendum

Technical/evidence follow-ups for Architecture and implementation. [The PRD](prd.md) defines product behaviour; these notes select no library or additional features.

## PDF extraction and coverage

Architecture must verify usable-text and concrete text-unreliability signals against local T1–T3. Under revised FR-40/FR-41, use readable, source-verifiable text even when graphical/table content is unavailable; show an evidence-based nonblocking omission notice. Stop only for insufficient remaining text or concrete failures that make retained main text unreliable, alongside ordinary invalid/protected/resource-limit input failures. Graphical presence, a textless page, generic parser warnings or plain/layout differences alone do not reject the whole PDF. Neither nonempty pages nor a notice establishes complete extraction; empty text alone does not prove a blank page or a scan.

The limited PDFKit inspection found figure loss, including T2 page 12 and T3 page 30. Use these cases when verifying the chosen parser and coverage policy. The [research input](../../research/technical-pdf-source-reliability-2026-10-29/research.md) explains structural/image limitations; neither it nor the pilot selects the app's library. OCR, advanced figural interpretation and PDF repair remain excluded.

## Resource and validation boundaries

- Verify byte/page/text/context, processing-time and cost bounds before implementation depends on them. Actual T1–T3 sizes are test inputs, not upload limits; flag bounds excluding them.
- Define page-local excerpt matching and permitted normalization. Test whitespace, Unicode, wrong-page and hyphen/line-break cases; location matching remains separate from factual-support review.
- Failed generation or no usable output requires manual Try again, never automatic regeneration/repair. Deliver valid card/quiz subsets without automatic refill. Preserve valid active-session state and reject late results after confirmed New session. Failed file selection/generation cannot restore the ended session. Ending a session returns to empty startup without requiring another upload.
- Verify per-upload acknowledgement, provider configuration and working-copy cleanup deadlines before real transfer/use. Resource limits and implementation mechanisms remain open, without invented numeric values.

## Evaluation and regression evidence

The developer freezes points from readable, source-verifiable native text in the original PDF, item/reference sampling/counting and comparable timing tasks/target after the T1 evaluation pilot, before full scoring. Do not restrict expected points to the parser's returned text or drop missing expected text points after seeing outputs. Report omitted image/figure/uninterpretable-table content separately without claiming full-PDF coverage. Check every generated factual claim against the original PDF and each multi-reference location/combined support; correctness, source and joint 9/10 thresholds remain unchanged. A controlled text-insufficiency/unreliability stop is a failure-handling result, not a quality pass; disclose blocked cases.

Record model/prompt/parser/configuration versions; preserve first outputs, failures, omissions, fixes and retests. Recheck affected cases after changes. Apply the same rubric to saved demo content, separately from live integration. Record evidence owner, permitted uses, access and review/deletion conditions outside ordinary app logs/history. Local test files do not establish public-demo or external-transfer permission; select a shareable demo separately.

## Educational delivery follow-ups

The supporting context describes a solo IBE160 project with 70% functionality and 30% reflection assessment. Verify this against the original assignment/full rubric and confirm the exact deadline before delivery planning.

- Architecture/README: justify stack/model/parser; document cost/configuration, local startup, key-free demo and separate live setup, with credential-free `.env.example` where applicable.
- Development/reflection: retain permitted AI/prompt/decision, code-quality and test evidence, challenges and solutions; distinguish plans from completed checks.
- UX: sketch startup, navigation, source panel, warnings and wrong-answer flow; check keyboard use, readability and source-location/support wording before delivery.
