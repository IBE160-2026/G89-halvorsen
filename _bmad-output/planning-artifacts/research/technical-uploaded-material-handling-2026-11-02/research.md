---
title: 'Technical research: Uploaded material handling'
type: technical
topic: Uploaded material handling
decision: Define manageable uploaded-material handling inputs for the later AI Study Buddy PRD
source: Native web research
status: complete
preset: standard
validation: normal
claims_verified: 0
claims_unverified: 16
created: 2026-11-02
updated: 2026-11-02
---

# Uploaded material handling – AI Study Buddy

## Executive summary

**Recommendation:** use permissioned, non-sensitive PDFs; process them locally; keep working content only for the active document; and send page-indexed text to the chosen external model only when live generation is requested. Use one clearly shareable document for the saved demo. These are proposals for PRD discussion, not adopted requirements or an Architecture decision.

Local extraction reduces what leaves the device but does not make external generation private or offline. Provider data-use promises, retention and file-object deletion are different controls. Gemini's current documentation describes 55-day abuse retention and separate optional project logs; a 48-hour uploaded-file expiry is not deletion of every copy. [8][9][10][11]

For IBE160, avoid a document database, user accounts, hosted multi-user uploads and automatic study-history persistence. Prefer own-authored or appropriately licensed fixtures, a small data-flow notice, explicit local clearing, content-free operational logs and a documented provider-settings check. This keeps the planned source-reference workflow achievable without claiming zero retention or legal clearance.

**Main decisions still needed:** the actual test/demo PDFs and rights, provider/project eligibility and settings, browser versus local-backend extraction, cleanup behaviour and evidence-retention dates. No PDFs were uploaded to a model, no application tests were run, and no Product Brief or PRD was changed.

## 1. Evidence and project boundary

The updated Product Brief, addendum, teacher feedback, both earlier research reports and open session issues shaped the questions, not the external findings. [brief.md](brief.md) records these inputs. Previous research's need to retain evaluation outputs must be reconciled with rights and retention, since outputs and quotations can reproduce source material.

**Documented findings** describe retrieved sources. **Recommendations** are project judgments for later PRD/Architecture. **Open questions** require decisions or implementation evidence. All source-specific claims are medium confidence: primary-source supported, but not independently corroborated under BMAD's strict different-publisher rule. Reopening a vendor page is an attribution check, not independent verification. See [digests/](digests/) for claims, dates and retrieval limits. No supplied report was imported; `imports/` is empty.

## 2. Local processing and external transfer

**Documented findings:** PDF.js accepts binary PDF data as well as URL input, enabling local-byte processing as a capability. It does not prove that a particular app has no network traffic. [1] MDN documents that localStorage persists across browser restarts, so browser-local does not necessarily mean temporary. [2]

**Recommended boundary:** extract text locally and preserve physical page indexes for the existing source-reference design. Browser extraction plus a small API relay reduces raw-PDF transfer; an in-memory local backend can be simpler for another stack. Prototype one path before choosing. A backend is local only when running on the student's computer; hosting it creates another recipient.

| Stage | Proposed content handling | User-visible meaning |
|---|---|---|
| Browser / local process | Original PDF, filename, page text and study aids for the active document. | Selecting a file and extracting text can happen before model transfer. |
| App API relay | Bounded page-indexed text, document ID, language and generation options; API secret outside browser code. | Live generation sends content to the named external provider. |
| Model provider | Submitted text, response and associated service data under applicable terms. | Local extraction does not imply offline generation or zero retention. |

Keep the filename-to-document-ID mapping locally for filename/page references. Omit unnecessary filenames, paths and metadata from requests; the extracted text still needs inspection. Do not silently truncate coverage while implying the whole PDF was processed. Text extraction is neither anonymisation nor a copyright permission.

OWASP recommends allowlisting formats, checking beyond the client MIME header, size limits, maintained libraries and protected storage when server files are necessary. [3] Apply proportionate controls: PDF-only validation, understandable failures, bounded input/processing and no publicly served upload directory. Exact byte/page/text/time limits need prototype tests; this report sets none. Antivirus infrastructure and accounts are not new v1 requirements.

