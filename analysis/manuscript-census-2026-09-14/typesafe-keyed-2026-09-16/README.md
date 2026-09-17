# Keyed TypeSafe test on census labelling — 16 September 2026

<!-- SUMMARY: TypeSafe (jev-1.13.0) one-shot construction and evidence labelling on the 124 census claims that pair with the keyed set, scored beside Haiku and the census · status: complete · updated: 2026-09-16 -->

**Result: on construction ids TypeSafe is close behind Haiku's three-pass labelling; on evidence type it is well behind the census; its confidence is informative.** One request per claim through `tsq`, two `choice` questions each (the 22-id construction catalogue and the nine-value evidence enum, with the same rules text the Haiku run used). All 124 requests ran in 12.7 seconds. Responses are in `responses/`, the questions in `questions.json`, the scoring in `results.json`.

| Measure (55 keyed claims that pair; 156 pairings) | TypeSafe | Haiku (3 passes + rules) | Census (Aristotle) |
|---|---:|---:|---:|
| Keyed construction id reproduced on at least one paired claim | 43/55 | 51/55 | |
| Pairwise construction agreement with the key | 76/156 | 86/156 | |
| Keyed evidence type reproduced on at least one paired claim | 29/55 | | 46/55 |
| Pairwise evidence agreement with the key | 42/156 | | 86/156 |
| TypeSafe and Haiku give the same construction id | 120/156 | | |

| Construction confidence | n | agrees with key | agrees with Haiku |
|---|---:|---:|---:|
| below 0.5 | 34 | 9 | 16 |
| 0.5 to 0.8 | 53 | 29 | 39 |
| 0.8 and above | 69 | 38 | 65 |

Tokens: 238,067 in, 45,080 out for 124 claims. Pricing is on input only and cheap (Brett, 2026-09-16), so the whole 658-claim census would be about 1.3M input tokens. Mean construction confidence 0.71.

## Reading it

The comparison is not even-handed. Haiku had a first pass, a second pass over its taxonomic residue, and a rule over the census's free-text label; TypeSafe had one shot with the catalogue descriptions as criteria. Per keyed claim it still lands eight short of Haiku on constructions, and it agrees with Haiku on 120 of 156 pairings, so the two are labelling the same way most of the time.

Evidence type is the weak spot: 29 of 55 against the census's 46, and the census labels were themselves unkeyed. A one-sentence state with nine abstract rubric lines is probably too little for that judgment; the Aristotle census read whole sections.

The confidence signal is the useful finding. Agreement with Haiku rises from 16 of 34 below 0.5 to 65 of 69 at 0.8 and above, so a threshold near 0.8 would accept roughly half the claims with Haiku-level reliability and route the rest elsewhere. Agreement with the key rises less steeply because the key measure is noisy: a keyed claim spans several sentences and its paired census claims often concern other constructions.

## What it licenses

Use TypeSafe where a fast, cheap first pass with an abstention signal is wanted, accepting above a confidence threshold measured on the task and sending the rest to a stronger model; do not use it alone for evidence-type labelling in this form. This was one task with 124 items; it is a profile, not a verdict, and the vendor's calibration claim is tested here only against other models' labels, not against ground truth.
