# PromptEvals: A Dataset of Assertions and Guardrails for Custom Production LLM Pipelines

- Source: https://arxiv.org/abs/2504.14738 (NAACL 2025, selected for oral presentation)
- Type: paper + dataset (code pinned in `references/prompt-eval-recommendation/`)
- Accessed: 2026-09-13
- Course links: `5. Implementing Automated Evaluators.md`; `8. Evaluating Tool Use and Complex Agents.md`

## What it contributes

- A public dataset of real assertions and guardrails collected from production LLM pipelines.
- A taxonomy of eval function types — the shapes practitioners actually check (format, schema, semantic, tool-behavior, etc.).
- Grounds the "eval function" vocabulary Lesson 5 uses; the companion recommendation app suggests evals from prompt diffs.

## Use in this knowledge base

A library of proven assertion patterns to copy when building the Lesson 5 evaluators and the Lesson 8 prompt-change workflow — mechanical checks before reaching for an LLM judge.

## Questions to test

- Which PromptEvals assertion types map directly onto my own failure modes?
- Can I write one code assertion per mechanical failure before I need a judge at all?
