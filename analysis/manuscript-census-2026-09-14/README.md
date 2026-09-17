# Manuscript participation-claim census — 14 September 2026

**658 participation claims across all 28 sections.** This replaces the 56-claim convenience sample in [the expanded run](../expanded-json-2026-09-14) as the frame for anything counted about the manuscript. That sample was 8.5% of the population and was not drawn randomly.

| Check | Result |
|---|---:|
| Claims recorded | 658 |
| `quote` an exact substring of the manuscript | 658/658 |
| Sections reported / sections in the manuscript | 28/28 |
| Declared per-section counts matching claims recorded | 28/28 |
| Held-out acceptance cases reached | 10/10 |

The ten acceptance cases (*the lucky few*, *the very few*, *almost every experienced teacher*, *poor old me*, *Kim's preferences*, *the Smiths*, *only you*, *the idle rich*, *the few people*, *so many mistakes*) were withheld from the task. They exist because the previous sample missed *the lucky few* entirely, despite its being the worked example of Figure 6. All ten are now reached. Two sections, `sec:proposal` and `sec:economy`, are recorded as zero with a stated reason; both are short framing passages.

Aristotle completed in 24m 28s. The terminal status `COMPLETE_WITH_ERRORS` reflects the absence of Lake targets, which the task explicitly requested; no Lean work was asked for or produced.

## What is validated, and what is not

**The enumeration is validated.** Exact quotes, complete section coverage, self-consistent counts, all acceptance cases reached. It is usable as a frame and as an index into the manuscript.

**The `evidence_type` labels are not validated.** Unlike the [evidence-type run](../evidence-type-2026-09-14), which reproduced 54 withheld declared values exactly, this census has no key. A hand audit of 20 claims drawn with a fixed seed, each read in full manuscript context, found 17 defensible, 1 questionable and 2 exposing a schema defect ([audit](audit-2026-09-14.json)).

**The schema defect was mine, and is now repaired.** The enum shipped to this run had no value for "described by a source other than *CGEL*", so claims reporting Payne, Hudson, Spinillo, Sommerstein, Lyons, Palmer or Reynolds' own earlier papers fell to `not_determinable`, conflating "the basis is unclear" with "the basis is a third party". [`repartition.py`](repartition.py) adds `other_source_described` and reclassifies on a stated rule: a `not_determinable` claim whose surrounding context carries a real citation command becomes `other_source_described`, or `cgel_described` where only *CGEL* is cited. 42 of the 45 moved; 3 stayed (`pay-019`, `pay-020`, `his-011`), which are the same three a hand check had identified as genuinely lacking a source. Output is [census-repartitioned.json](census-repartitioned.json) with a [log](repartition-log.json); the returned `census.json` is left untouched.

## What this does not license

The label distribution is reported in [validation.json](validation.json) and should not be read as a verdict on the manuscript. In particular `authors_analysis` is the largest category, which is what a paper proposing a new categorization is expected to look like: stating its own analysis is the work, not a deficiency. Distinguishing an analytical proposal from a descriptive assertion that wants a source is a judgement the census makes possible and does not itself make.

The census records what the manuscript asserts and the basis it gives. It does not assess whether any claim is correct, and it adds no evidence to the paper.

## Normalized layer — 16 September 2026

**The census is now queryable.** [`normalize.py`](normalize.py) (`make census`) writes [census-normalized.json](census-normalized.json), a derived layer over the untouched census, giving every claim a controlled `construction_id`, `lexeme_ids` with a `subcategory`, the mechanical `basis_signals` at its sentence, and an `evidence_type_reconciled`. [`analysis/tools/census_tables.py`](../tools/census_tables.py) derives [the cross-tab](../generated/census-crosstab.md) (construction by subcategory, construction by basis) and [the corpus worklist](../generated/census-worklist.md) from it.

Before this, `construction` and `expression` were free text: 507 distinct construction strings and 378 distinct expressions over 658 claims, so nothing could be cross-tabulated. The catalogue is the expanded run's 11 construction ids plus eleven added here (genitive, agreement, number and grade inflection, predeterminer, coordination marker, compound base, fused head, external determination, taxonomic/meta, other); the lexeme table is the enriched run's 34 entries plus 62 new ones. Genitive forms map to their base lexeme, compounds in *some/any/every/no* + *one/body/thing/where* are determinatives by parity with `lex_anyone`, a multiword mention resolves to its last known noun-subcategory lexeme (*the lucky few* to *few*), and two colour adjectives are set by [lexeme-overrides.json](lexeme-overrides.json) with a manuscript grounding.

| Check | Result |
|---|---:|
| Claims with a construction id from the catalogue | 658/658 (139 remain `taxonomic_or_meta`, 2 `other`) |
| Claims with a subcategory | 580/658 (78 are phrases or classes with no resolvable lexeme) |
| Keyed manuscript claims (expanded run) whose construction id the census reproduces on at least one paired claim | 51/55 |
| Same, for `evidence_type` | 46/55 |
| Census quotations and lexeme groundings resolving against the live manuscript (`make check-claims`) | all |

The construction labels come from Haiku 4.5 through the Claude CLI with structured output, tools and MCP disabled, in batches of 20, then a second pass over the 238 claims the first pass parked as `taxonomic_or_meta` (76 reassigned). A regex rule over the census's free-text label for the residue was tried and retired the same day: [the full TypeSafe run](typesafe-full-2026-09-16/) contradicted all 23 of its assignments. Every model response is kept in `normalize-cache/` by prompt hash; the log records cost, model and provider per call. The GLM route was tried first and abandoned: at low effort it spent its whole output budget reasoning and returned no content, three times.

The key comparison is an agreement measure, not a strict key. A keyed claim in the expanded run aggregates several sentences, while a census claim is one sentence, so paired claims often concern different constructions of the same lexeme and both can be right; pairwise agreement is 86/156 for `evidence_type` and 86/156 for construction, and the per-claim any-match figures above are the informative ones. The 20-claim hand audit of 14 September stands as the only direct check of the census's own labels.

`evidence_type_reconciled` applies one rule: an attestation footnote at the sentence gives `retained_attestation`; `\ungram` in the quote gives `constructed_ungrammatical`; `searched_not_found` is kept; *CGEL* cited in the sentence gives `cgel_described` (`cgel_restricted` kept); another work cited in the sentence gives `other_source_described`; otherwise the census label stands. It changes 24 labels and flags 13 claims whose census label claims a source no citation in the sentence or paragraph supports. It does not touch the `constructed_illustration` versus `authors_analysis` boundary, which no mechanical signal can see.

[amendments.json](amendments.json) carries the current wording of a quoted sentence when the manuscript changes it, with the reason; `normalize.py` and `check_sources.py` both apply it. The first three entries record the two citation repairs of 16 September: the Payne contrast sentence (`pay-019`, `pay-020`) now cites Payne et al. (2010: 41–42), verified against the PDF, and every account row of `tab:rivals` carries its year (`his-011`).

The tables describe what the census records. They are not a verdict on the manuscript, and the worklist's 340 loci are places where an attestation or a judgment datum would change the recorded basis, not places where the claim is unsupported.
