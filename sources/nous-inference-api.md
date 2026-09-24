# Nous Research Inference API

- Source: https://portal.nousresearch.com/api-docs and https://inference-api.nousresearch.com/v1/models
- Type: API documentation and live public model catalog
- Accessed: 2026-09-24
- Course links: `2. LLMs and Evaluation Basics.md`; `5. Implementing Automated Evaluators.md`

## What it contributes

- The Nous inference endpoint is OpenAI-compatible at `https://inference-api.nousresearch.com/v1`; this project can call it directly without using OpenAI credentials or the OpenAI SDK.
- Requests use a bearer API key. The key belongs only in the active terminal environment, never in repository files, a trace, or a report.
- The public `/models` catalog lists current model IDs and supported request parameters. The model ID should be copied from the owner's Nous Portal rather than hard-coded from a tutorial because the catalog changes.

## Use in this knowledge base

It supplies the live model endpoint for `projects/nous-email-evals/`, the learner-built continuation of the Chapter 2 email-summarizer exercise.

## Questions to test

- Can one Nous model produce a traceable email summary when given one fixed prompt and input?
- Which output requirements are safe to turn into deterministic checks after inspecting several real traces?
