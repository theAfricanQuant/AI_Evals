# AI Evals: full topic kickoff — how we work, what evals are, why they matter, where they run

- Date: 2026-09-13
- Course links: all 12 lesson files; closest: `1.`–`5.`, `9. Continuous Integration and Deployment for LLM Agents.md`, `12. Improving LLM Agents.md`
- Source cards: `sources/course-repositories-audit.md`; `sources/who-validates-the-validators.md`; `sources/spade.md`; `sources/promptevals.md`; `sources/applied-llms.md`; `sources/hamel-evals-faq.md`; `sources/task-cascades.md`

## Question

What did we agree in this topic, what is AI evaluation, how is it different from test-driven development, why is it new, where does it run, and who are the people behind the course?

## Method and evidence

Kickoff conversation in the dedicated Telegram topic, grounded in the course syllabus, the 12 lesson files, and the seven source cards created the same day. Everything below was agreed or discussed in that conversation; agreements are the only things pushed to `main`.

## Part A — How we work (the agreed rules)

The topic is the working channel for the whole workspace. What we agree here gets committed and pushed; nothing else gets pushed. The full set lives in `AGENTS.md` § Working channel:

1. **The topic is the only channel for decisions.** Agreed here → committed to `main`.
2. **Keep the baseline sacred.** The syllabus and numbered lessons keep their wording. New ideas go in `notes/`, `sources/`, `projects/`.
3. **Trace → Test → Teach.** Every study session ends with a dated note (`notes/YYYY-MM-DD-<topic>.md`) and a working artifact (test set, evaluator, trace, or analysis). No advancing on summaries alone.
4. **One decision per push.** The commit message names the decision. Always `git pull --rebase` before every push — other agents work in this repo too — and never force-push.
5. **Safety.** No API keys, cookies, or private source text in these files. NotebookLM queries only when the owner has asked.
6. **Deliverables in website colors.** Anything presented to the owner renders as self-contained HTML in the sisengai.com theme (cream/mahogany/amber, Inter + Playfair Display). The repository baseline stays Markdown.
7. **MEMORY.md is the coordination ledger.** Every agent reads AGENTS.md + MEMORY.md before working. Any commit that changes the workspace also updates MEMORY.md: append a dated log entry (never edit or delete past entries) and refresh Current state. Never delete or redo work recorded in the log without an explicit instruction from the owner.

**Why the ledger exists:** the owner accesses this repo from other agents too. Git records *what* changed; MEMORY.md records *why, by whom, and what is next*. Together they mean nothing is missed and no one deletes or redoes someone else's work.

## Part B — The course at a glance

*AI Evals for Engineers & PMs* — 9 live lectures plus a bonus lecture, taught by Hamel Husain and Shreya Shankar. You build a support agent, instrument it so its behavior is measurable, find its failures with disciplined error analysis, put it under a CI/CD regression suite, red-team it, and improve both accuracy and cost.

- **Module 1 — Building Agents (L1–L3):** write a SPEC.md, build the agent on the OpenAI Agents SDK, instrument it (traces, spans, prompt hashes), stand up Langfuse + ClickHouse, generate ~500 synthetic support scenarios.
- **Module 2 — Error Analysis (L4–L5):** read real traces, build a failure taxonomy from data (open coding → axial coding), then one binary evaluator per failure mode. Validate judges against human labels (true-positive/true-negative rates, bootstrap confidence intervals). Homework: label 60+ traces, build a 5–8-mode taxonomy.
- **Module 3 — CI/CD (L6):** turn failures into test cases; mechanical failures become code assertions, subjective ones become pinned judge checks; wire a GitHub Actions gate; post-deploy monitoring on sampled traffic.
- **Module 4 — Safety & Governance (L7):** OWASP Top 10 for agentic applications, prompt-injection defense (authorization must hold even when the model is compromised), red-teaming with promptfoo, NIST AI RMF + EU AI Act floor.
- **Module 5 — Improving Agents (L8–L9):** compare variants on one frontier (same prompt, tools, harness, workload, suite), route fixes to the cheapest effective layer (prompt → tool → harness → model), profile cost, caching, cascades; homework freezes a winner on the test slice and runs the upgrade drill.

