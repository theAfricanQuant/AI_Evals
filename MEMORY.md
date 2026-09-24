# AI Evals — workspace memory

Coordination ledger for every agent working in this repository (Hermes in the Telegram topic, and any other agent the owner connects). **Read this file and AGENTS.md before touching anything.**

## How this file works

- `git log` records *what* changed; this file records *why, by whom, and what is next*.
- Any commit that changes the workspace also updates this file: append one dated entry to **Last actions** (never edit or delete past entries) and refresh **Current state**.
- Never delete or redo work recorded in the log without an explicit instruction from the owner.

## Current state

Workspace initialized (`8caf672`): syllabus + 12 lesson files for *AI Evals for Engineers & PMs*, `AGENTS.md`, `STUDY_METHOD.md`, `KNOWLEDGE_SOURCES.md`, `README.md`, and 9 pinned reference submodules under `references/`. `sources/` holds 8 source cards: `course-repositories-audit.md`, six paper/report cards (Who Validates the Validators, SPADE, PromptEvals, Task Cascades, Applied-LLMs report, Hamel's AI Evals FAQ), and Hamel's "Your AI Product Needs Evals" manifesto. `notes/` holds three dated study notes (2026-09-13 foundations kickoff, 2026-09-15 chapter 1 introduction, 2026-09-15 chapter 2 evaluation basics); `projects/` holds two working artifacts: the 5-case manual eval set for "Mama Nkechi's Kitchen" (`projects/manual-evalset/cases.md`) and the runnable email-summarizer checker (`projects/email-summarizer/` — prompt template, testset.json, check.py, README; offline, no API keys). Owner HTML reports are tracked in `reports/generated/` with names `chNN-exNN-topic-YYYY-MM-DD.html`, so they can be reviewed from any device. Current reports: `ch01-ex01-evals-background-2026-09-19.html` and `ch02-ex01-email-summarizer-practicum-2026-09-19.html`. The shared deliverable skill `skills/ai-evals-session/` (SKILL.md + mobile-first HTML template) is the single source of truth for HTML output across harnesses. Study session cadence: Trace → Test → Teach, one working artifact per session. Working agreement with the owner (AGENTS.md § Working channel): the Telegram topic is the decision channel; deliverables render as self-contained HTML in the owner's website theme (LivingStory); reports and learning materials are committed when agreed.

Latest scaffold (2026-09-24): the owner created `projects/nous-email-evals/` with `uv init --bare` and `uv add httpx`. This is a direct Nous API lab—no OpenAI dependency or credentials. `sources/nous-inference-api.md`, `notes/2026-09-24-nous-email-evals-scaffold.md`, and `reports/generated/ch02-ex02-nous-api-scaffold-2026-09-24.html` record the setup. No API key, live request, or trace has been stored; next is one learner-authored `main.py` request with terminal-only `NOUS_API_KEY` and `NOUS_MODEL`.

Owner learning preference (2026-09-22): practical sessions are learner-led—start from a blank lab the owner creates and advance one small observable step at a time; existing artifacts are references, not pre-built homework.

## Last actions (append-only, newest first)

- 2026-09-24 — Owner decision: scaffold the next Chapter 2 email-summarizer lab with a Nous API key, not OpenAI. Owner created `projects/nous-email-evals/` using `uv init --bare` and `uv add httpx`. Added a Nous API source card, scaffold study note, project README, and detailed self-contained report `ch02-ex02-nous-api-scaffold-2026-09-24.html`; all preserve the learner-led sequence and prohibit saved keys. By: Codex (owner conversation).
- 2026-09-22 — Owner decision: use a learner-led practical cadence. Future exercises begin in a blank lab the owner creates; teach one small observable step at a time, with existing projects treated as references rather than pre-built homework. Revised `reports/generated/ch02-ex01-email-summarizer-practicum-2026-09-19.html` so its first live LiteLLM run starts in `projects/first-litellm-call`, which the owner creates and writes themselves. By: Codex (owner conversation).
- 2026-09-19 — Owner decision: track self-contained HTML study reports in the repository for cross-device review. Report filenames now use `chNN-exNN-topic-YYYY-MM-DD.html`, putting chapter and exercise first and date last. Removed `reports/generated/` from `.gitignore`; updated `AGENTS.md` and `skills/ai-evals-session/SKILL.md` so all future agents follow the same convention. Retained reports: `ch01-ex01-evals-background-2026-09-19.html` and `ch02-ex01-email-summarizer-practicum-2026-09-19.html`. Superseded September 17 generated recap and Chapter 3 reports were removed by owner request. By: Codex (owner conversation).
- 2026-09-15 — Study session 2 (Trace→Test→Teach) on book ch. 2 "LLMs and Evaluation Basics" (full text in repo): dated note `notes/2026-09-15-ch2-llms-and-evaluation-basics.md`, working artifact `projects/email-summarizer/` (prompt template, 5-email testset, `check.py` — 4 reference-free mechanical checks, offline, no API keys; real run 9/12 passed, 3 failed as designed). Test step caught a criteria bug: phone regex missed "(415) 555-9021" — fixed with `\s*` after separators. HTML `reports/generated/2026-09-15-ch2-llms-and-evaluation-basics.html` (mobile-first, LivingStory). By: Hermes (Telegram topic).
- 2026-09-15 — Shared deliverable skill created in the repo so ANY harness reproduces the same output: `skills/ai-evals-session/SKILL.md` + `skills/ai-evals-session/templates/study-note.html` (LivingStory palette, mobile-first: `.tablewrap` scrollable tables, 720px breakpoint, 375px-safe). AGENTS.md: rule 6 corrected from teal to LivingStory, new rule 8 (every agent reads the skill, uses the template; rules win on conflict). Both existing HTML reports re-rendered mobile-safe. Hermes-side skill `ai-evals-study-session` created pointing at the repo skill. Commit `b92e2d3`. By: Hermes (Telegram topic).
- 2026-09-15 — Study session 1 (Trace→Test→Teach) on book ch. 1 "Introduction" (why evals matter): dated note `notes/2026-09-15-ch1-introduction.md`, source card for Hamel's manifesto `sources/hamel-your-ai-product-needs-evals.md`, first working artifact `projects/manual-evalset/cases.md` (5-case manual eval set for "Mama Nkechi's Kitchen"). Ch1 text is paywalled on O'Reilly; motivation sourced from the free manifesto + ch1 preview. By: Hermes (Telegram topic).
- 2026-09-13 — Expanded study note 001 to the full kickoff scope: agreed working rules + ledger rationale, course structure, evals vs TDD, why it is new, deployment layers/harnesses, the people behind the course (Shreya's papers + Hamel's guides), reference projects and learning order. Nigerian-anchored 10th-grade examples added per the owner's request. HTML re-rendered to match (LivingStory colors). By: Hermes (Telegram topic).
- 2026-09-13 — Correction: the first HTML render used the German-tenses teal palette, which is NOT the website theme. Re-rendered study note 001 in the correct sisengai.com palette (LivingStory: cream `#FDFBF7`, mahogany `#321208`, amber `#D4720A`; Inter + Playfair Display), verified from the live site CSS. Skill `ricky-phone-html-design` updated with the site palette and a pitfall entry. By: Hermes (Telegram topic).
- 2026-09-13 — First study note: AI Evals Foundations (`notes/2026-09-13-evals-foundations.md`) — what evals are, evals vs TDD, why it is new, where evals deploy. HTML render delivered to the owner (`reports/generated/`, not pushed). By: Hermes (Telegram topic).
- 2026-09-13 — Added 6 source cards for the core papers and reports behind the course: Shreya Shankar's Who Validates the Validators?, SPADE, PromptEvals, Task Cascades; Hamel Husain's AI Evals FAQ; the Applied-LLMs industry report. Commit `8e89bd1`. By: Hermes (Telegram topic).
- 2026-09-13 — Created the coordination ledger (`MEMORY.md`) and added AGENTS.md rule 7 (read AGENTS.md + MEMORY.md before work; every workspace commit also updates the ledger; never delete or redo logged work without the owner's instruction). Commit `2abc115`. By: Hermes (Telegram topic).
- 2026-09-13 — AGENTS.md: strengthened rule 4 — always `git pull --rebase` immediately before every push; the remote may be advanced by other agents. Commit `1c87051`. By: Hermes (Telegram topic).
- 2026-09-13 — AGENTS.md: added the Telegram working-channel agreement (6 rules). Commit `d7a76fb`. By: Hermes (Telegram topic).
- 2026-09-13 — Initialized the workspace: course baseline, study method, knowledge-source catalog, reference submodules. Commit `8caf672`. By: Hermes (Telegram topic).

## In progress

- Nothing in progress. First study session complete; next session not started.

## Open decisions

- None.

## Next up

- Start the first Trace step: choose a decision-relevant question from Lessons 1–3.
- Practice manual trace review with `references/recipe-chatbot/` Homework 2 (per `sources/course-repositories-audit.md`).
