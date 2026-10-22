"""Small, text-only oatmeal-v3 rule checker for teaching purposes."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).parent
DEFAULT_FIXTURES = ROOT / "checker-fixtures.jsonl"

OATMEAL_RE = re.compile(r"\b(?:oatmeal|rolled oats|oats)\b", re.IGNORECASE)
TREE_NUT_RE = re.compile(
    r"\b(?:peanuts?|almonds?|walnuts?|cashews?|pecans?|pistachios?|"
    r"hazelnuts?|macadamias?|brazil nuts?)\b",
    re.IGNORECASE,
)
SWEETENER_RE = re.compile(
    r"\b(?:sugar|honey|maple syrup|syrup|stevia|monk[ -]?fruit(?: extract)?|sweetened)\b",
    re.IGNORECASE,
)
DAIRY_RE = re.compile(
    r"\b(?:dairy milk|cow'?s milk|whole milk|skim milk|Greek yogurt|yogurt|"
    r"cream|whey)\b",
    re.IGNORECASE,
)
PLANT_MILK_RE = re.compile(
    r"\b(?:soy|soya|oat|almond|cashew|coconut|rice|hemp|pea) milk\b",
    re.IGNORECASE,
)
NEGATION_PREFIX_RE = re.compile(
    r"\b(?:no|without|avoid|omit|exclude|free of|do not use|don't use|zero)\s+"
    r"(?:(?:added|refined)\s+)?$",
    re.I,
)


def ingredient_lines(response: str) -> list[str]:
    """Return bullet/list items within an Ingredients heading."""
    lines = response.splitlines()
    in_ingredients = False
    found: list[str] = []
    for line in lines:
        stripped = line.strip()
        if re.match(r"#{1,6}\s*ingredients\s*$", stripped, re.I):
            in_ingredients = True
            continue
        if in_ingredients and (stripped.startswith("#") or re.match(r"\*\*[^*]+\*\*:?\s*$", stripped)):
            break
        if in_ingredients and re.match(r"^(?:[-*+]\s+|\d+[.)]\s+)", stripped):
            found.append(stripped)
    return found


def has_positive_match(pattern: re.Pattern[str], line: str) -> bool:
    """Ignore a prohibited item when the ingredient line explicitly rejects it."""
    for match in pattern.finditer(line):
        prefix = line[max(0, match.start() - 48) : match.start()]
        if not NEGATION_PREFIX_RE.search(prefix):
            return True
    return False


def check_response(response: str) -> tuple[str, list[str]]:
    """Apply a deliberately narrow and inspectable approximation of oatmeal-v3."""
    reasons: list[str] = []
    if not OATMEAL_RE.search(response):
        return "Fail", ["No oatmeal or oats identified."]

    items = ingredient_lines(response)
    if not items:
        return "Review", ["Could not find a readable Ingredients list."]

    for line in items:
        # Do not fail merely because an ingredient is mentioned as something to avoid.
        if has_positive_match(SWEETENER_RE, line):
            reasons.append("Ingredient list suggests an added sweetener.")
            break

    for line in items:
        if has_positive_match(TREE_NUT_RE, line):
            reasons.append("Ingredient list suggests peanuts or a tree nut.")
            break

    for line in items:
        if has_positive_match(DAIRY_RE, line):
            reasons.append("Ingredient list suggests a dairy ingredient.")
            break
        if has_positive_match(re.compile(r"\bbutter\b", re.I), line):
            # Nut butter is caught by the nut rule; seed butter is allowed.
            if re.search(r"\b(?:sunflower|pumpkin|sesame) seed butter\b", line, re.I):
                continue
            if not re.search(r"\b(?:peanut|almond|walnut|cashew|pecan) butter\b", line, re.I):
                reasons.append("Butter type is unclear or dairy butter is listed.")
                break
        if has_positive_match(re.compile(r"\bmilk\b", re.I), line) and not PLANT_MILK_RE.search(line):
            reasons.append("Milk type is unclear.")

    if reasons:
        if any(reason.startswith("Ingredient list suggests") for reason in reasons):
            return "Fail", reasons
        return "Review", reasons
    return "Pass", ["No listed oatmeal-v3 violation found by these keyword rules."]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixtures", type=Path, default=DEFAULT_FIXTURES)
    args = parser.parse_args()

    mismatches = 0
    count = 0
    with args.fixtures.open(encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, start=1):
            if not line.strip():
                continue
            count += 1
            case = json.loads(line)
            predicted, reasons = check_response(case["response"])
            expected = case["expected"]
            matched = predicted == expected
            mismatches += not matched
            marker = "MATCH" if matched else "MISMATCH"
            print(f"{case['id']}: expected={expected}, predicted={predicted} [{marker}]")
            for reason in reasons:
                print(f"  Reason: {reason}")
            if not matched:
                print(f"  Fixture line: {line_number}")

    if count == 0:
        print("No fixtures found.", file=sys.stderr)
        return 2
    print(f"Fixture labels matched: {count - mismatches}/{count}")
    return 1 if mismatches else 0


if __name__ == "__main__":
    raise SystemExit(main())
