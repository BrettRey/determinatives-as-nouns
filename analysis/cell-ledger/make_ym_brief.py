#!/usr/bin/env python3
"""The short version of the y-to-m review: only what Brett has to decide (24 Oct 2026).

Usage: python3 analysis/cell-ledger/make_ym_brief.py RUN_DIR
Writes RUN_DIR/YM-FOR-BRETT.md. The full sheet (YM-REVIEW.md, from
make_ym_review.py) keeps every flagged cell, the splits included.
"""
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
from make_ym_review import MEANING, READING, REGISTER  # noqa: E402

QUESTIONS = [  # (columns, question) for section 1; the evidence lines come from the matrix
    (["selects_plural_heads", "selects_non_count_heads", "selects_count_singular_heads"],
     "**Head selection** (three columns: as a determiner, it requires a plural head / a non-count head / a count singular head). "
     "In 2021, *my*, *our*, *your*, *her*, and *their* are y in all three columns, and *the* is n in all three, so no one reading fits. "
     "Did you mean **requires** (then the genitive rows, determinative *what*, and *enough* are slips) or **can take** (then the n's for *the*, *all*, *any*, *some*, and *no* are slips)?"),
    (["non_affirmative"],
     "**Non-affirmative.** 2021 has y for every wh-form (interrogative, relative, free relative) as well as *any*, *either*, *much*. "
     "Did you mean **is a polarity item** (then the wh-rows are slips) or **occurs in non-affirmative contexts**, interrogatives included (*CGEL* ch. 9 §4.4, p. 834)?"),
    (["free_choice"],
     "**Free choice.** 2021 has y for interrogative and plain relative *which*, *who*, *whom*, *whose*. "
     "Did those cells record the fused-relative use (*invite who you like*), or something else?"),
    (["existential"],
     "**Existential.** 2021 has y for *no*, *nobody*, *no one*, *nothing*, *nowhere*, and dummy *it*; every other n is a wh-form, generic *one*, dummy *there*, or zero. "
     "Did you count the negative quantifiers (\"there is no X\") and dummy *it* as existential?"),
    (["occurs_after_predeterminer_modifiers_multipliers", "occurs_after_predeterminer_modifiers_fractions"],
     "**After *twice* or *half*.** 2021 has y for *him*, *me*, *them*, *us*, and accusative *her* (and *it* after *half*). "
     "The coders say these need *twice his size*, *twice what he earns*, or *half of him*. Did you count those, or *half him* itself?"),
    (["compatible_count_sing_NP"],
     "**Combines with a count singular.** 2021 has y for *anyone*, *anybody*, *someone*, *somebody*, *nobody*, *no one*, and relative *who*, *whom*, *which*, but n for *everyone*, *everybody*, *everything*. "
     "What did the column mean?"),
]


def ex(note):
    """The quoted example in a coder's note, else the note's second field."""
    q = re.search(r'"([^"]+)"', note)
    if q:
        return q.group(1)
    parts = [p.strip() for p in note.split("|")]
    return parts[1] if len(parts) > 1 else ""


def why(note):
    parts = [p.strip() for p in note.split("|")]
    w = parts[-1] if len(parts) > 2 else ""
    return (w[:110] + "…") if len(w) > 110 else w


