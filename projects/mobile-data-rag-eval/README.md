# Synthetic mobile-support RAG evaluation lab

This Chapter 7 practice lab uses fictional mobile-support text to explore retrieval ranking, chunking, and answer grounding. It contains no real customer data and makes no model or API calls.

## Files

- `corpus.md` and `eval_cases.md`: four synthetic FAQ passages and three queries with expected source documents.
- `retrieval_baseline.py`: shared-word ranking with Recall@1, Recall@2, Precision@2, and MRR.
- `chunking_source.md` and `chunking_case.md`: a longer synthetic article and its evidence sentence.
- `chunking_experiment.py`: compares fixed-size word chunks with different overlap settings and checks whether the full evidence sentence is retrieved.
- `generation_eval.md`: hand-written answer examples labeled for faithfulness and relevance.

## Reproduce

Run from the repository root:

`uv run --no-project python projects/mobile-data-rag-eval/retrieval_baseline.py`

`uv run --no-project python projects/mobile-data-rag-eval/chunking_experiment.py`

## Observed results

The three-query baseline returned Recall@1 = 0.67, Recall@2 = 1.00, Precision@2 = 0.50, and MRR = 0.83. On the chunking query, 16-word chunks without overlap did not return the complete evidence in the top two; 16-word chunks with 4-word overlap and 24-word chunks without overlap returned it in the top result.

## Limits and next step

This is a tiny synthetic exercise using whitespace word counts and lexical overlap, not a production RAG evaluation. The generation examples are manually authored, not model outputs. Next, add graded relevance judgments and calculate NDCG@2.

See the [dated study note](../../notes/2026-10-28-ch7-rag-retrieval-chunking.md), [Chapter 7 report](../../reports/generated/ch07-ex01-rag-retrieval-chunking-2026-10-28.html), and the [Chapter 7 lesson](../../7.%20Evaluating%20Retrieval-Augmented%20Generation.md).
