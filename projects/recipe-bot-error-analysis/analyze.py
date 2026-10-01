#!/usr/bin/env python3
"""Summarize the fixed Chapter 3 Recipe Chatbot trace-review exercise.

The upstream JSONL is read in place; this exercise stores only trace IDs and
human labels, so the reference dataset remains the single copy of responses.
"""

from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
WORKSPACE_DIR = PROJECT_DIR.parents[1]
SAMPLE_PATH = PROJECT_DIR / "sample_ids.json"
LABELS_PATH = PROJECT_DIR / "labels.csv"


def main() -> None:
    sample = json.loads(SAMPLE_PATH.read_text())
    source_path = (PROJECT_DIR / sample["source_dataset"]).resolve()
    source_rows = {
        row["id"]: row
        for line in source_path.read_text().splitlines()
        if line.strip()
        for row in [json.loads(line)]
    }
    trace_ids = sample["trace_ids"]
    labels = list(csv.DictReader(LABELS_PATH.open(newline="")))

    if len(trace_ids) != len(set(trace_ids)):
        raise ValueError("sample_ids.json contains duplicate trace IDs")
    missing_source = sorted(set(trace_ids) - set(source_rows))
    if missing_source:
        raise ValueError(f"trace IDs not found in source dataset: {missing_source}")
    label_ids = [row["trace_id"] for row in labels]
    if set(label_ids) != set(trace_ids) or len(label_ids) != len(trace_ids):
        raise ValueError("labels.csv must contain exactly one label for each selected trace")
    if any(row["decision"] not in {"acceptable", "unacceptable"} for row in labels):
        raise ValueError("decision must be acceptable or unacceptable")
    if any(
        row["decision"] == "unacceptable" and not row["failure_mode"]
        for row in labels
    ):
        raise ValueError("every unacceptable trace needs a failure mode")

    decisions = Counter(row["decision"] for row in labels)
    failures = Counter(
        row["failure_mode"] for row in labels if row["decision"] == "unacceptable"
    )

    print(f"Source traces available: {len(source_rows)}")
    print(f"Fixed review sample: {len(trace_ids)} traces")
    print(f"Acceptable: {decisions['acceptable']}")
    print(f"Unacceptable: {decisions['unacceptable']}")
    print("\nFirst-failure taxonomy (one label per unacceptable trace):")
    for failure_mode, count in failures.most_common():
        print(f"- {failure_mode}: {count}/{len(trace_ids)} ({count / len(trace_ids):.0%})")
    print("\nLimitation: this is a 20-trace synthetic, single-turn teaching slice; it is not production data or evidence of saturation.")


if __name__ == "__main__":
    main()
