---
title: 'Technical research: Quality and evaluation'
type: technical
topic: Quality and evaluation
decision: Define manageable evaluation inputs for the later PRD
source: Native web research
status: complete
preset: standard
validation: normal
claims_verified: 1
claims_unverified: 8
created: 2026-11-02
updated: 2026-11-02
---

# Quality and evaluation – AI Study Buddy

## Executive summary

**Recommendation:** use a small, repeatable manual review against the original PDF, supported by deterministic format and reference checks. Review correctness, source support, coverage and usability separately. Keep the Product Brief’s existing test matrix and thresholds as the baseline; the refinements below are proposals for the later PRD, not adopted requirements.

Research distinguishes summary consistency from fluency/relevance and distinguishes answer quality from citation quality. A convincing answer or an existing citation is insufficient evidence of factual support. [3][5] Published automated metrics and LLM judges offer useful signals, but their inspected studies do not validate this application or Bokmål. [4][6]

The feasible IBE160 deliverable is a documented local acceptance check, with saved outputs, item-level judgments, failures and retests. It cannot demonstrate general accuracy or improved learning. No actual PDFs were selected, outputs generated, model calls made or application tests run in this research.

**Next action:** discuss the proposals and select the test material. BMAD’s catalog places `bmad-prd` next in planning when ready; use a fresh context and this report as input, without treating its recommendations as approved requirements.

## 1. Evidence and project boundary

The updated Product Brief, addendum, teacher feedback, theme 1 report and relevant session issues shaped the questions; they are **project context, not external evidence**. See [brief.md](brief.md). Retrieved evidence and limitations are in [digests/](digests/). No imported report was supplied; `imports/` is empty.

**Documented findings** below describe retrieved sources. **Recommendations** are project judgments requiring later decisions. **Open questions** remain unresolved. For ledger purposes, `verified` means independently corroborated, while `unverified` means a cited claim lacks independent corroboration. Single-source methodological claims are medium confidence here even where the extraction digest describes their within-study evidence as high. None is a measured app result.

This bounded review uses historical methodological studies and official guidance, not a current-model leaderboard or an exhaustive literature review. Their age and task/language limitations matter; see §7. No vendor, model, library or evaluation platform is selected.

## 2. Documented findings

| Finding | Evidence and practical limit | Confidence |
|---|---|---|
| F1 — Quality has distinct dimensions. | SummEval separately rates consistency, coherence, fluency and relevance, and reports differences between expert and crowd judgments. Its setting is English news summaries, not course PDFs. Adapt the dimensions; do not transfer its scores. [3] | Medium; single study |
| F2 — Citation support needs its own review. | ALCE separates correctness, fluency and citation quality, including whether cited passages support statements and whether citations are relevant. NIST independently recommends checking sources/citations. This corroborates the general need for citation review, not an app-specific metric. [1][5] | Medium; corroborated, historical |
| F3 — Automation is a proxy with dependencies. | QAFactEval uses question-answering components whose choices affect evaluation. MT-Bench documents position/verbosity biases and reasoning-grading limitations for its tested judges. Neither study establishes current-model or Bokmål accuracy. [4][6] | Medium per study |
| F4 — MCQ structure can be reviewed explicitly. | NBME advises a focused question, one best answer, plausible comparable options and review for unintended clues/ambiguity. These principles come from health-sciences examinations; applying them to IT subjects is a proposed transfer. [7] | Medium; professional guidance |
| F5 — Retrieval and feedback have bounded experimental support. | A prose-learning experiment found delayed benefits from retrieval practice; a separate MCQ study’s abstract reports feedback improving later recall and reducing distractor intrusions. Neither validates AI-generated study aids or proves this app improves learning. [8][9] | Medium per study |
| F6 — Small local checks warrant modest conclusions. | NIST warns against extrapolating from narrow assessments. Its statistics handbook describes uncertainty in small-sample proportions. Ten convenience-selected items are a local check, not a population accuracy estimate. [1][2] | Medium; same-publisher guidance, historical |

**Cross-dimension implication:** source-faithful output may omit key topics, while a well-written question may have an incorrect key. A single overall quality score can hide these failures. Use separate recorded judgments and inspect the same item’s answer and references together. This is the project’s proposed application of F1–F4.

## 3. Proposed manual rubric