Our workspace's study cadence: four passes (Foundations L1–3 → Measurement L4–5 → Operations L6–7 → Improvement L8–9), finishing each pass with one working artifact.

## Part C — What are AI evals?

**Think of NAFDAC.** Before goods reach the market, NAFDAC checks them. AI evals are the same for AI agents: tests that check whether an agent behaves correctly before real users see it.

**A closer example — the neighborhood POS agent.** Many people trust their POS agent with money every day. How do you know the agent is reliable? You don't test "must say exactly these words" — you check properties: Do they give correct change? Do they send the right alert? Do they not run away with the money? Do customers leave satisfied? Those checks are evals.

**Why normal tests don't work for AI:** ordinary software is a timetable — a danfo bus that leaves exactly at 7:00, every day, same route. Test it once and it holds. An AI agent is a keke driver — the route depends on traffic, the passenger, and judgment. Ask it the same question twice and you may get two different answers. So evals test *properties and judgments*, not exact outputs.

**The loop (the course's whole flywheel): Analyze → Measure → Improve:**
Trace (record what the agent did) → Failure taxonomy (name the failure modes from real data) → Evaluator (one test per failure mode) → Regression gate (run every time you change the agent) → Monitor (watch live traffic after deploy).

## Part D — Evals vs TDD (test-driven development)

TDD is testing a **calculator**: you know the exact answer, so you assert `2 + 2 == 4` and the machine checks it forever. Deterministic, precise, green or red.

An AI agent is a **salesperson**, not a calculator. You cannot assert "must say exactly this sentence" — good behavior varies. So you check properties: Did they greet the customer? Quote the right price? Not promise what the shop cannot deliver? Did the customer leave satisfied?

| | TDD (classic) | AI Evals |
| --- | --- | --- |
| Asserts | Exact output: `assert 2+2 == 4` | Properties & judgments: right tool? grounded? safe? helpful? |
| Determinism | Same input → same output, forever | Output varies run to run; tests must be statistical |
| Spec | Knowable — you can read the code | Emergent — "whatever a human judges as good" |
| Test cases | Enumerate known cases | Infinite input space — sample from real traces |
| Trust | Green = correct | The judge itself must be validated against human labels |

**The course rule:** mechanical failures → code assertions (that's TDD, and it works fine in AI — schemas, tool arguments, permissions). Subjective failures → judged evals. TDD is the subset of evals where the output is exactly verifiable.

## Part E — Why is it a big deal now?

Classic software testing worked for 50 years because of three assumptions. LLMs break all three at once:

1. **You knew the expected answer.** A function has a spec; you read the source. An LLM's "source" is billions of web pages — the spec is emergent.
2. **Same input → same output.** An LLM can answer differently each run — and a vendor can change its behavior overnight without your code moving. Like a tomato supplier at the market who quietly switches quality: you only find out by checking again.
3. **You could enumerate the test cases.** Human language is effectively infinite. You cannot write one test per question — you must sample from real traces.

Plus two things classic SE never had to test:

4. **Semantic failures with real damage.** The code *runs* — but the answer is subtly wrong, hallucinated, or the agent took a real action: sent an email, spent money, granted access. Like a POS transfer that goes to the wrong account — the transaction succeeded, but it is wrong.
5. **Cost and latency are part of correctness.** Two agents can both be "right" — one is 10× cheaper and 5× faster. Evals must track accuracy × cost × speed together.

And the trap most teams fall into: **"let the AI judge itself" fails.** That is exactly what Shreya's paper *Who Validates the Validators?* proved. A judge is like a market-union chairman: you trust his judgment only after you have watched him settle many disputes fairly. An LLM judge must be validated against human labels before you trust it as a CI gate.

## Part F — Where are evals deployed?

Not inside one harness — as a layer around *any* agent. Three places:

1. **Development (offline):** run the agent against test scenarios and measure. Runners: promptfoo, Inspect AI, DeepEval, RAGAS — or tracing platforms with eval built in: Langfuse, LangSmith, Braintrust, Arize Phoenix.
2. **CI/CD gate:** every pull request runs the suite before merge (e.g. GitHub Actions). That is Lesson 6.
3. **Production monitoring:** capture real traffic, run *frozen* judges on a sample, dashboards and alerts when pass-rate drops.

**The harnesses:** OpenClaw (an open-source personal assistant that runs on your machine via Telegram/WhatsApp, same family as Hermes), Hermes itself, Claude Code / Codex CLI, and apps built on the OpenAI Agents SDK — all are *subjects under test*. The eval layer looks identical for all of them. Evals also ship as agent skills (`npx skills add ai-evals-course/evals-skills`), and MCP lets any harness call the same evals. **Don't shop for "the harness with evals" — pick any harness; the flywheel is the same.**

## Part G — The people behind the course

**Shreya Shankar** (UC Berkeley PhD, course co-instructor) — academic papers:
- *Who Validates the Validators?* (UIST 2024, arxiv 2404.12272) — judges must be aligned with human preferences.
- *SPADE: Synthesizing Data Quality Assertions* (VLDB 2024, arxiv 2401.03038) — auto-generate assertions from prompt deltas; code pinned in `references/spade-experiments/`.
- *PromptEvals* (NAACL 2025, arxiv 2504.14738) — real assertions from production pipelines; code pinned in `references/prompt-eval-recommendation/`.
- *Task Cascades* (SIGMOD 2026, arxiv 2601.05536) — vary the task per stage for cost savings (Lesson 12).
- Also: DocWrangler (UIST 2025), DocETL (VLDB 2025), FrugalGPT-adjacent cost work. Full list: sh-reya.com/papers.

**Hamel Husain** (course co-instructor) — not an academic paper publisher; practitioner guides:
- *What We've Learned From a Year of Building with LLMs* (applied-llms.org, with Shreya + 4 others) — the industry bible on what breaks in production.
- *AI Evals: Everything You Need to Know* (hamel.dev/blog/posts/evals-faq/) — plain-language answers from the course.
- Maintains `evals-skills` (the skill pack) with Shreya.

All six are captured as source cards in `sources/`.

## Part H — Reference projects and learning order

The `references/` folder pins 9 upstream repositories as read-only submodules. From the audit card (`sources/course-repositories-audit.md`), the recommended order:

1. Learn the vocabulary; write a five-case manual eval set in this workspace.
2. Use `references/recipe-chatbot/` Homework 2 to practice manual trace review and failure taxonomy. **Best first codebase.**
3. Move to Homework 3 only after a failure mode has a clear binary definition; use `references/judgy/` only after a human-labeled calibration set exists.
4. Use the Cartwheel course (`references/cartwheel-homeworks/`) to connect tools, authorization, traces, CI, safety, and optimization into one production-style system.
5. Introduce `evals-skills` (`references/evals-skills-course/`) against our own traces; consult optional platforms (Braintrust, FastHTML review interfaces, SPADE, prompt-eval-recommendation) only when their problem arises.

NotebookLM: the workspace notebook (ID `6112cb5e-0188-45a2-ae89-b6f268c6c9f0`, 62 sources) is queried only when the owner has asked; source metadata is captured as cards, not copied text.

## Takeaway

AI evaluation is an empirical, statistical discipline layered around any agent — not a feature of any single harness. TDD remains valid for the deterministic subset; the new work is naming failures from real traces and validating judges against humans before trusting them. Where the agent runs (Hermes, OpenClaw, custom bots) does not change the eval layer. The workspace rules + MEMORY.md ledger keep multi-agent work honest: nothing missed, nothing deleted, everything agreed.

## Next retrieval

- [ ] Choose the first decision-relevant study question from Lessons 1–3 and start the Trace step.
- [ ] Practice manual trace review and failure taxonomy with `references/recipe-chatbot/` Homework 2.
- [ ] Build one working artifact (test set, evaluator, or trace analysis) before advancing to Lesson 4.
