# Final source proofreading
The reviewed substantive repairs are applied. No further argument, grammar, citation-key, or source-level LaTeX defect emerged. All 649 live census quotations now match the source; the generated tables agree with their inputs, and the numerical totals are unchanged. The apparent unresolved `tab:rules` reference resolves in the included coverage table.

The remaining house-style issue is paragraph length. These are minor readability repairs, not PDF layout work. I propose the following breaks, preserving the wording except for the small sentence split in the supplement catalogue.

| Location and current paragraph opening | Proposed break before |
| --- | --- |
| Main §2.1, “Each of the people takes singular agreement…” | “That variation is agreement…” |
| Main §2.3, “Case gives a further partial connection.” | “The compounds' genitives belong to the NP…” |
| Main §3.1, “CGEL's treatment of my supplies a precedent…” | “The inference has two stages.” |
| Main §3.2, “Van Eynde draws the same line…” | “With peripheral a in a few…” |
| Main §5.3, “Enough also modifies adjectives…” | “Reynolds surveys the determinatives…” |
| Main Data and analysis materials, “The accompanying supplements are…” | End the first sentence after the quantifier supplement. Begin a new paragraph “Two further supplements are [claim-register title]…”; retain the existing descriptions and final directory sentences. |
| Quantifier supplement, Contextual restriction with _few_, “NOW: Daily Times…” | “Of 94 NOW lines…” |
| Claim-register supplement, “This supplement records participation claims…” | “It exists so that…” |
| Claim-register methods, “A census of the article's sentences…” | “Each claim was then labelled…”; “Since the census…”; “The quotation check tests…” |
| Coverage supplement, “The article's §5 compares four implementations…” | “This audit records how…” |
| Coverage supplement, “The classifications are the author's…” | “S and D2 codes count cells…”; “Beside each cell…” |

The automated suggestions to write “unsupervized” and remove every “therefore” are not valid corrections here. The flagged inference words do inferential work. The cadence warnings don't justify another prose pass. Terminology flags were checked against the definitions in the introduction and relevant sections; they don't call for adding a glossary to the abstract. The quoted “paving the way” is an attestation and stays as quoted.

No PDF was built or inspected. No new source, numerical analysis, or model coding was added.
## House-style tool's sentence-length output
Recorded before the proposed paragraph breaks; these breaks don't change the sentences, except for the catalogue sentence split noted above.

```text
SENTENCE LENGTH
============================================================

  --- determinatives-as-nouns.tex ---
    801 sentences | median 15 | mean 16.6 | middle half 10-20 (10 words)
         1-9  #################         167   21%
       10-14  ########################  232   29%
       15-19  ###################       183   23%
       20-24  ###########               109   14%
       25-29  #####                      47    6%
       30-34  ###                        26    3%
       35-39  #                          11    1%
         40+  ###                        26    3%
```

The final supplement linter output, including its sentence-length distributions, is preserved [verbatim](2026-09-19-supplement-style-output.txt). Its remaining flags concern optional contractions, contrastive wording, the inference word “therefore”, and paragraph cadence; none warrants another edit.

---
comments:
  c1:
    body: apply if the issue is egregious, but don't be too strict about lengths.
    by: user
    at: 2026-09-19T17:48:11.755Z
  c2:
    body: Applied paragraph breaks only to the two methods paragraphs exceeding 200 words, in the claim-register and coverage supplements. The other proposed length changes were not applied.
    by: Codex
    at: "2026-09-19T17:48:59.441Z"
    re: c1
