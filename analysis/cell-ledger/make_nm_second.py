#!/usr/bin/env python3
"""Second-pass packets for the n-to-m pass (24 Oct 2026).

Every cell the Muse screen graded m or y, plus a random tenth of the cells it
graded n (seed fixed below), for a Claude subagent that doesn't see Muse's
grades. The sample of Muse's n's estimates what the screen misses.

Usage: python3 analysis/cell-ledger/make_nm_second.py RUN_DIR OUT_DIR [--neutral]
Reads RUN_DIR/nm-map.json and analysis/cell-ledger/coder-cells-nm.csv;
writes OUT_DIR/second-pK/PACKET.md and RUN_DIR/second-map.json.

--neutral (a side agent's note, relayed by Brett, 24 Oct): the same cells and
packets with no claim shown ("claimed never to have" primes agreement with the
2021 value, while the new noun rows were coded with no claim). Writes
OUT_DIR/neutral-pK/PACKET.md and RUN_DIR/neutral-map.json. Comparing the two
Claude runs on identical cells measures the framing effect.
"""
import csv
import json
import random
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CB = ROOT / "analysis" / "codebook"
sys.path.insert(0, str(HERE))
from make_nm import COMMON  # noqa: E402
from make_wave3_ym import CODER_DEF, clean, screen, words_of  # noqa: E402

SEED = 20261024
SAMPLE = 0.10
PER_PACKET = 300


def main():
    run, out = Path(sys.argv[1]), Path(sys.argv[2])
    neutral = "--neutral" in sys.argv[3:]
    prefix = "neutral" if neutral else "second"
    nmap = json.loads((run / "nm-map.json").read_text())
    fid = {v: k for k, v in nmap["forms"].items()}
    defs = {r["column"]: r for r in csv.DictReader((CB / "definitions.csv").open())}
    label = {f["form"]: f["blind_label"] for f in csv.DictReader((CB / "forms.csv").open())}
    muse = {(r["form"], r["column"]): r["value"] for r in csv.DictReader((HERE / "coder-cells-nm.csv").open())
            if "MUSE" in r["proposer"]}
    flagged = sorted(k for k, v in muse.items() if v != "n")  # parse_nm.py has already dropped its STALE columns
    ns = sorted(k for k, v in muse.items() if v == "n")
    sample = sorted(random.Random(SEED).sample(ns, round(SAMPLE * len(ns))))
    chosen = set(flagged) | set(sample)
    colorder = [c for info in nmap["packets"].values() for c in info["columns"].values()]
    bycol = defaultdict(list)
    for f, c in sorted(chosen, key=lambda k: fid[k[0]]):
        bycol[c].append(f)
    items = [(c, bycol[c]) for c in colorder if bycol[c]]
    packets, cur, n = [], [], 0
    for c, fs in items:
        if n and n + len(fs) > PER_PACKET:
            packets.append(cur)
            cur, n = [], 0
        cur.append((c, fs))
        n += len(fs)
    if cur:
        packets.append(cur)
    smap = {"forms": nmap["forms"], "seed": SEED, "sample_share": SAMPLE,
            "flagged": len(flagged), "sampled_n": len(sample), "packets": {}}
    for p, pk in enumerate(packets, start=1):
        used = sorted({f for _, fs in pk for f in fs}, key=lambda f: fid[f])
        d = out / f"{prefix}-p{p}"
        d.mkdir(parents=True, exist_ok=True)
        task = (["For each form listed under a column below, grade whether it can do what the column describes:",
                 "", "- **y**: it can, naturally (in some variety or register is enough);",
                 "- **m**: it can, but only in a degraded way;", "- **n**: it never does.", ""] if neutral else
                ["Each form listed under a column below has been claimed **never** to have that property. For each listed form, grade the claim:",
                 "", "- **n**: the claim holds; the form never does this;", "- **m**: it can, but only in a degraded way;",
                 "- **y**: it can, naturally (in some variety or register is enough).", ""])
        L = ["# How available is each use? A grading task", "", COMMON] + task + [
             "## Forms", "", "| id | form |", "|---|---|"]
        L += [f"| {fid[f]} | {label[f]} |" for f in used]
        L += ["", "## Columns, each with the forms to grade" if neutral else "## Columns, each with the forms claimed never to have it", ""]
        cmap = {}
        for k, (c, fs) in enumerate(pk, start=1):
            dd = dict(defs[c])
            if c in CODER_DEF:
                dd["definition"], dd["anchor_y"], dd["anchor_n"] = CODER_DEF[c]
            text = re.sub(r" \(Brett[^)]*\)", "", clean(dd["definition"]))
            text, _ = screen(text, words_of(used))
            _, hit = screen("", words_of(used, exempt=False))
            ay = dd["anchor_y"] if dd["anchor_y"] and not hit(dd["anchor_y"]) else ""
            L.append(f"- **C{k:02d}**: {text}" + (f" Yes: *{ay}*." if ay else ""))
            L.append(f"  - forms: {', '.join(fid[f] for f in fs)}")
            cmap[f"C{k:02d}"] = c
        L += ["", "## Output (follow exactly)", "", "```", "GRADES",
              "C01: F003 n, F017 m, F040 y, ...   (every listed form, in the order given)", "...",
              "NOTES", "F017 | C01 | m | example | why degraded",
              "F040 | C01 | y | example | variety:, set:, echo:, or nothing", "```", "",
              "Notes only for m and y, one line each, the example ten words or fewer. Stop when both sections are done."]
        (d / "PACKET.md").write_text("\n".join(L))
        smap["packets"][f"p{p}"] = {"columns": cmap, "cells": sum(len(fs) for _, fs in pk),
                                    "listed": [[f, c] for c, fs in pk for f in fs]}
    (run / f"{prefix}-map.json").write_text(json.dumps(smap, indent=1))
    print(f"second pass: {len(flagged)} flagged + {len(sample)} sampled n = {len(chosen)} cells in {len(packets)} packets: "
          + ", ".join(str(v["cells"]) for v in smap["packets"].values()))


if __name__ == "__main__":
    main()
