import os
import sys

import httpx

BASE_URL = "https://inference-api.nousresearch.com/v1"

api_key = os.environ.get("NOUS_API_KEY")
model = os.environ.get("NOUS_MODEL")
if not api_key or not model:
    raise SystemExit("Set NOUS_API_KEY and NOUS_MODEL in this terminal first.")

email = """Hello support team,
My account is still locked.
Please reset it and call me on 0803 555 0142 when I can log in.
Thanks, Amina"""

payload = {
    "model": model,
    "messages": [
        {
            "role": "system",
            "content": (
                "Summarize the email in two short bullet points. Name the sender."
            ),
        },
        {"role": "user", "content": email},
    ],
    "max_tokens": 320,
}

try:
    response = httpx.post(
        f"{BASE_URL}/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json=payload,
        timeout=60,
    )
    response.raise_for_status()
except httpx.HTTPStatusError as error:
    print(f"Nous returned HTTP {error.response.status_code}", file=sys.stderr)
    print(error.response.text, file=sys.stderr)
    raise SystemExit(1)
except httpx.RequestError as error:
    raise SystemExit(f"Could not reach Nous: {error}")

body = response.json()
choice = body["choices"][0]
message = choice["message"]
answer = message.get("content")

print(f"MODEL: {model}")
print("\n--- RAW MODEL OUTPUT ---")
print(answer)

if answer is None:
    print("\n--- RESPONSE METADATA ---")
    print(f"finish_reason: {choice.get('finish_reason')}")
    print(f"message keys: {', '.join(message.keys())}")
