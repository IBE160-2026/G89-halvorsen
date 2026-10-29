---
title: 'Technical research: PDF source reliability'
type: technical
topic: PDF source reliability
decision: Define feasible PDF extraction and citation behaviour for AI Study Buddy PRD
source: Native research using official documentation and standards
status: complete
preset: standard
validation: normal
created: 2026-10-29
updated: 2026-10-29
claims_verified: 3
claims_unverified: 3
---

# PDF source reliability — AI Study Buddy

## Executive summary

**Recommendation for PRD:** require page-based source records, application-validated references, and explicit failure/coverage messages. Keep the final PDF library and model choice for Architecture. This is a proposed approach, not an adopted requirement or a tested implementation.

Page-level text APIs make a small implementation plausible. Extraction can still scramble layout or omit image content. [1][2][3][5] A matching excerpt shows that the quoted text occurs in the extracted page text. It does not show that extraction accurately reflects the visible PDF or that the quotation supports the answer. That distinction is central to the proposed design.

Use physical PDF page positions starting at 1, retain the original extracted text, and compare each excerpt only with its cited page. Keep excerpts in the source language even when study aids are translated. Warn when a nonempty quote cannot be found; reject nonexistent source locations. These are recommendations based on the findings below.

**Evidence boundary:** documentation research only. The research used no uploaded PDFs or T1–T3 fixtures. No libraries were installed, models called, accuracy measured or application tests run. Representative files must validate feasibility before architecture is finalized.

## 1. Decisions to take into PRD

The following are recommendations for discussion, not changes to the approved brief:

| Decision | Recommended starting point | Basis |
|---|---|---|
| What exactly is checked? | Require occurrence on the cited physical page, with explicit status wording. | F1–F5; high confidence in the distinction, no app results. |
| What may matching normalize? | Exact first; NFC and whitespace only as a documented fallback. | F5; conservative judgment, medium evidence confidence. |
| How are references formed? | App-owned source IDs and page metadata; original-language excerpts; one reference per page. | F2–F4 plus design inference. |
| What happens to malformed references? | Do not present invalid locations as working references. A nonempty excerpt that cannot be found on a valid page triggers a warning; the AI answer may remain visible as unconfirmed. Handling the answer when the source location itself is invalid remains open. | Brief's existing-location requirement plus F4; provisional discussion outcome. |
| What is a partially readable document? | Prefer conservative handling: stop on clear extraction errors, explain the problem and avoid presenting incomplete coverage as complete. Exact stopping criteria require representative-file testing. | F1/F6, beginner scope and the user's provisional preference. |
| What does quality acceptance require? | Assess answer correctness and supporting references on the same sampled items, while retaining separate scores. | Proposed refinement of the brief, not a research-derived threshold. |
| What does v1 promise for difficult files? | Explicit errors, no OCR/password workflow by default; document diagram/table limitations. | F1/F6/F7 and beginner scope. |

Architecture should select one extraction path, implementation limits and model strategy after representative-file checks. PRD should describe observable behaviour without prescribing an untested parser or model.

**Discussion outcome, 2026-10-29:** the user considers simple page-local quotation checks and clear warnings realistic for v1 and provisionally prefers conservative PDF handling to limit complexity. These are research recommendations only, not final requirements. Reassess them after testing representative PDFs; this closes the current research discussion without starting PRD.

## 2. Evidence and scope

The current Product Brief, addendum and previous session notes define the research questions; they are not evidence of technical correctness. See [brief.md](brief.md) for scope and [digests/](digests/) for retrieved claims and provenance.

All external evidence is primary documentation retrieved on 2026-10-29. **Documented findings** describe those sources. **Possible solution** sections are design proposals. **Recommendations** require a later product decision.

Confidence is high where independent maintainers corroborate a general finding; medium for an authoritative source without independent corroboration. In the claim ledger, `unverified` means not independently corroborated, not that the cited page was unread. No version, speed or comparative accuracy claim is made. Living/draft API references must be rechecked against the selected release.

