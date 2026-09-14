# Response to the completed Roughdraft read

I checked all six comments and the tentative footnote, including the annotation already present when we committed. After removing review markup and normalizing Markdown formatting, the reading copy matches the current manuscript: there are no additional unmarked prose changes to recover.

## Hudson’s inventory — s1 and c1

The qualification belongs in the main sentence. Section 6 already explains the narrower inventory, so a second footnote would repeat that explanation. Replace the paragraph at the end of §5.2 with:

> Nesting determinative inside pronoun would add pronoun to the inheritance path from Noun without changing this fragment’s judgments. Applying Hudson’s nesting to the full determinative inventory used here is an extrapolation; §6 discusses the inventory differences.

One detail from checking the source: Hudson explicitly mentions CGEL’s PP determiners, including *over thirty ties*, on p. 10. He distinguishes CGEL’s usage from his narrower one; this passage doesn’t supply the extended fragment we construct here. The existing “implementations here” qualification remains appropriate. [Held article, pp. 9–10](/Users/brettreynolds/projects/LLM-CLI-projects/literature/Hudson2004_Are_determiners_heads.pdf)

## Separate the overall assessment — c2

Yes. Rename §5.4 **Comparison of the four implementations** and insert **§5.5 Overall assessment** before “I favour the D-noun package”. Its two paragraphs then visibly assess the combined profile and structural argument. Section 6 can continue to address the further question of coordinate versus nested rank. No paragraphs need moving or rewriting.

## The 232-to-155 reduction — c3

Your recollection is substantially right, and our supplement already explains it. Comparing the archived files identifies **76 omitted singleton columns and one omitted all-zero column**. There are also eleven changed cells in a retained feature, and one singleton remains. The reduction shouldn’t be presented as an unexplained numerical mismatch. [Lineage record](../analysis/results/matrix-lineage.json) · [Audit](../matrix-audit.pdf)

The published methods and code still describe the 232-feature inventory without specifying that filtering step. The recovered working matrix also isn’t authenticated as the published input. I suggest this replacement footnote:

> Relative to a recovered 232-feature working matrix, the public 155-feature file omits 76 singleton columns and one all-zero column. The accompanying *Replication audit of the English determinative–pronoun feature matrix* documents the remaining coding differences, reproduces the published statistical decomposition, and examines sensitivity. The recovered matrix isn’t authenticated as the published input; the public file is preserved unchanged.

## Extending the matrix — c4, c5, and c6

The scope justification works, but the reason should be the design and validation work required. The 2021 paper itself already identifies adjective sampling and semantic coding as obstacles to extending the comparison. [Published discussion, §4](https://cadernos.abralin.org/index.php/cadernos/article/view/399)

Even a small extension changes both dimensions. For illustration, adding twenty word forms and twenty features to the public matrix creates **6,260 additional cells**: 20 × 155 for the new rows, plus 158 × 20 for the new columns. Many would be straightforward; the difficult work is defining the diagnostics, checking uncertain cases, and validating their coding. Every new feature also needs coding for the original 138 forms. Previously removed singleton features would need reconsideration because they might become shared in the enlarged sample.

Using only the nouns and adjectives already discussed here could support an exploratory pilot. Those examples were selected for particular comparisons, so that pilot wouldn’t by itself supply representative category profiles. A defensible extension therefore amounts to a further empirical study. The cell count shows the scale; a credible time estimate would require settling the sample and feature set first.

Add the following paragraph after the discussion of what Reynolds (2021) establishes:

> Extending that study to nouns and adjectives would require a new sampling and coding design. The examples discussed here offer starting points, but don’t constitute representative samples of the open categories. New diagnostics would also need coding for the existing forms, with the feature selection reconsidered across the enlarged sample. That further empirical study lies beyond the present comparison of grammatical profiles.

I’d omit the forecast about LLMs. Possible assistance with coding doesn’t settle the sampling, diagnostic, or validation questions, and the paper doesn’t need to predict when the extension will become feasible. The proposed paragraph states the limitation and the work needed to address it.

These are local revisions. No extension of the matrix or additional review pass is proposed.


## Implementation and verification

The Roughdraft review completed without further annotations, and all four revisions above are applied. The new scope paragraph explicitly names common nouns, proper nouns, and adjectives. The original annotated reading copy remains intact; the [fresh reading copy](../notes/determinatives-as-nouns-review-2026-09-13-complete.md) reflects the revised source.

Two XeLaTeX passes produced a 35-page PDF with resolved citations and cross-references, no overfull or underfull boxes, and no new warnings. Pages 26, 29, and 30 were rendered and visually checked for the Hudson qualification, new subsection, scope paragraph, and revised footnote. Existing font and microtype advisories remain. The Markdown conversion preserves eleven trees, seven tables, four formal displays, and 41 adjacent notes. Bibliography and empirical materials are unchanged.

The house-style check found the same twelve existing flags; none was introduced by these revisions. Final polish remains deferred. Sentence-length output follows verbatim.

```text
============================================================
SENTENCE LENGTH
============================================================

  --- determinatives-as-nouns.tex ---
    854 sentences | median 14 | mean 14.3 | middle half 10-18 (8 words)
         1-9  ###################       209   24%
       10-14  ########################  269   31%
       15-19  ##################        207   24%
       20-24  ##########                108   13%
       25-29  ####                       48    6%
       30-34  #                           7    1%
       35-39                              3    0%
         40+                              3    0%
```
