#!/usr/bin/env python3
"""Independently recompute numerical quantities from saved assignments.

Uses NumPy, not the R clustering/scoring implementations. No fitting, selection
or mutation of the historical data. Writes a verification record and a plain
text summary of the complete exploratory surface.
"""
from pathlib import Path
from collections import Counter, defaultdict
import csv
import hashlib
import json
import math
import sys
import numpy as np

ROOT = Path(__file__).resolve().parent
OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "results"


def read(name):
    with (OUT / name).open(newline="") as f:
        return list(csv.DictReader(f))


def number(row, name):
    return float(row[name])


def same(actual, expected, label, tol=2e-9):
    if not np.allclose(actual, expected, atol=tol, rtol=tol):
        raise AssertionError(f"{label}: max difference {np.max(np.abs(actual-expected))}")


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


with (ROOT / "../data/matrix155-lingbuzz.csv").open(encoding="utf-8-sig", newline="") as f:
    original = list(csv.reader(f))
feature_names = original[0][1:]
items = [r[0] for r in original[1:]]
X = np.array([[int(v == "y") for v in r[1:]] for r in original[1:]], dtype=np.int64)
assert X.shape == (138, 155)
reference = np.array([1] * 73 + [2] * 65)
feature_index = {f: j for j, f in enumerate(feature_names)}
blocks = [r["block"] for r in read("feature-inventory.csv")]
for entry in json.loads((ROOT / "input-manifest.json").read_text()):
    assert sha(ROOT / entry["local_path"]) == entry["sha256"]
    assert sha(entry["source_path"]) == entry["sha256"]
protected = json.loads((ROOT / "protected-files-before.json").read_text())
for name, checksum in protected.items():
    assert sha(name) == checksum, f"Pre-existing file changed: {name}"


def adjusted_rand(a, b):
    cells = Counter(zip(a, b))
    a_sizes = Counter(a)
    b_sizes = Counter(b)
    choose2 = lambda n: n * (n - 1) / 2
    index = sum(choose2(n) for n in cells.values())
    sa = sum(choose2(n) for n in a_sizes.values())
    sb = sum(choose2(n) for n in b_sizes.values())
    expected = sa * sb / choose2(len(a))
    denom = (sa + sb) / 2 - expected
    if abs(denom) < 1e-14:
        return float(np.array_equal(a[:, None] == a[None, :], b[:, None] == b[None, :]))
    return (index - expected) / denom


def silhouette(cl, distance):
    values = []
    for i in range(len(cl)):
        own = (cl == cl[i])
        own[i] = False
        if own.sum() == 0:
            values.append(0.0)
            continue
        a = distance[i, own].mean()
        b = min(distance[i, cl == g].mean() for g in set(cl) if g != cl[i])
        values.append((b - a) / max(a, b) if max(a, b) > 0 else 0.0)
    return float(np.mean(values))


assignments = defaultdict(list)
for row in read("assignments.csv"):
    assignments[row["spec_id"]].append(row)
specs = read("specifications.csv")
assert len(specs) == len(set(r["spec_id"] for r in specs))
weights = defaultdict(list)
for row in read("feature-weights.csv"):
    weights[row["geometry_id"]].append(row)
feature_sets = defaultdict(list)
for row in read("feature-sets.csv"):
    feature_sets[row["feature_set"]].append(row["feature"])
