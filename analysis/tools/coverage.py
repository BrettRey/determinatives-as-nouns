#!/usr/bin/env python3
"""Coverage of the extracted claim set by construction and noun subcategory.

The paper argues that common noun, proper noun, pronoun and determinative are
four coordinate subcategories of Noun (determinatives-as-nouns.tex:716).  A
diagnostic that separates or unites those subcategories is worth more when it
has been applied across them.  This script reports, per construction, which
subcategories the claim set actually covers.

IMPORTANT: absence from the claim set is not absence from the manuscript.  The
extraction is "a bounded selection from the full documents, not an exhaustive
inventory" (expanded-json-2026-09-14/README.md).  Every gap this reports is a
place to look in the manuscript, not a finding about the manuscript.

SUBCATEGORY assignments below are the analyst's, grounded in the manuscript
lines cited in the `why' field.  They are not a field in records.json; the
lexeme entries carry only id and forms.
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / "analysis" / "expanded-json-2026-09-14"

# (subcategory, grounding).  "CGEL/paper default" marks the uncontroversial
# determinative inventory the paper takes over without separate argument.
SUBCATEGORY = {
    "lex_the": ("determinative", "CGEL/paper default"),
    "lex_a": ("determinative", "CGEL/paper default"),
    "lex_every": ("determinative", "CGEL/paper default"),
    "lex_some": ("determinative", "CGEL/paper default"),
    "lex_few": ("determinative", "CGEL/paper default"),
    "lex_no": ("determinative", "CGEL/paper default"),
    "lex_many": ("determinative", "CGEL/paper default"),
    "lex_much": ("determinative", "CGEL/paper default"),
    "lex_little": ("determinative", "CGEL/paper default"),
    "lex_several": ("determinative", "supplement: CGEL includes several among determinatives"),
    "lex_all": ("determinative", "CGEL/paper default"),
    "lex_both": ("determinative", "CGEL/paper default"),
    "lex_any": ("determinative", "CGEL/paper default"),
    "lex_enough": ("determinative", "CGEL/paper default"),
    "lex_this": ("determinative", "CGEL/paper default"),
    "lex_that": ("determinative", "CGEL/paper default"),
    "lex_certain": ("determinative", "supplement: CGEL treats certain/various as marginal determinatives"),
    "lex_various": ("determinative", "supplement: CGEL treats certain/various as marginal determinatives"),
    "lex_anyone": ("determinative", "ms: 'anyone takes the premodifiers of its determinative base any'"),
    "lex_something": ("determinative", "ms: 'Compound determinatives also take post-head adjectives'"),
    "lex_ten": ("determinative", "cardinal numeral, treated with the determinative inventory"),
    "lex_thirty": ("determinative", "cardinal numeral, treated with the determinative inventory"),

    "lex_my": ("pronoun", "ms: 'Dependent my and independent mine belong to one pronoun paradigm'"),

    "lex_book": ("common noun", "the paper's plain common-noun control"),
    "lex_lot": ("common noun", "ms: CGEL categorizes quantificational plenty/lot as common nouns"),
    "lex_lots": ("common noun", "quantificational common noun, with lot"),
    "lex_heaps": ("common noun", "quantificational common noun, with lot"),
    "lex_deal": ("common noun", "ms: 'Quantificational nouns occur in degree modifiers such as a great deal smaller'"),
    "lex_plenty": ("common noun", "ms: CGEL categorizes quantificational plenty as a common noun"),

    "lex_numerous": ("adjective (control)", "ms §2.3 'Quantificational adjectives and nominal independence'"),
    "lex_multiple": ("adjective (control)", "ms §2.3"),
    "lex_countless": ("adjective (control)", "ms §2.3"),
    "lex_rich": ("adjective (control)", "ms: 'only the former has a noun as lexical head'"),
    "lex_second": ("adjective (control)", "ms: 'Adjective fusion permits indefinite ordinal a second'"),
}

# The four coordinate subcategories the paper's taxonomy asserts.
FOUR = ["determinative", "common noun", "pronoun", "proper noun"]

# Manuscript verification of the gaps the claim set shows, done by hand against
# determinatives-as-nouns.tex on 2026-09-14.  Line numbers are from that file.
# This is what keeps a claim-set gap from being reported as a manuscript gap.
VERIFIED = {
    "dependent_det": (
        "artifact",
        "L118 gives Det function for a pronoun (*my preferences*), a proper noun "
        "(*Kim's preferences*) and a common noun (*people's preferences*), citing "
        "CGEL 354-355, 470-471. The manuscript covers 4/4 here; the extraction "
        "simply did not select that passage."),
    "peripheral_mod_admission": (
        "partly artifact",
        "Sec. `Modifier selection and attachment' gives *only you* (pronoun) and "
        "*Usually a careful driver, Anne found...* (common noun) alongside "
        "*almost every experienced teacher*. Manuscript covers 3/4; proper noun "
        "remains untested."),
    "comparative_complement": (
        "principled",
        "L164 groups comparative complementation with grade and degree-modifier "
        "selection as an *adjectival* property, weighed as a counterweight. "
        "Four-way nominal coverage is not expected and its absence is not a gap."),
    "dependent_internal_mod": (
        "principled",
        "This is the adjectival control construction of Sec. 2.3 (*numerous "
        "people* against *many people*). It exists to contrast with the nominal "
        "diagnostics, not to be one."),
}


def main():
    records = json.loads((RUN / "records.json").read_text())
    supplement = {e["query_id"] for e in json.loads((RUN / "supplement-cell-map.json").read_text())}

    missing = [l["id"] for l in records["lexemes"] if l["id"] not in SUBCATEGORY]
    if missing:
        sys.exit(f"unassigned lexemes: {missing}")

    by_con = defaultdict(lambda: defaultdict(list))
    for c in records["participation_claims"]:
        sub = SUBCATEGORY[c["lexeme_id"]][0]
        block = "supplement" if c["id"] in supplement else "manuscript"
        by_con[c["construction_id"]][sub].append((c["id"], c["form"], block))

    out = []
    out.append("# Claim-set coverage by construction and noun subcategory\n")
    out.append("Generated by `analysis/tools/coverage.py` from "
               "`analysis/expanded-json-2026-09-14/records.json`.\n")
    out.append("The paper argues that common noun, proper noun, pronoun and determinative are "
               "four coordinate subcategories of Noun. A diagnostic carries more weight when it "
               "has been applied across them. This table reports what the *claim set* covers.\n")
    out.append("**Absence here is not absence from the manuscript.** The extraction is a bounded "
               "selection, so each gap is a place to check, not a finding.\n")

    # Per-subcategory totals.
    totals = defaultdict(int)
    lex_totals = defaultdict(set)
    for c in records["participation_claims"]:
        sub = SUBCATEGORY[c["lexeme_id"]][0]
        totals[sub] += 1
        lex_totals[sub].add(c["lexeme_id"])
    out.append("## Claims by subcategory\n")
    out.append("| Subcategory | Lexemes | Claims |")
    out.append("|---|---:|---:|")
    for sub in FOUR + ["adjective (control)"]:
        out.append(f"| {sub} | {len(lex_totals[sub])} | {totals[sub]} |")
    out.append("")

    empty = [s for s in FOUR if not totals[s]]
    thinnest = [s for s in FOUR if 0 < totals[s] <= 2]
    out.append("## The two legs that carry least\n")
    if empty:
        out.append(f"**{', '.join(empty)}: no claims at all**, across all "
                   f"{len(by_con)} constructions. The manuscript is not silent on proper nouns, "
                   "but what it has is taxonomic statement plus three data points borrowed from "
                   "*CGEL* (*Kim's preferences* L118, *the Smiths* L184, *Kim left* L370) and two "
                   "restrictive property claims (L148, L734). Exactly one of the paper's eleven "
                   "constructions has a proper-noun instance anywhere in the manuscript "
                   "(*Kim's preferences* in Det function); the other ten have none. L726 "
                   "concedes the point: "
                   "extending the feature matrix to common nouns, proper nouns and adjectives "
                   "\"would require new sampling, feature selection, and coding across all "
                   "groups.\"\n")
    for s_ in thinnest:
        out.append(f"**{s_}: {totals[s_]} claim{'' if totals[s_] == 1 else 's'}** "
                   f"({', '.join(sorted(l for l in lex_totals[s_]))}). The manuscript adds "
                   "*poor old me* (L732), *She left* (L370), *only you* (modifier section) and "
                   "the case/genitive discussion (L190), all CGEL-cited.\n")
    out.append("The determinative and common-noun legs carry "
               f"{totals['determinative']} and {totals['common noun']} claims. The taxonomy is "
               "four-way; the evidence is close to two-way, with an adjectival contrast class "
               f"({totals['adjective (control)']} claims) doing more work than two of the four "
               "subcategories it is meant to sit beside.\n")
    out.append("## Coverage by construction\n")
    out.append("`n/4` counts how many of the four coordinate subcategories appear. "
               "Adjective controls are listed but not counted, since the paper uses them as a "
               "contrast class rather than a noun subcategory.\n")
    out.append("| Construction | n/4 | Determinative | Common noun | Pronoun | Proper noun | Adj (control) |")
    out.append("|---|---:|---|---|---|---|---|")

    def cell(entries):
        if not entries:
            return "~"
        forms = sorted({f for _, f, _ in entries})
        return ", ".join(f"*{f}*" for f in forms)

    order = sorted(by_con, key=lambda k: -sum(len(v) for v in by_con[k].values()))
    for con in order:
        subs = by_con[con]
        n = sum(1 for s in FOUR if subs.get(s))
        row = [con, f"**{n}/4**"] + [cell(subs.get(s, [])) for s in FOUR] + [cell(subs.get("adjective (control)", []))]
        out.append("| " + " | ".join(row) + " |")
    out.append("")

    thin = [c for c in order if sum(1 for s in FOUR if by_con[c].get(s)) <= 1]
    out.append("## Constructions resting on a single subcategory\n")
    out.append(f"{len(thin)} of {len(order)} constructions have claims from at most one of the "
               "four coordinate subcategories:\n")
    for c in thin:
        subs = [s for s in FOUR if by_con[c].get(s)]
        n_claims = sum(len(v) for v in by_con[c].values())
        plural = "claim" if n_claims == 1 else "claims"
        out.append(f"- `{c}` ({n_claims} {plural}): "
                   f"{subs[0] if subs else 'none of the four'} only")
        verdict, note = VERIFIED.get(c, ("unchecked", "Not yet checked against the manuscript."))
        out.append(f"  - **{verdict}**: {note}")
    out.append("")
    out.append("`artifact` means the manuscript covers what the claim set does not, so the gap is "
               "in the extraction. `principled` means four-way coverage is not expected there. "
               "Neither is a defect in the paper.\n")

    out.append("## Subcategory assignments used\n")
    out.append("| Lexeme | Subcategory | Grounding |")
    out.append("|---|---|---|")
    for lid, (sub, why) in sorted(SUBCATEGORY.items(), key=lambda kv: (kv[1][0], kv[0])):
        out.append(f"| `{lid}` | {sub} | {why} |")

    dest = ROOT / "analysis" / "coverage-2026-09-14.md"
    dest.write_text("\n".join(out) + "\n")
    print(f"wrote {dest.relative_to(ROOT)}")
    print("\n".join(out[:0]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
