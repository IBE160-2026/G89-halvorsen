# Provider terms evidence digest — Gemini Developer API

Acquired 2026-11-02 (client date). Research firewall: only the delegated question and newly retrieved official evidence were used; no other project context was inspected. Provisional candidate only; this digest does not select a provider or establish legal compliance. Connected search service used. Google pages are related vendor assertions, not independent corroboration. Publication metadata below distinguishes effective dates from page update dates.

## Claim records

Each record contains claim, URL, publisher, pub_date, accessed, confidence, and class. Confidence measures support for the narrow statement, not compliance of an eventual app.

### P01 — Service and age boundaries
- claim: These terms govern Developer API/AI Studio; developer professional/business use is specified. Users must be 18+, and API clients must not target or likely be accessed by under-18s. EEA client availability requires Paid Services.
- URL: https://ai.google.dev/gemini-api/terms
- publisher: Google
- pub_date: Effective 2026-03-23
- accessed: 2026-11-02
- confidence: High; explicit use restrictions and age section.
- class: Provider contractual assertion

### P02 — Free, paid, and EEA distinction
- claim: Unpaid use permits product/ML improvement and human review; sensitive/confidential/personal inputs are prohibited there. EEA/Swiss/UK users receive paid data-use terms even on free AI Studio/API quota. API Paid Services require an active-billing Cloud Project; AI Studio also qualifies through project access or Workspace enterprise. These are distinct rules.
- URL: https://ai.google.dev/gemini-api/terms
- publisher: Google
- pub_date: Effective 2026-03-23
- accessed: 2026-11-02
- confidence: High for wording; operational regional qualification remains unresolved.
- class: Provider contractual assertion

### P03 — Paid content and transfers
- claim: Paid prompts/files/responses are excluded from product improvement and processed under Google's processor addendum. Abuse/security/legal logging persists; transient storage/caching can occur in any Google/agent facility country. Other operational/account data has separate controller terms.
- URL: https://ai.google.dev/gemini-api/terms
- publisher: Google
- pub_date: Effective 2026-03-23
- accessed: 2026-11-02
- confidence: High; Paid Services data-use section.
- class: Provider contractual assertion

### P04 — Abuse monitoring is a separate data lifecycle
- claim: Google specifies 55-day retention for prompts, contextual information, and output for policy enforcement, safety/security, and required disclosures. Automated monitoring and authorized employee review of flagged content apply. Logged data is excluded from model training/fine-tuning except models specifically for policy enforcement. Scope covers API and AI Studio.
- URL: https://ai.google.dev/gemini-api/docs/usage-policies
- publisher: Google
- pub_date: Last updated 2026-06-09 UTC
- accessed: 2026-11-02
- confidence: High; explicit retention and investigation sections.
- class: Provider operational assertion

### P05 — Files object retention
- claim: Files API uploads automatically delete after 48 hours; a manual files.delete operation is documented. This statement describes uploaded objects, not every downstream copy or abuse log.
- URL: https://ai.google.dev/gemini-api/docs/files
- publisher: Google
- pub_date: Last updated 2026-10-26 UTC
- accessed: 2026-11-02
- confidence: High for upload deletion; downstream limitation follows from separate lifecycle evidence P04/P06.
- class: Provider operational assertion, with explicit scope limitation

### P06 — Retention varies by feature
- claim: Developer API ZDR documentation retains abuse monitoring and directs guaranteed-ZDR workloads to Vertex AI. Files remain at rest until deletion/expiry independently of logging. Search/Maps grounding stores data for 30 days without a storage opt-out. Interactions state stores by default (store=false disables it); Live resumption can retain state up to 24 hours. Explicit caches have TTL/expiry; implicit cache is project-isolated RAM with 24-hour TTL.
- URL: https://ai.google.dev/gemini-api/docs/zdr
- publisher: Google
- pub_date: Last updated 2026-09-14 UTC
- accessed: 2026-11-02
- confidence: High for documented behavior; not an audit of actual erasure.
- class: Provider operational assertion

### P07 — Developer logs, datasets, and sharing
- claim: Billing-enabled developer logs are separate from abuse logs. Logging defaults ON for Interactions, and Generate Content projects created from 2026-10-26; owners can disable it. Default logs are not used for product improvement; after 55 days by default (configurable 7/14/28/55), they are marked for deletion. Dataset logs have no set retention. Optional dataset sharing permits model improvement/training and human review under unpaid terms; options depend on location. An invite-only Contributor Tier exchanges data-use permission for discounts and also invokes unpaid terms.
- URL: https://ai.google.dev/gemini-api/docs/logs-policy
- publisher: Google
- pub_date: Last updated 2026-10-26 UTC
- accessed: 2026-11-02
- confidence: High for documented defaults; EEA interaction with sharing terms unresolved.
- class: Provider operational assertion

