# Recipe Bot review-agreement pilot — Chapter 4

- Date: 2026-10-03
- Course link: `4. Collaborative Evaluation Practices.md`
- Upstream traces: `../../references/recipe-chatbot/homeworks/hw2/reference_files/query_response.jsonl`

## Question

Can a reviewer consistently check whether a recipe uses every specifically named ingredient the user requests?

## Artifact

- `rubric.md` — the binary requested-ingredient rubric, version 0.
- `shared-set.md` — 10 fixed Recipe Bot trace IDs.
- `reviewer-a.csv` — one independent review pass.

## Method

The reviewer compared each source query’s explicitly named ingredients with the recipe’s ingredients and instructions.

The review intentionally ignored recipe quality, cooking time, pantry claims, and dietary or health claims.

## Result

Reviewer A marked all 10 selected traces as `Pass`.

## Reproduce the check

From the repository root, run:

```sh
uv run python projects/recipe-bot-review-agreement/check.py
```

Expected output:

```text
Source traces available: 250
Shared set: 10 fixed traces
Reviewer A labels: 10
Pass: 10
Fail: 0
IAA / Cohen's Kappa: not calculated (one reviewer; one label class)
```

## Limitation

This is a pilot, not an inter-annotator-agreement result:

- only one reviewer labeled the set;
- the set contained no `Fail` labels;
- therefore, Cohen’s Kappa must not be calculated or reported.

A second reviewer agreeing on ten easy Pass cases would not show that the rubric handles ambiguity.

## Decision

Do not turn this rubric into an automated evaluator yet.

## Next

Build a new shared set with deliberate failures and borderline cases, then ask a second reviewer to label it independently before measuring agreement.
