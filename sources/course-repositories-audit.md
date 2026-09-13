# Course repositories: verified technical audit

- Source: user-supplied *Technical Audit of Course Repositories and Tooling for AI Evals for Engineers*, checked against repository metadata and primary READMEs.
- Accessed: 2026-09-13
- Course links: `AI Evals For Engineers & PMs — Syllabus.md`; `2. LLMs and Evaluation Basics.md`; `3. Error Analysis.md`; `4. Collaborative Evaluation Practices.md`; `5. Implementing Automated Evaluators.md`; `7. Evaluating Retrieval-Augmented Generation.md`; `8. Evaluating Tool Use and Complex Agents.md`; `9. Continuous Integration and Deployment for LLM Agents.md`

## What the ecosystem contributes

The repositories implement one coherent workflow: build an application with observable behavior, inspect real traces, name failure modes, turn confirmed failures into evaluators, validate automated judges against human labels, and use the resulting suite for regression testing and iteration. This is the practical meaning of the course's Analyze → Measure → Improve flywheel.

## Local reference checkouts

| Reference | Local path | Use it for | Study stage |
| --- | --- | --- | --- |
| [Cartwheel homework](https://github.com/ai-evals-course/cartwheel-homeworks) | `references/cartwheel-homeworks/` | End-to-end support-agent course: deterministic world, tracing, evaluation, CI, adversarial tests, and improvement | Main hands-on project after fundamentals |
| [Recipe chatbot](https://github.com/ai-evals-course/recipe-chatbot) | `references/recipe-chatbot/` | Five compact assignments covering error analysis, judge design, RAG evaluation, and multi-turn failure analysis | Best first codebase for this curriculum |
| [Evals Skills](https://github.com/ai-evals-course/evals-skills) | `references/evals-skills-course/` | Agent-facing workflows for error discovery, synthetic data, judge prompts, validation, RAG, and review interfaces | Use once a concrete application or trace dataset exists |
| [judgy](https://github.com/ai-evals-course/judgy) | `references/judgy/` | Bias-corrected LLM-as-a-judge success-rate estimates with bootstrap confidence intervals | Later, after human labels and a calibrated binary judge exist |

All checkouts are references, not templates to edit. Keep personal exercises in `projects/` and link the exact upstream file used from the related study note.

## Cataloged for later use

| Reference | Why it is useful | When to reach for it |
| --- | --- | --- |
| [Braintrust course implementation](https://github.com/braintrustdata/ai-evals-course-2025) | An alternative, platform-specific implementation of synthetic data, tracing, calibrated judges, RAG, and failure-transition analysis | When evaluating whether to use Braintrust; it requires external account/API setup |
| [FastHTML workshop](https://github.com/ai-evals-course/isaac-fasthtml-workshop) | Patterns for a purpose-built human trace-review and annotation interface | When spreadsheets no longer make nested traces reviewable |
| [SPADE experiments](https://github.com/shreyashankar/spade-experiments) | Research experiments on assertions for LLM pipelines | Advanced reading after building a basic regression suite |
| [Prompt-eval recommendation](https://github.com/shreyashankar/prompt-eval-recommendation) | Streamlit app that recommends eval functions from prompt diffs | Advanced prompt-change and regression work |

## Corrections and cautions

- `ai-evals-course/error-discovery-skill` resolves to the current `ai-evals-course/evals-skills` repository. Track it as one source, not two.
- The separate `references/evals-skills/` checkout came from the older `hamelsmu/evals-skills` repository. Prefer `references/evals-skills-course/` for the active course-owned version.
- `judgy` corrects a measured binary judge rate; it does not make an unvalidated judge trustworthy. Human labels and held-out calibration remain prerequisites.
- The Cartwheel and recipe repositories contain runnable applications and may require dependencies, service containers, and model-provider keys. Read their local `AGENTS.md` or README before any setup; do not run them merely to study the concepts.

## Recommended learning order

1. Learn the vocabulary and write a five-case manual eval set in this workspace.
2. Use `recipe-chatbot` Homework 2 to practice manual trace review and failure taxonomy work.
3. Move to Homework 3 only after the failure mode has a clear binary definition; use `judgy` after a human-labeled calibration set exists.
4. Use the Cartwheel course to connect tools, authorization, traces, CI, safety, and optimization into one production-style system.
5. Introduce Evals Skills against your own traces, then consult the optional platform and research references only when their problem arises.

## Questions to test

- Can I distinguish a product requirement, a failure mode, an evaluator, and a release decision?
- Can I write five cases that would reveal a real defect in an LLM application's behavior?
- What evidence would convince me that an LLM judge agrees with the human judgment I actually care about?
