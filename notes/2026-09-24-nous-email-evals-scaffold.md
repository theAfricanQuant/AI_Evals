# Nous email-evals scaffold and first trace

- Date: 2026-09-24
- Course links: `2. LLMs and Evaluation Basics.md`
- Source cards: [Nous Research Inference API](../sources/nous-inference-api.md)
- Working artifact: [`projects/nous-email-evals/`](../projects/nous-email-evals/)

## Question

How can a learner create a reproducible first live email-summarizer lab using a Nous API key, without putting a secret or an OpenAI dependency into the repository?

## Method and evidence

The learner created `projects/nous-email-evals/`, ran `uv init --bare`, and ran `uv add httpx`. The resulting `pyproject.toml` declares `httpx`; `uv.lock` records the resolved dependency versions. The learner then added Ruff as a development dependency and ran `uv run ruff format main.py`, which reformatted the first client program.

The client uses direct HTTPS: bearer authentication with terminal-only `NOUS_API_KEY`, base URL `https://inference-api.nousresearch.com/v1`, and a `NOUS_MODEL` value copied from the owner's current Nous Portal catalog. `main.py` called `/chat/completions` once using `deepseek/deepseek-v4.1-flash`, the fixed Ada locked-account email, and `max_tokens=160`. The saved result is [`traces/trace-001.md`](../projects/nous-email-evals/traces/trace-001.md). It named Ada and captured both her reset and sign-in-update requests. No API key is present in the project, note, trace, or report.

## Takeaway

The scaffold is now a reproducible first trace, but not yet an evaluation. One output shows that the request works; it cannot establish reliability, a pass rate, or a release gate. The output puts the sender after the bullets, which is a candidate format decision to make explicit before testing.

## Next retrieval

- [ ] Create four new, deliberately different support emails; do not reuse the existing offline test set as if it were a live result.
- [ ] Write the first binary decision rule before running them—for example, whether every output must contain a `Sender:` line.
- [ ] Run the same prompt and model on all five cases, save the traces, and inspect failures before writing a check.
