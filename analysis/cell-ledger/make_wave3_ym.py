#!/usr/bin/env python3
"""Packets for wave 3 and the y-to-m pass (24 Oct 2026, after Brett's review).

wave3: the 20 columns Brett revised and the 4 he added, recoded blind on the
       new definitions, for the 18 reference rows and 8 calibration forms;
       one packet; all three coders. The intro states the head rule and asks
       for m wherever a use is possible but degraded.
ym:    the y-to-m pass (codebook pass 2): Brett's 2021 y cells in the 62
       columns whose definitions are settled (no revised, gender, form,
       derived, label or unclear column), graded y / m / n by Muse and
       Claude; six packets.

Usage: python3 analysis/cell-ledger/make_wave3_ym.py OUT_DIR
Writes OUT_DIR/wave3-p1/PACKET.md, OUT_DIR/ym-pN/PACKET.md, and maps.
"""
import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CB = ROOT / "analysis" / "codebook"
REVISED = ["paradigm_has_genitive_form", "definite", "semantically_uncountable", "semantically_countable",
           "can_be_modified_by_not", "can_be_modified_by_at_least", "takes_adverb_quite_as_a_modifier",
           "can_be_modified_by_almost", "can_be_modified_by_approximately", "can_be_modified_by_hardly",
           "functions_as_degree_modifier_in_AdjP", "functions_as_subject_of_present_participal_of_joining_you",
           "functions_as_determiner_in_day_s_time_ago", "Coordinates_with_dependent_genitives",
           "May_coordinate_with_non_fused_determiners", "takes_else_or_more_as_a_post_head_dependent",
           "deictic_marker", "pro_form", "functions_as_attrib_modifier_in_nominal",
           "functions_as_prehead_modifier_in_nominal"]
NEW = ["definite_reference_possible", "at_least_focus", "takes_more_as_a_post_head_dependent",
       "inflects_for_dependent_independent_use"]
CALIB = ["some", "few", "each", "this", "someone", "she", "which_int_det", "the"]

COMMON = """Thank you for helping. This is part of a descriptive grammar of English: we need your independent judgment of what each word form below can do. Please use no tools and consult no files or sources; the judgments should be your own. Think carefully, but keep the output to the format at the end.

Two conventions hold throughout:
- **The head of a phrase like *the dog* is *dog*, not *the*.** Where a column says a modifier attaches to a phrase the form heads, *quite the scholar* doesn't count for *the*: *quite* is the sibling of an NP headed by *scholar*.
- **Use m** wherever a use is possible but sounds degraded to speakers generally. Don't round a degraded use up to y or down to n.

A use available only in some varieties or registers is y, with a note beginning "variety:". A mistake, a quotation, a pun, or an unrelated word with the same spelling (*lot* meaning a plot of land, *number* the verb) doesn't count. A use for a kind of individual, with an article or a plural (*the Smiths*, *an Ophelia*), isn't a different word for this task, whatever the form: grade it separately, with a note beginning "set:".
"""


# Coder-facing wording where the codebook definition cites CGEL, lists answers for
# forms being coded, or names categories.
CODER_DEF = {
    "definite": ("It makes the NP it determines or heads definite, as the does in the dog: a classification, not merely occurring in a definite NP.", "the dog", "a dog"),
    "can_be_modified_by_not": ("Not modifies the phrase the form heads, as part of that phrase (not many, not all, not a little), not as negation of a whole constituent (not the teacher but the student).", "not many", ""),
    "can_be_modified_by_at_least": ("At least as a lower bound on a quantity (at least two, at least a little).", "at least two", ""),
    "deictic_marker": ("Its meaning is anchored to the speech situation: the speaker, the addressee, or the time or place of speaking (I, you, here, now, next week). A third-person form used with pointing doesn't count, and neither does reference back to an antecedent.", "next week", ""),
    "pro_form": ("It can stand for a phrase recoverable from context, as an anaphoric pro-form. Interrogatives and dummies (It's raining) don't count.", "", ""),
    "inflects_for_dependent_independent_use": ("It is one of a pair of distinct inflectional forms for dependent and independent use (my book / the book is mine).", "my", "his (one form for both)"),
    "functions_as_subject_determiner": ("It, or an NP it heads, can be a genitive in determiner function, whether the genitive is a form of its own (my book) or made with 's (anybody's guess).", "my", ""),
    # Redefined 24 Oct (codebook section 5); the override follows the new sense.
    "existential": ("It expresses existential quantification, positive or negative: it asserts or denies that there is something meeting a description. A form with no quantificational meaning, such as a dummy, is x.", "several", ""),
}


