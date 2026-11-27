# Adversarial seam review — condensed architecture candidate

Date: 27 November 2026 (Europe/Oslo).\
Verdict: **PASS — no new critical, high or medium cross-unit divergence found in the condensed candidate.**\
Candidate: `reviews/ARCHITECTURE-SPINE.candidate.md`, SHA-256 `41a0d7a29f0fe2c2abd7a18952386f1769cc08616f70f323d7b45237d06f6957`.\
Full approved baseline: `ARCHITECTURE-SPINE.md`, SHA-256 `410dc0ef55b9a43bfce68d88e6dc1e111fada44cb1a6b339d92d569510e8e035`.

## Scope and method

Applied the configured adversarial floor: try to construct two separately implemented units that obey every candidate rule but become incompatible. Compared the condensed AD-1–AD-17 and its bootstrap gates against the full approved architecture. This is a new seam-focused pass, not a repetition of the earlier rubric review. Concentrated on the source representation, startup/admission clocks, request relevance, session ending, cost settlement, IPC, shared types, lease wire semantics, Docker/Windows and permission boundaries.

The candidate is staged in `reviews/`; its relative references intentionally target the future canonical document location. That staging convention is not reported as a link defect. No API/web/model request, app implementation, dependency installation, build, runtime test or private PDF access was performed. Only this review file is written.

## Findings

No new actionable critical/high/medium seam finding is identified. The condensed text preserves the approved safeguards at the seams tested below, including the newly explicit canonical IPC contract, original-text segments, shared lease wire semantics and request relevance independent of the selected tab. No request to reopen an adopted technical decision is needed from this review.

This is an architecture-document pass, not proof that a future implementation has the specified properties. The existing owned bootstrap and pre-live gates remain binding.

## Adversarial attempts

| Independently built pair / attempted divergence | Why the candidate prevents it |
| --- | --- |
| Frontend drops or overwrites an accepted generation merely because the user switches Summary/Quiz/cards; backend treats the generation as still valid | AD-3 explicitly binds relevance to preparation/function attempts, not the selected tab. Navigation/source inspection must not erase valid work/cache, and accepted publication must not force navigation. Both units must preserve the same active attempt independently of view selection. |
| A late PDF task reports Source ready after New session; a browser poll starts a paid Summary anyway | AD-3 and AD-17 require current session/attempt relevance before mutation, invalidate pending continuations/polls on end/expiry/reload, reject unknown identities and forbid worker/status-triggered model calls. The one-shot browser intent and backend duplicate-admission guard are both required. |
| Source-ready polling is retried several times and each response silently generates a new Summary | Status is read-only and starts no work/model call. AD-17 consumes startup continuation once, and the backend rejects duplicate admissions. A busy admission preserves the source and requires manual retry rather than polling/queueing. |
| Upload handler closes a request-scoped spool while a background preparation task still needs it | AD-17 requires parent ownership of the bounded raw copy before request handles close. AD-11 assigns child/attempt/deadline/upload ownership to the parent, and AD-2 requires release on every outcome rather than depending on one request object's lifetime. |
| Registration reserves the only slot, but a client never sends a body; backend waits for the 30-minute lease | AD-17 explicitly starts the existing 30-second upload clock at reservation. AD-12 reserves before unbounded body spooling, disallows hidden queues and keeps cleanup/control outside the heavy slot. Parser and generation clocks remain separate and do not reset on progress. |
| One unit releases capacity as soon as it marks an attempt cancelled; another child continues consuming resources | AD-12 retains reservations until child/tasks/copies are released and explicitly forbids releasing a running child's slot. AD-11 requires bounded terminate/wait/reap, closing pipes and parent/task copies on every exit, without relying on killed-child finally blocks. |
| Browser uses milliseconds/its own wall clock for lease validity while backend uses another unit and accepts delayed renewal | AD-10 makes server time/expiry authoritative and checks before every access/renewal. The canonical bootstrap explicitly owns lease wire clock/unit semantics before parallel dependent work. A delayed heartbeat cannot revive expired identity, server work cannot renew itself, and uncertain wake validity requires validation. |
| Supervisor expects one JSON page-map shape while child emits another, each calling its own format valid | The bootstrap contract owner's scope now explicitly includes child IPC request/result DTOs consumed by both supervisor and worker before parallel work. Pure contract dependencies are shown for supervisor, adapters and worker. AD-11 adds independent complete-result byte/shape/current-attempt gates; stream buffer size is not mistaken for the total cap. |
| A worker imports the main FastAPI module to obtain DTOs and inherits live credentials/session state | The dependency rule permits only pure extraction/IPC contracts in the worker and explicitly forbids application/bootstrap/secrets/live adapters/session/cost state. Contracts have no network/file operations or service/bootstrap imports. |
| Model quotes and frontend offsets use different Unicode/whitespace representations, highlighting the wrong text | AD-4 retains immutable original per-page text separately from the generation scope and validates on the cited physical page. AD-13 returns backend-resolved original-language context/highlight segments, not raw model quotes or unlabelled Python/JavaScript offsets. Exact/NFC-whitespace matching is explicitly constrained. |
| A quote is found in original text that was excluded from generation, and is accepted as a source anyway | AD-4 states excluded content is never source-eligible, separately from location matching. AD-7 uses only whole accepted retained text; omitted unsafe material cannot be reintroduced. Matching alone proves neither retained-scope eligibility nor semantic support. |
| A malformed Quiz is partially salvaged; another unit applies item filtering to the whole schema error | AD-13 orders strict whole-structure validation before reference filtering. Malformed reply fails as a whole; only otherwise valid card/Quiz sets can lose whole items for invalid references. Summary fails as a whole for any invalid reference; zero valid items is an error and actual accepted count drives score. |
| A study cancellation prevents settlement, or the accounting job keeps the cancelled PDF/prompt alive to finish billing | AD-3 explicitly says stale study output never prevents global cost settlement. AD-14 requires settlement for failed/stale/ended attempts, durable held reservations and numeric accounting that does not retain study tasks/objects. Unknown settlement is held or blocks live calls rather than guessed free. |
| A project restart or container recreation creates a new spending allowance | AD-9 forbids restart/session/reset growth, AD-14 persists numeric cost state with corruption/missing-state fail-closed behaviour, and AD-15 mounts the existing cost directory outside image/writable layer for later authorised live Docker use. One live API instance owns the project authority. Demo does not initialise live cost state. |
| Runtime cost arithmetic assumes characters establish token fit or treats the US$0.35 example as per-call spending permission | AD-7 independently requires full assembled context/cost verification. AD-9 includes all billed dimensions and unresolved attempts. AD-14 labels US$0.35 conditional only, without transfer authority, fit certificate or all-in billing promise. Unsupported accounting must be resolved before transfer. |
| A key supplied in the environment silently turns the examiner's saved demo into live generation | AD-15 expressly forbids environment-key activation, requires key-free default saved playback and no provider/token/budget health request, and prohibits silent live/demo substitution. Shared UI/source/rubric and selected language/level assets apply in both packaging paths. |
| Git-ignored private PDFs/cost files still enter Docker layers or build caches | AD-15 separately requires `.dockerignore` and narrow COPY exclusions before context transfer/caching. Git exclusion or deletion in a later layer is explicitly insufficient; private ordinary-study volumes are not introduced. |
| Windows parser cancellation is implemented as Unix SIGTERM/SIGKILL, or native support is inferred from Docker success | AD-11 names Windows terminate/kill equivalence and parent cleanup; AD-16 requires actual pinned event-loop/process/filesystem/timing verification, a one-process/no-autoreload baseline and separate native Mac/Windows checks. AD-15 distinguishes Linux VM/container limits from native child RSS. |
| A soft 256 MiB RSS sample threshold becomes a hard memory guarantee or silently disappears when unavailable | AD-12 states sampling overshoot is possible, requires live registered-process identity, fails unreadable monitoring for a live child and rejects peak RSS/address-space as substitutes. Container limits have explicitly different scope. |
| Documentation approval is treated as permission to implement, create accounts, call models/token/billing APIs or transfer private T1–T3 | The opening authorisation boundary and deferred gates expressly limit current work to documentation. Provisional candidates, source citations, numeric budgets and structural approval do not authorise calls, builds, credentials, purchases, publication or document transfer. |

