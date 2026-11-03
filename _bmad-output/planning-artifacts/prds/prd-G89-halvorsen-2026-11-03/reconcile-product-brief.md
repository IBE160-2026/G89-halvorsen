# Input reconciliation — Product brief bundle

Reviewed 2026-11-03 against the current draft `prd.md`, `addendum.md` and the chronological decisions in `.memlog.md` through the approved security/evaluation plan and Finalize audit.

## Inputs and precedence

- [Product brief](../../briefs/brief-G89-halvorsen-2026-09-26/product-brief.md), draft updated 2026-10-29.
- [Supporting context](../../briefs/brief-G89-halvorsen-2026-09-26/addendum.md).
- [Brief decision history](../../briefs/brief-G89-halvorsen-2026-09-26/.memlog.md), including overrides of the original broader scope.

The brief is the baseline. Later confirmed PRD decisions take precedence. Earlier proposals and superseded brief decisions are not requirements to restore. Missing implementation, completed tests or technical parameter values are not counted as reconciliation gaps.

## Verdict

The central learning workflow and source-verification intent are preserved and substantially refined. Four bounded carry-forward gaps remain: the full explicit scope exclusions, educational delivery context, the original primary-user/initial-evaluation context, and explicit unsupported/damaged-file error coverage. These can be repaired from already supplied material without new feature decisions.

## Genuine gaps

### G1 — Complete the explicit scope boundary

**Source:** brief, Scope and Vision (lines 83–91); supporting context, Current decisions and Later scope.

The current PRD excludes accounts, automatic study-history saving, scanned-PDF support, adaptive learning and several advanced practice features. It does not explicitly carry forward all of the brief's exclusions: plain-text/other non-PDF inputs, login, cross-device synchronization, personal learning plans and written-answer assessment. Browser-local saved progress was explicitly optional phase 2 only after the core had been implemented and tested. Current temporary-session rules correctly exclude restoration in v1; the original optional future item should not be mistaken for an outstanding v1 obligation.

**Suggested disposition:** add one concise scope paragraph grouping the retained exclusions, with optional phase-2 saved progress clearly separated from v1. Keep future accounts/synchronization/plans as possibilities rather than commitments. No new approval is needed to retain these earlier agreed boundaries.

### G2 — Preserve the educational deliverables and constraints downstream

**Source:** brief, Executive summary and Success Criteria (lines 14, 71, 77); supporting context, User-provided assessment requirements (lines 3–11).

The PRD records an IBE160 project and calls for test evidence, but neither current PRD nor its addendum explicitly preserves the requirement to document how AI was used and how code was quality-assured, or the reflection report about process/challenges/solutions. The user-provided 70% code/functionality and 30% reflection weighting and current approximate submission window are likewise available only by following the original input link.

**Suggested disposition:** place the educational delivery context in the current addendum or a short delivery-constraints paragraph. Preserve mid-December 2026 as approximate, exact date unconfirmed; the original assignment/full rubric have not been supplied. Do not revive the older late-November/early-December estimate from the historical memlog or treat the old brief deadline as current. Numeric grading weights are context, not application acceptance thresholds.

### G3 — Retain the primary-user and initial-evaluation context

**Source:** brief, Who This Serves (lines 42–46), The Problem (lines 20–22); supporting context, Current decisions.

The PRD appropriately broadens supported study material across disciplines and makes IBE110 illustrative. It does not retain that the initial design/evaluation anchor is a Molde University College bachelor's student in IT-related subjects, studying independently before exams, with initial evaluation using the developer's own courses/materials. Broader subject support does not itself supersede that initial audience or establish broad validation.

**Suggested disposition:** retain the primary-user context and initial evaluation boundary in a compact audience/evidence statement. Keep IBE110 illustrative, other disciplines supported within the documented PDF envelope, and wider usefulness/learning effects unproven. Do not restore the approximately 40-slide example as observed research.

### G4 — Make the inherited file-error cases explicit

**Source:** brief, Error handling criterion (line 68); supporting context, PRD downstream work (line 31).

