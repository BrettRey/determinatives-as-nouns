#!/usr/bin/env python3
"""Apply Brett's register ruling to the blind coders' m grades (24 Oct 2026).

Brett, on the y-to-m sheet: "I'm disinclined to consider register." The codebook
already says a use limited to a variety or register is y with a variety note,
and rarity isn't on the scale. So an m whose note gives only register, variety,
or rarity as the reason becomes a proposed y with the note kept as a variety
note. An m whose note also gives a sign of degradation (awkward, odd, strained,
stilted, and the like) stays m: the word list can't tell which reason the coder
weighed, so those are listed for Brett.

Reads analysis/cell-ledger/coder-cells.csv (pilot) and coder-cells-{wave2,wave3,ym}.csv (whichever
exist); writes analysis/cell-ledger/coder-cells-register-rule.csv (gitignored
with the other coder files, since it quotes coder notes) and prints counts.
"""
import csv
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from make_ym_review import REGISTER  # noqa: E402

DEGRADED = re.compile(r"awkward|\bodd\b|degrad|strain|stilted|marginal|unnatural|clumsy|forced|contrived|"
                      r"questionable|sounds? (?:off|wrong|bad)|hard to|difficult|resist", re.I)


def main():
    out, kept = [], []
    for f in sorted(HERE.glob("coder-cells*.csv")):
        if f.name == "coder-cells-register-rule.csv":
            continue
        for r in csv.DictReader(f.open()):
            if r["value"] != "m" or not REGISTER.search(r["note"]):
                continue
            if DEGRADED.search(r["note"]):
                kept.append((f.name, r["form"], r["column"], r["proposer"]))
                continue
            out.append({**r, "value": "y", "variety": "register or rarity (coder's m, reclassified)",
                        "note": "variety: " + r["note"],
                        "proposer": f"register rule (Brett, 24 Oct) on {r['proposer']}"})
    fields = list(out[0]) if out else ["form"]
    with (HERE / "coder-cells-register-rule.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(out)
    print(f"{len(out)} m grades reclassified y (variety); {len(kept)} kept m because the note also cites degradation")
    print("reclassified by source:", dict(Counter(r["proposer"].split("(")[-1].split(",")[0] for r in out)))


if __name__ == "__main__":
    main()
