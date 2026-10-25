#!/usr/bin/env python3
"""Brett's review sheet for the y-to-m pass (24 Oct 2026).

Usage: python3 analysis/cell-ledger/make_ym_review.py RUN_DIR
Reads RUN_DIR/ym-map.json, the coders' outputs (through coder-cells-ym.csv) and
the 2021 matrix; writes RUN_DIR/YM-REVIEW.md (gitignored with the run). Order:
  1. sense questions: columns where the cells both coders reject share one reason,
     so the disagreement is over what the column means, not over cells (the
     columns in READING, picked by reading the cells, plus any where both reject
     a quarter or more);
  2. candidate 2021 slips: both coders n, outside those columns;
  3. candidate m's: both coders m, sorted by whether the notes cite register,
     variety or rarity (which the codebook codes y with a variety note);
  4. splits, listed in full.
Form and column codes in the notes are resolved to names.
"""
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
REGISTER = re.compile(r"archaic|\b(?:in)?formal\b|\brare|literary|register|variety|old-fashioned|obsolete|dated|journalese|"
                      r"for many speakers|some speakers|regional|\bBrE\b|\bAmE\b|prescripti|usage guide", re.I)
MEANING = {"quantification", "definiteness", "number_meaning", "countability", "reference"}
SENSE_SHARE = 0.25          # both-n share of a column's cells that makes it a sense question
SENSE_MIN = 5

# Claude's reading of each sense question, from the 2021 y and n lists (24 Oct).
READING = {
    "selects_plural_heads": "The coders read 'requires'. That reading fits every 2021 cell except the dependent genitives (my, our, your, her, their), determinative what, and enough. A 'may take' reading would instead make the 2021 n for the, all, any, some, and no wrong. So 'requires' fits better, and the genitive rows look like one row copied across the three head-selection columns.",
    "selects_non_count_heads": "As for plural heads: the same genitive rows and what are y in all three head-selection columns, while the is n in all three.",
    "selects_count_singular_heads": "As for plural heads.",
    "non_affirmative": "2021 has y for every wh-form (interrogative, relative, and free relative) as well as any, either, and much. The coders read 'polarity item' and rejected the wh-forms. If the 2021 sense was 'occurs in or creates a non-affirmative context' (CGEL ch. 9 §4.4, p. 834, treats interrogative clauses among the contexts that sanction NPIs), the definition needs rewording; if it was the polarity-item sense, the wh-rows are slips.",
    "free_choice": "2021 has y for every wh-form. Both coders reject the interrogatives (which, whichever, who, whom, whose) and relative which and whose; relative who and whom get n from Muse and m from Claude, who cites the fused-relative use (invite who you like). The 2021 cells may record that use on the plain rows.",
    "existential": "2021 has y for no, nobody, no one, nothing, nowhere, and dummy it; the coders read 'existential import' and said these deny or lack it. Both coders rejected no other 2021 y in the column (the 2021 n's are wh-forms, generic one, dummy there, and zero), so the question is narrower: did 2021 count the negative quantifiers and dummy it?",
    "occurs_after_predeterminer_modifiers_multipliers": "2021 has y for the accusative personal pronouns (him, me, them, us, her). The coders say these need twice his size or twice what he earns. The definition was inferred, so the 2021 sense may have counted those.",
    "occurs_after_predeterminer_modifiers_fractions": "2021 has y for him, me, them, her, and it; the coders say half of him, not half him. The definition was inferred.",
    "compatible_count_sing_NP": "2021 has y for the compound pronouns (anyone, someone, nobody, no one, anybody, somebody) and relative who, whom, which, but n for everybody, everyone, everything. The coders read 'combines with a count singular NP or nominal' and rejected the compounds. The definition was inferred, and no reading I've found fits all the 2021 cells.",
}


