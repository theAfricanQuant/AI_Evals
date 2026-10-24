# 2026-10-24 — AI governance from law to runtime

**Question.** What is "runtime governance for AI systems", why did it appear, who has implemented it, and how much evaluation does it actually require?

**Takeaway.** Runtime governance is the control layer that inspects an AI interaction while it is happening — identity, policy, redaction, blocking, action limits — and records what happened so a third party can reconstruct it. Evaluation supplies the quality evidence; it is not the control itself. Policy tools say what should happen; runtime tools prove what did happen.

**Artifact.** `reports/generated/lecture-ai-governance-runtime-evals-2026-10-24.html` — a 12-chapter lecture with a four-week study plan, a 39-term glossary, and a referenced reading list. Built from `build/governance/part1–6.html` with `build/governance/build.py`. Diagrams: origins timeline, AI Act decision path, request path, and three time scales.

**What it connects to the course.** Chapter 8 is the bridge: evals answer "is it good?"; governance answers "is it allowed, and can we prove it?" The four contact points are the release gate, guardrail calibration, online sampling, and post-market monitoring (AI Act Articles 15 and 72). The precision/base-rate arithmetic is the reason audit mode precedes blocking.

**Evidence and limits.** Legal dates and article numbers were checked against the official texts and the AI Act Service Desk in October 2026; the 2026 omnibus moved several high-risk deadlines, so verify before advising. Company figures come from interviews or a vendor case study and are labelled as such. The eval thresholds are illustrative, not benchmark results. Nothing here is legal advice.

**Next task.** Apply the Chapter 9 file to one real system (Job Seeker Studio): write the system card, classify it under the AI Act, and draft the five-row risk register before building the eval plan.
