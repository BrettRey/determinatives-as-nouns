#!/usr/bin/env python3
"""Re-partition not_determinable after adding other_source_described to the enum.

The enum shipped to the census had no value for "described by a source other than
CGEL", so claims reporting Payne, Hudson, Spinillo, Sommerstein, Lyons, Palmer or
Reynolds' own earlier papers fell to not_determinable, conflating "the basis is
unclear" with "the basis is a third party". The extracting model flagged this in
its own summary.

Rule: a not_determinable claim whose surrounding manuscript context carries a real
citation command becomes other_source_described, or cgel_described if the only
cited work is CGEL. Everything else stays not_determinable, which then means only
what it says.

Writes census-repartitioned.json; the returned census.json is left untouched.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CITE = re.compile(r"\\(?:textcite|citep|citealp|citeyear)\s*(?:\[[^\]]*\])*\s*\{([^}]+)\}")
WINDOW = 300


def main():
    census = json.loads((HERE / "census.json").read_text())
    text = (ROOT / "determinatives-as-nouns.tex").read_text()

    changed, kept, detail = 0, 0, []
    for claim in census["claims"]:
        if claim["evidence_type"] != "not_determinable":
            continue
        pos = text.find(claim["quote"])
        if pos < 0:
            sys.exit(f"{claim['id']}: quote no longer in the manuscript")
        ctx = text[max(0, pos - WINDOW): pos + len(claim["quote"]) + WINDOW]
        keys = {k.strip() for group in CITE.findall(ctx) for k in group.split(",")}
        if not keys:
            kept += 1
            detail.append({"id": claim["id"], "verdict": "not_determinable", "keys": []})
            continue
        non_cgel = {k for k in keys if "huddleston" not in k.lower()}
        new = "other_source_described" if non_cgel else "cgel_described"
        claim["evidence_type"] = new
        claim["evidence_type_repartitioned_from"] = "not_determinable"
        claim["evidence_type_sources"] = sorted(keys)
        changed += 1
        detail.append({"id": claim["id"], "verdict": new, "keys": sorted(keys)})

    (HERE / "census-repartitioned.json").write_text(
        json.dumps(census, indent=2, ensure_ascii=False) + "\n")
    (HERE / "repartition-log.json").write_text(json.dumps({
        "rule": "not_determinable + a real citation command within 300 chars -> "
                "other_source_described (or cgel_described if only CGEL is cited); "
                "otherwise unchanged.",
        "reclassified": changed, "left_as_not_determinable": kept, "detail": detail,
    }, indent=2) + "\n")

    import collections
    dist = collections.Counter(c["evidence_type"] for c in census["claims"])
    print(f"reclassified: {changed}    left as not_determinable: {kept}")
    for k, v in dist.most_common():
        print(f"  {v:4}  {k}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
