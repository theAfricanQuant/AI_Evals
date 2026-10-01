# Recipe Chatbot error analysis — Chapter 3 working artifact

- Date: 2026-09-17
- Study note: [notes/2026-09-17-ch3-error-analysis.md](../../notes/2026-09-17-ch3-error-analysis.md)
- Course links: `3. Error Analysis.md`
- Upstream reference dataset: `references/recipe-chatbot/homeworks/hw2/reference_files/query_response.jsonl`

## What this is

A reproducible **20-trace teaching slice** from the course's local Recipe Chatbot Homework 2 dataset. The artifact stores only selected IDs and human labels; it reads the upstream JSONL in place, so it does not copy the 250 query/response pairs into this workspace.

Each pair is a single-turn trace: the user query and the bot's final response. The review records one binary decision and the first observed failure for every unacceptable trace. Open codes were written before the structured `failure_mode` labels were assigned.

## Files

- `sample_ids.json` — fixed IDs, source path, selection rule, and coverage dimensions.
- `labels.csv` — manual binary decisions, first-failure open codes, and the final axial-code label.
- `analyze.py` — validates the sample and labels, then reports the category counts.

## Run

From the repository root:

```sh
uv run python projects/recipe-bot-error-analysis/analyze.py
```

Expected result: 20 reviewed traces, 13 unacceptable; the two leading categories are `unverified_restriction` and `unsupported_time_claim`, at 4 traces each.

## Decision rule and limitation

Mark a response **unacceptable** when the first observed problem breaks a stated user constraint, makes a safety-sensitive claim without a check, or promises a time/pantry property the instructions do not support. Assign only that first failure to prevent downstream symptoms from inflating counts.

This is practice data, not production evidence: it is synthetic, has no tool calls, and has only 20 traces. It is too small to claim theoretical saturation or to set a release gate.
