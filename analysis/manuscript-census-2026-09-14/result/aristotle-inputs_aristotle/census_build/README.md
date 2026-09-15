# How `census.json` was produced

`census.json` (in the project root) is the deliverable: an exhaustive census of the
participation claims made by the manuscript supplied, section by section, in `task.json`.

## Method

1. Every section in `task.json` was read in the order given by `section_inventory`.
2. Each assertion that a specific expression **does** occur, **does not** occur, or occurs
   **only under stated conditions** in a specific syntactic function or construction was
   recorded as one claim. Worked examples, syntactic trees, and the formal displays and
   comparison tables were treated as claim sources on the same footing as running prose.
3. Individuation follows the instructions in `task.json`: a distinct expression or a
   distinct construction yields a distinct claim, so one sentence or one table row can
   yield several entries. Pure restatements of a claim already recorded in the same
   section (same expression, same construction) were not duplicated.
4. `evidence_type` records the basis **the manuscript** gives:
   - `cgel_described` / `cgel_restricted` — cited to *CGEL*, as a description or a restriction;
   - `constructed_illustration` / `constructed_ungrammatical` — the manuscript's own
     constructed examples, the latter marked with `\ungram`;
   - `retained_attestation` — an attested example the manuscript preserves;
   - `searched_not_found` — a search reported as returning no qualifying result;
   - `authors_analysis` — presented as the manuscript's own proposal or commitment;
   - `not_determinable` — the basis is a third-party account or otherwise unclear.
5. Two sections record zero claims (`sec:proposal`, `sec:economy`); each carries a note in
   `section_counts` explaining why. Zero is a substantive finding, not an omission.

## Reproducing and checking

```
python3 census_build/build_census.py
```

The builder assembles `census_build/parts/part1.py` … `part11.py` and **fails** unless, for
every claim: the `section_label` exists, the `quote` is an exact substring of that section's
text in `task.json` (LaTeX markup included), `status` and `evidence_type` are in the schema's
enumerations, and the `id` is unique. Per-section counts are computed from the recorded
claims, so they cannot drift from the claim list. The output also validates against
`schema.json` under JSON Schema 2020-12.

No source text was edited.
