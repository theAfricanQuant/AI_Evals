from pathlib import Path
import re

folder = Path(__file__).resolve().parent
source_words = (folder / "chunking_source.md").read_text(
    encoding="utf-8"
).split()
case_text = (folder / "chunking_case.md").read_text(encoding="utf-8")

question_match = re.search(
    r"^Question:\s*(.+)$", case_text, re.MULTILINE
)
evidence_match = re.search(
    r"^Evidence sentence:\s*(.+)$", case_text, re.MULTILINE
)

if question_match is None or evidence_match is None:
    raise SystemExit("Could not read the question or evidence sentence.")

question = question_match.group(1)
evidence = evidence_match.group(1)

stop_words = {
    "how", "is", "the", "in", "what", "a", "an", "for", "of", "to",
    "does", "after", "from", "its",
}


def terms(text):
    return {
        word
        for word in re.findall(r"[a-z0-9]+", text.lower())
        if word not in stop_words
    }


def make_chunks(words, size, overlap):
    step = size - overlap
    chunks = []

    for start in range(0, len(words), step):
        chunk_words = words[start : start + size]
        if not chunk_words:
            break

        chunks.append(
            (
                start + 1,
                start + len(chunk_words),
                " ".join(chunk_words),
            )
        )

        if start + size >= len(words):
            break

    return chunks


def normalize(text):
    return " ".join(text.lower().split())


query_terms = terms(question)
evidence_normalized = normalize(evidence)
settings = [(16, 0), (16, 4), (24, 0)]

print(f"Question: {question}")
print(f"Source length: {len(source_words)} words")

for size, overlap in settings:
    chunks = make_chunks(source_words, size, overlap)
    ranked = sorted(
        (
            (len(query_terms & terms(text)), start, end, text)
            for start, end, text in chunks
        ),
        key=lambda result: (-result[0], result[1]),
    )

    top_1_text = ranked[0][3]
    top_2_text = " ".join(item[3] for item in ranked[:2])

    evidence_at_1 = evidence_normalized in normalize(top_1_text)
    evidence_at_2 = evidence_normalized in normalize(top_2_text)

    print(f"\nChunk size: {size} words; overlap: {overlap}")
    for rank, (score, start, end, text) in enumerate(ranked[:2], start=1):
        print(f"  {rank}. words {start}-{end}, score {score}: {text}")
    print(f"  Complete evidence in top 1: {'YES' if evidence_at_1 else 'NO'}")
    print(f"  Complete evidence in top 2: {'YES' if evidence_at_2 else 'NO'}")
