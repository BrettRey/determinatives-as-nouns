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
