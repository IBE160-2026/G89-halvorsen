# Local processing and lifecycle — round 1

Accessed: 2026-11-02. Primary documentation only. No implementation or network tests performed. Records distinguish documented capabilities from proposed project behaviour.

| ID | Claim | Source / publisher | Published/updated | Confidence / class |
|---|---|---|---|---|
| L1 | PDF.js getDocument accepts binary PDF data via its data parameter as well as URL loading. This supports local-byte processing as a capability, not proof that a specific app makes no network calls. | https://mozilla.github.io/pdf.js/api/draft/module-pdfjsLib.html — Mozilla PDF.js draft API | Undated | Medium, single publisher; API |
| L2 | localStorage persists across browser restarts; sessionStorage is tab/origin scoped and normally cleared on tab closure. | https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API — MDN / Mozilla | 2025-02-22 | Medium, single publisher; patterns |
| L3 | OWASP recommends a file-type allowlist, distrust of client Content-Type, size limits, maintained libraries and protected storage outside public webroot when server storage is used. It warns that external scanning services can disclose data. | https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html — OWASP | Undated | Medium, single publisher; security-patterns |

## Proposed application (inferences, not source claims)

Choose between browser extraction plus text-only relay and a local backend extracting PDFs in memory. Neither requires persistent document storage. Browser extraction reduces raw-PDF transfer; local backend extraction may be easier depending on stack. Both external model calls disclose selected text. Keep original filename only locally for required references; send document ID and page-indexed text, map ID back locally. Do not promise anonymisation from text extraction or omitted metadata. Browser code dependencies, remote assets, logs and HTTP payloads still need inspection.

Prefer one document in memory, explicit reset/replacement cleanup for PDF/text/outputs/object URLs and late-request handling. No automatic localStorage/IndexedDB/service-worker document persistence in v1. Local backend is on the student's computer only if deployed that way; a hosted backend changes the recipient boundary. Original user disk file is outside app cleanup. Retained evaluation fixtures and saved demo are deliberate separate artifacts with a retention/rights record. No universal safe file/page/input/time limit is established; choose and test later.

## Verification and gaps

PDF.js capability is directly documented but not independently corroborated here; version-specific compatibility not asserted. MDN storage principle is stable but doc age exceeds a one-month API freshness bar if treated as compatibility; report it only as a storage pattern. All living docs need Architecture-time recheck. No filesystem, browser recovery, crash cleanup or provider deletion behaviour measured. Stop local dimension at coverage; runtime evidence belongs to implementation.
