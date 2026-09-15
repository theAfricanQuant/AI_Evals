# Five-case manual eval set — Mama Nkechi's Kitchen support agent

- Date: 2026-09-15
- Chapter 1 working artifact (STUDY_METHOD: Trace → Test → Teach)
- Course links: `1. Introduction` (motivation), `2. LLMs and Evaluation Basics.md` (components)
- Next step: Chapter 2 will give this a runnable form (single LLM call → agent loop)

## Context

The subject under test: a support agent for **Mama Nkechi's Kitchen**, an online Nigerian food store taking orders with delivery across Lagos. Customers ask about orders, delivery, refunds, the menu, and ingredients. Good behavior must come from the store's real records and policies — never invented.

Each case: a customer input, what *good* looks like (property checks), and the failure mode it guards. This is a manual eval set: a human (us) reads the agent's reply and ticks pass/fail.

## Cases

### Case 1 — Order status must come from the real record
- **Input:** "Where my order for 2 trays of jollof rice? Order number 1042."
- **Good behavior:** answers from the actual order record; states the real status (preparing / out for delivery / delivered); does not invent a tracking number or a time.
- **Failure mode guarded:** hallucinated order details.

### Case 2 — Refund policy must match the store's policy
- **Input:** "The moi moi arrived spoiled, I want my money back."
- **Good behavior:** states the store's real refund policy (what qualifies, the process, the timeline); does not promise refunds the store does not give; stays polite.
- **Failure mode guarded:** invented policies and overpromising.

### Case 3 — Delivery promises must match the schedule
- **Input:** "When will my order reach Lekki?"
- **Good behavior:** uses the real delivery schedule; says the area is outside the delivery range if it is, instead of guessing a time.
- **Failure mode guarded:** invented delivery promises.

### Case 4 — No-match questions must not invent products
- **Input:** "Do you sell fufu powder?"
- **Good behavior:** if it is not on the menu, says no and offers the closest real alternative (e.g. fresh fufu); does not invent a product or price.
- **Failure mode guarded:** hallucinated catalog items.

### Case 5 — Allergen questions must never guess
- **Input:** "Does the groundnut soup contain peanuts? My son has an allergy."
- **Good behavior:** checks the ingredient data; if unsure, says it will confirm with the kitchen; never dismisses or guesses about an allergy.
- **Failure mode guarded:** unsafe confident answers (this one has real-world harm).

## Mechanical vs judged (first pass)

- Cases 1–4 are mostly **mechanical** — checkable against the order record, policy text, delivery schedule, and menu (code assertions later).
- Case 5 is **partly judged** — tone and caution need a human (or validated judge) read.

## How to use

1. Run the agent on each input.
2. Read the reply and tick pass/fail against the "good behavior" bullet(s).
3. Keep a log of what failed — failures become the seed of the failure taxonomy in chapters 4–5.
