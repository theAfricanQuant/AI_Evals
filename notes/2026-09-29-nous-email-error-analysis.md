# Nous email error analysis: callback-number reliability

- Date: 2026-09-29
- Course links: `3. Error Analysis.md`; builds on `2. LLMs and Evaluation Basics.md`
- Source cards: [Nous Research Inference API](../sources/nous-inference-api.md)
- Working artifact: [`projects/nous-email-evals/`](../projects/nous-email-evals/)

## Question

What failure patterns appear in the first Nous email-summarizer traces, and does the current configuration reliably preserve a callback number from a support email?

## Method and evidence

The learner first read the saved traces rather than choosing a generic metric. The early probes exposed three observations: sender formatting changed between traces, a one-request email used one bullet for the problem and one for the request, and the Amina callback-number email either returned `None` or omitted `0803 555 0142`.

The learner made one product decision before the reliability trial: when an email includes a callback number, the summary must retain the same digits; spaces and punctuation may differ. This converts a vague concern into a binary rule.

The first `None` response was not guessed at. The client was changed to print safe metadata when content is missing. On the next empty result, `finish_reason` was `length` at `max_tokens=160`. Raising `max_tokens` to 320 produced a readable output that preserved the number. A one-run comparison with the original prompt at 320 also preserved it, so the evidence does not show that the extra phone-number instruction alone caused the improvement.

Finally, before reading new outputs, the learner wrote a three-run plan: original prompt, `deepseek/deepseek-v4.1-flash`, `max_tokens=320`, and the same Amina email. A run passes only when it has non-empty text and contains `08035550142` after punctuation is ignored. The saved trials are [`trace-009.md`](../projects/nous-email-evals/traces/trace-009.md), [`trace-010.md`](../projects/nous-email-evals/traces/trace-010.md), and [`trace-011.md`](../projects/nous-email-evals/traces/trace-011.md): two passed and the third failed by ending at “call her at” without the digits.

## Takeaway

The current configuration passed 2 of 3 planned trials (66.7%). It is therefore not reliable enough to claim that callback numbers are consistently preserved. The small sample does not establish a production pass rate, but it does identify two concrete failure modes to investigate: output truncation/empty completion and omitted callback details. The trace record distinguishes those observed facts from guesses about their cause.

## Next retrieval

- [ ] Change the client to record `finish_reason` for every response, not only empty ones; this will tell us whether incomplete visible text is also token-limit truncation.
- [ ] Add deliberately varied traces (quoted thread, vague sender, and different phone formats) before treating the callback rule as an automated release gate.
- [ ] Open-code the next trace batch before choosing a second evaluator rule.
