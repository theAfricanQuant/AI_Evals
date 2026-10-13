# LLMs Get Lost in Multi-Turn Conversation

- Source: [arXiv:2505.06120](https://arxiv.org/abs/2505.06120); [ICLR 2026 proceedings](https://proceedings.iclr.cc/paper_files/paper/2026/hash/59f6421e64707225fdf5b28840679a07-Abstract-Conference.html)
- Type: paper
- Accessed: 2026-10-13
- Course links: [6. Evaluating Multi-Turn Conversations](../6.%20Evaluating%20Multi-Turn%20Conversations.md)

## What it contributes

- **Authors' claim:** Their simulations compare single-turn and multi-turn conditions across six generation tasks. They report an average performance drop of 39% across those tasks and analyze more than 200,000 simulated conversations.
- **Authors' claim:** They separate the loss into a smaller decline in task aptitude and a larger increase in unreliability. Their analysis points to early assumptions and weak recovery after an incorrect conversational turn.
- **Scope:** These findings describe the paper's chosen models, tasks, and simulation setup. The 39% figure is not a universal estimate for every deployed assistant.

## Use in this knowledge base

This paper supports Chapter 6's focus on measuring full conversations. It motivates testing whether an assistant incorporates information added later, and comparing a failed dialogue with a single prompt that includes the same information.

## Questions to test

- When a conversational session fails, does the failure remain when all user information is supplied in one turn?
- When a passing dialogue is perturbed with a changed preference or correction, does the assistant update its final answer?