## 3. External AI terms: Gemini as a provisional candidate

These findings concern **Gemini Developer API**, with AI Studio only where its documentation governs the API project. Consumer Gemini chat settings and Vertex AI controls are not interchangeable evidence. No provider/model is selected.

| Documented finding | Consequence for the candidate design |
|---|---|
| Terms effective 2026-03-23 require Paid Services for EEA-facing API clients; API paid status means a project with active billing. A separate EEA clause extends paid data-use protections to otherwise unpaid use. [8] | Do not equate EEA data-use protection with permission to deploy an unpaid API client. Confirm project eligibility and cost in Architecture. |
| Under paid data-use terms, prompts/responses are excluded from product improvement, but security logging and worldwide facility processing remain possible. [8] | No-training language establishes neither no retention nor EEA-only processing. |
| Abuse monitoring retains prompts, context and outputs for 55 days; authorised employees can review flagged content. The stated training exclusion has a policy-enforcement-model exception. [9] | Disabling optional logs cannot justify a no-human-access or zero-retention promise. |
| Files API objects expire after 48 hours and can be manually deleted. [10] | This is a file-object lifecycle, not an erasure promise for abuse logs or other copies. |
| Optional developer logs are distinct from abuse logs. Generate Content logging defaults on for projects created from 2026-10-26. Logs default to being marked for deletion after 55 days; datasets have no set retention. Sharing datasets invokes additional improvement/training terms. [11] | Inspect settings on the actual project; propose disabling optional request/response logging, creating no datasets and enabling no voluntary sharing/Contributor Tier. |

Terms also restrict developers to 18+ and prohibit API clients directed to or likely accessed by under-18s. Confirm the intended adult test audience and service suitability before adopting this provider; this is a vendor condition, not a general age rule for study apps. [8]

**Recommendation:** use a simple text request without Files API uploads, explicit caching, stateful interactions or external search grounding unless later justified. This reduces additional stored objects, not all provider processing. Google's zero-data-retention documentation distinguishes these feature lifecycles and does not establish guaranteed zero retention for this Developer API design. [12] Ordinary provider-managed processing/cache behaviour can remain.

**Unresolved:** the EEA data-use exception and voluntary-sharing rules are not fully reconciled in the inspected pages. Keep optional sharing out of the proposal. Actual regional qualification, destinations, contract applicability and deletion propagation were not established. Another provider would need its own terms review; no vendor survey is necessary now.

## 4. Proposed storage and deletion lifecycle

The table is a **design recommendation**, not observed behaviour. Keep source inspection available while the active study aids are visible; deleting their source while keeping working references would undermine the brief's verification goal.

| Copy / location | Proposed lifetime and removal | Boundary to disclose |
|---|---|---|
| User's original disk PDF | App reads it; app clearing leaves that original under user control. | Clearing the app does not delete the user's file. |
| Active PDF bytes, extracted/normalised text, filename mapping, study aids and object URLs | In memory for one active document. Explicit Clear and document replacement release all associated state; invalidate in-flight results. | Best-effort application cleanup, not forensic erasure of OS/browser memory. |
| Browser persistent stores and caches | No automatic PDF/text/output storage in localStorage, IndexedDB or service-worker caches in v1. Review HTTP caching and restore behaviour. | A restart/refresh should require a new upload; verify it rather than promise it from design alone. |
| Local backend request and temporary files | Prefer memory. If framework writes temporary files, delete after extraction or on success/error/cancellation and provide bounded recovery cleanup after crashes. | Document and test any residual-file exception; do not claim all crash paths are covered without evidence. |
| Application/SDK logs and error reports | Record case IDs, status, timing and error category; exclude PDFs, prompts, responses, excerpts, keys and identifying paths. Inspect debug defaults. | OWASP recommends excluding/sanitising secrets and sensitive information in logs. [4] |
| Provider data | Follow the reviewed terms/settings; avoid extra stored objects. Delete provider file objects if introduced and report failures honestly. | App Clear cannot undo a completed transfer or establish deletion of provider security logs. [9][10][11] |
| Evaluation evidence and saved demo | Explicitly retained, permissioned artifacts separate from runtime uploads. Set owner, purpose, access and review/deletion date. | Clearing a study session does not remove deliberately saved fixtures, screenshots or repository copies. |

