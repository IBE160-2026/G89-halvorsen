# Internal v1 reliability scenario mapping

These 17 manually supplied scenarios are a UX test matrix. They are not 17 product screens. The selector sits outside the product frame and loads fresh, separate sample data; it is not a student feature. Technical reason codes appear only in internal JavaScript and this mapping.

**Current policy alignment — 26 November 2026:** The user approved revised FR-40/FR-41. Readable, source-verifiable text remains usable despite uninterpretable images, figures or tables, with evidence-based nonblocking notices. Stop only for insufficient usable text or concrete retained-main-text unreliability, alongside detected file errors. Unknown full-PDF coverage, generic parser warnings and plain/layout differences alone do not reject the PDF. The IDs below are retained for traceability; legacy reason-code names do not define current product policy. Existing prototype JavaScript/copy and its original 17-case classification of 13 errors, three notices and one information state are unchanged prior-scope evidence. The current expected outcomes below supersede those old conditions; no prototype tests have been rerun for this amendment.

Four reusable outcome patterns share the selected status/notice geometry:

- **Blocking document error:** stop for detected file errors, insufficient usable text or concrete unusable/unreliable retained main text; explain the problem and recover with New session or applicable manual extraction retry.
- **Retryable generation error:** name the failed learning function, give a short reason, retain the valid active session, and offer Try again when it can help. Missing live setup uses this same presentation with Go to Summary instead of a retry that cannot work.
- **Usable content notice:** keep accepted content available with an actual item count or a known omission. Do not repair, reconstruct or refill automatically.
- **Demo info:** identify saved study material and the boundary to live generation.

The existing **pending** pattern is separate. Manual retry starts the named pending operation. No time estimate, progress percentage, automatic completion, API call, PDF analysis, OCR or persistence is simulated.

| External fixture ID | Internal reason code | Pattern | Supplied condition and publication rule | Retained valid data / recovery |
|---|---|---|---|---|
| `unsupported` | `unsupported_file_type` | Blocking document error | Selected format is not PDF; publish nothing. | New session, select PDF. |
| `damaged` | `pdf_open_failed` | Blocking document error | Parser cannot open supplied PDF; publish nothing. No repair. | New session, another PDF. |
| `no-text` | `no_usable_extracted_text` | Blocking document error | No usable extracted text supplied; publish nothing. This does not identify scans or every cause of extraction failure. | New session, PDF with readable text. |
| `material-loss` | `material_extraction_loss` (legacy ID) | Blocking document error only for the revised condition | Concrete extraction failure makes retained main text unusable or its meaning unreliable, or insufficient usable text remains. Missing graphical/table content alone does not satisfy this blocking condition. | Applicable manual extraction retry or New session. The preserved prototype's broader omission trigger is prior-scope only. |
| `uncertain-extraction` | `extraction_coverage_uncertain` (legacy ID) | Usable content notice when there is observable omission evidence | Readable, source-verifiable text remains; the supplied evidence identifies an uninterpreted graphical/table limitation. Unknown full-PDF coverage alone is not a rejection reason and does not justify inventing a specific omitted part. | Generate from usable text with a short evidence-based notice/pages where known. The preserved prototype still illustrates the former blocking condition; implement the revised FR-40/FR-41 outcome. |
| `incidental-omission` | `known_nonessential_omission` (legacy ID) | Usable content notice | Supplied fixture identifies an unreadable figure on physical page 4 while readable, source-verifiable text remains. Generate from available text without reconstructing the figure; proving that every omitted figure is incidental is not an additional gate. | Summary remains available with one short notice naming only the known limitation. |
| `reduced-flashcards` | `flashcards_source_filtered_subset` | Usable content notice | Structurally valid output has whole items removed after source-location rejection; accept the remaining 3 whole cards. | Summary + 3 cards; actual counter, previous/next and restart. No refill. |
| `reduced-quiz` | `quiz_source_filtered_subset` | Usable content notice | Structurally valid output has whole questions removed after source-location rejection; accept the remaining 1 whole question. | Summary + 1 question; score denominator is 1. No refill. |
| `zero-flashcards` | `flashcards_source_filter_empty` | Retryable generation error | Source-location filtering leaves zero whole cards; reject the new set. | Summary + existing Quiz, with second answer selected and unconfirmed. Manual Flashcards retry. |
| `zero-quiz` | `quiz_source_filter_empty` | Retryable generation error | Source-location filtering leaves zero whole questions; reject the new quiz and publish no score for it. | Summary + existing Flashcards at Card 2. Manual Quiz retry. |
| `invalid-flashcards` | `flashcards_schema_invalid` | Retryable generation error | New response is structurally invalid; reject the whole response. Do not salvage fields or repair it automatically. | Summary + existing Quiz, second answer selected and unconfirmed. Manual Flashcards retry. |
| `invalid-quiz` | `quiz_schema_invalid` | Retryable generation error | New response is structurally invalid; reject the whole response and publish no quiz score. | Summary + existing Flashcards at Card 2. Manual Quiz retry. |
| `invalid-summary` | `summary_source_match_failed` | Retryable generation error | At least one Summary source-location check fails; reject the whole new Summary. No previous Summary is supplied in this fixture. | Nothing new becomes available; manual Summary retry or New session. |
| `saved-demo` | `saved_demo_live_boundary` | Demo info | Prewritten material is supplied without live generation; identify the live boundary. | Summary, Flashcards and Quiz usable without private keys or paid accounts. Synthetic PDF is not a final demo asset. |
| `missing-setup` | `live_setup_missing` | Retryable generation error | Live generation is unavailable because setup is incomplete; stop. Do not show students a provider/key form or a retry that cannot fix setup. | Summary + existing Quiz, second answer selected and unconfirmed; Go to Summary. |
| `service-unavailable` | `generation_service_unavailable` | Retryable generation error | Service failure supplies no accepted Flashcards response. | Summary + existing Quiz, second answer selected and unconfirmed. Manual retry. |
| `timeout` | `generation_timeout` | Retryable generation error | Request takes too long; stop and withhold the new Quiz. | Summary + existing Flashcards at Card 2. Manual retry. |