SUFFIXES = ("_det", "_pron", "_int", "_rel", "_acc", "_dep", "_plain", "_dum", "_sing", "_plur", "_s")


def words_of(forms, exempt=True):
    """Words naming the coded forms, for screening examples. With exempt=True (examples
    inside definitions) a, I and the are skipped as too common; anchors are screened
    with exempt=False, since an anchor names the form it is about."""
    out = set()
    for f in forms:
        w = f
        for s in SUFFIXES:
            if w.endswith(s):
                w = w[: -len(s)]
        w = w.replace("_", " ").lower()
        if not exempt or w not in ("a", "i", "the"):
            out.add(w)
    return out


def screen(text, words):
    """Drop parenthetical examples and anchor strings that name a coded form."""
    import re as _re
    def hit(s):
        s2 = " " + _re.sub(r"[^a-z' ]", " ", s.lower()) + " "
        return any(" " + w + " " in s2 for w in words)
    return _re.sub(r" \([^()]*\)", lambda m: "" if hit(m.group(0)) else m.group(0), text), hit


def clean(d):
    for k in ("RECODE (Brett, 24 Oct: the 2021 column was wrong): ", "SPLIT: "):
        d = d.replace(k, "")
    for k in (" (Brett, 24 Oct)", " (Brett, 24 Oct: the 2021 column was wrong)"):
        d = d.replace(k, "")
    d = d.replace(" Taking 's is a separate column (accepts_genitive_apstrophe_s); 's is not counted morphologically.",
                  " A genitive formed by adding 's isn't counted.")
    d = d.split(" CHECK:")[0].split(" n in 2021")[0]
    import re as _re
    return _re.sub(r" \(CGEL[^)]*\)", "", d)


