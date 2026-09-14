# Qwen JSON extraction pilot — 14 September 2026

**Result: the tested setup is not ready for unattended population of the lexeme/construction records.** It produced valid JSON but failed to extract elementary facts explicitly present in the supplied excerpts.

## What ran

One initial request to the installed `qwen3.8:27b` (Q4_K_M, Ollama 0.32.12) covered seven lexemes and 20 participation queries. It used an enforced JSON schema, temperature 0, thinking disabled, and a 16,384-token context. The non-streaming request hit its 600-second client timeout without returning a result. Its accuracy is therefore unassessed, not zero.

One smaller recovery request covered three lexemes and four participation claims, using four source excerpts, a simpler enforced schema, streaming, and an 8,192-token context. Temperature remained 0 and thinking remained disabled. It completed in 76.16 seconds, with first output at 23.67 seconds and 233 output tokens. No further runs or repairs were made.

## Observed results

| Check | Result |
| --- | --- |
| JSON/schema validity | Passed |
| Actual word forms | 0/3 lexeme entries correct; it returned use labels such as `dependent` and `independent` as forms |
| Participation status | 1/4 correct; all four were marked `not_stated` |
| Dependent *few* | Missed explicitly supplied target and dependent restrictions |
| Independent *few* | Missed explicitly supplied number/count properties and permitted dependents |
| Independent *mine* | Missed the explicit possessor/agreement distinction |
| *Some* as degree modifier of an adjective | Correctly left unknown; this was the one case absent from the supplied excerpts |
| Source links | None returned, including for the three supported cases |

The one correct unknown is not strong evidence of calibrated abstention, because the response abstained on every case. It supplied no usable linguistic conditions.

The records are retained as failed draft output. They have not been corrected, accepted into a database, or used to change the manuscript. This test supports withholding unattended extraction with this configuration. It does not establish that Qwen could not do better with different prompting, thinking enabled, or another runtime configuration; those were not tested.

## Files

- [Reduced output](small-records.json), [assessment](assessment.json), and [raw response with timing](small-response.json).
- [Reduced request](small-request.json) and [runner](small-run.py).
- [Source excerpts and manuscript hash](sources.json).
- Original [request](request.json), [schema](schema.json), [queries](queries.json), [assessment criteria](expected.json), [runner](run.py), and [timeout record](attempt-1-failure.json).

Identifiers, construction definitions, and query cases were supplied by the pilot. This tested constrained extraction, not autonomous schema design or exhaustive discovery. Sources are manuscript excerpts; their underlying linguistic claims were not independently reverified in this pilot. The manuscript source hash is unchanged.
