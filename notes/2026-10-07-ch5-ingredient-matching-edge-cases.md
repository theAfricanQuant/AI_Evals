# Chapter 5: Ingredient Aliases and Whole-Word Matching

- Date: 2026-10-07
- Course link: [5. Implementing Automated Evaluators](../5.%20Implementing%20Automated%20Evaluators.md)
- Working artifact: [Recipe Bot ingredient evaluator](../projects/recipe-bot-automated-evaluator/)
- Related note: [Ingredient-presence evaluator](2026-10-06-ch5-ingredient-presence-evaluator.md)

## Question

Can a deterministic ingredient-presence check handle one known synonym while avoiding a false match inside a longer word?

## Method and evidence

Added two explicitly synthetic cases to the existing two real Pass traces and one synthetic missing-ingredient fixture:

- `fixture-002`: requested “scallions”; response says “green onions”; expected Pass.
- `fixture-003`: requested “ham”; response says “shamrock”; expected Fail.

The first version of the checker produced a false negative for `fixture-002` because it searched only for the exact requested text. An explicit alias map now records `green onions` as an accepted name for `scallions`. The checker also uses regular-expression word boundaries around each escaped alias, so `ham` does not match inside `shamrock`.

Command run from the repository root:

```sh
uv run python projects/recipe-bot-automated-evaluator/check.py
```

Observed result: all five labels matched. The output marked both real cases Pass, `fixture-001` Fail with salmon missing, `fixture-002` Pass, and `fixture-003` Fail with ham missing.

## Key ideas

- Deterministic code is useful for a narrow, objective rule when the inputs are already structured.
- A synonym list makes accepted wording explicit and reviewable. It does not provide general synonym understanding.
- Whole-word matching prevents a short ingredient name from matching inside a longer word.
- A five-case result built from two real Pass traces and three synthetic fixtures demonstrates behavior on those examples. It does not estimate real failure rates or establish broad evaluator validity.

## Takeaway

The explicit alias and whole-word checks fix the two constructed edge cases, but the evaluator still needs reviewed real Fail and borderline traces before we can assess its usefulness on Recipe Bot behavior.

## Next retrieval

- [ ] Find and manually review real traces that may be clear Fail or borderline for requested-ingredient presence; keep synthetic fixtures separate from real evidence.
