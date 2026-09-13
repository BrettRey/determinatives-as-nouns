# Implementation of the review through §5
The [approved reconciliation](./2026-09-13-rd-and-fable-response.md) is implemented in the working draft. The manuscript retains the four-account comparison and presents §5 as conditions on labelled structures, following [Pullum’s verified 2020 article](https://cadernos.abralin.org/index.php/cadernos/article/view/279). The rewritten fragment separates lexical use permissions, selected forms, target restrictions, dependent permissions, and Head relations. It includes internal Mod and prepositional-complement uses, distinguishes dependent from independent phrase expansion, and makes the fusion configurations match the diagrams. Statement counts aren't treated as a measure of grammatical economy.

The treatment preserves NP degree modifiers, the two motivated approximative attachment sites, restricted complex _a few_, and ordinary Head for _mine_. Separate D receives the same structural credit where it uses the same NP projection. A category-naming convention isn't used to rule that alternative out.

The accepted wording changes are incorporated throughout the reviewed sections. The profile table adds nominal premodification of proper names and the relevant determinative-headed modifiers. _All we who signed up_ is identified as peripheral; it isn't presented as ordinary internal modification of a pronoun. The ordinary compound example no longer carries an unnecessary CGELBank citation. The Honda quotation is attributed to the English Web Treebank source text, with CGELBank identified separately as the annotation source.

Figure 1 now places all four trees in one row at normal size. Figure 6 places _present_ vertically below Nom while retaining the separate diagonal Head link to DP. The degree section incorporates the temporal NP examples and representative quantified plural measure examples supplied in the review; temporal modification and degree modification remain distinct, and the possible phrasal-compound analysis is left open.
## The fourteen inventory cells
The follow-up stopped after focused checks of the remaining cells. Ten have qualifying attestations; four have no qualifying attestation retained. All queries, exclusions, source links, and verification limits are in the [evidence record](../notes/2026-09-13-quantifier-cells.json).

| Expression | Newly attested cells | Searched without a qualifying attestation |
| --- | --- | --- |
| _certain_ | Existential with partitive | Argument with relative; bare existential |
| _various_ | Argument with relative; existential with partitive | Existential with relative; bare existential |
| _numerous_ | Argument with relative; existential with partitive; bare existential | —   |
| _multiple_ | Argument with relative | —   |
| _countless_ | Argument with relative; bare argument; bare existential | —   |

Seven new examples were checked against their original published pages as well as NOW. The _multiple who_ example (London Free Press), _countless who_ example (WFTV), and bare existential _countless_ (Financial Post) were checked in NOW concordance context with source metadata; their original pages weren't available. The manuscript identifies these limits. Quoted interview text wasn't checked against audio.

The four S cells report the result of bounded searches. They don't establish ungrammaticality, usage rates, or an implication scale. The cline remains a hypothesis requiring matched judgments. No broader distributional study was added.
## Verification
The XeLaTeX/Biber build passes at **35 pages**, with no overfull or underfull boxes and no unresolved citations or cross-references. Existing font, fancyhdr, and microtype advisories remain. The native arm64 Biber binary was used because the installed wrapper's extraction failed; project tooling wasn't changed. Rendered pages containing both revised figures, the changed tables, the new existential examples, and the formal displays were inspected.

The fresh [reading copy](../notes/determinatives-as-nouns-review-2026-09-13-constraints.md) has eleven trees, seven tables, four formal displays, and 41 adjacent notes. Pandoc produced no warnings. Reference labels and all ten evidence URLs were checked. Both earlier annotated Markdown files remain byte-for-byte unchanged. Machine-readable checks are [here](./2026-09-13-implementation-checks.json).

The required house-style check was confined to assessing the changed material. Its remaining flags are pre-existing prose, paragraph-opening advisories, an emphatic full-form qualification in the table caption, and the incorrect suggestion to spell _unsupervised_ with a _z_. No further whole-manuscript polish pass was run. The computed sentence-length section follows verbatim.

```text
============================================================
SENTENCE LENGTH
============================================================

  --- determinatives-as-nouns.tex ---
    851 sentences | median 14 | mean 14.3 | middle half 10-18 (8 words)
         1-9  ###################       212   25%
       10-14  ########################  269   32%
       15-19  ##################        201   24%
       20-24  ##########                108   13%
       25-29  ####                       49    6%
       30-34  #                           7    1%
       35-39                              2    0%
         40+                              3    0%
```

Subsequent author corrections make the fusion branches vertical in Figures 4 and 6 and identify the extension of PP determiners to the alternative implementations as an extrapolation for this fragment. The matching reading-copy passage is updated. The PDF remains 35 pages; both diagrams and the revised §5.2 display were visually checked, and the build has no new warnings. The house-style check reports no new flags.

The author’s theoretical aim is now stated after the inventory: non-trivial implications could predict unexamined distributions and reduce independently stipulated permissions. The table explores one possible basis without establishing an implication scale or excluding patterns recoverable through other properties, finer constructions, or different methods. The added paragraph is synchronized in the reading copy; the 35-page build and its rendered page 9 pass. The style checker retains its existing advisories, including the paragraph-opening cadence advisory; no new violation was verified.
