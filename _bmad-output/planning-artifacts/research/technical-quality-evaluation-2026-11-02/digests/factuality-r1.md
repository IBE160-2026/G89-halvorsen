# Factuality and citation evaluation — primary-evidence digest

Research date/accessed: 2026-11-02. Research firewall: no project files read. Decision context informed questions only. Four original papers inspected through publisher pages and PDFs; five web calls. Findings concern published evaluation settings, not this app's measured quality.

## Evidence

### F1 — Separate source consistency from writing quality and relevance

- **Claim:** SummEval evaluates consistency (claims entailed by the source), coherence, sentence fluency, and relevance separately. It collected source-visible ratings and found meaningful disagreement between expert and crowd judgments; a second expert annotation round improved agreement. A human rubric therefore needs explicit dimensions, examples, and disagreement review rather than an undifferentiated impression of quality.
- **Source:** [SummEval: Re-evaluating Summarization Evaluation](https://aclanthology.org/2021.tacl-1.24/), original PDF sections 4.3–5.1.
- **Publisher/date:** MIT Press, TACL 9; April 2021 (PDF publication statement). **Accessed:** 2026-11-02.
- **Confidence/class:** High; peer-reviewed empirical study, with the final rubric implication an inference.
- **Scope/limitations:** English CNN/DailyMail news summaries from earlier neural systems; evidence does not establish performance for educational PDFs or Bokmål. Its ROUGE comparisons are correlations in that setting, not a guarantee that lexical overlap establishes an individual output's source support. Human references can themselves contain extraneous material, so reference overlap should not replace checking the actual PDF.

### F2 — Automated factuality metrics add model dependencies

- **Claim:** QAFactEval checks whether source-based answers agree with answers selected from a summary; it reports that question generation and answerability classification materially affect metric performance. QA and entailment methods supplied complementary signals. Choosing a named factuality metric does not remove the need to validate its components locally.
- **Source:** [QAFactEval: Improved QA-Based Factual Consistency Evaluation for Summarization](https://aclanthology.org/2022.naacl-main.187/), sections 1 and method overview.
- **Publisher/date:** Association for Computational Linguistics, NAACL; July 2022. **Accessed:** 2026-11-02.
- **Confidence/class:** High; peer-reviewed empirical study; local-validation recommendation is inference.
- **Scope/limitations:** Summarization factual-consistency benchmarks; not evidence for Norwegian course material, MCQ pedagogy, PDF extraction, or this app. The QA method requires multiple learned components and is consequently a greater implementation burden than a small manual audit. This burden assessment is engineering inference, not a measured cost comparison in the paper.

### F3 — Citation presence and citation support are different checks

- **Claim:** ALCE distinguishes correctness, fluency, and citation quality. Citation recall asks whether a statement is fully supported by its cited passages; citation precision identifies irrelevant citations. Human evaluation checks full/partial/no support. Its automatic citation evaluation uses an NLI model and is limited by that model, including partial-support errors. A page number existing is thus an insufficient support test.
- **Source:** [Enabling Large Language Models to Generate Text with Citations](https://aclanthology.org/2023.emnlp-main.398/), sections 3.3, 6, limitations, Appendix F.
- **Publisher/date:** Association for Computational Linguistics, EMNLP; December 2023. **Accessed:** 2026-11-02.
- **Confidence/class:** High; peer-reviewed benchmark/method study; page-number implication is inference.
- **Scope/limitations:** Open-domain answers using retrieved passages, not uploaded teaching PDFs. Adapt its distinction, not its reported scores, to the app. “Recall” here means support coverage of generated statements, not coverage of every important source topic. Checking that a summary includes key teaching points needs a separate relevance/coverage rubric.

### F4 — LLM judges can assist, but preference agreement is not source verification

- **Claim:** The MT-Bench/Chatbot Arena study finds strong human-preference agreement in its experiments while documenting position bias, verbosity bias, and grading failures on reasoning. It proposes swapping answer order for pairwise evaluation and treating inconsistent preferences conservatively. The paper explicitly says its small study cannot determine whether models exhibit self-enhancement bias; do not report that as conclusively established here.
- **Source:** [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://papers.neurips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html), sections 3–4.
- **Publisher/date:** NeurIPS proceedings, 2023; inspected PDF revision dated 2023-12-24. **Accessed:** 2026-11-02.
- **Confidence/class:** High; peer-reviewed empirical study.
- **Scope/limitations:** Particular 2023 judges and chatbot-preference tasks; no validated claim about current models, Bokmål, or PDF fidelity. Agreement with preferences cannot be interpreted as factual accuracy for this application. An LLM judge should receive source passages and a narrow rubric, and its verdicts need comparison against local human labels; that is a proposed application, not a validated result from this paper.

## Manageable evaluation proposal (engineering recommendation, not established empirical result)

Use a small, fixed evaluation pack of permissioned course PDFs, with English and Bokmål represented separately. Save the PDF/page text, generated item, settings and model identifier. Select examples across document lengths and layouts, including extraction failures; report the tested sample and language split explicitly. Do not infer population accuracy from this convenience sample.

For each sampled summary, flashcard, or MCQ, inspect the original page and record:

1. **Source support:** supported / partially supported / unsupported / contradicted / cannot assess because extraction or source is unclear. Record the claim and supporting page or offending text.
2. **Citation:** target exists and resolves to the intended PDF page; cited text actually supports the claim; identify claims missing support.
3. **Useful content:** important concepts covered, relevant to the requested topic, and understandable in the requested language. Keep this separate from factual support.
4. **Item-specific checks:** a flashcard answer follows from its question and source. An MCQ has one defensible keyed answer, coherent options and explanation, and no unintended second correct option. These item-design checks are proposed requirements; the four papers do not validate them.

Have a second reader independently label a subset, reconcile disagreements, and improve rubric examples. Report counts and denominators per artifact type/language and retain representative failures. Compare the same pack after prompt/model changes. Choose any acceptance policy explicitly as a project decision after inspecting failures; no universal threshold follows from these sources.

Start with deterministic checks for valid page references, required fields, duplicate options and answer-key validity, plus the human rubric. ROUGE or similar overlap scores may be exploratory signals when a reference exists; they should not stand in for source inspection. If volume later justifies it, pilot a source-visible LLM judge against the human-labelled subset, record disagreements and use it to prioritize review. QA/NLI metrics are a later research option when their maintenance and language-validation effort can be justified.

## Leads and unresolved gaps

- None of the inspected studies validates Bokmål factuality scoring or bilingual agreement; local fluent-reader assessment remains necessary.
- No direct evidence here on educational MCQ distractor quality, learning effectiveness, OCR/table fidelity, or optimal sample size. Keep those as separate evaluation questions.
- Useful leads already linked by the original papers include SummaC for factual-consistency benchmarking and the ALCE implementation for citation-check mechanics. They were not separately inspected or used as evidence in this round.
- This bounded round supports a feasible evaluation design, not any claim that a particular model, prompt, pipeline, or app is accurate.
