#!/usr/bin/env python3
"""Brett's check of the block cells (reviews/external-nm-pass-20261024/BLOCK-CELLS.md,
edited by him, 24 Oct 2026). A blank call keeps the value he was shown; a written
call replaces it. For the subject column he asked for a split ("split into subject
of main clause, subject of non-finite, etc.") and ruled that emphatic reflexives
"Doesn't count or it's a frame", so each subject cell is recorded in the frame its
example belongs to (Claude's assignment from the examples, listed below). Three
object cells (relative who, whom, whose) have the structure of relative which,
which he marked "Too embedded to count"; asked, he said "same call for all four".
The object column splits like the subject ("2 yes"), so the four relatives are n
as main-clause objects and, from their examples (the book which I read), y as
objects of an embedded tensed clause: accepted, since Brett hasn't seen that value.
Writes analysis/cell-ledger/brett-block-check-2026-10-24.csv."""
import csv
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SHEET = HERE.parents[1] / "reviews" / "external-nm-pass-20261024" / "BLOCK-CELLS.md"
EMPH = {"herself", "himself", "itself", "myself", "ourselves", "themself", "themselves", "yourself", "yourselves"}
NONTENSED = {"each_other", "one_another", "them_plur", "them_sing"}      # For them to quit ...
EMBEDDED = {"whom_int", "whom_rel"}                                      # whom I think is guilty
RELATIVES = {"which_rel_pron", "who_rel", "whom_rel", "whose_rel"}


def main():
    out = []
    for line in SHEET.read_text().splitlines():
        if not line.startswith("| appears") and not line.startswith("| functions"):
            continue
        cells = [c.strip() for c in line.strip("|").split(" | ")]
        col = re.sub(r"\s*\\\[.*", "", cells[0]).replace("\\_", "_").strip()
        form = cells[1].strip("*").replace("\\_", "_")
        shown = cells[2].split()[0]
        call = cells[4].strip(" |") if len(cells) > 4 else ""
        # The coder's example stays in BLOCK-CELLS.md (gitignored): coder output is local.
        note = f"BLOCK-CELLS.md; shown {cells[2]}" + (f"; Brett: \"{call}\"" if call else "; Brett left it")
        frame, value, status = "default", shown, "judged"
        if call:
            if call.split()[0] in ("y", "m", "n"):
                value = call.split()[0]
            elif "embedded" in call.lower():
                value = "n"
        if col == "appears_in_subject":
            if form in EMPH:
                out.append(dict(form=form, column=col, frame="emphatic reflexive modifier", value="y", status="judged", note=note + "; Brett: a frame"))
                frame, value = "subject of a main clause", "n"
            elif form in NONTENSED:
                frame = "subject of a non-tensed clause"
            elif form in EMBEDDED:
                frame = "subject of an embedded tensed clause"
            else:
                frame = "subject of a main clause"
        if col == "appears_in_object":
            if form in RELATIVES:
                out.append(dict(form=form, column=col, frame="object of an embedded tensed clause", value="y",
                                status="accepted", note=note + "; frame from the example; value not yet seen by Brett"))
                frame, value = "object of a main clause", "n"
                note += "; Brett: same call for all four relatives (too embedded)"
            else:
                frame = "object of a main clause"
        out.append(dict(form=form, column=col, frame=frame, value=value, status=status, note=note))
    with (HERE / "brett-block-check-2026-10-24.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["form", "column", "frame", "value", "status", "evidence_type", "note",
                                           "proposer", "judged_by", "date"])
        w.writeheader()
        for r in out:
            w.writerow({**r, "evidence_type": "Brett judgment (block check)", "proposer": "Brett, BLOCK-CELLS.md",
                        "judged_by": "Brett" if r["status"] == "judged" else "", "date": "2026-10-24"})
    from collections import Counter
    print(len(out), "rows;", dict(Counter((r["column"], r["frame"], r["value"]) for r in out)))


if __name__ == "__main__":
    main()
