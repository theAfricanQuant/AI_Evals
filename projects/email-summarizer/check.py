#!/usr/bin/env python3
"""
Reference-free mechanical checks for the email summarizer (Chapter 2 artifact).

Runs L1 unit-test style assertions (Chapter 1's 'mechanical failures -> code
assertions') on the summarizer's OUTPUT text. No LLM, no API keys, no network:
deterministic, offline, repeatable.

Usage: python3 check.py
"""
import json
import re
import sys

# --------------------------------------------------------------------------
# The checks: each returns (name, passed, detail)
# --------------------------------------------------------------------------

def run_checks(email: str, summary: str):
    results = []
    add = lambda name, ok, detail="": results.append((name, ok, detail))

    # 1. Format: the summary must start with a Sender line.
    add("has Sender line",
        bool(re.search(r"(?m)^\s*Sender\s*:", summary)),
        "template requires '- Sender: <name>' first")

    # 2. Format: exactly three request bullets.
    bullets = re.findall(r"(?m)^\s*[-*]\s+", summary)
    add("exactly 3 request bullets", len(bullets) == 3,
        f"found {len(bullets)} bullet(s)")

    # 3. No invented content: the email's first line must not be copied
    #    verbatim into the summary (guards against quoting the thread).
    first_line = email.strip().splitlines()[0][:40] if email.strip() else ""
    add("no verbatim quoting",
        first_line not in summary,
        "first 40 chars of the email must not appear in the summary")

    # 4. Completeness: if the email contains a phone number, the summary
    #    must handle it (mention call/phone/contact or a normalized number).
    if re.search(r"\d{3}[-.)\s]\s*\d{3}[-.)\s]\s*\d{4}", email):
        add("phone number handled",
            bool(re.search(r"call|phone|contact|reach|\+\d", summary, re.I)),
            "email has a phone number; summary should mention it")
    else:
        add("phone number handled", True, "no phone number in email")

    return results


# --------------------------------------------------------------------------
# Demo runs (canned outputs — in real life these come from the LLM)
# --------------------------------------------------------------------------

DEMOS = [
    # (label, email, summary)
    ("good  -> all checks pass",
     "Hi, my account was locked after travel. Please reset it. — Alice",
     "Sender: Alice\nRequests:\n  - Reset account access\n  - Verify travel notice\n  - Confirm contact email"),
    ("bug 1 -> missing Sender, 2 bullets, quotes the email",
     "Hi, my account was locked after travel. Please reset it. — Alice",
     "Summary:\n  - Reset account access\n  - Hi, my account was locked after travel"),
    ("bug 2 -> phone in email ignored by summary",
     "Please reset my password and call me at (415) 555-9021 ext. 7 to verify my email on file. — Alice Johnson",
     "Sender: Alice Johnson\nRequests:\n  - Reset password\n  - Verify email on file\n  - Send updates by SMS"),
]


def main():
    with open("testset.json") as fh:
        testset = json.load(fh)
    print(f"Test set: {len(testset['cases'])} input emails in testset.json\n")

    total_checks = 0
    total_failed = 0
    for label, email, summary in DEMOS:
        print(f"=== {label} ===")
        for name, ok, detail in run_checks(email, summary):
            total_checks += 1
            if not ok:
                total_failed += 1
            mark = "PASS" if ok else "FAIL"
            print(f"  [{mark}] {name}" + (f"  ({detail})" if not ok else ""))
        print()

    print(f"Summary: {total_checks - total_failed}/{total_checks} checks passed "
          f"({total_failed} failed as expected)")
    sys.exit(0)


if __name__ == "__main__":
    main()
