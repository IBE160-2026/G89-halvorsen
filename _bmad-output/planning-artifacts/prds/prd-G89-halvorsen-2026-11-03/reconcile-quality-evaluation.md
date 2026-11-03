# Input reconciliation — Quality and evaluation research

Reviewed 2026-11-03 against the current `prd.md`, `addendum.md` and latest chronological PRD `.memlog.md` decisions.

**Input:** [Technical research: Quality and evaluation](../../research/technical-quality-evaluation-2026-11-02/research.md), completed 2026-11-02. The report separates findings, proposals and open questions. Its status is completed research, not completed application validation.

## Verdict and precedence

All approved headline evaluation decisions are represented: the case matrix and baseline thresholds, full manual summary factual review, predefined source-mapped point coverage, joint answer/source scoring, first-output/failure preservation, fair preparation-time comparison, T1 pilot and freezing the concrete protocol before full scoring. No additional app test execution or populated evidence file is required merely to finish this PRD.

The source report's statement that paired scoring and summary thresholds remain unapproved is historical. The user approved them later, as recorded near the end of the PRD memlog. Likewise, its open UI question about invalid/unmatched references is superseded by the PRD's bounded recovery, valid-subset and zero-valid-output rules.

Three bounded protocol-detail gaps or insufficiently explicit carry-forwards remain. They need not expand the product or block Architecture: retain the underlying intent and assign the concrete protocol before scoring. Where the source only proposes a refinement, do not present it as separately user-approved without that qualification.

## Remaining gaps

### G1 — Make the independent manual review basis explicit

**Source:** §3 Proposed manual rubric, especially the opening paragraphs and Both languages row.

The report says to compare factual meaning with the **original visible PDF**, using extracted text only as an aid, and to inspect definitions, numbers, negation, conditions, exceptions and technical terms. It also says that an ambiguous or apparently wrong source should be recorded and clarified, rather than silently accepted or corrected. The current manual protocol says "against the source" and excludes an unclear passing verdict, but it does not make the original-visible-document basis explicit. Review against only the application's extracted excerpt could miss extraction errors and weaken the independence of the manual check.

**Disposition:** clarify the basis in the manual protocol or its test-protocol handoff. Both output languages require their own meaning checks; original-language quotations are not language failures. The exact annotation fields can be assigned to Camilla before the T1 pilot/full scoring. No new numerical threshold is needed.

### G2 — Preserve the multi-reference/citation-coverage counting issue

**Source:** §3 Reference proposal; §4 Protocol steps 3 and 5; §6 citation-granularity open question.

FR-35 permits multiple passages and SM-4 separates reference support from joint item-level correctness/support. However, the current protocol does not explicitly say how a multi-claim summary or multi-reference answer is judged for **complete support**, or how a missing citation enters the denominator. A valid or relevant selected reference must not allow other unsupported factual content in the same assessed item to disappear from the evaluation.

The source proposes four judgments: location existence, excerpt occurrence, semantic support and citation coverage. It further proposes recording both a selected-reference result and whether all attached passages collectively support the whole assessed claim. Exact selection/counting rules were not separately adopted in the current memlog and can remain protocol choices; the gap is losing the issue entirely rather than deferring it explicitly.

**Disposition:** retain this as an owner-assigned protocol definition, with Camilla freezing the claim/item/reference counting unit and missing-citation rule after the T1 pilot and before full scoring. Keep summary detail levels separately assessable. Product failure policy for an item with one bad reference among several remains a separate product review question, not resolved by this report.

### G3 — Make demo-quality and reproducibility follow-ups explicit

**Source:** §4 Protocol steps 2 and 6; §5 retained-evidence paragraphs; §6 reviewer/variation limitations.

FR-42 and SM-5 correctly distinguish the saved demo from live integration, and the protocol preserves initial outputs, failures, omitted items, defects, corrections and retests. The following source refinements are not explicit in the current PRD/addendum handoff:

- Apply the **same manual content rubric** to the saved demo aids, separately from the key-free demo workflow check. Editing a saved demo does not establish a live-generation fix.
- Retain enough run provenance to reproduce/interpret results: case/output/item ID, live/demo mode, document/version and source pages, model/prompt/settings version, date and reviewer. A simple Markdown log suffices; no evaluation service or history feature is required.
- After a model/prompt/extraction change, regenerate affected cases and recheck relevant regression examples; preserve earlier results. If the pilot reveals instability, investigate/repeat affected cases rather than claiming general reliability from one selected run.
- Record unresolved subject/language judgments; use competent help where needed and disclose single-reviewer limits. A second reviewer is useful, not a mandatory new requirement.

**Disposition:** assign these proposed evidence/protocol details to Camilla before full evaluation and to implementation regression work when the generation pipeline changes. Do not imply that any checks have run, that a second reviewer is compulsory or that all cases must be repeatedly rerun without cause.

## Full extraction and coverage mapping

