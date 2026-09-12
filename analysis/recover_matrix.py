#!/usr/bin/env python3
"""Recover the 232-feature working matrix and audit its published reduction.

The working CSV has an extraneous first row and empty trailing columns. The
second row contains the actual header. This script extracts that rectangular
block without inferring or repairing feature values. It does not establish
that this working file was the input to the published 2021 analysis.
"""
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
OUT = ROOT / "results"


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.reader(stream))


def write_csv(path, rows):
    with path.open("w", encoding="utf-8", newline="") as stream:
        csv.writer(stream, lineterminator="\n").writerows(rows)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    OUT.mkdir(exist_ok=True)
    raw_path = DATA / "wordlist-first-cut-source.csv"
    public_path = DATA / "matrix155-lingbuzz.csv"
    raw = read_csv(raw_path)
    public = read_csv(public_path)
    assert len(raw) == 140 and all(len(row) == 463 for row in raw)
    assert raw[1][0] == "names" and raw[1][233] == "Category"
    assert all(not any(row[234:]) for row in raw[1:])
    recovered = [row[:233] for row in raw[1:]]
    assert len(recovered) == len(public) == 139
    assert len(recovered[0]) == 233 and len(public[0]) == 156
    assert len(set(recovered[0])) == 233
    assert len(set(public[0])) == 156
    for matrix in (recovered, public):
        assert len({row[0] for row in matrix[1:]}) == 138
        assert all(value in ("y", "n") for row in matrix[1:] for value in row[1:])
    categories = [row[233] for row in raw[2:]]
    assert categories == ["determinative"] * 73 + ["pronoun"] * 65
    aliases = {"somewhat_424": "somewhat", "such_435": "such"}
    assert [aliases.get(r[0], r[0]) for r in recovered[1:]] == [r[0] for r in public[1:]]
    shared = public[0][1:]
    assert set(shared) <= set(recovered[0][1:])
    removed = [f for f in recovered[0][1:] if f not in shared]
    changes = [["word", "feature", "working232", "public155"]]
    for old, new in zip(recovered[1:], public[1:]):
        for feature in shared:
            a, b = old[recovered[0].index(feature)], new[public[0].index(feature)]
            if a != b:
                changes.append([new[0], feature, a, b])
    removed_counts = [["feature", "positive_word_forms"]]
    for feature in removed:
        index = recovered[0].index(feature)
        removed_counts.append([feature, sum(row[index] == "y" for row in recovered[1:])])
    recovered_path = DATA / "matrix232-recovered.csv"
    write_csv(recovered_path, recovered)
    write_csv(DATA / "word-mapping.csv", [["working_name", "public_name", "category"]] + [
        [old[0], new[0], category]
        for old, new, category in zip(recovered[1:], public[1:], categories)
    ])
    write_csv(OUT / "removed-features.csv", removed_counts)
    write_csv(OUT / "coding-changes.csv", changes)
    # The archived manuscript's selected comparison groups, retained solely
    # to audit its numerical claims. These are not a prototype measure.
    core = "this that these those some any every each no all most many few".split()
    pron = "he she it_plain it_dum there they_plur I we_pron".split()
    vectors = {row[0]: row[1:] for row in public[1:]}
    hamming = lambda a, b: sum(x != y for x, y in zip(vectors[a], vectors[b]))
    distance_rows = [["form", "comparison", "n", "sum_hamming", "mean_hamming"]]
    for word in ("the", "a", "this", "some"):
        for name, group in (("selected_determinatives", core), ("selected_pronouns", pron)):
            others = [other for other in group if other != word]
            total = sum(hamming(word, other) for other in others)
            distance_rows.append([word, name, len(others), total, total / len(others)])
    write_csv(OUT / "legacy-distance-audit.csv", distance_rows)
    report = {
        "source_sha256": digest(raw_path),
        "public_sha256": digest(public_path),
        "recovered_sha256": digest(recovered_path),
        "word_forms": 138,
        "working_features": 232,
        "public_features": 155,
        "removed_features": len(removed),
        "removed_all_zero": sum(row[1] == 0 for row in removed_counts[1:]),
        "removed_singletons": sum(row[1] == 1 for row in removed_counts[1:]),
        "shared_feature_cell_changes": len(changes) - 1,
        "name_changes": aliases,
        "retained_singletons": [
            f for j, f in enumerate(public[0][1:], 1)
            if sum(row[j] == "y" for row in public[1:]) == 1
        ],
        "provenance_limit": "Recovered working matrix; not authenticated as the published analysis input.",
    }
    (OUT / "matrix-lineage.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
