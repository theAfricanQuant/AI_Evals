# AI Evals — workspace memory

Coordination ledger for every agent working in this repository (Hermes in the Telegram topic, and any other agent the owner connects). **Read this file and AGENTS.md before touching anything.**

## How this file works

- `git log` records *what* changed; this file records *why, by whom, and what is next*.
- Any commit that changes the workspace also updates this file: append one dated entry to **Last actions** (never edit or delete past entries) and refresh **Current state**.
- Never delete or redo work recorded in the log without an explicit instruction from the owner.

## Current state

Workspace initialized (`8caf672`): syllabus + 12 lesson files for *AI Evals for Engineers & PMs* (Hamel Husain, Shreya Shankar), `AGENTS.md`, `STUDY_METHOD.md`, `KNOWLEDGE_SOURCES.md`, `README.md`, and 9 pinned reference submodules under `references/`. `sources/` holds 7 source cards: `course-repositories-audit.md` plus six paper/report cards (Who Validates the Validators, SPADE, PromptEvals, Task Cascades, Applied-LLMs report, Hamel's AI Evals FAQ). `notes/` holds the first dated study note (`2026-09-13-evals-foundations.md`); rendered HTML for the owner lives in `reports/generated/` (gitignored) in the correct sisengai.com LivingStory colors (cream/mahogany/amber). Working agreement with the owner (AGENTS.md § Working channel): the Telegram topic is the decision channel; deliverables to the owner render as self-contained HTML in SisengAI teal colors; the repository baseline stays Markdown.

## Last actions (append-only, newest first)

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
