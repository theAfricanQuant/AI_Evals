# Recipe Bot Time Evaluator

## Question

Can a small rule-based evaluator classify whether a recipe fits the user's stated time limit, while sending uncertain cases to human review?

## Decision rule

See [`rubric.md`](rubric.md). The checker uses a reviewer-entered total when all required durations are known. It can also return Fail from a known minimum that already exceeds the requested cap, even if other durations are unstated. For a range, the upper end is the cap; the 5-minute tolerance applies only to a single approximate target in this exercise.

## Files

- `cases.jsonl` — six course-provided Recipe Bot traces and three synthetic fixtures. Course trace IDs are synthetic examples from the homework dataset, not production evidence.
- `rubric.md` — the human labeling rule and time-counting assumptions.
- `check.py` — deterministic classifier for structured annotations; it does not read recipe text or estimate durations itself.

## Reproduce

From the repository root:

```sh
uv run --no-project python projects/recipe-bot-time-evaluator/check.py
```

The last observed run before adding SYN069 printed `Case label matches: 8/8`. SYN069 was then manually labeled Fail and the checker was updated to handle a known minimum above the cap. Rerun the command to confirm the new case and branch.

## Limitation

The reviewer supplies the requested cap, duration completeness, and any known minimum or estimated total. A matching label count only checks that the code applies these annotations consistently; it does not show that the annotations or time estimates are correct. The source examples are from the course homework dataset, not production Recipe Bot traces. The suite is small and should not be used to estimate real-world performance.

## Study record

- [Chapter 5, Exercise 3 note](../../notes/2026-10-08-ch5-recipe-time-claims.md)
