# Author reframing and scar-tissue pass — 10 September 2026

Brett approved the [assessment of his comments through §2.1](../author-comments-through-2-1-response-2026-09-10.md), then requested a scar-tissue check during implementation. The revision is complete in the LaTeX master. The [fresh reading copy](../determinatives-as-nouns-review-2026-09-10-reframed.md) contains the resulting manuscript; the earlier annotated copy remains preserved.

## Result

The abstract, opening proposal, figure descriptions, nominal comparison, cumulative argument, formal fragment and conclusion now present one D-noun analysis with inherited nominal projection. The fragment compares it with separate D admitting ordinary heads and with CGEL's separate D using fusion. Its rules, lexical permissions and judgments remain the same. The strongest separate-D rival still limits the taxonomic inference: shared projection alone does not establish nounhood. The article-membership argument and provisional coordinate classification remain.

The introduction incorporates the relational wording and historical Palmer contrast, removes the auxiliary footnote, and states the rejection of the DP hypothesis for English with the existing Abney, Pullum–Miller and Bruening references. CGEL's anaphoric and predicative genitive analyses remain explicitly attributed. The text makes no unargued commitment to retaining genitive fusion in the proposed grammar. The earlier requested 1 pt Head edges and example underlining remain.

The [scar-tissue record](2026-09-10-editorial-scar-tissue.md) identifies eight edits, with exact originals and replacements. These include the new footnote preserving the fourth comparison: it was unnecessary after the reframing, and CGEL's genitives already demonstrate that nouns and fusion can coexist. The counterexamples, second-best analogy, live comparative restrictions and empirical correction record remain. The pass is recorded against the final manuscript.

## Verification

The full serial XeLaTeX/Biber build passes. The PDF is 23 pages, with all 24 citation keys resolved and no rerun requests. Six figures, eleven trees and four formal schemata remain; all tree and schema source blocks are unchanged from the pre-reframing snapshot. The five tables remain, with the account table reduced to three rows. Nine footnotes remain. All 35 protected analysis, bibliography and supplement files are unchanged.

There are three existing small overfull lines (4.46857, 5.04185 and 4.2891 pt), plus existing font, header and microtype advisories. No new overfull line was introduced. Images were not inspected, following Brett's instruction. PDF text confirms the revised DP paragraph, inherited projection and three-account table. This is a successful working-draft build; visual production checking remains separate.

The fresh Markdown conversion contains all eleven trees, five tables, four schemata and nine notes, with no Pandoc warnings. It preserves the two underlines and removes obsolete variant labels. The original annotated review copy and the assessment were not overwritten.

The local style alerts were inspected. The remaining therefore uses express actual inferences and follow Brett's standing allowance. The mathematical subscript is part of the formal notation, and the flagged comparison language describes live alternatives. The sentence distribution below is computed from the final source. No automatic rhythm rewrite was applied.

See the [complete source diff](2026-09-10-author-reframing-source.diff), [build log](2026-09-10-author-reframing-build.log) and [machine-readable verification](2026-09-10-author-reframing-check.json).

## Computed sentence lengths

```text
SENTENCE LENGTH
============================================================

  --- determinatives-as-nouns.tex ---
    512 sentences | median 14 | mean 14.7 | middle half 10-18 (8 words)
         1-9  ###################       118   23%
       10-14  ########################  153   30%
       15-19  ######################    143   28%
       20-24  #########                  58   11%
       25-29  ####                       27    5%
       30-34  #                           8    2%
       35-39                              1    0%
         40+  #                           4    1%
```
