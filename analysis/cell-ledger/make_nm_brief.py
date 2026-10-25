#!/usr/bin/env python3
"""Brett's sheet for the n-to-m pass (24 Oct 2026): column-level questions.

The cells where all three runs (Muse, Claude with the claim shown, Claude
without) graded a 2021 n as m or y cluster in a few columns, so the sheet asks
one question per column, with the forms and an example each; the scattered
remainder is counted, not listed. Writes RUN_DIR/NM-FOR-BRETT.md.

Usage: python3 analysis/cell-ledger/make_nm_brief.py RUN_DIR
"""
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
MIN_CELLS = 9
QUESTIONS = """## The questions

Eight questions settle most of the 399 cells. The tables below are the evidence; each question names its sections.

1. **"Appear in" an NP: does being its determiner count, or must the form head it?** In 2021 you have n for *any*, *every*, *the*, and *this* in the existential column, though *There isn't any milk* and *There's this guy I know* are fine, so your 2021 sense looks like "heads the NP". The same question decides the subject and object columns (*Its lid broke*, *The queen herself came*). Sections 1, 6, 11.
2. **Presentational and list existentials** (*There's only me*, *There's the problem of cost*, *There's always tomorrow*): count, or a frame of their own? Section 1.
3. **Person deixis: does reference that takes in the speaker or addressee only through a partitive, a binder, or an imperative count** (*All of us agreed*, *We love each other*, *Everybody sit down!*)? Section 3.
4. **A genitive in determiner function: does an 's genitive count** (*anybody's guess*, *each other's books*), or only a form that is itself a genitive (*my*, *whose*)? Your 's ruling suggests the second, with the 's genitive in the 's column. Section 4.
5. **Degree: gradable meaning, or use as a degree modifier?** The coders took it as the second (*a little tired*, *all alone*, *any better*, *anything like his father*). Section 7. And **very**: do *the very last day* (very as an adjective in the NP) and *That's very him* count? Section 10.
6. **Universal: does free-choice *any* count** (*Any child could do that*)? *CGEL* p. 423 calls *any* an existential quantifier ("non-affirmative or free choice"), which says no. Section 9.
7. **Special constructions to treat as frames rather than as y in ordinary use:** arithmetic (*twice two is four*, *half three is one and a half*), British clock time (*half three*), free indirect discourse (*Tomorrow was Christmas*), and post-head numerals (*page one*, *room three*). Sections 5, 13, 14, 15.
8. **The rest look like 2021 slips to confirm or reject as a block:** quantity words as the bare complement of *seem* (*Opportunities seem few*, *That seems enough*), fused heads as predicative complements (*That's the least I can do*), post-head *all*, *each*, *both* and emphatic reflexives (*They cost ten dollars each*, *the queen herself*), and *all* before *last week*, numerals, and *today* (*all last week*, *all three books*). Sections 2, 5, 8, 12.

For each, answer **yes**, **no**, or **by form** (then mark the rows in the section). The 77 scattered cells in other columns come after these are settled.
"""




def ex(note):
    parts = [p.strip() for p in note.split("|")]
    e = parts[1] if len(parts) > 1 else ""
    return e.strip('"*')


def main():
    run = Path(sys.argv[1])
    defs = {r["column"]: r for r in csv.DictReader((ROOT / "analysis" / "codebook" / "definitions.csv").open())}
    v, n = defaultdict(dict), defaultdict(dict)
    for r in csv.DictReader((HERE / "coder-cells-nm.csv").open()):
        p = r["proposer"]
        lab = "M" if "MUSE" in p else ("N" if "no claim" in p else "C")
        v[(r["form"], r["column"])][lab] = r["value"]
        n[(r["form"], r["column"])][lab] = r["note"]
    cand = {k: x for k, x in v.items() if set(x) == {"M", "C", "N"} and "n" not in x.values()}
    bycol = defaultdict(list)
    for (f, c), x in sorted(cand.items()):
        bycol[c].append(f)
    big = sorted((c for c in bycol if len(bycol[c]) >= MIN_CELLS), key=lambda c: -len(bycol[c]))
    rest = sum(len(bycol[c]) for c in bycol if c not in big)
    L = ["# The n-to-m results: what needs you",
         "<!-- SUMMARY: column-level questions from the n-to-m pass, where three blind runs graded Brett's 2021 n cells m or y · status: for Brett · updated: 2026-10-24 -->", "",
         f"Three blind runs (Muse, and a Claude coder twice, with and without your 2021 value shown) graded your 2021 n cells. All three said the use is possible (m or y) for {len(cand)} cells. Most fall in a few columns, so each section asks one question about the column, with the forms and one example each (the neutral Claude run's, or the other run's where it gave none). Values are listed as Muse / Claude with claim / Claude without.", "",
         QUESTIONS, "## The evidence, by column", ""]
    for i, c in enumerate(big, start=1):
        d = defs[c]["definition"].split(" n in 2021")[0]
        L += [f"### {i}. {c} ({len(bycol[c])} cells)", "", f"*{d}*", "", "| form | values | example |", "|---|---|---|"]
        for f in bycol[c]:
            x, nn = v[(f, c)], n[(f, c)]
            e = ex(nn.get("N", "")) or ex(nn.get("C", "")) or ex(nn.get("M", ""))
            L.append(f"| *{f}* | {x['M']} / {x['C']} / {x['N']} | {e} |")
        L += [""]
    (run / "NM-FOR-BRETT.md").write_text("\n".join(L) + "\n")
    print(f"{len(cand)} candidates; {len(big)} column questions covering {len(cand) - rest}; remainder {rest} in {len(bycol) - len(big)} columns")


if __name__ == "__main__":
    main()
