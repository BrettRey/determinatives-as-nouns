# Comparative revision — 8 September 2026 (UTC)

The working LaTeX source now incorporates the bounded comparative revision requested in the three reports. The review copy is `determinatives-as-nouns-review-2026-09-08.md`; it preserves the manuscript prose, references, tables, all nine trees and the four displayed schemata. Trees and schemata use text notation for commenting. The LaTeX file remains the master.

## Changes

- Added separate D with ordinary Head to the matched fragment and comparison table, including cross-category Nom projection. It receives the same permissions as the nominal account and can share the reduced phrase-type inventory in Det function. The preference for inclusion now explicitly concerns inheritance through Noun, not an exclusive coverage gain.
- Compared *few survivors*, independent *few*, *the lucky few* and *the idle rich*. A second tree gives the genuine Mod–Head fusion rival for *the lucky few*, acknowledging reuse of existing adjectival fusion machinery.
- Added paired ordinary-Head and fusion trees for *hardly anyone present*. Base-specific premodifier permissions and the compound’s post-head, non-recursive restrictor conditions are stated separately. The account sketches *someone* and *everybody* without pretending that every base admits the same adverbs.
- Made the hierarchy of commitments explicit: inclusion first, ordinary Head a further proposal, coordination provisional. Section 6 leads with the proper-name cross-cut and contrasts the range of external determination available to independent quantifiers with its marginality for pronouns.
- Clarified the two-stage article argument. *My* blocks an exclusion criterion; its paradigm does not supply the articles’ positive evidence. A competing cluster of otherwise exceptional synchronic restrictions would favour a separate article category.
- Cut *or so* and *the selected two*. Retained *the remaining three* with the common-noun alternative explicitly live, and treated cardinal unification as conditional on the 2026 analysis.
- Shortened the main-text matrix discussion and retained numerical detail in Appendix A. Added the row-exchangeability qualification: permutation values describe comparisons with shuffled partitions, without a defended population-level exchangeability assumption.
- The corpus subsection, including the missing *few/either/neither* attestations and both numbered corpus examples, is byte-identical to the pre-revision source. No empirical data, numerical outputs or analysis scripts were changed.
- Updated Reynolds 2025 to “Manuscript submitted to Folia Linguistica,” consistent with the local submission record. Model-name verification remains a proof-stage task.

## Source checks

| Source and pages | Result |
|---|---|
| Palmer 1924, p. 24 | Re-read the HathiTrust scan and downloaded the page PDF. His stated grounds include disputed classification and most members’ ability to function as pronouns or modifiers of nouns. Reworded to follow this directly. |
| CGEL, pp. 411–412 | Page 411 uses both modifier and complement terminology. The explicit partitive analysis and p. 412 tree [7a] assign Comp to the PP within Nom. Corrected the tree and rival schemata accordingly. |
| CGEL, pp. 328, 392, 395–396, 536 | Re-read the cited pages: bare-role NP restriction, *several* predication, formal *many* predication, and exclusion of specifying *be* from the diagnostic are supported. |
| CGEL, pp. 415–417 | Re-read the determinative Mod–Head analysis and examples, and the restrictions on adjectival fusion. Used these in the matched comparison. |
| CGEL, p. 431 n. 47 | Verified numerical *or so* as coordination; removed the paragraph because that fact supplies no independent category argument here. |
| Payne, Huddleston & Pullum 2010, pp. 40–42, 60–61 | Re-read the published pages: modifier/category continuity and the limits of distribution-only classification support the retained discussion. |
| Payne, Huddleston & Pullum 2010, p. 75 n. 3 | Verified *an almost textbook case*. Replaced the claimed exceptionless Noun-wide ban with the narrower cost of systematic adverbial premodification in a noun subcategory. |
| Payne, Huddleston & Pullum 2007, pp. 581–583 | Read the compound discussion, tree (13d), and explicit post-head/non-recursive restrictor conditions. |
| Spinillo 2004, pp. 140–144 | Retained the account checked directly against UCL’s page scans in the preceding restoration: dependent/independent continuity, comparison with complement alternations, and her proposed pronominal grouping. No return to the earlier inaccurate demonstratives-only characterization. |

## Validation and remaining work

The revised draft built successfully with XeLaTeX/Biber and no overfull boxes or unresolved citations/references. Two subsequent verb-agreement corrections are in the source and review copy. Existing font/header warnings remain. The current source is 8,644 words by TeXcount, 274 above the pre-revision source. The built PDF is 25 pages.

Brett explicitly deferred proofing because this is not the final build. Page-layout inspection stopped; no final visual proof is claimed. No new review board, corpus study, submission or public update was undertaken.

At proof stage, check the vendor designations for GPT-6 (Astra), Claude Opus 5, Claude Haiku 4.5, GLM-5.3-Flash and GPT-5.6 (Sol), preserving the identities of the models actually used. The dated usage record is `analysis/ai-assistance.txt`.

## Sentence-length output

The mechanical style check also flagged existing contractions/connectives, paragraph cadence, and two non-prose subscript/identifier false positives. These are advisory; another broad style pass was not undertaken.

```text
SENTENCE LENGTH
============================================================

  --- determinatives-as-nouns.tex ---
    582 sentences | median 14 | mean 14.6 | middle half 10-18 (8 words)
         1-9  ##################        133   23%
       10-14  ########################  177   30%
       15-19  ####################      151   26%
       20-24  ###########                79   14%
       25-29  ####                       30    5%
       30-34  #                           9    2%
       35-39                              1    0%
         40+                              2    0%
    [advisory] 61% of sentences fall in 12-26 words; the band is narrow, so check whether the rhythm has flattened
```
