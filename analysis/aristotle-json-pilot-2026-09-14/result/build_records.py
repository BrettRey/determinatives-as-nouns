#!/usr/bin/env python3
"""Build records.json for the lexeme/construction extraction task.

Every evidence quote is checked to be an exact nonempty substring of the
corresponding supplied excerpt, and the result is validated against the
supplied JSON schema (structurally, including enums and required keys).
"""

import json
import re
import sys

ROOT = "/workspace/request-project"

prompt = json.load(open(f"{ROOT}/prompt.json"))
schema = json.load(open(f"{ROOT}/schema.json"))
SRC = {e["id"]: e["text"] for e in prompt["source_excerpts"]}
CAT = prompt["construction_catalog"]


def q(sid, text):
    return {"source_id": sid, "quote": text}


def C(bearer, requirement):
    return {"bearer": bearer, "requirement": requirement}


# --- table rows in S05 -------------------------------------------------
ROW_THE = r"\mention{the} & yes & -- & -- & -- & No count or number restriction"
ROW_EVERY = r"\mention{every} & yes & yes & -- & -- & Singular count; Mod after genitive Det"
ROW_SOME = r"\mention{some} & yes & -- & yes & yes & Plural count or non-count"
ROW_FEW = r"\mention{few} & yes & yes & yes & yes & Plural count"
ROW_NO = r"\mention{no} & yes & -- & -- & -- & No count or number restriction"
ROW_NONE = r"\mention{none} & -- & -- & yes & yes & Not applicable"
ROW_MY = r"\mention{my} & yes & -- & -- & -- & No count or number restriction"
ROW_MINE = r"\mention{mine} & -- & -- & yes & yes & Not applicable"

lexemes = [
    {"id": "lex_the", "forms": ["the"]},
    {"id": "lex_every", "forms": ["every"]},
    {"id": "lex_some", "forms": ["some"]},
    {"id": "lex_few", "forms": ["few"]},
    {"id": "lex_no", "forms": ["no", "none"]},
    {"id": "lex_my", "forms": ["my", "mine"]},
    {"id": "lex_book", "forms": ["book", "books"]},
]

constructions = [{"id": k, "description": v} for k, v in CAT.items()]

claims = []


def add(pid, lex, form, con, status, conditions, evidence):
    claims.append({
        "id": pid,
        "lexeme_id": lex,
        "form": form,
        "construction_id": con,
        "status": status,
        "conditions": conditions,
        "evidence": evidence,
    })


# P01 -- the as Det
add("P01", "lex_the", "the", "dependent_det", "licensed",
    [
        C("target_nominal", "No count or number restriction."),
        C("target_nominal",
          "May itself be a nominal headed by an independent determinative, e.g. plural "
          "few in the few."),
    ],
    [
        q("S05", ROW_THE),
        q("S07", r"Target restrictions apply to the nominal being determined or modified, including a nominal headed by an independent determinative. Thus \mention{the} permits plural \mention{few} in \mention{the few}."),
    ])

# P02 -- the in independent argument use
add("P02", "lex_the", "the", "independent_argument", "excluded",
    [],
    [
        q("S01", r"The articles lack an independent argument form"),
        q("S05", ROW_THE),
        q("S11", r"The article's exclusion from argument use remains a separate condition."),
    ])

# P03 -- every as Det
add("P03", "lex_every", "every", "dependent_det", "licensed",
    [
        C("target_nominal", "Singular count."),
        C("own_phrase", "Requires another nominal; it cannot stand without a target."),
    ],
    [
        q("S05", ROW_EVERY),
        q("S08", r"\mention{every} requires another nominal"),
    ])

# P04 -- every as internal Mod
add("P04", "lex_every", "every", "dependent_internal_mod", "licensed",
    [
        C("target_nominal", "Singular count."),
        C("own_phrase", "In Mod function it occurs after a genitive Det."),
        C("construction", "Mod is internal, i.e. a use before another nominal."),
    ],
    [
        q("S05", ROW_EVERY),
        q("S05", r"Det and Mod concern uses before another nominal; Mod is internal."),
    ])

# P05 -- every independent
add("P05", "lex_every", "every", "independent_argument", "excluded",
    [],
    [
        q("S05", ROW_EVERY),
        q("S08", r"\mention{every} requires another nominal"),
        q("S09", r"These permissions don't transfer to \mention{every} or the articles."),
    ])