## Condensation parity

The candidate retains all 17 adopted decision identities and the important shared boundaries:

- One browser controller and one API/session/cost authority, with a supervised local extraction child and no database/queue/cache/RAG subsystem.
- One accepted extraction snapshot, applicable manual extraction retry, transient raw input, immutable physical-page records and separately retained generation/source-eligible scope.
- Revised readable-text FR-40/FR-41: graphical/table omissions and unknown completeness are not blanket stops; unsafe retained text is excluded or stops when needed; evidence-based notice claims remain bounded.
- One external generation request per explicit attempt, fixed candidate routing/no fallback, strict structure then source validation, no automatic repair/regeneration/refill or live/demo substitution.
- The complete adopted input/text/time/capacity/result/RSS and renewable-lease values, with busy/no-queue and independent control/cleanup paths.
- Typed inert results and attached verified original passages, practice preservation and same-set reuse, atomic current-attempt publication and independent restart-safe numeric cost settlement.
- Same key-free native/optional Docker app, narrow build context and durable live-cost directory, one live owner and explicit native Windows execution/verification boundaries.

Omitting long historical probe counts and repeated status/rationale paragraphs does not weaken a shared invariant; the evidence companions and memlog remain referenced. The candidate correctly treats previous PDF measurements and dated endpoint advertising as evidence with limits, not implemented resource enforcement or model-quality results.

## Gates intentionally left owned

Exact runtime/dependency/image pins, API/model/result/IPC field details, lengths, schema generation and lease wire representation remain one-owner bootstrap prerequisites before parallel consumers. This is not permission for independent units to pick arbitrary latest packages or field shapes. Actual retained-text isolation, RSS/parent-loss/cleanup/atomic-file behaviour, permitted demo assets and model/account/context/cost/quality verification retain named owners/triggers. Those are implementation/pre-live acceptance gates; their absence from a documentation-only task is not a new adversarial failure.

## Handoff conclusion

The condensed candidate is suitable to replace the full narrative as the shared architecture foundation after the parent completes its other configured reviews. No new decision or source-policy weakening is requested. Preserve the stated bootstrap/pre-live authorisation and acceptance gates when preparing later tasks; this review neither implements nor empirically verifies them.