The reduced-set and whole-response cases have different publication rules, even though they reuse only two message patterns. Source-location matching is not proof that an answer is factually supported or correct. The notices make no verified-quality or reliable-extraction guarantee.

The extraction conditions and known omission are supplied test signals. This prototype does not discover or classify them. Current implementation must distinguish insufficient/unreliable retained text from graphical/table omissions that leave usable text. Observable stop criteria, evidence-based notices, parser behaviour and source matching remain Architecture decisions; there is no universal PDF detector, OCR path or invented threshold here. Accuracy/source rules and 9/10/all-smaller-set thresholds are unchanged; original-PDF readable-text evaluation and visual omissions are recorded separately. The revised PRD/addendum remain authoritative.

## Preserved state-preservation review — prior prototype scope

Useful selectors are stable across generated IDs:

- `[data-reliability-scenario]` selects one of the 17 fixtures outside `.app-frame`; groups are Errors, Warnings and Demo.
- `[data-status-view][data-reliability-pattern]` identifies the shared document/generation/pending presentation. The pattern is a UI contract, not a reason code.
- `[data-reliability-notice][data-reliability-pattern]` identifies usable-content or demo notices.
- `[data-preview="summary"]`, `[data-preview="flashcards"]` and `[data-preview="quiz"]` are product navigation.
- `[data-reliability-retry]` starts the failed operation. `[data-status-pending]` then remains visible until another fixture is explicitly loaded or the session ends.

Expected proof:

1. For `zero-flashcards`, `invalid-flashcards` and `service-unavailable`, open Quiz. Radio `value="1"` is already selected, while `[data-feedback]` is hidden and Confirm answer is enabled. Change the selection, visit Summary/Flashcards, retry Flashcards, and return to Quiz: the new selection is preserved. Confirming an answer before retry also preserves its locked feedback afterward. `missing-setup` preserves the same Quiz state and shows no retry.
2. For `zero-quiz`, `invalid-quiz` and `timeout`, open Flashcards. `[data-card-count]` starts at Card 2 of 3. Move to Card 3, visit Summary/Quiz, retry Quiz, then return to Flashcards: Card 3 remains selected and its answer is hidden on function return. No new Quiz or score appears.
3. Summary text remains the same through these visits and retries. Retry does not change any ready flag or reset card/answer values. Pending generation never marks the requested output ready and never overwrites existing valid content.
4. Reduced Flashcards really has 3 navigable cards; reduced Quiz really has 1 question and a result out of 1. Restart repeats the same accepted set. It never generates replacements.
5. New session → Cancel retains the active session. Confirming New session removes the session and disables the review selector; old content cannot return through navigation. Reload is required to load another test fixture after ending the session.

These checks establish presentation/state behaviour for their recorded prototype version only. They do not validate the revised 26 November PDF policy, real PDFs, detector accuracy, generated educational quality or production request/session handling. No new browser or regression execution is claimed here.
