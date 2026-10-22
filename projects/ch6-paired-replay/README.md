# Chapter 6: Paired Conversation Replay

## Purpose

This lab compares one request sent all at once with the same request delivered over several turns.

## Question

Does the assistant give a useful oatmeal suggestion when it receives the dietary details later in the conversation?

## Comparison

- **Control:** Ask for a healthy oatmeal breakfast and include the lactose-free and low-sugar requirements in the first message.
- **Replay:** Ask for a healthy oatmeal breakfast first. Add the lactose-free and low-sugar requirements in a later message.

Keep the model, tools, and success rule the same. Change only when the dietary details arrive.

## Success rule

The rule is in [`rubric.md`](rubric.md). Finalize it before running either version.

## What to record

For each run, save the exact messages, model and settings, assistant response, Pass/Fail/Review label, and a short reason for the label. Store results in `results/`.

## Current status

The first manual pair (`oatmeal-001`) used GPT-6 Luna with Medium reasoning and rubric v1. Its original replay label was Review because the rubric did not define non-calorie sweeteners; it has since been re-scored under rubric v2 in the result file. Fresh pair `oatmeal-002` used Gemini 3.8 in both conditions and rubric v2; both responses are Pass. Pair `oatmeal-003` used Gemini 3.8 in both conditions and added peanut-free and tree-nut-free constraints under rubric v3; both responses are Pass. Pair `oatmeal-004` used Gemini 3.8 to test correction of an initially requested tree-nut ingredient under a later dietary constraint; both responses are Fail because each offers stevia or monk-fruit, which the rubric counts as added sweeteners. The small keyword checker matched all seven fixtures, including excerpts from both oatmeal-004 failures. This demonstrates behavior on the hand-built fixtures only; it does not establish a general effect of multi-turn format or validate the checker on a broader response set.

## Run the rubric checker

```sh
uv run --no-project python projects/ch6-paired-replay/check.py
```

Fixtures live in [`checker-fixtures.jsonl`](checker-fixtures.jsonl). The checker reads ingredient-list bullets and looks for specific oatmeal, dairy, sweetener, and peanut/tree-nut terms. It does not judge nutrition claims, and it can miss violations phrased in instructions, prose, or unrecognized ingredient names. A 7/7 fixture match is not an accuracy estimate.

## Background

- [Chapter 6 study note](../../notes/2026-10-13-ch6-multiturn-conversations.md)
- [Earlier trace review](../ch6-multiturn-conversation-review/README.md)

## Chapter 6 closeout and next step

Chapter 6's planned paired replay and one controlled constraint perturbation are complete. Before Chapter 7, retrieve from memory why we compare a single-turn control with a multi-turn replay and why these one-response-per-condition pairs do not establish a general effect. For the next lesson, switch to a domain the learner knows well; recipes were only the source of visible practice constraints.