def main():
    out = Path(sys.argv[1])
    defs = {r["column"]: r for r in csv.DictReader((CB / "definitions.csv").open())}
    cols = {r["column"]: r for r in csv.DictReader((CB / "columns.csv").open())}
    forms = list(csv.DictReader((CB / "forms.csv").open()))
    label = {f["form"]: f["blind_label"] for f in forms}

    # wave 3
    rows = [f["form"] for f in forms if f["source"].startswith("reference")] + \
           [f["form"] for f in forms if f["form"] in CALIB]
    wcols = REVISED + NEW
    W3 = words_of(rows)
    d = out / "wave3-p1"
    d.mkdir(parents=True, exist_ok=True)
    L = ["# What can these English words do? A coding task", "", COMMON,
         "## Values", "", "- **y**: the form can do this (one clear, natural example is enough);",
         "- **m**: it can, but only in a degraded way;", "- **n**: it never does;",
         "- **x**: not applicable (the question can't arise for this form).", "",
         "## Forms", "", "| id | form |", "|---|---|"]
    L += [f"| R{i + 1:02d} | {label[f]} |" for i, f in enumerate(rows)]
    L += ["", "## Columns", ""]
    for k, c in enumerate(wcols, start=1):
        dd = dict(defs[c])
        if c in CODER_DEF:
            dd["definition"], dd["anchor_y"], dd["anchor_n"] = CODER_DEF[c]
        text, _ = screen(clean(dd["definition"]), W3)
        _, hit = screen("", words_of(rows, exempt=False))
        ay = dd["anchor_y"] if dd["anchor_y"] and not hit(dd["anchor_y"]) else ""
        an = dd["anchor_n"] if dd["anchor_n"] and not hit(dd["anchor_n"]) else ""
        anchors = (f" Yes: *{ay}*." if ay else "") + (f" No: *{an}*." if an else "")
        L.append(f"- **C{k:02d}**: {text}{anchors}")
    L += ["", "Column order for the output: " + " ".join(f"C{k:02d}" for k in range(1, len(wcols) + 1)), "",
          "## Output (follow exactly)", "", "```", "CODES", "R01: <one value per column, in order, separated by spaces>",
          "...", "NOTES", "R07 | C05 | n | strongest y considered: \"...\" (C) | why it fails", "...", "FRAMES",
          "<new frame or reading> | example | columns it affects", "```", "",
          "Notes are required for every n (the strongest y you considered, ten words or fewer, C constructed or A attested with source, and why it fails; \"none\" if no candidate), for every m (example and why it's degraded), and for a y only if it isn't obvious. One line each. Stop when the three sections are done."]
    (d / "PACKET.md").write_text("\n".join(L))
    (out / "wave3-map.json").write_text(json.dumps(
        {"rows": {f"R{i + 1:02d}": f for i, f in enumerate(rows)},
         "packets": {"p1": {f"C{k:02d}": c for k, c in enumerate(wcols, start=1)}}}, indent=1))

    # y-to-m pass
    m = list(csv.reader((ROOT / "analysis" / "matrix-2026-10" / "matrix-2026-10.csv").open()))
    h, mrows = m[0], m[1:]
    settled = [c for c in h[h.index("genitive_case"):] if cols[c]["type"] == "possibility"
               and c not in REVISED and cols[c]["super_column"] != "gender"
               and "UNCLEAR" not in defs[c]["definition"]]
    fid = {f: f"F{i + 1:03d}" for i, f in enumerate(r[0] for r in mrows)}
    items = [(c, [r[0] for r in mrows if r[h.index(c)] == "y"]) for c in settled]
    total = sum(len(v) for _, v in items)
    npk = 6
    target = total / npk
    packets, cur, n = [], [], 0
    for c, fs in items:
        cur.append((c, fs))
        n += len(fs)
        if n >= target and len(packets) < npk - 1:
            packets.append(cur)
            cur, n = [], 0
    if cur:
        packets.append(cur)
    ymap = {"forms": {v: k for k, v in fid.items()}, "packets": {}}
    for p, pk in enumerate(packets, start=1):
        used = sorted({f for _, fs in pk for f in fs}, key=lambda f: fid[f])
        d = out / f"ym-p{p}"
        d.mkdir(parents=True, exist_ok=True)
        L = ["# How available is each use? A grading task", "", COMMON,
             "Each form listed under a column below has been claimed to have that property. For each listed form, grade the claim:",
             "", "- **y**: fully available in the form's ordinary use;", "- **m**: available, but degraded;",
             "- **n**: not actually available.", "",
             "## Forms", "", "| id | form |", "|---|---|"]
        L += [f"| {fid[f]} | {label[f]} |" for f in used]
        L += ["", "## Columns, each with the forms claimed to have it", ""]
        cmap = {}
        for k, (c, fs) in enumerate(pk, start=1):
            dd = dict(defs[c])
            if c in CODER_DEF:
                dd["definition"], dd["anchor_y"], dd["anchor_n"] = CODER_DEF[c]
            text, _ = screen(clean(dd["definition"]), words_of(used))
            _, hit = screen("", words_of(used, exempt=False))
            ay = dd["anchor_y"] if dd["anchor_y"] and not hit(dd["anchor_y"]) else ""
            anchors = (f" Yes: *{ay}*." if ay else "")
            L.append(f"- **C{k:02d}**: {text}{anchors}")
            L.append(f"  - forms: {', '.join(fid[f] for f in fs)}")
            cmap[f"C{k:02d}"] = c
        L += ["", "## Output (follow exactly)", "", "```", "GRADES",
              "C01: F003 y, F017 m, F040 n, ...   (every listed form, in the order given)", "...",
              "NOTES", "F017 | C01 | m | example | why degraded",
              "F040 | C01 | n | strongest y considered: \"...\" (C) | why it fails", "```", "",
              "Notes only for m and n, one line each. Stop when both sections are done."]
        (d / "PACKET.md").write_text("\n".join(L))
        ymap["packets"][f"p{p}"] = {"columns": cmap, "cells": sum(len(fs) for _, fs in pk)}
    (out / "ym-map.json").write_text(json.dumps(ymap, indent=1))
    print(f"wave 3: {len(rows)} forms x {len(wcols)} columns; y-to-m: {total} cells in {len(packets)} packets: "
          + ", ".join(str(v["cells"]) for v in ymap["packets"].values()))


if __name__ == "__main__":
    main()
