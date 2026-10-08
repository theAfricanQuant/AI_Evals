import json
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
CASES_PATH = PROJECT_DIR / "cases.jsonl"
TIME_TOLERANCE_MINUTES = 5


def read_cases():
    with CASES_PATH.open(encoding="utf-8") as file:
        return [json.loads(line) for line in file if line.strip()]


def evaluate_case(case):
    target = case.get("requested_time_limit_minutes")
    estimate = case.get("reviewer_estimated_total_minutes")
    known_minimum = case.get("known_minimum_total_minutes")
    durations_complete = case.get("all_required_durations_stated", False)
    tolerance = case.get("time_tolerance_minutes", TIME_TOLERANCE_MINUTES)

    if target is None:
        return "Review"

    maximum_allowed = target + tolerance

    # A known minimum beyond the limit proves failure even if other durations
    # are missing. Missing information matters only when it could change the label.
    if known_minimum is not None and known_minimum > maximum_allowed:
        return "Fail"

    if estimate is None or not durations_complete:
        return "Review"

    if estimate > maximum_allowed:
        return "Fail"

    return "Pass"


cases = read_cases()
matches = 0

for case in cases:
    predicted = evaluate_case(case)
    expected = case["expected"]
    status = "MATCH" if predicted == expected else "MISMATCH"
    print(f'{case["id"]}: expected={expected}, predicted={predicted} [{status}]')
    matches += predicted == expected

print(f"Case label matches: {matches}/{len(cases)}")
