# Expanded source extraction — 14 September 2026

**Completed: Opus accepted the corrected 110-claim batch with no further correction requests.** Read [records.json](records.json) with [queries.json](queries.json), [exceptions.json](exceptions.json), and the [source texts and hashes](inputs/sources.json). The exception file is part of the result: the fixed status field cannot carry all the source's qualifications on its own.

The batch covers every cell of the quantifier supplement's nine-expression, six-frame comparison (54 queries), plus 56 additional uses from the full manuscript. There are 34 lexeme entries, 33 with new participation queries; `lex_book` is retained as a control entry without a new query. The 11-entry construction catalog includes all five original definitions verbatim and six additions. The six scope answers address boundaries and unresolved source questions. This is a bounded selection from the full documents, not an exhaustive inventory. See the [cell map](supplement-cell-map.json) and [scope selection](scope/result.json).

The record fields, three statuses and six condition bearers are unchanged. Identifier enums and construction definitions expanded as data. One parent correction to the proposed scope moved X098 (*a lot of delegates*) to the general argument construction, so the query did not assume that its undetermined of-complement was partitive; the [before/after record](scope-adjustments.json) is preserved.

| Check | Result |
|---|---:|
| Query IDs, lexeme links, forms, schema and catalog | Passed |
| Record quotations exactly matching the supplied texts | 659/659 |
| Exception-note quotations exactly matching the supplied texts | 67/67 |
| Full initial Opus review | All 110 claims, 34 entries, 11 constructions and 6 scope answers |
| Final changed-claim recheck | 7/7, plus the updated scope answer |
| Manuscript and supplement source hashes | Unchanged |

Seven claims changed after review (6.4% of the batch): X012, X030, X037, X042, X067, X100 and X109. There was one status change: X100 moved from `excluded` to `not_stated`. The final counts are **98 licensed, 7 excluded and 5 not_stated**, all interpreted with their query contexts and conditions. One scope answer was updated to explain X100. All other JSON records are structurally identical to the first extraction. These change counts are not a benchmark accuracy estimate.

The initial full review found an omitted constructed example, three missing supporting quotations, and an overstatement of *plenty*'s resistance to modification. The parent inspected a six-record sample selected before extraction returned, plus the exception notes. That check identified missing attachment grounding for *none* and mixed NP/adjective properties for *the rich*. It also challenged Opus's initial proposal to replace *plenty*'s unsupported exclusion with `licensed`. A focused Opus review agreed that `not_stated`, with the resistance preserved in the exception file, was the faithful fixed-schema rendering. Aristotle applied the combined corrections; Opus then accepted the changed records. See the [initial review](review-1/result.json), [focused resolution](spotcheck-resolution/result.json), [final review](review-2/result.json), and [parent sample assessment](parent-sample-assessment.json).

The 21 exception notes retain limitations. In particular, searched-but-unattested cases and the unresolved *plenty* judgment share `not_stated` for different reasons; restricted R cells retain their qualifications; evidence types are carried in prose rather than a dedicated field; some lexeme identities and selection properties remain unsettled by the sources. The *none* attachment inference and *rich* bearer convention are explicit. Final acceptance concerns the documented extraction bundle; it does not settle these source questions.

| Opus phase | Elapsed | Output tokens, including thinking |
|---|---:|---:|
| Scope selection | 15.04 min | 76,109 |
| Full review | 4.98 min | 24,904 |
| Three-record resolution | 2.47 min | 12,214 |
| Focused final recheck | 1.85 min | 9,319 |
| **Total** | **24.35 min** | **122,546** |

Opus 5 reported 350,241 processed input tokens (8 uncached, 346,525 cache creation, 3,708 cache reads). Of its 122,546 output tokens, 98,843 were thinking tokens. Ancillary Haiku usage from the Claude CLI is included separately in [manifest.json](manifest.json). All four CLI cost estimates total **$6.79**; these are reported list estimates, not a statement of subscription charges. Scope selection accounts for about fifteen minutes of the supervisory work. Root-token savings and a direct-Opus expansion comparison were not measured.

Aristotle's initial completion was observed after about 25.4 minutes; its correction task reported 7 min 36 s. A dropped status stream did not stop the initial job, and completion-check errors in the correction job recovered. Both tasks completed without needing a `resume`. No added process timeout was imposed. Raw candidates, service archives, prompts, diffs, reviews and per-stage usage remain in this directory. No manuscript changes or external-literature expansion were made.