No arbitrary statutory retention duration is inferred. Choose a date for evaluation evidence based on assessment needs and applicable institutional rules; after that date delete unnecessary private copies or retain only a cleared example and minimal non-content results. Use synthetic case IDs in a shared defect log. Keep private fixtures and outputs outside tracked/shared folders; `.gitignore` is a guard, not proof of permission or removal from history.

A simple proposed notice before live generation: **“This document is processed locally first. Generating study aids sends extracted text to [provider]. Clear removes this app's active content; it does not delete your original PDF or override the provider's retention.”** Replace the wording with the selected implementation and current provider facts. Demo mode should clearly use its predefined PDF and saved results; never silently send a newly selected file or imply saved results came from it.

## 5. Privacy and material rights

### Documented findings

Personal information includes direct and indirect identifiers; absence of accounts does not determine whether a PDF contains personal data. Datatilsynet identifies lawful basis, transparency, minimisation and storage limitation as core principles. [5][6] Where GDPR transfer rules apply, Datatilsynet explains that transfers outside the EEA need the applicable transfer basis/conditions. [7] This does not establish an exemption for this app or other people's data. **Design implication:** do not treat an uploader acknowledgement alone as establishing lawful processing of information about people mentioned in a PDF.

Norwegian government guidance recommends cleared input and checking rights in generated outputs. [14] Kopinor's university/college model agreement limits use to its defined institutional/internal setting and does not authorise public internet publication; its AI-training exclusion does not itself resolve inference-time upload. The actual signed institutional agreement was not examined. [13] These sources support treating access, external processing and redistribution as separate questions; they do not decide the legality of a particular course PDF.

CC BY 4.0 permits sharing/adaptation with attribution, licence link and change indication; its deed warns that other rights can still apply. CC0 waives copyright/related rights to the extent legally possible but does not settle privacy or verify a labelled work's provenance. [15][16]

### Recommended fixture policy

| Intended use | Proposed manageable rule |
|---|---|
| Local private test | Use material lawfully held; keep uncleared course content outside shared artifacts. Private access is not public-sharing permission. |
| Live external-model test | Prefer own-authored non-sensitive material without third-party content, or a verified licence/permission covering the planned use. Do not infer permission from LMS access or no-training settings. |
| Examiner demo | Use one separately cleared PDF with matching saved study aids and source excerpts; record who may receive and retain it. |
| Public repository, report or screenshots | Share only cleared source content and outputs; preserve attribution and review every reproduced passage/image. Generated does not automatically mean unrestricted. |

Prefer an own-authored fixture with no copied course passages, third-party figures or personal cases. CC0 or verified CC BY material is an alternative; inspect exclusions and third-party content. Do not require every private T1–T3 file to be publicly distributable, but clear external processing and any retained evidence separately. An artificially simple demo does not replace representative T1–T3 evaluation.

Keep a small material register: **ID/title, author/rightsholder, source/version, licence or permission evidence, exclusions/changes, allowed local/API/demo/repository uses, attribution, access and retention date.** A practical CC BY credit is “Title — Author, source link, CC BY 4.0 licence link; changes: …”. Attribution is not a substitute for permission where no licence applies.

Inspect text, filename, annotations and metadata before live use. Omit unnecessary identifiers; rejecting sensitive/confidential material is more manageable than building an automatic redaction/classification system. Removing a name does not prove anonymity. For real personal data or wider hosted use, resolve responsible parties, lawful basis, notices, processor agreement and transfer conditions with institutional support first. No blanket student-project exemption, mandatory DPIA or completed compliance assessment is asserted here.

