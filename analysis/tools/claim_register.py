#!/usr/bin/env python3
"""Claim register and diagnostic coverage from the normalized census.

Reads analysis/manuscript-census-2026-09-14/census-normalized.json. Writes
  analysis/generated/claim-register.tex   one row per (diagnostic, lexeme): subcategory, statuses, bases, sections, claims
  analysis/generated/claim-coverage.tex   one row per diagnostic: lexemes by subcategory and status
  analysis/generated/claim-register.md    the same register for the repository
`check` verifies the committed .tex files are current.
Excludes claims labelled taxonomic_or_meta or other, and claims with no resolvable lexeme.
"""
import collections, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "analysis/manuscript-census-2026-09-14/census-normalized.json"
OUT = ROOT / "analysis/generated"
LABEL = {"independent_argument": "independent argument use", "independent_partitive": "independent use with partitive of-PP",
         "dependent_det": "Det before a nominal", "dependent_internal_mod": "internal Mod before a nominal",
         "internal_mod_admission": "admits an internal modifier", "peripheral_mod_admission": "admits a peripheral modifier",
         "external_determination": "takes an external determiner", "degree_modifier_adj": "degree modifier of an adjective",
         "degree_modifier_nonadj": "degree modifier of a non-adjective", "predicative_complement": "predicative complement",
         "comparative_complement": "comparative than-complement", "existential_displaced_subject": "existential displaced subject",
         "number_agreement": "number agreement or transparency", "number_inflection": "number inflection", "grade_inflection": "grade inflection",
         "genitive_marking": "genitive marking", "predeterminer_mod": "predeterminer modifier", "coordination_marker": "marker of coordination",
         "compound_base": "base of a compound determinative", "fused_head": "fused-head analysis", "relative_postmod_admission": "relative postmodifier"}
BASIS = {"retained_attestation": "attested", "cgel_described": "CGEL", "cgel_restricted": "CGEL (restricted)", "other_source_described": "other source",
         "constructed_illustration": "constructed", "constructed_ungrammatical": "constructed (starred)", "authors_analysis": "analysis",
         "searched_not_found": "searched, none", "not_determinable": "n/d"}
SUBS = ["common noun", "proper noun", "pronoun", "determinative", "adjective (control)"]  # Table 2 order, controls last
TYP = json.loads((ROOT / "analysis/typicality.json").read_text())["cells"]
RANK = {"general": 2, "restricted": 1, "absent": 0}
def typ(con, side):
    return (TYP.get(con) or {}).get(side)
def discrimination(con):
    """positive favours Noun (property general for nouns, absent for adjectives); None when a side is unsourced"""
    a, b = typ(con, "common_noun"), typ(con, "adjective")
    return None if a is None or b is None else RANK[a] - RANK[b]
# Order follows the article's argument: §2.1 functions and constructional range, §§2.2 and 2.5 nominal
# connections, §2.4 the adjectival profile, then the structural analysis of §4. Within a block, the
# section's own order. A diagnostic not listed here falls into a final block.
GROUPS = [("Functions and constructional range", ["independent_argument", "independent_partitive", "existential_displaced_subject", "dependent_det", "dependent_internal_mod", "predeterminer_mod", "coordination_marker"]),
          ("Nominal connections", ["number_agreement", "external_determination", "internal_mod_admission", "peripheral_mod_admission", "relative_postmod_admission", "genitive_marking", "number_inflection", "compound_base"]),
          ("Adjectival profile", ["grade_inflection", "degree_modifier_adj", "degree_modifier_nonadj", "comparative_complement", "predicative_complement"]),
          ("Structural analysis", ["fused_head"])]


def tex(s):
    return s.replace("&", "\\&").replace("%", "\\%").replace("_", "\\_").replace("#", "\\#")


