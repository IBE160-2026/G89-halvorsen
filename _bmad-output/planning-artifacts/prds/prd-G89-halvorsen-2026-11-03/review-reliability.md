# Reliability and privacy review

## Verdict

**Pass for the PRD gate, with one low-severity UX clarification.** No critical, high or medium reliability/privacy contradiction was found in the reviewed requirements. The adopted app-owned cleanup boundary, malformed-reply and source-failure rules, and bilingual saved demo resolve the earlier material questions.

This is a document review of the current `prd.md` and `addendum.md`, checked against the latest decision-log entries for the three approved clarifications. It is not application validation, a provider audit or a legal-compliance determination.

## Findings by severity

### Critical

None.

### High

None.

### Medium

None.

### Low — R1: Define the flashcard position after successful language replacement

**References:** FR-21, FR-30 and FR-31.

The current function is replaced on a successful language change. FR-31 specifies position retention when returning from Summary or Quiz, but neither it nor FR-21 says where a successfully replaced flashcard set starts. The regenerated set may be shorter: a student could be on card 10 of 10 before the change and receive seven valid cards afterwards.

This is not a privacy or architecture blocker. Record a simple explicit outcome during UX refinement, such as starting the replacement set on the first card's front. Keep the existing set/position on failed replacement under FR-23. Do not apply navigation-only position retention to a new set without checking that the position exists.

**Disposition:** Minor refinement, suitable for the next UX specification or a short PRD acceptance example. No new feature or additional progress storage is needed.

## Coupled-flow review

| Scenario | Relevant requirements | Review result |
| --- | --- | --- |
| New accepted upload, before any external AI check/generation | FR-44/45 | Active acknowledgement must precede extracted-content transfer, including an external AI check. A notice alone cannot satisfy the gate. No contradiction found. |
| Replacement cancelled or rejected | FR-15, FR-43, FR-45 | Prior PDF, study aids, practice state and acknowledgement remain. A failed candidate must not be treated as an accepted new session. No contradiction found. |
| Replacement accepted or Clear confirmed during a request | FR-14–18, NFR-5 | Old-session results cannot repopulate the cleared or new session. App-owned working copies are removed according to the adopted boundary. Architecture must implement and verify identity/invalidation and cleanup; no fixed mechanism is required by this PRD. |
| Reload or close | FR-17, NFR-5 | No session restoration; any other app-owned ended-session copies have finite cleanup expiry defined and tested downstream. This avoids equating a non-restored UI with proof that every backend copy disappeared immediately. |
| Clear versus provider storage and original file | FR-16, FR-46, NFR-5 | Original disk file is unaffected, app-owned cleanup is separately required, and provider storage is not represented as recalled or deleted by Clear. No zero-retention or legal-clearance promise is made. |
| Ordinary logs versus deliberate evidence | NFR-4/5; addendum evaluation evidence | Runtime app/SDK/error logs cannot contain the study material. Permitted evaluation/demo artifacts are a separate intentional record with owner, access and review/deletion conditions. No automatic student-history exception is implied. |
| Both summary levels exist; language change succeeds/fails | FR-20–23, FR-36 | Confirmation precedes generation; both old-language levels remain until success. Success installs the requested new-language level and removes the old-language levels, without changing other functions. Failure preserves previous valid summaries. |
| Started quiz language change succeeds/fails | FR-21–23 | Success replaces quiz content and resets answers/progress after explicit confirmation; failure/cancellation preserves old content and state. No reset-on-request-start conflict found. |
| Well-formed card/quiz set contains invalid references | FR-35–37, NFR-3 | Finite source recovery precedes filtering. Any persistently invalid reference rejects its whole item, even when other references are valid. Remaining usable items use actual counts and notices; zero usable items gives an error/retry and preserves prior state. |
| Structurally malformed model reply | NFR-3, FR-37 | Whole-reply rejection is explicit. Source-invalid-item filtering cannot be used to salvage a structurally malformed reply. |
| New summary retains one invalid citation after recovery | FR-36 | The whole new summary is withheld and prior valid content is preserved. The rule no longer leaves partial-summary publication open. |
| Excerpt exists but does not support the generated claim | FR-34/35; SM-4; manual protocol | Excerpt location is not represented as factual validation. Manual checks review support against the original PDF, including multi-reference claims. No implementation-time guarantee of semantic correctness is inferred. |
| Main-text coverage cannot be established | FR-38–41; addendum | Conservative stop and understandable recovery are explicit. Architecture owns observable criteria and representative checks without a claim of detecting every important omission. |
| Source panel opened/closed or learning function changed | FR-3/12/13/31 | Source-panel closure preserves place/state. Returning from a different learning function preserves flashcard position but hides its back; a source-panel visit is expressly not such a switch. No contradiction found. |
| Saved demo language/detail selection | FR-42 | Both languages and both summary levels have saved variants; actions truthfully load saved content. Own PDFs/fresh generation require live mode, and unsupported demo actions show a limitation. General confirmation/progress rules still apply where relevant; demo playback is not live-generation evidence. |

