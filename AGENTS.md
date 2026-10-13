# AI Evals knowledge base

This folder is a durable study workspace for *AI Evals for Engineers & PMs*.

## Start here

When asked to add learning material, synthesize sources, or plan a study session, read [STUDY_METHOD.md](STUDY_METHOD.md) first. For available external material and its safe access path, read [KNOWLEDGE_SOURCES.md](KNOWLEDGE_SOURCES.md). Before producing any deliverable (study note or HTML report), read [skills/ai-evals-session/SKILL.md](skills/ai-evals-session/SKILL.md). For every new HTML report, copy [skills/ai-evals-session/templates/newspaper-homepage.html](skills/ai-evals-session/templates/newspaper-homepage.html); the newspaper homepage version below is the owner's standing preference.

## Working agreement

The owner may make decisions and authorize changes in any active collaboration channel. No specific messaging channel is required.

1. Keep the baseline sacred. The syllabus and numbered lesson files keep their wording; interpretations, exercises, and extensions go in `notes/`, `sources/`, and `projects/`.
2. Trace → Test → Teach. Every study session ends with a dated note (`notes/YYYY-MM-DD-<topic>.md`) and a working artifact (test set, evaluator, trace, or analysis). No advancing on summaries alone.
3. Every push is one agreed decision. The commit message names the decision. Always run `git pull --rebase` immediately before every push — the remote may have advanced through another agent's or the user's work — and never force-push.
4. Safety holds: no API keys, cookies, or private source text in these files; NotebookLM queries only when the user has asked.
5. **HTML report style — Newspaper Homepage (owner's standing preference):** every new report is a self-contained, newspaper-style front page based on [the newspaper-homepage skill](https://github.com/theAfricanQuant/newspaper-homepage-skill) and the shared template at `skills/ai-evals-session/templates/newspaper-homepage.html`. Use a compact three-part publication line; oversized centered serif masthead and short italic motto; double-rule edition strip; exactly three columns on desktop (dominant lead, secondary briefs, slim right rail); small uppercase red story labels; warm paper colors, near-black serif headlines, thin rules, and editorial whitespace. The right rail has exactly two square-cornered bordered boxes titled **YOUR DAY** and **THE ALMANAC**. On narrow screens, stack the same content in reading order. Keep the report compact but complete: include the study question, method and result, relevant source links beside claims, a reproducible lab command or clear reason none was run, observed output, limitation, and the next retrieval task. Put the next task in **YOUR DAY**. Write in clear, mature 12th-grade English: explain technical terms in plain language without talking down to the reader. Include at least one visually polished, topic-specific diagram that clarifies a key idea, process, or decision; make it self-contained, accessible, and readable on a phone. Do not append a second page, long continuation, source directory, or footer. Keep the report offline-ready: no external fonts, CDNs, or remote assets. This newspaper design replaces the former LivingStory template for all new HTML reports. Store and track reports at `reports/generated/chNN-exNN-topic-YYYY-MM-DD.html`, with chapter and exercise first and date last. Reports are part of the repository baseline and may be committed and pushed.
6. [MEMORY.md](MEMORY.md) is the coordination ledger. Every agent reads AGENTS.md and MEMORY.md before working. Any commit that changes the workspace also updates MEMORY.md: append a dated log entry (never edit or delete past entries) and refresh the Current state block. Other agents may be working from this repository — never delete or redo work recorded in the log without an explicit instruction from the owner.
7. Shared deliverable skill. `skills/ai-evals-session/SKILL.md` defines the study workflow and newspaper report conventions; `skills/ai-evals-session/templates/newspaper-homepage.html` is the canonical HTML starter. Every agent producing study notes or HTML for the owner reads the skill and uses the newspaper template so all harnesses produce the same style. `skills/ai-evals-session/templates/study-note.html` is retained for historical reference only and must not be used for new reports. If an external skill and these workspace rules disagree, these rules win.

## Python toolchain

Use **uv only** for Python work in this workspace: create environments, add or remove dependencies, lock them, and run scripts or tests with `uv run`. Do not introduce `pip`, `venv`, Conda, Poetry, or another Python environment/package workflow.

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
