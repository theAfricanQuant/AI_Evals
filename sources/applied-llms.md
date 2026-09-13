# What We've Learned From a Year of Building with LLMs (Applied-LLMs)

- Source: https://applied-llms.org/ (O'Reilly Radar, Parts I & II)
- Type: article (industry report)
- Accessed: 2026-09-13
- Course links: all lessons; closest to `2. LLMs and Evaluation Basics.md`; `9. Continuous Integration and Deployment for LLM Agents.md`; `12. Improving LLM Agents.md`

## What it contributes

- Six practitioners (Eugene Yan, Bryan Bischof, Charles Frye, Hamel Husain, Jason Liu, Shreya Shankar) report what actually breaks in production LLM applications.
- Covers evals, tracing/observability, caching, cost, RAG failure modes, and model-vendor risk.
- The recurring message: instrument and evaluate early, because failure modes appear only under real traffic.

## Use in this knowledge base

The reality check for every lesson — production failure patterns and practices from real teams. Read a section whenever a lesson's claim needs a concrete industry example.

## Questions to test

- Which of the report's documented production failures would my current agent exhibit on 20 real traces?
- Which of its eval practices am I skipping, and what evidence do I have that skipping is safe?
