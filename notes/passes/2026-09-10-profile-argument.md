# Cumulative profile argument — revision record

10 September 2026. Brett authorized revision after clarifying that similarity across semantics, syntax and morphology supplies the main justification for one superordinate category. The latest annotations in the sections 1–3 reading copy were included in that revision. The annotated file remains intact.

The [new reading copy](../determinatives-as-nouns-review-2026-09-10-profile.md) corresponds to [the manuscript source](../../determinatives-as-nouns.tex) and [29-page PDF](../../determinatives-as-nouns.pdf).

## Argument

The combined profile now governs the abstract, introduction, §3.1, §4.7, §5, §7.3 and conclusion. The author makes a cumulative classificatory judgment, weighing overlapping properties against systematic differences. CGEL's pronoun classification provides a starting comparison. Shared external functions are one source of evidence, with the interrogative construction illustrating why equal functions don't imply equal distribution. The argument retains the strongest modifier objection and the adjectival affinities of grade and derivation.

Nominal projection, ordinary Head structure, NP realization of determiner function and the treatment of cardinal uses are connected consequences. Comparative economy remains secondary. The matched fragment and strongest separate-D alternative remain available for assessing those consequences; the revision doesn't require a unique prediction or net rule saving before the author can defend a category judgment.

## Annotation decisions

| Annotation | Implementation |
|:---|:---|
| c1; s1–3 | Language-specific scope moved to a footnote; determiner defined as the function characteristically performed by phrases headed by determinatives. |
| s4–5, s7–8 | Palmer, Postal and Sommerstein now have textual citations at their mentions. |
| c2; s24 | Four connected structural consequences are enumerated, including the shared NP realization of determiner function. The primary argument is stated separately. |
| c8; s9–10 | Table 1 gives the named historical accounts individual rows and distinguishes analytical levels. The additional pronoun-within-proper-noun and determinative-within-common-noun arrangement appears as a logical alternative. |
| s11 | The Sommerstein discussion retains the historical count restriction and adds the later common-count-noun analysis of anaphoric *one*. |
| s12–15 | Hudson's criteria are described as also limited; Spinillo's three retained articles are identified by their lack of ordinary independent use; the requested list punctuation is applied. |
| c3; s16 | Determinative uses in determiner function have concrete examples. Pronoun case explicitly includes genitive. |
| c4–5 | The ambiguous reflexive-number wording is replaced. Singular/plural *you* and *yourself/yourselves* distinguish number expression from inflection within one lexeme. |
| c6 | The table and §3.4 compare specific affixes, separating base selection from output category. The available comparison establishes no noun-selecting suffix shared by pronouns and determinatives; this is a limit of the comparison, not a claim of universal absence. |
| s17–20 | Pro-form gender has its own row and explanatory paragraph. Referent construal is distinguished from noun-class gender. |
| s21–23 | Relative postmodification appears for common nouns and pronouns. The prose retains the documented restrictions on personal-pronoun modification. |
| c7 | CGEL's external-function rationale no longer serves as the governing membership test. The four profiles are assessed together. |
| s24–25; c9 | The minor NP determiner examples are retained without calling them nonstandard. Actual PP exceptions replace *almost ten*, which has NP status under the proposed analysis. c9 contains no comment text. |

## Source checks and limits

CGEL p. 356 documents the minor NP determiners and PP alternatives; p. 486 explicitly treats singular and plural *you* as distinct lexemes. Chapter 10 §§7.1 and 7.9 supports the comparison between interrogative words and phrases, including *what size shoes*. Chapter 19 §§5.6.2(b) and 5.7.2 supplies the affix comparisons; p. 566 supplies noun-based adverbial *-ly* examples. The pro-form-gender paragraph uses the existing cited Reynolds paper and its distinction between referent construal and lexical noun-class gender.

The one new bibliography entry, `payne2013anaphoric`, was verified against the [published article on Pullum's site](https://www.lel.ed.ac.uk/~gpullum/PaynePullumScholzBerlage.pdf) and the [University of Edinburgh publication record](https://www.research.ed.ac.uk/en/publications/anaphoric-emone-emand-its-implications/): *Language* 89(4), 794–829, DOI 10.1353/lan.2013.0071. The article header supplies Barbara C. Scholz, preferred over the repository metadata's conflicting middle initial. Section 3.1, pp. 797–798, distinguishes common-count anaphoric *one*, personal-pronoun *one* and determinative *one*. The citation doesn't import every theoretical commitment of that paper.

The morphology discussion retains the previously verified dictionary attestations for *thisness*, *fewness*, *muchness* and *mostly*. Their existence doesn't establish uniform productivity or the lexical category of every historical base. The additional affix comparisons are bounded examples, not an exhaustive survey or a quantitative result.

## Verification

The full XeLaTeX/Biber build succeeds: 29 pages, 22 resolved citation keys, no missing references or citations. All cited entries have author, title and year fields. The 2,174 bibliography entries unused by this manuscript belong to the shared/local bibliography pool and are informational, not deletion candidates.

All eleven trees and four formal schemata match the snapshot. Three tables are unchanged; Tables 1 and 2 were revised. All 70 protected files match their recorded hashes, including the original annotations, empirical analyses, completed multiverse work, central bibliography and supplements. The local bibliography contains the one verified addition.

The reading copy contains eleven text trees, four text schemata, five tables and thirteen adjacent notes. Table 1 has twelve data rows; Table 2 has nine. Pandoc reports no warnings. Citation-parenthesis artifacts and a discretionary hyphen from conversion were normalized. Roughdraft's Markdown doctor passes. PDF text extraction places the complete revised tables on pages 5 and 8. No images were generated or inspected.

Two pre-existing small overfull lines remain: 4.46857 pt at source lines 343–344 and 5.04185 pt at lines 419–420. The existing font-substitution and microtype advisories remain production issues. The style checker reports seventeen potential flags; these include retained inferential *therefore*, legitimate mathematical subscripts, optional contractions and cadence advisories. They are not seventeen verified violations. No new long-paragraph flag appears.

Machine-readable results are in [the checks file](2026-09-10-profile-argument-checks.json), the complete style output in [the style record](2026-09-10-profile-argument-style.txt), and the source changes in [the diff](2026-09-10-profile-argument.diff). The prior source and annotations are in `../snapshots/2026-09-10-profile-argument-revision/`.

The computed sentence-length section follows verbatim.

```text
============================================================
SENTENCE LENGTH
============================================================

  --- determinatives-as-nouns.tex ---
    612 sentences | median 14 | mean 14.8 | middle half 10-19 (9 words)
         1-9  ####################      144   24%
       10-14  ########################  174   28%
       15-19  ########################  172   28%
       20-24  ###########                77   13%
       25-29  #####                      35    6%
       30-34  #                           5    1%
       35-39                              0    0%
         40+  #                           5    1%
    [advisory] 61% of sentences fall in 12-26 words; the band is narrow, so check whether the rhythm has flattened

```
