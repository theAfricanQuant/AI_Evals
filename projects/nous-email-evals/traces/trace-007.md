# Trace 007 — higher token limit preserved callback number

- Date: 2026-09-29
- Model: deepseek/deepseek-v4.1-flash
- Endpoint: https://inference-api.nousresearch.com/v1/chat/completions
- Request settings: max_tokens=320

## Prompt

Summarize the email in two short bullet points. Name the sender.
If the email includes a callback phone number, preserve all its digits
in the summary.

## Input

Hello support team,
My account is still locked.
Please reset it and call me on 0803 555 0142 when I can log in.
Thanks, Amina

## Output

- Amina reports her account is still locked and asks support to reset it.
- She asks to be called at 0803 555 0142 once she can log in.

## Result

This one run satisfies the callback-number requirement.
