---
title: Input reconciliation — PDF source reliability
created: 2026-11-03
status: reconciled-with-follow-ups
input: ../../research/technical-pdf-source-reliability-2026-10-29/research.md
---

# PDF source reliability reconciliation

Reviewed the original research against the current [PRD](prd.md), [addendum](addendum.md) and chronological decisions in [.memlog.md](.memlog.md). Later confirmed product decisions take precedence over provisional research recommendations. This is a source extract and coverage review, not new product approval or implementation evidence.

## Evidence carried forward

The research is documentation research dated 2026-10-29. It tested no PDFs, installed no parser, called no model and measured no accuracy or processing limits. Its official-documentation findings support the following distinctions:

- Page-wise extraction can retain physical page identity, but reading order, tables, columns, image-only material and existing OCR layers can still be unreliable.
- Successful PDF loading does not establish complete or faithful extraction. Empty extracted text alone cannot distinguish a blank page, an image-only page and extraction failure.
- A syntactically valid model response does not establish that its page, source ID, quotation or factual claim is correct.
- Finding an excerpt on the cited page establishes occurrence in extracted text. It does not establish extraction fidelity, answer correctness or semantic support.
- Canonical and compatibility normalization differ. Aggressive normalization can erase meaningful distinctions in technical material; any accepted transformation requires an explicit tested policy.
- Password handling is a product scope choice even when a parser supports decryption.

These findings are represented in FR-11, FR-34, FR-36, FR-38–FR-41, FR-43, NFR-3, SM-4 and the addendum's extraction/validation notes. No parser, model or performance promise is inferred from the findings.

## Coverage and disposition

| Source topic | Current coverage | Reconciliation |
| --- | --- | --- |
| Physical page identity, distinct from printed page labels | FR-11; FR-12 | Adopted. Physical file order starts at 1. An implementation must not renumber later pages after filtering empty pages. Internal page/source bookkeeping remains Architecture work. |
| Filename and original supporting excerpt | FR-11; FR-12; FR-35 | Adopted. Source text remains the original text when output is translated or paraphrased. The panel highlights that original excerpt. |
| Multiple passages/pages supporting one explanation | FR-35 | Adopted. Multiple inspectable references are supported. Exact source-record and per-page segment design remains optional implementation guidance. The mixed-validity boundary needs clarification below. |
| Application validation of generated references | FR-36; NFR-3; addendum, Resource and validation boundaries | Adopted outcome. Invalid/missing pages and missing/empty/unverifiable excerpts cannot become valid-looking citations. App-owned source locations are included in structural validation. |
| Page-local comparison rather than a document-wide match | FR-11; FR-36; addendum, Resource and validation boundaries | Covered as a downstream mechanism: the addendum explicitly calls for matching against cited physical pages. Architecture defines and verifies the exact algorithm. |
| Excerpt occurrence versus factual support | FR-34; SM-4; manual evaluation protocol | Adopted distinction. Location checks do not replace human review. Answer correctness and actual source support are evaluated jointly on the same card/quiz items. |
| Unmatched quote may remain visible with a warning | FR-36; FR-37; later memlog source decisions | Superseded. The user chose bounded recovery followed by withholding persistent source-invalid content, rather than releasing it as unconfirmed. |
| Persistent invalid source handling | FR-36; FR-37 | Adopted. Cards/questions are filtered after bounded recovery; remaining valid items are delivered with a notice, and zero usable items produces an error/retry. Prior valid state is preserved. Summary failure granularity needs clarification below. |
| Page preview, original-PDF navigation or in-PDF highlighting | FR-12; later memlog source decisions | Deferred beyond v1. A simple source sidepanel and highlighting inside it are sufficient. |
| Conservative PDF handling | FR-38; FR-40; FR-41; addendum, PDF extraction and coverage | Refined by later decisions. Incidental unreadable figures/tables may be omitted with a notice when reliable main text remains. Material loss or uncertainty about adequate reliable main-text coverage stops generation. The research's blanket preference to stop on clear extraction errors is not the final product rule. |
| No usable text, damaged or unreadable content | FR-39; FR-41; FR-15 | Covered through controlled processing failure, explanation, retry/another PDF and preservation of a rejected replacement's old session. Error classification and exact observable stop signals remain downstream work. No scan diagnosis follows solely from empty text. |
| Password workflow | FR-43 | Resolved by the user: reject PDFs requiring a password; no password entry, unlocking or removal workflow. |
| OCR, advanced repair and complex layout handling | FR-38; scope statements | Outside v1. Ordinary text is prioritized; reliable simple table/figure content may be used, but missing material must not be invented. |
| Numerical upload/text/context/time limits | addendum, Resource and validation boundaries; PRD Final review items | Explicit Architecture follow-up before implementation depends on limits. T1–T3 are test-size bands, not limits. No numerical value can be taken from this research. |
| Quality checks, known errors and test evidence | SM-1–SM-6; manual evaluation protocol | Adopted/refined by later evaluation approval. Matching source locations does not excuse incorrect answers; known errors are corrected and retested. The test protocol retains first outputs, failures, omissions, corrections and retests. |
| Saved demo content | FR-42; SM-5; NFR-4 | Demo/source flows and live validation are separate. Apply the same location/support acceptance to saved aids; saved outputs do not prove live generation or parser reliability. Test execution is still pending. |

