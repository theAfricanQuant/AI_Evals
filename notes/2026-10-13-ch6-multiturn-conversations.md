# Chapter 6: Evaluating Multi-Turn Conversations

- Date: 2026-10-13
- Course link: [6. Evaluating Multi-Turn Conversations](../6.%20Evaluating%20Multi-Turn%20Conversations.md)
- Source card: [Laban et al., “LLMs Get Lost in Multi-Turn Conversation”](../sources/laban-et-al-llms-get-lost-in-multi-turn-conversation.md)
- Working artifact: [Chapter 6 trace review](../projects/ch6-multiturn-conversation-review/)

## Question

Did the assistant complete the user's goal after the user supplied dietary constraints in a later turn, and what evidence would show whether the failure is truly multi-turn?

## Method and evidence

We set a session-level rule before reviewing one Recipe Chatbot Homework 5 trace: Pass requires a usable oatmeal breakfast suggestion that respects the user's lactose intolerance and low-sugar preference by the end of the session. If no suggestion is given, the session is Fail.

The source trace (`000e4b33-6c6d-42c7-9903-9d39e4940112`) shows the assistant asking about dietary constraints after a recipe-generation error. The user supplies both constraints. The assistant acknowledges them but provides no recommendation. The session is therefore Fail under the stated rule. The dataset separately labels `GenRecipeArgs` as the first failed pipeline state; this is turn-level diagnostic metadata, not a session-level label.

Reproduce the lookup from the repository root:

```sh
jq -c 'select(.conversation_id == "000e4b33-6c6d-42c7-9903-9d39e4940112")' references/recipe-chatbot/homeworks/hw5/reference_files/labeled_traces.jsonl
```

The command returned the one trace and its `GenRecipeArgs` annotation. This manual review did not run a model. To separate a single-turn problem from a multi-turn one, the next experiment is to compare a prompt containing all constraints at once with the same request spread across two turns, holding model and tool setup constant.

## Takeaway

Start with the session question: did the user reach the goal? Use turn and pipeline details to locate the failure, then replay the failed turn with all relevant context in one message. This trace fails at the session level, but its root cause remains untested.

## Next retrieval

- [x] Create a small lab and run paired single-turn controls and multi-turn replays with the same model within each pair.
- [x] Perturb a passing conversation with a later constraint and test whether the assistant updates its answer.
- [x] Build a small rule-based checker for explicit final-answer constraints and record its limits.

## Chapter 6 follow-up — 2026-10-22

The paired replay lab now contains three Gemini 3.8 comparisons under clarified text-only rubrics: oatmeal-002 was Pass/Pass, oatmeal-003 was Pass/Pass after adding peanut-free and tree-nut-free constraints, and oatmeal-004 was Fail/Fail because both answers offered stevia or monk-fruit despite the low-sugar rule. The earlier GPT-6 Luna pilot is retained separately because its model and rubric differed. Each condition was sampled once. Since the paired conditions received the same label in these small comparisons, the results show no observed difference between the formats here; they do not establish that multi-turn context is harmless or identify the cause of the original Recipe Chatbot trace failure.

The oatmeal-v3 checker matched all seven hand-built fixtures, including excerpts from both oatmeal-004 failures. It is an observable implementation exercise, not a validated evaluator: it only checks terms in recognizable ingredient-list bullets and may miss violations elsewhere or language it does not recognize. Recipe content was a convenient source of visible constraints; the course skill practiced was isolating and evaluating multi-turn behavior.

Chapter 6 is complete for this study pass. The next retrieval is to explain, from memory, how a paired single-turn control helps investigate a multi-turn failure, and why one pair cannot support a general conclusion. Then begin [Chapter 7: Evaluating Retrieval-Augmented Generation](../7.%20Evaluating%20Retrieval-Augmented%20Generation.md) using a domain the learner knows well.
