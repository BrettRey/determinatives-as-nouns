#!/usr/bin/env python3
"""Build the exclusion-checks table body for the quantifier supplement from analysis/exclusion-checks.json."""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
d = json.loads((ROOT / "analysis/exclusion-checks.json").read_text())
rows = []
for c in d["checks"]:
    q = "; ".join("\\texttt{" + s.replace("[", "{[}").replace("]", "{]}").replace("*", "{*}").replace("/", "/\\allowbreak{}") + "}" for s in c["queries"])
    rows.append(f"{c['claim']} & {q} & {c['hits']} & {c['result']}; {c['handling']} \\\\")
out = ROOT / "analysis/generated/exclusion-table.tex"
body = "\n".join(rows) + "\n"
if len(sys.argv) > 1 and sys.argv[1] == "check":
    sys.exit(0 if out.read_text() == body else "exclusion-table.tex is stale; run: python3 analysis/tools/exclusion_table.py")
out.write_text(body); print(f"wrote {out} ({len(rows)} rows)")
