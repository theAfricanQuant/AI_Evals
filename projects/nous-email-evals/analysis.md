
# Provisional analysis — Nous email traces

## Question

What failure patterns appear in the initial Nous email-summarizer traces, and is the callback-number requirement reliable at max_tokens=320?

## Evidence

- Trace 001: the sender appeared as `Sender: Ada`, after two bullets.
- Trace 002: the one-request email produced one problem bullet and one request bullet.
- Trace 003: the same callback-number email returned `None`.
- Trace 004: retrying produced text but omitted `0803 555 0142`.

## Provisional categories

- Specification ambiguity: the prompt does not define the sender format or what to do with a one-request email.
- Specification gap: the prompt does not say callback numbers must be preserved.
- Runtime uncertainty: one request returned no text. The client currently lacks response metadata needed to diagnose why.

## Decision not made yet

Do not call any of these a pass or failure until we choose the expected behavior.


## Product decision

When a support email includes a callback phone number, the summary must retain the same phone-number digits. Spacing or punctuation may differ.


## Reliability test plan

Test the current configuration three times in a row:

- Prompt: original prompt, without the phone-number instruction.
- Model: deepseek/deepseek-v4.1-flash.
- Token limit: 320.
- Input: Amina’s callback-number email.

A run passes only when:

1. the output is not `None`; and
2. it contains the digits `08035550142`, ignoring spaces or punctuation.

Report the total as passed runs out of 3.

## Reliability result

The current configuration passed 2 of 3 planned trials (66.7%).

- Trials 1 and 2 retained the callback-number digits.
- Trial 3 omitted them and ended mid-sentence.

Conclusion: `max_tokens=320` improved the earlier empty completions, but this configuration does not yet preserve callback numbers reliably.
