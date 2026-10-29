# Citation validation evidence — round 1

Accessed: 2026-10-29. Primary sources retrieved through web search and direct open. No application experiment.

## U1 — Unicode normalization

- Source: https://www.unicode.org/reports/tr15/tr15-58.html (version linked by the retrieved current annex).
- Publisher: Unicode Consortium. Published: 2026-08-12. Class: standard semantics. Confidence: medium, authoritative single source; no independent verification of the standard's definitions is claimed.
- Documented: NFC represents canonical equivalence. NFKC additionally folds compatibility differences, including distinctions that can matter in mathematics. Normalization is not a general semantic-equivalence test.
- Implication (recommendation): compare source and excerpt after the same conservative NFC/whitespace transformation. Do not strip punctuation, digits or case, or apply blanket NFKC to technical course material. Exact comparison first; any normalization is an explicit application policy.

## G1 — Structured model output

- Source: https://ai.google.dev/gemini-api/docs/structured-output
- Publisher: Google, Google AI for Developers. Updated: 2026-10-21 (confirmed in page footer). Class: API behaviour. Confidence: medium, official single source; API/model compatibility not evaluated.
- Documented: structured output uses JSON Schema; application-side validation remains necessary for semantically incorrect values.
- Implication (recommendation): a schema containing source IDs and excerpts does not establish that either exists. Validate against the app's page records, and distinguish occurrence from factual support. This is provider-independent proposed behaviour; Gemini is not selected here.

## M1 — Independent evidence of extraction ambiguity

- Source: https://pdfminersix.readthedocs.io/en/latest/topic/converting_pdf_to_text.html
- Publisher: pdfminer.six maintainers. Published: undated page. Class: extraction pattern. Confidence: medium individually; useful independent cross-check against pypdf's explanation.
- Documented: layout analysis reconstructs words, lines and boxes from character positions using configurable heuristics; extraction is not simply reading ready-made paragraphs.
- Implication (inference): matching an excerpt to extracted text cannot establish that the extractor preserved the visual reading order or that the excerpt supports the generated answer.

## P1 — Parser robustness

- Source: https://pypdf.readthedocs.io/en/stable/user/robustness.html
- Publisher: pypdf maintainers. Published: undated page. Class: parser behaviour. Confidence: medium, official single source.
- Documented: strict mode raises exceptions on nonconformance; forgiving mode uses best-effort processing and warnings.
- Implication (recommendation): successful parsing and a nonempty result are insufficient acceptance checks. Capture extraction failure separately from low-confidence readability; do not describe best-effort parsing as reliable repair.

## Open follow-up

Follow-up complete: the retrieved Google best-practice section explicitly requires application validation and handling of semantically incorrect output. Unicode's normalization section explicitly warns against blindly applying NFKC/NFKD because meaningful distinctions may be removed. Page-API and unreadable-PDF evidence is in extraction-r1.md. No claim is made about a minimum text threshold, performance, model quality, or correctness on T1–T3.
