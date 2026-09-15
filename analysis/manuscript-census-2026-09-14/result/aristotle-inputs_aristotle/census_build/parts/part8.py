# -*- coding: utf-8 -*-
# Part 8: sec:economy (no claims), sec:fragment

CLAIMS = []

# ---------------- sec:fragment: permission table ----------------
# (form label, row quote, Det, Mod, Subj, Obj/CompP, target note)
ROWS = [
 (r"\mention{the}",  r"\mention{the} & yes & -- & -- & -- & No count or number restriction",
  "yes", "no", "no", "no", "No count or number restriction on the target."),
 (r"\mention{a}", r"\mention{a} & yes & -- & -- & -- & Singular count",
  "yes", "no", "no", "no", "Singular count target."),
 (r"\mention{every}", r"\mention{every} & yes & yes & -- & -- & Singular count; Mod after genitive Det",
  "yes", "yes", "no", "no", "Singular count target; Mod use only after a genitive Det."),
 (r"\mention{some}", r"\mention{some} & yes & -- & yes & yes & Plural count or non-count",
  "yes", "no", "yes", "yes", "Plural count or non-count target."),
 (r"\mention{few}", r"\mention{few} & yes & yes & yes & yes & Plural count",
  "yes", "yes", "yes", "yes", "Plural count target."),
 (r"\mention{no}", r"\mention{no} & yes & -- & -- & -- & No count or number restriction",
  "yes", "no", "no", "no", "No count or number restriction on the target."),
 (r"\mention{none}", r"\mention{none} & -- & -- & yes & yes & Not applicable",
  "no", "no", "yes", "yes", "No target: the form is independent only."),
 (r"\mention{my}", r"\mention{my} & yes & -- & -- & -- & No count or number restriction",
  "yes", "no", "no", "no", "No count or number restriction on the target."),
 (r"\mention{mine}", r"\mention{mine} & -- & -- & yes & yes & Not applicable",
  "no", "no", "yes", "yes", "No target: the form is independent only."),
 (r"\mention{she}", r"\mention{she} & -- & -- & yes & -- & Not applicable",
  "no", "no", "yes", "no", "Nominative form, subject use only."),
 (r"\mention{her} (plain)", r"\mention{her} (plain) & -- & -- & -- & yes & Not applicable",
  "no", "no", "no", "yes", "Plain (accusative) form; object and prepositional complement only."),
]

FUNCS = [
 ("det", "Det (determiner before another nominal)"),
 ("mod", "internal Mod before another nominal"),
 ("subj", "subject"),
 ("objcomp", "object or complement of a preposition"),
]

n = 0
for form, rowq, det, mod, subj, obj, target in ROWS:
    vals = {"det": det, "mod": mod, "subj": subj, "objcomp": obj}
    for key, label in FUNCS:
        n += 1
        allowed = vals[key] == "yes"
        CLAIMS.append((
            "frg-t%03d" % n, "sec:fragment", form, label,
            "conditional" if (allowed and key in ("det", "mod")) else ("licensed" if allowed else "excluded"),
            "authors_analysis", rowq,
            target if allowed and key in ("det", "mod") else "",
            "Permission table of the fragment; a dash marks absence of the stated permission."))

