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

The three synthetic fixtures cover Pass, Fail, and Review. Before SYN069 was added, the owner ran:

```sh
uv run --no-project python projects/recipe-bot-time-evaluator/check.py
```

Observed result at that point: all eight existing labels matched (5/5 original cases plus SYN023, SYN017, and SYN031). After the SYN069 label was added, the checker was updated so a known minimum over the cap yields Fail even when other durations are missing. The updated checker has not yet been run.

## Key ideas

- Missing timing detail calls for Review only when it could change the classification.
- A known lower bound can prove a recipe exceeds its cap, even when the full total is unknown.
- When steps overlap, count elapsed time rather than adding every step duration.
- A deterministic checker can apply structured annotations consistently, but a human still has to interpret the recipe and provide trustworthy annotations.

## Takeaway

SYN069 is a clear Fail because its minimum known duration is 90 minutes against a 60-minute maximum. The example improves the rubric by separating uncertainty from evidence that already proves failure.

## Next retrieval

- [ ] Run the updated checker and confirm that SYN069 is Fail while uncertain cases remain Review.
- [ ] Review another timed trace with overlapping steps and decide whether its known minimum or a complete estimate supports Pass or Fail.
