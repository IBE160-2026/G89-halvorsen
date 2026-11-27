# Adversarial seams review — AI Study Buddy architecture

Date: 27 November 2026\
Review lens: configured BMAD FINALIZE-REVIEW adversarial floor\
Reviewed artifact: [ARCHITECTURE-SPINE.md](../ARCHITECTURE-SPINE.md), draft with AD-1–AD-17 adopted and the cold-start ownership/ordering seed present.

## Verdict

**Pass for structural consistency, subject to the document's existing bootstrap and pre-live gates. No critical or high-severity architecture hole was demonstrated.** I could not construct a pair of independently permitted feature units that obeys every adopted decision *and the required bootstrap order* yet necessarily integrates incompatibly. The tempting counterexamples below either violate an explicit invariant or depend on bypassing the backend-owned contract prerequisite.

This is a document review, not application verification or permission to implement. It does not establish parser reliability, model quality, spending enforcement, supported OS behaviour, cleanup timing or an operational demo. Exact schemas and version pins remain legitimate owner-gated bootstrap work. They must not be relabelled as independently selectable feature assumptions.

## Scope and method

Applied the configured attack: construct two units one level down with incompatible data, ownership or state mutation despite local compliance. The units considered were the frontend session controller/views, API lifecycle services, PDF supervisor/child, saved/live adapters, numeric cost controls, and native/container launch packaging. Reviewed the adopted decisions and the dependency rules, planned tree, canonical contract ownership/order and consistency conventions together.

The parent reported that the mechanical lint passed with zero findings. This reviewer did not rerun it. No API or web access, app implementation, server/build, dependency installation, app tests or private-PDF extraction was performed. Only this review file was written.

## Critical and high findings

None demonstrated in the inspected snapshot. In particular, the formerly pending startup boundary is now AD-17 rather than an unadopted proposal, and the new bootstrap order closes the formerly possible independent-JSON-contract fork.

## Bootstrap watchpoints — existing gates, not new architecture choices

### S-1 — Freeze meanings as well as generated field types

**Classification:** medium integration watchpoint; already blocked by the canonical-contract prerequisite. No additional user decision is required by this review.

**Attempted pair:** the API emits a numeric lease representation and the frontend interprets the same number using a different clock/scale. A second attempted pair uses a zero-based Quiz answer key on one side and a one-based key on the other. Generated TypeScript types alone would not reveal either mismatch.

**Why this is not a compliant post-bootstrap counterexample:** the cold-start section requires the backend owner to freeze enum/ID/unit/source-display conventions before dependent feature work, and explicitly assigns Quiz indexing to the canonical schemas. AD-10 makes server expiry authoritative and prohibits client-time revival. Implementing these interpretations independently would skip the prerequisite, not exercise an allowed architectural freedom.

**Required owner action when implementation is authorised:** include lease wire semantics, Quiz indexing, terminal-versus-preserving failures, phase transitions and request relevance in the published contract, with examples. Ensure the supervised child JSON protocol is included in the backend-owned contract work too; it must not become a separate PDF-agent invention merely because it is not an HTTP/OpenAPI payload. The existing requirement to share extraction/data-protocol code provides the direction. No generator package or concrete fields are selected here.

**Revisit trigger:** before frontend, model-adapter or PDF-supervisor/worker work proceeds in parallel, and whenever canonical contracts or saved fixtures change.

### S-2 — The cost lifecycle remains separate from study cancellation

**Classification:** medium implementation/pre-live watchpoint; already fail-closed under AD-9/AD-14.

**Attempted pair:** the study service cancels and releases its task-held PDF/model copies on New session, while the cost component expects that same task to remain alive with a full request object until settlement. This would either retain study material or forget an unresolved charge.

**Why the harmful pair is not permitted:** AD-3/AD-10/AD-11 require bounded release of study copies; the dependency rules restrict the cost module to numeric accounting inputs; AD-14 requires durable reservations before transfer and forbids clearing them on session end. The cost component cannot require a retained study object. It may preserve an unresolved conservative reservation and block later live calls if settlement is uncertain. That can limit availability but is an expressly allowed safe outcome.

**Required owner action when implementation is authorised:** define the numeric reservation/settlement interface and crash transitions before live enablement, including a late response after study cancellation and restart with pending amounts. The no-study-data/no-identifiers restrictions on the durable file remain binding. Do not add forbidden identifiers or assume an unresolved reservation can be released merely to make a test pass. Exact reconciliation mechanics and provider/account evidence remain pre-live work; this review does not invent a billing guarantee.

**Revisit trigger:** before any authorised provider transfer, after changing the cost schema/adapter, and before enabling live operation in Docker.

### S-3 — Platform verification must remain scoped to the actual execution path

**Classification:** medium acceptance watchpoint; not an unmade topology decision.

**Attempted pair:** packaging verifies a Linux-container child and announces native Windows readiness, while the API supervision unit relies on Windows async subprocess behaviour that was never exercised. Another attempted pair treats a container memory limit as the adopted child-RSS measurement.

**Why these pairs are excluded:** AD-16 explicitly distinguishes native macOS/Windows verification from Linux-container success and names the event-loop constraint. AD-12/AD-15 explicitly distinguish child observed RSS from container/VM memory. AD-11/AD-15 require parent-loss, signal, reaping and scratch-lifecycle checks rather than assuming init or container stop supplies them.

**Required owner action when implementation is authorised:** keep the native and container evidence separate, choose one supported live-RSS reader/runtime baseline, and verify the adopted cancellation/release timings on the target path. Exact versions, minimum OS/CPU targets and launch mechanisms are bootstrap/verification gates. They do not authorise a second API worker, a thread-based parser replacement, a mandatory service stack or weaker cleanup semantics.

