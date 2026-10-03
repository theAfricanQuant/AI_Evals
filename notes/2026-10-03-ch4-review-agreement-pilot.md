# Chapter 4 — Review-agreement pilot

- Date: 2026-10-03
- Course links: `4. Collaborative Evaluation Practices.md`
- Source card: [course repositories audit](../sources/course-repositories-audit.md)
- Working artifact: [Recipe Bot review-agreement pilot](../projects/recipe-bot-review-agreement/)

## Question

Can a reviewer consistently check whether a Recipe Bot response uses every specific ingredient named by the user?

## Method and evidence

I wrote `rubric.md` with one binary criterion: mark Pass when every explicitly named requested ingredient appears in the recipe’s ingredients or instructions; otherwise mark Fail.

I selected ten fixed source traces in `shared-set.md` from the local Recipe Chatbot Homework 2 dataset. I reviewed them independently and recorded one Pass/Fail label plus a short reason for each trace in `reviewer-a.csv`.

Result: Reviewer A marked all 10 of 10 traces Pass.

The reproducible validation command was:

```sh
uv run python projects/recipe-bot-review-agreement/check.py
```

It confirmed 250 upstream source traces, 10 fixed shared traces, 10 Reviewer A labels, 10 Pass labels, and 0 Fail labels. It intentionally printed no IAA or Cohen's Kappa result because there is one reviewer and one label class.

## Takeaway

The rubric was easy to apply to this sample, but the pilot does not show that multiple reviewers would apply it consistently. There was only one reviewer and no Fail labels. A second reviewer agreeing on easy Pass cases would not be meaningful evidence of agreement.

Cohen’s Kappa must not be calculated for this pilot. A dataset with only one label class makes chance-adjusted agreement uninformative.

## Next retrieval

- [ ] Build a new shared set with clear Pass cases, clear Fail cases, and borderline cases.
- [ ] Ask a second human reviewer to label the new set without seeing Reviewer A’s labels.
- [ ] Measure agreement per criterion only after both independent label files exist.