## Mechanisms retained for Architecture consideration

These research proposals remain candidates, not newly adopted product requirements:

- Choose one feasible extraction path for the actual stack and representative course PDFs. pypdf and PDF.js were conditional candidates, neither selected nor benchmarked. Extra fallback parsers, OCR and a vector database were not justified by the research.
- Retain one record per physical page, including blank/failed pages; assign internal document/source IDs independently of filenames. If model input is segmented, retain page identity. Derive display metadata from trusted application records rather than model-provided filenames or page labels.
- Consider exact page-local substring matching first, with an explicitly documented NFC/whitespace fallback if representative fixtures justify it. General compatibility folding, fuzzy matching, punctuation/number deletion, silent dehyphenation or translated quotations were not proven safe.
- Preserve original extracted text for source display separately from any normalized matching representation. Normalized offsets do not establish a mapping for highlighting the visible original PDF; that feature is deferred anyway.
- Use understandable status wording that distinguishes an excerpt's location from factual support. The research's specific wording and internal match-method records are optional, not chosen UI text.
- Establish finite retry/resource limits and extraction stop signals through representative-file checks. No universal character-count or readability threshold was established.

Recheck the chosen library's living API documentation and selected release during Architecture. The report's earliest dated-source recheck was 2027-01-21; that date does not remove the need to recheck living/draft parser APIs when selecting an implementation.

## Remaining product ambiguities

1. **Summary recovery unit:** FR-36 says persistent unverifiable content is not released, but only cards/quizzes have an explicit partial-success policy. Clarify whether one persistently invalid summary passage withholds the entire newly generated level or permits a reduced summary. Either choice must preserve the previous valid summary when the new generation is treated as failed. This is an observable product boundary, not a parser choice.
2. **Mixed-validity references on one item:** FR-35 allows several references, while FR-37 omits an item whose reference remains unverifiable. Clarify whether a card/question with one valid reference and one persistently invalid reference is wholly withheld, or whether the invalid reference may be removed after checking that the remaining references still support the whole content. Valid occurrence alone must not be substituted for that support decision.

These ambiguities were not resolved by the research and are not silently decided in this reconciliation. They do not reopen the approved sourcepanel, bounded recovery, valid-subset or coverage rules.

## Downstream verification follow-ups

Architecture owns fixture selection and mechanisms; Camilla owns the permissioned evaluation protocol before full scoring. Carry the following source-derived checks into that work without claiming they have run:

- Compare T1–T3 extracted text with the visible source, including columns, technical terms, Norwegian characters and any simple tables/figures used.
- Check a cover page, printed-number offset, blank middle page and duplicate filename for stable physical page identity.
- Exercise exact/allowed-normalized quotes, wrong-page quotes, repeated headers, invented/missing excerpts and changed numbers or negation. A quote elsewhere in the document must not pass the cited-page check.
- Include a semantically wrong answer with an exact matching excerpt: occurrence can pass while factual-support evaluation must fail.
- Check original-language excerpts for both output languages and the same source rules on saved demo aids.
- Test image-only, mixed-content, garbled, damaged and password-required fixtures against coverage notices, conservative stopping, understandable recovery and prior-state preservation. Empty pages alone must not be treated as a complete coverage detector.

No additional product capability is missing from this input once the two failure-boundary ambiguities above are resolved. Exact normalization, source-record design, excerpt length, extraction thresholds and numerical limits remain explicit downstream decisions.
