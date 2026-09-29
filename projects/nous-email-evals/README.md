# Nous email evals — learner-built Chapter 2 lab

- Date: 2026-09-24
- Study notes: [Nous API scaffold](../../notes/2026-09-24-nous-email-evals-scaffold.md) · [Nous error analysis](../../notes/2026-09-29-nous-email-error-analysis.md)
- Source card: [Nous Research Inference API](../../sources/nous-inference-api.md)
- Course links: `2. LLMs and Evaluation Basics.md`

## What exists now

The learner created this project with `uv init --bare`, added `httpx` with `uv add httpx`, and added Ruff as a development dependency with `uv add --dev ruff`. `pyproject.toml` declares the dependencies and `uv.lock` preserves the resolved versions.

`main.py` sends one fixed support email to the Nous chat-completions endpoint. The learner saved eleven key-free traces from `deepseek/deepseek-v4.1-flash` and recorded the first error-analysis pass in [`analysis.md`](analysis.md). No API key is stored in this project.

The current client uses `max_tokens=320`. It also prints safe response metadata when content is missing; that showed an earlier empty completion stopped with `finish_reason: length` at the lower 160-token limit.

## Why direct `httpx`

Nous exposes an OpenAI-compatible HTTP API, but this lab uses plain `httpx` rather than the OpenAI SDK. The endpoint and key are explicit in the code, so the setup makes clear that it uses Nous credentials and a Nous Portal model ID.

## Secret rule

Set `NOUS_API_KEY` only in the terminal that runs the program. Do not create a `.env` file, paste a key into `main.py`, or commit it. Record the selected model ID and non-sensitive request settings in saved traces later.

## Format and check the client

Python has no built-in equivalent to Rust's `cargo fmt`. This project uses Ruff:

```sh
uv run ruff format main.py
uv run ruff check main.py
```

`ruff format` lays out valid Python consistently. `ruff check` looks for common code-quality problems. Neither command sends a request to Nous.

## About the `VIRTUAL_ENV` warning

If `uv run` says that an existing `VIRTUAL_ENV` does not match this project's `.venv`, it is informational: `uv` ignores the unrelated active environment and uses the project environment it manages. Nothing is broken, and do not use `uv run --active` here.

Running `unset VIRTUAL_ENV` is optional. It removes only that variable from the current terminal session, which hides the warning. It does not delete, deactivate, or alter any virtual environment.

## Chapter 3 result

The learner made one product rule: a callback number in an input email must retain the same digits in the summary. With the original prompt, Amina's email, and `max_tokens=320`, the predeclared three-run reliability test passed 2/3 times. The third output ended at “call her at” and omitted the digits.

That is useful evidence, not a release gate or production pass rate. Read [`analysis.md`](analysis.md) and traces 009–011 before making a broader test set.

## Next action

Record `finish_reason` for every response, including non-empty responses, then add varied inputs such as quoted threads, vague senders, and other Nigerian phone formats. Open-code those traces before defining a second evaluator rule.