distances = {}
partitions = {}
for row in specs:
    spec_id = row["spec_id"]
    a = assignments[spec_id]
    assert [r["word"] for r in a] == items
    cl = np.array([int(r["cluster"]) for r in a])
    assert set(cl) == {1, 2}
    partitions[spec_id] = cl
    matched = int((cl == reference).sum())
    assert matched == int(row["matched"]) and matched >= 69
    assert (matched == 69) == (row["orientation_tied"] == "TRUE")
    same(adjusted_rand(cl, reference), number(row, "ari"), f"ARI {spec_id}")
    same(np.mean([np.mean(cl[reference == g] == g) for g in (1, 2)]),
         number(row, "balanced_accuracy"), f"balanced accuracy {spec_id}")
    assert (cl == 1).sum() == int(row["size_1"])
    assert (cl == 2).sum() == int(row["size_2"])
    assert row["converged"] == "TRUE"
    geometry_id = "__".join(spec_id.split("__")[:-1])
    if geometry_id not in distances:
        wr = weights[geometry_id]
        names = [r["feature"] for r in wr]
        assert names == feature_sets[row["feature_set"]]
        assert len(names) == int(row["features"])
        cols = [feature_index[f] for f in names]
        z = X[:, cols]
        w = np.array([float(r["weight"]) for r in wr])
        mode = row["weighting"]
        if mode == "equal_features":
            expected_w = np.ones(len(cols))
        elif mode == "equal_domains":
            counts = Counter(blocks[c] for c in cols)
            expected_w = np.array([1 / counts[blocks[c]] for c in cols])
        elif mode == "unique_profiles":
            keys = [tuple(z[:, j]) for j in range(z.shape[1])]
            counts = Counter(keys)
            expected_w = np.array([1 / counts[k] for k in keys])
        elif mode == "idf_presence":
            expected_w = np.log(len(items) / np.maximum(1, z.sum(axis=0)))
        else:
            raise AssertionError(mode)
        same(w, expected_w / expected_w.sum(), f"weights {geometry_id}")
        # Direct pairwise mismatches, independently of R's intersection formula.
        mismatch = np.sum(np.abs(z[:, None, :] - z[None, :, :]) * w, axis=2)
        if row["distance"] == "sqrt_hamming":
            distance = np.sqrt(mismatch)
        elif row["distance"] == "hamming":
            distance = mismatch
        elif row["distance"] == "jaccard":
            union = np.sum(np.maximum(z[:, None, :], z[None, :, :]) * w, axis=2)
            distance = np.divide(mismatch, union, out=np.zeros_like(mismatch), where=union > 0)
        else:
            raise AssertionError(row["distance"])
        distances[geometry_id] = distance
    distance = distances[geometry_id]
    same(silhouette(cl, distance), number(row, "silhouette"), f"silhouette {spec_id}")
    if row["method"] == "energy":
        objective = sum(distance[np.ix_(cl == g, cl == g)].sum() / (2 * (cl == g).sum())
                        for g in (1, 2))
        same(objective, number(row, "objective"), f"energy objective {spec_id}")
    elif row["method"] == "pam":
        # The medoid minimizes total distance within its assigned cluster.
        objective = sum(distance[np.ix_(cl == g, cl == g)].sum(axis=0).min()
                        for g in (1, 2)) / len(cl)
        same(objective, number(row, "objective"), f"PAM objective {spec_id}")

starts = defaultdict(list)
for row in read("energy-starts.csv"):
    starts[row["fit_id"]].append(row)
for fit_id, rows in starts.items():
    assert [int(r["seed"]) for r in rows] == list(range(1, 101))
    chosen = [r for r in rows if r["selected"] == "TRUE"]
    assert len(chosen) == 1
    same(float(chosen[0]["objective"]), min(float(r["objective"]) for r in rows), fit_id)
    assert int(chosen[0]["iterations"]) < 100 or int(chosen[0]["last_moves"]) == 0

for method in ("pam", "average", "energy"):
    selected = [r for r in specs if r["scope"] == "core" and r["method"] == method]
    co = np.mean([partitions[r["spec_id"]][:, None] == partitions[r["spec_id"]][None, :]
                  for r in selected], axis=0)
    saved = read(f"coassignment-core-{method}.csv")
    assert [r["word"] for r in saved] == items
    same(co, np.array([[float(r[item]) for item in items] for r in saved]), f"{method} coassignment")
    same(np.diag(co), np.ones(len(items)), f"{method} coassignment diagonal")
    valid = [r for r in selected if r["orientation_tied"] == "FALSE"]
    labels = np.stack([partitions[r["spec_id"]] for r in valid], axis=1)
    membership = read(f"membership-core-{method}.csv")
    assert [r["word"] for r in membership] == items
    for i, r in enumerate(membership):
        assert int(r["specifications"]) == len(valid)
        assert int(r["determinative_aligned_count"]) == (labels[i] == 1).sum()
        assert int(r["pronoun_aligned_count"]) == (labels[i] == 2).sum()
        assert int(r["agreement_count"]) == (labels[i] == reference[i]).sum()

