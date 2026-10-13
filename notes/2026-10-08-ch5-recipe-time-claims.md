# Chapter 5: Checking Recipe Time Claims

- Date: 2026-10-08
- Course link: [5. Implementing Automated Evaluators](../5.%20Implementing%20Automated%20Evaluators.md)
- Working artifact: [Recipe Bot time evaluator](../projects/recipe-bot-time-evaluator/)
- Trace source: [`query_response.jsonl`](../references/recipe-chatbot/homeworks/hw2/reference_files/query_response.jsonl), a course homework dataset of synthetic examples

## Question

Can a deterministic evaluator distinguish clear time-limit failures from cases that need human review?

## Method and evidence

We wrote a rubric for numeric time limits, vague requests, required steps, parallel work, and pre-prepared ingredients. The checker consumes structured reviewer annotations; it does not parse recipe text.

The owner reviewed six course-provided traces. Five were labeled Review because the query was vague or required recipe durations were missing. For SYN069, the request allowed 30–60 minutes. The response required urad dal to soak for at least 60 minutes, pressure cook for at least 15 minutes, and simmer for at least 15 minutes after cooking. Masala preparation overlaps with pressure cooking, so the known required minimum is still 90 minutes. The owner labeled it Fail. Natural pressure release adds unstated time, but it cannot bring the known minimum within the 60-minute cap.

In a follow-up review, the owner revisited SYN031. Quinoa simmers for about 15 minutes and rests for 5; beans cook in parallel. Prep, bringing the quinoa to a boil, and assembly times are unstated. The evidence does not prove that the recipe fits the 30-minute limit or that it exceeds it, so Review remains the supported label.

The three synthetic fixtures cover Pass, Fail, and Review. After adding SYN069 and its known-minimum rule, the owner ran:

```sh
uv run python projects/recipe-bot-time-evaluator/check.py
```

Observed output: all nine case labels matched (SYN018, SYN025, three synthetic fixtures, SYN023, SYN017, SYN031, and SYN069). SYN069 predicted Fail; SYN031 and the other uncertain cases predicted Review. This checks that the code applies the supplied annotations consistently. It does not verify that the human timing annotations are correct.

## Key ideas

- Missing timing detail calls for Review only when it could change the classification.
- A known lower bound can prove a recipe exceeds its cap, even when the full total is unknown.
- When steps overlap, count elapsed time rather than adding every step duration.
- A deterministic checker can apply structured annotations consistently, but a human still has to interpret the recipe and provide trustworthy annotations.

## Takeaway

SYN069 is a clear Fail because its minimum known duration is 90 minutes against a 60-minute maximum. The example improves the rubric by separating uncertainty from evidence that already proves failure.

## Next retrieval

- [x] Run the updated checker: all 9/9 expected labels matched, including SYN069 as Fail.
- [x] Revisit SYN031: overlapping bean cooking and missing prep, heating, and assembly times leave the result uncertain, so Review is appropriate.
- [ ] Begin Chapter 6, “Evaluating Multi-Turn Conversations,” by retrieving the Chapter 5 decision rule from memory before reading the next lesson.
