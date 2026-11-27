# BMAD architecture rubric review — AI Study Buddy

Date: 27 November 2026 (Europe/Oslo).\
Verdict: **PASS WITH MINOR CONCERNS — no critical or high architecture blocker identified.**\
Snapshot: AD-1–AD-17, `ARCHITECTURE-SPINE.md` SHA-256 `410dc0ef55b9a43bfce68d88e6dc1e111fada44cb1a6b339d92d569510e8e035`.

## Review scope

Applied the good-spine checklist in `.agents/skills/bmad-architecture/references/reviewer-gate.md` to the current architecture, current PRD/addendum and final DESIGN/EXPERIENCE contracts. This is the independent rubric walker's structural/requirements review, not the separate technology-currentness or adversarial-seam review. The parent reports a zero-finding mechanical lint pass; this reviewer did not rerun it.

Only this review file is written. No implementation, API/provider request, web research, dependency installation, private PDF access, extraction, browser execution or application test was performed. Existing local PDF evidence is assessed only through the architecture's stated scope and limitations.

The user's requested single understandable English document with concise reasons takes precedence over the skill's terse-spine preference. Concise rationale is therefore not treated as a format defect.

## Findings

### R-M1 — Make PDF IPC schema ownership and pure-contract dependencies explicit

**Severity:** Medium; integration clarification, not an unsafe behaviour already implemented.\
**References:** Design paradigm/dependency rules; AD-11; AD-13; Cold-start seed and contract ownership.

The canonical bootstrap contract is explicitly assigned for Pydantic/OpenAPI/frontend and model-candidate versus accepted-result data. AD-11 separately requires a bounded, validated data-only JSON physical-page result from the PDF child. It does not explicitly include that IPC schema in the canonical contract owner's scope. The structural seed lists API/model/accepted-result schemas and a separate extraction worker, while the dependency diagram says its arrows are allowed code dependencies but does not show an adapter-to-pure-contract or child-to-pure-IPC-contract path.

Two units could consequently define different field names/page-map envelopes for supervisor and worker, each obeying the stated bounded-JSON/physical-page rules, and fail integration until they discover the mismatch. The receiving guard should safely reject it, so this is not a source-validation bypass or a high-severity data loss claim.

**Suggested resolution — autofix before feature/bootstrap handoff:** Include the PDF child request/result protocol in the one canonical bootstrap contract responsibility, with both supervisor and child consuming a pure data-only protocol module. State that this module imports no API/session/cost/live-adapter code. Either show the allowed pure-contract dependency edges for adapters/worker, or make clear which diagram edges are illustrative rather than an exhaustive import allowlist. No need to pick every JSON field in the architecture or introduce another framework/service.

### R-L1 — Reconcile the working-state summary with the completed coached decisions

**Severity:** Low; editorial/status clarity.\
**References:** Working state; Remaining architecture closure and implementation gates.

The working-state paragraph still says the draft requires the remaining “AI/resource/runtime decisions,” while the closing section correctly says AD-1–AD-17 record the coached structural decisions and assigns runtime/schema work to owned bootstrap prerequisites. Both passages correctly retain provisional model/account status and no-call permission, but the first wording can invite agents to reopen already adopted choices instead of observing their verification gates.

**Suggested resolution — autofix during final polish:** After review reconciliation, describe the outstanding work consistently as final review plus explicitly owned bootstrap/verification gates. Preserve candidate status and the ban on implementation/API calls; do not imply that structural approval proves model, platform or resource behaviour.

## Good-spine checklist

| Criterion | Assessment |
| --- | --- |
| Real divergence points fixed at feature-to-epic altitude | **Pass.** Ownership, session/request invalidation, one-shot startup, extraction isolation, source eligibility, typed publication, cost persistence and delivery parity are explicit. R-M1 is the remaining small protocol-ownership clarification. |
| Enforceable decisions prevent their stated divergence | **Pass.** Each AD has Binds/Prevents/Rule and material rules describe backend authority, complete-result gates, explicit deadlines/admission and failure handling. No claimed cancellation, billing or hard-memory guarantee is inferred from weaker controls. |
| Named design paradigm and dependency direction | **Pass after the parent's revision.** Client-server with a modular monolith backend is named in frontmatter and prose. The frontend controller, pure contracts, services, adapters, session store, PDF worker and cost boundary are described, with a binding dependency diagram. R-M1 concerns clarity at its pure IPC edge, not a missing paradigm. |
| Capabilities and quiet requirements inherited | **Pass.** See the capability reconciliation below. The current readable-text revision is honoured rather than restoring the earlier whole-PDF-coverage gate. |
| Deferred/open items cannot silently diverge | **Pass with controlled gates.** One bootstrap owner must pin compatible runtimes/packages/images before parallel feature work; one backend contract owner publishes schemas/OpenAPI/frontend types first. Features cannot independently select latest packages or invent fields. Model, RSS, platform, account and demo evidence remain explicitly gated rather than silently assumed. |
| Full operational/environmental envelope covered | **Pass.** Native development, same-origin local demonstration, optional one-service Docker, macOS/Windows, loopback exposure, image exclusions, singleton live authority, child supervision, startup/shutdown/parent-loss cleanup and durable numeric cost state are addressed. Minimum versions/actual mechanisms are named prerequisites, not silently omitted dimensions. |
| Appropriate simplicity and reference adaptation | **Pass with an acknowledged verification burden.** Vite plus a small FastAPI adapter, no database/RAG/queue/cache, one API owner and one heavy slot constrain scope. Optional Docker reuses the same app/assets. The child supervisor and two-platform tests add real work, but they implement explicitly adopted bounded-cleanup/resource requirements rather than an imported production platform. No unrequested larger framework is needed. |
| Existing code/parent-spine consistency | **Not applicable / no conflict found.** This is a greenfield design, with no implementation ratification or parent AD inheritance claimed. Current PRD/UX govern behaviour, and technology.md is treated as a preferred example rather than an adopted platform wholesale. |
| Technology evidence and currentness | **Evidence status is explicit; not independently re-browsed here.** Primary links and local probe versions are given. Probe versions, historical advertised prices and candidate identifiers are not represented as fully validated application/runtime/account pins. The dedicated currentness reviewer and later bootstrap must check the exact chosen baseline. |

