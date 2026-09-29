# Trace 008 — original prompt preserved callback number at 320 tokens

- Date: 2026-09-29
- Model: deepseek/deepseek-v4.1-flash
- Endpoint: https://inference-api.nousresearch.com/v1/chat/completions
- Request settings: max_tokens=320

## Prompt

Summarize the email in two short bullet points. Name the sender.

## Input

Hello support team,
My account is still locked.
Please reset it and call me on 0803 555 0142 when I can log in.
Thanks, Amina

## Output

- Amina reports her account is still locked and asks support to reset it.
- She requests a call at 0803 555 0142 once she can log in.

Sender

## Observation

The callback number was preserved without the phone-number instruction.
One comparison is not enough to prove why; run-to-run variation remains.
