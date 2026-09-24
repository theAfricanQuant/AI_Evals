# Nous email evals — learner-built Chapter 2 lab

- Date: 2026-09-24
- Study note: [Nous API scaffold](../../notes/2026-09-24-nous-email-evals-scaffold.md)
- Source card: [Nous Research Inference API](../../sources/nous-inference-api.md)
- Course links: `2. LLMs and Evaluation Basics.md`

## What exists now

The learner created this empty Python project with `uv init --bare` and added `httpx` with `uv add httpx`. `pyproject.toml` declares the dependency and `uv.lock` preserves the exact resolved versions.

No `main.py`, API key, model response, or evaluator is stored yet. This is intentional: the learner will type the first direct Nous request and inspect its raw response before designing checks.

## Why direct `httpx`

Nous exposes an OpenAI-compatible HTTP API, but this lab uses plain `httpx` rather than the OpenAI SDK. The endpoint and key are explicit in the code, so the setup makes clear that it uses Nous credentials and a Nous Portal model ID.

## Secret rule

Set `NOUS_API_KEY` only in the terminal that runs the program. Do not create a `.env` file, paste a key into `main.py`, or commit it. Record the selected model ID and non-sensitive request settings in saved traces later.

## Next action

Create `main.py` by following `reports/generated/ch02-ex02-nous-api-scaffold-2026-09-24.html`, set `NOUS_API_KEY` and `NOUS_MODEL` in the terminal, and run one request. Save the raw output only after confirming it has no private information.