# P06 -- some as Det
add("P06", "lex_some", "some", "dependent_det", "licensed",
    [
        C("target_nominal", "Plural count or non-count (the target restriction of unstressed some)."),
        C("own_phrase",
          "Excludes external determination, partitive complements, and relative "
          "postmodifiers within its own phrase."),
    ],
    [
        q("S05", ROW_SOME),
        q("S05", r"Unstressed \mention{some} has the target restriction shown."),
        q("S09", r"In Det or internal Mod function before a target, ordinary \mention{some} and \mention{few} exclude external determination, partitive complements, and relative postmodifiers within their own phrase."),
    ])

# P07 -- independent some
add("P07", "lex_some", "some", "independent_argument", "licensed",
    [
        C("own_phrase", "Permits selected partitives and relatives."),
        C("own_phrase",
          "Takes its number/count interpretation from the construction and domain."),
        C("construction", "Covers Subj and Obj / CompP uses."),
    ],
    [
        q("S05", ROW_SOME),
        q("S09", r"Independent \mention{some} and \mention{few} permit selected partitives and relatives"),
        q("S07", r"\mention{some} takes its interpretation from the construction and domain"),
        q("S06", r"Subj and Obj denote subject and object; CompP denotes complement of a preposition."),
    ])

# P08 -- few as Det
add("P08", "lex_few", "few", "dependent_det", "licensed",
    [
        C("target_nominal", "Plural count."),
        C("own_phrase",
          "Excludes external determination, partitive complements, and relative "
          "postmodifiers within its own phrase."),
    ],
    [
        q("S05", ROW_FEW),
        q("S09", r"In Det or internal Mod function before a target, ordinary \mention{some} and \mention{few} exclude external determination, partitive complements, and relative postmodifiers within their own phrase."),
    ])

# P09 -- few as internal Mod in "the few people"
add("P09", "lex_few", "few", "dependent_internal_mod", "licensed",
    [
        C("target_nominal", "Plural count; in the few people it is the nominal headed by people."),
        C("own_phrase",
          "Excludes external determination, partitive complements, and relative "
          "postmodifiers within its own phrase."),
        C("outer_np",
          "The article the determines the outer nominal headed by people, not the "
          "phrase headed by few."),
    ],
    [
        q("S05", ROW_FEW),
        q("S09", r"In Det or internal Mod function before a target, ordinary \mention{some} and \mention{few} exclude external determination, partitive complements, and relative postmodifiers within their own phrase."),
        q("S10", r"In \mention{the few people}, its phrase is an internal Mod of the nominal headed by \mention{people}"),
    ])

# P10 -- independent few
add("P10", "lex_few", "few", "independent_argument", "licensed",
    [
        C("own_phrase", "Permits selected partitives and relatives."),
        C("own_phrase",
          "Permits definite determination and adjectival premodification, as in the lucky few."),
        C("own_phrase", "Is plural count."),
        C("construction", "Covers Subj and Obj / CompP uses."),
    ],
    [
        q("S05", ROW_FEW),
        q("S09", r"Independent \mention{some} and \mention{few} permit selected partitives and relatives; independent \mention{few} also permits definite determination and adjectival premodification, as in \mention{the lucky few}."),
        q("S07", r"\mention{few} is plural count"),
        q("S10", r"in \mention{the lucky few}, \mention{few} heads the independently determined NP"),
    ])

# P11 -- dependent no
add("P11", "lex_no", "no", "dependent_det", "licensed",
    [
        C("target_nominal", "No count or number restriction."),
        C("own_phrase", "The dependent form no is the one selected, as in no students."),
        C("own_phrase", "Permits almost."),
    ],
    [
        q("S05", ROW_NO),
        q("S02", r"dependent \mention{no students} contrasts with independent \mention{none}, while both permit \mention{almost}"),
    ])

# P12 -- no in independent argument use
add("P12", "lex_no", "no", "independent_argument", "excluded",
    [],
    [
        q("S05", ROW_NO),
        q("S02", r"dependent \mention{no students} contrasts with independent \mention{none}"),
    ])

# P13 -- none in independent argument use
add("P13", "lex_no", "none", "independent_argument", "licensed",
    [
        C("own_phrase", "The independent form none is required; no target nominal applies."),
        C("own_phrase", "Permits almost."),
        C("construction", "Covers Subj and Obj / CompP uses."),
    ],
    [
        q("S05", ROW_NONE),
        q("S02", r"dependent \mention{no students} contrasts with independent \mention{none}, while both permit \mention{almost}"),
        q("S06", r"Subj and Obj denote subject and object; CompP denotes complement of a preposition."),
    ])

