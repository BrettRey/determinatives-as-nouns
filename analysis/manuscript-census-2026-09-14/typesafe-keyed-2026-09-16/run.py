#!/usr/bin/env python3
"""Keyed test of TypeSafe (System One, jev) on census construction and evidence labelling.

Scope: the census claims that pair with the expanded run's 56 keyed manuscript claims
(normalize-key-check.json), so TypeSafe, Haiku (census-normalized.json) and the key are
compared on the same items. One request per claim: a `choice` over the 22-id construction
catalogue and a `choice` over the evidence_type enum. Responses cached in responses/.
"""
import collections, concurrent.futures as cf, importlib.machinery, importlib.util, json, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
CEN = HERE.parent
ROOT = CEN.parents[1]
tsq_spec = importlib.util.spec_from_loader("tsq", importlib.machinery.SourceFileLoader("tsq", str(ROOT.parents[2] / "tools/typesafe/bin/tsq")))
tsq = importlib.util.module_from_spec(tsq_spec); tsq_spec.loader.exec_module(tsq)
norm_spec = importlib.util.spec_from_file_location("normalize", CEN / "normalize.py")
normalize = importlib.util.module_from_spec(norm_spec); norm_spec.loader.exec_module(normalize)

EVIDENCE = {
    "cgel_described": "the sentence reports a description or analysis from CGEL (Huddleston & Pullum 2002), usually with a citation",
    "cgel_restricted": "the sentence reports a restriction or exclusion stated in CGEL",
    "other_source_described": "the sentence reports a description from a source other than CGEL (Payne, Hudson, Spinillo, Lyons, Sommerstein, Palmer, Reynolds' earlier papers)",
    "constructed_illustration": "the basis is a constructed example presented as possible or well formed",
    "constructed_ungrammatical": "the basis is a constructed example marked ungrammatical or excluded",
    "retained_attestation": "the basis is an attested corpus or web example, usually with a footnoted source",
    "searched_not_found": "the sentence reports a search that returned no qualifying attestation",
    "authors_analysis": "the sentence states the manuscript's own analysis or proposal, not a source or an example",
    "not_determinable": "the basis cannot be determined from the sentence",
}


def main():
    norm = json.loads((CEN / "census-normalized.json").read_text())
    kc = json.loads((CEN / "normalize-key-check.json").read_text())
    claims = {c["id"]: c for c in norm["claims"]}
    ids = sorted({p["census"] for p in kc["pairs"]})
    catalogue = {c["id"]: c["description"] for c in norm["catalogue"]}
    questions = {
        "construction": {"type": "choice",
                         "instructions": {"task": "Assign this claim about an English expression to one construction id from the criteria.",
                                          "rules": normalize.RULES},
                         "criteria": catalogue},
        "evidence_type": {"type": "choice",
                          "instructions": "What basis does the manuscript sentence give for this claim? Classify the stated grounds, not their strength.",
                          "criteria": EVIDENCE},
    }
    (HERE / "questions.json").write_text(json.dumps(questions, indent=1, ensure_ascii=False) + "\n")

    def one(cid):
        out = HERE / "responses" / f"{cid}.json"
        if out.exists():
            return cid, json.loads(out.read_text()), True
        c = claims[cid]
        state = {"expression": c["expression"], "manuscript_construction_label": c["construction"], "sentence": c["quote"],
                 "note": c.get("note"), "section": c["section_label"]}
        r = tsq.request({"state": state, "model": tsq.MODEL, "questions": questions})
        out.write_text(json.dumps(r, indent=1, ensure_ascii=False) + "\n")
        return cid, r, False

    t0 = time.time(); usage = collections.Counter(); fresh = 0; answers = {}
    with cf.ThreadPoolExecutor(max_workers=4) as ex:
        for cid, r, cached in ex.map(one, ids):
            answers[cid] = r["answers"]
            if not cached:
                fresh += 1; usage["input_tokens"] += r["usage"]["input_tokens"]; usage["output_tokens"] += r["usage"]["output_tokens"]
    elapsed = time.time() - t0

    # scoring against the keyed claims, alongside Haiku (census-normalized) on the same pairs
    pair = collections.Counter(); per = collections.defaultdict(lambda: collections.defaultdict(bool))
    conf_rows = []
    for p in kc["pairs"]:
        a = answers[p["census"]]
        ts_c, ts_e = a["construction"]["choice"], a["evidence_type"]["choice"]
        hk_c, hk_e = p["construction"][1], p["evidence_type"][1]
        ky_c, ky_e = p["construction"][0], p["evidence_type"][0]
        for name, val in (("ts_construction", ts_c == ky_c), ("haiku_construction", hk_c == ky_c),
                          ("ts_evidence", ts_e == ky_e), ("census_evidence", hk_e == ky_e), ("ts_vs_haiku_construction", ts_c == hk_c)):
            pair[name, val] += 1; per[p["keyed"]][name] |= val
        conf_rows.append((a["construction"]["confidence"], ts_c == ky_c, ts_c == hk_c))
    pairwise = {k: f"{pair[k, True]}/{pair[k, True] + pair[k, False]}" for k in ("ts_construction", "haiku_construction", "ts_evidence", "census_evidence", "ts_vs_haiku_construction")}
    anymatch = {k: f"{sum(d[k] for d in per.values())}/{len(per)}" for k in ("ts_construction", "haiku_construction", "ts_evidence", "census_evidence")}
    # confidence buckets: does higher confidence mean more agreement with the key and with Haiku?
    buckets = collections.defaultdict(lambda: [0, 0, 0])
    for conf, ok_key, ok_hk in conf_rows:
        b = "<0.5" if conf < 0.5 else "0.5-0.8" if conf < 0.8 else ">=0.8"
        buckets[b][0] += 1; buckets[b][1] += ok_key; buckets[b][2] += ok_hk
    calib = {b: {"n": n, "agree_key": k, "agree_haiku": h} for b, (n, k, h) in sorted(buckets.items())}
    # whole-set distribution of TypeSafe construction ids vs Haiku on these claims
    dist_ts = collections.Counter(answers[i]["construction"]["choice"] for i in ids)
    dist_hk = collections.Counter(claims[i]["construction_id"] for i in ids)
    res = {"model": next(iter(json.loads((HERE / "responses" / f"{ids[0]}.json").read_text()).get("model", "") for _ in [0])),
           "claims_tested": len(ids), "fresh_requests": fresh, "usage_fresh": dict(usage), "elapsed_s": round(elapsed, 1),
           "pairings": len(kc["pairs"]), "keyed_claims": len(per),
           "pairwise_agreement": pairwise, "per_keyed_claim_any_match": anymatch, "construction_confidence_buckets": calib,
           "construction_distribution": {"typesafe": dist_ts.most_common(), "haiku": dist_hk.most_common()},
           "mean_construction_confidence": round(sum(c for c, _, _ in conf_rows) / len(conf_rows), 3)}
    (HERE / "results.json").write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps(res, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