## 6. PRD inputs, validation and open decisions

**Cross-dimension insight:** source excerpts, saved AI outputs and screenshots are copies worth including in the same rights/retention inventory as the PDF. The prior evaluation report's recommendation to save outputs can be followed with cleared content and explicit retention; it should not become automatic permanent storage for ordinary uploads. Source verification needs temporary source access, not a document database.

The provider limits are a counterweight to an entirely local design promise; the educational/private-use context also does not establish unrestricted sharing. Conversely, the inspected licensing and paid data-use terms offer workable permission/protection routes. This research does not conclude that every API upload infringes or that every provider trains on every submission. No dedicated red-team pass was run; these limits arose during acquisition.

| Proposed downstream input | Basis / limitation | Decision owner or evidence needed |
|---|---|---|
| Distinguish local selection from live transfer; disclose recipient and copied data. | Documented capability plus provider terms; implementation untested. | PRD flow/notice; Architecture data flow. |
| One active document; no automatic persistence; Clear handles PDF, outputs and pending requests. | Project scope and minimisation judgment, not a validated implementation. | PRD lifecycle and error states; cleanup prototype. |
| Separate mandatory provider retention from optional logs/files; review billing, age and sharing eligibility. | Current single-vendor documentation, time-sensitive. | Architecture/README; actual project-settings record. |
| Permissioned test/demo register and explicit evidence-retention date. | Regulator, agreement and licence guidance; exact files unresolved. | Test plan/README; document owner and institutional rules. |

A small later verification set is sufficient. These are **unrun proposed checks**, not new adopted acceptance thresholds:

1. Inspect network payloads to confirm the chosen boundary and no live call in demo.
2. Exercise Clear/replacement/refresh plus delayed or failed requests and verify no old source/output reappears.
3. Inspect storage, temp directories and SDK/error logs on success/failure.
4. Record provider settings and test file-object deletion failures only if that feature is used.
5. Review demo/repository contents against the material register.

Open questions before final requirements:

- Which actual T1–T3 and demo PDFs have the required permissions, and what exact institutional agreement/exam-sharing rules apply? Obtain file-level evidence; ask the institution/rightsholder where unclear.
- Which provider/project configuration is suitable for the adult Norwegian/EEA test audience, and are its cost and retention acceptable? Recheck current terms before the first real upload.
- Browser extraction or local backend, and which observable events end a session? Prototype cleanup and source viewing; set byte/page/text/time limits from representative files.
- What happens to pending external requests and provider deletion failures? Local cancellation must not be described as recalling data already sent.
- Who can access saved evaluation evidence, and when should it be reviewed/deleted after assessment? Choose a concrete date after confirming institutional needs.

These refine existing open issues; they do not close file selection, final policy or actual testing. Next discuss the proposals, then use the three research reports as inputs to **bmad-prd** in a fresh context when ready. No PRD is started here.

## 7. Sources and freshness

All accessed **2026-11-02**. Dates below are displayed document/update/effective dates; undated is not an inferred publication date. Vendor sources describe promises/documented controls, not an independent audit. Legal conclusions for unseen files and this particular deployment remain unresolved. Background legal sources with retrieval limitations are recorded in the rights digest but not used as directly inspected statute evidence here.

