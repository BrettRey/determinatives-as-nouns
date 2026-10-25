#!/usr/bin/env python3
"""Harvest \\needs[id]{...} markers from the category paper's drafts into
planning/evidence-ledger.md (24 Oct 2026).

Why: data needs often only show up while writing. Drafting marks them in place
(drafts/needs.tex defines the macro); this script gathers them so nothing is
lost, and keeps one ledger row per need, with columns for what each rival
analysis predicts. A datum is worth gathering only where the predictions differ.

Behaviour:
- scans drafts/*.tex (comments ignored) for \\needs[id]{text}, braces balanced;
- an unnamed marker gets an id from its file and order (e.g. intro-2);
- new ids are appended to the ledger table with status "open";
- ids in the ledger that no longer appear in any draft are marked
  "not in draft" (rows are never deleted, so the history stays), except
  seed rows (section "seed"), which were entered before drafting;
- prints a summary: open, gathering, have, failed, dropped, not in draft.

Usage: python3 tools/evidence_needs.py [--check]
  --check  exit 1 if any marker remains in the drafts or any ledger row is still
           open or gathering, seed rows included (for the submission gate); rows
           left "not in draft" are listed as a warning.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRAFTS = ROOT / "drafts"
LEDGER = ROOT / "planning" / "evidence-ledger.md"
COLS = ["id", "section", "claim / what would show it", "CGEL (separate category)",
        "Hudson (nested in pronoun)", "split A/N (English hypothesis)", "coordinate (this paper)",
        "discriminates?", "record", "status", "result"]
HEADER = "| " + " | ".join(COLS) + " |\n|" + "---|" * len(COLS) + "\n"


def strip_comments(text):
    return "\n".join(re.sub(r"(?<!\\)%.*", "", line) for line in text.split("\n"))


def braced(text, i):
    """Return (content, end) for the brace group starting at text[i] == '{'."""
    depth, j = 0, i
    while j < len(text):
        if text[j] == "{" and text[j - 1] != "\\":
            depth += 1
        elif text[j] == "}" and text[j - 1] != "\\":
            depth -= 1
            if depth == 0:
                return text[i + 1:j], j + 1
        j += 1
    raise ValueError(f"unbalanced braces from offset {i}")


def harvest():
    found = []
    for f in sorted(DRAFTS.glob("*.tex")):
        if f.name == "needs.tex":
            continue
        text = strip_comments(f.read_text())
        n = 0
        for m in re.finditer(r"\\needs\b", text):
            k = m.end()
            ident = ""
            if k < len(text) and text[k] == "[":
                close = text.index("]", k)
                ident = text[k + 1:close].strip()
                k = close + 1
            while k < len(text) and text[k].isspace():
                k += 1
            if k >= len(text) or text[k] != "{":
                continue
            body, _ = braced(text, k)
            n += 1
            ident = ident or f"{f.stem}-{n}"
            found.append((ident, f.stem, " ".join(body.split())))
    return found


def read_ledger():
    rows, pre, post = {}, "", ""
    if not LEDGER.exists():
        return rows, pre, post
    lines = LEDGER.read_text().split("\n")
    i = 0
    while i < len(lines) and not lines[i].startswith("| id |"):
        pre += lines[i] + "\n"
        i += 1
    i += 2  # header and separator
    order = []
    while i < len(lines) and lines[i].startswith("|"):
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        cells += [""] * (len(COLS) - len(cells))
        rows[cells[0]] = cells
        order.append(cells[0])
        i += 1
    post = "\n".join(lines[i:])
    rows["__order__"] = order
    return rows, pre, post


def main():
    found = harvest()
    rows, pre, post = read_ledger()
    order = rows.pop("__order__", [])
    if not pre:
        pre = ("# Evidence ledger: the category paper\n"
               "<!-- SUMMARY: one row per data need, harvested from \\needs markers in drafts/ by "
               "tools/evidence_needs.py; rival-prediction columns filled by hand · status: active -->\n\n"
               "Statuses: open, gathering, have, failed, dropped, not in draft. "
               "Fill the four prediction columns before gathering: if all four predict the same, "
               "the datum doesn't discriminate and is illustration, not evidence.\n\n")
    seen = set()
    for ident, sec, body in found:
        seen.add(ident)
        if ident in rows:
            rows[ident][1] = sec
            if rows[ident][9] == "not in draft":
                rows[ident][9] = "open"
        else:
            row = [ident, sec, body] + [""] * (len(COLS) - 3)
            row[9] = "open"
            rows[ident] = row
            order.append(ident)
    # Seed rows (section "seed") predate the drafts, so absence from them means
    # nothing; a draft that reuses the id takes the row over (section updated above).
    for ident, row in rows.items():
        if ident not in seen and row[1] != "seed" and row[9] in ("open", "gathering"):
            row[9] = "not in draft"
    out = pre + HEADER + "".join(
        "| " + " | ".join(c.replace("|", "\\|") for c in rows[i]) + " |\n" for i in order)
    LEDGER.write_text(out + (post if post.strip() else ""))
    counts = {}
    for row in rows.values():
        counts[row[9]] = counts.get(row[9], 0) + 1
    print(f"{len(found)} markers in drafts; ledger rows: " +
          ", ".join(f"{k or 'blank'} {v}" for k, v in sorted(counts.items())))
    if "--check" in sys.argv:
        unresolved = [i for i in order if rows[i][9] in ("open", "gathering")]
        loose = [i for i in order if rows[i][9] == "not in draft"]
        if found:
            print("open markers remain:", ", ".join(i for i, _, _ in found))
        if unresolved:
            print("ledger rows still open or gathering:", ", ".join(unresolved))
        if loose:
            print("warning, marker removed but row not resolved (set have, failed or dropped):",
                  ", ".join(loose))
        if found or unresolved:
            sys.exit(1)


if __name__ == "__main__":
    main()
