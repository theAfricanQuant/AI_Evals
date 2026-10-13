---
name: ai-evals-session
description: Use for study sessions and deliverables in the AI Evals workspace. Defines Trace→Test→Teach, file conventions, source grounding, and the owner's required newspaper-homepage HTML style.
---

# AI Evals study session and newspaper report skill

This skill is shared by every agent working in this repository. Read it with `AGENTS.md` and `MEMORY.md` before starting. The owner's standing preference is for HTML reports in the newspaper-homepage version described below.

## 1. Read first

- `AGENTS.md` — workspace rules and the owner's current preferences.
- `MEMORY.md` — coordination ledger: what happened, why, and what comes next.
- `STUDY_METHOD.md` — the Trace → Test → Teach workflow.
- `KNOWLEDGE_SOURCES.md` when external course material or a safe access path is needed.

## 2. Study-session workflow: Trace → Test → Teach

1. **Trace:** read the relevant lesson, source card, dataset, or conversation trace.
2. **Test:** make a small observable artifact, such as a labeled example set, evaluator, trace review, or controlled comparison. Write the decision rule before interpreting the result.
3. **Teach:** add `notes/YYYY-MM-DD-<topic>.md` with the question, method and evidence, takeaway, and next retrieval. Link source cards instead of copying their summaries.
4. **Report:** when an HTML report is requested or needed for the session, copy the newspaper template below and replace the content while preserving its layout.

Every completed study session has both a dated note and a working artifact. A summary alone does not complete a session.

## 3. HTML reports: Newspaper Homepage

The canonical visual reference is [theAfricanQuant/newspaper-homepage-skill](https://github.com/theAfricanQuant/newspaper-homepage-skill). Its source describes the editorial structure and constraints; this repository's template adapts that design for AI Evals study reports.

- **Output path:** `reports/generated/chNN-exNN-topic-YYYY-MM-DD.html`. Put chapter and exercise first, date last. Keep each report self-contained and free of secrets or private source text.
- **Template:** start from `skills/ai-evals-session/templates/newspaper-homepage.html`. Preserve the newspaper layout and use the existing CSS rather than returning to the retired LivingStory card layout.
- **Front-page shape:** compact three-part publication line; centered oversized serif masthead; short italic motto; double-rule edition strip; exactly three desktop columns (lead story, secondary briefs, slim right rail); warm paper, near-black serif headlines, small uppercase red story labels, thin rules, and editorial whitespace.
- **Right rail:** include exactly two compact, square-cornered bordered boxes titled **YOUR DAY** and **THE ALMANAC**. Use **YOUR DAY** for the concrete next retrieval or implementation task. Use **THE ALMANAC** for sourced course context, a definition, or a useful fact. Do not invent appointments, weather, or daily plans.
- **Study content:** make the page compact but complete. Explain the decision sequence in plain language: question, success rule, method, result, and what the result can and cannot show. Define jargon inline. Include a trace/case when relevant. Put source links beside the claims they support; do not add a source directory or footer.
- **Lab log:** include a clearly labeled lab or reproduction item with the actual secret-free command, observed or expected output, and limitation. If no command or model run was done, say so clearly.
- **Diagrams:** include at least one visually polished, topic-specific diagram that makes a key idea, process, or decision easier to understand. Use a clear reading order, useful labels, balanced spacing, and the newspaper palette. Build it from self-contained HTML or inline SVG; make it accessible and readable on a phone. Avoid decoration that competes with the explanation.
- **Scope:** stop after the newspaper front page. Do not add a second page or a long continuation below it. On narrow screens, stack the same content in reading order.
- **Offline and accessibility:** do not load external fonts, CDNs, images, or other remote assets. Use semantic headings, readable contrast, keyboard-visible links, and responsive text. Give diagrams accessible descriptions when useful.
- **Verify:** check that the HTML parses with no unclosed tags, story claims and links match the sources, the right rail contains exactly the two required boxes, and the page has no horizontal overflow at a 375px viewport.

## 4. Writing style

- Address the owner as **Boss** when writing directly to him.
- Write in clear, mature **12th-grade English**. Use direct sentences and explain technical terms when they first appear. Keep the language accessible without making it childish or talking down to the owner.
- Anchor examples in Nigeria when it helps explain the idea (for example, a POS transaction, a market purchase, or a keke trip).
- End the report's reading path with a clear next task inside **YOUR DAY**.

## 5. Sources and safe research

- Keep a source's claim separate from the learner's interpretation.
- New source cards go in `sources/<slug>.md` and record title, URL or stable identifier, source type, access date, contribution, and course links.
- Never include API keys, cookies, passwords, or private source text.
- NotebookLM queries add a conversation turn. Use `ask` only when the owner has asked a question or approved that interaction.

## 6. Commit discipline

- A commit names one agreed decision.
- Before every push, run `git pull --rebase`; never force-push.
- When a workspace-changing commit is made, append a dated entry to `MEMORY.md` and refresh its Current state block. Never rewrite or delete earlier log entries.
- Do not stage unrelated or unreviewed files as part of a study-session change.
