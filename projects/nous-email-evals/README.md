# Nous email evals — learner-built Chapter 2 lab

- Date: 2026-09-24
- Study note: [Nous API scaffold](../../notes/2026-09-24-nous-email-evals-scaffold.md)
- Source card: [Nous Research Inference API](../../sources/nous-inference-api.md)
- Course links: `2. LLMs and Evaluation Basics.md`

## What exists now

The learner created this project with `uv init --bare`, added `httpx` with `uv add httpx`, and added Ruff as a development dependency with `uv add --dev ruff`. `pyproject.toml` declares the dependencies and `uv.lock` preserves the resolved versions.

`main.py` sends one fixed support email to the Nous chat-completions endpoint. `traces/trace-001.md` preserves the first successful response from `deepseek/deepseek-v4.1-flash`. No API key is stored in this project.

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

## Next action

Inspect `traces/trace-001.md`, then create four more deliberately different emails. Before running them, decide whether the next requirement should be “names the sender,” “captures every request,” or a stricter output format. Do not call a rule an evaluator until its decision rule is written down.