| Source intent | Current mapping | Status |
| --- | --- | --- |
| Separate correctness, source support, coverage and usefulness rather than use one masking aggregate | SM-1–SM-6; separate/joint scores; counterchecks | Preserved. |
| Bounded local manual acceptance, not general model accuracy or proven learning gains | SM-6; planned-check wording; follow-ups | Preserved. No app results claimed. |
| 12 summary, six card and six quiz cases; not independent population-accuracy estimates | SM-1–SM-3; protocol per-case reporting | Preserved. No broad inference is made. |
| Review every summary factual claim; no unsupported additions/contradictions or unclear passing result | Manual protocol item 1; SM-1 | Approved and preserved. G1 improves explicit review basis. |
| Source-mapped five Brief core points/ten Detailed eligible points, all five plus at least three additional for Detailed; short-source exception fixed before scoring | Manual protocol item 2 | Approved and preserved. Actual points/eligible shorter lists are future protocol inputs. |
| T1 pilot to check feasibility/workload before full evaluation | Manual protocol item 2 and closing protocol sentence | Approved and preserved. No pilot is represented as already executed. |
| Card accuracy, sufficiency, clarity and no duplication; independently assess usefulness/support | FR-7, FR-30; SM-2, SM-4 | Core product qualities preserved; detailed annotation rows remain test-protocol work. |
| MCQ one defensible key, plausible distinct alternatives, no ambiguity/clues, correct feedback | FR-8, FR-9, FR-24, FR-28; SM-3–SM-5; NFR-3 | One correct/unambiguous key and structural validation preserved. Plausibility/clue review are source-proposed rubric refinements suitable for protocol, not a new quiz mode. |
| Review both languages semantically, especially negation/numbers/terms; preserve original quotations | FR-4, FR-11; bilingual SM matrix; protocol language review | Preserved at headline level; G1 makes the method explicit. |
| Existing locations for all references; 9/10 relevant/supporting references, all-pass smaller cases | FR-11, FR-34–FR-37; SM-4 | Preserved. Occurrence is not semantic support. |
| Same sampled item jointly passes correctness and source support | SM-4; manual protocol item 3 | Later approved joint 9/10/all-pass policy supersedes source's earlier open question. |
| Account for missing support/coverage and multiple passages | FR-35; SM-4 | Product allows multiple sources; exact protocol counting issue needs G2. |
| Select samples before quality review and avoid swapping in better runs/items | Manual protocol item 4 | Approved and preserved. Exact sample/reference-selection rule is explicitly deferred. |
| Seeded sampling when more than ten, inspect all when ten or fewer; no mandatory second reviewer | Actual sampling rules deferred to protocol; standard generated set is at most ten | Appropriate deferral. Do not infer another sampling requirement or artificial set size from this proposal. |
| Save first complete output and failed attempts; record defects/fixes/retests | Manual protocol item 4; SM-5 | Approved and preserved. G3 adds proposed provenance and change-triggered follow-up. |
| No pooled result hiding a failing language/document/type | Manual protocol item 4 | Approved and preserved. |
| Check wrong-answer key/explanation/reference; try a wrong option for each reviewed item | FR-9; SM-5 | Expected feedback preserved. Specific wrong-option exercise belongs in the detailed protocol. |
| Automate schema/key/location/quote rules, not semantic truth; no extra learned evaluator needed | NFR-3; FR-34–FR-37 | Preserved. Automated metric/judge proposals were not adopted. |
| Negative examples: reversed negation/changed number, wrong page, empty/missing reference, ambiguous MCQ, bad translation, invented example, omitted key point | Source/structure requirements; SM-1–SM-5 | Suitable regression/protocol fixtures, not missing product features. G3 assigns relevant regression follow-up without requiring test execution now. |
| Saved demo checked with same content rubric; live and demo results distinct | FR-42; SM-5 | Distinction preserved; same-rubric requirement should be explicit through G3. |
| Compare equivalent manual/app-assisted tasks including review/corrections; disclose familiarity/order effects | SM-6; protocol item 5; counterchecks | Later approved and preserved, now explicitly including failed attempts. |
| Model/prompt changes trigger affected-case reevaluation; variability needs modest claims | Generic corrections/retests only | Proposed detail should be retained through G3. No claim of current model performance is made. |
| Historical research evidence is not current-model/Bokmål validation | Research linked as input; no imported scores or performance claims | Preserved by not transferring external benchmark scores or claiming app results. |

## Non-gaps and remaining ownership

- Actual permissioned PDFs, source-mapped points, concrete sampling/reference rules, timing tasks, item logs and results are intentionally future inputs. The current PRD names Camilla and the T1-pilot/before-scoring condition; the review does not demand that they already exist.
- The source's example automated measures and LLM judges are optional research possibilities, not required evaluation infrastructure. Their historical freshness/transfer limits would matter if later adopted; they do not block a manual scoped PRD.
- The research's original UI fallback question is settled by later PRD decisions. Warning-only acceptance of an unmatched quotation must not be reintroduced through evaluation reconciliation.
- Numerical release targets remain project acceptance choices, not scientifically established reliability standards. Known errors still require correction/retest even if a threshold passes.
- The saved-demo/action variant scope and any summary/multi-reference failure-boundary product decisions remain with the root Finalize review; this extraction does not choose them.
