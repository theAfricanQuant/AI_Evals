# Chapter 5: A Code-Based Ingredient-Presence Evaluator

- Date: 2026-10-06
- Course link: [5. Implementing Automated Evaluators](../5.%20Implementing%20Automated%20Evaluators.md)
- Working artifact: [Recipe Bot ingredient evaluator](../projects/recipe-bot-automated-evaluator/)

## Question

Can a code-based evaluator detect when a recipe leaves out an ingredient the user explicitly requested?

## Method and evidence

The evaluator reads `cases.jsonl`. For the two real Recipe Bot cases, it looks up each response by trace ID in `references/recipe-chatbot/homeworks/hw2/reference_files/query_response.jsonl`. A synthetic fixture carries its own response. The reviewer records a canonical `requested_ingredients` list for each case; the script lowercases the response and checks whether each ingredient string occurs in it. This prototype exercises Chapter 5 implementation mechanics only; it does not lift Chapter 4's decision to wait for a second reviewer and balanced human labels before operationalizing this rubric.

Command run from the repository root:

```sh
uv run python projects/recipe-bot-automated-evaluator/check.py
```

Observed result: `SYN025` Pass/Pass, `SYN031` Pass/Pass, and `fixture-001` Fail/Fail. The fixture correctly reported `salmon` missing. All three case labels matched.

The `SYN031` query asks for “avocados”; the recipe uses a singular avocado. The owner judged this a Pass because no quantity was specified. The case stores the canonical ingredient as `avocado`.

## Key ideas

- Ingredient presence is an objective, narrow criterion, so a small deterministic code check is a reasonable first evaluator. An LLM judge would add cost and variability without helping this string-presence task.
- The script checks a structured ingredient list supplied by a person. It does not extract ingredients from free-form requests.
- Matching is case-insensitive substring search. It does not handle synonyms or all wording variations, and a substring can match the wrong word in some cases.
- Two real Pass cases plus one synthetic Fail fixture can show that this implementation follows those examples. They cannot estimate real Recipe Bot failure prevalence or establish rubric agreement.

## Takeaway

A code check is useful when the criterion can be expressed as a direct rule, but its result is only as broad as the structured inputs and text-matching rule it uses.

## Next retrieval

- [ ] Explain why the ingredient-presence rule is a better fit for code than an LLM judge, and name one false positive or false negative the substring check could make.
