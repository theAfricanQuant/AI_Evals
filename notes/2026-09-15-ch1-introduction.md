# Chapter 1 — Introduction: why evaluation is essential

- Date: 2026-09-15
- Book: *Evals for AI Engineers* (Hamel Husain & Shreya Shankar, O'Reilly, early release), ch. 1 "Introduction"
- Course links: `2. LLMs and Evaluation Basics.md` (chapter 2 opens by referencing this motivation); every later chapter builds on it
- Source cards: `sources/hamel-your-ai-product-needs-evals.md`; `sources/applied-llms.md`; `sources/hamel-evals-faq.md`
- Working artifact: `projects/manual-evalset/cases.md` — the five-case manual eval set (first artifact of the course)

## Question

Why does evaluation deserve a whole book? What exactly is an *LLM application* versus an *LLM agent*, and what does systematic evaluation look like in practice?

## Method and evidence

- O'Reilly preview of chapter 1 (paywalled after the opening paragraphs) — gives the definitions of LLM application and LLM agent, and the range from a single LLM call with no tools to a loop that calls many tools and makes many decisions.
- Full text of Hamel's manifesto *Your AI Product Needs Evals* (hamel.dev/blog/posts/evals/, saved 2026-09-15) — the motivation chapter 1 builds on, including the Lucy (Rechat) case study and the three levels of evaluation.

## Key ideas

1. **The vocabulary.** An *LLM application* is a software product that embeds LLMs (customer service, content creation, decision support, information extraction). The *LLM agent* is the LLM-driven component inside it — the part that makes decisions, calls tools, and produces output. The book covers the full range: simplest single LLM call (no tools) up to a system that runs in a loop with many tools and many decisions.
2. **The root cause.** Hamel's five years of building LLM products: unsuccessful products almost always share one root cause — a failure to create robust evaluation systems.
3. **Iterating quickly == success.** You need processes for (1) evaluating quality, (2) debugging issues, (3) changing the system. Most teams do only #3, which is why so many products never get past demo. All three together make the virtuous cycle.
4. **The Lucy case study (Rechat).** A real-estate AI assistant that progressed fast with prompt engineering, then plateaued: fixing one failure created others (whack-a-mole), there was no visibility beyond "vibe checks", and prompts grew long and unwieldy. The fix was a systematic approach centered on evaluation.
5. **Three levels of evaluation.** L1: unit tests — fast, cheap assertions run on every code change (e.g. a regex asserting no UUID is exposed; scenario tests like "exactly one listing matches"). L2: model & human evaluation, which includes debugging. L3: A/B testing after significant product changes. Cost runs L3 > L2 > L1, and cadence follows cost.
6. **Test cases.** Use an LLM to generate synthetic inputs ("write 50 instructions a real-estate agent gives his assistant to create contacts…"). Update tests constantly from real observed data. Pass rate is a product decision — you do not always need 100%.
7. **Eval infrastructure is debugging infrastructure.** A searchable trace database, assertions that flag bad behavior, log search and navigation tools, and a fast change-and-test loop.
8. **The closing lessons.** Remove all friction from looking at data; keep it simple; "you are doing it wrong if you aren't looking at lots of data"; do not rely on generic evaluation frameworks — build an eval system specific to your problem; write lots of tests and update them frequently; use LLMs to unblock eval creation; reuse eval infrastructure for debugging and fine-tuning.

## Takeaway

Evaluation is the engine of AI product improvement, not a chore at the end. Without evals you cannot see failures; without seeing failures you cannot improve; without a test you cannot prove an improvement is real. That is the whole argument of chapter 1, and it is why this workspace exists.

## Next retrieval

- [ ] Chapter 2: learn the components of LLM applications (single call → agent loops) and the two evaluation modes (absolute vs comparative).
- [ ] Turn the five-case manual eval set (`projects/manual-evalset/cases.md`) into a runnable starter test suite.
- [ ] Note which of the five cases are mechanical (code assertions) vs subjective (judged) — a bridge to chapters 4–5.
