---
title: AI Study Buddy — PRD Addendum
status: final
created: 2026-11-03
updated: 2026-11-14
---

# AI Study Buddy — PRD Addendum

Technical/evidence follow-ups for Architecture and implementation. [The PRD](prd.md) defines product behaviour; these notes select no library or additional features.

## PDF extraction and coverage

Architecture must verify observable unreadable/unreliable-extraction signals against local T1–T3. FR-41 stops generation on material loss or uncertain main-text coverage. Neither a nonempty page nor a coverage notice establishes complete extraction; an empty page does not establish lost content. Define representative fixtures and explicit stop rules without promising automatic assessment of every omission's importance.

The limited PDFKit inspection found figure loss, including T2 page 12 and T3 page 30. Use these cases when verifying the chosen parser and coverage policy. The [research input](../../research/technical-pdf-source-reliability-2026-10-29/research.md) explains structural/image limitations; neither it nor the pilot selects the app's library. OCR, advanced figural interpretation and PDF repair remain excluded.

## Resource and validation boundaries

- Verify byte/page/text/context, processing-time and cost bounds before implementation depends on them. Actual T1–T3 sizes are test inputs, not upload limits; flag bounds excluding them.
- Define page-local excerpt matching and permitted normalization. Test whitespace, Unicode, wrong-page and hyphen/line-break cases; location matching remains separate from factual-support review.
- Failed generation or no usable output requires manual Try again, never automatic regeneration/repair. Deliver valid card/quiz subsets without automatic refill. Preserve valid active-session state and reject late results after Clear/New session. Failed file selection/generation cannot restore the ended session.
- Verify per-upload acknowledgement, provider configuration and working-copy cleanup deadlines before real transfer/use. Resource limits and implementation mechanisms remain open, without invented numeric values.

## Evaluation and regression evidence

The developer freezes original-PDF points, item/reference sampling/counting and comparable timing tasks/target after the T1 evaluation pilot, before full scoring. Check each multi-reference location and combined support. A controlled extraction stop is a failure-handling result, not a quality pass; disclose blocked cases.

Record model/prompt/parser/configuration versions; preserve first outputs, failures, omissions, fixes and retests. Recheck affected cases after changes. Apply the same rubric to saved demo content, separately from live integration. Record evidence owner, permitted uses, access and review/deletion conditions outside ordinary app logs/history. Local test files do not establish public-demo or external-transfer permission; select a shareable demo separately.

## Educational delivery follow-ups

The supporting context describes a solo IBE160 project with 70% functionality and 30% reflection assessment. Verify this against the original assignment/full rubric and confirm the exact deadline before delivery planning.

- Architecture/README: justify stack/model/parser; document cost/configuration, local startup, key-free demo and separate live setup, with credential-free `.env.example` where applicable.
- Development/reflection: retain permitted AI/prompt/decision, code-quality and test evidence, challenges and solutions; distinguish plans from completed checks.
- UX: sketch startup, navigation, source panel, warnings and wrong-answer flow; check keyboard use, readability and source-location/support wording before delivery.
