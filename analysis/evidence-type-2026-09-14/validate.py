#!/usr/bin/env python3
"""Validate returned evidence_type assignments against the withheld key."""

import collections
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "analysis" / "expanded-json-2026-09-14"
HERE = Path(__file__).resolve().parent


def main():
    path = HERE / "assignments.json"
    if not path.exists():
        sys.exit(f"missing {path.name}; extract it from the result archive first")
    data = json.loads(path.read_text())
    assigns = data["assignments"] if isinstance(data, dict) else data

    sources = {s["id"]: s["text"] for s in json.loads((SRC / "inputs" / "sources.json").read_text())}
    records = json.loads((SRC / "records.json").read_text())
    supplement = {e["query_id"] for e in json.loads((SRC / "supplement-cell-map.json").read_text())}
    key = json.loads((HERE / "withheld-key.json").read_text())
    expected = {c["id"] for c in records["participation_claims"]}

    report = {}

    got = [a["query_id"] for a in assigns]
    dupes = [q for q, n in collections.Counter(got).items() if n > 1]
    report["count"] = len(assigns)
    report["ids_complete"] = set(got) == expected
    report["missing_ids"] = sorted(expected - set(got))
    report["unexpected_ids"] = sorted(set(got) - expected)
    report["duplicate_ids"] = dupes

    bad_quotes = []
    for a in assigns:
        text = sources.get(a["source_id"], "")
        if a["basis_quote"] not in text:
            bad_quotes.append(a["query_id"])
    report["quotes_checked"] = len(assigns)
    report["quotes_exact"] = len(assigns) - len(bad_quotes)
    report["quote_failures"] = bad_quotes

    by_id = {a["query_id"]: a for a in assigns}
    hits, confusion = 0, collections.Counter()
    disagreements = []
    for qid, want in key.items():
        got_t = by_id.get(qid, {}).get("evidence_type")
        if got_t == want:
            hits += 1
        else:
            confusion[(want, got_t)] += 1
            disagreements.append({"query_id": qid, "key": want, "returned": got_t,
                                  "quote": by_id.get(qid, {}).get("basis_quote", "")[:160]})
    report["held_out_n"] = len(key)
    report["held_out_correct"] = hits
    report["held_out_accuracy"] = round(hits / len(key), 4) if key else None
    report["held_out_confusion"] = [
        {"key": k, "returned": g, "n": n} for (k, g), n in confusion.most_common()]
    report["held_out_disagreements"] = disagreements

    man = collections.Counter(
        a["evidence_type"] for a in assigns if a["query_id"] not in supplement)
    report["manuscript_block_distribution"] = dict(man.most_common())
    report["manuscript_block_n"] = sum(man.values())

    if isinstance(data, dict) and data.get("responsibility_notice", "").strip():
        report["responsibility_notice"] = data["responsibility_notice"]

    (HERE / "validation.json").write_text(json.dumps(report, indent=2) + "\n")

    print(f"assignments:            {report['count']}")
    print(f"ids complete:           {report['ids_complete']}")
    print(f"quotes exact:           {report['quotes_exact']}/{report['quotes_checked']}")
    print(f"held-out accuracy:      {report['held_out_correct']}/{report['held_out_n']}"
          f"  ({report['held_out_accuracy']})")
    if report["held_out_confusion"]:
        print("confusions (key -> returned):")
        for c in report["held_out_confusion"]:
            print(f"   {c['n']:3}  {c['key']} -> {c['returned']}")
    print("manuscript block (no key):")
    for k, v in report["manuscript_block_distribution"].items():
        print(f"   {v:3}  {k}")
    if "responsibility_notice" in report:
        print("\nRESPONSIBILITY NOTICE RETURNED:\n" + report["responsibility_notice"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
