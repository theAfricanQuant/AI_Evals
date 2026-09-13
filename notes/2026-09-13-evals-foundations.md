# AI Evals Foundations: what they are, how they differ from TDD, where they run

- Date: 2026-09-13
- Course links: `2. LLMs and Evaluation Basics.md`; `3. Error Analysis.md`; `4. Collaborative Evaluation Practices.md`; `5. Implementing Automated Evaluators.md`; `9. Continuous Integration and Deployment for LLM Agents.md`; `12. Improving LLM Agents.md`
- Source cards: `sources/who-validates-the-validators.md`; `sources/spade.md`; `sources/promptevals.md`; `sources/applied-llms.md`; `sources/hamel-evals-faq.md`; `sources/task-cascades.md`

## Question

What is AI evaluation, how does it differ from classical test-driven development, and where does it get deployed?

## Method and evidence

Grounding session with the workspace owner, anchored in the course lessons and the six core source cards added the same day.

- **What evals are.** Tests that check whether an AI agent behaves correctly before real users see it. Agents are non-deterministic, so evals test properties and judgments rather than exact outputs. The loop is Analyze → Measure → Improve: trace → failure taxonomy → evaluator → regression gate → monitoring.
- **Evals vs TDD.** TDD asserts exact expected outputs on deterministic code (the calculator). Evals check properties of behavior that cannot be enumerated (the salesperson). They are not opposites: mechanical failures get code assertions (TDD-style); subjective failures get judged evals. Course rule: code checks first, LLM judges only where interpretation is needed.
- **Why it is new.** Classical testing assumed (1) a knowable spec, (2) same input → same output, (3) an enumerable input space. LLMs break all three; add semantic failures with real-world side effects, and cost/latency as part of correctness.
- **Where it deploys.** Three layers: development (offline eval runners: promptfoo, Inspect AI, DeepEval, RAGAS, or tracing platforms Langfuse/LangSmith/Braintrust), CI/CD gate (e.g. GitHub Actions, Lesson 6), production monitoring (frozen judges on sampled traffic). The layer is harness-agnostic: Hermes, OpenClaw, Claude Code, and OpenAI Agents SDK apps are all subjects under test; the eval layer looks identical. Evals also ship as agent skills (`npx skills add ai-evals-course/evals-skills`) and MCP lets any harness call the same evals.

## Takeaway

AI evaluation is an empirical, statistical discipline layered around any agent — not a feature of any single harness. TDD remains valid for the deterministic subset; the new work is naming failures from real traces and validating judges against humans before trusting them (Who Validates the Validators). Where the agent runs (Hermes, OpenClaw, custom bots) does not change the eval layer.

## Next retrieval

- [ ] Choose the first decision-relevant study question from Lessons 1–3 and start the Trace step.
- [ ] Practice manual trace review and failure taxonomy with `references/recipe-chatbot/` Homework 2 (per `sources/course-repositories-audit.md`).
