#!/usr/bin/env python3
"""Build the cell ledger (planning/codebook.md, section 8): one row per
(form, column, frame) value claim, with provenance, from every source we have.

Sources, in order:
  1. analysis/matrix-2026-10/matrix-2026-10.csv: judged cells. Provenance
     "Brett 2021" unless the cell is one of the record-backed changes in
     applied_changes.csv (then "matrix-2026-10 change", with the record), or
     the row was added in 2026-10 (whomever).
  2. analysis/matrix-2026-10/corrections.csv: proposed corrections awaiting Brett.
  3. analysis/matrix-2026-10/new_feature_values.csv: the 2026-10 added column.
  4. analysis/noun-coding-2026-10-24/: Claude's draft coding (status on hold).
  5. analysis/codebook/morphology-facts.csv: Claude's draft of the morphology
     facts (base, word and lexeme levels), proposed, 24 Oct.
  6. analysis/cell-ledger/brett-judgments-2026-10-24.csv: Brett's calls on the
     y-to-m sheet (judged), 24 Oct.
  7. blind coder outputs parsed by parse_coders.py, parse_wave.py and parse_ym.py,
     and the register rule's reclassifications (apply_register_rule.py), if
     present (analysis/cell-ledger/coder-cells*.csv).

A judged cell has status "judged". A cell Brett hasn't judged is "accepted"
(Brett, 24 Oct: "agree on accepted separate from judged") when all three model
families coded it alike in one blind run (Codex, Muse, Claude), with no m and no
"set:" or "echo:" note, the register rule applied first; accepted cells await a
random audit by Brett (codebook, fork 7). Facts drafted by rule become accepted
once Brett approves the rules. Everything else is "proposed" or "on hold".
The analysis runs on judged cells alone and on judged plus accepted.

Run: python3 analysis/cell-ledger/build_ledger.py
"""
import csv
import json
import re
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
M = ROOT / "analysis" / "matrix-2026-10"
NC = ROOT / "analysis" / "noun-coding-2026-10-24"
COLS = ROOT / "analysis" / "codebook" / "columns.csv"
OUT = HERE / "cells.csv"
FIELDS = ["form", "super_column", "column", "frame", "value", "variety", "status", "evidence_type",
          "locator", "quote", "note", "proposer", "judged_by", "date"]


def norm(v):
    return {"marginal": "m", "NA": "x"}.get(v, v)


def core(text):
    """A definition's wording without examples, anchors, or punctuation."""
    t = re.sub(r"\*\*C\d\d\*\*\s*(\([^)]*\))?\s*:", "", text)
    t = re.split(r"\s(?:Yes|No):", t)[0]
    while re.search(r"\([^()]*\)", t):
        t = re.sub(r"\s*\([^()]*\)", "", t)
    return " ".join(re.sub(r"[^a-z' ]", " ", t.lower()).split())


def current_wording_matches():
    """(run, column) -> whether the run's packet worded the column as it is defined now."""
    import sys
    sys.path.insert(0, str(HERE))
    from make_wave3_ym import CODER_DEF, clean
    defs = {r["column"]: r for r in csv.DictReader((ROOT / "analysis" / "codebook" / "definitions.csv").open())}
    now = {}
    for c, r in defs.items():
        d = CODER_DEF[c][0] if c in CODER_DEF else r["definition"]
        now[c] = core(clean(d))
    out = {}
    for run, rundir, prefix in (("wave2", "external-blind-coding-wave2-20261024", "wave2"),
                                ("wave3", "external-blind-coding-wave3-20261024", "wave3")):
        base = ROOT / "reviews" / rundir
        if not (base / f"{prefix}-map.json").exists():
            continue
        mp = json.loads((base / f"{prefix}-map.json").read_text())
        for pk, cmap in mp["packets"].items():
            text = (base / f"{prefix}-{pk}" / "PACKET.md").read_text()
            for line in text.splitlines():
                mm = re.match(r"- \*\*(C\d\d)\*\*", line)
                if mm and mm.group(1) in cmap:
                    col = cmap[mm.group(1)]
                    out[(run, col)] = core(line) == now.get(col)
    return out