## Capability and quiet-requirement reconciliation

- **Startup/navigation/session:** AD-2/AD-3/AD-10/AD-17 preserve one fixed-setting PDF session, one initial explicit Summary intent, no generation from status polling/navigation, cancellation preservation, empty Home after confirmed ending, and rejection of late results. A backend-owned lease bounds orphans while quiet/background reading is not ended merely by blur.
- **Summary/cards/Quiz:** AD-13 and shared conventions preserve selected Summary level, separate language choices, normally ten source-supported items with reduced valid sets, four-option/one-key validation, explicit confirmation, locked answers, actual-count scoring and same-set restart without generation. Detailed UI interactions remain inherited from final UX; the architecture does not invent new learning modes.
- **Sources:** Original-language passages, 1-based physical pages, immutable original text versus separately retained scope, exact/NFC-whitespace matching, exclusion eligibility, whole-Summary versus whole-item rejection and correctly mapped original-text highlighting are preserved. Attached passages support the chosen source panel without a new lazy-fetch state. Location matching is not promoted to factual support.
- **Readable-text scope:** AD-4 aligns with revised FR-40/FR-41. Missing graphics, table content, unknown full-PDF completeness, generic diagnostics or plain/layout differences do not become blanket rejection gates. Unsafe retained fragments cannot be guessed back into meaning; meaningful retained text and source checks remain necessary. Earlier feasibility counts are not declared app-quality passes.
- **Trust and privacy:** PDF/model content remains inert data, not tools/actions/settings. The child has no live credentials; model/private keys stay backend-owned. Acknowledgement precedes external text transfer, provider policies are a separate verified pre-live gate, and app cleanup does not assert provider deletion. The saved demo is not a failed-live fallback.
- **Budget and resources:** One request per explicit attempt, no transport/application/repair/refill retries, full retained context without silent cutting, complete-output validation, busy admission, bounded upload/child/result/character limits and a soft observed RSS stop are clear. Cost amounts/reservations survive restart without study history; unresolved cost stays conservatively held. No all-in billing or hard RSS ceiling is promised.
- **Delivery/evaluation:** The key-free saved-content path needs no private key, provider health check or live budget file; assets/permissions/language-level variants remain a real deliverable gate. Accuracy, original-PDF readable-text coverage, joint correctness/source support and unchanged 9/10/all-smaller-set criteria remain required. Native/container/platform/cleanup/model evidence is not fabricated by the architecture review.

## Intentional gates, not new architecture findings

The following are genuine future prerequisites, but their absence at this planning-only checkpoint is not evidence that the architecture violates the PRD or that this reviewer should start implementation/testing:

1. Exact compatible runtime/dependency/image pins, concrete schema/length/API field seed and generator tooling, owned and completed before parallel feature work.
2. Actual RSS-reader choice, process-start/parent-loss/cancellation/crash handling and end-to-end cleanup/platform verification before claiming the execution/delivery paths work.
3. Approved demo material and reviewed saved variants before claiming an examiner-ready demonstration.
4. Authorised later provider/account, token/context/complete-cost and model-quality evaluation before enabling or finally selecting the live candidate.
5. Original assignment/deadline/reflection/evaluation evidence under the PRD's delivery owners.

## Handoff interpretation

No critical/high rubric issue remains after the parent's paradigm/dependency/bootstrap revision and AD-17 adoption. Apply R-M1 and R-L1 as clear documentation fixes, reconcile the other independent reviewers, and keep all explicit pre-feature/pre-live gates visible. This verdict approves neither app implementation nor API calls and certifies no measured production behaviour.
