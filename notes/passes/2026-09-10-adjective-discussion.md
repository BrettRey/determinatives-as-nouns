# Local revision: adjectival independence and second best

This is a check of the September 10 revision, not a repeat of the overnight whole-manuscript passes. The main changes are in §4.4, with number added to the §3.1 comparison preview. The section develops nominal number, the benefit and possible costs of reducing fusion, and the apparent adjectival counterexamples.

The Henrietta example and *Bluer is better* remain in the main argument. Colour-category ambiguity and coordination are distinguished; coordination is not claimed to prove ellipsis. The comparison with bare comparative *bluer* in a situational shirts context is explicitly constructed and has no imposed grammaticality mark. The evaluative subject's phrase category is explicitly unresolved. These are live analytical questions, not findings of ungrammaticality or established ellipsis.

A short footnote links the possible compensating costs of reducing fusion to Lipsey and Lancaster's theory of second best. This is explicitly an analogy about interacting grammatical choices. It does not establish a formal optimum for the grammar or imply that retaining fusion elsewhere cancels a local simplification.

## Source verification

- CGEL printed pp. 236, 417 and 418 were checked directly in the local PDF text. They support restricted non-NP subjects, the bare colour/age/size constructions, and the contrast between adjective and noun morphology/modification respectively.
- The Stanford CS329X [Codeswitching LLMs slides](https://web.stanford.edu/class/cs329x/slides/Lecture12_B_Codeswitching%20LLMs.pdf), slide 8, contain *Bluer is better*. Direct download and `pdftotext` confirmed the wording. The claim about a degree/property interpretation is marked as the paper's analysis, not attributed to the slide author.
- Lipsey and Lancaster's metadata was verified against [Oxford Academic's original article record](https://academic.oup.com/restud/article-abstract/24/1/11/1542458) and [issue 24(1)](https://academic.oup.com/restud/issue/24/1). The introductory argument on printed pp. 11–12 was read in the [full text uploaded by Lipsey](https://www.researchgate.net/publication/261833990_The_General_Theory_of_Second_Best). The local entry uses the publisher's 1956 year; the JSTOR volume cover says 1956–1957. DOI: 10.2307/2296233.

## Validation

The full XeLaTeX/Biber build passes: 24 pages, 24 resolved citation keys, no Biber warnings/errors, unresolved references/citations or rerun requests. The new Lipsey–Lancaster reference appears correctly in the extracted bibliography. The Stanford PDF hyperlink was checked in the generated PDF's URI annotations. Six figures, eleven trees and five tables are byte-for-byte unchanged as source blocks. The empirical supplement sources and analysis files were not edited.

The new number paragraph initially produced an overfull line at the unbreakable slash pair. Allowing a break after the slash removed it without changing the words. The final log retains the four pre-existing overfull lines (4.46857, 5.04185, 4.2891 and 1.27979 pt), plus the existing header, microtype footnote-patch and font-substitution warnings. No image inspection was performed. The changed prose and footnotes were checked in the extracted PDF text. `git diff --check` passes, and the untracked main TeX has no trailing whitespace.

The automated style warnings were inspected locally. The new *therefore* marks an inference, and the contrast between an NP's distribution and its head's properties is substantive. The standing author instruction permits *therefore*. Other flags belong to unchanged prose or math. The sentence-length section below is reproduced verbatim; the advisory did not prompt mechanical sentence edits. This local check is not recorded as a new complete whole-manuscript pass.

The verified reference is in the local bibliography. Central bibliography merge remains deferred under the previously documented dirty-file protection. No Zotero import, central bibliography mutation, commit, push or submission was performed.

## Computed sentence lengths

```text
SENTENCE LENGTH
============================================================

  --- determinatives-as-nouns.tex ---
    524 sentences | median 14 | mean 14.8 | middle half 10-18 (8 words)
         1-9  ###################       118   23%
       10-14  ########################  152   29%
       15-19  ########################  149   28%
       20-24  ##########                 63   12%
       25-29  #####                      29    6%
       30-34  #                           9    2%
       35-39                              1    0%
         40+                              3    1%
    [advisory] 61% of sentences fall in 12-26 words; the band is narrow, so check whether the rhythm has flattened
```