These are manageable review rules, **not validated scales or new requirements**. Use `Pass`, `Fail` or `Unclear`, with an exact failure example and source page. `Unclear` never counts as a pass; resolve it or report the case as inconclusive. Do not average away a wrong answer with a high readability score.

For each factual statement, check meaning against the original visible PDF, using extracted text only as an aid. Check definitions, numbers, negation, conditions, exceptions and technical terms. A sentence with multiple factual claims passes only if all are supported and correct within the course context. If the original is ambiguous or appears wrong, record a source-content issue and seek clarification rather than silently trusting or correcting it. Source faithfulness alone does not establish truth beyond the course material.

| Artifact | Proposed checks | Recorded result |
|---|---|---|
| Summary | Review every factual statement; mark unsupported additions and contradictions. Check understandable language, logical organization, relevant content and repetitions. Detailed examples must come from or be justified by the source. | Correct/supported claims ÷ all factual claims; missed key points; language/level pass or fail; unresolved claims. |
| Flashcard | Front asks a bounded, understandable recall question; back answers it accurately and sufficiently. No hidden dependency on another card, misleading simplification or duplicate question. | Separate answer-correctness, clarity/usefulness and source-support judgments. |
| MCQ | Read the stem before options; assess each option in its stated context. Exactly one defensible keyed answer, plausible alternatives, no accidental clues, duplicate options or ambiguity. Review explanation against source. | Correct/unambiguous key, item-design quality, feedback correctness and source support separately. |
| Both languages | Check selected language and meaning, especially technical terms, negation, units and qualifiers. A correct English item does not establish a correct Bokmål translation. Original-language quotations remain unchanged. | Language/meaning result for each language, plus concrete translation defects. |

**Summary coverage proposal:** before viewing generated output, write five key points per PDF for Brief and ten for Detailed, each mapped to pages. Reuse these lists across languages; Detailed includes the five core points. Count a point only when correctly represented. Propose all five core points for Brief, all five core points plus at least three additional points for Detailed. These counts/thresholds are project choices, not research findings. Pilot them on T1 first; short sources may not contain ten distinct points. In that case define the smaller eligible list and its required subset before scoring. Keep both versions different in depth without padding or invented examples. Final counts and level criteria remain PRD decisions.

**Reference proposal:** record four separate checks: (a) existing document/page, (b) quotation occurrence on that page, (c) semantic support for the associated statement/answer, and (d) whether all factual parts needing support have a reference. A matching but irrelevant passage fails (c). A correct answer supported elsewhere still fails its cited support check. A factual claim with no citation fails coverage (d), rather than disappearing from the denominator. Preserve theme 1’s distinction between invalid location and unmatched quotation; application behavior for these states remains open.

## 4. Proposed test protocol and measurable criteria

The current brief already plans **12 summary cases**, **six flashcard cases** and **six quiz cases**: T1–T3 × two languages, with two detail levels only for summaries. These 24 generated sets are not 24 independent estimates of model accuracy.

**Workload control:** reuse the same selected card/question for correctness, usefulness and reference review. Twelve complete summary reviews plus up to 60 cards and 60 questions form the core proposed content workload; references and feedback are additional checks on those outputs, not necessarily extra generation. Pilot one T1 case to measure actual effort before committing to optional repeats or a second reviewer. A second competent reader checking a small subset is useful if available, not a new requirement for the solo project. Without one, disclose single-reviewer subjectivity and recheck unclear cases after a break.

### Protocol

1. Select permissioned T1–T3 PDFs and inspect their visible content and extraction quality. Prepare key-point lists before scoring. Keep a small failure fixture set separate from normal-content acceptance cases.
2. Save the first complete output of each planned case, with timestamp, document/version identifier, model identifier, prompt version, settings and output. Record failed generation attempts; do not silently replace them with a better run.
3. Review all 12 summaries for factual claims, coverage and selected level. For references use a separate sample for each summary level, avoiding a good level masking a bad one.
4. For flashcards and quizzes, select up to ten items per case **before assessing their quality**. Proposed repeatable rule: if more than ten, use a seeded random sample of ten and save the seed and item IDs; if ten or fewer, review all. Use those same items for answer and reference checks. Add targeted edge examples separately; do not substitute them into the acceptance sample after seeing failures.
5. For references, select one associated reference for each sampled item/summary claim using a recorded rule (first reference, or seeded selection if several). Judge the selected reference for relevance and support of its attributed content. Separately judge whether all attached references collectively support the whole claim; report reference-level and claim-level results separately. With fewer than ten eligible references, inspect all. Missing references remain coverage failures. Check **every displayed location** for existence, beyond the sample.
6. Record original scores, defects, corrections and retests. A corrected saved demo output is not evidence that live generation was fixed. After a prompt/model change, regenerate the affected cases and check the fixed regression examples; a final matrix run gives the acceptance snapshot. Do not run every case repeatedly without a reason.