## 3. Extract text and retain the correct page

### Documented findings

- **F1 — Extraction has limits (high).** pypdf documents page-wise extraction, layout complications, image-only limitations and imperfect pre-existing OCR layers. pdfminer.six independently describes layout reconstruction through character-position heuristics. Readable-looking PDFs therefore need not yield reliable paragraph order. [1][5]
- **F2 — Page identity can be retained (high).** pypdf accesses page objects by zero-based index; PDF.js exposes one-based `getPage()` and separate optional page labels. PDF.js provides text per page, with whitespace normalization. [1][2][3]
- **F3 — JavaScript text reconstruction needs care (medium).** PDF.js returns text items with text/position metadata and line-end information. Its API is an extraction building block, not a promise of faithful table or column reconstruction. [4]

### Possible solution

Keep one record per physical page, including blank and failed pages:

```text
document_id | original_filename | file_page_number
extracted_text | extraction_status | warnings
```

The application assigns `file_page_number` from file order before filtering. Removing an empty cover page must never renumber later references. A filename is a display label; an internal document ID prevents collisions between files with identical names.

Two conditional candidates are sufficient for Architecture to investigate:

| Candidate | Documented route | Remaining work |
|---|---|---|
| pypdf, if a Python backend fits | Page object → extracted text. [1] | Validate actual course PDFs and error behaviour. |
| PDF.js, if JavaScript fits | Page object → text items. [2][3][4] | Define text-item joining and test reading order. |

Neither is selected or benchmarked here. Avoid adding multiple fallback parsers, OCR or a vector database before the selected course files demonstrate a need. This complexity recommendation is project judgment, not a comparative library finding.

## 4. Generate references without inventing locations

### Documented finding

**F4 — Structured output is insufficient (medium).** Google's structured-output documentation requires application-side validation of values and handling of semantically incorrect responses. A valid JSON response does not establish that a page, source ID or excerpt exists. [7]

### Possible solution

1. Extract pages and assign source IDs in the application. If a page must be split for model limits, every segment retains its page ID and stays within that page.
2. Give the model page-tagged text and request an answer/statement with source ID(s) and short verbatim excerpts.
3. Resolve source IDs against the uploaded document. Derive filename and page number from application records rather than trusting model-supplied labels.
4. Validate source locations and quote occurrence before displaying reference status.
5. In **View source**, show filename, physical page position, original-language excerpt and the check result. A page preview/open-original action is an optional UX decision; precise visual highlighting is not necessary for this proposal.

For a statement using two pages, use two references rather than a single excerpt crossing the page boundary. A Norwegian study aid from English material should retain its English source quotation; a translated quotation is not a verbatim occurrence check. These are proposed rules for testability.

## 5. Check the excerpt on the cited page

### Documented finding

**F5 — Normalization has trade-offs (medium).** Unicode distinguishes canonical normalization (NFC) from compatibility normalization (NFKC); compatibility folding can remove meaningful distinctions, including in mathematical text. It cautions against applying it indiscriminately. [6]

### Recommended matching policy — not yet adopted

First reject invalid source IDs, noninteger/out-of-range page positions and empty/whitespace-only excerpts. Then perform an exact substring search on that page's extracted text. If needed, compare both strings after **NFC normalization and collapsing whitespace runs to a single space**, with leading/trailing whitespace removed.

Preserve case, punctuation, numbers and mathematical symbols. Do not silently remove hyphens, fold all ligatures, apply general NFKC, translate the quotation or accept fuzzy similarity as a successful match. Legitimate quotes can consequently fail at line-break hyphenation or extraction errors; surface the limitation rather than treating approximate text as found. Any later exception needs an explicit rule and tests.

