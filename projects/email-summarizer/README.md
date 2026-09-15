# Email summarizer — working artifact (Chapter 2)

- Date: 2026-09-15
- Study note: [notes/2026-09-15-ch2-llms-and-evaluation-basics.md](../../notes/2026-09-15-ch2-llms-and-evaluation-basics.md)
- Course links: `2. LLMs and Evaluation Basics.md`

## What this is

The book's running example — a simple email summarizer (sender + key requests) — turned into a **runnable, offline test artifact**. It demonstrates Chapter 2's *absolute, reference-free evaluation*: we check the summarizer's output against criteria we define (format, completeness, no invented content) with deterministic assertions — no LLM, no API keys, no gold summaries needed.

## Files

- `prompt.md` — the prompt template (course Example 2-1).
- `testset.json` — 5 input emails covering the failure modes we care about.
- `check.py` — 4 mechanical reference-free checks; run on canned outputs.

## Run

```
python3 check.py
```

## What it teaches

- Mechanical failures → code assertions (the L1 unit-test level from Chapter 1).
- `case-04` and `case-05` are deliberately *judgment* cases: a one-request email can't honestly fill "exactly 3 bullets", and a vague email needs the agent's ambiguity policy (ask vs infer) — those are product decisions, not code bugs.
