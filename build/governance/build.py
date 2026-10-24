#!/usr/bin/env python3
"""Build the AI governance lecture from its part files.

Assembles the tok-study-guide template, removes the remote Google Fonts links so
the page is fully offline, and adds one phone-only rule that lets the dense SVG
diagrams be panned at readable size instead of shrinking to ~10px text.
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = "/mnt/HC_Volume_106515957/AI_Evals/reports/generated/lecture-ai-governance-runtime-evals-2026-10-24.html"
ASSEMBLE = "/root/.hermes/skills/tok-study-guide/scripts/assemble.py"

PARTS = [os.path.join(HERE, f"part{i}.html") for i in range(1, 7)]

PHONE_CSS = """<style id="phone-diagrams">
@media (max-width:640px){
  figure.diagram{overflow-x:auto;-webkit-overflow-scrolling:touch;padding-bottom:.5rem}
  figure.diagram svg{min-width:600px}
  figure.diagram figcaption{min-width:300px}
  figure.diagram::after{content:"Swipe the diagram sideways to see it at full size →";display:block;font-size:.8rem;color:var(--muted);margin-top:.35rem}
}
</style>"""


def main():
    subprocess.run(
        [
            sys.executable,
            ASSEMBLE,
            "--title",
            "The Gate, the Ledger, and the Machine — AI Governance from Law to Runtime",
            "--description",
            "A lecture on AI governance: the four layers, the EU AI Act, runtime controls, case studies, and where evaluation fits.",
            "--accent",
            "#1F6FEB",
            "--out",
            OUT,
            *PARTS,
        ],
        check=True,
    )
    with open(OUT, encoding="utf-8") as fh:
        page = fh.read()

    page = re.sub(r'\n<link rel="preconnect" href="https://fonts\.googleapis\.com">', "", page)
    page = re.sub(r'\n<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>', "", page)
    page = re.sub(r'\n<link href="https://fonts\.googleapis\.com/css2\?[^"]*" rel="stylesheet">', "", page)
    page = page.replace("</head>", PHONE_CSS + "\n</head>")

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(page)
    print(f"Built {OUT} ({os.path.getsize(OUT):,} bytes)")


if __name__ == "__main__":
    main()
