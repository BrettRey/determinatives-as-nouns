#!/usr/bin/env python3
"""Check that every quotation in the claim set still resolves against the live sources.

The claim set is a snapshot of a moving manuscript, and nothing otherwise reports
when the two diverge. This is that signal: if a quoted passage is edited, moved or
deleted, the quote stops resolving and this fails.

SOURCE_PARTS maps each source_id to the files that now make up that source. The
supplement is two files because the body of tab:quant-controls was moved into a
generated file (see analysis/tools/quant_table.py); a quote spanning the table row
resolves against the generated part. Concatenation order does not matter, since
each quote is tested against the parts individually.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "analysis" / "expanded-json-2026-09-14"
CENSUS = ROOT / "analysis" / "manuscript-census-2026-09-14"

SOURCE_PARTS = {
    "M": ["determinatives-as-nouns.tex"],
    "Q": ["quantifier-controls.tex", "analysis/generated/quant-table.tex"],
}


def load_sources():
    out = {}
    for sid, parts in SOURCE_PARTS.items():
        texts = []
        for rel in parts:
            path = ROOT / rel
            if not path.exists():
                sys.exit(f"source part missing: {rel}")
            texts.append(path.read_text())
        out[sid] = texts
    return out


def main():
    live = load_sources()
    records = json.loads((RUN / "records.json").read_text())
    exceptions = json.loads((RUN / "exceptions.json").read_text())

    census = json.loads((CENSUS / "census-repartitioned.json").read_text())
    amend_path = CENSUS / "amendments.json"
    amend = json.loads(amend_path.read_text()) if amend_path.exists() else {}
    for c in census["claims"]:
        if c["id"] in amend and not c["id"].startswith("_"):
            c["quote"] = amend[c["id"]]["quote"]
    census["claims"] = [c for c in census["claims"] if not amend.get(c["id"], {}).get("withdrawn")]
    norm_path = CENSUS / "census-normalized.json"
    norm = json.loads(norm_path.read_text()) if norm_path.exists() else {"lexemes": []}
    groups = [
        ("census_claims", [(c["id"], {"source_id": "M", "quote": c["quote"]}) for c in census["claims"]]),
        # only lexemes normalize.py labelled carry exact manuscript groundings; the enriched
        # run's 34 entries carry analyst notes ("CGEL/paper default"), which are not quotes
        ("census_lexeme_groundings", [(l["id"], {"source_id": "M", "quote": l["subcategory_grounding"]}) for l in norm["lexemes"]
                                      if l.get("subcategory_grounding") and "subcategory_provenance" in l]),
        ("participation_claims", [(c["id"], e) for c in records["participation_claims"]
                                  for e in c["evidence"]]),
        ("scope_checks", [(s["id"], e) for s in records["scope_checks"]
                          for e in s.get("evidence", [])]),
        ("exceptions", [(x["query_id"], e) for x in exceptions
                        for e in x.get("evidence", [])]),
    ]

    total = ok = 0
    failures = []
    for name, items in groups:
        n = good = 0
        for owner, ev in items:
            n += 1
            sid = ev["source_id"]
            if sid not in live:
                failures.append((name, owner, sid, "unknown source id", ev["quote"][:80]))
                continue
            q = ev["quote"]
            if not any(q in text for text in live[sid]):
                # hash-pinned bundles cannot be edited; _evidence amendments rewrite a quote's changed span
                for e in amend.get("_evidence", []):
                    q = q.replace(e["old"], e["new"])
            if any(q in text for text in live[sid]):
                good += 1
            else:
                failures.append((name, owner, sid, "quote not found", ev["quote"][:80]))
        print(f"{name:22} {good}/{n} resolve")
        total += n
        ok += good

    print(f"{'TOTAL':22} {ok}/{total} resolve")

    if failures:
        print(f"\n{len(failures)} failure(s):")
        for name, owner, sid, why, snippet in failures[:20]:
            print(f"  [{name}] {owner} source={sid}: {why}\n      {snippet!r}")
        print("\nThe claim set no longer matches the manuscript. Either the text moved "
              "(update SOURCE_PARTS) or the quoted passage was edited (the claim is stale).")
        return 1

    print("\nThe claim set is current against the live sources.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