FR-1/FR-38 establish text-based PDF scope, FR-39/FR-41 cover processing failures and unreliable coverage, and FR-43 adds password rejection. SM-5 broadly mentions unusable-PDF handling. The original explicit planned cases—unsupported formats such as `.txt`, invalid/damaged PDFs and scanned PDFs without extractable text—are not named together as acceptance fixtures or corresponding refusal cases. A generic coverage failure should not silently replace format/parse validation.

**Suggested disposition:** carry these existing planned negative cases into the failure acceptance examples or validation plan. Require an understandable explanation and useful next step, preserving an existing session when a replacement is rejected. Do not add OCR, repair or password support. Exact parser signals and fixtures remain implementation/test-protocol work.

## Detailed extraction and mapping

| Source intent or requirement | Current destination | Reconciliation |
| --- | --- | --- |
| Save study-material preparation effort to leave more time for understanding/practice | Product purpose; UJ-1; SM-6 and counterchecks | Preserved. Review/correction effort and failures are now included, with no claimed achieved savings or learning gain. |
| Simple browser-based app, manageable for a beginner/solo course project | Confirmed direction; UJ-1; temporary-tab session requirements | Browser use and limited solo-project stakes are present. Educational process/documentation constraints need G2. |
| University/college students; initial IT bachelor's student at Molde; own-course evaluation | Cross-discipline purpose and Camilla UJ-1 | Wider supported subjects are an accepted refinement; initial audience/evaluation context needs G3. |
| Upload text-based academic PDF notes/slides/readings, generate all three aids | FR-1, FR-2, FR-38; summaries, cards and quiz groups | Preserved. Later user decisions add compendia/material, reliability boundaries and one active PDF. |
| Bokmål/English output independent of source language | FR-4; FR-20–FR-23; SM-1–SM-3 | Preserved and refined with per-function success-only language replacement. |
| Brief main points/key concepts; Detailed fuller source-grounded explanations/examples | FR-5, FR-6, FR-20; manual evaluation protocol | Preserved. Both levels can coexist after generation; no regeneration just to switch. |
| Summary levels do not govern cards/quiz/wrong-answer explanations | FR-5, FR-9 | Preserved. |
| Comprehension questions may appear at the end of summaries | FR-19 | Explicitly superseded: summary leads to the existing quiz; no separate questions/set/mode. Do not restore. |
| Multiple-choice quiz, feedback gives correct answer, explanation and source | FR-8–FR-10, FR-13, FR-24–FR-29 | Preserved with confirmed one-at-a-time/four-option/locked-answer/result/restart flow. |
| Fuller explanation after an incorrect answer | FR-9; chronological PRD memlog explains wording reconciliation | Later user asked for a short explanation that explains the error and correct answer. No separate long-explanation mode was agreed. The source's "fuller" must not be inflated to an additional "full explanation" feature. |
| Source filename, physical page position from 1 and short excerpt; View source | FR-11, FR-12, FR-34, FR-35 | Preserved and refined into a simple sidepanel with original-language excerpt highlighting, multiple supporting passages and return without losing place. A real PDF viewer/highlighting is explicitly outside v1. |
| Excerpt occurrence does not establish correctness or semantic support | FR-34; SM-4; manual evaluation protocol | Preserved. Generated paraphrases cite original supporting passages, not invented quotations reproducing generated wording. |
| Unmatched excerpts produce warning | FR-36, FR-37 | Explicitly superseded: bounded recovery, no invalid-looking citation; omit persistent source-invalid cards/questions, deliver valid subset with notice, error/retry if none. Prior valid state survives failure. |
| Existing source location for every displayed reference | FR-11, FR-36, FR-37; SM-4; NFR-3 | Preserved and strengthened with application validation. Human semantic review remains separate. |
| External language-model API; candidate Gemini model provisional | Material-handling requirements; FR-42; NFR-4; Architecture follow-ups | Live external generation remains planned and separate from demo. Not copying an optional model candidate into product requirements is appropriate; model choice remains Architecture-owned. |
| One predefined document with saved aids, clearly labelled demo, runnable without private key/paid account | FR-42; external-processing acceptance example; SM-5 | Preserved at baseline level. Exact saved variant/action coverage is a separate Finalize review issue, not a missing source requirement for a particular mechanism. |
| Three PDF categories and bilingual/detail test matrix | Validation plan; SM-1–SM-3 | Matrix retained. Later accepted size bands T1 1–10, T2 15–25, T3 30–40 supersede old bands; neither old nor new test bands are upload limits. Language/content axes remain additional coverage. |
| Summary factual review; correct cards/keys; relevant supporting references; 9/10 thresholds and all-pass smaller samples | SM-1–SM-4; confirmed manual protocol | Preserved and refined with no unresolved summary factual errors, predefined source-mapped coverage and joint answer/source scoring. |
| Feedback/error/demo functional acceptance and defect correction/retest | SM-5; relevant feature acceptance examples | Preserved broadly; explicit inherited file-error case list needs G4. |
| Time comparison and usefulness, not established benefits | SM-6; counterchecks; manual protocol | Preserved. Raw generation speed cannot stand in for completed preparation effort. |
| Broader testing not required for initial evaluation; exact files selected later | Final review follow-ups; protocol preparation | No broad-user test is imposed. Missing actual files/results are correctly described as future work. Initial own-course rationale needs G3. |
| No accounts/login/sync/plans/adaptive recommendations/written-answer assessment/non-PDF/OCR in v1 | Confirmed direction and several feature-specific exclusions | Partly explicit; complete boundary through G1. |
| Same-browser saved progress only optional phase 2 after core tested | FR-17 prevents v1 restoration; no v1 history | Compatible with later stronger temporary-session choice. Future optional item should be distinguished through G1, not implemented as a v1 task. |
| Detailed limits, errors/demo/material lifecycle to PRD; mechanism/model/library/key setup to Architecture/README | FR-14–FR-18, FR-21–FR-23, FR-36–FR-46; NFRs; final follow-ups and current addendum | Product behaviour is substantially resolved; technical caps/retry/matching/stop criteria are appropriately owner-assigned downstream. README demo requirement is explicit. `.env.example` is a teacher recommendation rather than a locked product mechanism. |
| Honest positioning: overlapping existing tools, no uniqueness claim | Product purpose and limited-project direction make no uniqueness claim | Intent is respected. The PRD need not reproduce a competitive section or vendor URLs to avoid unsupported novelty claims. |
| Future accounts/sync/learning plan only if a useful first version warrants them | Not committed in current PRD | Correctly not promised. A compact future-scope statement under G1 is enough if retained. |
| Norwegian conversation, English documents; product name AI Study Buddy, project folder unchanged | English artifact; PRD memlog language override; workspace paths | Preserved. Earlier English-only conversation instruction was expressly superseded. |
| Coaching preference and shaping decisions together | PRD Discovery description and chronological decision log | Preserved; source-derived additions should remain distinguished from later user approvals. |

## Items intentionally not treated as gaps

- Historical larger-scope decisions about saved inter-visit progress, accounts, personal plans or plain-text input were superseded and must not be recovered as current requirements.
- Exact output length, upload bytes/pages/text/time, retry count and matching normalization were never established by the source brief. Their absence as invented values is correct; owners and pre-use verification conditions are present.
- The original brief's precise headings and paragraph formatting were user requirements for that brief, not a mandated PRD schema.
- The older approximate deadline in the brief memlog is historical. The current supporting-context estimate is mid-December, with exact date still unconfirmed.
- Source reports, actual PDF fixtures, live provider tests and completed application validation are not expected to exist merely because the PRD is being finalized. The artifact correctly distinguishes planned checks from results.
- Original assignment and full grading rubric are missing supplied inputs, not evidence that additional application features are required. Current follow-up to confirm them before delivery planning is appropriate.

## Qualitative intent check

The PRD preserves the source's useful emphasis: a simple workflow, understandable explanations, source checking that students can perform themselves, and a stable scope suitable for a beginner. The later accepted navigation/session rules make the original ease-of-use intent concrete. Claims remain modest, and source occurrence is not conflated with correctness. The gaps above concern retaining the educational/audience/scope context and explicit negative cases, not expanding functionality.
