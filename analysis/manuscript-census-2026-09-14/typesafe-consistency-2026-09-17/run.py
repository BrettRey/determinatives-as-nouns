#!/usr/bin/env python3
"""Internal-consistency screen over the census: every pair of claims that share a lexeme,
asked whether they make incompatible claims, with a relation label. Candidates above the
floor are for a human reading. Responses cached per pair."""
import collections, concurrent.futures as cf, importlib.machinery, importlib.util, itertools, json, time
from pathlib import Path

HERE = Path(__file__).resolve().parent; CEN = HERE.parent; ROOT = CEN.parents[1]
spec = importlib.util.spec_from_loader("tsq", importlib.machinery.SourceFileLoader("tsq", str(ROOT.parents[2] / "tools/typesafe/bin/tsq")))
tsq = importlib.util.module_from_spec(spec); spec.loader.exec_module(tsq)
norm = json.loads((CEN / "census-normalized.json").read_text())
lex = {l["id"]: l["forms"][0] for l in norm["lexemes"]}
claims = [c for c in norm["claims"] if c["lexeme_ids"]]
by_lex = collections.defaultdict(list)
for c in claims:
    for i in c["lexeme_ids"]: by_lex[i].append(c)
pairs = {}
for i, cs in by_lex.items():
    for a, b in itertools.combinations(cs, 2):
        pairs[(a["id"], b["id"])] = i
print("lexeme groups", len(by_lex), "pairs", len(pairs))
Q = {"incompatible": {"type": "noul", "instructions": "Do sentence A and sentence B make incompatible claims about English: does one assert, for the same expression in the same construction or use, what the other denies (licensed versus excluded, permitted versus not permitted, singular versus plural, and so on)?",
                      "criteria": {"true": "the two sentences cannot both be true of the same expression in the same construction", "false": "they are compatible: the same claim restated, claims about different constructions or uses, one a qualified version of the other, or unrelated"}},
     "relation": {"type": "choice", "instructions": "What is the relation between the two claims?",
                  "criteria": {"contradiction": "one asserts what the other denies about the same expression and construction", "qualification": "one is a hedged, restricted, or conditional version of the other (e.g. one says excluded, the other says rare or restricted)", "restatement": "the same claim in different words", "different_constructions": "compatible claims about different constructions or uses of the expression", "unrelated": "no substantive overlap"}}}
def state(c): return {"expression": c["expression"], "construction": c["construction"], "status": c["status"], "section": c["section_label"], "sentence": c["quote"]}
byid = {c["id"]: c for c in claims}
def one(key):
    a, b = key; out = HERE / "responses" / f"{a}__{b}.json"
    if out.exists(): return key, json.loads(out.read_text()), True
    r = tsq.request({"state": {"lexeme": lex[pairs[key]], "A": state(byid[a]), "B": state(byid[b])}, "model": tsq.MODEL, "questions": Q})
    out.write_text(json.dumps(r) + "\n"); return key, r, False
t0 = time.time(); usage = 0; fresh = 0; rows = []
with cf.ThreadPoolExecutor(max_workers=8) as ex:
    for key, r, cached in ex.map(one, sorted(pairs)):
        if not cached: fresh += 1; usage += r["usage"]["input_tokens"]
        ans = r["answers"]; rows.append({"a": key[0], "b": key[1], "lexeme": lex[pairs[key]], "p_incompatible": round(ans["incompatible"]["noul"], 2), "relation": ans["relation"]["choice"], "relation_confidence": round(ans["relation"]["confidence"], 2)})
rows.sort(key=lambda x: -x["p_incompatible"])
res = {"pairs": len(rows), "fresh": fresh, "input_tokens_fresh": usage, "elapsed_s": round(time.time() - t0, 1),
       "p_incompatible_bins": collections.Counter("<0.2" if x["p_incompatible"] < 0.2 else "0.2-0.5" if x["p_incompatible"] < 0.5 else "0.5-0.8" if x["p_incompatible"] < 0.8 else ">=0.8" for x in rows),
       "relation": collections.Counter(x["relation"] for x in rows), "candidates_ge_0.5": sum(x["p_incompatible"] >= 0.5 for x in rows)}
(HERE / "pairs.json").write_text(json.dumps(rows, indent=0) + "\n"); (HERE / "results.json").write_text(json.dumps(res, indent=1) + "\n")
print(json.dumps(res, indent=1))