def main():
    run = Path(sys.argv[1])
    mp = json.loads((run / "ym-map.json").read_text())
    fid = mp["forms"]
    col_packet = {c: (pk, code) for pk, info in mp["packets"].items() for code, c in info["columns"].items()}
    defs = {r["column"]: r for r in csv.DictReader((ROOT / "analysis" / "codebook" / "definitions.csv").open())}
    supcol = {r["column"]: r["super_column"] for r in csv.DictReader((ROOT / "analysis" / "codebook" / "columns.csv").open())}
    label = {r["form"]: r["blind_label"] for r in csv.DictReader((ROOT / "analysis" / "codebook" / "forms.csv").open())}
    m = list(csv.reader((ROOT / "analysis" / "matrix-2026-10" / "matrix-2026-10.csv").open()))
    h, mrows = m[0], m[1:]

    cells, notes = defaultdict(dict), defaultdict(dict)
    for r in csv.DictReader((HERE / "coder-cells-ym.csv").open()):
        c = r["proposer"].split()[2]
        cells[(r["form"], r["column"])][c] = r["value"]
        notes[(r["form"], r["column"])][c] = r["note"]
    both = {k: v for k, v in cells.items() if len(v) == 2}

    def resolve(note, col):
        """Form ids to names; a column code to nothing if it is the note's own column, else to its name."""
        pk, own = col_packet[col]
        cmap = mp["packets"][pk]["columns"]
        note = re.sub(r"F\d{3}", lambda x: fid.get(x.group(0), x.group(0)), note)
        note = re.sub(r"\s*\((C\d\d)\)", lambda x: "" if x.group(1) == own else f" ({cmap.get(x.group(1), x.group(1))})", note)
        return re.sub(r"^[ymn] \| ", "", note)

    def line(form, col, v):
        ns = "; ".join(f"{k}: {resolve(notes[(form, col)].get(k, ''), col) or '(no note)'}" for k in ("MUSE", "CLAUDE"))
        return f"- *{form}* ({label.get(form, form)}): Muse {v['MUSE']}, Claude {v['CLAUDE']}. {ns}"

    def pattern(v):
        return "".join(sorted(v.values()))

    per_col = defaultdict(Counter)
    for (f, c), v in both.items():
        per_col[c][pattern(v)] += 1
    sense = [c for c, x in per_col.items() if c in READING or
             (x["nn"] >= SENSE_MIN and x["nn"] / sum(x.values()) >= SENSE_SHARE)]
    sense.sort(key=lambda c: -per_col[c]["nn"])

    pats = Counter(pattern(v) for v in both.values())
    L = ["# The y-to-m pass: review sheet",
         "<!-- SUMMARY: Brett's 2021 y cells that blind coders graded m or n, sorted into sense questions, candidate 2021 slips, candidate m's, and splits · status: for Brett · updated: 2026-10-24 -->", "",
         "Generated by `analysis/cell-ledger/make_ym_review.py`. Two blind coders (Muse Wonder 1.0 and a Claude Opus 5.5 subagent) graded every 2021 y cell in the 62 columns whose definitions were settled: y if fully available, m if available but degraded, n if not available. They saw plain labels for the forms and the codebook's definition of each column, and nothing else. Their notes are model output, unedited except that form and column codes are replaced by names. Nothing here is a judgment until you make it.", "",
         f"Of {len(both)} cells, both coders said y for {pats['yy']}. Both said n for {pats['nn']}, both m for {pats['mm']}; they split m/y on {pats['my']}, n/y on {pats['ny']}, and m/n on {pats['mn']}.", ""]

    # 1. sense questions
    nn_sense = sum(per_col[c]["nn"] for c in sense)
    L += ["## 1. Sense questions", "",
          f"In these {len(sense)} columns the 2021 y cells that both coders rejected ({nn_sense} of the {pats['nn']} cells where both said n) are rejected for one shared reason, which I picked out by reading the cells. That pattern means the coders and the 2021 coding are answering different questions, so the cells can't be judged until you say what the column meant in 2021. Two coders agreeing here counts once, since they read the same definition.", ""]
    for c in sense:
        i = h.index(c)
        ys = [r[0] for r in mrows if r[i] == "y"]
        ns_ = [r[0] for r in mrows if r[i] == "n"]
        rej = sorted(f for (f, cc), v in both.items() if cc == c and pattern(v) == "nn")
        d = defs[c]
        L += [f"### {c}",
              f"- **Definition the coders saw:** {d['definition'].split(' n in 2021')[0]} (confidence: {d['confidence'].lower()})",
              f"- **2021 y ({len(ys)}):** {', '.join(ys)}",
              f"- **2021 n ({len(ns_)}), first 20:** {', '.join(ns_[:20])}",
              f"- **Both coders n ({len(rej)}):** {', '.join(rej)}",
              f"- **Claude's reading:** {READING.get(c, '(none written)')}", ""]
        ex = rej[0]
        L += ["  Example notes:", "  " + line(ex, c, both[(ex, c)]), ""]

    # 2. candidate slips
    slips = sorted(((f, c), v) for (f, c), v in both.items() if pattern(v) == "nn" and c not in sense)
    L += ["## 2. Candidate 2021 slips", "",
          f"Both coders said n, in columns where the definition otherwise matched the 2021 coding ({len(slips)} cells). Some look like grain problems (a use of one row coded on another), so check the row's label first.", ""]
    by = defaultdict(list)
    for (f, c), v in slips:
        by[c].append(line(f, c, v))
    for c in sorted(by):
        L += [f"### {c}", f"*{defs[c]['definition'].split(' n in 2021')[0]}*", ""] + by[c] + [""]

    # 3. candidate m's
    mm = sorted(((f, c), v) for (f, c), v in both.items() if pattern(v) == "mm")
    def reg(k, coder):
        return bool(REGISTER.search(notes[k].get(coder, "")))
    groups = {"neither": [], "one": [], "both": []}
    for k, v in mm:
        n = reg(k, "MUSE") + reg(k, "CLAUDE")
        tag = "; a meaning column" if supcol.get(k[1]) in MEANING else ""
        groups[["neither", "one", "both"][n]].append(line(k[0], k[1], v) + f" [column: {k[1]}{tag}]")
    allm = [(k, c) for k, v in both.items() for c, x in v.items() if x == "m"]
    regm = sum(reg(k, c) for k, c in allm)
    mean_mm = sum(supcol.get(k[1]) in MEANING for k, v in mm)
    L += ["## 3. Candidate m's", "",
          f"Both coders said m for {len(mm)} cells. The codebook keeps m for degraded acceptability and codes a use limited to a variety or register as y with a variety note; rarity isn't on the scale at all. Yet {regm} of the {len(allm)} individual m grades cite register, variety, or rarity (archaic, formal, rare, literary, and the like; matched by a word list, so check). Sorted by that test below. A further {mean_mm} of the {len(mm)} are in meaning columns (quantification, definiteness, number, countability, reference), where an m records a weak or cancellable reading (few implies but doesn't entail that some came), not degraded acceptability; the scale wasn't built for those, and they're marked.", "",
          f"### Neither note cites register or rarity ({len(groups['neither'])}): the real m candidates", ""] + groups["neither"] + ["",
          f"### One note does ({len(groups['one'])})", ""] + groups["one"] + ["",
          f"### Both notes do ({len(groups['both'])}): by the codebook, y with a variety note", ""] + groups["both"] + [""]

    # 4. splits
    L += ["## 4. Splits", "", "One coder y and the other m or n, or one m and the other n. Listed by column.", ""]
    by = defaultdict(list)
    for (f, c), v in sorted(both.items()):
        if len(set(v.values())) > 1:
            by[c].append(line(f, c, v))
    for c in sorted(by):
        tag = " (sense question above)" if c in sense else ""
        L += [f"### {c}{tag}", ""] + by[c] + [""]
    (run / "YM-REVIEW.md").write_text("\n".join(L) + "\n")
    print(f"sense questions {len(sense)} ({nn_sense} both-n cells); slips {len(slips)}; both-m {len(mm)} "
          f"(neither {len(groups['neither'])}, one {len(groups['one'])}, both {len(groups['both'])}); "
          f"register-citing m grades {regm}/{len(allm)}; splits {sum(len(x) for x in by.values())}")


if __name__ == "__main__":
    main()
