# Knowledge sources

This catalog records access paths and provenance. It is not a copy of the underlying material.

## NotebookLM: Building Practical LLM Evaluations: Lessons from the Trenches

- Notebook: <https://notebook.google.com/notebook/6112cb5e-0188-45a2-ae89-b6f268c6c9f0>
- Notebook ID: `6112cb5e-0188-45a2-ae89-b6f268c6c9f0`
- Access: authenticated local `notebooklm` CLI; verified 2026-09-13.
- Scope: 62 ready sources across tool and agent evaluation, LLM-as-a-judge, dataset construction, error analysis, CI/CD, tracing, reliability, and cost.

### What it adds to this course

The course files supply a structured path from agent design through error analysis, CI/CD, security, and improvement. This notebook adds a broad practitioner library: tool-call and trace evaluation, judge alignment, repetitions, online evaluation, implementation walkthroughs, and tooling case studies.

### Retrieval protocol

1. Start with the relevant numbered course lesson and a decision-relevant question.
2. Query the notebook only for that question; ask it to name the supporting source titles.
3. Make a source card for the specific source or cluster that changes the study plan.
4. Create a study note only after testing or applying the idea.

The direct notebook URL can be queried even when the notebook does not appear in the active account's ordinary `notebooklm list` output. Treat source metadata and NotebookLM summaries as pointers; consult the original item when a precise technical claim matters.

### Notable source clusters

- **Evaluator design:** golden datasets, binary versus score evaluators, LLM-as-a-judge, and human-preference alignment.
- **Agent diagnosis:** function/tool-call checks, trace-level evals, transition matrices, retrieval evaluation, and multi-turn/voice/multimodal cases.
- **Production:** CI/CD, online evaluation, experiments, annotations, reliability repetitions, and cost/ROI.
- **Frameworks and practice:** Braintrust, Arize Phoenix, LangSmith, Weights & Biases, Inspect, and case studies including GitHub Copilot.

## Adding a new source

Add a source only when it supports an active course question or an implementation decision. Record the original URL or stable identifier in `sources/`; link the resulting study note from the relevant project README when code is involved. This keeps the knowledge base auditable, lightweight, and searchable.