### P08 — Processor addendum location, transfers, and deletion
- claim: Section 10 permits processing wherever Google/subprocessors have facilities, subject to additional transfer terms. Appendix 3A uses a Data Transfer Solution and/or applicable SCC arrangements for restricted European transfers; it states DPF applies to certified Google US entities. Section 6 requires deletion after an irreversible customer deletion request, or at term end, as soon as reasonably practicable, unless applicable law requires storage. Section 7 restricts personnel/subprocessor access to necessary instructions and confidentiality obligations. These are contractual mechanisms, not evidence of a specific request's routing or a completed legal assessment.
- URL: https://business.safety.google/processorterms/
- publisher: Google
- pub_date: Version 10, dated 2026-05-07; contractual effectiveness is acceptance/agreement date, distinct from version date.
- accessed: 2026-11-02
- confidence: High for clauses; no claim about present legal adequacy of a specific transfer.
- class: Provider contractual assertion

### P09 — Norway access availability
- claim: Norway is listed among regions where AI Studio and Gemini API are available. Availability is evidence of service access, not a Norway/EEA processing-location guarantee.
- URL: https://ai.google.dev/gemini-api/docs/available-regions
- publisher: Google
- pub_date: Last updated 2026-10-22 UTC
- accessed: 2026-11-02
- confidence: High for listing; processing-location distinction follows from P03/P08.
- class: Provider availability assertion, with explicit scope limitation

## Practical implications (inferences, not provider/legal facts)

- P02's EEA data-use exception does not erase P01's Paid Services rule for an EEA-facing client. Treat billing/project configuration as an explicit release decision.
- No-product-improvement language alone cannot justify a no-retention or no-human-access promise (P03–P06).
- Sending extracted text inline can avoid creating a Files object; it does not avoid prompt/context abuse retention (P04–P06). This is a lifecycle inference, not a tested deletion guarantee.
- Developer API terms cannot be substituted with consumer Gemini app settings. P01 names the governed services; consumer-app terms were not evaluated.
- P07 means a newly created project needs an explicit logging/sharing configuration review, including datasets. Turning off developer logs does not turn off P04 abuse monitoring. A manual file deletion alone cannot substantiate deletion of all provider data.
- Provisional v1 design recommendation: disable optional developer request/response logging in AI Studio, avoid dataset sharing and Contributor Tier, and record those settings. This reduces a configurable data path (P07); mandatory abuse retention/review still remains (P04), so it supports no blanket zero-retention promise.
- P03/P08 do not establish EEA-only storage/processing. A regional-processing requirement would need a separately evidenced product/contract/configuration path; no such guarantee was found for this Developer API evidence set.
- P01's under-18 restriction is a product-scope gate for a study aid; the intended cohort must be resolved before implementation. This is an implication of provider terms, not an independent legal age rule.

## Contradictions and scope tensions

- P02 extends paid data-use protection to EEA unpaid use; P07 says shared datasets/Contributor Tier invoke unpaid data-use terms and that options depend on location. The retrieved pages do not explicitly reconcile the interaction for EEA accounts. Do not conclude EEA logs are automatically training data, or that every voluntary sharing path is protected. Keep sharing/Contributor Tier out of the provisional handling design until this is resolved.
- P03's product-improvement restriction and P04's security review are different purposes, not contradictory no-human-review promises.
- P05's 48-hour file expiry and P04/P07's 55-day logs address different objects. P06's ZDR page directs guaranteed-ZDR needs to Vertex AI; it does not promise an automatic zero footprint on Developer API.
- P01 requires Paid Services for EEA-facing API clients; P02's free-use data exception concerns how data is used. The distinct clauses should not be flattened into a free production-use permission.

## Leads and unanswered questions

- Operational determination of being "in" the EEA (account entity, billing country, access location, or other signals) is not established by the retrieved terms.
- The actual transfer destinations/subprocessors and necessary transfer assessment for this app remain unverified. DPF/SCC statements here report the contract, not a legal sufficiency determination.
- Full deletion propagation/backups and abuse-log deletion-on-demand behavior are not established; the DPA's reasonable-practicability language does not create a measured erasure SLA.
- AI Studio vs API Paid Services status differs in P02. Verify the actual API project and settings rather than relying on an AI Studio screen alone.
- Vertex AI appears only as Google's lead for guaranteed-ZDR requirements in P06. Its contracts, regions, controls, pricing, and eligibility were not researched; no Vertex recommendation is made.
- Consumer Gemini Apps were deliberately excluded; importing their history toggles/retention numbers into this API design would be unsupported.

## Acquisition and evidence limits

Seven distinct primary official pages were opened; all claims above came from this acquisition. A single targeted follow-up search for EEA/log sharing interaction and Developer API residency yielded forum discussions rather than an authoritative reconciliation; those results were not promoted to provider facts. Search snippets about archive terms and third-party discussions were leads only and were not adopted as current authority. No independent verification or measured API behavior is claimed. Publication/crawl labels in search results were not substituted for displayed effective/update dates. No provider selection, model comparison, or legal-compliance conclusion follows from this digest.
