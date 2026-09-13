# Study method: trace, test, teach

Use this loop for every topic. It converts a large collection of sources into reusable evaluation practice rather than a pile of summaries.

## Folder map

- `AI Evals For Engineers & PMs — Syllabus.md` and `1.`–`12.` lesson files: course baseline.
- `sources/`: compact source cards for material outside the course.
- `notes/`: dated learning sessions and retrieval notes.
- `projects/`: optional runnable exercises, datasets, traces, or evaluator code. Each project begins with a `README.md` that links to its study note.

## 60–90 minute loop

### 1. Trace — frame one evaluable question (5 minutes)

Choose one lesson and write a question that would change an engineering decision. Good examples:

- “How do I measure whether this tool-call router selects the correct tool?”
- “Which failures should be deterministic assertions versus judged evaluations?”
- “What regression gate is justified for this agent before deployment?”

Locate the relevant numbered lesson first. Then consult one external source only when it adds a concrete method, example, or counterexample.

### 2. Capture — create or update a source card (10 minutes)

For a new source, create `sources/<slug>.md` using this template:

```md
# <Source title>

- Source: <URL or stable ID>
- Type: <paper | video | article | repository | NotebookLM>
- Accessed: YYYY-MM-DD
- Course links: <lesson filenames>

## What it contributes

<2–5 grounded claims or techniques, each clearly distinct from your interpretation.>

## Use in this knowledge base

<Which decision, exercise, or evaluator it improves.>

## Questions to test

- <A question that can be answered with data, a trace, or an implementation.>
```

For NotebookLM material, capture the notebook URL and the titles of the particular sources used; do not copy its underlying source text wholesale.

### 3. Test — make a smallest useful artifact (25–40 minutes)

Turn the question into evidence. Pick the cheapest method that can disprove your current belief:

| If studying | Create |
| --- | --- |
| A deterministic behavior | A small input/expected-output test set and code assertion |
| A judgment call | A rubric, 10–20 labeled examples, and agreement check |
| An agent failure | A trace slice, failure taxonomy entry, and a binary evaluator candidate |
| A proposed improvement | A frozen baseline and variant measured on the same held-out cases |
| Reliability or cost | Repeated runs with a recorded budget, pass-rate, latency, and failure count |

Name the artifact, retain its inputs, and state the decision rule before reading the result. A result without a predeclared decision rule is an observation, not an evaluation.

### 4. Teach — write a dated study note (10–15 minutes)

Create `notes/YYYY-MM-DD-<topic>.md`:

```md
# <Topic>

- Date: YYYY-MM-DD
- Course links: <lesson filenames>
- Source cards: <relative links>

## Question

<One decision-relevant question.>

## Method and evidence

<Dataset/trace, evaluator, run conditions, and result.>

## Takeaway

<A falsifiable conclusion and its boundary.>

## Next retrieval

- [ ] <Smallest next query, experiment, or implementation step.>
```

Write from the evidence upward: method and result first, conclusion second. Link to the source card instead of repeating its summary.

### 5. Review — retrieve before advancing (5–10 minutes)

At the start of the next session, answer from memory:

1. What exact behavior was evaluated?
2. What made the evaluator trustworthy enough for its decision?
3. What failure did it miss or leave uncertain?
4. What would change the conclusion?

Correct the prior study note only when the evidence changes; add a dated follow-up when your understanding changes.

## Course cadence

Study the existing sequence in four passes:

1. **Foundations (Lessons 1–3):** define scope, traces, and scenarios.
2. **Measurement (Lessons 4–5):** make a failure taxonomy and validate evaluators.
3. **Operations (Lessons 6–7):** create regression gates, monitoring, and adversarial tests.
4. **Improvement (Lessons 8–9):** compare variants on a held-out suite and track accuracy/cost trade-offs.

Finish each pass with one working artifact. Avoid advancing on summaries alone.
