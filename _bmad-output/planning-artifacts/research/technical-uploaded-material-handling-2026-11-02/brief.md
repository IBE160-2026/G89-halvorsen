---
type: technical
topic: Uploaded material handling
intent: run
shape: explore
status: approved
created: 2026-11-02
---

# Research brief: Uploaded material handling

**Decision:** What manageable handling of uploaded PDF material should inform the later AI Study Buddy PRD, including local processing, external AI transfer, storage/deletion, privacy and test/demo sharing rights?

User approved the plan on 2026-11-02. Communicate in Norwegian; write research in English. Do not create PRD or edit Product Brief.

## Framing context (not external evidence)

Inputs: Product Brief updated 2026-10-29; its addendum and teacher feedback; PDF source reliability research (2026-10-29); quality/evaluation research (2026-11-02); relevant issues.md items. Brief scope: text-based PDFs, page/filename/excerpt references, external model API, no accounts or sync, no OCR, optional local progress only in phase 2. Gemini is provisional, not selected. T1–T3 and a permissioned shared demo are not selected. Prior research needs saved evaluation outputs; these may reproduce source content and therefore also need a retention/sharing policy. Existing reports are context, never external evidence for this run.

## Approved dimensions and bounds

1. Local PDF processing versus external transfer: distinguish browser, local backend and provider.
2. External AI data terms: Gemini candidate, training/use, retention, regional/account conditions, uploaded files versus inline text.
3. Storage and deletion: original PDF, extracted text, outputs, caches, logs and external copies; modest v1 lifecycle.
4. Privacy and rights: private tests versus API transfer versus demo/repository redistribution; Norwegian/EEA context.

Technical pack pruned to integration patterns and implementation burden. Standard caps: eight sources per dimension per round, at most two rounds; normal validation. Focused breadth-first evidence gathering with two research assistants and a fresh-context semantic checker. Primary regulator/legal and vendor documentation preferred. Web search available through connected search service and harness; no external handoffs/orchestration. Markdown for skill-invoked output. Estimate: 10–15 minutes. Stop on coverage; follow up only material gaps. No enterprise compliance programme, complete legal opinion, model/library selection, app implementation or runtime tests.

## Artifacts and evidence rules

Same shape as previous reports: brief.md, research.md, imports/ (empty unless supplied material), digests/, .memlog.md, quality-check.md, dated-claims.json and staleness.json. Claims trace to source digests, with publisher, URL, publication/update date (undated if absent), access date and confidence. Vendor assertions remain single-publisher supported, not independently verified merely by rereading. Separate documented findings, proposed choices and unresolved decisions. Revalidate living terms at Architecture and before first real upload or wider deployment.
