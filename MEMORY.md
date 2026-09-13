# AI Evals — workspace memory

Coordination ledger for every agent working in this repository (Hermes in the Telegram topic, and any other agent the owner connects). **Read this file and AGENTS.md before touching anything.**

## How this file works

- `git log` records *what* changed; this file records *why, by whom, and what is next*.
- Any commit that changes the workspace also updates this file: append one dated entry to **Last actions** (never edit or delete past entries) and refresh **Current state**.
- Never delete or redo work recorded in the log without an explicit instruction from the owner.

## Current state

Workspace initialized (`8caf672`): syllabus + 12 lesson files for *AI Evals for Engineers & PMs* (Hamel Husain, Shreya Shankar), `AGENTS.md`, `STUDY_METHOD.md`, `KNOWLEDGE_SOURCES.md`, `README.md`, and 9 pinned reference submodules under `references/`. `sources/` holds 7 source cards: `course-repositories-audit.md` plus six paper/report cards (Who Validates the Validators, SPADE, PromptEvals, Task Cascades, Applied-LLMs report, Hamel's AI Evals FAQ). `notes/` and `projects/` are created on demand. Working agreement with the owner (AGENTS.md § Working channel): the Telegram topic is the decision channel; deliverables to the owner render as self-contained HTML in SisengAI teal colors; the repository baseline stays Markdown.

## Last actions (append-only, newest first)

- 2026-09-13 — Added 6 source cards for the core papers and reports behind the course: Shreya Shankar's Who Validates the Validators?, SPADE, PromptEvals, Task Cascades; Hamel Husain's AI Evals FAQ; the Applied-LLMs industry report. By: Hermes (Telegram topic).
- 2026-09-13 — Created the coordination ledger (`MEMORY.md`) and added AGENTS.md rule 7 (read AGENTS.md + MEMORY.md before work; every workspace commit also updates the ledger; never delete or redo logged work without the owner's instruction). Commit `2abc115`. By: Hermes (Telegram topic).
- 2026-09-13 — AGENTS.md: strengthened rule 4 — always `git pull --rebase` immediately before every push; the remote may be advanced by other agents. Commit `1c87051`. By: Hermes (Telegram topic).
- 2026-09-13 — AGENTS.md: added the Telegram working-channel agreement (6 rules). Commit `d7a76fb`. By: Hermes (Telegram topic).
- 2026-09-13 — Initialized the workspace: course baseline, study method, knowledge-source catalog, reference submodules. Commit `8caf672`. By: Hermes (Telegram topic).

## In progress

- Nothing in progress. First study session not started.

## Open decisions

- None.

## Next up

- Start the first Trace → Test → Teach session (suggested: Lesson 5 evaluator work via `references/recipe-chatbot/` Homework 2, per `sources/course-repositories-audit.md`).
