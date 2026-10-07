# Recipe Bot Automated Evaluator

## Question

Can a code-based evaluator detect when a recipe leaves out an ingredient the user explicitly requested?

## Metric

For each case, mark **Pass** if every recorded requested ingredient appears in the recipe response. Mark **Fail** if one or more are missing. The failure rate is the number of Fail results divided by the number of cases checked.

## Input and matching

Each case has a `requested_ingredients` list. Real traces are loaded from the Recipe Bot source file by ID; synthetic fixtures include the response directly. A person records the ingredient list from the query. Matching is case-insensitive and requires a whole word or phrase. The explicit alias map currently treats “green onions” as an alias for “scallions.” The evaluator does not extract ingredients from free-form queries, find unlisted synonyms, or judge recipe quality or quantities.

The `avocados` request in `SYN031` was normalized by the reviewer to `avocado`, because the recipe uses one avocado and the request did not specify a quantity.

## Files

- `cases.jsonl` — two Recipe Bot Pass traces and three synthetic edge cases.
- `check.py` — deterministic ingredient-presence evaluator with an explicit alias map and whole-word matching.

## Study record

- [Chapter 5, Exercise 1 note](../../notes/2026-10-06-ch5-ingredient-presence-evaluator.md)
- [Chapter 5, Exercise 2 note](../../notes/2026-10-07-ch5-ingredient-matching-edge-cases.md)

## Reproduce

From the repository root, run:

```sh
uv run python projects/recipe-bot-automated-evaluator/check.py
```

Observed output after Exercise 2: all five expected labels matched. The two real traces were Pass; the synthetic missing-salmon and substring-collision cases were Fail; the synthetic scallion/green-onion alias case was Pass.

## Limitation

This is a logic demonstration, not a measured Recipe Bot failure rate. The two real traces are both Pass cases; all three edge cases are synthetic. Only one alias is configured. Whole-word matching still cannot infer unlisted aliases, distinguish a recipe from a statement that an ingredient was omitted, or handle every plural and wording variation. This does not lift the Chapter 4 decision to wait for a second reviewer and a balanced clear-Pass/clear-Fail/borderline set before operationalizing this rubric.