def main():
    d = json.loads(SRC.read_text()); lex = {l["id"]: l for l in d["lexemes"]}
    rows = collections.defaultdict(lambda: {"claims": 0, "status": collections.Counter(), "basis": collections.Counter(), "sections": set(), "sub": None})
    for c in d["claims"]:
        if c["construction_id"] in ("taxonomic_or_meta", "other") or not c["lexeme_ids"]:
            continue
        for lid in c["lexeme_ids"]:
            r = rows[(c["construction_id"], lex[lid]["forms"][0].lower())]
            r["claims"] += 1; r["status"][c["status"]] += 1; r["basis"][c["evidence_type_reconciled"]] += 1
            r["sections"].add(c["section_label"].replace("sec:", "")); r["sub"] = lex[lid].get("subcategory") or "other"
    present = {k[0] for k in rows}
    grouped = [(g, sorted([c for c in cs if c in present], key=lambda c: (discrimination(c) is None, -(discrimination(c) or 0), cs.index(c)))) for g, cs in GROUPS]
    rest = sorted(c for c in present if not any(c in cs for _, cs in GROUPS))
    if rest: grouped.append(("Other", rest))
    order = [c for _, cs in grouped for c in cs]
    reg, md = [], ["# Claim register", "", "<!-- SUMMARY: every participation claim in the census by diagnostic and lexeme, with status and stated basis; generated by analysis/tools/claim_register.py · status: generated · updated: 2026-09-17 -->", "",
                   "| Diagnostic | Lexeme | Subcategory | Status | Basis | Sections | Claims |", "|---|---|---|---|---|---|---:|"]
    for gname, cons in grouped:
      reg.append(f"\\multicolumn{{7}}{{l}}{{\\itshape {tex(gname)}}} \\\\")
      md.append(f"| **{gname}** | | | | | | |")
      for con in cons:
        for (c, form), r in sorted(((k, v) for k, v in rows.items() if k[0] == con), key=lambda kv: (SUBS.index(kv[1]["sub"]) if kv[1]["sub"] in SUBS else 9, kv[0][1])):
            st = ", ".join(f"{k} {v}" if v > 1 else k for k, v in r["status"].most_common())
            ba = ", ".join(f"{BASIS.get(k, k)} {v}" if v > 1 else BASIS.get(k, k) for k, v in r["basis"].most_common())
            secs = ", ".join(sorted(r["sections"]))
            reg.append(f"{tex(LABEL.get(con, con))} & \\mention{{{tex(form)}}} & {tex(r['sub'])} & {tex(st)} & {tex(ba)} & {tex(secs)} & {r['claims']} \\\\")
            md.append(f"| {LABEL.get(con, con)} | *{form}* | {r['sub']} | {st} | {ba} | {secs} | {r['claims']} |")
    cov = []
    for gname, cons in grouped:
      cov.append(f"\\multicolumn{{9}}{{l}}{{\\itshape {tex(gname)}}} \\\\")
      for con in cons:
          cells = [tex(typ(con, "common_noun") or "?"), tex(typ(con, "adjective") or "?")]
          for s in SUBS:
              g = [(k, v) for k, v in rows.items() if k[0] == con and v["sub"] == s]
              if not g: cells.append(""); continue
              lic = sum(1 for k, v in g if v["status"]["licensed"] or v["status"]["conditional"]); exc = sum(1 for k, v in g if v["status"]["excluded"] and not (v["status"]["licensed"] or v["status"]["conditional"]))
              cells.append(f"{len(g)} ({lic}/{exc})")
          tot = len([k for k in rows if k[0] == con])
          cov.append(f"{tex(LABEL.get(con, con))} & " + " & ".join(cells) + f" & {tot} \\\\")
    body_reg, body_cov = "\n".join(reg) + "\n", "\n".join(cov) + "\n"
    if len(sys.argv) > 1 and sys.argv[1] == "check":
        ok = (OUT / "claim-register.tex").read_text() == body_reg and (OUT / "claim-coverage.tex").read_text() == body_cov
        sys.exit(0 if ok else "claim register is stale; run: python3 analysis/tools/claim_register.py")
    OUT.mkdir(exist_ok=True)
    (OUT / "claim-register.tex").write_text(body_reg); (OUT / "claim-coverage.tex").write_text(body_cov)
    (OUT / "claim-register.md").write_text("\n".join(md) + "\n")
    print(f"register rows {len(reg)}; coverage rows {len(cov)}; claims covered {sum(r['claims'] for r in rows.values())}")


if __name__ == "__main__":
    main()
