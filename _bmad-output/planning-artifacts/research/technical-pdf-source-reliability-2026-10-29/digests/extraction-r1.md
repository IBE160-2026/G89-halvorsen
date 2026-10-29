# PDF text extraction evidence digest

Research date/access date: 2026-10-29. Scope: page-level extraction for a small beginner web app. All findings below come from primary documentation retrieved in this run; project framing is not evidence. No stack, version, performance, or extraction-accuracy winner is selected. Seven cited pages; source paraphrases stay below 130 words per page.

## Documented findings

### S1 — pypdf text extraction

- URL: https://pypdf.readthedocs.io/en/stable/user/extract-text.html
- Publisher: pypdf project; publication date: undated; accessed: 2026-10-29.
- Evidence class: official library guide; confidence: high for documented behavior, not measured accuracy.
- The guide extracts a page using `reader.pages[0].extract_text()` and explicitly calls `reader.pages[3]` page four. Layout mode supplies a fixed-width approximation. Absolutely positioned text complicates rows, columns, whitespace, and reading sequence; unknown fonts may lack font dictionaries, and scrambled fonts can impede extraction. Image-only content is not OCR-extracted; existing OCR text layers can be extracted but may contain compounded errors. Complex-document visitor coordinates may be wrong. Thus page access is documented, while dependable paragraph/table reconstruction is not established by this guide. [S1](https://pypdf.readthedocs.io/en/stable/user/extract-text.html)

### S2 — PDF.js document pages and labels

- URL: https://mozilla.github.io/pdf.js/api/draft/module-pdfjsLib-PDFDocumentProxy.html
- Publisher: Mozilla PDF.js project; publication date: undated; accessed: 2026-10-29.
- Evidence class: official API reference (draft); confidence: high for API contract, conditional on chosen installed release.
- `numPages` is the PDF file's total page count. `getPage(pageNumber)` starts at one; `getPageIndex(ref)` starts at zero. `getPageLabels()` separately returns labels corresponding to page indexes, or null when absent. File position and optional page labels therefore have distinct documented representations. [S2](https://mozilla.github.io/pdf.js/api/draft/module-pdfjsLib-PDFDocumentProxy.html)

### S3 — PDF.js page text

- URL: https://mozilla.github.io/pdf.js/api/draft/module-pdfjsLib-PDFPageProxy.html
- Publisher: Mozilla PDF.js project; publication date: undated; accessed: 2026-10-29.
- Evidence class: official API reference (draft); confidence: high for contract, not text fidelity.
- `pageNumber` starts at one. `getTextContent()` resolves to that page's text content, with whitespace replaced by standard spaces. `getStructTree()` can return null when the page has no structure tree. A plain text API response should therefore not be treated as preserved original whitespace or proof of available semantic structure. [S3](https://mozilla.github.io/pdf.js/api/draft/module-pdfjsLib-PDFPageProxy.html)

### S4 — PDF.js extraction items and parse handling

- URL: https://mozilla.github.io/pdf.js/api/draft/module-pdfjsLib.html
- Publisher: Mozilla PDF.js project; publication date: undated; accessed: 2026-10-29.
- Evidence class: official API reference (draft); confidence: high for documented fields/options.
- `getDocument()` loads PDF data, including binary input. `TextContent.items` contains text items and optionally marked-content items; text items expose `str`, direction, transform, dimensions, font name, and `hasEOL`. `stopAtErrors` can reject extraction-related promises on unparseable data instead of attempting recovery; the documented default is false. A password option supports protected PDFs. The API documents components, not a universal guarantee of column/table reading order. [S4](https://mozilla.github.io/pdf.js/api/draft/module-pdfjsLib.html)

### S5 — pypdf malformed files

- URL: https://pypdf.readthedocs.io/en/stable/user/robustness.html
- Publisher: pypdf project; publication date: undated; accessed: 2026-10-29.
- Evidence class: official library guide; confidence: high.
- `strict=True` raises exceptions for specification violations; `strict=False` attempts best-effort recovery and logs warnings. Recovery is not a documented guarantee of correct interpretation. [S5](https://pypdf.readthedocs.io/en/stable/user/robustness.html)

### S6 — pypdf passwords

- URL: https://pypdf.readthedocs.io/en/stable/user/encryption-decryption.html
- Publisher: pypdf project; publication date: undated; accessed: 2026-10-29.
- Evidence class: official library guide; confidence: high.
- The example checks `reader.is_encrypted` and calls `reader.decrypt()` with an appropriate password. AES handling requires an extra cryptographic dependency. [S6](https://pypdf.readthedocs.io/en/stable/user/encryption-decryption.html)

### S7 — PDF.js password/loading states

- URL: https://mozilla.github.io/pdf.js/api/draft/module-pdfjsLib-PDFDocumentLoadingTask.html
- Publisher: Mozilla PDF.js project; publication date: undated; accessed: 2026-10-29.
- Evidence class: official API reference (draft); confidence: high.
- Loading exposes a completion promise. `onPassword` requests a password when none or a wrong password was supplied, passing a callback and reason. Initialization can throw an exception, as described by `getData()`. [S7](https://mozilla.github.io/pdf.js/api/draft/module-pdfjsLib-PDFDocumentLoadingTask.html)

## Proposed solution implications — not documented product behavior

- **Physical position:** emit one record for every source page, including empty/error pages, with immutable `file_page_number` starting at one. Python candidate: enumerate `reader.pages` from one; JavaScript candidate: iterate `1..numPages` with `getPage(n)`. Keep printed/optional page labels separate. Basis: S1–S3; confidence: high; evidence class: design inference.
- **Conditional candidates:** pypdf offers a Python page-to-text path (S1); PDF.js offers a JavaScript page-to-items path requiring explicit reconstruction policy (S2–S4). Choose only after implementation-context and representative-file checks. Confidence: high; evidence class: design inference; no comparative benchmark retrieved.
- **Incomplete extraction:** record per-page status and warnings, preserve original text, and avoid silently treating blank text as a blank physical page. Mixed text/image or mixed-page documents should be assessed page by page; extracting some text does not establish that every visible word was captured. Basis: S1, S3–S5; confidence: medium; evidence class: conservative design inference. This run does not establish PDF.js OCR capability.
- **Failure UX:** separate password-required/wrong-password, document parse failure, page extraction failure, and successful-but-empty text. Decide whether protected files are supported or clearly rejected. Treat recovery warnings as review signals. Basis: S4–S7; confidence: high; evidence class: design inference.
- **Validation proposal:** compare output and page identity against actual PDFs containing a cover/printed numbering offset, columns, tables, unusual fonts, image-only and mixed content, malformed data, and password protection. These are proposed tests, not completed empirical evidence. Basis: S1–S7; confidence: medium for coverage; evidence class: proposed validation.