def main():
    fam = {r["column"]: r["super_column"] for r in csv.DictReader(COLS.open())}
    rows = []

    def add(**kw):
        r = {k: "" for k in FIELDS}
        r.update(kw)
        r["super_column"] = fam.get(r["column"], "")
        r["frame"] = r["frame"] or "default"
        rows.append(r)

    m = list(csv.reader((M / "matrix-2026-10.csv").open()))
    header, forms = m[0], m[1:]
    start = 1  # every matrix column, the 2021 word-part columns included (24 Oct)
    applied = {(r["form"], r["feature"]): r for r in csv.DictReader((M / "applied_changes.csv").open())}
    for f in forms:
        for j in range(start, len(header)):
            key = (f[0], header[j])
            if key in applied:
                a = applied[key]
                add(form=f[0], column=header[j], value=norm(f[j]), status="judged",
                    evidence_type="record", locator=a["record"], note=a["evidence"],
                    proposer="matrix-2026-10 change", judged_by="Brett", date="2026-10")
            elif f[0] == "whomever":
                add(form=f[0], column=header[j], value=norm(f[j]), status="proposed",
                    evidence_type="", proposer="matrix-2026-10 (row added)", date="2026-10")
            else:
                add(form=f[0], column=header[j], value=norm(f[j]), status="judged",
                    evidence_type="Brett judgment", proposer="Brett 2021", judged_by="Brett", date="2021")

    for r in csv.DictReader((M / "corrections.csv").open()):
        add(form=r["form"], column=r["feature"], value=norm(r["proposed_value"]), status="proposed",
            evidence_type=r["source_type"], locator=r["source"], note=r["note"],
            proposer="matrix-2026-10 corrections (needs Brett: %s)" % r["needs_brett"], date="2026-10")

    for r in csv.DictReader((M / "new_feature_values.csv").open()):
        add(form=r["form"], column=r["feature_id"], value=norm(r["proposed_value"]), status="proposed",
            evidence_type=r["source_type"], locator=r["source"],
            proposer="matrix-2026-10 new feature (needs Brett: %s)" % r["needs_brett"], date="2026-10")

    for fname in ("proposed-new-rows.csv", "proposed-new-columns.csv"):
        t = list(csv.reader((NC / fname).open()))
        for r in t[1:]:
            for j, c in enumerate(t[0][1:], start=1):
                if fname == "proposed-new-columns.csv" and c == "heads_nominal_after_separate_determiner":
                    continue  # already in from new_feature_values.csv
                add(form=r[0], column=c, value=norm(r[j]), status="on hold",
                    proposer="Claude draft 2026-10-24 (superseded by codebook)", date="2026-10-24")

    for r in csv.DictReader((ROOT / "analysis" / "codebook" / "morphology-facts.csv").open()):
        add(form=r["form"], column=r["column"], value=r["value"], status="proposed", evidence_type="fact of form",
            note="; ".join(x for x in (r["basis"], r["check"] and "CHECK: " + r["check"]) if x),
            proposer="Claude morphology facts 2026-10-24", date="2026-10-24")

    for r in csv.DictReader((HERE / "brett-judgments-2026-10-24.csv").open()):
        add(**{k: r.get(k, "") for k in FIELDS if k != "super_column"})
    bc = HERE / "brett-block-check-2026-10-24.csv"
    if bc.exists():  # Brett's check of the block cells; supersedes their accepted values
        for r in csv.DictReader(bc.open()):
            add(**{k: r.get(k, "") for k in FIELDS if k != "super_column"})
    nm = HERE / "brett-nm-rulings-2026-10-24.csv"
    if nm.exists():  # Brett's block rulings and the multiverse arms from the n-to-m sheet
        for r in csv.DictReader(nm.open()):
            add(**{k: r.get(k, "") for k in FIELDS if k != "super_column"})

    for coder in sorted(HERE.glob("coder-cells*.csv")):
        for r in csv.DictReader(coder.open()):
            add(**{k: r.get(k, "") for k in FIELDS if k != "super_column"})

    # Accepted by agreement: one row per cell where all three families agree.
    ctype = {r["column"]: r["type"] for r in csv.DictReader(COLS.open())}
    judged = {(r["form"], r["column"]) for r in rows if r["status"] == "judged"}
    override = {}
    for r in rows:
        if r["proposer"].startswith("register rule"):
            override[(r["form"], r["column"], r["proposer"].split(" on ", 1)[1])] = r["value"]
    runs = defaultdict(dict)
    for r in rows:
        pr = r["proposer"]
        if not pr.startswith("blind coder "):
            continue
        fam_, run = pr.split()[2], pr.split("(", 1)[1].split(",")[0]
        v = override.get((r["form"], r["column"], pr), r["value"])
        runs[(r["form"], r["column"], r["frame"], run)][fam_] = (v, r["note"])
    # Only where the coders answered the current question (a side agent's note,
    # 24 Oct): the column's wording in the run's packet must match its current
    # definition, examples and anchors aside. The pilot used an earlier scheme
    # (frames, its own codes, gender one way), so none of its cells qualify.
    same_def = current_wording_matches()
    # Columns marked for blind recoding after today's redesign (a frame added or
    # the sense changed) predate every run so far, whatever their wording.
    recode = {r["column"] for r in csv.DictReader(COLS.open()) if "recode blind" in r["action"]}
    acc = 0
    for (form, col, frame, run), byfam in sorted(runs.items()):
        if set(byfam) != {"CODEX", "MUSE", "CLAUDE"} or (form, col) in judged:
            continue
        if not same_def.get((run, col)) or col in recode:
            continue
        if ctype.get(col) not in ("possibility", "universal"):
            continue
        vals = {v for v, _ in byfam.values()}
        if len(vals) != 1 or "m" in vals or any(n.lstrip("ymnx |").lower().startswith(("set:", "echo:")) or
                                                 " set:" in n or " echo:" in n for _, n in byfam.values()):
            continue
        add(form=form, column=col, frame=frame, value=vals.pop(), status="accepted",
            evidence_type="three model families agree", note=f"blind run {run}; awaiting Brett's audit",
            proposer="agreement rule (Brett, 24 Oct)", date="2026-10-24")
        acc += 1

    with OUT.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=FIELDS)
        w.writeheader()
        w.writerows(rows)
    from collections import Counter
    print(len(rows), "ledger rows;", dict(Counter(r["status"] for r in rows)))
    print("by proposer:", dict(Counter(r["proposer"].split(" (")[0] for r in rows)))


if __name__ == "__main__":
    main()
