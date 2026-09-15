# AI Evals knowledge base

This folder is a durable study workspace for *AI Evals for Engineers & PMs*.

## Start here

When asked to add learning material, synthesize sources, or plan a study session, read [STUDY_METHOD.md](STUDY_METHOD.md) first. For available external material and its safe access path, read [KNOWLEDGE_SOURCES.md](KNOWLEDGE_SOURCES.md). Before producing any deliverable (study note or HTML report), read the shared skill at [skills/ai-evals-session/SKILL.md](skills/ai-evals-session/SKILL.md) and copy its template — every harness must produce identical output.

## Working channel (Telegram)

This workspace is run from a dedicated Telegram topic. Agreements made there are the only changes pushed to this repository.

1. The topic is the only channel for decisions about this workspace. What we agree there gets committed to `main`; nothing is pushed that was not settled there.
2. Keep the baseline sacred. The syllabus and numbered lesson files keep their wording; interpretations, exercises, and extensions go in `notes/`, `sources/`, and `projects/`.
3. Trace → Test → Teach. Every study session ends with a dated note (`notes/YYYY-MM-DD-<topic>.md`) and a working artifact (test set, evaluator, trace, or analysis). No advancing on summaries alone.
4. Every push is one agreed decision. The commit message names the decision. Always run `git pull --rebase` immediately before every push — the remote may have advanced through another agent's or the user's work — and never force-push.
5. Safety holds: no API keys, cookies, or private source text in these files; NotebookLM queries only when the user has asked.
6. Deliverables presented to the user in the topic render as self-contained HTML in the owner's website theme (sisengai.com "LivingStory": cream `#FDFBF7`, mahogany `#321208`, amber `#D4720A`, Inter + Playfair Display), using the shared template in `skills/ai-evals-session/`; the repository baseline stays Markdown.
7. [MEMORY.md](MEMORY.md) is the coordination ledger. Every agent reads AGENTS.md and MEMORY.md before working. Any commit that changes the workspace also updates MEMORY.md: append a dated log entry (never edit or delete past entries) and refresh the Current state block. Other agents may be working from this repository — never delete or redo work recorded in the log without an explicit instruction from the owner.
8. Shared deliverable skill. `skills/ai-evals-session/SKILL.md` and `skills/ai-evals-session/templates/study-note.html` define the deliverable workflow and the exact HTML template (owner's website colors and fonts). Every agent producing study notes or HTML for the owner reads the skill and uses the template, so all harnesses produce identical output. If the skill and these rules disagree, these rules win.

## Working rules

- Treat the numbered top-level lesson files and the syllabus as the course baseline. Preserve their wording; put interpretations, exercises, and extensions in new notes.
- Before creating a note, search existing Markdown for the concept so each claim has one home and related lessons are linked rather than restated.
- Add a new source as a source card in `sources/<slug>.md`. Add a completed study session in `notes/YYYY-MM-DD-<topic>.md`. Create either directory only when its first file is needed.
- Every source card records the original title, URL or stable identifier, source type, access date, and a short account of what it contributes. Keep a distinction between a source's claim and the learner's interpretation.
- Every study note connects one concrete question to one or more course lessons, states a testable takeaway, and ends with the next retrieval or implementation task.
- Prefer querying a connected NotebookLM notebook for synthesis over copying video transcripts or PDFs into this repository. Never put account cookies, access tokens, passwords, or private source text in these files.
- A NotebookLM `ask` operation adds a conversation turn. Use it only when the user has asked a question or approved that interaction; listing metadata and reading a supplied notebook's summary are read-only research steps.
- For changes involving code or an agent, turn the lesson into an observable artifact: a small dataset, evaluator, trace, regression test, or analysis. Record the command, inputs, result, and limitation in the study note.

## Done means

A learning addition is complete when its provenance is recoverable, its connection to the course is explicit, a learner can reproduce the exercise or query, and the next action is unambiguous.
