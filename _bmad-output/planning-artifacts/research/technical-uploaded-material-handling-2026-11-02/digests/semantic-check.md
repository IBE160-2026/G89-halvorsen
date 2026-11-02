# Fresh-context semantic citation check

Access date: **2026-11-02** (client date). Scope: only `research.md`, followed by current external primary-source retrieval. No other project context, application inspection, uploads, implementation tests, skills or subagents were used. Four web calls retrieved eleven distinct pages (including one PDF), with targeted follow-up views/finds. Findings are source-to-statement checks, not an audit of provider behaviour or a legal clearance.

## Findings requiring attention

1. **Privacy-transfer wording needs a scope qualifier.** Section 5 says transfers outside the EEA need a valid transfer basis. This matches the regulator's headline for covered processing, but the same page expressly excludes a private person sending their own personal data and explains adequacy decisions and applicable exceptions. Suggested qualification: “Where GDPR transfer rules apply, establish the applicable basis/conditions for transfers outside the EEA.” This does not establish an exemption for this project, its future users or other people's data. The report appropriately leaves actual responsible parties and applicability unresolved. [Datatilsynet transfer guidance](https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/overforing-av-personopplysninger-ut-av-eos/), retrieved lines 59, 76–88.
2. **Government source is not wholly undated in current retrieval.** The page's generated reference identifies the ministry and **2025**, while warning that generated references can contain errors. No exact publication/update day was established. Record “2025 in generated citation; exact date unconfirmed,” rather than silently treating 2025 as an exact date. The report's substantive cleared-input/output-review statement is supported. [Government guide, chapter 10](https://www.regjeringen.no/no/dokumenter/ki-assistenter-i-arbeidslivet-en-praktisk-guide/id3109040/?ch=10), lines 153–155, 350–362.
3. **No material mismatch found in the selected Gemini and copyright claims.** The report correctly separates EEA deployment eligibility from data-use protection, optional logging from abuse retention, and file-object deletion from all-copy erasure. These distinctions must survive downstream summaries.
4. **Independent-publisher corroboration was not achieved for Gemini-specific facts.** All checked Gemini pages are Google publications. Other publishers support separate privacy/copyright boundaries; they do not independently verify Google's retention promises. Keep the report's medium-confidence/primary-source-supported designation. Re-retrieval and this fresh-context pass are not different-publisher corroboration.

## Source checks

### [8] Gemini terms — supported

[Google Gemini API Additional Terms](https://ai.google.dev/gemini-api/terms), effective **2026-03-23**. Retrieved lines 95–104 and 122–129 support the report: EEA-facing API clients must use Paid Services; API paid status requires active project billing; the separate regional provision applies paid data-use terms even to unpaid quota. Those clauses address different matters. Paid inputs/outputs are excluded from product improvement, while safety logging and facilities outside the EEA remain possible. The source also supports the stated 18+ developer/client-audience condition (line 99). These terms do not establish this project's eligibility, actual destinations, settings or contract compliance. No inference that the EEA exception authorises an unpaid deployment is warranted.

### [9] Abuse monitoring — supported

[Google Abuse monitoring](https://ai.google.dev/gemini-api/docs/usage-policies), last updated **2026-06-09 UTC**. Lines 98–105 specify 55-day retention of prompts, added context and outputs, authorised employee review of flagged content, and a training exclusion with a policy-enforcement-model exception. Scope includes the API and AI Studio (line 116). This supports the report's wording, including its warning against zero-retention and no-human-access claims. It is a documented vendor policy, not evidence that a particular request was retained or reviewed.

### [10] Files API — supported, correctly bounded

[Google Files API](https://ai.google.dev/gemini-api/docs/files), last updated **2026-10-26 UTC**. Lines 464–466 describe automatic file deletion after 48 hours and manual deletion; lines 547–550 describe the same storage period. The report's file-object lifecycle statement matches. Neither passage asserts deletion of distinct abuse logs, datasets or every possible copy. The report's limitation is an appropriate cross-source interpretation rather than an additional erasure promise.

### [11] Developer logs/datasets — supported

[Google Data logging and sharing](https://ai.google.dev/gemini-api/docs/logs-policy), last updated **2026-10-26 UTC**. Lines 90–105 distinguish project-owned logging from abuse logs, restrict availability to billing-enabled projects, and set Generate Content logging on by default for projects created **on or after 2026-10-26**. The report's “from” date is substantively correct; retain inclusive-date precision downstream. The 55-day default leads to marking logs for deletion, not an asserted completed erasure time. Dataset logs lack a set retention period. Lines 97–109 and 129 describe improvement/training and human review for voluntarily shared data and Contributor Tier. The page notes regional dependence; its relationship to the regional terms exception remains unresolved, as the report admits. No actual project setting was verified.

### [5] Personal information — supported

[Datatilsynet Personal information](https://www.datatilsynet.no/rettigheter-og-plikter/personopplysninger/), last changed **2025-03-31**. Line 57 includes direct and indirect links to an individual. The report's account-free/PDF-content distinction follows from that definition; it does not prove that any particular uploaded document contains personal data.

### [6] Privacy principles — supported within applicable scope

[Datatilsynet Privacy principles](https://www.datatilsynet.no/rettigheter-og-plikter/personvernprinsippene/), last changed **2023-07-27**. Lines 65–81 cover legal basis, transparency, data minimisation and deletion/anonymisation when no longer needed. The report uses these as general principles and leaves concrete legal applicability open. The claim that an uploader acknowledgement alone does not supply a legal basis for other people's data is a reasonable implication of the need for an applicable legal basis, not a separately inspected determination about this app. No claim of a mandatory DPIA or universal student exemption is established.

### [7] EEA transfers — supported with qualification above

[Datatilsynet Transfers outside the EEA](https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/overforing-av-personopplysninger-ut-av-eos/), last changed **2026-01-29**. See finding 1. This retrieval establishes neither that a particular Gemini request is a legally relevant third-country transfer nor which transfer mechanism would apply.

### [13] Kopinor/UHR agreement — supported, not inference clearance

[Kopinor/UHR model agreement PDF](https://kopinor.no/wp-content/uploads/2026/02/Monsteravtale-universiteter-og-hogskoler-2025-2029.pdf), negotiated **June 2024**, term **2025-01-01 through 2029-12-31**; publication day remains unconfirmed. Page 2 section 1 gives the institutional/internal scope; page 4 sections 4–5 specify permitted recipients/channels, prohibit public publication under the agreement, and exclude using copied material as ML/generative-AI training material without another agreement or legal basis. There are limited permitted external recipients; the report's “defined institutional/internal setting” remains fair and should not become “absolutely no external recipient.” The training exclusion does not itself decide inference-time upload. The report accurately states that the actual institutional contract was not examined. The PDF was checked through extracted page-indexed text, not rendered-image inspection.

### [14] Government copyright guidance — supported; year metadata caveat

[Norwegian government AI-assistant guide, section 10.4.5](https://www.regjeringen.no/no/dokumenter/ki-assistenter-i-arbeidslivet-en-praktisk-guide/id3109040/?ch=10). Lines 350–362 recommend own/cleared input and review of generated material rather than assuming unrestricted ownership/reuse. This directly supports the report. The source is guidance for workplace organisations, not a judgement about particular student PDFs. Its separate TDM/training discussion was not used to infer that every inference upload infringes. See finding 2 for the available **2025** metadata; no exact publication/update date was verified.

### [15] CC BY 4.0 — supported

[Creative Commons CC BY 4.0 deed](https://creativecommons.org/licenses/by/4.0/), undated, version **4.0**. Lines 48–61 support sharing/adaptation, attribution, licence link, change indication and residual rights. Lines 76–78 add conditional supplied attribution notices and retention of earlier modification indications. The report's sample credit is a practical example, not a full licence-compliance checklist. The deed explicitly summarises rather than replaces the legal code. No actual work, licensor authority or third-party exclusion was verified.

### [16] CC0 1.0 — supported

[Creative Commons CC0 deed](https://creativecommons.org/publicdomain/zero/1.0/), undated, version **1.0**. Lines 47–60 support waiver to the extent legally allowed, remaining privacy/publicity and other third-party rights, and the absence of provenance/copyright-status verification by Creative Commons. The report's boundaries are accurate. A CC0 label alone does not establish that a proposed fixture was validly dedicated.

## Explicit gaps and limits

- [1]–[4] (PDF.js, MDN and OWASP) and [12] (zero data retention page) were outside this focused re-retrieval pass. Their citations were read in the report but not revalidated here. No claim of a complete citation audit is made.
- No provider DPA, country-specific account configuration, independent provider audit, institutional signed agreement, specific fixture licence/provenance, exam-sharing policy or actual settings was inspected.
- The government guide and Kopinor provide distinct-publisher support for the broad need to review input/reuse rights. This is contextual convergence, not independent corroboration of each legal proposition, any vendor fact or file-level permission.
- No current external source contradicted the selected core factual claims. The privacy scope qualification and government year metadata should be resolved before describing this pass as clean without qualifications.

Research report unchanged by this verifier.