# Check the legacy control against both direct distances and the existing audit.
legacy = read("legacy-control.csv")[0]
legacy_a = read("legacy-control-assignments.csv")
lc = np.array([int(r["cluster"]) for r in legacy_a])
assert [r["word"] for r in legacy_a] == items
ld = np.sqrt(np.abs(X[:, None, :] - X[None, :, :]).sum(axis=2))
lw = sum(ld[np.ix_(lc == g, lc == g)].sum() / (2 * (lc == g).sum()) for g in (1, 2))
same(lw, float(legacy["objective"]), "legacy energy objective")
assert int((lc == reference).sum()) == int(legacy["matched"])
with (ROOT / "../results/kgroups-summary.csv").open(newline="") as f:
    historical_audit = next(r for r in csv.DictReader(f) if r["variant"] == "public155")
same(lw, float(historical_audit["objective"]), "existing audit objective")
assert int(legacy["matched"]) == int(historical_audit["best_of_100_matched"])

# Recompute all held-domain predictions directly, excluding target rows by index.
folds = defaultdict(list)
for row in read("prediction-folds.csv"):
    folds[row["fold_id"]].append(row)
prediction_a = defaultdict(list)
for row in read("prediction-assignments.csv"):
    prediction_a[row["prediction_id"]].append(row)
by_feature = defaultdict(list)
for row in read("prediction-by-feature.csv"):
    by_feature[row["prediction_id"]].append(row)
by_item = defaultdict(list)
for row in read("prediction-by-item.csv"):
    by_item[row["prediction_id"]].append(row)
predictions = read("held-domain-prediction.csv")


def direct_predictions(y, cl):
    p = np.empty_like(y, dtype=float)
    for i in range(len(cl)):
        others = [j for j in range(len(cl)) if cl[j] == cl[i] and j != i]
        p[i] = (y[others].sum(axis=0) + 1) / (len(others) + 2)
    return p


for row in predictions:
    pred_id = row["prediction_id"]
    fold_id = row["held_domain"] + "__" + row["coding"]
    schema = folds[fold_id]
    target = [feature_index[r["feature"]] for r in schema if r["role"] == "target"]
    train = [feature_index[r["feature"]] for r in schema if r["role"] == "train"]
    assert set(target).isdisjoint(train)
    assert all(blocks[t] == row["held_domain"] for t in target)
    assert all(blocks[t] != row["held_domain"] for t in train)
    assert len(target) == int(row["held_features"])
    assert len(train) == int(row["training_features"])
    target_profiles = {tuple(X[:, j]) for j in target} | {tuple(1 - X[:, j]) for j in target}
    assert not any(tuple(X[:, j]) in target_profiles for j in train)
    a = prediction_a[pred_id]
    assert [r["word"] for r in a] == items
    cl = np.array([int(r["cluster"]) for r in a])
    y = X[:, target]
    models = {"cluster": cl, "baseline": np.ones(len(items), dtype=int), "reference": reference}
    losses = {}
    for model, labels in models.items():
        p = direct_predictions(y, labels)
        ell = np.where(y == 1, -np.log(p), -np.log1p(-p))
        losses[model] = ell
        same(ell.mean(), float(row[model + "_logloss"]), f"{pred_id} {model} logloss")
        same(np.mean((y - p) ** 2), float(row[model + "_brier"]), f"{pred_id} {model} Brier")
    same((losses["baseline"] - losses["cluster"]).mean(), float(row["gain_over_baseline"]), pred_id)
    same((losses["reference"] - losses["cluster"]).mean(), float(row["gain_over_reference"]), pred_id)
    assert row["converged"] == "TRUE"
    fs = by_feature[pred_id]
    ws = by_item[pred_id]
    assert [r["feature"] for r in fs] == [feature_names[j] for j in target]
    assert [r["word"] for r in ws] == items
    for model, ell in losses.items():
        same(ell.mean(axis=0), np.array([float(r[model + "_logloss"]) for r in fs]), pred_id)
        same(ell.mean(axis=1), np.array([float(r[model + "_logloss"]) for r in ws]), pred_id)

