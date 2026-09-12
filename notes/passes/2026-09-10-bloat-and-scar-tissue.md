# Bloat and editorial scar tissue — completed pass

10 September 2026. Author request: “remove bloat and scar tissue.”

The [manuscript](../../determinatives-as-nouns.tex) is now **24 pages and 7,356 words**, down from 29 pages and 9,247 words: **1,891 words removed (20.4%)**. The [fresh reading copy](../determinatives-as-nouns-review-2026-09-10-trimmed.md) presents the shorter version; earlier annotations remain intact.

## Routing and contract

This was clarity repair. The reader's question is whether English determinatives belong within Noun; the answer is four coordinate subcategories, justified by their combined semantic, syntactic and morphological similarities. The intended reader is a descriptive or theoretical grammarian. The exposition proceeds through competing classifications, comparative profiles, nominal constructions, hierarchy, restricted membership and structural consequences. Its argument, section structure and audience were already settled for this pass.

Section 7.2 remains the hardest passage: readers must distinguish category membership, nominal projection and use permissions. Its rules and worked examples, including the inner and outer NPs in *the apple*, remain. Reconstruction would have been warranted if the cuts exposed a missing premise or made the central inference unrecoverable. Reading the complete source before and after the edit supported retaining the architecture.

## Cuts

| Location | Change and reason |
|:---|:---|
| Introduction | One statement of the primary justification and one roadmap replace repeated framing. Historical claims and all four structural consequences remain. |
| §2 | Historical contributions and limits are stated directly. Repeated assurances about retaining predecessors and another list of comparison domains are removed. |
| §3.1 | Concrete comparisons replace methodological replies to earlier comments. The external-function counterexample, pro-form gender and singular/plural *you* remain; the section ends with the substantive synthesis. |
| §§3.2–3.3 | Repeated figure walkthroughs and reminders are shortened. *Almost ten* is integrated as an NP example. The strongest premodifier objection, exceptions and negative examples remain. |
| §3.4 | Affix input, output and productivity limits are stated once at their point of use. Every affix and example remains. |
| §4 | Redundant closers, advance summaries and the unused explanation of *productivity* are removed. Fusion, silence, adjective, number, compound and predicative countercases retain their actual conditions. |
| §5 | The gender comparison is applied to the hierarchy question through a cross-reference. The positive coordination argument and the matrix's limits remain. |
| §6 | The three membership conditions are given through their concrete application to articles; their abstract rehearsal is removed. |
| §7 and conclusion | The costs subsection assesses consequences without repeating the profile case. The conclusion gives one taxonomic judgment and its structural consequences. |

The [change ledger](2026-09-10-bloat-and-scar-tissue-changes.json) records the original passages, replacements and reasons; the [source diff](2026-09-10-bloat-and-scar-tissue.diff) records the exact final edit. The final reading check also removed a duplicated roadmap and joined the nesting criterion to its semantic comparison.

## Verification

All 254 distinct example/form strings, direct quotations, 22 citation keys, eleven trees, four formal schemata, five tables and both numbered example blocks are preserved. All 72 protected files match the baseline, including bibliography, earlier annotations, analyses and supplements. Thirteen footnotes remain. No new citation or empirical claim was introduced, and no material was moved elsewhere to reduce the count.

The full XeLaTeX/Biber build passes with no overfull boxes or unresolved citations/references. The previous overfull lines disappeared with the redundant prose; two introduced line-fitting issues were resolved. PDF text extraction confirms 24 pages. Table 1 is complete on page 4 and Table 2 on page 6; page 3 is occupied by Figure 1, and page 24 contains the final bibliography entries. Image inspection remains deferred at the author's request. Existing EB Garamond font-substitution and microtype footnote-patch advisories remain.

The fresh Markdown has eleven text trees, four text schemata, five tables and thirteen adjacent notes. Pandoc emits no warnings and Roughdraft's doctor passes. Citation-parenthesis artifacts from conversion were normalized. Both the tracked diff and an explicit comparison of the untracked manuscript with its snapshot have no whitespace errors.

The exact word totals use TeXcount on the document body with semantic text-macro rules and tree notation excluded. This avoids a parsing failure in the preamble's sourcemap. The [before/after counts](2026-09-10-bloat-texcount.json) include text, headings and captions/notes; bibliography is excluded. A [separate plain-text comparison](2026-09-10-bloat-and-scar-tissue-counts.json) corroborates the reduction with a different tokenization. Mechanical checks are in [the validation record](2026-09-10-bloat-and-scar-tissue-checks.json).

The inventory and style candidates were checked against the source. Apparent long paragraphs combine prose with footnotes or formal displays; the remaining paired references have valid antecedents. The style checker reports ten potential flags, including optional contractions, inferential *therefore*, legitimate mathematical subscripting and cadence advisories. These are not ten verified defects. The [full style output](2026-09-10-bloat-and-scar-tissue-style.txt) retains the diagnostics; its computed sentence-length section follows verbatim.

```text
============================================================
SENTENCE LENGTH
============================================================

  --- determinatives-as-nouns.tex ---
    483 sentences | median 14 | mean 14.8 | middle half 10-18 (8 words)
         1-9  ###################       111   23%
       10-14  #######################   135   28%
       15-19  ########################  141   29%
       20-24  ##########                 60   12%
       25-29  #####                      27    6%
       30-34  #                           5    1%
       35-39                              0    0%
         40+  #                           4    1%
    [advisory] 61% of sentences fall in 12-26 words; the band is narrow, so check whether the rhythm has flattened

```