| Check result | Proposed user behaviour |
|---|---|
| Exact/normalized match on cited page | Say “Excerpt found on page”; never “Answer verified”. Record the match method internally. |
| Existing page, nonempty excerpt not found | Provisionally allow the AI answer to remain visible with a clear unconfirmed-reference warning and source inspection. Do not present the excerpt as verified. |
| Missing/invalid source or empty excerpt | Treat as malformed generated output; never construct a working-looking reference to a nonexistent page. Whether to retry, show an error or retain the answer as unconfirmed remains a PRD discussion question. |
| Page unavailable after extraction failure | Do not report a match; explain that this source could not be checked. |

Searching the entire document cannot substitute for checking the claimed page. Repeated headers may occur on many pages without supporting an answer. Even a long, exact match cannot prove semantic support: occurrence, extraction fidelity and factual support are separate checks. This is a logical limitation of the proposed test, reinforced by F1 and F4; manual relevance review remains necessary.

Keep original extracted text for display and normalized text separately for matching. Do not use normalized character offsets to promise visual PDF highlighting without an additional mapping mechanism.

## 6. Handle unreadable and incomplete PDFs

### Documented findings

**F6 — Recovery is best effort (high for the general pattern).** pypdf distinguishes strict errors from forgiving parsing with warnings. PDF.js also exposes extraction error/recovery behaviour. Successful loading is therefore not evidence of complete extraction. [8][4]

**F7 — Encryption is a separate state (medium).** pypdf documents encrypted-document detection and password-based decryption. Supporting password workflows is a product choice; it is not required merely because a library can do it. [9]

### Recommended behaviour — subject to PRD decisions

| Situation | Proposed response and next step |
|---|---|
| Unsupported format | Explain that v1 accepts text-based PDFs; ask for PDF export. |
| Invalid/damaged PDF or fatal page parse error | Stop generation; suggest reopening and exporting a new copy. Hide technical traces from the user. |
| Password required | For a small v1, reject clearly and request an accessible copy the user is authorized to use. Password entry is optional scope, not a recommendation. |
| No usable text anywhere | Stop; explain that the app could not extract usable text and that image-only scans need a text-based alternative. Do not claim the file is definitely a scan. |
| Some pages have no extracted text | Preserve page positions and list affected pages. They may be blank, image-only or extraction failures; empty text alone does not distinguish these. |
| Some text exists but appears garbled/incomplete | Offer an extracted-text preview and request a cleaner export. Any heuristic is only a warning signal. |

The discussion's **provisional preferred approach is conservative handling: stop at clear extraction errors**, explain the issue and suggest a cleaner PDF export. Generating from readable parts after explicit confirmation remains an alternative, but is not the preferred starting point because it adds coverage and interaction states. A warning is still needed when partial coverage is detected; incomplete extraction must not be described as a complete document review. These are recommendations awaiting representative-file testing, not final requirements.

An empty page alone is not a confirmed extraction error. A text-bearing page can still contain an unread diagram, so a list of empty pages is not a complete coverage guarantee. The proposed handling cannot promise automatic detection of every omission or reading-order error. These limitations follow from F1.

No universal character-count or printable-character threshold is established by these sources. A short title slide must not automatically fail as unreadable. File size, page count, extracted-text/model-input size and processing-time limits must be selected and tested later; T1–T3 length categories do not determine them.

## 7. Proposed validation and remaining uncertainty

These checks have **not** been run:

- Compare extracted text and references with the selected T1–T3 files, including columns, tables, technical terms and Norwegian characters. Record omissions and reading-order errors manually.
- Use a cover page, printed numbering offset, blank middle page and duplicate filenames to check physical page identity.
- Check exact quotes, whitespace/canonical-character variants, wrong-page quotes, repeated headers, invented text, empty quotes and changed numbers/negation. Only allowed transformations may pass.
- Generate Bokmål and English study aids and check that quotations remain in source language.
- Test image-only, mixed-content, garbled-font, damaged and password-protected fixtures. Verify understandable next steps and no silent claim of full coverage.
- Include a semantically wrong answer with an exact matching quote: occurrence may pass, while manual factual-support review must fail. This prevents conflating the two quality checks.

