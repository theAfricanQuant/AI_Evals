# AI Evals knowledge base

A private, hands-on learning workspace for *AI Evals for Engineers & PMs*. It holds the course notes, personal study evidence, and pinned upstream reference projects.

## Start here

1. Read [STUDY_METHOD.md](STUDY_METHOD.md) and choose one decision-relevant question.
2. Use the numbered lesson files as the course baseline.
3. Capture external material in `sources/`, record learning sessions in `notes/`, and put runnable work in `projects/`.

## Current hands-on progress

Chapter 2 now has a learner-built live Nous API lab at [`projects/nous-email-evals/`](projects/nous-email-evals/). The owner created the project with `uv`, used direct `httpx` rather than an OpenAI dependency, formatted the client with Ruff, and saved key-free Nous traces from `deepseek/deepseek-v4.1-flash`.

Chapter 3 used those traces for a small callback-number reliability test. The learner declared the pass rule before running three identical trials at `max_tokens=320`: two passed and one failed because it omitted the number and ended mid-sentence. That is evidence of a concrete failure mode, not a reliable pass rate. See the [scaffold note](notes/2026-09-24-nous-email-evals-scaffold.md), [error-analysis note](notes/2026-09-29-nous-email-error-analysis.md), and [Chapter 3 report](reports/generated/ch03-ex01-nous-email-error-analysis-2026-09-29.html).

An earlier Chapter 3 practice session applies the same method to a fixed 20-trace slice of the Recipe Chatbot Homework 2 data. Its reproducible trace-review artifact found 13 unacceptable traces; unverified dietary, religious, or health restrictions and unsupported time claims each occurred in 4 of 20. See the [study note](notes/2026-09-17-ch3-error-analysis.md), [working artifact](projects/recipe-bot-error-analysis/), and [Chapter 3 practice report](reports/generated/ch03-ex02-recipe-bot-error-analysis-2026-09-17.html).

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
