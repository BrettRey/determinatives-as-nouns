#!/usr/bin/env python3
"""Assemble and validate census.json against schema.json and the manuscript text."""

import importlib.util
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

STATUSES = {"licensed", "excluded", "conditional", "not_stated"}
EVIDENCE = {
    "cgel_described", "cgel_restricted", "constructed_illustration",
    "constructed_ungrammatical", "retained_attestation", "searched_not_found",
    "authors_analysis", "not_determinable",
}

RESPONSIBILITY = (
    "This census was produced by Aristotle (Harmonic) by reading the manuscript "
    "sections supplied in task.json and recording the participation claims they make. "
    "Each entry reports what the manuscript asserts, with the basis the manuscript "
    "itself gives; recording a claim is not an endorsement of it, and evidence_type "
    "classifies the manuscript's stated grounds rather than assessing their strength. "
    "Every quote is an exact substring of the supplied section text, including LaTeX "
    "markup, and no source text was edited. Claim individuation follows the "
    "instructions in task.json: a distinct expression or a distinct construction "
    "yields a distinct claim, so a single sentence can license several entries, and "
    "per-section counts are the actual number of entries recorded for that section. "
    "Judgement was required in deciding which sentences state a participation claim "
    "rather than a taxonomic, semantic, or methodological point; borderline cases are "
    "flagged in the note field. Responsibility for the manuscript's own analysis "
    "remains with its author."
)


ZERO_NOTES = {
    "sec:proposal": (
        "Genuinely zero. The section is a two-sentence framing passage: it observes that "
        "the existing Noun category is internally varied and poses the question the "
        "following subsections answer, without asserting of any expression that it does, "
        "does not, or conditionally does occur in a syntactic function or construction."
    ),
    "sec:economy": (
        "Genuinely zero. The section defines what a grammatical fragment is and states how "
        "the four accounts will be compared. It makes no assertion about the occurrence of "
        "any expression in any function or construction."
    ),
}


def load(name):
    path = os.path.join(HERE, "parts", name)
    spec = importlib.util.spec_from_file_location(name[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.CLAIMS


def main():
    task = json.load(open(os.path.join(ROOT, "task.json")))
    sections = {s["label"]: s["text"] for s in task["sections"]}
    order = [s["label"] for s in task["section_inventory"]]

    raw = []
    for i in range(1, 12):
        raw.extend(load("part%d.py" % i))

    claims = []
    seen_ids = set()
    errors = []
    for (cid, label, expr, constr, status, evidence, quote, cond, note) in raw:
        if cid in seen_ids:
            errors.append("duplicate id: %s" % cid)
        seen_ids.add(cid)
        if label not in sections:
            errors.append("%s: unknown section %s" % (cid, label))
        elif quote not in sections[label]:
            errors.append("%s: quote not an exact substring of %s:\n    %r" % (cid, label, quote))
        if status not in STATUSES:
            errors.append("%s: bad status %s" % (cid, status))
        if evidence not in EVIDENCE:
            errors.append("%s: bad evidence_type %s" % (cid, evidence))
        if not quote:
            errors.append("%s: empty quote" % cid)
        item = {
            "id": cid,
            "section_label": label,
            "expression": expr,
            "construction": constr,
            "status": status,
            "evidence_type": evidence,
            "quote": quote,
        }
        if cond:
            item["condition"] = cond
        if note:
            item["note"] = note
        claims.append(item)

    if errors:
        print("VALIDATION ERRORS (%d):" % len(errors))
        for e in errors:
            print(" -", e)
        sys.exit(1)

    # Order claims by section inventory order, keeping within-section order.
    claims.sort(key=lambda c: order.index(c["section_label"]))

    counts = []
    for label in order:
        n = sum(1 for c in claims if c["section_label"] == label)
        row = {"section_label": label, "claims_recorded": n}
        if n == 0:
            row["note"] = ZERO_NOTES[label]
        counts.append(row)

    out = {
        "claims": claims,
        "section_counts": counts,
        "responsibility_notice": RESPONSIBILITY,
    }
    with open(os.path.join(ROOT, "census.json"), "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print("claims: %d" % len(claims))
    for row in counts:
        print("  %-24s %3d" % (row["section_label"], row["claims_recorded"]))


if __name__ == "__main__":
    main()
