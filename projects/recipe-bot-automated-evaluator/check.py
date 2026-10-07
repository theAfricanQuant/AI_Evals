import json
import re
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
ROOT_DIR = PROJECT_DIR.parent.parent

CASES_PATH = PROJECT_DIR / "cases.jsonl"
TRACES_PATH = (
    ROOT_DIR
    / "references"
    / "recipe-chatbot"
    / "homeworks"
    / "hw2"
    / "reference_files"
    / "query_response.jsonl"
)


INGREDIENT_ALIASES = {
    "scallions": ["scallions", "green onions"],
}


def read_jsonl(path):
    with path.open(encoding="utf-8") as file:
        return [json.loads(line) for line in file if line.strip()]


cases = read_jsonl(CASES_PATH)
source_traces = read_jsonl(TRACES_PATH)
traces_by_id = {trace["id"]: trace for trace in source_traces}


def response_for(case):
    if "response" in case:
        return case["response"]
    return traces_by_id[case["id"]]["response"]


def evaluate_case(case):
    response = response_for(case).casefold()
    missing = []
    for ingredient in case["requested_ingredients"]:
        aliases = INGREDIENT_ALIASES.get(
            ingredient.casefold(),
            [ingredient.casefold()],
        )
        found = any(
            re.search(rf"\b{re.escape(alias.casefold())}\b", response)
            for alias in aliases
        )
        if not found:
            missing.append(ingredient)
    label = "Fail" if missing else "Pass"
    return label, missing

matches = 0

for case in cases:
    predicted, missing = evaluate_case(case)
    expected = case["expected"]
    status = "MATCH" if predicted == expected else "MISMATCH"

    print(f'{case["id"]}: expected={expected}, predicted={predicted} [{status}]')
    if missing:
        print(f"  Missing: {', '.join(missing)}")

    matches += predicted == expected

print(f"Case label matches: {matches}/{len(cases)}")
