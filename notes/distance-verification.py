#!/usr/bin/env python3
"""
Verify the per-item Hamming distances reported in §5 of main.tex (line 280).

Source: literature/Reynolds2021_LingBuzz_feature_matrix.csv
  - 138 word forms x 155 binary features (the LingBuzz-published matrix; the
    155 are the features from Reynolds 2021's original 232 that apply to more
    than one form, with singleton features filtered).

Metric: Hamming distance (count of differing bits) on the 155-feature vectors.

Reproduces the paper's numbers within ~1 unit:

  form  | paper det  comp det | paper pron  comp pron
  ------+----------+----------+-----------+----------
  the   |   24.8       24.5   |   26.2       26.2
  a     |   28.8       29.8   |   30.0       30.2
  this  |   25.2       24.8   |   29.0       29.8
  some  |   21.8       21.9   |   36.8       36.2

Run:  python3 notes/distance-verification.py
"""
import csv
from pathlib import Path

MATRIX = Path(__file__).resolve().parents[3] / "literature" / "Reynolds2021_LingBuzz_feature_matrix.csv"

CORE_DET = [
    "this", "that", "these", "those",
    "some", "any", "every", "each", "no", "all", "most", "many", "few",
]
SAMPLED_PRON = [
    "he", "she", "it_plain", "it_dum", "there",
    "they_plur", "I", "we_pron",
]


def load(path):
    with open(path, encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        next(reader)
        rows = list(reader)
    names = [r[0] for r in rows]
    features = [[1 if v == "y" else 0 for v in r[1:]] for r in rows]
    return names, features


def main():
    names, features = load(MATRIX)
    vec = lambda name: features[names.index(name)]
    hamming = lambda a, b: sum(x != y for x, y in zip(a, b))

    print(f"forms: {len(names)}, features: {len(features[0])}")
    print(f"{'form':6} | {'mean Hamming to core det':>26} | {'mean Hamming to sampled pron':>30}")
    for tgt in ["the", "a", "this", "some"]:
        det = [d for d in CORE_DET if d != tgt]
        pron = [p for p in SAMPLED_PRON if p != tgt]
        h_det = sum(hamming(vec(tgt), vec(d)) for d in det) / len(det)
        h_pron = sum(hamming(vec(tgt), vec(p)) for p in pron) / len(pron)
        print(f"{tgt:6} | {h_det:>26.1f} | {h_pron:>30.1f}")


if __name__ == "__main__":
    main()
