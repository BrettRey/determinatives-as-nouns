#!/usr/bin/env python3
"""Make blind-coding packets from the codebook tables (wave 2, 24 Oct 2026).

Wave 2 codes the 18 reference-set rows (nouns and adjectives) on every column
the pilot didn't cover, excluding facts of form, derived and unclear columns,
and the analysis label; columns worded as universals are given in their
reversed, possibility form. Gender is coded under both candidate definitions
so that Brett's fork can be settled without recoding. Eight pronoun and
determinative forms are included in every packet for calibration against
Brett's 2021 cells. Coders see plain labels only.

Usage: python3 analysis/cell-ledger/make_packets.py OUT_DIR
Writes OUT_DIR/wave2-pN/PACKET.md and OUT_DIR/wave2-map.json.
"""
import csv
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CB = HERE.parent / "codebook"
PILOT = {"personal_gender_as_head_or_fused_head", "non_personal_gender", "semantically_singular",
         "semantically_plural", "Must_be_stressed_as_object_after_particle", "takes_prehead_AdjP_modifier",
         "takes_relative_clause_modifier", "takes_post_head_AdjP", "takes_ly_adverb_modifier",
         "functions_as_head_of_partitive_construction", "heads_nominal_after_separate_determiner"}
CALIB = ["some", "few", "each", "this", "someone", "she", "which_int_det", "the"]
GENDER = [
    ("gender_ref_personal", "When it refers, it can select personal pro-forms (who, he, she): the doctor ... she; the few who came.",
     "the doctor ... who", "the table ... *who"),
    ("gender_ref_nonpersonal", "When it refers, it can select non-personal pro-forms (it, which): the table ... it.",
     "the table ... which", "she ... *which"),
    ("gender_lex_personal", "The word itself fixes personal gender, whatever it refers to (someone, she; not dog, few).",
     "someone", "something"),
    ("gender_lex_nonpersonal", "The word itself fixes non-personal gender, whatever it refers to (something, it; not dog, few).",
     "something", "someone"),
]
INTRO = """# What can these English words do? A coding task

Thank you for helping. This is part of a descriptive grammar of English: we need your independent judgment of what each word form below can do. Please use no tools and consult no files or sources; everything you need is here, and the judgments should be your own. Think carefully, but keep the output to the format at the end.

## Values

- **y**: the form can do this (one clear, natural example is enough);
- **m**: it can, but only in a way that sounds degraded to speakers generally;
- **n**: it never does;
- **x**: not applicable (the question can't arise for this form).

If something is available only in some varieties or registers, code it **y** and add a note beginning "variety:". If it's available only in a special construction or reading, code it as you would without that and propose the construction or reading as a new frame at the end. Code each form in its ordinary uses. A mistake, a quotation, a pun, or an unrelated word with the same spelling (*a lot* meaning a plot of land; *number* the verb) doesn't count. A use for a kind of individual, with an article or a plural (*the Smiths*, *an Ophelia*), isn't a different word for this task, whatever the form: grade it separately, with a note beginning "set:". "It" in a column means the form, as the main word of its phrase unless the column says otherwise.
"""
OUTRO = """
## Output (follow exactly)

```
CODES
R01: <one value per column, in the column order above, separated by spaces>
...
NOTES
R07 | C05 | n | strongest y considered: "..." (C) | why it fails
...
FRAMES
<new frame or reading> | example | columns it affects
```

Notes are required for **every n** (the strongest y you considered, ten words or fewer, marked C for constructed or A for attested with the source, and a few words on why it fails; "none" if you can think of no candidate), for **every m** (example and why it's degraded), and for **a y only if it isn't obvious**. Keep each note to one line. Stop when the three sections are done.
"""


def main():
    out = Path(sys.argv[1])
    cols = list(csv.DictReader((CB / "columns.csv").open()))
    defs = {r["column"]: r for r in csv.DictReader((CB / "definitions.csv").open())}
    forms = list(csv.DictReader((CB / "forms.csv").open()))
    keep = []
    for c in cols:
        if c["type"] in ("form", "derived", "label", "unclear") or c["column"] in PILOT:
            continue
        if c["super_column"] == "gender":
            continue
        d = defs[c["column"]]
        if "UNCLEAR" in d["definition"]:
            continue
        text = d["definition"].split(" n in 2021")[0].replace(" (CGEL's subject-determiner)", "")
        text = text.replace("RECODE as may_follow_particle_unstressed_as_object: ", "").replace(
            "RECODE as may_occur_without_a_binder: ", "").split(" CHECK:")[0]
        keep.append((c["column"], c["super_column"], text, d["anchor_y"], d["anchor_n"]))
    keep += [(g, "gender", t, ay, an) for g, t, ay, an in GENDER]
    rows = [f for f in forms if f["source"].startswith("reference")] + \
           [f for f in forms if f["form"] in CALIB]
    # three packets, columns grouped by super-column
    keep.sort(key=lambda k: k[1])
    n = 3
    size = -(-len(keep) // n)
    packets = [keep[i:i + size] for i in range(0, len(keep), size)]
    mapping = {"rows": {f"R{i + 1:02d}": f["form"] for i, f in enumerate(rows)}, "packets": {}}
    for p, pcols in enumerate(packets, start=1):
        d = out / f"wave2-p{p}"
        d.mkdir(parents=True, exist_ok=True)
        lines = [INTRO, "## Forms", "", "| id | form |", "|---|---|"]
        lines += [f"| R{i + 1:02d} | {f['blind_label']} |" for i, f in enumerate(rows)]
        lines += ["", "## Columns", ""]
        ids = []
        for k, (cid, fam, text, ay, an) in enumerate(pcols, start=1):
            code = f"C{k:02d}"
            ids.append(code)
            anchors = (f" Yes: *{ay}*." if ay else "") + (f" No: *{an}*." if an else "")
            lines.append(f"- **{code}** ({fam.replace('_', ' ')}): {text}{anchors}")
        lines += ["", "Column order for the output: " + " ".join(ids), OUTRO]
        (d / "PACKET.md").write_text("\n".join(lines))
        mapping["packets"][f"p{p}"] = {code: cid for code, (cid, *_) in zip(ids, pcols)}
    (out / "wave2-map.json").write_text(json.dumps(mapping, indent=1))
    print(f"{len(rows)} forms; {len(keep)} columns in {len(packets)} packets: "
          + ", ".join(str(len(p)) for p in packets))


if __name__ == "__main__":
    main()
