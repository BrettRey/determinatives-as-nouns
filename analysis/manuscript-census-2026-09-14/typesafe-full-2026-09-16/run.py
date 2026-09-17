#!/usr/bin/env python3
"""Full-census TypeSafe run with a 0.8 confidence threshold.

Every census claim gets the same two `choice` questions as the keyed test (questions.json
there). TypeSafe's construction label is accepted at confidence >= THRESHOLD and Haiku's
label (census-normalized.json) kept otherwise; the evidence-type answer is recorded but
never accepted, since the keyed test showed it weak. Writes census-typesafe.json (a derived
layer, one record per claim) and results.json. Responses cached in responses/; the keyed
run's responses are reused.
"""
import collections, concurrent.futures as cf, importlib.machinery, importlib.util, json, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
CEN = HERE.parent
KEYED = CEN / "typesafe-keyed-2026-09-16"
ROOT = CEN.parents[1]
THRESHOLD = 0.8
spec = importlib.util.spec_from_loader("tsq", importlib.machinery.SourceFileLoader("tsq", str(ROOT.parents[2] / "tools/typesafe/bin/tsq")))
tsq = importlib.util.module_from_spec(spec); spec.loader.exec_module(tsq)


def main():
    norm = json.loads((CEN / "census-normalized.json").read_text())
    questions = json.loads((KEYED / "questions.json").read_text())
    claims = norm["claims"]

    def one(c):
        cid = c["id"]
        for d in (HERE / "responses", KEYED / "responses"):
            if (d / f"{cid}.json").exists():
                return cid, json.loads((d / f"{cid}.json").read_text()), True
        state = {"expression": c["expression"], "manuscript_construction_label": c["construction"], "sentence": c["quote"],
                 "note": c.get("note"), "section": c["section_label"]}
        r = tsq.request({"state": state, "model": tsq.MODEL, "questions": questions})
        (HERE / "responses" / f"{cid}.json").write_text(json.dumps(r, indent=1, ensure_ascii=False) + "\n")
        return cid, r, False

    t0 = time.time(); usage = collections.Counter(); fresh = 0; ans = {}; model = None
    with cf.ThreadPoolExecutor(max_workers=8) as ex:
        for cid, r, cached in ex.map(one, claims):
            ans[cid] = r["answers"]; model = r.get("model", model)
            if not cached:
                fresh += 1; usage["input_tokens"] += r["usage"]["input_tokens"]; usage["output_tokens"] += r["usage"]["output_tokens"]

    out, stats = [], collections.Counter()
    agree_by_bucket = collections.defaultdict(lambda: [0, 0])
    taxo_resolved = []
    disagree_accepted = []
    for c in claims:
        a = ans[c["id"]]; con = a["construction"]; conf = con["confidence"]
        accepted = conf >= THRESHOLD
        hk = c["construction_id"]
        combined = con["choice"] if accepted else hk
        top3 = sorted(con["probabilities"].items(), key=lambda kv: -kv[1])[:3]
        rec = {"id": c["id"], "section_label": c["section_label"], "expression": c["expression"],
               "haiku_construction_id": hk, "typesafe_construction_id": con["choice"], "typesafe_confidence": round(conf, 3),
               "typesafe_top3": [[k, round(v, 3)] for k, v in top3], "accepted_at_0.8": accepted, "construction_id_combined": combined,
               "typesafe_evidence_type": a["evidence_type"]["choice"], "typesafe_evidence_confidence": round(a["evidence_type"]["confidence"], 3),
               "census_evidence_type": c["evidence_type"], "evidence_type_reconciled": c["evidence_type_reconciled"]}
        out.append(rec)
        b = "<0.5" if conf < 0.5 else "0.5-0.8" if conf < 0.8 else ">=0.8"
        agree_by_bucket[b][0] += 1; agree_by_bucket[b][1] += con["choice"] == hk
        stats["accepted"] += accepted
        if accepted:
            stats["accepted_agree_haiku"] += con["choice"] == hk
            if con["choice"] != hk:
                disagree_accepted.append((c["id"], hk, con["choice"], round(conf, 2), c["construction"][:60]))
        if hk == "taxonomic_or_meta" and accepted and con["choice"] != "taxonomic_or_meta":
            taxo_resolved.append((c["id"], con["choice"], round(conf, 2), c["construction"][:60]))
        stats["ts_evidence_agree_census"] += a["evidence_type"]["choice"] == c["evidence_type"]
        stats["ts_evidence_agree_reconciled"] += a["evidence_type"]["choice"] == c["evidence_type_reconciled"]

    res = {"model": model, "threshold": THRESHOLD, "claims": len(claims), "fresh_requests": fresh, "usage_fresh": dict(usage),
           "elapsed_s": round(time.time() - t0, 1),
           "accepted": stats["accepted"], "accepted_agree_haiku": stats["accepted_agree_haiku"],
           "agreement_with_haiku_by_confidence": {b: {"n": n, "agree": k} for b, (n, k) in sorted(agree_by_bucket.items())},
           "haiku_taxonomic_given_confident_specific_label": len(taxo_resolved),
           "combined_distribution": collections.Counter(r["construction_id_combined"] for r in out).most_common(),
           "typesafe_distribution": collections.Counter(r["typesafe_construction_id"] for r in out).most_common(),
           "evidence_type": {"ts_agree_census": stats["ts_evidence_agree_census"], "ts_agree_reconciled": stats["ts_evidence_agree_reconciled"],
                             "ts_distribution": collections.Counter(r["typesafe_evidence_type"] for r in out).most_common()},
           "accepted_disagreements_with_haiku": disagree_accepted, "taxonomic_resolved": taxo_resolved}
    (HERE / "census-typesafe.json").write_text(json.dumps({"derived_from": "census-normalized.json + TypeSafe responses", "threshold": THRESHOLD, "claims": out}, indent=1, ensure_ascii=False) + "\n")
    (HERE / "results.json").write_text(json.dumps(res, indent=1, ensure_ascii=False) + "\n")
    for k in ("model", "claims", "fresh_requests", "usage_fresh", "elapsed_s", "accepted", "accepted_agree_haiku", "agreement_with_haiku_by_confidence",
              "haiku_taxonomic_given_confident_specific_label", "evidence_type"):
        print(k, "=", json.dumps(res[k]))
    print("typesafe dist:", res["typesafe_distribution"])
    print("combined dist:", res["combined_distribution"])
    print("\naccepted disagreements with Haiku (first 30):")
    for d in disagree_accepted[:30]: print("  ", d)
    print("\nHaiku-taxonomic resolved by confident TypeSafe label (first 25):")
    for d in taxo_resolved[:25]: print("  ", d)


if __name__ == "__main__":
    main()
