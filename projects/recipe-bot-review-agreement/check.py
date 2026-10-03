#!/usr/bin/env python3
"""Validate the Chapter 4 requested-ingredient review pilot."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
SHARED_SET_PATH = PROJECT_DIR / "shared-set.md"
LABELS_PATH = PROJECT_DIR / "reviewer-a.csv"
SOURCE_PATH = (
    PROJECT_DIR
    / "../../references/recipe-chatbot/homeworks/hw2/reference_files/query_response.jsonl"
).resolve()


def main() -> None:
    trace_ids = re.findall(r"^- (SYN\d{3})$", SHARED_SET_PATH.read_text(), re.MULTILINE)
    labels = list(csv.DictReader(LABELS_PATH.open(newline="")))
    source_ids = {
        json.loads(line)["id"] for line in SOURCE_PATH.read_text().splitlines() if line.strip()
    }

    if len(trace_ids) != 10 or len(trace_ids) != len(set(trace_ids)):
        raise ValueError("shared-set.md must contain exactly 10 unique SYN trace IDs")
    if set(trace_ids) - source_ids:
        raise ValueError("shared-set.md contains IDs missing from the source dataset")
    if len(labels) != len(trace_ids):
        raise ValueError("reviewer-a.csv must contain one row per shared trace")
    if {row["trace_id"] for row in labels} != set(trace_ids):
        raise ValueError("reviewer-a.csv trace IDs must match shared-set.md")
    if any(row["label"] not in {"Pass", "Fail"} for row in labels):
        raise ValueError("labels must be Pass or Fail")

    counts = Counter(row["label"] for row in labels)
    print(f"Source traces available: {len(source_ids)}")
    print(f"Shared set: {len(trace_ids)} fixed traces")
    print(f"Reviewer A labels: {len(labels)}")
    print(f"Pass: {counts['Pass']}")
    print(f"Fail: {counts['Fail']}")
    print("IAA / Cohen's Kappa: not calculated (one reviewer; one label class)")


if __name__ == "__main__":
    main()
