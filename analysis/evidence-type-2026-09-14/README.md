# Required evidence_type re-extraction — 14 September 2026

**Result: the extraction assigned `evidence_type` to all 110 claims and reproduced all 54 withheld values correctly.** Every `basis_quote` is an exact substring of its cited source. See [assignments.json](assignments.json), [validation.json](validation.json) and [manifest.json](manifest.json).

The accepted claim set from [the expanded run](../expanded-json-2026-09-14) was reused rather than re-derived. A fresh extraction would have risked regressing the seven corrections that run's supervision loop settled, and its `records.json` is hash-pinned in a provenance bundle. Only the missing field was requested. That bundle was not modified; the manifest records its hash.

The 54 supplement claims state their evidential basis inside their own conditions. Those 50 condition strings were stripped before submission, so the extraction had to recover G/R/I/S and the attestation references from the supplement text like any other claim. Their declared values were withheld and held as a key.

| Check | Result |
|---|---:|
| Assignments returned, all query IDs present exactly once | 110/110 |
| `basis_quote` an exact substring of the cited source | 110/110 |
| Held-out key reproduced | 54/54 |
| Extraction disagreements with a declared value | 0 |
| Returned responsibility notice | empty |

Sources were the stored, hash-verified texts from the original run, not the live files: `quantifier-controls.tex` has since been refactored so its table body sits in `analysis/generated/quant-table.tex`.

## What the field shows

Within the 54 supplement claims, which enumerate one table cell by cell, 22 rest on a retained attestation and 32 do not. That proportion is meaningful because the frame is complete.

The 56 manuscript claims are a convenience sample of the manuscript's 658 participation claims (see [the census](../manuscript-census-2026-09-14)), drawn against a quota rather than a frame. Their evidence_type values are individually sound, but no proportion over them estimates anything about the paper. An earlier version of this file reported such proportions, including a list of constructions said to have no attested claim; those are withdrawn.

## Limits

The 56 manuscript assignments have no key, so their accuracy is inferred from the 54 rather than measured. The extraction was offered `not_determinable` and never used it across 110 claims; the held-out result is good evidence against confabulation, but never abstaining is worth noting rather than reading as confidence. A single label is also forced onto evidence that is sometimes mixed: X061 assigns `constructed_ungrammatical` to *so numerous mistakes* while its own note records that the contrast carries a *CGEL* citation.

`authors_analysis` is a category added for this run, not drawn from the supplement's vocabulary. It marks claims the manuscript itself attributes to its proposed analysis rather than to a source, and the manuscript states this directly ("Determinative modifier attachments are analytical commitments").

This run assigns an evidential label to existing claims. It does not verify the underlying linguistic judgments, and it adds no new evidence to the paper.