| Ref | Supports | Publisher and primary source | Published/updated | Accessed | Confidence |
|---|---|---|---|---|---|
| [1] | Binary PDF input capability | [Mozilla PDF.js — pdfjsLib draft API](https://mozilla.github.io/pdf.js/api/draft/module-pdfjsLib.html) | Undated | 2026-11-02 | Medium |
| [2] | Browser persistence distinction | [MDN — Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API) | 2025-02-22 | 2026-11-02 | Medium |
| [3] | Upload validation and storage controls | [OWASP — File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) | Undated | 2026-11-02 | Medium |
| [4] | Logs as a sensitive-data copy | [OWASP — Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) | Undated | 2026-11-02 | Medium |
| [5] | Direct/indirect personal identifiers | [Datatilsynet — Personal information](https://www.datatilsynet.no/rettigheter-og-plikter/personopplysninger/) | 2025-03-31 | 2026-11-02 | Medium |
| [6] | Privacy principles | [Datatilsynet — Privacy principles](https://www.datatilsynet.no/rettigheter-og-plikter/personvernprinsippene/) | 2023-07-27 | 2026-11-02 | Medium |
| [7] | EEA transfer basis | [Datatilsynet — Transfers outside the EEA](https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/overforing-av-personopplysninger-ut-av-eos/) | 2026-01-29 | 2026-11-02 | Medium |
| [8] | EEA/paid/age/data-use boundaries | [Google — Gemini API terms](https://ai.google.dev/gemini-api/terms) | Effective 2026-03-23 | 2026-11-02 | Medium |
| [9] | Security retention and human review | [Google — Abuse monitoring](https://ai.google.dev/gemini-api/docs/usage-policies) | 2026-06-09 | 2026-11-02 | Medium |
| [10] | File-object expiry/deletion | [Google — Files API](https://ai.google.dev/gemini-api/docs/files) | 2026-10-26 | 2026-11-02 | Medium |
| [11] | Optional logging/datasets/sharing | [Google — Data logging and sharing](https://ai.google.dev/gemini-api/docs/logs-policy) | 2026-10-26 | 2026-11-02 | Medium |
| [12] | Feature-specific retention limits | [Google — Zero data retention](https://ai.google.dev/gemini-api/docs/zdr) | 2026-09-14 | 2026-11-02 | Medium |
| [13] | Scope of institutional copying permission | [Kopinor/UHR — Model agreement 2025–2029](https://kopinor.no/wp-content/uploads/2026/02/Monsteravtale-universiteter-og-hogskoler-2025-2029.pdf) | Negotiated June 2024; term 2025–2029; page publication date unconfirmed | 2026-11-02 | Medium |
| [14] | Input and generated-output copyright review | [Norwegian government — AI assistants, copyright guidance](https://www.regjeringen.no/no/dokumenter/ki-assistenter-i-arbeidslivet-en-praktisk-guide/id3109040/?ch=10) | 2025 in generated citation; exact date unconfirmed | 2026-11-02 | Medium |
| [15] | Attribution licence route and limits | [Creative Commons — CC BY 4.0 deed](https://creativecommons.org/licenses/by/4.0/) | Undated; version 4.0 | 2026-11-02 | Medium |
| [16] | CC0 route and remaining rights | [Creative Commons — CC0 1.0 deed](https://creativecommons.org/publicdomain/zero/1.0/) | Undated; version 1.0 | 2026-11-02 | Medium |

### Staleness map

See generated [staleness.json](staleness.json) and its input [dated-claims.json](dated-claims.json). Technical-pack windows: stable storage/security patterns 24 months; AI-adjacent provider behaviour 3 months. Regulatory/contract guidance gets a project-specific 3-month review window because it is decision-critical, not because law expires on that schedule. Dated old guidance is flagged rather than relabelled newly published; undated documentation is excluded from date arithmetic and must be rechecked at the decision point. The current agreement's 2025–2029 term is not an invented publication date. Its known negotiation month is used as the document date; month-only arithmetic uses the first day. The government guide's uncertain generated-citation year is excluded from date arithmetic.

Revalidate provider terms, logging defaults and relevant legal/licence conditions during Architecture and **before the first real API upload**, and again if deployment, account, features or recipients change. Computed dates flag sources for review based on their age; they do not establish when legal validity expires or guarantee future accuracy.

The helper flags **6 of 10 dated entries** beyond these conservative review windows. Earliest computed recheck: **2023-10-27** (already past); earliest future recheck: **2026-12-14**. All were retrieved in this run; revisit living sources at the earlier decision point above.