# P14 -- none in partitive
add("P14", "lex_no", "none", "independent_partitive", "licensed",
    [
        C("own_phrase",
          "Requires the independent form none; the dependent form no is excluded here "
          "(no of the students)."),
    ],
    [
        q("S02", r"The partitive \mention{none of the students} requires the independent form; \ungram{\mention{no of the students}} is excluded."),
        q("S05", ROW_NONE),
    ])

# P15 -- dependent my
add("P15", "lex_my", "my", "dependent_det", "licensed",
    [
        C("target_nominal", "No count or number restriction."),
        C("own_phrase",
          "In the ordinary NP construction the dependent form my requires a following nominal."),
        C("construction",
          "Quotation, metalinguistic naming, and subordinate-clause uses of dependent "
          "genitives fall outside the fragment."),
    ],
    [
        q("S05", ROW_MY),
        q("S01", r"\mention{My} remains a noun even though, in the ordinary NP construction, it requires a following nominal."),
        q("S06", r"Quotation, metalinguistic naming, and subordinate-clause uses of dependent genitives fall outside the fragment."),
    ])

# P16 -- independent mine as subject
add("P16", "lex_my", "mine", "independent_argument", "licensed",
    [
        C("own_phrase", "The independent form mine is required; no target nominal applies."),
        C("possessor", "The genitive's person identifies the possessor."),
        C("possessed_referent",
          "The independent NP's agreement reflects the possessed entity or entities "
          "(Mine is ready vs Mine are ready)."),
        C("construction", "Ordinary Head needs a constructional agreement condition."),
    ],
    [
        q("S05", ROW_MINE),
        q("S03", r"The genitive's person identifies the possessor; the independent NP's agreement reflects the possessed entity or entities. Compare constructed \mention{Mine is ready} (\enquote*{my contribution}) and \mention{Mine are ready} (\enquote*{my slides}). Ordinary Head therefore needs a constructional agreement condition."),
    ])

# P17 -- bare singular count book as subject
add("P17", "lex_book", "book", "independent_argument", "excluded",
    [
        C("own_phrase",
          "A singular count noun normally requires determination; bare book leaves that "
          "requirement unsatisfied."),
    ],
    [
        q("S11", r"Bare \ungram{\mention{Book arrived}} fails that requirement"),
        q("S08", r"A singular count noun normally requires determination"),
    ])

# P18 -- bare plural books as subject
add("P18", "lex_book", "books", "independent_argument", "licensed",
    [
        C("own_phrase",
          "Bare plural books satisfies the determination requirement that bare singular "
          "book fails."),
    ],
    [
        q("S11", r"Bare \ungram{\mention{Book arrived}} fails that requirement, while \mention{Books arrived} passes."),
    ])

# P19 -- some as degree modifier of an adjective
add("P19", "lex_some", "some", "degree_modifier_adj", "not_stated", [], [])

# P20 -- dependent form my in independent argument use
add("P20", "lex_my", "my", "independent_argument", "excluded",
    [],
    [
        q("S05", ROW_MY),
        q("S01", r"Dependent \mention{my} and independent \mention{mine} belong to one pronoun paradigm."),
        q("S02", r"Form selection remains necessary, just as with \mention{my}/\mention{mine}."),
    ])

