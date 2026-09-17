# TypeSafe stability under three phrasings — 16 September 2026

<!-- SUMMARY: same 658 claims and catalogue, three phrasings of the construction question; 412 labels stable, confidence predicts stability, the taxonomic escape is the phrasing-sensitive boundary · status: complete · updated: 2026-09-16 -->

**Result: where TypeSafe is confident it is also stable, and the instability it does show sits almost entirely on the `taxonomic_or_meta` boundary.** Phrasing A is the full run's question with its rules block; B is a terse one-liner with no rules; C is a procedural decision list that opens with the taxonomic test ([phrasings.json](phrasings.json)). Same criteria, same state, one construction question. B and C cost 1.67M input tokens and 65 seconds for all 1,316 requests. Per-claim labels and confidences are in [per-claim.json](per-claim.json), scoring in [results.json](results.json).

| Label agreement across A, B, C | claims |
|---|---:|
| all three the same | 412 |
| two the same | 201 |
| all different | 45 |

| A's confidence | n | stable under all three |
|---|---:|---:|
| below 0.5 | 151 | 41 |
| 0.5 to 0.8 | 254 | 146 |
| 0.8 and above | 253 | 225 |

Of the 253 claims the full run accepted at 0.8, 28 change label under B or C, and 165 are at 0.8 or above under all three phrasings. The stable 412 agree with the Haiku layer on 347; the majority vote over three phrasings agrees on 469, no better than A alone at 478. The confidence value itself is not stable: its range across the three phrasings averages 0.22 per claim.

## Where it moves

The taxonomic escape is phrasing-driven. A calls 198 claims taxonomic, B (no rules) 124, C (taxonomic test first) 222; B sends the difference mostly to `fused_head` (79 against 56) and `external_determination` (30 against 17). By Haiku's label, the unstable claims concentrate in `internal_mod_admission` (41 of 63), `independent_argument` (68 of 135) and `peripheral_mod_admission` (18 of 33), while `number_agreement` (0 of 13), `dependent_det` (14 of 62) and `degree_modifier_adj` (5 of 22) hold. The instability is in the same place both models struggle: whether a sentence asserts participation in a construction or makes a point about the analysis.

## What it licenses

If TypeSafe labels are used, the safe acceptance set is confidence 0.8 or above under more than one phrasing (165 claims here), not one phrasing's threshold. A single confidence figure should be read as a stability signal, not a calibrated probability: it moves by a fifth with a rewording. The Haiku layer in `census-normalized.json` remains the labelling of record, and nothing here changes it.

## Calibration curve

[calibration.pdf](calibration.pdf) (`calibration_plot.py`; the binned numbers are in `calibration-bins.json`) plots phrasing A's confidence in equal-count bins against three observed rates with Wilson intervals. Against the Haiku layer the curve sits above the diagonal below 0.7 (agreement 0.58 at mean confidence 0.45) and on it from about 0.75 up (0.83, 0.91, 0.83, 0.92, 1.00 across the top five bins), so relative to that reference the score is under-confident at the low end and roughly calibrated at the top. Stability across phrasings runs below the diagonal until about 0.75 (0.18 at 0.34, 0.26 at 0.51) and then tracks agreement, so a low score means a label that will move under rewording more than it means disagreement with Haiku. Against the keyed set the curve is flat and wide (0.42 to 0.65 across the top three bins, intervals spanning 0.3), which is the pairing measure's ceiling rather than the model's: a keyed claim aggregates sentences that concern different constructions. None of the three references is ground truth. The house chart-style audit was not run; this is an analysis figure, not a paper figure.
