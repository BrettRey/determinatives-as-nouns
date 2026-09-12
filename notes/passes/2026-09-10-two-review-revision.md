# September 10: validation of the revision from two supplied reviews

The bounded revision is complete. The [decision record](../review-triage/2026-09-10-two-reviews.md) distinguishes adopted changes from reviewer suggestions that conflict with Brett's decisions or do not provide a valid comparative test. The [source diff](2026-09-10-two-review-source.diff) is against the snapshot immediately before this revision, rather than against the much older Git baseline.

## Source grounding

The added relative-clause comparison was checked against CGEL pp. 414 and 422–423. In particular, direct text extraction of the local PDF's printed p. 423 confirms that compounds admit ordinary relative clauses and PPs after a specialized restrictor. The constructed examples in the manuscript instantiate those described constructions; they are not presented as corpus attestations. The genitive *someone's book* was supplied in Brett's review material and is treated as a constructional parallel. The manuscript does not claim that CGEL explicitly derives this example, or that every determinative inflects for genitive.

The existing number contrast was rechecked against CGEL's number discussion and p. 418. The auxiliary qualification names non-modal auxiliaries and a constructed have/has/had paradigm, avoiding the reviewer's generalization of ordinary agreement across all modals. It retains the previously verified Pullum–Wilson citation for taxonomic inclusion, without inventing a new page-specific attribution of their argument.

The earlier [adjective source record](2026-09-10-adjective-discussion.md) preserves direct checks of the Henrietta example, Stanford attestation and Lipsey–Lancaster argument. These sources remain in the compressed discussion. The DP contrast retains the existing, verified Abney citation. No reference entries were added or altered.

Glossa's original [publisher PDF](https://www.glossa-journal.org/article/5263/galley/12814/download/) confirms the journal and Bruening article metadata. Title casing is a local display normalization of the journal subtitle for the reference list; the original title is otherwise unchanged. Biber's generated entry and the final PDF both read *Glossa: A Journal of General Linguistics*. The two mixed page locators now render “p. 75, n. 3” and “p. 582, (13d)”. The second-best citation is no longer followed by a misplaced possessive.

## Build and preservation

The full serial XeLaTeX/Biber build passes. The article remains 24 pages with 24 citation keys, all resolved. There are no LaTeX errors, unresolved references or citations, Biber warnings/errors, or rerun requests. Six figures and eleven trees remain; all tree source blocks are byte-identical. Of the five tables, only Table 2 changed. All 31 protected analysis and supplement files are unchanged; the local bibliography is also unchanged.

The expanded table's initial overfull label was corrected by adjusting its column widths. No new overfull lines remain. Three pre-existing small overfull lines remain (4.46857, 5.04185 and 4.2891 pt), along with the earlier font-substitution, header and microtype advisories. This is a successful working-draft build, not a claim of completed visual production proofing.

Figure 1 now floats onto page 3; page 2 contains 523 extracted words rather than the reported sparse page. PDF text geometry confirms separate someone / and / everybody tokens on page 14, with a 1.76 pt gap before and. The narrow visual spacing remains a production question; no global mention-macro change was made. No images were opened, as Brett requested.

The revised prose, table, footnotes and reference list were checked in the extracted PDF text. The unresolved shirts judgment has been removed from the article and remains preserved in the pre-edit snapshot and earlier research note. Both countercases and the second-best mention remain. Git whitespace checking passes, and the untracked master source has no trailing whitespace. The [machine-readable check](2026-09-10-two-review-check.json) records the final hashes and checks.

## Local style check

The linter's alerts were inspected against the changed source. The remaining therefore uses express inferences and are permitted by the standing author instruction. The mathematical subscript is math notation, not a house-style prose violation. The table/comparison passages marked as contrasts express the actual analytical contrasts. The repeated opening alert mostly concerns definitions or explicit shifts of analytical level. No mechanical rhythm rewrite was applied.

This is local verification of the authorized revision, not a fresh completion of all whole-manuscript passes. The central bibliography, empirical results and submission packages were not changed. No new review board, commit, push or submission was performed.

## Computed sentence lengths

```text
SENTENCE LENGTH
============================================================

  --- determinatives-as-nouns.tex ---
    520 sentences | median 14 | mean 14.9 | middle half 10-19 (9 words)
         1-9  ####################      123   24%
       10-14  ########################  146   28%
       15-19  ########################  144   28%
       20-24  ##########                 63   12%
       25-29  #####                      29    6%
       30-34  ##                         10    2%
       35-39                              1    0%
         40+  #                           4    1%
    [advisory] 60% of sentences fall in 12-26 words; the band is narrow, so check whether the rhythm has flattened
```
