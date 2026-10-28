from pathlib import Path
import re

folder = Path(__file__).resolve().parent
corpus = (folder / "corpus.md").read_text(encoding="utf-8")
eval_cases = (folder / "eval_cases.md").read_text(encoding="utf-8")

doc_pattern = re.compile(
    r"^##[ \t]+(DOC-[A-Z])[ \t]+—[^\n]*\n(.*?)(?=^##[ \t]+DOC-[A-Z][ \t]+—|\Z)",
    re.MULTILINE | re.DOTALL,
)
docs = dict(doc_pattern.findall(corpus))

case_pattern = re.compile(
    r"^##[ \t]+(Q\d+)[ \t]*\n(.*?)(?=^##[ \t]+Q\d+[ \t]*$|\Z)",
    re.MULTILINE | re.DOTALL,
)
cases = list(case_pattern.finditer(eval_cases))

if not docs or not cases:
    raise SystemExit("Could not read the documents or evaluation cases.")

stop_words = {
    "when", "will", "my", "the", "a", "an", "for", "is", "does", "do",
    "what", "how", "much", "can", "i", "it", "of", "to", "in", "on",
    "and", "if", "after", "at", "from", "this", "that", "with", "before",
    "or", "your", "you",
}


def terms(text):
    return {
        word
        for word in re.findall(r"[a-z0-9]+", text.lower())
        if word not in stop_words
    }


k = 2
recall_at_1_values = []
recall_at_k_values = []
precision_at_k_values = []
reciprocal_ranks = []

for case in cases:
    case_id = case.group(1)
    case_text = case.group(2)

    question_match = re.search(
        r"^Question:\s*(.+)$", case_text, re.MULTILINE
    )
    gold_match = re.search(
        r"^Relevant document:\s*(DOC-[A-Z])$", case_text, re.MULTILINE
    )

    if question_match is None or gold_match is None:
        raise SystemExit(f"Could not read {case_id}.")

    question = question_match.group(1)
    gold_doc = gold_match.group(1)

    if gold_doc not in docs:
        raise SystemExit(f"{case_id} refers to missing document {gold_doc}.")

    question_terms = terms(question)
    ranked = sorted(
        (
            (len(question_terms & terms(document)), doc_id)
            for doc_id, document in docs.items()
        ),
        key=lambda result: (-result[0], result[1]),
    )

    gold_rank = next(
        (
            rank
            for rank, (_, doc_id) in enumerate(ranked, start=1)
            if doc_id == gold_doc
        ),
        None,
    )

    recall_at_1 = gold_rank is not None and gold_rank <= 1
    recall_at_k = gold_rank is not None and gold_rank <= k
    precision_at_k = sum(
        doc_id == gold_doc for _, doc_id in ranked[:k]
    ) / k
    reciprocal_rank = 1 / gold_rank if gold_rank is not None else 0.0

    recall_at_1_values.append(recall_at_1)
    recall_at_k_values.append(recall_at_k)
    precision_at_k_values.append(precision_at_k)
    reciprocal_ranks.append(reciprocal_rank)

    print(f"{case_id}: {question}")
    for rank, (score, doc_id) in enumerate(ranked, start=1):
        print(f"  {rank}. {doc_id} — {score} shared words")
    print(f"  Gold: {gold_doc} (rank {gold_rank})")
    print(f"  Recall@1: {int(recall_at_1):.1f}")
    print(f"  Recall@{k}: {int(recall_at_k):.1f}")
    print(f"  Precision@{k}: {precision_at_k:.2f}")
    print(f"  Reciprocal rank: {reciprocal_rank:.2f}")

count = len(cases)
print(
    f"\nOverall Recall@1: "
    f"{sum(recall_at_1_values)}/{count} = "
    f"{sum(recall_at_1_values) / count:.2f}"
)
print(
    f"Overall Recall@{k}: "
    f"{sum(recall_at_k_values)}/{count} = "
    f"{sum(recall_at_k_values) / count:.2f}"
)
print(f"Mean Precision@{k}: {sum(precision_at_k_values) / count:.2f}")
print(f"MRR: {sum(reciprocal_ranks) / count:.2f}")