## Downstream verification, not gate findings

- Architecture must choose and verify numeric upload/resource/time bounds, finite source-recovery caps, source matching/normalization, observable extraction coverage criteria and cleanup expiry/mechanisms. Their current lack of numerical values is explicitly assigned work, not a missing product outcome.
- Tests should exercise rejected/accepted replacement, Clear with delayed responses, acknowledgement before every newly accepted upload's first transfer, failed new-language generation, structural failure versus source-only failure, reduced/empty valid sets, invalid new summaries and saved demo controls. This review does not claim any such test has run.
- The selected provider's actual project configuration and terms must be checked before real transfer. This review neither repeats dated provider-specific figures as current facts nor converts acknowledgement into material-use permission or legal clearance.
- UX should make confirmation, loading and limitation messages clear and reflect the current function/language rather than imply automatic generation of all study aids.

## Review boundary

No stack, provider, retention duration, source-matching algorithm or new feature is selected. The low finding can be resolved without expanding scope. Material reliability/privacy outcomes are sufficiently specified to proceed to the next planning stage, with implementation evidence still outstanding as explicitly documented.

## Final conformance after editorial condensation

**PASS.** Targeted comparison of the condensed PRD and addendum against the latest confirmed decisions found no material loss in the requested reliability/privacy/evaluation boundaries.

- FR-20–23 retain both old summary levels until successful language replacement, then replace both with the requested new-language level; failure preserves prior work. Quiz answers/position survive failed changes and function navigation; successful replacement resets the quiz.
- FR-31 now resolves R1 explicitly: a successful new-language flashcard set starts at its first front, including shorter sets; failure preserves the old set/position. Source-panel closure remains distinct from a function return and does not reset an exposed card to its front.
- FR-45 retains per-accepted-upload active acknowledgement before any extracted-content transfer to external AI, including checks. FR-46/NFR-5 preserve separate app-owned cleanup, content-free ordinary logs, evidence governance and provider-claim boundaries.
- NFR-3/FR-36–37 preserve whole malformed-reply rejection, whole failed-new-summary withholding, whole-item omission for any persistent invalid reference, reduced usable-set notices/counts and zero-usable error/retry. FR-42 preserves both saved languages, both summary levels and card/quiz sets, truthful demo actions and separate live validation.
- FR-38/40/41 retain incidental-omission continuation with disclosure and stopping on substantial/central or uncertain main-text coverage. The manual protocol retains original-PDF review, five Brief core points, ten Detailed eligible points with at least three additional beyond the core, short-source prespecified alternatives, joint 9/10 or all-if-smaller scoring, original failures/retests and correction/failed-attempt time in evaluation evidence.

No new findings or implementation-cap demands were introduced by this targeted pass.
