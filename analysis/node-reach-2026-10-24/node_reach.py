#!/usr/bin/env python3
"""Desk count for the evidence ledger's pronoun-node-reach row (24 Oct 2026).

Question: how far across the determinative inventory do the properties shared
with pronouns reach, against the properties determinatives have and pronouns
lack (where the links with quantity common nouns would sit)?

Input: analysis/matrix-2026-10/matrix-2026-10.csv (139 forms: 73 determinatives,
66 pronouns; no common or proper nouns) and analysis/data/word-mapping.csv for
CGEL's category of each form (whomever, added in 2026-10, is a pronoun).
Only the syntactic and semantic columns are used (from genitive_case on); the
first 50 columns record word components (some-, -body, wh-) and are skipped.

Output: node-reach.csv (one row per feature: counts among determinatives,
pronouns, and the three groups of determinatives defined below) and a summary
on stdout.

Groups (defined from the matrix, not from CGEL):
  A  pronoun-like determinatives: any of personal gender as head, interrogative,
     person deixis, or must-be-stressed-as-object-after-a-particle;
  B  quantity-like determinatives: not A, and head of a partitive;
  C  the rest.
Counts are of forms, not lexemes (fewer and fewest, which_rel and which_int,
count separately). The matrix's features are theory-informed and some are
suspect (see README.md); 13 corrections await Brett (matrix-2026-10/REPORT.md).
"""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MATRIX = ROOT / "analysis" / "matrix-2026-10" / "matrix-2026-10.csv"
MAPPING = ROOT / "analysis" / "data" / "word-mapping.csv"
OUT = Path(__file__).resolve().parent / "node-reach.csv"

A_FEATURES = ["personal_gender_as_head_or_fused_head", "interrogative",
              "person_deixis", "Must_be_stressed_as_object_after_particle"]
PARTITIVE = "functions_as_head_of_partitive_construction"
COMPAT = Path(__file__).resolve().parent / "compatibility.csv"
PRON_LIKE = ["personal_gender_as_head_or_fused_head", "interrogative", "person_deixis",
             "takes_else_or_more_as_a_post_head_dependent",
             "Must_be_stressed_as_object_after_particle"]
QUANT_LIKE = [PARTITIVE, "paradigm_has_comparative_and_superlative_forms",
              "functions_as_degree_modifier_in_AdjP",
              "appears_in_existentials_there_s_on_the_table",
              "May_coordinate_with_non_fused_determiners"]


def main():
    rows = list(csv.reader(MATRIX.open()))
    header, forms = rows[0], rows[1:]
    cat = {}
    for r in csv.DictReader(MAPPING.open()):
        cat[r["working_name"]] = r["category"]
        cat[r["public_name"]] = r["category"]
    cat["whomever"] = "pronoun"
    col = {f: i for i, f in enumerate(header)}
    D = [r for r in forms if cat[r[0]] == "determinative"]
    P = [r for r in forms if cat[r[0]] == "pronoun"]
    A = [r for r in D if any(r[col[f]] == "y" for f in A_FEATURES)]
    B = [r for r in D if r not in A and r[col[PARTITIVE]] == "y"]
    C = [r for r in D if r not in A and r not in B]

    def n(group, j):
        return sum(r[j] == "y" for r in group)

    start = col["genitive_case"]
    with OUT.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["feature", "det", "pron", "A_pronoun_like", "B_quantity_like", "C_rest",
                    "pattern"])
        for j in range(start, len(header)):
            d, p = n(D, j), n(P, j)
            pattern = ("shared" if d and p else "det only" if d else
                       "pron only" if p else "none")
            w.writerow([header[j], d, p, n(A, j), n(B, j), n(C, j), pattern])

    # Four-gamete (pairwise compatibility) test across the determinative forms:
    # two binary characters fit one tree without homoplasy only if the forms
    # don't show all four combinations of their values.
    with COMPAT.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["pronoun_like_feature", "quantity_like_feature", "combinations",
                    "compatible", "forms_with_both"])
        bad = 0
        for a in PRON_LIKE:
            for b in QUANT_LIKE:
                combos = {(r[col[a]] == "y", r[col[b]] == "y") for r in D}
                both = [r[0] for r in D if r[col[a]] == "y" and r[col[b]] == "y"]
                bad += len(combos) == 4
                w.writerow([a, b, len(combos), len(combos) < 4, " ".join(both)])

    print(f"forms: {len(D)} determinatives, {len(P)} pronouns")
    for name, g in (("A pronoun-like", A), ("B quantity-like", B), ("C rest", C)):
        print(f"{name} ({len(g)}): {', '.join(r[0] for r in g)}")
    print(f"four-gamete: {bad} of {len(PRON_LIKE) * len(QUANT_LIKE)} pairs incompatible")
    print(f"wrote {OUT.relative_to(ROOT)}, {COMPAT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