verification = {
    "status": "passed",
    "numpy_version": np.__version__,
    "two_group_specifications": len(specs),
    "core_specifications": sum(r["scope"] == "core" for r in specs),
    "domain_transfer_fits": len(predictions),
    "distance_matrices_independently_reconstructed": len(distances),
    "energy_fits_with_100_starts": len(starts),
    "protected_preexisting_files_unchanged": len(protected),
    "legacy_control_matched": int(legacy["matched"]),
    "checks": [
        "source hashes, fixed inventory and feature/weight alignment",
        "reference agreement, adjusted Rand index, balanced accuracy",
        "direct pairwise distances, energy and PAM objectives, silhouette",
        "energy objective-based start selection and selected-fit convergence",
        "all core coassignment cells and per-form membership counts",
        "legacy result against the pre-existing audit",
        "domain disjointness and exact duplicate/complement leakage exclusions",
        "all domain-transfer log losses, Brier scores, per-feature and per-item losses",
    ],
}
(OUT / "verification.json").write_text(json.dumps(verification, indent=2) + "\n")


def span(rows, col, fmt=".3f"):
    vals = [float(r[col]) for r in rows]
    return f"{min(vals):{fmt}}–{max(vals):{fmt}}"


lines = [
    "EXPLORATORY MULTIVERSE — RESULTS",
    "",
    "The reciprocals project already contained a 40-row specification curve on",
    "the same matrix. It targets each_other and one_another; 20 of those rows",
    "are distinct geometric specifications. This run extends the comparison",
    "to the partition of all 138 forms.",
    "",
    f"New run: {len(specs)} two-group specifications",
    f"  core representations: {verification['core_specifications']}",
    f"  single-domain diagnostics: {len(specs)-verification['core_specifications']}",
    f"  withheld-domain transfer fits: {len(predictions)}",
    f"  aliased weighting/distance choices omitted: {len(read('equivalent-choices.csv'))}",
    "",
    "CORE REFERENCE AGREEMENT",
    "Agreement orients cluster labels after fitting; chance-adjusted pair",
    "agreement is reported as ARI. The input inventory remains 73 D / 65 pronoun.",
]
for method in ("pam", "average", "energy"):
    rr = [r for r in specs if r["scope"] == "core" and r["method"] == method]
    lines.append(f"  {method:8s} n={len(rr):3d}: matched {span(rr,'matched','.0f')}/138; "
                 f"ARI {span(rr,'ari')}")
lines += ["", "BREAKDOWN BY FEATURE SET AND METHOD",
          "feature set                         method    n   agreement/138   ARI"]
for fs in feature_sets:
    for method in ("pam", "average", "energy"):
        rr = [r for r in specs if r["feature_set"] == fs and r["method"] == method]
        lines.append(f"{fs:35s} {method:8s} {len(rr):2d}   "
                     f"{span(rr,'matched','.0f'):>9s}       {span(rr,'ari')}")

spec_by_id = {r["spec_id"]: r for r in specs}
aliases = {(r["feature_set"], r["weight"], r["distance"]): r["canonical_weight"]
           for r in read("equivalent-choices.csv")}


def resolve(fs, weight, distance, method):
    weight = aliases.get((fs, weight, distance), weight)
    return spec_by_id.get("__".join((fs, weight, distance, method)))


paired = []
seen_pairs = set()


