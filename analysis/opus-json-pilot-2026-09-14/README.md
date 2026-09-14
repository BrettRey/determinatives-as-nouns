# Opus JSON extraction pilot — 14 September 2026

**Result: Opus passed the full, bounded extraction pilot.** The output is suitable as a checked draft of records for the supplied cases.

The run used `claude-opus-5` through Claude Code 2.1.270, requested with `--model opus --effort xhigh`. It completed in **110.09 seconds**. No process timeout was added. The original full Qwen pilot's system prompt, source excerpts, schema, 20 queries, and assessment criteria were reused unchanged. Expected answers and previous responses were not supplied to Opus. Tools, MCP access, and project customizations were disabled; the CLI's structured-output mechanism was enabled.

| Check | Result |
| --- | --- |
| JSON schema and record links | Passed |
| Lexeme/form groups | 7/7 correct for the pilot inventory |
| Construction catalog | All five supplied definitions preserved |
| Licensed/excluded/not-stated statuses | 20/20 matched the pre-existing answers |
| Evidence quotations | All 65 were exact substrings of their cited excerpts |
| Critical content checks | All ten passed on manual inspection |
| Phrase-scope questions | Both answered correctly |

The output preserves dependent target selection versus the independent head's own properties; conditions within the determining/modifying phrase versus those on the larger NP; the no/none and my/mine paradigms; and possessor person versus independent NP agreement. It retains selected partitives and relatives, restricts definite determination and adjective premodification appropriately, and leaves the unsupported degree-modifier use of some unknown.

This is a guided extraction test, not autonomous schema design, exhaustive lexeme discovery, or independent grammatical verification. The input fixed identifiers and construction definitions. Query context remains part of each record's interpretation: for example, P17 excludes bare singular count book as an ordinary subject, not every independent NP headed by book. Conditions are still partly prose. The result supports using Opus to prepare draft records with checking; it does not establish unattended reliability across the inventory.

The output has not been repaired or edited. The manuscript remains unchanged. There was one Opus run. Qwen's earlier 20-case attempt timed out, so it has no accuracy score on the full set; its completed smaller attempt used different inputs and settings.

## Files

- [Extracted records](records.json).
- [Mechanical validation](validation.json) and [manual assessment](assessment.json).
- [Prompt](prompt.json), [system instructions](system-prompt.txt), [schema](schema.json), [source excerpts](sources.json), [queries](queries.json), and [pre-existing assessment criteria](expected.json).
- [Raw response](raw-response.json), [run metadata](manifest.json), and [runner](run.py).

The CLI usage metadata records the substantive Opus 5 response and an additional 19 output tokens under Haiku 4.5. That ancillary usage is preserved in the raw response; no separate Haiku extraction was requested. Reported list-price-equivalent cost was approximately $0.385, not a statement about subscription billing.
