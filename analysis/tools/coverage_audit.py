#!/usr/bin/env python3
"""Generate the coverage-audit supplement tables from analysis/coverage-audit.json and the claim register.

    python3 analysis/tools/coverage_audit.py         # write analysis/generated/coverage-audit.tex and coverage-summary.tex
    python3 analysis/tools/coverage_audit.py check   # exit 1 if the committed files differ from a fresh build
"""
import collections, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
J = json.loads((ROOT / "analysis/coverage-audit.json").read_text())
REG = json.loads((ROOT / "analysis/manuscript-census-2026-09-14/census-normalized.json").read_text())
TEX = (ROOT / "determinatives-as-nouns.tex").read_text()
OUT_GRID, OUT_SUM = ROOT / "analysis/generated/coverage-audit.tex", ROOT / "analysis/generated/coverage-summary.tex"
IMPL = [i for i, _ in J["implementations"]]


def section_numbers():
    """§ numbers of the article's labels, from the order of \\section and \\subsection commands (appendix excluded)."""
    nums, s, ss = {}, 0, 0
    for m in re.finditer(r"\\(section|subsection)\*?\{[^}]*\}\\label\{([^}]*)\}", TEX):
        if m.start() > TEX.find(r"\appendix"): break
        if m.group(1) == "section": s += 1; ss = 0; nums[m.group(2)] = f"§{s}"
        else: ss += 1; nums[m.group(2)] = f"§{s}.{ss}"
    return nums


def tex(s):
    return s.replace("&", "\\&").replace("%", "\\%").replace("_", "\\_").replace("#", "\\#").replace("{N, D}", "$\\{$N, D$\\}$")


def main():
    secs = section_numbers()
    groups = {g["id"]: g for g in J["groups"]}
    fams = J["families"]
    # claim counts per cell from the register
    counts = {}
    for f in fams:
        for g in J["groups"]:
            n = collections.Counter()
            for c in REG["claims"]:
                if c.get("construction_id") in f["constructions"] and set(c.get("lexeme_ids", [])) & set(g["lexemes"]):
                    n[c["status"]] += 1
            counts[f"{f['id']}|{g['id']}"] = n
    # grid
    grid = ["{\\footnotesize\\setlength{\\tabcolsep}{3pt}", "\\begin{longtable}{>{\\raggedright\\arraybackslash}p{2.2cm}cccc>{\\raggedright\\arraybackslash}p{1.0cm}>{\\raggedright\\arraybackslash}p{7.2cm}}",
            "\\caption{The grid. Codes: D derived by a general rule; Dn derived only by admitting D as the head of Nom and NP; D2 derived by a rule stated once for nouns and again for determinatives (or for NP and DP); L stored on the lexeme; S stated for this construction alone; U not covered. Claims: register claims for the cell, as licensed/conditional/excluded.}\\label{tab:grid}\\\\",
            "\\toprule", "Lexeme group & I1 & I2 & I3 & I4 & Claims & Basis \\\\", "\\midrule", "\\endfirsthead",
            "\\toprule", "Lexeme group & I1 & I2 & I3 & I4 & Claims & Basis \\\\", "\\midrule", "\\endhead", "\\bottomrule", "\\endfoot"]
    per_impl = {i: collections.Counter() for i in IMPL}
    differ, stip, twice = [], {i: [] for i in IMPL}, {i: [] for i in IMPL}
    ncells = 0
    for f in fams:
        grid.append(f"\\multicolumn{{7}}{{l}}{{\\itshape {tex(f['label'])} ({secs.get(f['section'], f['section'])})}} \\\\")
        for g in J["groups"]:
            key = f"{f['id']}|{g['id']}"
            if key not in J["cells"]: continue
            ncells += 1
            codes = J["cells"][key]["codes"]; note = J["cells"][key]["note"]
            n = counts[key]; nstr = "/".join(str(n[s]) for s in ("licensed", "conditional", "excluded")) if sum(n.values()) else "--"
            short = g["label"].split(" (")[0]
            grid.append(f"{tex(short)} & {' & '.join(codes)} & {nstr} & {tex(note)} \\\\")
            for i, code in zip(IMPL, codes):
                per_impl[i][code] += 1
                if code == "S": stip[i].append((f.get("short", f["label"]), short))
                if code == "D2": twice[i].append((f.get("short", f["label"]), short))
            if len(set(codes)) > 1: differ.append((f["label"], short, codes))
    grid.append("\\end{longtable}}")
    OUT_GRID.write_text("\n".join(grid) + "\n")
    # summary
    s = ["\\begin{table}[H]\\centering\\small", f"\\caption{{Cells by class, over the {ncells} classified cells.}}\\label{{tab:counts}}",
         "\\begin{tabular}{lrrrrrr}", "\\toprule", "Implementation & D & Dn & D2 & L & S & U \\\\", "\\midrule"]
    for i, lab in J["implementations"]:
        c = per_impl[i]; s.append(f"{i}: {lab} & {c['D']} & {c['Dn']} & {c['D2']} & {c['L']} & {c['S']} & {c['U']} \\\\")
    s += ["\\bottomrule", "\\end{tabular}", "\\end{table}", "",
          "{\\small", "\\begin{longtable}{>{\\raggedright\\arraybackslash}p{5.2cm}>{\\raggedright\\arraybackslash}p{4.2cm}cccc}",
          "\\caption{Cells on which the implementations differ.}\\label{tab:differ}\\\\", "\\toprule",
          "Family & Lexeme group & I1 & I2 & I3 & I4 \\\\", "\\midrule", "\\endfirsthead", "\\toprule", "Family & Lexeme group & I1 & I2 & I3 & I4 \\\\", "\\midrule", "\\endhead", "\\bottomrule", "\\endfoot"]
    for fl, gl, codes in differ: s.append(f"{tex(fl)} & {tex(gl)} & {' & '.join(codes)} \\\\")
    s += ["\\end{longtable}}", "",
          "\\begin{table}[H]\\centering\\small", "\\caption{What each implementation states for a construction alone (S) or states twice (D2).}\\label{tab:stip}",
          "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{1.6cm}>{\\raggedright\\arraybackslash}p{6.5cm}>{\\raggedright\\arraybackslash}p{6.1cm}}", "\\toprule",
          "Account & Stated for the construction alone & Stated twice \\\\", "\\midrule"]
    def by_family(items):
        d = collections.OrderedDict()
        for fl, gl in items: d.setdefault(fl, []).append(gl)
        return "; ".join(f"{fl} ({', '.join(gs)})" for fl, gs in d.items()) or "--"
    for i, lab in J["implementations"]:
        s.append(f"{i} & {tex(by_family(stip[i]))} & {tex(by_family(twice[i]))} \\\\")
    s += ["\\bottomrule", "\\end{tabular}", "\\end{table}"]
    OUT_SUM.write_text("\n".join(s) + "\n")
    print(f"cells {ncells}; differ {len(differ)}; " + "; ".join(f"{i} D{per_impl[i]['D']} Dn{per_impl[i]['Dn']} D2:{per_impl[i]['D2']} L{per_impl[i]['L']} S{per_impl[i]['S']} U{per_impl[i]['U']}" for i in IMPL))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "check":
        before = {p: p.read_text() if p.exists() else None for p in (OUT_GRID, OUT_SUM)}
        main()
        ok = all(before[p] == p.read_text() for p in before)
        for p, t in before.items():
            if t is not None: p.write_text(t)
        sys.exit(0 if ok else "coverage audit is stale; run: python3 analysis/tools/coverage_audit.py")
    main()
