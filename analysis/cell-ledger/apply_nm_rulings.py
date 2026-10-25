#!/usr/bin/env python3
"""Apply Brett's answers on the n-to-m sheet (24 Oct 2026) to the cells.

His answers (reviews/external-nm-pass-20261024/NM-FOR-BRETT.md, edited by him):
  1 "Yes, being its determiner counts ... embedded two or three layers down in a
    relative clause doesn't count. It or the phrase it heads should be a sibling
    of the noun or nom." -> the subject and object cells where all three runs
    said m or y are set, as a block, at the median of the three grades
    (n < m < y). The existential column is left for recoding (answer 2 adds a frame).
    Status "accepted", not "judged": Brett ruled on the column's sense, not on these
    values (a side agent's note, 24 Oct), so they wait for his check (BLOCK-CELLS.md).
  4 "is this a morphology or a syntax property. I expect it's syntax, so 's
    should count" -> the genitive-determiner cells are set the same way.
  8 "do all or both" -> read as: run both arms. The cells keep Brett's 2021 n
    and get the three runs' median as a second, proposed value, marked as an arm.
  2, 3, 5, 6, 7 -> columns redefined or given frames, recoded blind (codebook).
A cell whose note puts the use in the set-denoting frame or an echo question
("set:", "echo:") isn't judged in the default frame.

Writes analysis/cell-ledger/brett-nm-rulings-2026-10-24.csv.
"""
import csv
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ORDER = {"n": 0, "m": 1, "y": 2}
BLOCK = {"appears_in_subject": 1, "appears_in_object": 1, "functions_as_subject_determiner": 4}
ARMS = {"functions_as_predicative_complement_to_seem", "functions_as_predicative_complement",
        "takes_predeterminer_modifiers_all_or_both"}


def main():
    v, notes = defaultdict(dict), defaultdict(dict)
    for r in csv.DictReader((HERE / "coder-cells-nm.csv").open()):
        p = r["proposer"]
        lab = "M" if "MUSE" in p else ("N" if "no claim" in p else "C")
        v[(r["form"], r["column"])][lab] = r["value"]
        notes[(r["form"], r["column"])][lab] = r["note"]
    out, skipped = [], 0
    for k, x in sorted(v.items()):
        if set(x) != {"M", "C", "N"} or "n" in x.values() or (k[1] not in BLOCK and k[1] not in ARMS):
            continue
        if any(t in n for n in notes[k].values() for t in ("set:", "echo:")):
            skipped += 1
            continue
        med = sorted(x.values(), key=ORDER.get)[1]
        var = "; ".join(sorted({n.split("variety:")[1].split("|")[0].strip() for n in notes[k].values() if "variety:" in n}))
        if k[1] in BLOCK:
            out.append({"form": k[0], "column": k[1], "frame": "default", "value": med, "variety": var,
                        "status": "accepted", "evidence_type": "Brett's ruling applied by Claude to three blind runs; values not yet seen by Brett",
                        "note": f"NM-FOR-BRETT question {BLOCK[k[1]]}; runs Muse {x['M']}, Claude with claim {x['C']}, without {x['N']}; 2021 n superseded",
                        "proposer": "Brett's ruling (NM-FOR-BRETT.md), applied by Claude", "judged_by": "", "date": "2026-10-24"})
        else:
            out.append({"form": k[0], "column": k[1], "frame": "default", "value": med, "variety": var,
                        "status": "proposed", "evidence_type": "multiverse arm (Brett: 'do all or both')",
                        "note": f"NM-FOR-BRETT question 8; arm beside Brett's 2021 n; runs Muse {x['M']}, Claude with claim {x['C']}, without {x['N']}",
                        "proposer": "arm: three blind runs (n-to-m pass)", "judged_by": "", "date": "2026-10-24"})
    # Brett's check sheet for the block cells.
    run = HERE.parents[1] / "reviews" / "external-nm-pass-20261024"
    L = ["# Cells your rulings changed: check the values",
         "<!-- SUMMARY: the 65 cells set by applying Brett's n-to-m rulings 1 and 4 (subject, object, genitive determiner), with values and examples, for his check · status: for Brett · updated: 2026-10-24 -->", "",
         "Your answers to questions 1 and 4 said what the columns mean. Applying them turned these 2021 n's into m or y, at the middle of the three blind runs' grades. You haven't seen the values, so they're marked accepted, not judged. Mark any you'd change in the last column. Separate columns, \"heads a subject NP\" and \"heads an object NP\", now keep the fact that reflexive and accusative forms don't head a subject.", "",
         "| column | form | value | example | your call |", "|---|---|---|---|---|"]
    for r in sorted(out, key=lambda r: (r["column"], r["form"])):
        if r["status"] != "accepted":
            continue
        k = (r["form"], r["column"])
        e = next((n.split("|")[1].strip() for lab in ("N", "C", "M") for n in [notes[k].get(lab, "")] if "|" in n), "")
        L.append(f"| {r['column']} | *{r['form']}* | {r['value']}{' (' + r['variety'] + ')' if r['variety'] else ''} | {e} | |")
    (run / "BLOCK-CELLS.md").write_text("\n".join(L) + "\n")
    with (HERE / "brett-nm-rulings-2026-10-24.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)
    from collections import Counter
    print(len(out), "rows;", dict(Counter((r["column"], r["status"], r["value"]) for r in out)), f"; {skipped} left for frames")


if __name__ == "__main__":
    main()
