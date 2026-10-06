# Recipe Bot Automated Evaluator

## Question

Can a code-based evaluator detect when a recipe leaves out an ingredient the user explicitly requested?

## Metric

For each case, mark **Pass** if every recorded requested ingredient appears in the recipe response. Mark **Fail** if one or more are missing. The failure rate is the number of Fail results divided by the number of cases checked.

## Input and scope

Each case has a `requested_ingredients` list. Real traces are loaded from the Recipe Bot source file by ID; synthetic fixtures include the response directly. A person records the ingredient list from the query. This first evaluator checks case-insensitive text presence; it does not extract ingredients from free-form queries, resolve synonyms, or judge recipe quality or quantities.

The `avocados` request in `SYN031` was normalized by the reviewer to `avocado`, because the recipe uses one avocado and the request did not specify a quantity.

## Files

- `cases.jsonl` — two Recipe Bot trace labels and one synthetic Fail fixture.
- `check.py` — case-insensitive substring evaluator.

## Reproduce

From the repository root, run:

```sh
uv run python projects/recipe-bot-automated-evaluator/check.py
```

Observed output: all three expected labels matched; `fixture-001` was marked Fail with `salmon` reported missing.

## Limitation

This is a logic demonstration, not a measured Recipe Bot failure rate. The two real traces are both Pass cases, while the only Fail is synthetic. It does not lift the Chapter 4 decision to wait for a second reviewer and a balanced clear-Pass/clear-Fail/borderline set before operationalizing this rubric. The small set also does not validate the evaluator on aliases, paraphrases, or false-positive substring matches.
