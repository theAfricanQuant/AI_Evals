# SPADE: Synthesizing Data Quality Assertions for Large Language Model Pipelines

- Source: https://arxiv.org/abs/2401.03038 (VLDB 2024)
- Type: paper (code pinned in `references/spade-experiments/`)
- Accessed: 2026-09-13
- Course links: `5. Implementing Automated Evaluators.md`; `8. Evaluating Tool Use and Complex Agents.md`; `12. Improving LLM Agents.md`

## What it contributes

- SPADE auto-generates candidate assertions from prompt deltas (what changed between prompt versions) plus labeled inputs/outputs.
- Checks subsumption: redundant assertions are dropped so the suite stays minimal.
- Selects the final assertion set with an optimizer (ILP) rather than by hand.
- Evaluates assertions on synthetic data first, with a human labeling step, before trusting them.

## Use in this knowledge base

When a prompt changes, generate candidate evals instead of hand-writing them — but treat SPADE output as candidates to review, not a replacement for Lesson 5's validation discipline. Also feeds the Lesson 8 improvement loop (prompt-change detection).

## Questions to test

- Does SPADE's assertion for my prompt delta actually catch the regression I care about?
- Which of its generated assertions are redundant given my existing suite?
