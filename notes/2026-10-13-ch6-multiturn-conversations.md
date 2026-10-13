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

- [ ] Create a small blank lab and run the paired single-turn control and multi-turn replay with the same model and tools.
- [ ] If the replay passes, perturb one passing conversation by moving or changing one user constraint, then check whether the final answer updates.
