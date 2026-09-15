#!/usr/bin/env python3
"""Add evidence_type and subcategory to the extracted claim set.

The source run (analysis/expanded-json-2026-09-14) is a provenance bundle with
recorded hashes and a documented acceptance, so it is READ ONLY.  This script
writes a derived file, claims-enriched.json, and verifies that every original
field survives unchanged.

Two fields are added.

subcategory (on each lexeme)
    Which of the paper's four coordinate subcategories of Noun the lexeme
    belongs to, or `adjective (control)' for the contrast class.  Each carries
    the manuscript grounding for the assignment.  This is analyst-assigned:
    records.json has no category field.

evidence_type (on each participation claim)
    DECLARED ONLY.  The quantifier supplement defines its own evidential
    vocabulary in the caption of tab:quant-controls, and each of the 54
    supplement claims states which one applies.  Those 54 are classified from
    that declaration.  The 56 manuscript claims declare no evidential basis, so
    their evidence_type is null and they instead carry evidence_signals: a list
    of features actually detectable in the quoted evidence.

    A signal is an observable, not an epistemic type.  `cgel_cited' means a
    CGEL citation appears in the claim's evidence or conditions; it does not
    mean the claim rests on CGEL's authority.  Do not collapse signals into a
    type: a first attempt to classify evidence by keyword matching returned 50
    of 54 supplement claims as attestation-backed when the declared answer is
    22, because every claim carries the shared NOW/COCA footnote in its
    evidence list.  That failure is why this field is declaration-driven.
"""

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "analysis" / "expanded-json-2026-09-14"
OUT = ROOT / "analysis" / "claims" / "claims-enriched.json"
ASSIGN = ROOT / "analysis" / "evidence-type-2026-09-14" / "assignments.json"

# ---------------------------------------------------------------- subcategory

# (subcategory, grounding).  "CGEL/paper default" marks the uncontroversial
# determinative inventory the paper takes over without separate argument.
SUBCATEGORY = {
    "lex_the": ("determinative", "CGEL/paper default"),
    "lex_a": ("determinative", "CGEL/paper default"),
    "lex_every": ("determinative", "CGEL/paper default"),
    "lex_some": ("determinative", "CGEL/paper default"),
    "lex_few": ("determinative", "CGEL/paper default"),
    "lex_no": ("determinative", "CGEL/paper default"),
    "lex_many": ("determinative", "CGEL/paper default"),
    "lex_much": ("determinative", "CGEL/paper default"),
    "lex_little": ("determinative", "CGEL/paper default"),
    "lex_several": ("determinative", "supplement: CGEL includes several among determinatives"),
    "lex_all": ("determinative", "CGEL/paper default"),
    "lex_both": ("determinative", "CGEL/paper default"),
    "lex_any": ("determinative", "CGEL/paper default"),
    "lex_enough": ("determinative", "CGEL/paper default"),
    "lex_this": ("determinative", "CGEL/paper default"),
    "lex_that": ("determinative", "CGEL/paper default"),
    "lex_certain": ("determinative", "supplement: CGEL treats certain/various as marginal determinatives"),
    "lex_various": ("determinative", "supplement: CGEL treats certain/various as marginal determinatives"),
    "lex_anyone": ("determinative", "ms: 'anyone takes the premodifiers of its determinative base any'"),
    "lex_something": ("determinative", "ms: 'Compound determinatives also take post-head adjectives'"),
    "lex_ten": ("determinative", "cardinal numeral, treated with the determinative inventory"),
    "lex_thirty": ("determinative", "cardinal numeral, treated with the determinative inventory"),
    "lex_my": ("pronoun", "ms: 'Dependent my and independent mine belong to one pronoun paradigm'"),
    "lex_book": ("common noun", "the paper's plain common-noun control"),
    "lex_lot": ("common noun", "ms: CGEL categorizes quantificational plenty/lot as common nouns"),
    "lex_lots": ("common noun", "quantificational common noun, with lot"),
    "lex_heaps": ("common noun", "quantificational common noun, with lot"),
    "lex_deal": ("common noun", "ms: 'Quantificational nouns occur in degree modifiers such as a great deal smaller'"),
    "lex_plenty": ("common noun", "ms: CGEL categorizes quantificational plenty as a common noun"),
    "lex_numerous": ("adjective (control)", "ms 2.3 'Quantificational adjectives and nominal independence'"),
    "lex_multiple": ("adjective (control)", "ms 2.3"),
    "lex_countless": ("adjective (control)", "ms 2.3"),
    "lex_rich": ("adjective (control)", "ms: 'only the former has a noun as lexical head'"),
    "lex_second": ("adjective (control)", "ms: 'Adjective fusion permits indefinite ordinal a second'"),
}

# -------------------------------------------------------------- evidence_type