**Revisit trigger:** before claiming examiner readiness on either native OS or distributing the optional Docker package.

## Adversarial pair matrix

| Two units and attempted incompatibility | Relevant boundary | Result |
| --- | --- | --- |
| Frontend invents a Markdown result while backend returns typed blocks | AD-13; pure canonical contracts; frontend types derived from backend | Excluded. No Markdown renderer is permitted; independent fields violate the bootstrap order. |
| Backend returns Python code-point offsets while source view slices JavaScript UTF-16 | Shared source-display convention | Closed. Accepted display carries backend-resolved original text segments, not unlabelled offsets. The frontend renders inert strings. |
| Live adapter reconstructs settings or treats generated aids as the next source | AD-2/AD-7; service-only mutation | Excluded. Settings and immutable source scope are server-owned; adapters return data and cannot mutate session state. |
| Source validator matches an excerpt inside excluded text because it appears on the right physical page | AD-4/AD-7 | Excluded. Page-local location is necessary but retained-scope eligibility is separately mandatory. Exact/NFC-plus-whitespace matching cannot restore excluded material. |
| Card renderer retains some valid references on an item whose other reference is invalid | AD-13; FR-37 | Excluded. Whole shape validation precedes filtering; any invalid reference removes the whole item. Summary uses whole-new-Summary rejection instead. |
| Preparation completion starts a model call while the frontend has ended the session | AD-17/AD-3 | Closed. Preparation/status starts no model work; only the still-current one-shot browser intent requests initial generation. Transfer and publication guards remain separate. |
| Repeated Source-ready polls issue multiple initial generations | AD-17 | Closed. The browser continuation is consumed once and backend duplicate admission is mandatory. Polls are read-only. |
| Preparation retains the heavy slot indefinitely awaiting the next browser request | AD-12/AD-17 | Excluded. A reserved pre-body slot starts the upload deadline; Source ready follows child/raw-copy release. Later generation competes anew and may return busy without a queue. |
| A preparation timeout is presented as a generation timeout, or progress resets a parser clock | AD-8/AD-12/AD-17 | Excluded. Upload, child and generation have separate total admission boundaries; progress does not reset them. |
| Old ended-session failure clears a newer active session | AD-3/AD-17; common response relevance | Excluded. Identity/action relevance is checked before any mutation, including failure handling. Ended/expired versus preserving failures are separately represented. |
| Source close hides a revealed card because all modal closes use function-return logic | AD-13; inherited UX | Excluded. Source close preserves the revealed answer and focus; function return preserves position but shows the front. |
| Session cleanup resets an in-memory spending counter or drops pending charges | AD-9/AD-14 | Excluded. Durable project cost metadata survives New session/restart; unknown usage remains conservatively reserved or blocks live calls. |
| Docker starts a second live API owner with a fresh allowance | AD-15/AD-14 | Excluded. Only one live API instance for the project is allowed, and an existing cost directory must survive recreation. |
| Docker build copies ignored private PDFs or cost metadata because Git does not track them | AD-15 build-context contract | Excluded. Separate context exclusions and a narrow COPY allowlist are required before a build; later-layer deletion is insufficient. |
| Demo adapter lacks a language/level variant and silently calls live generation | AD-5/AD-15 | Excluded. Default demo is explicitly saved/key-free; absent or invalid variants fail honestly, never substitute another variant or call the provider. |
| Saved demo cannot start because the live key or cost-control file is absent | AD-14/AD-15 | Excluded. Core demo, startup/build/health must not require live setup or initialise a live ledger. |
| PDF child imports API assembly and inherits state/credential authority | AD-11; dependency rules | Excluded. The child imports only extraction/data-protocol code and has no model credentials or session/cost authority. |

## Source and ownership assessment

The source boundary is sufficiently explicit for this altitude: one original physical-page map, a separate retained eligibility scope, original-language source segments resolved by the backend, and no frontend source-content fetch. No second actor is allowed to repair, reselect or republish source data independently. Multiple supporting passages remain separately inspectable. Matching proves location, not support; the separate quality evaluation remains mandatory.

The state boundary is similarly explicit: one frontend controller owns browser state and intent; one FastAPI process owns server identity/settings/acknowledgement and admission; services orchestrate; adapters return data; the PDF child has no state authority; numeric cost metadata survives without restoring study state. This prevents the common two-owner failure without introducing a general framework.

## What this review does not turn into an architecture defect

- Exact field names, string/list length bounds, concrete Quiz answer-key shape, protocol schema versions, code-generation tooling and package/image pins have one named owner and an enforced-before-dependent-work ordering. Their current absence prevents coding those dependent units now; it does not allow units to select incompatible alternatives later.
- Actual reliable-text stop/isolation behaviour, model/schema/language/source quality, full-request context fit, conservative cost reservations and provider terms remain explicitly unproven. The selected candidates are provisional and live transfer is not authorised. Fail-closed gates must remain visible in the final handoff.
- Cancellation, parent death, bounded pipes/results, RSS sampling, filesystem atomicity and Windows/container behaviour require targeted implementation evidence. A clear verification obligation is not proof of support, but neither is it automatically an unmade architectural choice.
- Approved shareable demo material and its reviewed saved variants still need to be supplied. Private T1–T3 inputs are not automatically permissible demo/image assets.

## Disposition

No new load-bearing decision or user question is required by this lens. Retain the bootstrap order and the explicit implementation/pre-live gates. A small clarification that canonical backend contract work includes the child IPC and lease representation would help downstream owners, without changing AD-11/AD-17 or adopting a new transport. Do not mark the application implemented, tested or live-ready when closing the architecture review. Do not start implementation under this review's authority.
