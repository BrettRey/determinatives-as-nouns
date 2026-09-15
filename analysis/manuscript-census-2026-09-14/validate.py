#!/usr/bin/env python3
"""Validate the census: quote exactness, per-section completeness, acceptance cases."""

import collections
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OLD = ROOT / "analysis" / "expanded-json-2026-09-14"
SECTION = re.compile(r"^\\(sub)?section\{(.+?)\}\\label\{(.+?)\}", re.M)


def main():
    path = HERE / "census.json"
    if not path.exists():
        sys.exit("missing census.json; extract it from the result archive first")
    data = json.loads(path.read_text())
    claims = data["claims"]
    counts = {c["section_label"]: c["claims_recorded"] for c in data["section_counts"]}

    text = (ROOT / "determinatives-as-nouns.tex").read_text()
    labels = [m.group(3) for m in SECTION.finditer(text)] + ["front-matter"]
    acceptance = json.loads((HERE / "acceptance.json").read_text())

    rep = {"claims": len(claims)}

    bad = [c["id"] for c in claims if c["quote"] not in text]
    rep["quotes_exact"] = len(claims) - len(bad)
    rep["quote_failures"] = bad[:20]

    actual = collections.Counter(c["section_label"] for c in claims)
    mismatch = [{"section": s, "declared": n, "actual": actual.get(s, 0)}
                for s, n in counts.items() if actual.get(s, 0) != n]
    rep["section_count_mismatches"] = mismatch
    rep["sections_declared"] = len(counts)
    rep["sections_in_manuscript"] = len(labels)
    rep["sections_missing_from_report"] = sorted(set(labels) - set(counts))
    rep["unknown_section_labels"] = sorted(set(actual) - set(labels))
    rep["sections_with_zero"] = sorted(s for s in counts if actual.get(s, 0) == 0)

    blob = " ".join(c["quote"] + " " + c.get("expression", "") for c in claims)
    found = {a: (a in blob) for a in acceptance}
    rep["acceptance_found"] = sum(found.values())
    rep["acceptance_total"] = len(acceptance)
    rep["acceptance_missing"] = [a for a, ok in found.items() if not ok]

    rep["evidence_type"] = dict(collections.Counter(c["evidence_type"] for c in claims).most_common())
    rep["status"] = dict(collections.Counter(c["status"] for c in claims).most_common())
    rep["per_section"] = {s: actual.get(s, 0) for s in labels}

    old = json.loads((OLD / "records.json").read_text())["participation_claims"]
    cm = {e["query_id"] for e in json.loads((OLD / "supplement-cell-map.json").read_text())}
    rep["previous_manuscript_sample"] = sum(1 for c in old if c["id"] not in cm)
    if rep["previous_manuscript_sample"]:
        rep["census_multiple_of_previous"] = round(
            len(claims) / rep["previous_manuscript_sample"], 2)

    if data.get("responsibility_notice", "").strip():
        rep["responsibility_notice"] = data["responsibility_notice"]

    (HERE / "validation.json").write_text(json.dumps(rep, indent=2) + "\n")

    print(f"claims:                 {rep['claims']}")
    print(f"quotes exact:           {rep['quotes_exact']}/{rep['claims']}")
    print(f"sections reported:      {rep['sections_declared']}/{rep['sections_in_manuscript']}")
    print(f"section count mismatch: {len(mismatch)}")
    print(f"acceptance cases found: {rep['acceptance_found']}/{rep['acceptance_total']}")
    if rep["acceptance_missing"]:
        print("  MISSING:", ", ".join(rep["acceptance_missing"]))
    print(f"previous sample was:    {rep['previous_manuscript_sample']} claims "
          f"({rep.get('census_multiple_of_previous')}x smaller)")
    print("evidence_type:", rep["evidence_type"])
    if rep["sections_missing_from_report"]:
        print("SECTIONS NOT REPORTED:", rep["sections_missing_from_report"])
    if "responsibility_notice" in rep:
        print("\nRESPONSIBILITY NOTICE:\n" + rep["responsibility_notice"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
