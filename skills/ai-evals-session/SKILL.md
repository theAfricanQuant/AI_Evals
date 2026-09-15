---
name: ai-evals-session
description: Use when producing any deliverable for the AI Evals workspace owner — study notes, source cards, or self-contained HTML reports. Defines the study workflow (Trace→Test→Teach), file conventions, commit discipline, and the exact LivingStory HTML template in the owner's website colors so every agent harness produces identical output.
---

# AI Evals session & HTML deliverable skill

Shared by every agent working in this repository (Hermes, Claude Code, Codex CLI, OpenClaw, or any other harness that can read this repo). The owner views deliverables as **self-contained HTML** in his website theme. Follow this skill exactly so all harnesses produce the same output.

## 1. Read first (always)

- `AGENTS.md` — the operating rules (especially the Telegram working channel).
- `MEMORY.md` — the coordination ledger: what happened, by whom, what is next.
- `STUDY_METHOD.md` — the study loop this workspace runs on.

## 2. Study-session workflow (Trace → Test → Teach)

1. **Trace** — read the source material: lesson file, source card, or reference.
2. **Test** — apply it: produce a working artifact (eval set, evaluator, trace analysis, regression test).
3. **Teach** — write `notes/YYYY-MM-DD-<topic>.md` with this skeleton:
   - question, method & evidence, key ideas, takeaway, next retrieval;
   - link the relevant source cards (`sources/<slug>.md`);
   - then render the HTML for the owner.

Every session ends with BOTH the dated note AND a working artifact. No advancing on summaries alone.

## 3. HTML deliverables — the owner's website theme (LivingStory)

- **Output path:** `reports/generated/YYYY-MM-DD-<topic>.html` — gitignored, never pushed. The repository baseline stays Markdown.
- **Template:** copy `skills/ai-evals-session/templates/study-note.html` and replace the content sections. Do not restyle it.
- **Palette** (verified from the live sisengai.com CSS):
  - background cream `#FDFBF7`; cards white; borders `#F2EBD8` / `#E8DCC4`;
  - headings mahogany `#321208`; body text stone `#57534E`; muted `#78716C`;
  - accents/links amber `#D4720A` (hover `#B05A08`); panels `#FFF8EC`; chip accents `#FFDDA0`;
  - success sage `#2D5C3C` on `#F3F8F4`; danger `#BE3E24` on `#FDF5F2`.
- **Fonts:** body `"Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`; headings `"Playfair Display", Georgia, "Times New Roman", serif`; mono `"JetBrains Mono", SFMono-Regular, Menlo, Monaco, Consolas, monospace`. Never load external fonts or CDNs — the file must work offline with graceful fallbacks.
- **Structure:** dark mahogany gradient hero (kicker · serif title · subtitle · meta line) with an amber bottom border; content sections as white rounded cards (`h2` serif headings); two-column card grids collapsing to one column under 720px; tables with amber header rows and cream striping; callouts with colored left borders (amber / sage / ink / danger); footer with the source line.
- **Verify before delivery:** the file parses as HTML (no unclosed tags) and is meaningful in size.
- **Mobile-first:** reports must render well on phones. Wrap every table in `<div class="tablewrap">…</div>` (horizontal scroll), rely on the template's fluid type and breakpoint styles, and make sure the layout survives a 375px viewport without horizontal page overflow.

## 4. Writing style for the owner

- Address him as "Boss".
- 10th-grade English: short sentences, plain words, every jargon term explained inline.
- Anchor examples in Nigeria (NAFDAC checks, POS agents, market traders, keke vs danfo) — they land best with him.
- Every report ends with a clear "Next" section.

## 5. Commit discipline (per AGENTS.md)

- One decision per commit; the commit message names the decision.
- Always `git pull --rebase` immediately before every push; never force-push; other agents may have advanced the remote.
- On every workspace-changing commit, append a dated entry to MEMORY.md "Last actions" (never edit or delete past entries) and refresh the "Current state" block.
- Push only Markdown sources (notes/, sources/, projects/, skills/, AGENTS.md, MEMORY.md). HTML stays in `reports/generated/`.