def add_pair(comparison, before, after):
    if before is None or after is None:
        return
    key = (comparison, before["spec_id"], after["spec_id"])
    if key in seen_pairs:
        return
    seen_pairs.add(key)
    a = partitions[before["spec_id"]]
    b = partitions[after["spec_id"]]
    paired.append({
        "comparison": comparison, "before_spec": before["spec_id"], "after_spec": after["spec_id"],
        "method_before": before["method"], "method_after": after["method"],
        "matched_before": int(before["matched"]), "matched_after": int(after["matched"]),
        "change_in_matched": int(after["matched"]) - int(before["matched"]),
        "ari_before": float(before["ari"]), "ari_after": float(after["ari"]),
        "change_in_ari": float(after["ari"]) - float(before["ari"]),
        "between_partition_ari": adjusted_rand(a, b),
        "minimum_changed_forms": int(min((a != b).sum(), (a == b).sum())),
    })


for before_set, after_set in [
    ("full", "no_components"), ("full", "no_four_labels"),
    ("no_components", "no_components_or_four_labels"),
    ("full", "no_morph"), ("full", "no_phon"), ("full", "no_sem"), ("full", "no_synt"),
    ("synt_only", "synt_without_four_labels"),
]:
    for weight in ("equal_features", "equal_domains", "unique_profiles", "idf_presence"):
        for distance in (("jaccard",) if weight == "idf_presence" else
                         ("sqrt_hamming", "hamming", "jaccard")):
            for method in (("pam", "average", "energy") if distance == "sqrt_hamming" else
                           ("pam", "average")):
                add_pair(before_set + "_to_" + after_set,
                         resolve(before_set, weight, distance, method),
                         resolve(after_set, weight, distance, method))

for row in specs:
    if row["scope"] != "core":
        continue
    fs, weight, distance, method = (row[c] for c in ("feature_set", "weighting", "distance", "method"))
    if weight == "equal_features":
        add_pair("equal_features_to_equal_domains", row, resolve(fs, "equal_domains", distance, method))
        add_pair("equal_features_to_unique_profiles", row, resolve(fs, "unique_profiles", distance, method))
        if distance == "jaccard":
            add_pair("jaccard_equal_to_idf", row, resolve(fs, "idf_presence", distance, method))
    if distance == "sqrt_hamming" and method != "energy":
        add_pair("sqrt_hamming_to_hamming", row, resolve(fs, weight, "hamming", method))
        add_pair("sqrt_hamming_to_jaccard", row, resolve(fs, weight, "jaccard", method))
    if method == "pam":
        add_pair("pam_to_average", row, resolve(fs, weight, distance, "average"))
        if distance == "sqrt_hamming":
            add_pair("pam_to_energy", row, resolve(fs, weight, distance, "energy"))

