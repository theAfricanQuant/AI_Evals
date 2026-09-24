# AI Evals knowledge base

A private, hands-on learning workspace for *AI Evals for Engineers & PMs*. It holds the course notes, personal study evidence, and pinned upstream reference projects.

## Start here

1. Read [STUDY_METHOD.md](STUDY_METHOD.md) and choose one decision-relevant question.
2. Use the numbered lesson files as the course baseline.
3. Capture external material in `sources/`, record learning sessions in `notes/`, and put runnable work in `projects/`.

## Current hands-on progress

Chapter 2 now has a learner-built live Nous API lab at [`projects/nous-email-evals/`](projects/nous-email-evals/). The owner created the project with `uv`, used direct `httpx` rather than an OpenAI dependency, formatted the client with Ruff, and saved one key-free Nous trace from `deepseek/deepseek-v4.1-flash`.

The first trace correctly captured Ada's locked-account problem, reset request, and request for a sign-in update. It is evidence of one successful connection and response—not an evaluation score or a claim that the prompt is reliable. See the [study note](notes/2026-09-24-nous-email-evals-scaffold.md) and [Nous scaffold report](reports/generated/ch02-ex02-nous-api-scaffold-2026-09-24.html).

## Reference projects

The `references/` directory contains Git submodules: clean, pinned checkouts of the course's public tools and adjacent research. They are read-only study references; personal work belongs outside them.

After cloning this repository, fetch them with:

```bash
git submodule update --init --recursive
```

To deliberately refresh the reference checkouts later:

```bash
git submodule update --remote --recursive
```

Review the resulting commit changes before committing an update.

## Safety

Never commit API keys, browser cookies, NotebookLM exports containing private source text, `.env` files, or local service data. See [AGENTS.md](AGENTS.md) for the operating rules and [KNOWLEDGE_SOURCES.md](KNOWLEDGE_SOURCES.md) for source access.
