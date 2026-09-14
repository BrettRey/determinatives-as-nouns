"""Freeze Opus's query inventory and expand only schema identifier enums."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def save(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


scope = json.loads((ROOT / "scope/result.json").read_text())
if scope["responsibility_notice"]:
    raise SystemExit(scope["responsibility_notice"])
for query in scope["queries"]:
    if query["id"] == "X098":
        before = copy.deepcopy(query)
        query["construction_id"] = "independent_argument"
        query["request"] = "Quantificational lot in an independent argument phrase with an of-PP whose complement is an undetermined nominal, as in a lot of delegates, compared with a lot of the delegates. The article belongs to the frame. Keep the undetermined-complement use distinct from the partitive comparison, and record the number-transparency property and the count and non-count agreement examples."
        save(ROOT / "scope-adjustments.json", [{"by": "parent", "query_id": "X098", "reason": "The defined independent_partitive construction should not presuppose that a lot of delegates with an undetermined complement is partitive. The main source contrasts this with a lot of the delegates. The general argument construction leaves that distinction available.", "before": before, "after": query}])
sources = json.loads((ROOT / "inputs/sources.json").read_text())
catalog = {c["id"]: c["description"] for c in scope["construction_catalog"]}
scope_checks = {s["id"]: s["question"] for s in scope["scope_checks"]}
assert len(catalog) == len(scope["construction_catalog"])
assert len(scope_checks) == len(scope["scope_checks"])
assert len(set(scope["lexeme_ids"])) == len(scope["lexeme_ids"])
assert len({q["id"] for q in scope["queries"]}) == len(scope["queries"])
assert all(q["lexeme_id"] in scope["lexeme_ids"] and q["construction_id"] in catalog for q in scope["queries"])
base_catalog = json.loads((ROOT / "inputs/base-catalog.json").read_text())
assert all(catalog[k] == v for k, v in base_catalog.items() if k in catalog)
base_schema = json.loads((ROOT / "inputs/base-schema.json").read_text())
schema = copy.deepcopy(base_schema)
properties = schema["properties"]
properties["lexemes"]["items"]["properties"]["id"]["enum"] = scope["lexeme_ids"]
properties["constructions"]["items"]["properties"]["id"]["enum"] = list(catalog)
claims = properties["participation_claims"]["items"]["properties"]
claims["id"]["enum"] = [q["id"] for q in scope["queries"]]
claims["lexeme_id"]["enum"] = scope["lexeme_ids"]
claims["construction_id"]["enum"] = list(catalog)
checks = properties["scope_checks"]["items"]["properties"]
checks["id"]["enum"] = list(scope_checks)
for branch in [claims, checks]:
    branch["evidence"]["items"]["properties"]["source_id"]["enum"] = [s["id"] for s in sources]


def without_id_enums(value):
    if isinstance(value, dict):
        return {k: without_id_enums(v) for k, v in value.items() if k != "enum"}
    if isinstance(value, list):
        return [without_id_enums(v) for v in value]
    return value


assert without_id_enums(schema) == without_id_enums(base_schema)
assert claims["status"] == base_schema["properties"]["participation_claims"]["items"]["properties"]["status"]
assert claims["conditions"] == base_schema["properties"]["participation_claims"]["items"]["properties"]["conditions"]
task = {
    "task": "Extract one lexeme record per supplied ID, the construction catalog verbatim, one participation claim per query, and every scope answer, using only the two complete source documents below. Preserve query context and all relevant source qualifications. This is an expanded extraction batch; it does not repeat or merge the original pilot. No new analysis, citations, outside facts, or Lean proof is requested.",
    "instructions": "Statuses concern the exact requested use under its stated conditions, not unconditional grammaticality. Preserve distinctions between described uses, constructed positive illustrations, selected attestations, restrictions, variation, and searches with no retained result. An S cell is not a ban; R/ hardly omissible must not become an absolute exclusion. If the fixed vocabulary cannot preserve a material source distinction, flag that query in exceptions.json rather than manufacturing a precise answer. not_stated records must have empty evidence and conditions; exceptions may preserve the source qualifications that cannot fit there. Keep lexemes distinct from phrases, and do not transfer permission between own_phrase, target_nominal, outer_np or different constructions. Evidence quotes must be exact, nonempty substrings of the cited full source, including LaTeX markup. Include relevant attestation and verification limits as concise construction qualifications. Do not treat the manuscript's citations as independently checked here, or silently import the claims of a historical/alternative analysis into the author's account. Do not edit source files. All record fields and status/bearer values are fixed; only ID inventories have expanded.",
    "lexeme_ids": scope["lexeme_ids"],
    "construction_catalog": catalog,
    "queries": scope["queries"],
    "scope_checks": scope_checks,
    "source_excerpts": sources,
    "output_schema": schema,
    "supervisor_coverage_notes": scope["coverage_notes"],
    "supervisor_scope_limitations": scope["omitted_or_ambiguous"],
}
save(ROOT / "inputs/task.json", task)
save(ROOT / "inputs/schema.json", schema)
save(ROOT / "queries.json", scope["queries"])
save(ROOT / "scope-checks.json", scope_checks)
upload = ROOT / "aristotle-inputs"
upload.mkdir(exist_ok=True)
save(upload / "task.json", task)
save(upload / "schema.json", schema)
(upload / "task.md").write_text("# Expanded source-to-JSON extraction\n\nFollow task.json using only the two complete source texts it supplies. Return records.json matching schema.json, and exceptions.json as an array of any unresolved items (each with query_id, reason, and source evidence); use [] when there are none. Preserve all IDs, exact source quotations, conditions, qualifications and scope distinctions. Do not replace the requested JSON with Lean work. You may write a concise extraction summary separately.\n")
print(json.dumps({"lexemes": len(scope["lexeme_ids"]), "queries": len(scope["queries"]), "constructions": len(catalog), "scope_checks": len(scope_checks), "schema_shape_unchanged": True}))