def main():
    run = Path(sys.argv[1])
    fid = json.loads((run / "ym-map.json").read_text())["forms"]
    defs = {r["column"]: r for r in csv.DictReader((ROOT / "analysis" / "codebook" / "definitions.csv").open())}
    supcol = {r["column"]: r["super_column"] for r in csv.DictReader((ROOT / "analysis" / "codebook" / "columns.csv").open())}
    cells, notes = defaultdict(dict), defaultdict(dict)
    for r in csv.DictReader((HERE / "coder-cells-ym.csv").open()):
        c = r["proposer"].split()[2]
        cells[(r["form"], r["column"])][c] = r["value"]
        notes[(r["form"], r["column"])][c] = re.sub(r"F\d{3}", lambda x: fid.get(x.group(0), x.group(0)), r["note"])
    both = {k: v for k, v in cells.items() if len(v) == 2}

    def pick(k):
        c, m_ = notes[k].get("CLAUDE", ""), notes[k].get("MUSE", "")
        return m_ if (not c or why(c).lower().startswith("same")) and m_ else c

    def plain(col):
        d = defs[col]["definition"].split(" n in 2021")[0]
        return d.split(". ")[0].rstrip(".")

    def pat(v):
        return "".join(sorted(v.values()))

    L = ["# The y-to-m results: what needs you",
         "<!-- SUMMARY: the short sheet for Brett from the y-to-m grading of his 2021 y cells: six questions about what a 2021 column meant, one policy question, 15 possible m's, 32 possible slips, and whether to grade the 2021 n cells too · status: for Brett · updated: 2026-10-24 -->", "",
         "Two blind coders (Muse and a Claude subagent) graded each of your 2021 y cells y, m, or n. They agreed on y for 1,478 of 1,941. This sheet has only what needs your judgment; everything else, the 292 cells where they split included, is in `YM-REVIEW.md` beside it. Write your answer in the last column or after each question.", "",
         "## 1. What did the 2021 column mean?", "",
         "In these columns the coders reject the same 2021 y's for the same reason, so the issue is the column's sense, not the cells. 80 of the 112 cells where both coders said n fall here. Once you answer, I'll fix the definition and either recode the column or mark the cells as slips.", ""]
    for i, (cols, q) in enumerate(QUESTIONS, start=1):
        L += [f"{i}. {q}", "", "   Your answer:", ""]

    # 2. register policy
    allm = [(k, c) for k, v in both.items() for c, x in v.items() if x == "m"]
    regm = [(k, c) for k, c in allm if REGISTER.search(notes[k].get(c, ""))]
    exs = []
    strong = re.compile(r"archaic|formal|literary", re.I)
    for k, c in sorted(regm, key=lambda kc: not strong.search(notes[kc[0]][kc[1]])):
        if k[0] not in {e[0] for e in exs} and k[1] not in {e[3] for e in exs} and REGISTER.search(why(notes[k][c])):
            exs.append((k[0], ex(notes[k][c]), why(notes[k][c]), k[1]))
        if len(exs) == 4:
            break
    L += ["## 2. Should register count as m?", "",
          f"{len(regm)} of the {len(allm)} m grades give register, variety, or rarity as the reason, for instance "
          + "; ".join(f"*{f}*: \"{e}\" ({w})" for f, e, w, _ in exs) + ". "
          "The codebook says a use limited to a variety or register is y with a variety note, and rarity isn't on the scale. "
          "Apply that rule to all of them (they become y, with the note kept), or look at them one by one? They're all listed in `YM-REVIEW.md`, section 3.", "",
          "Your answer:", ""]

    # 3. candidate m's
    mm = sorted(k for k, v in both.items() if pat(v) == "mm"
                and not any(REGISTER.search(notes[k].get(c, "")) for c in ("MUSE", "CLAUDE"))
                and supcol.get(k[1]) not in MEANING)
    L += [f"## 3. Possible m's ({len(mm)})", "",
          "Both coders said m, neither cited register or rarity, and the column is about form, not meaning. The example and reason are Claude's unless Claude's note only points to another row.", "",
          "| form | column | example | why degraded | your call (y / m / n) |", "|---|---|---|---|---|"]
    for f, c in mm:
        n = pick((f, c))
        L.append(f"| *{f}* | {plain(c)} | *{ex(n)}* | {why(n)} | |")
    L.append("")

    # 4. candidate slips
    sense = {c for cols, _ in QUESTIONS for c in cols} | set(READING)
    slips = sorted(k for k, v in both.items() if pat(v) == "nn" and k[1] not in sense)
    L += [f"## 4. Possible 2021 slips ({len(slips)})", "",
          "Both coders said n where 2021 has y, in columns whose definitions otherwise match. The example is the best case for y that a coder found, and the reason is why the coder rejected it.", "",
          "| form | column | best case for y | why rejected | your call (y / m / n) |", "|---|---|---|---|---|"]
    for f, c in slips:
        n = pick((f, c))
        L.append(f"| *{f}* | {plain(c)} | *{ex(n)}* | {why(n)} | |")
    L.append("")

    # 5. n-to-m
    L += ["## 5. Should your 2021 n cells be graded too?", "",
          "This pass graded only your y cells, so a 2021 n can never become m, while the new noun and adjective rows were coded fresh and can get m from either side. A real but rare determinative use (*the some will become the many*) stays n while a comparable noun use comes back m, and that difference would feed straight into the nesting test.",
          "",
          "There are 6,676 n cells in the same 62 columns (3,513 determinative, 3,163 pronoun). My suggestion: one coder screens all of them, a second grades every cell the first flags plus a random tenth of the rest (which measures what the screen misses), and the corpus records are mapped onto cells alongside. Run it, run it only for the columns the nesting test uses, or wait?", "",
          "Your answer:", ""]
    (run / "YM-FOR-BRETT.md").write_text("\n".join(L) + "\n")
    print(f"questions {len(QUESTIONS)}; register m's {len(regm)}/{len(allm)}; possible m's {len(mm)}; slips {len(slips)}")


if __name__ == "__main__":
    main()
