# BMAD rubric and condensation fidelity review

Date: 27 November 2026 (Europe/Oslo).\
Verdict: **PASS — both minor editorial concerns were verified closed in the targeted follow-up below; no critical or high architecture blocker identified.** The condensed candidate preserves the adopted technical foundation and is suitable to replace the longer spine after review reconciliation; it does not authorise implementation or certify runtime, platform, model or billing behaviour.

## Targeted closure check — 27 November 2026

Verified only the two requested fixes against candidate SHA-256 `769fa1c9f8dc1fdec21b35da5a3527e6dfb504aa9c38e8639d7a594d2b158bae`; no further broad review was performed. **RC-L1: closed.** AD-6 now distinguishes the full 12 Summary / six card / six Quiz matrix, five Brief core points and ten Detailed eligible points from the all-five / five-plus-at-least-three pass thresholds, and freezes short-source adaptation and item/reference sampling/counting before full scoring. **RC-L2: closed.** DTO, IPC and RSS are expanded once before their technical use. The original findings below remain as the review record, not outstanding actions.

## Reviewed snapshots and limits

- Candidate: `ARCHITECTURE-SPINE.candidate.md`, SHA-256 `41a0d7a29f0fe2c2abd7a18952386f1769cc08616f70f323d7b45237d06f6957`; 4,567 whitespace-delimited words, 318 lines.
- Canonical source: `../ARCHITECTURE-SPINE.md`, SHA-256 `410dc0ef55b9a43bfce68d88e6dc1e111fada44cb1a6b339d92d569510e8e035`; 10,164 words, 427 lines.
- Rubric: `.agents/skills/bmad-architecture/references/reviewer-gate.md`. Also checked current PRD/addendum, the final EXPERIENCE contract, and the previous rubric/adversarial reviews for inherited requirements and unresolved seams.

This is an independent documentation review. Only this report is written. No application code, tests, private PDF inspection/extraction, API/provider calls, browsing, installations, builds, server execution or purchases were performed. Technology links and dated evidence were not independently reverified. Candidate relative links are intentionally evaluated at its intended canonical parent location, not its temporary `reviews/` location.

The user's request for one understandable English technical foundation with concise reasons governs the presentation. Short rationale is useful here; the review does not require an artificially terse list or a full duplicate of the PRD/UX specifications.

## Critical and high findings

None. No adopted AD is removed, renumbered or materially weakened. No deferred item grants two dependent units permission to invent incompatible contracts after the stated bootstrap prerequisite.

## Minor findings

### RC-L1 — Make the evaluation recap distinguish the candidate pool from the pass threshold

**Severity:** Low, documentation precision; not a weakened binding threshold.\
**References:** Candidate AD-6, lines 126–128; current PRD, Manual evaluation protocol, points 2–5; addendum, Evaluation and regression evidence.\
**Disposition:** Autofix during final polish; no new user decision or evaluation is required.

The candidate correctly preserves five Brief points, those five plus at least three additional Detailed points, unchanged per-case/joint 9/10 or all-smaller-set thresholds, original-PDF review, no post-result baseline changes and the full 12/6/6 matrix. The PRD is explicitly authoritative, so nothing permits reducing its criteria. However, the compact recap does not distinguish the PRD's **ten Detailed eligible points** from the Detailed passing coverage threshold, and it does not restate frozen item/reference sampling and counting before full scoring. The longer canonical AD-6 already uses a similar shorthand; this is not a new contradiction introduced by condensation.

For a document that will be read as the single technical foundation, add one short clause: “Freeze five Brief core points, ten Detailed eligible points and item/reference sampling/counting before full scoring; Detailed must cover the five core points plus at least three additional points.” Keep pre-agreed short-source adaptation and the existing pilot/PRD authority. This prevents a reader from interpreting eight expected points as the complete Detailed candidate pool. Do not introduce different thresholds or require new calls now.

### RC-L2 — Expand three boundary abbreviations once

**Severity:** Low, reader accessibility.\
**References:** Candidate dependency diagram/rules, AD-11/AD-12 and bootstrap contract.\
**Disposition:** Optional editorial autofix before final delivery.

The candidate is substantially easier to navigate than the longer source and retains a short reason for every decision. A few compressed terms still assume implementation experience. Expand “DTO” to “typed data contract,” “IPC” to “parent/child process messages,” and “RSS” to “observed process memory” at first use. The technical names may remain in parentheses for agents. This improves readability for Camilla and the lecturer without adding more architecture, explaining every implementation detail or changing any decision.

## Good-spine checklist