### Acceptance criteria

| Criterion | Baseline from Product Brief | Proposed clarification for PRD |
|---|---|---|
| Summary accuracy/level | Manual factual review of all 12; selected detail level. | No unresolved factual error or unsupported factual addition in a passing summary; coverage/level checklist above. This is a proposed threshold. |
| Flashcards | At least 9/10 correct answers per case; if the case contains fewer than ten items, all must pass. | Keep correctness count; record clarity and support on the same item. |
| Quiz | At least 9/10 correct, unambiguous keys per case; if the case contains fewer than ten items, all must pass. | Another defensible answer is a key failure, even if the intended key is correct. |
| References | At least 9/10 relevant, supporting references per type/document/language; existing locations for all. | Separate occurrence from semantic support and missing-citation coverage; evaluate summary levels separately. |
| Paired quality | Joint answer/reference passing is still open. | Report `both pass ÷ same reviewed items` alongside separate scores. Example: if the answer failure and citation failure affect different items, each separate score can be 9/10 while only 8/10 items pass both checks. A joint release threshold needs approval. |
| Incorrect-answer feedback | Every tested wrong answer shows key, explanation and reference. | For every reviewed quiz item, try a wrong option; explanation must be understandable, correct and supported. |
| Language | All study aids follow selected language. | Review meaning in both languages; do not flag original-language quotations as failures. |

**Interpretation:** preserve per-case numerators/denominators; do not pool languages or PDFs to conceal a failing case. The brief’s thresholds are project acceptance targets, not scientifically established reliability standards. Record and correct known errors even when a 9/10 target is met. If a reviewer cannot resolve a technical claim, obtain help or use material they can assess; do not guess.



## 5. Automation, negative tests and retained evidence

**Automate simple rules:** required fields, valid answer-key index, duplicate options, known source ID, physical page range and theme 1’s page-local excerpt occurrence. These establish structure/location, not factual meaning. Selected language and semantic equivalence still need review. No new evaluation service or learned metric is needed for v1.

Proposed small regression examples (not yet implemented):

- Matching quotation with a reversed negation or changed number in the answer: occurrence passes, correctness/support fail.
- Correct quote on the wrong physical page, nonexistent document/page, empty quote and missing reference: the appropriate structural/coverage check fails; no false successful status.
- Two defensible MCQ answers, duplicate options, or a mismatched key: quiz check fails.
- Fluent but incorrect translation, or Detailed summary adding an unsupported example: manual review fails.
- A key topic omitted from a fluent summary: coverage fails independently of correctness.

Keep an item log with `case ID, output/item ID, mode (live/demo), settings/prompt/model version, source page(s), correctness, location, excerpt result, semantic support, coverage, language/usefulness, defect, fix, retest`. Record inspection date and reviewer. A Markdown table is sufficient. This research does not create a populated test log or claim that these tests pass.

Evaluate saved demo material with the same content rubric; test its workflow without an API key separately. Report live API integration results separately. For practical value, later time a comparable manual and app-assisted preparation task including review/correction time; disclose task familiarity and order effects. Usefulness ratings and time savings do not prove learning gains.

## 6. Limitations and open decisions

**Contrary evidence and limits:** the judge study found useful human-preference agreement as well as biases, so automated judging is not inherently useless. [6] QAFactEval provides evidence for specialized factuality methods in its benchmarks. [4] They remain optional later aids because their local language/task validation adds work. No dedicated red-team pass was run (normal validation); these counterpoints came from the acquisition sources. Human review is also fallible, as SummEval’s annotator differences show. [3]

Before PRD acceptance tests are finalized:

- Which actual T1–T3 documents and key-point lists are fair and feasible? Run a small pilot; resolve coverage counts and summary-level rules from it.
- Should correctness and source support require a joint 9/10, or only separate thresholds? Review the paired-score example and agree explicitly.
- What citation granularity and missing-citation policy should the UI support, especially for multi-claim summaries and multi-page support? Define claim/reference denominators consistently before implementation.
- What should users see when a reference is invalid versus when an excerpt cannot be found? Carry forward theme 1; this report does not settle fallback behavior.
- Can one reviewer reliably assess both languages and the selected technical concepts? Record uncertain cases and seek a competent second reader where necessary.
- How much generation variability appears locally? One saved run per case cannot answer this. If instability appears in the pilot, repeat the affected case and preserve both runs; wider reliability/learning-effectiveness studies stay outside v1.

These refine existing open items rather than closing them: documents, acceptance policy and actual tests are still pending. Product Brief/addendum remain unchanged.

## 7. Sources and freshness

All sources accessed **2026-11-02**. Source-specific statements are medium confidence unless a general principle is independently corroborated above. Older papers establish what their studies reported, not what current models achieve. The original MCQ feedback study was inspected through its primary abstract only. Dates are publication dates or explicitly identified document dates, not inferred from URL paths.

| Ref | Supports | Publisher and primary source | Published/document date | Accessed | Confidence |
|---|---|---|---|---|---|
| [1] | Citation checking; narrow-test limitations | [NIST — Generative AI Profile, AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf) | 2024-07 (released 2024-07-26) | 2026-11-02 | Medium individually |
| [2] | Small-sample proportion uncertainty | [NIST/SEMATECH — Confidence intervals](https://itl.nist.gov/div898/handbook/prc/section2/prc241.htm) | Undated living page | 2026-11-02 | Medium |
| [3] | Summary dimensions; reviewer differences | [MIT Press / TACL — SummEval](https://aclanthology.org/2021.tacl-1.24/) | 2021-04 | 2026-11-02 | Medium |
| [4] | QA-based factuality metrics and dependencies | [ACL / NAACL — QAFactEval](https://aclanthology.org/2022.naacl-main.187/) | 2022-07 | 2026-11-02 | Medium |
| [5] | Correctness versus citation support | [ACL / EMNLP — Enabling LLMs to Generate Text with Citations (ALCE)](https://aclanthology.org/2023.emnlp-main.398/) | 2023-12 | 2026-11-02 | Medium individually |
| [6] | Useful preference judging and limitations | [NeurIPS — Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://papers.neurips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html) | 2023 proceedings | 2026-11-02 | Medium |
| [7] | Single-best-answer item-writing principles | [NBME — Item-Writing Guide](https://www.nbme.org/sites/default/files/2021-02/NBME_Item%20Writing%20Guide_R_6.pdf) | Cover: 2024-10; preface: 2020-08 | 2026-11-02 | Medium; cross-domain transfer proposed |
| [8] | Bounded retrieval-practice rationale | [Psychological Science — Roediger & Karpicke, Test-Enhanced Learning (author-hosted original)](https://learninglab.psych.purdue.edu/downloads/2006/2006_Roediger_Karpicke_PsychSci.pdf) | 2006-03 | 2026-11-02 | Medium |
| [9] | Corrective MCQ feedback experiment | [Memory & Cognition — Butler & Roediger (primary abstract, PubMed)](https://pubmed.ncbi.nlm.nih.gov/18491500/) | 2008-04 | 2026-11-02 | Medium; abstract only |

**Staleness map:** [dated-claims.json](dated-claims.json) and helper-generated [staleness.json](staleness.json) apply the technical pack’s 24-month patterns window to dated methodological evidence. Old studies are explicitly historical; an expired window does not overturn an experiment, but prevents treating it as current capability evidence. Undated statistical guidance is excluded from publication-date arithmetic, not assigned an invented date. No pricing, version, performance or compatibility claim is made.

The earliest computed recheck is **2008-03-01**, already past; all eight dated entries exceed the window as of this run. This signals that they must remain historical evidence, not a future deadline or proof that they are false. Exact dates and final citation/ledger checks are recorded in [quality-check.md](quality-check.md). Revisit the age-flagged evidence before adopting an automated metric/judge, and update the local evaluation pack whenever the selected model, prompt or extraction behavior changes. Refresh/Deepen can extend this run later.
