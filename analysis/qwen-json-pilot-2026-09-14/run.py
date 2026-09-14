"""Run one local extraction request and check its structure and evidence links."""
import hashlib
import json
import time
import urllib.request
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parent


def read(name):
    return json.loads((ROOT / name).read_text())


def write(name, value):
    (ROOT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


if (ROOT / "response.json").exists():
    raise SystemExit("Response already exists; this pilot does not rerun automatically.")

request = read("request.json")
started = time.monotonic()
print("Sending one request to local qwen3.8:27b", flush=True)
http_request = urllib.request.Request(
    "http://localhost:11434/api/chat",
    data=json.dumps(request).encode(),
    headers={"Content-Type": "application/json"},
)
with urllib.request.urlopen(http_request, timeout=600) as response:
    result = json.load(response)
write("response.json", result)
elapsed = time.monotonic() - started
records = json.loads(result["message"]["content"])
write("records.json", records)
errors = [e.message for e in jsonschema.Draft202012Validator(read("schema.json")).iter_errors(records)]

queries = {q["id"]: q for q in read("queries.json")}
sources = {s["id"]: s["text"] for s in read("sources.json")["excerpts"]}
claims = records.get("participation_claims", [])
ids = [c["id"] for c in claims]
if len(ids) != len(set(ids)) or set(ids) != set(queries):
    errors.append("Participation IDs are duplicated, missing, or unexpected.")
lexemes = {x["id"]: x["forms"] for x in records.get("lexemes", [])}
expected_lexemes = set(q["lexeme_id"] for q in queries.values())
if set(lexemes) != expected_lexemes or len(lexemes) != len(records.get("lexemes", [])):
    errors.append("Lexeme IDs are duplicated, missing, or unexpected.")
expected_constructions = set(q["construction_id"] for q in queries.values())
construction_ids = [x["id"] for x in records.get("constructions", [])]
if set(construction_ids) != expected_constructions or len(construction_ids) != len(set(construction_ids)):
    errors.append("Construction IDs are duplicated, missing, or unexpected.")
for claim in claims:
    query = queries.get(claim["id"])
    if query and any(claim[k] != query[k] for k in ("form", "lexeme_id", "construction_id")):
        errors.append(f"{claim['id']}: changed query identity")
    if claim["form"] not in lexemes.get(claim["lexeme_id"], []):
        errors.append(f"{claim['id']}: form missing from linked lexeme")
    if claim["status"] != "not_stated" and not claim["evidence"]:
        errors.append(f"{claim['id']}: no evidence")
    if claim["status"] == "not_stated" and (claim["conditions"] or claim["evidence"]):
        errors.append(f"{claim['id']}: unsupported details in not_stated record")
scope_ids = [x["id"] for x in records.get("scope_checks", [])]
if sorted(scope_ids) != ["the_apple", "the_few_people"]:
    errors.append("Scope check IDs are duplicated, missing, or unexpected.")
evidence_count = 0
for item in claims + records.get("scope_checks", []):
    for evidence in item["evidence"]:
        evidence_count += 1
        quote = evidence["quote"]
        if not quote or quote not in sources.get(evidence["source_id"], ""):
            errors.append(f"{item['id']}: evidence quote is not an exact source substring")
paper = ROOT.parent.parent / "determinatives-as-nouns.tex"
source_unchanged = hashlib.sha256(paper.read_bytes()).hexdigest() == read("sources.json")["source_sha256"]
if not source_unchanged:
    errors.append("Manuscript source changed since preparation.")
validation = {
    "elapsed_seconds": round(elapsed, 2),
    "done_reason": result.get("done_reason"),
    "prompt_tokens": result.get("prompt_eval_count"),
    "output_tokens": result.get("eval_count"),
    "claims": len(claims),
    "evidence_quotes_checked": evidence_count,
    "source_unchanged": source_unchanged,
    "errors": errors,
    "note": "Mechanical checks only; linguistic assessment is separate.",
}
write("validation.json", validation)
print(json.dumps(validation, indent=2), flush=True)
