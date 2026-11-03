# AI security notes — AI Study Buddy

**Reviewed:** 2026-11-03. **Status:** short research supplement; recommendations are not adopted requirements or tested controls.

Scope: a supplement to [PDF reliability](technical-pdf-source-reliability-2026-10-29/research.md), [quality/evaluation](technical-quality-evaluation-2026-11-02/research.md) and [uploaded-material handling](technical-uploaded-material-handling-2026-11-02/research.md). No implementation, model calls or security tests were performed.

## Documented findings

- **Indirect prompt injection:** instructions inside external files can change a model's behaviour. Content need not be visibly readable to affect it if it reaches the model. OWASP describes manipulated answers and unintended actions; impact depends on the model's available capabilities. [1][s1]
- **Defence limits:** separating trusted instructions from source data helps, but wording and delimiters are not an enforcement boundary. Keyword filters can miss attacks and block legitimate content. No prompt-only protection establishes immunity. [1][s1] [2][s2]
- **Improper output handling:** model responses require validation before use by other components. Interpreting generated content as browser code can cause cross-site scripting; executing it as commands creates additional risks. OWASP recommends context-appropriate encoding and validation. [3][s3]
- **Safe display:** OWASP recommends APIs that render data as text and framework escaping. Raw HTML requires a maintained sanitizer; validation alone does not replace safe rendering. [4][s4]

## Implications for this project — assessment

A PDF could request altered quiz answers, a different output language or an external image. These are hypothetical scenarios. Valid JSON or a matching quotation would not establish resistance to manipulation; existing manual correctness/source-support checks remain necessary.

Constrain application capabilities alongside careful prompting. A separate security model or elaborate attack classifier is unnecessary for this scope.

## Candidate PRD requirements — proposals

| Candidate | Recommended behaviour for v1 |
|---|---|
| Treat documents as source data | PDF content must not authorize application actions/settings changes. Keep language and mode under application/user control; instruct the model to analyse document instructions as content. Model compliance needs testing. |
| Display untrusted text safely | Render study aids, filenames and excerpts as text. Do not interpret their HTML/scripts, load their images, fetch their URLs or create clickable model-generated links. Keep application-owned View source controls. |
| Validate before use | Check required fields, types, lengths, answer-key range and application-owned source IDs/pages. Do not show malformed results as a working quiz or valid source. Valid structure does not establish factual correctness. |
| Restrict capabilities and secrets | Give the model no shell, arbitrary file access or URL-fetching tools. Never execute returned code or use it as a file path. Keep API credentials outside prompts, responses and browser-delivered code. |
| Handle failures clearly | Explain invalid responses without exposing raw payloads, secrets or technical traces. Preserve the distinction between an invalid source location and an unmatched quotation; final user behaviour remains a PRD decision. |

Apply these proposals to demo content too. Basis: capability restrictions/validation [1][s1] [3][s3], defence limits [2][s2], and rendering guidance [4][s4].

## Architecture decisions and minimal checks — proposals

Architecture should choose the prompt/message structure, schema validator, safe rendering APIs, input/output limits and bounded retry policy. Prefer plain text fields; any later Markdown support needs a restricted renderer with raw HTML, remote images and unsafe links disabled. Assess Content Security Policy as an additional layer, not a substitute for safe rendering. [3][s3] [4][s4]

Keep four small checks for implementation:

1. Use a synthetic PDF requesting altered answers/language and a benign document discussing such instructions. Record task adherence and false refusals.
2. Supply HTML-like text and an external-image reference in output, filename and excerpt fields: verify inert display and no content-triggered network request.
3. Supply malformed JSON, an invalid answer key and an invented source ID: verify controlled failure without executable/raw payload display.
4. Inspect request construction and rendering code: credentials stay outside model content; responses cannot invoke tools or arbitrary fetches. Use dummy secrets in fixtures.

Passing these checks would cover those cases only, not prove general injection resistance.

## Open questions

- Agree the final response to invalid output: discard the affected item or the entire generated set, and whether to permit one bounded retry.
- Confirm plain text is sufficient for v1, including technical course examples; choose rendering components in Architecture.
- Finalize the small attack/benign fixture set and record results against the selected model and prompt version.

## Sources

Official OWASP guidance, accessed 2026-11-03; not application validation. Recheck component-specific guidance during Architecture.

1. [OWASP LLM01:2025 — Prompt Injection][s1]
2. [OWASP — LLM Prompt Injection Prevention Cheat Sheet][s2]
3. [OWASP LLM05:2025 — Improper Output Handling][s3]
4. [OWASP — Cross Site Scripting Prevention Cheat Sheet][s4]

[s1]: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
[s2]: https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html
[s3]: https://genai.owasp.org/llmrisk/llm052025-improper-output-handling/
[s4]: https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
