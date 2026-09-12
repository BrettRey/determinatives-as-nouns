# Second author round: implementation and validation

10 September 2026

Implemented the reviewed [second-round assessment](../second-author-round-2026-09-10.md), including the further author comments saved before Done Reviewing. The source, PDF, status, decisions and annotated assessment were copied to `notes/snapshots/2026-09-10-second-round-implementation/` before editing. The assessment and its comments remain untouched.

## Decisions on the further comments

The author's consolidation of the first two economies is accepted: primary-category and phrasal-projection reduction are one opening point. Ordinary Head structure **in the NP** is the second. Cardinal uses provide the third benefit: determinative, common-noun and proper-noun uses now fall within primary Noun. Section 7.3 makes that removed overlap explicit. The benefit concerns cardinals; it neither subsumes adjectival ordinals nor makes complex numeral phrases single lexemes. Shared NP status with genitive determiners and stable projection across dependent and independent uses are already consequences of the first point, developed in §§3.2 and 7.1. They are not counted again as separate numerical savings.

The low-confidence feature-list edit is resolved as **inflection, modification and determination**. Inflection accommodates the morphological contrast without turning grade into a new diagnostic introduced only at the end of §5. Gender and deixis are not clean boundaries here: the paper presents pro-form gender across pronouns and determinatives, and cites their shared deictic properties. Those comparisons remain in their existing places.

The uptake objection is accepted. CGELBank demonstrates implementation within the CGEL tradition, not independent adoption. The introduction now says: “As a syntactic representation, fusion of functions appears to have seen little adoption outside work based on CGEL.” This is a qualified authorial assessment, not a measured rate or a claim that no independent work discusses fusion. It is not used as evidence of grammatical inadequacy.

A bounded primary-source check found relevant independent engagement. [Doug Arnold's HPSG 2018 abstract](https://phiz.c.u-tokyo.ac.jp/~hpsg2018/arnold.pdf) explores a formalization but reaches largely negative conclusions. [Zhen Wu's 2020 UCL thesis, abstract p. 4](https://discovery.ucl.ac.uk/id/eprint/10118908/1/Exocentric%20Noun%20Phrases%20in%20English.pdf) argues against a unified fusion account. [Elazar and Goldberg's 2019 article](https://aclanthology.org/Q19-1030/) frames its computational task in terms of recovering implicit nominal information. These sources distinguish discussion, criticism and phenomenon-level borrowing from adoption of the dual-function representation. They do not establish an exhaustive absence or an adoption rate. No new citations were added to the manuscript for this qualitative assessment.

The remaining reviewed proposals are implemented: a direct fourfold claim in the abstract, opening and conclusion; an explicit classification-to-inheritance connection; a positive coordination argument in §5; inheritance-path wording in §7.2 that does not imply an increased global node count; and the author's DP disambiguation with a resolved §2.1 cross-reference. The fragment's compatibility with nesting remains explicit.

## Verification

The full XeLaTeX, Biber, XeLaTeX, XeLaTeX sequence passed. The PDF has 23 pages and all 24 citation keys resolve. No citation or cross-reference reruns remain. Two existing overfull lines remain, at 4.47 pt and 5.04 pt; the former overfull §5 closing paragraph is resolved by the revision. The existing font, header and microtype advisories remain. No image inspection was performed, following Brett's instruction.

Source comparison confirms that all six figures containing eleven trees, four formal schemata, five tables and displayed examples are unchanged. Hash comparison confirms all 35 protected empirical, supplement and bibliography files are unchanged. PDF text extraction confirms the revised opening, motivation, §5 closing and conclusion are present. The fresh [reading copy](../determinatives-as-nouns-review-2026-09-10-round-two.md) has eleven text trees, four text schemata, five tables, nine adjacent footnotes and two underlined spans, with no Pandoc warnings or unresolved placeholders. It has a new filename to preserve the earlier author annotations.

A scoped read of the changed paragraphs found no added editorial explanations of the revision history in the manuscript. The existing comparative limits remain where the argument needs them. No whole-manuscript review pass was rerun or marked current.

The house-style checker reports 14 potential flags. The new “therefore” states the reviewed inheritance relationship; it is retained under the author's standing instruction to permit substantive inferential uses. The motivation opener states the paper's reason directly, so its cadence advisory requires no change. The remaining flags concern retained wording, optional contractions or formal mathematical notation. No automatic substitutions were made. The computed sentence-length section follows verbatim.

```text
============================================================
SENTENCE LENGTH
============================================================

  --- determinatives-as-nouns.tex ---
    516 sentences | median 14 | mean 14.8 | middle half 10-18 (8 words)
         1-9  ##################        116   22%
       10-14  ########################  152   29%
       15-19  #######################   145   28%
       20-24  #########                  60   12%
       25-29  #####                      30    6%
       30-34  #                           8    2%
       35-39                              1    0%
         40+  #                           4    1%
```
