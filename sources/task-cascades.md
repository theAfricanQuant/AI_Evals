# Task Cascades for Efficient Unstructured Data Processing

- Source: https://arxiv.org/abs/2601.05536 (to appear, SIGMOD 2026)
- Type: paper
- Accessed: 2026-09-13
- Course links: `12. Improving LLM Agents.md`

## What it contributes

- Extends the FrugalGPT idea: instead of only cascading across models, vary what the model is asked to do at each stage — a cheap model answers a simplified version, harder cases escalate to an expensive model.
- Targets cost/accuracy trade-offs for unstructured data processing with guarantees.
- Lesson 12 cites it as the follow-up to FrugalGPT (Chen et al. 2023) for the cost-improvement track.

## Use in this knowledge base

Design source for the Lesson 9/12 cost-optimization exercise — a cascade plan for the course's support agent, measured on the same held-out suite as the baseline.

## Questions to test

- On my workload, does a task cascade beat a model-only cascade on cost at equal accuracy?
- Where in the cascade does my failure rate actually rise, and is the escalation rule catching it?
