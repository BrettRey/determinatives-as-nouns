#!/usr/bin/env python3
"""Packets for the n-to-m pass (24 Oct 2026; Brett: "go for it").

The y-to-m pass let a 2021 y become m but never a 2021 n, while the new noun
and adjective rows were coded fresh and can get m from either side (a side
agent's note, relayed by Brett). This pass grades Brett's 2021 n cells y / m / n.

Columns: the 62 graded in the y-to-m pass, less the lexeme facts and the
derived column (no m by the codebook) and the twelve columns being redesigned
after Brett's answers (head selection and compatibility, non-affirmative, free
choice, existential, semantic number). Design: Muse screens every cell; a
Claude subagent then grades every cell Muse flags plus a random tenth of the
rest, which measures what the screen misses (make_nm_second.py).

Usage: python3 analysis/cell-ledger/make_nm.py OUT_DIR
Writes OUT_DIR/nm-pN/PACKET.md and OUT_DIR/nm-map.json.
"""
import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CB = ROOT / "analysis" / "codebook"
sys.path.insert(0, str(HERE))
from make_wave3_ym import CODER_DEF, clean, screen, words_of  # noqa: E402

REDESIGN = {"selects_singular_heads", "selects_count_singular_heads", "selects_non_count_heads", "selects_plural_heads",
            "compatible_count_sing_NP", "compatible_count_plur_NP", "compatible_non_count_NP",
            "non_affirmative", "free_choice", "existential", "semantically_singular", "semantically_plural"}
PER_PACKET = 340

COMMON = """Thank you for helping. This is part of a descriptive grammar of English: we need your independent judgment of what each word form below can do. Please use no tools and consult no files or sources; the judgments should be your own. Think carefully, but keep the output to the format at the end.

Conventions:
- **The head of a phrase like *the dog* is *dog*, not *the*.** Where a column says a modifier attaches to a phrase the form heads, *quite the scholar* doesn't count for *the*: *quite* is the sibling of an NP headed by *scholar*.
- **m** means possible but degraded to speakers generally. Don't round a degraded use up to y or down to n.
- **Register, variety, and rarity aren't degradation.** A use that is formal, archaic, literary, informal, regional, or rare is y, with a note beginning "variety:".
- A mistake, a quotation, a pun, or an unrelated word with the same spelling (*lot* meaning a plot of land, *number* the verb) doesn't count.
- A use for a kind of individual, with an article or a plural (*the Smiths*, *an Ophelia*), isn't a different word for this task, whatever the form. If that is the only use with the property, grade it y or m with a note beginning "set:".
- An echo question (*You saw WHO?*) is a construction of its own. If a use is available only in echo questions, grade it y or m with a note beginning "echo:".
"""


def main():
    out = Path(sys.argv[1])
    defs = {r["column"]: r for r in csv.DictReader((CB / "definitions.csv").open())}
    cols = {r["column"]: r for r in csv.DictReader((CB / "columns.csv").open())}
    label = {f["form"]: f["blind_label"] for f in csv.DictReader((CB / "forms.csv").open())}
    ym = json.loads((ROOT / "reviews" / "external-ym-pass-20261024" / "ym-map.json").read_text())
    graded = [c for info in ym["packets"].values() for c in info["columns"].values()]
    use = [c for c in graded if cols[c]["type"] == "possibility" and c not in REDESIGN]
    m = list(csv.reader((ROOT / "analysis" / "matrix-2026-10" / "matrix-2026-10.csv").open()))
    h, mrows = m[0], m[1:]
    fid = {r[0]: f"F{i + 1:03d}" for i, r in enumerate(mrows)}
    items = [(c, [r[0] for r in mrows if r[h.index(c)] == "n"]) for c in use]
    packets, cur, n = [], [], 0
    for c, fs in items:
        if n and n + len(fs) > PER_PACKET:
            packets.append(cur)
            cur, n = [], 0
        cur.append((c, fs))
        n += len(fs)
    if cur:
        packets.append(cur)
    nmap = {"forms": {v: k for k, v in fid.items()}, "packets": {}}
    for p, pk in enumerate(packets, start=1):
        used = sorted({f for _, fs in pk for f in fs}, key=lambda f: fid[f])
        d = out / f"nm-p{p}"
        d.mkdir(parents=True, exist_ok=True)
        L = ["# How available is each use? A grading task", "", COMMON,
             "Each form listed under a column below has been claimed **never** to have that property. For each listed form, grade the claim:",
             "", "- **n**: the claim holds; the form never does this;", "- **m**: it can, but only in a degraded way;",
             "- **y**: it can, naturally (in some variety or register is enough).", "",
             "## Forms", "", "| id | form |", "|---|---|"]
        L += [f"| {fid[f]} | {label[f]} |" for f in used]
        L += ["", "## Columns, each with the forms claimed never to have it", ""]
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
        nmap["packets"][f"p{p}"] = {"columns": cmap, "cells": sum(len(fs) for _, fs in pk)}
    (out / "nm-map.json").write_text(json.dumps(nmap, indent=1))
    total = sum(v["cells"] for v in nmap["packets"].values())
    print(f"n-to-m: {len(use)} columns, {total} cells in {len(packets)} packets: "
          + ", ".join(str(v["cells"]) for v in nmap["packets"].values()))


if __name__ == "__main__":
    main()