| Criterion | Assessment |
| --- | --- |
| Real divergence points fixed | **Pass.** One frontend controller, one API/session authority, one canonical contract owner, source eligibility, request relevance, one-shot startup, process supervision, numeric cost authority and demo/live boundaries are explicit. |
| Rules enforceable and aligned with their stated prevention | **Pass.** All 17 decisions retain Binds/Prevents/Rule, clear authority and concrete failure/publication constraints. No cancellation, billing, semantic detector or hard-memory guarantee is inferred from weaker mechanisms. |
| Paradigm and allowed dependencies | **Pass.** Client-server with a modular monolith backend is named. Services compose, adapters return data, contracts remain pure, and the worker cannot import assembly/secrets/session/cost authority. Small modules/functions suffice. |
| Deferred items cannot silently diverge | **Pass.** Runtime/lock baseline comes first; backend schemas, IPC, lease wire meanings and frontend types come next, before parallel dependent work. Verification mechanics have named owners and acceptance triggers. These roles need not be assigned to named people at this documentation checkpoint. |
| Spec capabilities and quiet UX rules | **Pass.** PRD/addendum and final UX retain explicit authority. The candidate preserves the structural decisions needed for the fixed-language/level session, practice/source flows, safe failures and key-free demo. It does not need to repeat every keyboard, visual or scoring detail to keep them binding. |
| Operational/environmental envelope | **Pass.** Native development, same-origin loopback demonstration, optional one-service Docker, Mac/Windows targets, scratch cleanup, singleton live authority, context exclusions and restart-safe numeric accounting are covered. Minimum versions and measured platform behaviour remain explicit gates. |
| Technology verification/currentness | **Pass as an honest evidence boundary, not a currentness certificate.** Families are adopted; exact compatible pins are a pre-feature bootstrap obligation. pypdf and Gemini/Vertex remain provisional. The catalog/prices are dated and explicitly not account availability or educational evidence. No web verification was authorised for this review. |
| Brownfield/parent consistency | **No conflict identified.** This is a proposed application foundation, not a claim to ratify a working implementation. All adopted source ADs are retained; technology.md remains an adapted reference. |
| Appropriate IBE160 scope and readability | **Pass, with RC-L2.** No database, RAG, generic agent framework, queue service or mandatory Docker stack is added. Process supervision and platform verification remain real work, justified by already adopted resource/cleanup constraints rather than new production scope. |

## Fidelity checks that matter

**All numerical limits remain intact.** The candidate preserves 10 MiB upload, 50 physical pages, 100,000 retained and 1,000,000 original code points, one shared heavy slot, two workspaces including cleanup, 30-second upload and separate 30-second child deadlines, 120-second generation deadline, 2 MiB UTF-8 result, observed 256 MiB RSS sampled every 250 ms, 30-minute renewable lease, 60-second heartbeat, 30-second sweep/five-second release target/31-minute backend deletion deadline, US$5 project total, `max_tokens=8192`, and maximum US$0.30/US$2.50 input/output rates. It retains the conditional US$0.35 reservation seed without presenting it as a guarantee or permission.

**Readable-text and source rules remain intact.** Missing visual/table material and unknown completeness do not become blanket stops. Known unsafe fragments/tables are excluded, or their whole page when that is the smallest reliable boundary. Unisolatable meaning-affecting retained-text failures and insufficient usable text stop. Original page positions and text remain separate from retained scope. Exact matching precedes NFC plus collapsed whitespace, with no fuzzy, translation, compatibility, case, punctuation, hyphen or number repair. Excluded content is ineligible; location matching is not factual support. Malformed structures reject the whole reply; any invalid new Summary reference withholds that Summary; any invalid card/Quiz reference removes its whole item. Nonempty valid subsets use actual counts, never automatic refill.

**The quiet lifecycle/UX constraints remain intact.** Navigation does not invalidate an otherwise current attempt or force publication navigation. Source close preserves the revealed card and trigger focus; function return preserves card position and shows the front. Quiz draft/locked answers and actual-count scoring remain memory-owned. Navigation, source inspection and same-set restart do not generate or fetch source content. Confirmed New session clears immediately; cancellation preserves; expired/ended identities cannot revive. The server checks expiry before access/renewal and server work never renews itself.

**The prior seam findings are closed more explicitly than in the longer source.** Candidate lines 299–306 assign child request/result IPC and lease clock/unit semantics to the backend contract owner before parallel frontend/adapter/worker work. The dependency diagram now shows pure-contract edges for the supervisor, adapters and child, while the prose prohibits impure/bootstrap imports. Candidate line 32 also replaces the stale suggestion that adopted AI/resource choices still need to be made. These resolve prior R-M1/R-L1 and the lease/IPC watchpoint without inventing a new protocol or service.

**Privacy, costs and delivery remain separate authorities.** Per-upload acknowledgement precedes every external-content transfer, terms/settings must support retention claims, ordinary logs exclude study content, and deliberate evaluation/demo evidence needs separate permissions and handling. The content-free cost file and sidecars stay ignored and never reset with study state; unresolved charges remain reserved or block live use. Saved demo build/start/health/use requires neither key, provider request nor live cost-file initialisation; an environment key cannot enable live mode silently. Both languages and Summary levels, approved shareable assets, Docker context exclusions, ephemeral scratch and an existing mounted cost directory for later authorised live Docker operation remain binding.

## Gate interpretation

The bootstrap and verification order is sufficiently clear for this altitude. Exact packages, schemas, RSS reader, crash mechanics, minimum host versions, approved demo assets and complete-request billing/context evidence are **owned prerequisites**, not independent feature freedoms and not proof already obtained. PRD model evaluation and provider/account verification remain separately authorised pre-live work. A candidate failure returns to a coached choice; it does not allow silent fallback, reduced cases or weaker quality.

RC-L1 and RC-L2 can be addressed as small text edits. No further architectural coaching question is required by this lens. Reconcile the other reviewers and preserve the documentation-only boundary when finalising the spine; final architecture review grants no permission to implement, call APIs, purchase or publish.
