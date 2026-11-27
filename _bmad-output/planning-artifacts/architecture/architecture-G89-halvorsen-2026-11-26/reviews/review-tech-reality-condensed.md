# Condensed candidate: technology and reality review

Date: 2026-11-27\
Lens: Configured BMAD architecture technology/reality floor\
Reviewed: temporary `ARCHITECTURE-SPINE.candidate.md`, draft at review, AD-1–AD-17. Its reconciled content is now the [final canonical spine](../ARCHITECTURE-SPINE.md); the disposable candidate was removed during Source Control cleanup.\
Baseline: [Prior full technology review](review-tech-reality.md) and the current canonical spine.

## Verdict

**PASS. Both low-severity documentation findings are closed after a targeted local recheck. No critical, high or medium technology/reality blocker was introduced by condensation.** The candidate preserves the distinction between adopted structural choices, dated local evidence, provisional candidates and unpassed bootstrap/implementation/pre-live gates. Neither finding required a new user decision or implementation.

This was a local comparison only. No additional web lookup, API endpoint, installation, build, server, application code, private PDF or extracted content was used. Existing primary-source checks and sanitized repository evidence were compared with the candidate. Relative source/evidence links were assessed from the intended canonical architecture directory, as instructed; their temporary location inside reviews is not treated as a broken-link finding.

## Findings

### C-TR-1 — Restore the explicit condition on the US$0.35 reservation

**Severity:** Low. **Disposition:** Closed. Candidate line 241 now explicitly requires the combined conservative upper bound for every billed dimension to fit US$0.35, otherwise stopping for review without silently enlarging it or the project budget. The original finding is retained below for provenance.

Candidate line 241 calls US$0.35 a conditional reservation seed and retains all-billable-dimensions verification, but drops the canonical gate's explicit condition: the conservative combined upper bound for every billable dimension must fit within that amount. The token arithmetic alone leaves only a small margin; knowing an additional charge exists is not proof that the chosen reservation covers it.

Add one sentence next to the formula:

> Use US$0.35 only if the verified combined conservative upper bound for every billable dimension is at most US$0.35; otherwise stop and return for a decision.

This restores the already agreed condition from canonical AD-14's cost-accounting implementation gate (canonical line 293). It does not introduce a new cap, authorize calls, change the US$5 budget or solve the separate context-fit gate. Other candidate safeguards at lines 138, 162–164 and 239–241 remain intact.

### C-TR-2 — Retain the verified OpenRouter limits documentation URL

**Severity:** Low. **Disposition:** Closed. Candidate line 318 now uses the previously verified docs/api_reference/limits URL. The original finding is retained below for provenance.

Candidate line 318 changes the key-limits reference to a different, unverified path:

- Candidate: https://openrouter.ai/docs/api-reference/limits
- Previously checked source: https://openrouter.ai/docs/api_reference/limits

Restore the previously checked URL. No claim is made that the candidate route is broken: additional browsing was prohibited for this pass. This is a source-provenance correction, not a product or provider-capability finding.

## Preserved technical facts and limits

| Area | Condensed candidate assessment |
| --- | --- |
| Starter and application families | Lines 68 and 299–306 retain official react-ts plus a small FastAPI application. One bootstrap owner selects the compatible baseline before dependent work; features cannot independently choose latest versions. The condensed text does not invent a router, state library, general worker framework or full-stack starter service. |
| Tested versus application versions | Line 314 retains the dated Python 3.14.7 / pypdf 7.1.1 / pdfplumber 0.11.11 trial and expressly says these are evidence, not application pins. It requires affected fixtures to be rechecked. The prior review's observation that current pypdf documentation showed 7.2.0 therefore remains compatible with the candidate. |
| Provisional model | Lines 32 and 120–130 keep Gemini/Vertex provisional and the 26 November catalog observation explicitly dated. Advertised context, maximum output and prices remain distinct from app limits, account availability, educational quality and tested fit. The catalog link was not fetched during this pass. |
| Output, cost and context | Lines 138, 162–164 and 239–241 preserve independent full-request context fit, reasoning/output mapping verification, account usage.cost reconciliation, durable unresolved reservations, no reset and no all-in billing guarantee. C-TR-1 restores one useful explicit mathematical condition. |
| Windows event loop | Lines 265–267 retain one API process/no autoreload, Proactor support for Windows async subprocesses, the Uvicorn reload/multi-worker Selector risk, and exact-runtime verification. They do not promise Unix signal, lock, replace or scheduling equivalence. |
| Child lifecycle | Lines 189–193 preserve owned subprocess/IPC boundaries, total-byte limits distinct from StreamReader.limit, bounded diagnostics, POSIX versus Windows termination and parent-loss uncertainty. No child-finally or automatic parent-death cleanup guarantee has appeared. |
| RSS and numeric bounds | Lines 205–217 preserve separate clocks, two-workspace accounting, cleanup-held reservations, control bypass, independent character/byte caps and a soft 256 MiB / 250 ms watchdog. psutil remains a candidate. Peak RSS, address space and container limits are not treated as equivalent measurements. |
| Docker facts and privacy | Lines 249–259 retain one final Python app runtime, optional packaging, localhost publication, explicit context exclusion before caching, non-root/init limits, ephemeral study scratch and stopped-layer persistence. Future live cost state uses the same external directory and allowance; no concurrent live instances or fresh container budget is allowed. |
| Extraction evidence | Lines 95–111 and 314–316 retain native-text feasibility and failed complete coverage, mixed parser behavior, no universal semantic detector and no semantic/model/app-cleanup certification. Condensation does not turn 74 page slots into complete coverage. |
| Authorization and readiness | Lines 32–36 and 303–310 retain documentation-only authorization and named owners/triggers for the unpassed gates. The candidate does not claim app, native platform, Docker or model tests were performed. |

## Exact pins and deferred gates

The single-owner bootstrap order remains a valid deferred gate, not an architectural contradiction: compatible versions and concrete canonical schemas/types must be established before feature code depends on them. Requiring installation, starter execution, lockfile creation or an API call during this documentation-only review would not be justified.

The previous review's three readiness obligations remain:

1. Record and lock the actual starter/runtime/package/image baseline before feature work.
2. Verify native and container cancellation, IPC, RSS, atomic-file and cleanup behavior with owned fixtures before support claims.
3. Obtain separate authorization and verify actual endpoint terms/capabilities, complete-request token/context/cost assumptions and the full PRD evaluation before enabling or finally adopting the live candidate.

The two small text/link corrections have been verified locally, and the condensed candidate preserves the prior technology/reality pass. This closure recheck covered only those two findings. The document remains an architecture contract with future verification gates, not a readiness certificate or implementation permission.
