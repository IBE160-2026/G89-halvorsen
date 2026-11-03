---
title: Input reconciliation — AI security notes
created: 2026-11-03
status: reconciled-with-follow-up
input: ../../research/ai-security-notes.md
---

# AI security notes reconciliation

Reviewed the [AI security notes](../../research/ai-security-notes.md) against the current [PRD](prd.md), [addendum](addendum.md) and latest chronological decisions in [.memlog.md](.memlog.md). The user approved the four proposed v1 security outcomes; the source's original proposal status therefore no longer means those outcomes are unadopted. Detailed mechanisms and negative-test results remain future work.

## Evidence and interpretation boundary

The source is an OWASP-based research supplement reviewed on 2026-11-03. No implementation, model calls or security tests were performed. Its documented findings are that untrusted files can carry indirect instructions, model output needs validation and safe rendering, and wording/delimiters alone do not form an enforcement boundary. Valid JSON and a matching quotation cannot demonstrate resistance to manipulation.

The approved requirements must be implemented as application boundaries and tested on the selected components. They do not establish general prompt-injection immunity. A passed synthetic test demonstrates the tested case only. Manual answer-correctness and source-support evaluation remains necessary even when structure and source locations pass validation.

## Adopted outcome coverage

| Source concern | PRD coverage | Reconciliation |
| --- | --- | --- |
| External PDF/model instructions must not authorize app changes | NFR-1; FR-4; FR-5; session/replacement requirements | Adopted. Uploaded and generated material is study data. User/application controls govern language, mode, settings and actions; model text cannot authorize changing them. Prompt/message layout is an implementation choice. |
| Safe handling of study aids, filenames and source excerpts | NFR-2; FR-6; FR-11; FR-12 | Adopted. Display must remain inert: no HTML/script execution, automatically loaded remote images or content-triggered external requests. Safe headings/emphasis/lists can support the agreed summary structure. Rendering components are Architecture-owned. |
| Application-owned View source controls | FR-11; FR-12; NFR-3 | Covered. Source controls inspect the accepted PDF's source records. Generated text does not obtain tool authority merely by containing a URL or instructions. |
| Required fields, types, lengths, quiz options/key and source locations | NFR-3; FR-8; FR-24; FR-36 | Adopted. Malformed output cannot become a working-looking study aid or valid-looking citation. Exact schemas and bounds must be selected and verified downstream. |
| Controlled failure with prior valid state preserved | NFR-3; FR-23; FR-36; FR-37 | Adopted. Failed generation/recovery preserves existing valid content and progress. Persistent source-invalid card/question handling is already resolved: omit invalid items, deliver a usable subset with a notice, or show an error for zero usable items. Non-source structural failure granularity remains open below. |
| Restricted capabilities | NFR-1 | Adopted. The model has no shell, arbitrary-file or URL-fetch tools. Returned code or file/URL text does not authorize execution or access. Actual request/tool configuration is Architecture and implementation work. |
| Secrets outside model and browser exposure | NFR-4 | Adopted. Private credentials stay outside model/PDF content, browser-delivered code and exposed errors/payloads. Provider and credential-handling implementation are unselected. |
| Safe handling of saved demo aids | NFR-4; FR-42; SM-5 | Adopted. Saved content uses the same content/rendering boundaries. A labelled key-free demo and live integration are validated separately. |
| Factual manipulation despite valid structure | FR-34; SM-2–SM-4; manual evaluation protocol | Covered. Source occurrence does not prove semantic support or answer correctness. Joint answer/support review, original defects and retests remain part of the approved evaluation. |

## Source proposals retained as implementation candidates

The following are not additional silently adopted product requirements:

- Prompt/message structure, explicit separation and model instructions should support the approved boundary, but their wording is not itself an enforcement guarantee.
- Architecture chooses the schema validator, restricted rendering APIs, input/output limits and finite recovery policy. Plain text is a candidate; safe formatted headings, lists and emphasis are already compatible with NFR-2 and FR-6. No specific framework, Markdown package or sanitizer is selected.
- If a renderer supports Markdown, disabling raw HTML, remote images and unsafe links is a candidate means of satisfying NFR-2. The source's blanket suggestion against clickable model-generated links is stricter implementation guidance, not a separately approved user requirement. It must not be confused with permission for automatic external requests.
- Content Security Policy may add protection but cannot replace inert rendering or validation. No security model, attack classifier or keyword filter is required for v1.
- Exact bounded retry counts are downstream choices. The source's suggestion of one retry does not select that number.

## Remaining product ambiguity

**Non-source malformed-output recovery unit:** NFR-3 requires rejection and a controlled error, but does not specify whether an otherwise parseable set with one structurally malformed card/question (for example, five quiz options or an out-of-range answer key) is rejected in full or can deliver the structurally valid subset. FR-37 explicitly resolves source-invalid items only. Clarify the boundary between an unusable top-level response and an invalid independently identifiable item; do not silently extend source filtering or assume all-or-nothing behaviour. Any failed replacement must preserve the old valid set/progress, and retries must remain finite if offered.

The summary source-failure unit and mixed-validity references are shared source-recovery ambiguities already recorded in [the PDF reliability reconciliation](reconcile-pdf-reliability.md), not new security decisions. No other product requirement gap was found in this supplement.

## Future checks and ownership

Architecture/development owns the mechanisms and small negative fixtures before release evidence is claimed. The source proposes four useful checks:

1. A synthetic PDF asking for altered answers/language and a benign PDF discussing similar instructions: record task adherence and false refusals for the selected model/prompt version.
2. HTML-like text and external-image references in output, filename and excerpt fields: verify inert rendering and no content-triggered network requests.
3. Malformed JSON, invalid answer keys and invented source IDs: verify the chosen controlled rejection/recovery boundary without executable/raw payload presentation.
4. Request construction and renderer inspection with dummy secrets: verify credentials remain outside model content and output cannot invoke tools or arbitrary fetches.

These checks are proposals for implementation evidence, not completed tests. Recheck component-specific official guidance when the stack and renderer are chosen. Passing cases must not be described as proof of general injection resistance or as a substitute for factual evaluation.
