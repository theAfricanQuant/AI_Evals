# Chapter 7 generation check — synthetic case

Question: How many days is the standard validity period?

Faithfulness: Is the answer supported by the retrieved context?
Relevance: Does the answer address the question?

## Case A — 16-word chunks, no overlap

Retrieved context:
- The Demo Mobile account lists the standard monthly bundle in Plan Details. Its standard validity period
- billing date appears under Plan Details. Travel passes have a separate seven-day validity period and do

Candidate answer: The standard validity period is seven days.

Faithfulness: Fail
Relevance: Pass
Reason:  The answer addresses the duration question, but the retrieved text says seven days applies to travel passes, not the standard bundle.

## Case B — 16-word chunks, 4-word overlap

Retrieved context:
- Its standard validity period is thirty days from activation. Any unused data expires with the bundle

Candidate answer: The standard validity period is thirty days from activation.

Faithfulness: Pass
Relevance: Pass
Reason: The retrieved context says the standard validity period is thirty days from activation, and the answer states that.
