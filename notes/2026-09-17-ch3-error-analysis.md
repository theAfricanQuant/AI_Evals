# Chapter 3 — Error Analysis

- Date: 2026-09-17
- Course links: `3. Error Analysis.md`; bridge to `4. Collaborative Evaluation Practices.md` and `5. Implementing Automated Evaluators.md`
- Source cards: [course repositories audit](../sources/course-repositories-audit.md); [Who Validates the Validators?](../sources/who-validates-the-validators.md)

## Question

For a recipe chatbot, which first failures recur in a small, diverse trace sample, and which of them are specific enough to become future binary evaluators?

## Method and evidence

Used the local Recipe Chatbot Homework 2 dataset, `references/recipe-chatbot/homeworks/hw2/reference_files/query_response.jsonl`. Rather than copy the 250 source pairs, the new working artifact at `projects/recipe-bot-error-analysis/` stores a fixed 20-ID sample and reads the source JSONL in place.

The selection takes one ID from each successive five-query synthetic cluster between `SYN001` and `SYN096`. It covers dietary, religious, and health constraints; time and effort requests; pantry claims; cuisines; and food safety. Each query/response pair is a single-turn trace: the original query and the final response.

I first made a binary acceptable/unacceptable decision and wrote one freeform open code for the earliest observed failure in each unacceptable trace. Only after that did I perform axial coding. The decision rule was: mark a trace unacceptable when its first problem breaks a stated user constraint, makes a safety-sensitive claim without a check, or promises a time/pantry property its instructions do not support. Assign one first failure only, so downstream effects do not inflate the count.

Command:

```sh
uv run python projects/recipe-bot-error-analysis/analyze.py
```

Result:

```text
Source traces available: 250
Fixed review sample: 20 traces
Acceptable: 7
Unacceptable: 13

unverified_restriction: 4/20 (20%)
unsupported_time_claim: 4/20 (20%)
pantry_claim_mismatch: 2/20 (10%)
missing_serving_context: 2/20 (10%)
missing_safety_guidance: 1/20 (5%)
```

The four `unverified_restriction` traces cover low-FODMAP, low-sodium, kosher, and halal requests. The response uses the claimed label without a concrete verification rule: for example, it shifts FODMAP checking to the user or assumes ingredients are kosher/halal. The four `unsupported_time_claim` traces call a recipe fast, quick, or 45 minutes even though the stated steps either omit a total time or exceed it.

## Takeaway

This 20-trace practice slice suggests two candidate failure modes worth formalizing first: **unverified user constraints** and **unsupported time claims**. They each appear in 4 of 20 traces, but frequency is not the only priority: dietary, religious, health, and food-safety constraints can be high-impact even when rare.

The conclusion is deliberately bounded. The dataset is synthetic, the traces are single-turn, and 20 traces are not enough to claim theoretical saturation or to describe a deployed product. It is strong enough to practice the Chapter 3 sequence: inspect traces → open-code first failures → form a taxonomy → count it.

## Next retrieval

- [ ] Chapter 4: write a binary pass/fail rubric for `unverified_restriction`, then have two reviewers label the same 10 traces and compare disagreements.
- [ ] Turn `unsupported_time_claim` into a candidate evaluator only after defining how preparation, resting, and optional steps count toward total time.
