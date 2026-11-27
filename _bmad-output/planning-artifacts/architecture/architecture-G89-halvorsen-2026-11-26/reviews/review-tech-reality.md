# Technology and reality review

Date: 2026-11-27\
Lens: Configured BMAD architecture FINALIZE-REVIEW technology/reality floor\
Artifact: [ARCHITECTURE-SPINE.md](../ARCHITECTURE-SPINE.md), draft with adopted AD-1–AD-17 and the cold-start ownership seed.

## Verdict

**PASS for the architecture technology/reality floor. No critical, high or medium architectural finding requires changing the selected stack or obtaining a new technical decision before documentation handoff.** This is not implementation, native-platform, model-quality, billing or delivery certification. The remaining bootstrap, implementation and pre-live gates are real gates; the document correctly does not claim they have passed.

Exact application pins are legitimately deferred to the single bootstrap owner, before feature work or code depends on them (spine lines 409–412, 425–427). Requiring installation, generated lockfiles, a running server, a Docker build or a model call now would contradict the user's documentation-only instruction and would not resolve a missing architectural choice. The bootstrap must still select and record a compatible baseline; independent features must not resolve their own versions or schemas.

## Review scope and method

Reviewed the current spine, its append-only [.memlog.md](../.memlog.md), the configured reviewer instructions, the preferred [technology reference](../../technology.md), PRD privacy/evaluation boundaries, and sanitized local parser evidence. Rechecked public primary HTML for the live Vite starter, FastAPI, HTTPX, Pydantic, pypdf and OpenRouter feature/routing documentation. Also used the primary Python/Uvicorn/Docker/psutil documentation checks recorded during this same architecture session.

No model/provider/catalog endpoint, token or billing API was called. No private PDF or extracted text was reopened. No dependency, starter, application, server, image or build was installed or executed. This review writes only this review artifact. The parent's deterministic lint result is reported as supplied; it was not rerun here.

## Findings requiring architecture changes

**None found in this lens.**

The following three items are implementation/readiness obligations, not failed architecture decisions:

1. **Bootstrap baseline and starter snapshot.** Pin one compatible runtime/package/image baseline and record the actual starter output before parallel feature work. The current starter remains appropriate, but its moving branch and package ranges are not a reproducible lockfile.
2. **Native supervision and resource enforcement.** Prove the promised cancellation, cleanup, IPC and soft-RSS behavior on the selected native targets and container path using owned fixtures. Documentation establishes feasibility and platform differences, not achieved deadlines.
3. **Live model/context/cost readiness.** Keep live generation disabled until endpoint capabilities, terms, complete-request context fit, accounting and PRD evaluation are verified under separate authorization. Neither the earlier advertised model limits nor the conditional US$0.35 calculation closes this gate.

## Decision-by-decision evidence

| Decision | Reality check and assessment |
| --- | --- |
| AD-1: React/TypeScript, Vite, minimal FastAPI | The official Vite guide still lists react-ts and static build output. The official template is a minimal React/TypeScript setup with HMR and lint configuration, rather than an application architecture. FastAPI's tutorial supports the small application approach. No obsolete full-stack starter or unneeded database/auth stack has been silently adopted. |
| AD-2: Extract once and temporary ownership | Process-local backend state, React-owned UI state and bounded upload handles are ordinary framework-supported choices. The spine explicitly limits the API to one state-owning process and admits restart loss. This is a design decision, not an unsupported database durability claim. |
| AD-3: Invalidation and late-result guards | Browser cancellation and close events are not treated as reliable deletion guarantees. Session/request relevance is the publication authority, with a separate backend lease. No unsupported promise that cancelling a browser fetch stops remote execution is made. |
| AD-4: Readable-text PDF path | Page-level native text and layout extraction are supported by pypdf. The local trial actually demonstrates native extraction and known graphic/order losses. The revised rule does not infer full coverage from nonempty text, promise OCR or assume a universal semantic detector. |
| AD-5: HTTPX/Pydantic/OpenRouter adapter | All selected families exist and fit a small explicit adapter. HTTPX documents optional connection retry behavior; Pydantic documents strict validation. The spine deliberately configures retry/fallback behavior rather than relying on gateway/starter defaults. |
| AD-6: Provisional Gemini/Vertex candidate | Model and route are explicitly provisional. The earlier catalog observation is dated, and actual account availability, schema behavior, educational quality and provider terms remain unverified. This review did not fetch that API link. No current endpoint or quality guarantee is adopted. |
| AD-7: Whole retained source | A single complete text context is a feasible request strategy conditional on the separately required full-request fit check. Character bounds are not misrepresented as a tokenizer or context-fit guarantee. |
| AD-8: Text/generation limits | The documented T1–T3 measurements support ordinary-case headroom, not worst-case performance. The 120-second total deadline is correctly distinct from a per-read HTTPX timeout. Limits remain operational choices requiring later tests. |
| AD-9: Output and project budget | The 8,192-token mapping, route rates, provider limit and all charge dimensions require verification. Unknown charges are not zero, and the PRD matrix cannot be shortened to fit the budget. No absolute all-in billing guarantee is made. |
| AD-10: Renewable lease | The adopted timing is a testable app contract, not a browser scheduling guarantee. Suspended tabs and unreachable cleanup requests have explicit limitations. Server expiry is checked before renewal, and server work cannot keep itself alive. |
| AD-11: Short-lived PDF subprocess | Python supports supervised subprocesses and bounded asynchronous pipe handling. The spine distinguishes POSIX escalation from Windows TerminateProcess and does not rely on child finally handlers or automatic parent-death cleanup. |
| AD-12: Resource envelope/RSS | Current child RSS in bytes is a supported psutil candidate measurement. It is correctly distinguished from peak RSS, address space and an OS hard cap. Missing measurement is not silently ignored. The dependency is not selected or pinned by mentioning it. |
| AD-13: Typed results/attached sources | Pydantic validation and inert app-owned React rendering fit the contract. Source location and schema validation are not presented as semantic factual validation. Backend mapping resolves NFC/whitespace matching to original text before display. |
| AD-14: Durable numeric costs | A small parent-owned content-free file can support the selected single-process design. Atomicity, crash durability and reconciliation remain tests. Study/session data, identifiers and credentials are excluded; no database or student-history exception is smuggled in. |
| AD-15: Native/optional Docker demo | Vite static output, FastAPI frontend serving and Docker multi-stage artifact copying support the topology. Loopback publication, build-context exclusion and writable-layer persistence are addressed. Docker init does not replace app supervision, and container limits are not relabelled child-RSS caps. |
| AD-16: Native macOS/Windows | Current Python and Uvicorn documentation supports the specified Windows loop guard. Reload/multiple-worker behavior is not assumed compatible. The target families are adopted, but native support is not falsely claimed tested. |
| AD-17: Staged startup | One parent-owned preparation task, local status and browser-controlled one-shot continuation are feasible in the chosen single-process topology. Raw-copy ownership is established before request upload handles close; polling does not become a paid generation trigger or hidden queue. |

