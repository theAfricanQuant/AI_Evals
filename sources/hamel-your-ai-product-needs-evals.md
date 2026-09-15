# Your AI Product Needs Evals (Hamel Husain's manifesto)

- Source: https://hamel.dev/blog/posts/evals/
- Type: article (practitioner manifesto)
- Accessed: 2026-09-15 (full text saved to web cache; 26,477 chars)
- Course links: `1. Introduction` (book ch1) — this post IS the motivation behind chapter 1; `2. LLMs and Evaluation Basics.md`; `5. Implementing Automated Evaluators.md`

## What it contributes

- **The root cause claim:** after five years of LLM products (since CodeSearchNet), unsuccessful products almost always share one root cause — a failure to create robust evaluation systems.
- **Iterating quickly == success:** you need processes for (1) evaluating quality, (2) debugging issues, (3) changing the system. Most teams only do #3, which keeps products at demo level. The three together form the virtuous cycle.
- **The Lucy case study (Rechat):** a real-estate AI assistant whose prompt engineering plateaued — fixing one failure created others (whack-a-mole), no visibility beyond vibe checks, prompts grew unwieldy. Systematic evaluation centered on "eval and curation" broke the plateau.
- **Three levels of evaluation:** L1 unit tests (assertions, fast and cheap, run on every code change — e.g. regex asserting no UUID is exposed; listing-count scenarios), L2 model & human eval (includes debugging), L3 A/B testing. Cost L3 > L2 > L1, so cadence follows cost.
- **Test-case generation:** use an LLM to synthesize test inputs (e.g. "write 50 instructions a real-estate agent gives his assistant to create contacts"); update tests constantly from real observed data; pass rate is a product decision, not always 100%.
- **Eval infrastructure == debugging infrastructure:** a searchable trace database, assertions that flag bad behavior, log search tools, and a fast change-and-test loop.
- **Closing lessons:** remove ALL friction from looking at data; keep it simple (use what you have first); "you are doing it wrong if you aren't looking at lots of data"; don't rely on generic evaluation frameworks — build an eval system specific to your problem; write lots of tests and update them frequently; use LLMs to unblock eval creation (generate cases, write assertions, critique, label); reuse eval infra for debugging and fine-tuning.

## Use in this knowledge base

Chapter 1 of the book is paywalled beyond its preview; this free post carries its full motivation. It also grounds Level 1 (unit tests) used in chapter 6's CI/CD work and the assertion-writing habits of chapters 4–5.

## Questions to test

- On my own product idea, which of the three activities (evaluate / debug / change) would I skip first — and what breaks?
- For one feature, can I write three assertion-style unit tests before reaching for an LLM judge?
