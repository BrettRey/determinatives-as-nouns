#!/usr/bin/env python3
"""Check every ledger quote against its source (planning/codebook.md, section 8).

A row with a quote must cite a locator whose file exists, and the quote must be
an exact substring of that file after whitespace is normalized and the PDF
ligatures fi/fl are expanded. A locator naming CGEL ("CGEL p. N") is checked
against literature/00-CGEL.md. Exit 1 if any quote fails.
"""
import csv
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
LIT = ROOT.parents[2] / "literature"


def norm(s):
    s = s.replace("ﬁ", "fi").replace("ﬂ", "fl").replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    return " ".join(s.split())


def source_for(locator):
    if re.search(r"\bCGEL\b", locator):
        return LIT / "00-CGEL.md"
    path = locator.split(":")[0].split(" ")[0]
    p = ROOT / path
    return p if p.exists() else None


def main():
    cache, bad, checked = {}, [], 0
    for r in csv.DictReader((HERE / "cells.csv").open()):
        if not r["quote"]:
            continue
        checked += 1
        src = source_for(r["locator"])
        if src is None:
            bad.append((r["form"], r["column"], "locator not found: " + r["locator"]))
            continue
        if src not in cache:
            cache[src] = norm(src.read_text(errors="replace"))
        if norm(r["quote"]) not in cache[src]:
            bad.append((r["form"], r["column"], "quote not in " + str(src.name)))
    print(f"{checked} quotes checked; {len(bad)} failed")
    for b in bad[:40]:
        print("  ", " | ".join(b))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