with (OUT / "paired-comparisons.csv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(paired[0]))
    writer.writeheader()
    writer.writerows(paired)
lines += ["", "MATCHED COMPARISONS",
          "Each pair changes the named choice, with the others held fixed.",
          "Equivalent choices are resolved to their saved canonical result.",
          "Positive change means greater agreement with the historical labels;",
          "it doesn't establish that the changed analysis is preferable.",
          "comparison                                        pairs  change in matched forms"]
for comparison in dict.fromkeys(r["comparison"] for r in paired):
    rr = [r for r in paired if r["comparison"] == comparison]
    lines.append(f"{comparison:50s} {len(rr):3d}          {span(rr,'change_in_matched','.0f')}")

lines += ["", "MEMBERSHIP SENSITIVITY IN CORE REPRESENTATIONS",
          "Counts use the post-fit orientation toward the historical labels.",
          "They are counts over this analysis menu, not category probabilities."]
focus = ["each_other", "one_another", "the", "a", "this", "that", "these", "those",
         "my", "his", "her_dep", "its", "it_dum", "there", "something", "someone"]
for method in ("pam", "average", "energy"):
    rr = read(f"membership-core-{method}.csv")
    by_word = {r["word"]: r for r in rr}
    mixed = [r for r in rr if 0 < int(r["determinative_aligned_count"]) < int(r["specifications"])]
    same_all = [r for r in rr if int(r["agreement_count"]) == int(r["specifications"])]
    opposite_all = [r for r in rr if int(r["agreement_count"]) == 0]
    lines += [f"  {method}: {len(mixed)} forms switch alignment; "
              f"{len(same_all)} always match; {len(opposite_all)} always differ.",
              "    Always differ: " + (", ".join(r["word"] for r in opposite_all) or "none")]
    for word in focus:
        r = by_word[word]
        lines.append(f"    {word:16s} D-aligned {r['determinative_aligned_count']}/"
                     f"{r['specifications']}; pronoun-aligned {r['pronoun_aligned_count']}/"
                     f"{r['specifications']}")

ks = read("k-sensitivity.csv")
k_groups = defaultdict(list)
for row in ks:
    if row["scope"] == "core":
        k_groups[row["spec_id"]].append(row)
lines += ["", "SILHOUETTE MAXIMA OVER K=2…8",
          "Ties choose the smaller k. This is an internal geometry diagnostic;",
          "it does not estimate a grammatical taxonomy or validate a category count."]
for method in ("pam", "average"):
    wins = Counter()
    for rr in k_groups.values():
        if rr[0]["method"] == method:
            winner = max(rr, key=lambda r: (float(r["silhouette"]), -int(r["k"])))
            wins[int(winner["k"])] += 1
    lines.append(f"  {method}: " + ", ".join(f"k={k}: {n}" for k, n in sorted(wins.items())))

lines += ["", "WITHHELD-DOMAIN TRANSFER",
          "Positive gain = lower average log loss than an ungrouped prevalence",
          "baseline. Each target form is excluded from estimation of its own",
          "held-out probabilities. Counts are descriptive specification counts.",
          "domain   coding             n    positive/baseline  gain range (nats/cell)"]
for domain in ("morph", "phon", "sem", "synt"):
    for coding in ("all_features", "omit_four_labels"):
        rr = [r for r in predictions if r["held_domain"] == domain and r["coding"] == coding]
        positive = sum(float(r["gain_over_baseline"]) > 0 for r in rr)
        lines.append(f"{domain:8s} {coding:18s} {len(rr):3d}       "
                     f"{positive:2d}/{len(rr):2d}             {span(rr,'gain_over_baseline','.4f')}")
        baseline = float(rr[0]["baseline_logloss"])
        cgel = float(rr[0]["reference_logloss"])
        lines.append(f"  Historical-label gain over baseline: {baseline-cgel:.4f} nats/cell. "
                     f"Learned gain over historical labels: {span(rr,'gain_over_reference','.4f')}.")

lines += ["", "VERIFICATION AND SCOPE",
          f"Independent numerical verification passed; {len(protected)} pre-existing files unchanged.",
          f"The historical coordinate-based control reproduces {legacy['matched']}/138 agreement.",
          "The new energy fits use a different, explicitly recorded start schedule.",
          "All learned groupings are fitted without using the historical class labels.",
          "The classes are used only for evaluation and the separate prediction comparator.",
          "Transfer remains within this hand-coded inventory, with related forms present.",
          "Independent recodings, a checked family map, and common/proper-noun comparators",
          "would require additional evidence. No paper text or publication action is included.",
          "",
          "FILES",
          "PROTOCOL.txt: choices, mathematical definitions, provenance and limits",
          "specifications.csv / assignments.csv: complete two-group results",
          "paired-comparisons.csv: matched changes of feature set, weights, distance or method",
          "coassignment-core-*.csv / membership-core-*.csv: stability by method",
          "k-sensitivity.csv: complete silhouette curves",
          "held-domain-prediction.csv: transfer scores and comparator scores",
          "prediction-by-feature.csv / prediction-by-item.csv: individual contributions",
          "energy-starts.csv: optimization audit",
          "verification.json: independently recomputed checks",
          ""]
(OUT / "RESULTS.txt").write_text("\n".join(lines))
print(json.dumps(verification, indent=2))
print("\n".join(lines[:24]))
