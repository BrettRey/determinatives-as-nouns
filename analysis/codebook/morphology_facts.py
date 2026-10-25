#!/usr/bin/env python3
"""Draft values for the morphology facts (24 Oct 2026), for Brett to check.

Brett, 24 Oct: morphology needs columns "for each of the words and their roots"
("I meant the bases, but both apply"), a column for each base ("there should be
a thing column"), a "takes plural -(e)s" column, and morphology columns for the
new noun rows. This drafts every fact column by rule, from the spelling, the
2021 compound_word column, and CGEL (p. 410: the dependent/independent pairs;
p. 423: compound determinatives join a determinative base to a nominal base,
body, one, thing, where). takes_plural_es is a possibility claim with a frame
split, so it goes to the blind coders, not here.

Writes analysis/codebook/morphology-facts.csv: form, column, value, basis, check.
"check" marks a cell the rule doesn't settle. All values are Claude's proposals.
"""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

BASES = {
    "base_body": "anybody everybody nobody somebody",
    "base_one": "anyone everyone no_one someone",
    "base_thing": "anything everything nothing something",
    "base_where": "anywhere everywhere nowhere somewhere",
    "base_self": "himself herself itself myself oneself ourselves themself themselves yourself yourselves",
    "base_other": "another each_other one_another",
    "base_ever": "whoever whomever whatever_det whatever_pron whichever_rel_det whichever_int_det whoever_s whosever",
    "base_soever": "whosoever whosoever_s",
    "base_day": "today yesterday",
    "base_night": "tonight",
    "base_morrow": "tomorrow",
    "base_every": "everybody everyone everything everywhere",
    "base_some": "somebody someone something somewhere somewhat",
    "base_any": "anybody anyone anything anywhere",
    "base_no": "nobody no_one nothing nowhere",
    "base_wh": "whoever whomever whatever_det whatever_pron whichever_rel_det whichever_int_det whoever_s whosever whosoever whosoever_s somewhat",
    "base_a": "another a_certain a_few a_little a_great_many many_a",
    "base_each": "each_other",
}
# The nominal base's own plural, where the form has one (x where it has none).
BASE_PLURAL = {"body": ("y", "bodies"), "one": ("y", "ones"), "thing": ("y", "things"), "where": ("n", "*wheres outside metalinguistic use"),
               "self": ("y", "selves, with f/v alternation"), "day": ("y", "days"), "night": ("y", "nights"),
               "morrow": ("n", "morrows is archaic at best")}
CHECK = {
    ("one_another", "base_one"): "one here is the numeral or determinative, not CGEL's nominal base one; coded n",
    ("one_another", "base_takes_plural_es"): "no nominal base unless other counts as one (others)",
    ("another", "base_takes_plural_es"): "no nominal base unless other counts as one (others)",
    ("each_other", "base_takes_plural_es"): "no nominal base unless other counts as one (others)",
    ("somewhat", "base_wh"): "some + what; what as a base of a degree adverb-like form",
    ("ourselves", "is_plural_in_es"): "the -s is the plural of the base self, not of the form; coded n",
    ("yourselves", "is_plural_in_es"): "as for ourselves",
    ("themselves", "is_plural_in_es"): "as for ourselves",
    ("his", "is_independent_form"): "his serves both uses (CGEL p. 410 lists no separate pair); coded n",
    ("numerous", "Monmorphemic"): "numer- is a bound root; coded n",
    ("multiple", "Monmorphemic"): "multi- + -ple, or one morpheme synchronically; coded n",
    ("plenty", "Monmorphemic"): "coded y (plenteous is a different word)",
    ("majority", "Monmorphemic"): "major + -ity; coded n",
    ("countless", "Monmorphemic"): "count + -less; coded n",
}
PAIR = {"no", "none"}   # CGEL p. 410, beside the genitive pairs


def main():
    m = list(csv.reader((ROOT / "analysis" / "matrix-2026-10" / "matrix-2026-10.csv").open()))
    h, rows = m[0], {r[0]: r for r in m[1:]}
    forms = list(csv.DictReader((HERE / "forms.csv").open()))
    ref = [f["form"] for f in forms if f["source"].startswith("reference")]
    pair_lex = {f for f, r in rows.items() if r[h.index("paradigm_has_distinct_independent_genitive_form")] == "y"} | PAIR
    out = []

    def add(form, col, val, basis):
        c = CHECK.get((form, col), "")
        out.append({"form": form, "column": col, "value": val, "basis": basis, "check": c})

    for f in [x["form"] for x in forms]:
        compound = (f in rows and rows[f][h.index("compound_word")] == "y")
        add(f, "is_plural_in_es", "y" if f in ("dogs", "numbers", "dozens") else "n", "spelling")
        add(f, "is_comparative_or_superlative_form", "y" if f in ("fewer", "fewest", "less", "least", "more", "most") else "n",
            "CGEL p. 356 (degree determinatives inflect for grade)")
        add(f, "is_independent_form", "y" if f in ("mine", "yours_sing", "yours_plur", "hers", "ours", "theirs_sing", "theirs_plur", "none") else "n",
            "CGEL p. 410")
        add(f, "paradigm_has_dependent_independent_pair", "y" if f in pair_lex else "n",
            "2021 paradigm_has_distinct_independent_genitive_form, plus no and none (CGEL p. 410)")
    # Fact columns the reference rows lack (2021 rows have Brett's values).
    MONO = {"lot", "number", "plenty", "dozen", "dog", "water", "Kim", "Toronto", "rich", "poor", "tall"}
    header = next(csv.reader((ROOT / "analysis" / "matrix-2026-10" / "matrix-2026-10.csv").open()))
    for f in ref:
        for col in header[1:header.index("genitive_case")]:
            add(f, col, "n", "contains none of the 2021 matrix's word parts")
        for col in ("genitive_case", "accusative_case", "nominative_case", "compound_word", "Start_with_th", "Start_with_hw"):
            add(f, col, "n", "not a case form; not a compound; spelling and sound")
        add(f, "Monmorphemic", "y" if f in MONO else "n", "morphemes of the form")
    with (HERE / "morphology-facts.csv").open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["form", "column", "value", "basis", "check"])
        w.writeheader()
        w.writerows(out)
    from collections import Counter
    print(len(out), "cells;", sum(1 for r in out if r["check"]), "to check;",
          dict(Counter((r["column"], r["value"]) for r in out if r["value"] == "y" and r["column"].startswith("base_") and r["column"] != "base_takes_plural_es").most_common(3)))


if __name__ == "__main__":
    main()
