# Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences

- Source: https://arxiv.org/abs/2404.12272 (UIST 2024)
- Type: paper
- Accessed: 2026-09-13
- Course links: `3. Error Analysis.md`; `4. Collaborative Evaluation Practices.md`; `5. Implementing Automated Evaluators.md`

## What it contributes

- An LLM judge is not trustworthy by default: evaluator criteria must be aligned with the human preferences the product actually cares about.
- Users need evaluation criteria to grade outputs, but grading outputs helps users discover what their criteria are — evaluation is iterative, not one-shot.
- Human-labeled preference data is the ground truth for validating any automated judge.
- Introduces EvalGen, a minimal interface for human evaluation of LLM outputs (integrated into ChainForge as EvalGen v2).

## Use in this knowledge base

The cornerstone for Lesson 5's judge-validation discipline: no LLM judge enters the CI suite until its true-positive/true-negative rates are measured against human labels (also the prerequisite for `references/judgy/`).

## Questions to test

- On my own 20 labeled traces, does my judge agree with my judgment at a level I would trust as a CI gate?
- Which criteria did I infer from real traces, and which did I invent before looking at data?