# The supplement's own vocabulary, from the caption of tab:quant-controls.
BASIS = re.compile(r"Evidential basis stated in the supplement's comparison table: (.+)")
DECLARED = [
    ("a numbered reference to a retained attestation", "retained_attestation"),
    (r'\textit{I}', "constructed_illustration"),
    ('G, "described in', "cgel_described"),
    ('R, "restricted there"', "cgel_restricted"),
]

# Observable features of the quoted evidence, for claims that declare no basis.
SIGNALS = [
    ("cgel_cited", re.compile(r"\\(citep|citealp|textcite)|\\textit\{CGEL\}")),
    ("ungrammaticality_marked", re.compile(r"\\ungram\{")),
    ("corpus_attestation", re.compile(r"\\href|\bNOW\b|\bCOCA\b")),
]


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    src = RUN / "records.json"
    before = sha256(src)
    records = json.loads(src.read_text())
    supplement = {e["query_id"] for e in json.loads((RUN / "supplement-cell-map.json").read_text())}

    missing = [l["id"] for l in records["lexemes"] if l["id"] not in SUBCATEGORY]
    if missing:
        sys.exit(f"unassigned lexemes: {missing}")

    out = {"lexemes": [], "constructions": records["constructions"],
           "participation_claims": [], "scope_checks": records["scope_checks"]}

    for lex in records["lexemes"]:
        sub, why = SUBCATEGORY[lex["id"]]
        out["lexemes"].append({**lex, "subcategory": sub, "subcategory_grounding": why})

    assigned = {}
    if ASSIGN.exists():
        blob = json.loads(ASSIGN.read_text())
        for a in (blob["assignments"] if isinstance(blob, dict) else blob):
            assigned[a["query_id"]] = a

    counts = {"declared": 0, "extracted": 0, "unassigned": 0}
    for claim in records["participation_claims"]:
        basis = None
        for cond in claim["conditions"]:
            found = BASIS.search(cond["requirement"])
            if found:
                basis = found.group(1)

        new = dict(claim)
        if claim["id"] in supplement:
            if basis is None:
                if claim["status"] != "not_stated":
                    sys.exit(f"{claim['id']}: supplement claim with no basis and status "
                             f"{claim['status']}")
                etype = "searched_not_found"
            else:
                etype = next((v for t, v in DECLARED if t in basis), None)
                if etype is None:
                    sys.exit(f"{claim['id']}: unrecognised declared basis: {basis[:60]}")
            new["evidence_type"] = etype
            new["evidence_type_provenance"] = "declared in the supplement"
            got = assigned.get(claim["id"])
            if got:
                new["evidence_type_basis_quote"] = got["basis_quote"]
                new["evidence_type_basis_source"] = got["source_id"]
                if got["evidence_type"] != etype:
                    sys.exit(f"{claim['id']}: extraction disagrees with the declared basis "
                             f"({got['evidence_type']} vs {etype}); resolve before merging")
            counts["declared"] += 1
        else:
            text = " ".join(e["quote"] for e in claim["evidence"]) + " " + \
                   " ".join(c["requirement"] for c in claim["conditions"])
            got = assigned.get(claim["id"])
            if got:
                new["evidence_type"] = got["evidence_type"]
                new["evidence_type_provenance"] = "extracted 2026-09-14, no declared value"
                new["evidence_type_basis_quote"] = got["basis_quote"]
                new["evidence_type_basis_source"] = got["source_id"]
                counts["extracted"] += 1
            else:
                new["evidence_type"] = None
                new["evidence_type_provenance"] = "not declared and not extracted"
                counts["unassigned"] += 1
            new["evidence_signals"] = [name for name, pat in SIGNALS if pat.search(text)]
        out["participation_claims"].append(new)

    # Verify: every original field survives untouched.
    added = {"evidence_type", "evidence_type_provenance", "evidence_signals",
             "evidence_type_basis_quote", "evidence_type_basis_source"}
    for old, new in zip(records["participation_claims"], out["participation_claims"]):
        stripped = {k: v for k, v in new.items() if k not in added}
        if stripped != old:
            sys.exit(f"{old['id']}: original fields were modified")
    for old, new in zip(records["lexemes"], out["lexemes"]):
        stripped = {k: v for k, v in new.items() if k not in
                    {"subcategory", "subcategory_grounding"}}
        if stripped != old:
            sys.exit(f"{old['id']}: original lexeme fields were modified")

    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")

    after = sha256(src)
    if before != after:
        sys.exit("FATAL: the source run artifact was modified")

    print(f"wrote {OUT.relative_to(ROOT)}")
    print(f"  source records.json sha256 unchanged: {before[:16]}...")
    print(f"  evidence_type: {counts['declared']} declared (extraction agreed on all), "
          f"{counts['extracted']} extracted, {counts['unassigned']} unassigned")
    return 0


if __name__ == "__main__":
    sys.exit(main())
