# Chapter 2 — LLMs and evaluation basics

- Date: 2026-09-15
- Course links: `2. LLMs and Evaluation Basics.md` (baseline, full text read)
- Source cards: none new (book chapter itself); context: `sources/hamel-your-ai-product-needs-evals.md`
- Working artifact: `projects/email-summarizer/` — runnable, offline, no API keys

## Question

What makes up an LLM application, and how do the two evaluation modes (absolute vs comparative) tell us what to build and how to measure it?

## Method and evidence

Read the chapter in full (593 lines). Built `projects/email-summarizer/`: the book's email-summarizer prompt template (Example 2-1), a 5-email test set, and `check.py` — 4 deterministic reference-free checks (Sender line present, exactly 3 bullets, no verbatim quoting, phone number handled).

Real run: `python3 check.py` → **9/12 checks passed, 3 failed as designed** (bug 1: missing Sender + 2 bullets; bug 2: phone in email ignored by summary).

**The Test step caught a criteria bug:** the first phone-detection regex `\d{3}[-.)\s]\d{3}[-.)\s]\d{4}` missed the common format "(415) 555-9021" (space after the area-code paren). Fix: allow optional spaces after each separator (`\s*`). Lesson: reference-free criteria look simple but have blind spots — run them on representative inputs before trusting them.

## Key ideas

1. **The components ladder** (each adds capability + its own failure modes): single-step LLM call → conversation (multi-turn) → retrieval (RAG) → tools → agent loop. An agent is just repeated LLM calls where the model decides each step (ReAct: Thought → Action → Observation); always cap steps.
2. **Messages**: `role` (system = rulebook, user = query, assistant = history, tool = tool results). Debugging tip: alternating user/assistant roles must be correct.
3. **Retrieval**: start with keyword search (BM25) — interpretable, transparent, often enough; move to embeddings when it misses semantic matches.
4. **Tools**: Python functions described to the model via OpenAPI-style specs (name, description, JSON-schema args — be precise about edge cases). MCP standardizes tool servers. Warning: tools mean real actions — validate inputs.
5. **Prompt templates**: role, objective, instructions, context, reasoning, output format, examples, delimiters. Store templates as files/config for versioning.
6. **Two evaluation modes**:
   - *Absolute* — "is this good enough to ship?" Reference-based (gold labels; expensive; penalizes valid alternative answers; only when one correct answer) vs **reference-free (the book's focus)** — criteria checks: format, completeness, factuality; rules or LLM judge.
   - *Comparative* — "which is better?" Pairwise comparisons, ranking/leaderboards (e.g. LMArena); closer to A/B testing; only worth it once one config works.
7. **Ambiguity policy is a design choice** you must make explicit in the prompt: "ask to clarify" (cautious) vs "infer and continue" (autonomous) — makes behavior predictable and evaluable.

## Takeaway

Before you can evaluate, you must know your application's components — each one (call, conversation, retrieval, tool, loop) has characteristic failure modes you will later name in error analysis. The practical evaluation engine is **absolute, reference-free checking**: define criteria, check outputs against them, no gold labels needed. Mechanical criteria → code assertions (what `check.py` does); subjective criteria → judged evals (later chapters).

## Next retrieval

- [ ] Chapter 3: systematic error analysis — specification failures (unclear/incomplete prompt) vs generalization failures (model inconsistent despite clear instructions).
- [ ] Extend `check.py`'s criteria to the judgment cases (case-04: one-request email vs "exactly 3 bullets"; case-05: vague input vs ambiguity policy).
- [ ] First pass marking each criterion mechanical vs judged, per the chapter 1 rule.