scope_checks = [
    {
        "id": "the_apple",
        "answer": (
            "Permissions follow each phrase's own lexical head, so the two levels are "
            "distinct. The smaller article phrase headed by the has the Det permission, "
            "used before the target nominal apple (no count or number restriction on that "
            "target). The outer NP has the argument permission through its head apple, "
            "whose determination requirement is satisfied by the article phrase. The "
            "article's exclusion from independent argument use is a separate condition on "
            "occurrences of the in that construction, so it does not block the outer NP "
            "from argument use: a permission applies to an occurrence in the specified "
            "construction, and intermediate Head relations within the projection need no "
            "further argument permission."
        ),
        "evidence": [
            q("S11", r"Each phrase's use permission follows its own lexical head. In \mention{the apple}, the smaller article phrase has Det permission; the outer NP has argument permission through \mention{apple}, whose determination requirement is satisfied."),
            q("S11", r"The article's exclusion from argument use remains a separate condition."),
            q("S04", r"A permission applies to an occurrence in the specified construction. Intermediate Head relations within its projection don't require a further argument permission."),
            q("S05", ROW_THE),
        ],
    },
    {
        "id": "the_few_people",
        "answer": (
            "No. In the few people the phrase headed by few is an internal Mod of the "
            "nominal headed by people, so the determines that larger nominal, not the "
            "phrase headed by few; in this dependent use ordinary few excludes external "
            "determination within its own phrase. By contrast, in the lucky few, few heads "
            "the independently determined NP, and independent few does permit definite "
            "determination and adjectival premodification. These are the two distinguished "
            "uses of few, and the relevant target restriction on the is only that the "
            "nominal it determines may itself be headed by an independent determinative, "
            "as in the few."
        ),
        "evidence": [
            q("S10", r"The constraints also distinguish the uses of \mention{few}. In \mention{the few people}, its phrase is an internal Mod of the nominal headed by \mention{people}; in \mention{the lucky few}, \mention{few} heads the independently determined NP."),
            q("S09", r"In Det or internal Mod function before a target, ordinary \mention{some} and \mention{few} exclude external determination, partitive complements, and relative postmodifiers within their own phrase."),
            q("S09", r"independent \mention{few} also permits definite determination and adjectival premodification, as in \mention{the lucky few}"),
            q("S07", r"Thus \mention{the} permits plural \mention{few} in \mention{the few}."),
        ],
    },
]

records = {
    "lexemes": lexemes,
    "constructions": constructions,
    "participation_claims": claims,
    "scope_checks": scope_checks,
}

# ---------------------------------------------------------------- checks
errors = []


def check_evidence(container, label):
    for ev in container:
        if not ev["quote"]:
            errors.append(f"{label}: empty quote")
        elif ev["quote"] not in SRC[ev["source_id"]]:
            errors.append(f"{label}: quote not a substring of {ev['source_id']}: {ev['quote'][:70]!r}")


for c in claims:
    check_evidence(c["evidence"], c["id"])
    if c["status"] == "not_stated" and (c["evidence"] or c["conditions"]):
        errors.append(f"{c['id']}: not_stated must have empty evidence and conditions")
    if c["status"] != "not_stated" and not c["evidence"]:
        errors.append(f"{c['id']}: missing evidence")
for s in scope_checks:
    check_evidence(s["evidence"], s["id"])

# query ids / forms / lexemes / constructions must match the supplied queries
by_id = {c["id"]: c for c in claims}
for qy in prompt["queries"]:
    c = by_id.get(qy["id"])
    if c is None:
        errors.append(f"missing query {qy['id']}")
        continue
    for k in ("form", "lexeme_id", "construction_id"):
        if c[k] != qy[k]:
            errors.append(f"{qy['id']}: {k} mismatch")
if len(claims) != len(prompt["queries"]):
    errors.append("claim count mismatch")
if {l["id"] for l in lexemes} != set(prompt["lexeme_ids"]):
    errors.append("lexeme id mismatch")
if {c["id"] for c in constructions} != set(prompt["construction_catalog"]):
    errors.append("construction id mismatch")
if {s["id"] for s in scope_checks} != set(prompt["scope_checks"]):
    errors.append("scope check id mismatch")


def validate(node, sch, path="$"):
    t = sch.get("type")
    if t == "object":
        if not isinstance(node, dict):
            errors.append(f"{path}: expected object")
            return
        for r in sch.get("required", []):
            if r not in node:
                errors.append(f"{path}: missing required {r}")
        props = sch.get("properties", {})
        for k, v in node.items():
            if k not in props:
                if sch.get("additionalProperties") is False:
                    errors.append(f"{path}: additional property {k}")
            else:
                validate(v, props[k], f"{path}.{k}")
    elif t == "array":
        if not isinstance(node, list):
            errors.append(f"{path}: expected array")
            return
        for i, v in enumerate(node):
            validate(v, sch["items"], f"{path}[{i}]")
    elif t == "string":
        if not isinstance(node, str):
            errors.append(f"{path}: expected string")
        elif "enum" in sch and node not in sch["enum"]:
            errors.append(f"{path}: {node!r} not in enum")


validate(records, schema)

if errors:
    print("FAILED:")
    for e in errors:
        print(" -", e)
    sys.exit(1)

with open(f"{ROOT}/records.json", "w") as f:
    json.dump(records, f, indent=2, ensure_ascii=False)
    f.write("\n")
print("records.json written; all checks passed")
print("claims:", len(claims), "lexemes:", len(lexemes), "constructions:", len(constructions))
print("status counts:", {s: sum(1 for c in claims if c["status"] == s)
                          for s in ("licensed", "excluded", "not_stated")})
