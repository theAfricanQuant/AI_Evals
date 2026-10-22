# Chapter 6: A Small Rule-Based Checker for Oatmeal Traces

- Date: 2026-10-22
- Course links: [5. Implementing Automated Evaluators](../5.%20Implementing%20Automated%20Evaluators.md); [6. Evaluating Multi-Turn Conversations](../6.%20Evaluating%20Multi-Turn%20Conversations.md)
- Related note: [Chapter 6 multi-turn trace review](2026-10-13-ch6-multiturn-conversations.md)
- Working artifact: [paired replay checker and fixtures](../projects/ch6-paired-replay/)
- External source cards: none used for this implementation

## Question

Can a small deterministic checker catch explicit oatmeal-v3 ingredient-list violations in the latest paired replay, including the two optional non-sugar sweeteners, while leaving a clear seed-based answer as Pass?

## Method and evidence

I wrote `projects/ch6-paired-replay/check.py` to apply narrow keyword rules to bullet items under an `Ingredients` heading. It checks for an oatmeal idea, listed dairy ingredients, sweeteners named by the rubric, peanut/tree-nut ingredients, and unclear plain milk. It returns Pass, Fail, or Review. Seven fixture rows in `checker-fixtures.jsonl` include excerpts from oatmeal-003 and both oatmeal-004 responses, plus synthetic checks for a negated nut mention, a listed tree nut, dairy, and unspecified milk.

Command:

```sh
uv run --no-project python projects/ch6-paired-replay/check.py
```

Observed output:

```text
oatmeal-003-control-excerpt: expected=Pass, predicted=Pass [MATCH]
fixture-negated-nut-mention: expected=Pass, predicted=Pass [MATCH]
oatmeal-004-control-sweetener: expected=Fail, predicted=Fail [MATCH]
oatmeal-004-replay-sweetener: expected=Fail, predicted=Fail [MATCH]
fixture-tree-nut: expected=Fail, predicted=Fail [MATCH]
fixture-dairy: expected=Fail, predicted=Fail [MATCH]
fixture-unclear-milk: expected=Review, predicted=Review [MATCH]
Fixture labels matched: 7/7
```

## Takeaway

The checker catches the known stevia/monk-fruit violations and distinguishes the seed-based Pass fixture in this small, purpose-built set. The result is a behavior check against seven supplied labels, not validation of the rubric or evidence of performance on unseen model responses. The parser only inspects bullet items under a recognizable Ingredients heading; it may miss a prohibited suggestion elsewhere in a response, miss unfamiliar ingredient names, or mishandle more complex negation. Nutrition claims, product brands, cross-contact, and medical safety are outside scope. The three same-model Gemini pairs in the lab received matching labels within each pair, but one response per condition cannot support a general conclusion about single-turn versus multi-turn performance.

## Next retrieval

- [ ] From memory, explain why a control/replay pair helps isolate a multi-turn failure and why one pair cannot support a general claim; then begin Chapter 7 with a familiar domain.
