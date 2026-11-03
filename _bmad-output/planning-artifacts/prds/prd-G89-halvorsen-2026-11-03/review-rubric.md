# PRD Quality Review — AI Study Buddy

## Overall verdict

This PRD is ready to guide UX, Architecture and story creation after light editorial cleanup. It makes the student's study workflow, temporary-session tradeoffs, citation-failure boundaries and quality acceptance concrete without claiming completed tests or forcing premature technical choices. The remaining risk is document maintenance: stale Discovery wording and repeated summaries of the same rules obscure an otherwise settled product definition.

## Decision-readiness — strong

The consequential decisions are explicit. V1 boundaries limits the product to one temporary PDF session, while FR-15–FR-18 specify what is lost, what survives rejection/failure and why session recovery cannot be assumed. Source verification chooses a real tradeoff: an unverifiable citation withholds a new summary, removes an entire affected card/question, or produces an error if nothing usable remains (FR-36–FR-37). Quality is allowed to reduce the set below ten rather than retaining invalid items.

Handoff conditions names the owners and stages for numeric resource bounds, extraction signals, matching and retries, permissioned files, assignment confirmation and evaluation preparation. These are appropriately staged technical/evidence dependencies for a solo assessed project, not evidence of an unresolved product scope. No additional parameter values or completed test artifacts are required to make the product direction actionable.

### Findings

- **low** Stale Discovery language understates decision readiness (§ opening, `prd.md:10`; Confirmed direction, `prd.md:35`; Features introduction, `prd.md:63`) — Phrases such as "Discovery is in progress", "remain inputs to be carried into the detailed requirements" and "will be added as Discovery continues" contradict the later statement that product-level review items are resolved. The evaluation/demo sections are already present. *Fix:* during final polish replace these with a concise statement of confirmed requirements and the explicitly owned downstream work; retain draft status until the review/polish gate actually closes.

## Substance over theater — strong

The named journey is functional rather than decorative: Camilla starts with Detailed to understand material, practises recall before seeing a card answer, confirms locked quiz answers, inspects original passages and resumes without losing position. These actions directly explain the unusual retained-state, language-replacement and source-panel rules. There is no unnecessary persona taxonomy or novelty claim.

The security requirements have concrete consequences: no model tool authority (NFR-1), inert content rendering (NFR-2), whole-reply structural rejection distinct from valid-set source filtering (NFR-3), credential boundaries (NFR-4), and separate working/evidence/provider lifetimes (NFR-5). Their mechanisms are left to Architecture rather than padded with generic scalability/security aspirations.

## Strategic coherence — strong

The thesis is clear in Product purpose: reduce preparation work so students can spend more effort understanding and practising, while remaining able to inspect the supporting course material. Summaries, recall cards, self-assessment and original-source inspection serve that same arc; the extra language/session details protect continuity rather than creating a second product.

Success measures check that thesis instead of merely counting generated output. SM-1–SM-4 test coverage, correctness and source support; SM-6 includes review/correction time and failed attempts in a like-for-like preparation comparison. Counterchecks explicitly prevent a larger output set or faster raw generation from masking poor quality. No learning-gain claim is inferred from a small local evaluation.

## Done-ness clarity — strong

The requirements carry testable consequences. For example, FR-20–FR-23 say exactly which summaries survive a language-change failure and when a successful change commits; FR-24 locks an answer only after explicit confirmation; FR-31 returns to the same card but hides its answer; and FR-36–FR-37 distinguish whole-summary withholding, valid-subset delivery and the zero-usable-item error. The examples make the consequential state transitions easy to verify.

The validation plan gives a feasible defined matrix, per-case thresholds, joint answer/source scoring, no unresolved summary factual errors, source-mapped coverage points, defect preservation and a T1 pilot. FR-41 does not pretend that the importance of missing PDF text is automatically knowable: it supplies a conservative product fallback and assigns observable criteria to Architecture. The absence of premature byte/time/retry numbers is acceptable under the named pre-use verification condition. Likewise, actual files and test execution are future evidence, not a prerequisite to a complete requirement.

## Scope honesty — strong

V1 boundaries explicitly excludes non-PDF input, accounts/login, synchronization, permanent history, learning plans, written-answer assessment, OCR/advanced repair and the advanced practice features most likely to creep into this project. Browser-saved progress is clearly a possible later extension after the tested core. FR-42 defines both saved-language/detail demo variants and the limit that own PDFs/fresh AI generation require live mode.

The artifact separates original source locations from semantic truth (FR-34), app cleanup from provider deletion (FR-46/NFR-5), and planned tests from completed evidence. There are no dangling product Open Questions or unmarked inferences requiring an Assumptions Index. Technical follow-ups have owners and revisit stages instead of pretending to have been solved. The small local evaluation and cross-discipline intent are not presented as broad validation.

## Downstream usability — adequate

The chain from UJ-1 to grouped FRs and then SMs is easy to extract. All 46 FR definitions, five NFR definitions and six SM definitions are unique and contiguous; the stable IDs remain usable even though they are grouped by feature rather than numerical order. References such as FR-15, FR-20–FR-23, FR-31, FR-36–FR-37 and NFR-3 point to the relevant rules. Camilla is the named protagonist of the single load-bearing journey.

The plain domain language and inline active-session definition are sufficient for this scope, although a short glossary would make isolated extraction more convenient. Architecture receives concrete boundaries through the addendum and named Handoff conditions, including permissioned fixtures, provenance, change-triggered evaluation and the separate evidence lifecycle. The larger extraction burden comes from duplication rather than missing domain definitions; the Shape fit finding addresses it without requiring a glossary merely to satisfy a checklist.

## Shape fit — adequate

Journey-led requirements fit this browser study application: UX and continuity are central, and the single named journey carries the context without persona overhead. Its rigor is greater than a casual hobby brief because source verification, bilingual content quality, saved demo behaviour and assessed educational delivery need to feed Architecture and stories. The document does not impose launch-scale operations or a large compliance program on the solo project.

Some narrative repetition is useful, but Confirmed direction now restates much of the journey and detailed requirements almost in full. The artifact would be easier to maintain if the top-level summary focused on the few defining decisions and tradeoffs, leaving interaction detail to UJ-1 and FRs.

### Findings

- **low** The top-level summary repeats detailed interaction rules (§ Confirmed direction, `prd.md:18–35`, compared with UJ-1 and the feature groups) — The long list repeats language commit semantics, source filtering, quiz interaction and card resumption that are fully specified later. Multiple full descriptions increase the chance that a future change updates one copy but not another. *Fix:* shorten Confirmed direction to the product's core capabilities, study/source thesis, temporary-session boundary and key tradeoffs; keep UJ-1, stable FRs and their acceptance examples authoritative for detailed behaviour.

## Mechanical notes

- IDs checked: FR-1 through FR-46, NFR-1 through NFR-5, and SM-1 through SM-6 are each defined exactly once, with no missing integers. Non-numerical presentation order reflects feature grouping and is not an ID gap.
- UJ-1 has one named protagonist and carries study context inline. There is no orphan journey.
- There are no inline `[ASSUMPTION]` or `[NOTE FOR PM]` tags, so no missing index roundtrip is implied.
- Terms such as Brief, Detailed, physical PDF page, View source and active study session are substantively consistent. A glossary is optional cleanup for extraction convenience, not a readiness blocker for this small product.
- The frontmatter remains `status: draft`, appropriately awaiting the root Finalize decision. Do not label this review as evidence that implementation or acceptance tests have passed.
- Findings: **0 critical, 0 high, 0 medium, 2 low**. Both findings are editorial and do not require new product decisions.
