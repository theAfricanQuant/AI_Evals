# Nous email-evals scaffold

- Date: 2026-09-24
- Course links: `2. LLMs and Evaluation Basics.md`
- Source cards: [Nous Research Inference API](../sources/nous-inference-api.md)
- Working artifact: [`projects/nous-email-evals/`](../projects/nous-email-evals/)

## Question

How can a learner create a reproducible first live email-summarizer lab using a Nous API key, without putting a secret or an OpenAI dependency into the repository?

## Method and evidence

The learner created `projects/nous-email-evals/`, ran `uv init --bare`, and ran `uv add httpx`. The resulting `pyproject.toml` declares `httpx`; `uv.lock` records the resolved dependency versions. No API key was supplied to this workspace, and no model request was made.

The planned client contract is direct HTTPS: bearer authentication with `NOUS_API_KEY`, base URL `https://inference-api.nousresearch.com/v1`, and a `NOUS_MODEL` value copied from the owner's current Nous Portal catalog. The first program will call `/chat/completions` with one fixed support email and print the untouched answer.

## Takeaway

The scaffold is reproducible but not yet an evaluation. It becomes evidence only when it saves a real input, the exact non-secret model configuration, and the resulting output. Until then, there is no pass rate to report.

## Next retrieval

- [ ] Set the two environment variables in the terminal only; do not send or save the key.
- [ ] Type `main.py`, run one fixed email through Nous, and return the output with the key removed.
- [ ] Save that output as the first trace, then decide which requirement is mechanical enough to check.
