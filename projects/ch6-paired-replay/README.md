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

One manual control/replay pair has been run in Codex with GPT-6 Luna and Medium reasoning. The exact conversation is saved in [results/oatmeal-001-v1-pilot.md](results/oatmeal-001-v1-pilot.md). Treat it as an exploratory pilot: rubric v1 has an unclear boundary around optional non-calorie sweeteners, so the replay label is Review. This single pair cannot establish that multi-turn format caused a failure.

## Background

- [Chapter 6 study note](../../notes/2026-10-13-ch6-multiturn-conversations.md)
- [Earlier trace review](../ch6-multiturn-conversation-review/README.md)

## Next step

Clarify the rubric with text-only checks before running a fresh pair. Do not make nutrition or medical judgments.
