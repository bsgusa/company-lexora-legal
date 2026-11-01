#!/usr/bin/env python3
"""Truthful-claims check.

Fails if the public surface starts claiming something we do not have:
certifications, customers, funding, a proprietary model, or guaranteed
outcomes.

A mention is allowed when the surrounding lines make clear the claim is not
held — "SOC 2 — not held", "there is no LexLLM", "✗ FedRAMP", the correction
notices in README/wiki, or a "we removed these claims" line.

Files that exist to quote the old, false claims (CHANGELOG.md) opt out with a
`<!-- truthful-claims: history -->` marker near the top. The marker is
deliberate: it should be rare and reviewable.

Run locally:  python3 scripts/check-claims.py
Exit code 0 = clean, 1 = a banned claim needs a human.
"""

from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent

# Only the public surface and the docs that describe it.
TARGETS = ["*.html", "legal/*.html", "*.md", "wiki/*.md", "docs/*.md"]

OPT_OUT_MARKER = "truthful-claims: history"

# Phrases that were false, full stop. (They may still appear inside a
# disclaimer such as "there is no LexLLM".)
HARD_BANS = [
    r"\b500\+ law firms\b",
    r"\b47 jurisdictions\b",
    r"\b2\.4M\+? documents\b",
    r"\b98% (client )?satisfaction\b",
    r"\b98% approval rate\b",
    r"\b15K\+ cases\b",
    r"\ba16z\b",
    r"\bSequoia\b",
    r"\bBessemer\b",
    r"LexLLM",
    r"\bguaranteed approval\b",
    r"\blicensed immigration attorneys?\b",
    r"\bFortune 500 legal teams\b",
]

# Certifications and regimes: fine to mention, not fine to claim.
SOFT_BANS = [
    r"\bSOC ?2\b",
    r"\bISO ?27001\b",
    r"\bHIPAA\b",
    r"\bFedRAMP\b",
    r"\bCCPA\b",
    r"\bGDPR\b",
]

# Any of these near a match means "this line is disclaiming the claim".
DISCLAIMER = re.compile(
    r"\b(?:"
    r"not|no|none|never|without|cannot|unable|"
    r"removed|false|untrue|fabricated|correction|"
    r"readiness|pending|planned|"
    r"does not exist|there is no|isn't|aren't|don't|doesn't"
    r")\b"
    r"|✗",
    re.IGNORECASE,
)

# How many lines above and below a match can carry the disclaimer.
WINDOW = 2


def files() -> list[pathlib.Path]:
    seen: list[pathlib.Path] = []
    for pattern in TARGETS:
        for path in sorted(ROOT.glob(pattern)):
            if path.is_file() and path not in seen:
                seen.append(path)
    return seen


def check(path: pathlib.Path) -> list[str]:
    rel = path.relative_to(ROOT)
    text = path.read_text(encoding="utf-8")
    if OPT_OUT_MARKER in text[:2000]:
        return []

    lines = text.splitlines()
    problems: list[str] = []

    for index, line in enumerate(lines):
        low = index - WINDOW if index >= WINDOW else 0
        high = min(len(lines), index + WINDOW + 1)
        context = "\n".join(lines[low:high])

        for label, patterns in (("banned claim", HARD_BANS), ("uncertified claim", SOFT_BANS)):
            for pattern in patterns:
                if not re.search(pattern, line, re.IGNORECASE):
                    continue
                if DISCLAIMER.search(context):
                    continue
                problems.append(
                    f"{rel}:{index + 1}: {label} /{pattern}/ — {line.strip()[:120]}"
                )

    return problems


def main() -> int:
    targets = files()
    problems: list[str] = []
    for path in targets:
        problems.extend(check(path))

    if problems:
        print("Truthful-claims check FAILED:\n")
        for problem in problems:
            print(f"  {problem}")
        print(
            "\nFix the copy, or say on a nearby line that the claim is not held "
            '("— not held", "there is no …", "✗"). '
            f"A file that must quote the old claims can opt out with `<!-- {OPT_OUT_MARKER} -->`."
        )
        return 1

    print(f"Truthful-claims check passed ({len(targets)} files scanned).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
