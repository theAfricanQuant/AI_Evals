# Chapter 7: Retrieval and Chunking Pilot

- Date: 2026-10-28
- Course links: [Chapter 7: Evaluating Retrieval-Augmented Generation](../7.%20Evaluating%20Retrieval-Augmented%20Generation.md)
- Source cards: None; this session used the course lesson and a fully synthetic practice corpus.

## Question

How do simple lexical retrieval and chunk boundaries affect whether a RAG system receives complete evidence for a mobile-support question?

## Method and evidence

The owner created a fictional mobile-support corpus, three labeled retrieval queries, and one longer article for a chunking comparison in [the lab](../projects/mobile-data-rag-eval/). The retrieval baseline ranks documents by shared words. It was run with:

`uv run --no-project python projects/mobile-data-rag-eval/retrieval_baseline.py`

On the three-query set, Recall@1 was 2/3 = 0.67, Recall@2 was 3/3 = 1.00, Precision@2 was 0.50, and MRR was 0.83. Q3 ranked the related billing-date document ahead of the gold rollover document; the gold document appeared at rank 2.

The chunking comparison used a fixed question and three word-based settings: 16 words with no overlap, 16 words with 4-word overlap, and 24 words with no overlap. The command was:

`uv run --no-project python projects/mobile-data-rag-eval/chunking_experiment.py`

The complete evidence sentence was absent from the top two retrieved chunks at 16 words with no overlap. It appeared in the top result with 16 words and 4-word overlap, and with 24 words and no overlap. The owner also labeled two hand-written answer fixtures: the seven-day answer was relevant but unfaithful to the no-overlap context; the thirty-day answer was faithful and relevant to the overlapping context. No model or API call was made.

## Takeaway

In this small synthetic example, 4-word overlap recovered the complete answer sentence in the first retrieved chunk, while 16-word chunks without overlap failed to return it in the top two. The larger 24-word chunk also contained the answer, with more surrounding text. The retrieval scores and chunking result show why retrieval coverage and answer grounding need separate checks.

## Limitations

The corpus is fictional, the retrieval set has only three queries, and the chunking comparison uses one question and one article. Whitespace word counts approximate token counts. Shared-word ranking is not semantic search, the evidence check is an exact sentence match, and the answer fixtures were written by hand. These results do not estimate production performance or establish a best chunk size.

## Next retrieval

- [ ] Add graded relevance labels and calculate NDCG@2, then broaden the query set with additional paraphrases and hard negatives.