CLAIMS += [

("frg-001", "sec:fragment", "relative postmodifiers",
 "admission into the fragment without analysis of their internal grammar",
 "licensed", "authors_analysis",
 r"It admits relative postmodifiers without analysing their internal grammar.",
 "", ""),

("frg-002", "sec:fragment", "predication, interrogative clause structure, and modification outside NP structure",
 "coverage by the fragment",
 "not_stated", "authors_analysis",
 r"Predication, interrogative clause structure, and modification outside NP structure lie beyond its scope.",
 "", "Outside the fragment's scope, so no permission is stated."),

("frg-003", "sec:fragment", "a phrase occurrence in a licensed construction",
 "intermediate Head relations within its projection",
 "licensed", "authors_analysis",
 r"Intermediate Head relations within its projection don't require a further argument permission.",
 "", ""),

("frg-004", "sec:fragment", r"unstressed \mention{some}",
 "target restriction before another nominal",
 "conditional", "authors_analysis",
 r"Unstressed \mention{some} has the target restriction shown.",
 "Plural count or non-count target.", "Table caption."),

("frg-005", "sec:fragment", "quotation, metalinguistic naming, and subordinate-clause uses of dependent genitives",
 "coverage by the fragment",
 "not_stated", "authors_analysis",
 r"Quotation, metalinguistic naming, and subordinate-clause uses of dependent genitives fall outside the fragment.",
 "", "Outside the fragment's scope."),

("frg-006", "sec:fragment", r"\mention{some} in \mention{some apples}",
 "Det permission with plural-count target selection",
 "licensed", "authors_analysis",
 r"In \mention{some apples}, \mention{some}'s phrase satisfies its Det permission and plural-count target selection.",
 "", ""),

("frg-007", "sec:fragment", r"\mention{some} in \mention{Some left}",
 "subject permission",
 "licensed", "authors_analysis",
 r"In \mention{Some left}, it satisfies its subject permission.",
 "", ""),

("frg-008", "sec:fragment", r"\mention{Every apple}",
 "dependent determiner use",
 "licensed", "authors_analysis",
 r"\mention{Every apple} passes the dependent checks",
 "", ""),

("frg-009", "sec:fragment", r"independent \mention{every}",
 r"subject use, as in \ungram{\mention{Every arrived}}",
 "excluded", "constructed_ungrammatical",
 r"independent \ungram{\mention{Every arrived}} fails its use permission",
 "", "Marked ungrammatical."),

("frg-010", "sec:fragment", r"\mention{the}",
 r"determination of a nominal headed by an independent determinative, as in \mention{the few}",
 "licensed", "authors_analysis",
 r"Thus \mention{the} permits plural \mention{few} in \mention{the few}.",
 "", ""),

("frg-011", "sec:fragment", r"\mention{this} in \mention{this much}",
 "degree modifier permission distinct from demonstrative Det selection",
 "licensed", "authors_analysis",
 r"The modifier \mention{this} in \mention{this much} expresses degree; its permission doesn't follow from demonstrative Det selection.",
 "", ""),

("frg-012", "sec:fragment", r"\mention{that day}",
 r"temporal adjunct, as in \mention{I saw him that day}",
 "licensed", "not_determinable",
 r"\mention{I saw him that day} is possible",
 "", "Hudson's temporal adjunct evidence."),

("frg-013", "sec:fragment", r"\mention{that point in time}",
 "temporal adjunct",
 "excluded", "constructed_ungrammatical",
 r"whereas \ungram{\mention{I saw him that point in time}} isn't, despite the similar temporal meanings",
 "", "Marked ungrammatical; Hudson's evidence for common-noun headedness."),

("frg-014", "sec:fragment", "a singular count noun",
 "argument use",
 "conditional", "authors_analysis",
 r"A singular count noun normally requires determination, while \mention{every} requires another nominal and \mention{some} doesn't.",
 "Determination normally required.", ""),

("frg-015", "sec:fragment", r"\mention{every}",
 "occurrence without another nominal",
 "excluded", "authors_analysis",
 r"A singular count noun normally requires determination, while \mention{every} requires another nominal and \mention{some} doesn't.",
 "", ""),

("frg-016", "sec:fragment", r"\mention{some}",
 "occurrence without another nominal",
 "licensed", "authors_analysis",
 r"A singular count noun normally requires determination, while \mention{every} requires another nominal and \mention{some} doesn't.",
 "", ""),

("frg-017", "sec:fragment", "an expression in an external use",
 "use permission, form selection, and target and dependent conditions",
 "conditional", "authors_analysis",
 r"In the external uses listed above, an expression has to pass three checks: permission for its use, selection of its form, and satisfaction of target and dependent conditions.",
 "All three checks must be satisfied.", ""),

("frg-018", "sec:fragment", r"independent \mention{none} in \mention{none of the students}",
 "form selection in the partitive",
 "conditional", "authors_analysis",
 r"$\operatorname{Form}$ checks the selected form, including independent \mention{none} in \mention{none of the students}.",
 "The independent form must be selected.", ""),
]
