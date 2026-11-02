# Privacy framing — round 1

Accessed 2026-11-02. Norwegian regulator guidance; no personal-data processing by the application inspected. No assertion that an IBE160 project has a blanket GDPR exemption or that it necessarily requires a DPIA.

| ID | Claim | URL / publisher | Published/updated | Confidence / class |
|---|---|---|---|---|
| P1 | Personal information includes direct and indirect identification, including names and identifying email addresses. | https://www.datatilsynet.no/rettigheter-og-plikter/personopplysninger/ — Datatilsynet | 2025-03-31 | Medium, authoritative single publisher; regulatory |
| P2 | Processing needs a legal basis and transparency; personal data should be limited to what the purpose requires, and deleted/anonymised once no longer needed. | https://www.datatilsynet.no/rettigheter-og-plikter/personvernprinsippene/ — Datatilsynet | 2023-07-27 | Medium, authoritative single publisher; regulatory |
| P3 | Transfers outside the EEA require a valid transfer basis; processing within the EEA still requires a processing basis. | https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/overforing-av-personopplysninger-ut-av-eos/ — Datatilsynet | 2026-01-29 | Medium, authoritative single publisher; regulatory |
| P4 | OWASP logging guidance advises excluding or sanitising secrets and sensitive data, treating names/paths specially, and considering logs/copies/backups in retention. | https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html — OWASP | Undated | Medium, single publisher; security-patterns |

## Implications (project recommendations, not legal clearance)

No login does not establish absence of personal data: a PDF may have author/lecturer/student identifiers or personal case examples, and technical metadata/logs need separate attention. Prefer intentionally authored, non-sensitive, permissioned fixtures for the prototype. Inspect/remove unnecessary identifiers manually before sending; an upload acknowledgement is information/permission confirmation, not blanket GDPR consent for people mentioned in a PDF. Removing a name alone does not establish anonymous data.

Before real personal data or broader hosted use, resolve who is controller/processor, applicable processing basis, notices, contract and transfer conditions with institutional support. Do not prescribe an enterprise programme for v1; choose constrained test material and document boundaries. Copyright permission and privacy basis answer different questions.

## Retrieval limits and verification

Direct EUR-Lex ELI and CELEX HTML versions returned robot challenges; direct Lovdata GDPR articles 2 and 5 returned 405/inaccessible. They are not cited as inspected evidence. No independent-publisher corroboration achieved for regulatory assertions; regulator guidance is sourced but ledger status remains unverified under BMAD independent-publisher definition. This does not mean unsupported. Datatilsynet articles have old displayed dates but were retrieved now; recheck legal guidance before actual data transfer rather than treating age as a new publication. Stop at coverage within normal validation; specific project's legal roles/exception unresolved.

## Final semantic qualification

The fresh-context pass found the regulator's express personal-sender scope qualification. Final report and ledger therefore say “where GDPR transfer rules apply”; this establishes no exemption for this project or other people's data. See semantic-check.md.
