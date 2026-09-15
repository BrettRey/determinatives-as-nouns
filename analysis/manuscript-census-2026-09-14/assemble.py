#!/usr/bin/env python3
"""Exhaustive census of the manuscript's participation claims.

Why this run exists. The 56 manuscript claims in the expanded run were produced
against a quota ("approximately 80-110 NEW participation queries"), not a
sampling frame, and its README calls the result a bounded selection. Proportions
over them estimate nothing: *the lucky few* appears eight times and is the worked
example of Figure 6, yet has no record in that set.

This run defines the frame instead. Every place the manuscript asserts that an
expression does, does not, or conditionally does occur in a syntactic function
or construction is to be recorded, section by section, with a required
per-section count so that omissions are visible.

evidence_type is required from the start rather than added afterwards.
"""

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
UPLOAD = HERE / "aristotle-inputs"
MS = ROOT / "determinatives-as-nouns.tex"

SECTION = re.compile(r"^\\(sub)?section\{(.+?)\}\\label\{(.+?)\}", re.M)

EVIDENCE_TYPE = [
    "cgel_described", "cgel_restricted", "constructed_illustration",
    "constructed_ungrammatical", "retained_attestation", "searched_not_found",
    "authors_analysis", "not_determinable",
]

# Held out from the task. Every one is a participation claim the manuscript
# plainly makes; an exhaustive census must reach all of them.
ACCEPTANCE = [
    "the lucky few", "the very few", "almost every experienced teacher",
    "poor old me", "Kim's preferences", "the Smiths", "only you",
    "the idle rich", "the few people", "so many mistakes",
]

INSTRUCTIONS = (
    "Enumerate EVERY participation claim the manuscript makes. A participation claim is any "
    "assertion that a specific expression does occur, does not occur, or occurs only under "
    "stated conditions, in a specific syntactic function or construction. "
    "This is a census, not a sample. There is NO target number. Do not stop at a round figure, "
    "do not select representative cases, and do not skip a claim because it resembles one "
    "already recorded: if the manuscript asserts it of a different expression or a different "
    "construction, it is a separate claim. "
    "Work through the sections in the order given and record every claim in each before moving "
    "on. For each section return a count, and make that count the actual number of claims you "
    "recorded for it. A section with genuinely no participation claim gets zero, which is a "
    "valid answer. "
    "Worked examples used in figures and formal displays are participation claims and are "
    "commonly missed: if the manuscript analyses an expression in a structure, the permissions "
    "that analysis attributes to it are claims. "
    "Every claim needs an exact, nonempty substring of the manuscript in `quote`, including "
    "LaTeX markup, and the label of the section it came from. "
    "Assign evidence_type from the enum, describing the basis THE MANUSCRIPT gives. A CGEL "
    "citation is cgel_described, not a weakness. Use authors_analysis where the manuscript "
    "presents the point as its own proposal, and not_determinable where the basis is genuinely "
    "unclear. Do not edit the source. Do not produce Lean work."
)


def main():
    text = MS.read_text()
    digest = hashlib.sha256(text.encode()).hexdigest()

    marks = [(m.start(), m.group(2), m.group(3)) for m in SECTION.finditer(text)]
    sections = []
    for i, (pos, title, label) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        sections.append({"label": label, "title": title, "text": text[pos:end]})
    front = text[: marks[0][0]]
    if front.strip():
        sections.insert(0, {"label": "front-matter", "title": "Front matter (abstract etc.)",
                            "text": front})

    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "object",
        "additionalProperties": False,
        "required": ["claims", "section_counts", "responsibility_notice"],
        "properties": {
            "claims": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["id", "section_label", "expression", "construction",
                                 "status", "evidence_type", "quote"],
                    "properties": {
                        "id": {"type": "string"},
                        "section_label": {"type": "string"},
                        "expression": {"type": "string"},
                        "construction": {"type": "string"},
                        "status": {"type": "string",
                                   "enum": ["licensed", "excluded", "conditional", "not_stated"]},
                        "evidence_type": {"type": "string", "enum": EVIDENCE_TYPE},
                        "quote": {"type": "string", "minLength": 1},
                        "condition": {"type": "string"},
                        "note": {"type": "string"},
                    },
                },
            },
            "section_counts": {
                "type": "array",
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": ["section_label", "claims_recorded"],
                    "properties": {
                        "section_label": {"type": "string"},
                        "claims_recorded": {"type": "integer"},
                        "note": {"type": "string"},
                    },
                },
            },
            "responsibility_notice": {"type": "string"},
        },
    }

    task = {
        "objective": "Exhaustive census of participation claims in the manuscript.",
        "instructions": INSTRUCTIONS,
        "evidence_type_enum": EVIDENCE_TYPE,
        "section_inventory": [{"label": s["label"], "title": s["title"]} for s in sections],
        "sections": sections,
        "source_sha256": digest,
        "output_schema": schema,
    }

    UPLOAD.mkdir(parents=True, exist_ok=True)
    for name, blob in [("task.json", task), ("schema.json", schema)]:
        (UPLOAD / name).write_text(json.dumps(blob, indent=2, ensure_ascii=False) + "\n")
    (HERE / "schema.json").write_text(json.dumps(schema, indent=2) + "\n")
    (UPLOAD / "task.md").write_text(
        "# Exhaustive participation-claim census\n\n"
        "Follow task.json. The manuscript is supplied split into its sections. Record every "
        "participation claim in every section and return `census.json` matching schema.json, "
        "including a per-section count that matches the claims you recorded. There is no target "
        "number of claims. Do not replace the requested JSON with Lean work.\n")
    (HERE / "acceptance.json").write_text(json.dumps(ACCEPTANCE, indent=2) + "\n")

    print(json.dumps({"sections": len(sections), "source_sha256": digest[:16],
                      "chars": len(text), "acceptance_cases": len(ACCEPTANCE)}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