The same citation checks should apply to saved demo content. Existing 9/10 thresholds do not excuse known errors or invalid locations. Actual extraction accuracy, meaningful readability thresholds, acceptable limits and the most useful excerpt length remain open until fixtures and a small prototype exist. Wider student validation and full learning-science research are outside this run.

The discussion leaves these specific questions open:

- Which observable extraction failures should stop processing, and how should blank/title pages be distinguished from suspected missing text without promising a reliable automatic classifier?
- How often do whitespace, hyphenation and table layout cause missed quotations in actual course PDFs, and which normalization rules are justified by those results?
- What should happen to the AI answer when the cited location is invalid, as distinct from an unmatched quotation on a valid page?
- Is partial processing useful enough to justify its additional complexity, or should conservative handling remain the v1 approach after testing?
- Do students understand the difference between an excerpt being found and the answer being factually supported?

Next: choose representative PDFs and test extraction and reference behaviour, then reconsider the provisional recommendations. This report can later inform `bmad-prd` in a fresh context; closing this research does not finalize product requirements or start PRD.

## 8. Source appendix

The dated ledger claims are evaluated by the BMAD helper in [staleness.json](staleness.json). Undated living documentation is excluded from date arithmetic rather than assigning a fictional publication date; recheck it when choosing the library/release in Architecture. The dated-source windows are three months for AI-adjacent API behaviour and 24 months for stable normalization patterns. See the generated file for exact recheck dates. The earliest dated-source recheck is **2027-01-21**; recheck living API references sooner when Architecture begins.

Source dates are publication/update dates where visible; “undated” is not an inferred release date. All were accessed 2026-10-29. Individual API claims remain medium confidence unless independently corroborated as noted above.

| Ref | Supports | Publisher and source | Published/updated | Accessed | Confidence |
|---|---|---|---|---|---|
| [1] | Page-wise extraction; layout/image limitations | [pypdf — Extract Text](https://pypdf.readthedocs.io/en/stable/user/extract-text.html) | Undated | 2026-10-29 | Medium individually; F1/F2 corroborated |
| [2] | Physical page access and separate labels | [Mozilla PDF.js — PDFDocumentProxy](https://mozilla.github.io/pdf.js/api/draft/module-pdfjsLib-PDFDocumentProxy.html) | Undated; draft API | 2026-10-29 | Medium individually; F2 corroborated |
| [3] | Per-page text and whitespace behaviour | [Mozilla PDF.js — PDFPageProxy](https://mozilla.github.io/pdf.js/api/draft/module-pdfjsLib-PDFPageProxy.html) | Undated; draft API | 2026-10-29 | Medium |
| [4] | Text items and extraction error/recovery options | [Mozilla PDF.js — pdfjsLib](https://mozilla.github.io/pdf.js/api/draft/module-pdfjsLib.html) | Undated; draft API | 2026-10-29 | Medium individually; F6 corroborated |
| [5] | Independent corroboration of layout heuristics | [pdfminer.six — Converting a PDF file to text](https://pdfminersix.readthedocs.io/en/latest/topic/converting_pdf_to_text.html) | Undated | 2026-10-29 | Medium individually; F1 corroborated |
| [6] | Canonical/compatibility normalization and cautions | [Unicode Consortium — UAX #15, revision 58](https://www.unicode.org/reports/tr15/tr15-58.html) | 2026-08-12 | 2026-10-29 | Medium; normative primary source |
| [7] | Structured output still requires semantic validation | [Google — Structured outputs](https://ai.google.dev/gemini-api/docs/structured-output) | 2026-10-21 | 2026-10-29 | Medium |
| [8] | Strict versus best-effort parsing | [pypdf — Robustness](https://pypdf.readthedocs.io/en/stable/user/robustness.html) | Undated | 2026-10-29 | Medium individually; F6 corroborated |
| [9] | Encryption/decryption handling | [pypdf — Encryption and decryption](https://pypdf.readthedocs.io/en/stable/user/encryption-decryption.html) | Undated | 2026-10-29 | Medium |
