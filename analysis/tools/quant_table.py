#!/usr/bin/env python3
"""Derive Table 1 of quantifier-controls.tex from the extracted claim set.

The 54 cells of tab:quant-controls correspond one-to-one with query IDs
X001-X054 in analysis/expanded-json-2026-09-14/records.json, mapped by
supplement-cell-map.json.  This script derives each cell's marker from the
claim and either emits the tabular body (build) or compares it against the
committed .tex (check).

What the check does and does not establish
------------------------------------------
It catches drift between the table and the extracted claim set: a marker
edited in the .tex without a corresponding change to the claims, or an
example relabelled on one side only.  It is not an independent validation of
the markers themselves.  The G/R/I markers are derived from each claim's
`Evidential basis' condition, which the extraction read off this same table;
the attestation refs are derived from each claim's own cited example item,
which is independent of the table row.  The table row quote that appears in
every claim's evidence list is excluded from label extraction so the check
does not compare the table against a copy of itself.
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "analysis" / "expanded-json-2026-09-14"
TEX = ROOT / "quantifier-controls.tex"

# Column order of tab:quant-controls.
COLUMNS = [
    ("argument", "partitive"),
    ("argument", "relative"),
    ("argument", "no dependent"),
    ("existential", "partitive"),
    ("existential", "relative"),
    ("existential", "no dependent"),
]

# Presentation conventions of the printed table, declared rather than inferred.
# Row order: the cell map runs lot (X043-X048) before plenty (X049-X054); the
# table prints the reverse.  Row labels: the claim form is the lexeme form, so
# lex_lot's form is `lot', while the table's row label keeps the article,
# following the supplement's "The common-noun controls retain \mention{a} in
# \mention{a lot}."  Neither difference carries content.
ROW_ORDER = ["many", "several", "certain", "various", "numerous",
             "multiple", "countless", "plenty", "lot"]
ROW_LABEL = {"lot": "a lot"}

# Derivation rules, keyed on the claim's `Evidential basis' condition.
BASIS = re.compile(r"Evidential basis stated in the supplement's comparison table: (.+)")
BASIS_MARKER = [
    ("a numbered reference to a retained attestation", "REF"),
    (r'\textit{I}', r"\textit{I}"),
    ('G, "described in', "G"),
    ('R, "restricted there"', "R"),
]

# Example item labels: \ea\label{} for a list's first item, \ex\label{} otherwise.
LABEL = re.compile(r"\\e[ax]\\label\{(ex:[^}]+)\}")
TABLE_ROW = re.compile(r"^\\mention\{")


def derive():
    """Return {(form, surrounding, dependent): marker} plus the form order."""
    records = json.loads((RUN / "records.json").read_text())
    claims = {c["id"]: c for c in records["participation_claims"]}
    cellmap = json.loads((RUN / "supplement-cell-map.json").read_text())

    cells = {}
    for entry in cellmap:
        qid = entry["query_id"]
        claim = claims[qid]
        form = entry["form"]

        basis = None
        for cond in claim["conditions"]:
            found = BASIS.search(cond["requirement"])
            if found:
                basis = found.group(1)

        if basis is None:
            if claim["status"] != "not_stated":
                sys.exit(f"{qid}: no evidential basis and status is {claim['status']}")
            marker = "S"
        else:
            marker = next((m for t, m in BASIS_MARKER if t in basis), None)
            if marker is None:
                sys.exit(f"{qid}: unrecognised evidential basis: {basis[:60]}")

        if marker == "REF":
            labels = set()
            for ev in claim["evidence"]:
                if TABLE_ROW.match(ev["quote"]):
                    continue  # the table row itself; excluded to keep the check honest
                labels |= set(LABEL.findall(ev["quote"]))
            if len(labels) != 1:
                sys.exit(f"{qid}: expected exactly one example label, got {sorted(labels)}")
            marker = r"(\ref{%s})" % labels.pop()

        key = (form, entry["surrounding_construction"], entry["dependent_configuration"])
        if key in cells:
            sys.exit(f"duplicate cell {key}")
        cells[key] = marker

    present = {form for form, _, _ in cells}
    if present != set(ROW_ORDER):
        sys.exit(f"ROW_ORDER does not cover the cell map: "
                 f"missing {sorted(present - set(ROW_ORDER))}, "
                 f"extra {sorted(set(ROW_ORDER) - present)}")
    return cells


def rows(cells):
    out = []
    for form in ROW_ORDER:
        marks = [cells[(form, s, d)] for s, d in COLUMNS]
        label = ROW_LABEL.get(form, form)
        out.append(r"\mention{%s} & %s \\" % (label, " & ".join(marks)))
    return out


def tex_rows():
    """Extract the committed generated body rows of tab:quant-controls."""
    gen = ROOT / "analysis" / "generated" / "quant-table.tex"
    text = gen.read_text() if gen.exists() else TEX.read_text()
    return [ln.strip() for ln in text.splitlines() if ln.strip().startswith(r"\mention{")]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("mode", choices=["build", "check"])
    args = ap.parse_args()

    cells = derive()
    derived = rows(cells)

    if args.mode == "build":
        out = ROOT / "analysis" / "generated" / "quant-table.tex"
        out.write_text("% Generated by analysis/tools/quant_table.py from the\n"
                       "% extracted claim set; do not edit by hand.\n"
                       + "\n".join(derived) + "\n")
        print(f"wrote {out.relative_to(ROOT)} ({len(derived)} rows)")
        return 0

    committed = tex_rows()
    if len(committed) != len(derived):
        print(f"FAIL: {len(committed)} rows in {TEX.name}, {len(derived)} derived")
        return 1

    bad = 0
    for got, want in zip(committed, derived):
        if " ".join(got.split()) != " ".join(want.split()):
            bad += 1
            print(f"FAIL\n  tex:     {got}\n  derived: {want}")
    if bad:
        print(f"\n{bad} of {len(derived)} rows differ")
        return 1

    print(f"OK: all {len(derived)} rows of tab:quant-controls match the claim set "
          f"({len(cells)} cells from X001-X054)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
