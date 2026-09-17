# Full-census TypeSafe run, 0.8 threshold — 16 September 2026

<!-- SUMMARY: all 658 census claims through TypeSafe jev-1.13.0; construction accepted at confidence >= 0.8 (253 claims, 233 agreeing with Haiku); exposed and retired the residue rule · status: complete · updated: 2026-09-16 -->

**Result: at confidence 0.8 and above TypeSafe's construction label agrees with the Haiku layer on 233 of 253 accepted claims, and its confident disagreements caught a defect in my own labelling.** Same two questions per claim as [the keyed test](../typesafe-keyed-2026-09-16/); `run.py` reuses those 124 responses and bought 534 more (1,024,500 input tokens, 25.9 seconds for the whole census). Per-claim output is in [census-typesafe.json](census-typesafe.json): Haiku's id, TypeSafe's id with confidence and top-three probabilities, the accepted-or-kept decision, and a `construction_id_combined` that takes TypeSafe's label when accepted and Haiku's otherwise. Scoring is in [results.json](results.json).

| Confidence | n | TypeSafe agrees with Haiku |
|---|---:|---:|
| below 0.5 | 151 | 68 |
| 0.5 to 0.8 | 254 | 177 |
| 0.8 and above (accepted) | 253 | 233 |

## What the run changed

The 23 claims my regex residue rule had pulled out of `taxonomic_or_meta` on the strength of a word in the census's free-text label (`Det function in CGEL` became `dependent_det`, and so on) were contradicted by TypeSafe on every one, 13 of them at 0.8 or above, while the model refinement pass agreed with TypeSafe on 122 of its 172 reassignments with only 3 confident disagreements. The rule was mine and had no key, so it is removed from `normalize.py`; those claims revert to `taxonomic_or_meta`, which is now 139 of 658, and the cross-tab and worklist are regenerated. The keyed-set figures are unchanged (51 of 55), since the rule never touched a keyed claim.

## What it does not do

TypeSafe is the more conservative labeller: it calls 198 claims taxonomic against Haiku's 139, and only 2 of Haiku's 139 receive a confident specific label from it, so it does not resolve the residue. The 20 confident disagreements that remain after the fix are listed in `results.json` under `accepted_disagreements_with_haiku`; on inspection they are mostly two defensible readings of one sentence (fused-head AdjP arguments as `fused_head` or `independent_argument`; postmodifiers of compounds as `compound_base` or `internal_mod_admission`), which is a review list, not a defect list. The evidence-type answers are recorded and never accepted; on the whole census they match the census label on 401 of 658, with `not_determinable` used 75 times.

The Haiku layer in `census-normalized.json` remains the labelling of record. The combined column is there for anyone who wants the accepted TypeSafe labels instead.
