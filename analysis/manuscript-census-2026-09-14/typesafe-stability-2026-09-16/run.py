#!/usr/bin/env python3
"""Stability check: the same 658 claims and construction catalogue under three phrasings of
the question. A is the full run's phrasing (rules block); B is a terse one-liner; C is a
procedural decision list. Only the construction question is asked. Responses cached per phrasing.
"""
import collections, concurrent.futures as cf, importlib.machinery, importlib.util, json, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
CEN = HERE.parent
ROOT = CEN.parents[1]
spec = importlib.util.spec_from_loader("tsq", importlib.machinery.SourceFileLoader("tsq", str(ROOT.parents[2] / "tools/typesafe/bin/tsq")))
tsq = importlib.util.module_from_spec(spec); spec.loader.exec_module(tsq)

PHRASINGS = {
    "B": "Which construction from the criteria does this sentence say the expression participates in? Choose the construction the sentence's claim concerns.",
    "C": {"question": "Identify the construction the manuscript's sentence attributes to the expression.",
          "how": ["First decide whether the sentence names any construction for the expression; if it only makes a category, taxonomy or method point, choose taxonomic_or_meta.",
                  "If the expression is described as subject, object, complement of a preposition, or in independent, pro-form or anaphoric use, choose independent_argument; with a partitive of-PP, independent_partitive.",
                  "If it precedes a separate nominal as Det, choose dependent_det; as an attributive modifier, dependent_internal_mod.",
                  "If the sentence is about a modifier attached inside the expression's own phrase (very few, the lucky few), choose internal_mod_admission; attached outside (almost every, only you), peripheral_mod_admission.",
                  "If the expression itself modifies an adjective, choose degree_modifier_adj; if it modifies anything else, degree_modifier_nonadj.",
                  "Otherwise choose the closest specific construction; use other only when none fits."]},
}


def main():
    norm = json.loads((CEN / "census-normalized.json").read_text())
    claims = norm["claims"]
    catalogue = {c["id"]: c["description"] for c in norm["catalogue"]}
    full = CEN / "typesafe-full-2026-09-16"
    keyed = CEN / "typesafe-keyed-2026-09-16"
    (HERE / "phrasings.json").write_text(json.dumps({"A": "see ../typesafe-keyed-2026-09-16/questions.json (construction)", **PHRASINGS}, indent=1) + "\n")

    def load_A(cid):
        for d in (full / "responses", keyed / "responses"):
            if (d / f"{cid}.json").exists():
                return json.loads((d / f"{cid}.json").read_text())["answers"]["construction"]

    usage = collections.Counter(); t0 = time.time()

    def run(tag):
        q = {"construction": {"type": "choice", "instructions": PHRASINGS[tag], "criteria": catalogue}}
        def one(c):
            out = HERE / f"responses-{tag}" / f"{c['id']}.json"
            if out.exists():
                return c["id"], json.loads(out.read_text()), True
            state = {"expression": c["expression"], "manuscript_construction_label": c["construction"], "sentence": c["quote"], "note": c.get("note"), "section": c["section_label"]}
            r = tsq.request({"state": state, "model": tsq.MODEL, "questions": q})
            out.write_text(json.dumps(r, indent=1, ensure_ascii=False) + "\n")
            return c["id"], r, False
        res = {}
        with cf.ThreadPoolExecutor(max_workers=8) as ex:
            for cid, r, cached in ex.map(one, claims):
                res[cid] = r["answers"]["construction"]
                if not cached: usage[tag] += r["usage"]["input_tokens"]
        return res

    A = {c["id"]: load_A(c["id"]) for c in claims}
    B, C = run("B"), run("C")
    elapsed = time.time() - t0

    rows, stats = [], collections.Counter()
    conf_diff = []; flip_accepted = 0; unstable_by_hk = collections.Counter(); hk_total = collections.Counter()
    maj_agree_hk = 0; A_agree_hk = 0; stable_agree_hk = [0, 0]
    for c in claims:
        a, b, cc = A[c["id"]], B[c["id"]], C[c["id"]]
        labels = [a["choice"], b["choice"], cc["choice"]]
        n_distinct = len(set(labels))
        kind = "stable" if n_distinct == 1 else "two_agree" if n_distinct == 2 else "all_differ"
        stats[kind] += 1
        hk = c["construction_id"]; hk_total[hk] += 1
        if kind != "stable": unstable_by_hk[hk] += 1
        maj = collections.Counter(labels).most_common(1)[0][0] if n_distinct < 3 else a["choice"]
        maj_agree_hk += maj == hk; A_agree_hk += a["choice"] == hk
        if kind == "stable":
            stable_agree_hk[0] += 1; stable_agree_hk[1] += a["choice"] == hk
        confs = [a["confidence"], b["confidence"], cc["confidence"]]
        conf_diff.append(max(confs) - min(confs))
        if a["confidence"] >= 0.8:
            stats["A_accepted"] += 1
            if kind != "stable": flip_accepted += 1
            if all(x >= 0.8 for x in confs): stats["accepted_under_all_three"] += 1
        rows.append({"id": c["id"], "haiku": hk, "A": [a["choice"], round(a["confidence"], 3)], "B": [b["choice"], round(b["confidence"], 3)],
                     "C": [cc["choice"], round(cc["confidence"], 3)], "kind": kind})
    stab_by_conf = collections.defaultdict(lambda: [0, 0])
    for r in rows:
        bkt = ">=0.8" if r["A"][1] >= 0.8 else "0.5-0.8" if r["A"][1] >= 0.5 else "<0.5"
        stab_by_conf[bkt][0] += 1; stab_by_conf[bkt][1] += r["kind"] == "stable"
    res = {"claims": len(claims), "usage_fresh_input_tokens": dict(usage), "elapsed_s": round(elapsed, 1),
           "label_stability": {k: stats[k] for k in ("stable", "two_agree", "all_differ")},
           "stability_by_A_confidence": {k: {"n": n, "stable": s} for k, (n, s) in sorted(stab_by_conf.items())},
           "A_accepted_at_0.8": stats["A_accepted"], "A_accepted_that_flip_under_B_or_C": flip_accepted,
           "accepted_under_all_three_phrasings": stats["accepted_under_all_three"],
           "agreement_with_haiku": {"A": A_agree_hk, "majority_of_three": maj_agree_hk, "stable_only": f"{stable_agree_hk[1]}/{stable_agree_hk[0]}"},
           "mean_confidence_range_across_phrasings": round(sum(conf_diff) / len(conf_diff), 3),
           "unstable_share_by_haiku_label": {k: f"{unstable_by_hk[k]}/{hk_total[k]}" for k, _ in hk_total.most_common(10)},
           "distribution": {t: collections.Counter(r[t][0] for r in rows).most_common(6) for t in ("A", "B", "C")}}
    (HERE / "results.json").write_text(json.dumps(res, indent=1) + "\n")
    (HERE / "per-claim.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n")
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