## Current starter and library details

The [Vite guide](https://vite.dev/guide/) currently lists the react-ts preset, a development server with HMR and optimized static production assets. It also states Node compatibility requirements, with an explicit warning that individual templates can require more. Therefore the spine's single bootstrap owner must select a supported runtime that satisfies the actual chosen template rather than copying a remembered minimum. The [official template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) presently describes minimal HMR and Oxlint configuration; it does not choose the project's session, API, router or response contracts. Those are owned explicitly in the spine.

The [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) remains a valid minimal start. Current [frontend/static serving documentation](https://fastapi.tiangolo.com/tutorial/static-files/) recommends its frontend helper for client routing. The spine appropriately binds the topology and requires compatible serving/build mechanisms later, instead of asserting that a generic root static mount already provides correct SPA routing and API precedence.

[HTTPX transports](https://www.python-httpx.org/advanced/transports/) document connection retries as a configurable transport behavior. Its [timeout documentation](https://www.python-httpx.org/advanced/timeouts/) describes a default inactivity timeout and distinct timeout dimensions, rather than the app's overall generation deadline. AD-5/AD-8 must remain explicit in the implementation. [Pydantic strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/) supports the intended validation family, but mode and validation entry point must be tested with the canonical schemas; strict mode is not a semantic/source-quality check.

The currently served [pypdf extraction documentation](https://pypdf.readthedocs.io/en/stable/user/extract-text.html) identifies itself as 7.2.0. The recorded local trial used 7.1.1. This is **not a factual error in the spine**: it dates the trial and explicitly says those versions are not application pins. Re-run affected owned extraction/source-location fixtures when the bootstrap selects its parser version. Official docs also warn about large extraction memory use; a small compressed upload is not a hard decompressed-memory bound.

## Platform and live-readiness boundaries

[Python platform support](https://docs.python.org/3.14/library/asyncio-platforms.html#subprocess-support-on-windows) requires Proactor for Windows asynchronous subprocesses. [Uvicorn's current loop documentation](https://uvicorn.dev/concepts/event-loop/) distinguishes single-process Windows from reload/multiple-worker loop selection. [Python subprocess termination](https://docs.python.org/3.14/library/asyncio-subprocess.html#asyncio.subprocess.Process.terminate) differs between POSIX and Windows. AD-11/AD-16 now capture these distinctions; exact pins and actual native tests remain necessary.

The [released psutil API documentation](https://psutil.io/7.2/#psutil.Process.memory_info) supports RSS in bytes and documents process-exit/PID-reuse races. This is fit evidence for a possible reader, not a selected dependency, hard cap or demonstrated 250 ms sampling guarantee.

Docker's [multi-stage build](https://docs.docker.com/build/building/multi-stage/), [build-context](https://docs.docker.com/build/concepts/context/#dockerignore-files) and [storage](https://docs.docker.com/engine/storage/) documentation support the proposed packaging/privacy separation. Its [container resource controls](https://docs.docker.com/engine/containers/resource_constraints/) cover a different scope from one child process. These sources support AD-15's constraints, not a completed build or proof of native-platform parity.

OpenRouter's [structured output](https://openrouter.ai/docs/guides/features/structured-outputs) and [provider routing](https://openrouter.ai/docs/guides/routing/provider-selection) documentation support the gateway strategy, conditional on the actual endpoint. [Usage accounting](https://openrouter.ai/docs/cookbook/administration/usage-accounting) describes account charge in usage.cost; [key/credit limits](https://openrouter.ai/docs/api_reference/limits) distinguish lifetime usage and remaining allowance from in-flight settlement. The spine correctly retains independent provider, durable reservation, context-fit and human authorization gates.

## Local evidence and handoff conditions

The sanitized [parser feasibility evidence](../checks/pdf-feasibility-2026-11-26.json) and [structural signal evidence](../checks/coverage-signals-2026-11-26.json) expressly limit their claims. They establish neither whole-PDF semantic coverage nor app lifecycle/model quality. The spine preserves those limits and the original-PDF evaluation baseline.

Documentation handoff can proceed from this lens once the parent completes the overall BMAD review. The first later authorized bootstrap owns pins, schemas/types and starter realization in the specified order. Feature work must consume that baseline. Live use additionally waits for the stated context/cost/provider/model/permission gates. None of these conditions authorizes implementation or API access now.
