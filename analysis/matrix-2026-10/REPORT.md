<!-- Saved verbatim by the parent session (Claude Opus 5.5), 2026-10-23, from the stage-1 subagent's final message (Agent tool, general-purpose). -->

## Matrix 2026-10, stage 1: what I found

I've written the three files. Stage 1 comes out uneven. The corrections and one new feature are ready for review. The secondary-use feature isn't: records reach only a minority of the forms. No responsibility notice is needed.

**Counts**
- **Corrections:** 19 rows, 13 needing Brett.
  - By source type: record+brett 5, record 3, CGEL 2, brett 1, suspected 8.
  - Three rows (the `sufficient` cells) come from CGEL alone, not from the 2026 records.
  - Proposed values: 13 to y, 3 to n, 2 to marginal (many's, every as fused head). The y→n rows are the much and sufficient modifier cells; the n→y rows include sufficient as fused head.
- **New features:** two delivered, two rejected.
  - `heads_nominal_after_separate_determiner` is ready. 20 of its 138 cells (14%) are Claude proposals or blank, and 30 need Brett.
  - `secondary_set_denoting_use` is not ready. 88 of its cells (64%) have no source and are left blank, not guessed. 105 need Brett.
- **Source-type tokens beyond the brief's four:**
  - `suspected`: I think the cell is wrong but can't source it.
  - `na_rule`: the cell is NA under the stated policy.
  - `none`: blank, with nothing found.
  - Combined types such as `record+brett`.

**Most sure (corrections)**
1. `either` genitive n→y: 17 of 30 COCA lines; Brett, 17 Oct: "all strike me as perfectly fine".
2. `neither` genitive n→y: 6 of 23 lines, judged fine.
3. `each` genitive n→y: 12 of 12 lines; "those three each's seem fine to me". This goes against CGEL p. 420's "of somewhat questionable status".
4. `everybody` poor/lucky/silly n→y: *Poor Val. Poor everybody.* (*New Yorker*, 2005) plus NOW and iWeb lines. Brett, 21 Oct: *Poor everybody!* is "in".
5. `us_pron` poor/lucky/silly n→y: CGEL p. 430 (checked) gives the construction to "the core personal pronouns" in "accusative or plain case".
6. `little` pre-head modifier n→y: CGEL p. 393, *the little money that remains*. `few` and `many` are already y there.
7. `somebody` poor/lucky/silly n→y. This rests on Brett's 21 Oct judgment plus Anstey (1884) and Binchy (*Irish Times*, 1996). COCA, NOW and iWeb have no line with *somebody* in the exclamation.

**Least sure**
1. The three `sufficient` rows (fused head n→y; both modifier features y→n). CGEL p. 397 says sufficient occurs "only as determiner ... (or fused determiner-head)". But the 2021 y may be coding the adjective (*a sufficient number*).
2. `whosoever` nominative n→y: 30 subject-gap tokens, never read.
3. `it_plain` and `someone` poor/lucky/silly. `it_plain` rests on CGEL's general wording. For `someone` there's only analogy, and all three corpora returned no *someone* line.
4. `much` attributive modifier y→n and `little` attributive modifier n→y. The 2021 matrix has no codebook, so nothing separates `prehead_modifier` from `attrib_modifier`.
5. `two_det` genitive n→y. *The two's* is 21 of 34 COCA lines, but only after a determiner. Whether that counts for the feature is Brett's call.
6. `every` fused head n→marginal (not used up by the two lists above). It rests on two NOW lines that check out on their publication pages (*Patch* 2025, *Guardian* 2024), plus COCA reply fragments and coordinations like *any and every*.

**Where the evidence contradicts the brief**
- **Somes and the some don't belong under (i).**
  - The somes record calls the coinage "a conversion from an answer label, not the secondary use".
  - The an-each/the-some record says *the some* is "the pattern of *the few* and *the many*, not the article-plus-description secondary use". The same record also calls these lines "set-denoting", which may explain the brief's grouping.
  - I coded `some` n on the secondary-use feature and marginal on the determiner feature. The *the some* readings are Claude's, not yet Brett's.
- **CGEL p. 416 is too strict on few and many.** It says they're "hardly admissible unless accompanied by a following modifier". The 321 COCA lines of an adjective before *few* with no noun go against that.
- **The known examples:**
  - The poor/lucky/silly, genitive and `every` examples check out. The 17 Oct edited-prose claim holds through the 16 Oct batch's counts (each 5, either 6, neither 2).
  - *Poor somebody!* is attested only outside COCA, NOW and iWeb.
  - Both and all aren't corrected: only partitives are attested (*Poor all of us*, *lucky both of us*), and Brett starred the bare forms.
- **(iii), restrictive adjective requiring a determiner: rejected.**
  - *Instant everything* (16 of 195 lines) has an adjective and no determiner, so `everything` can't be coded with two values.
  - Elsewhere it repeats (i) and (ii), which would double-count one fact in a distance analysis.
  - It rests on single Brett judgments: *Real us*, *Lucky few*, *Lucky hundred*, *Poor many*.
- **(iv), bare group use: rejected.** Only `few` is sourced (Brett, 23 Oct: *Few were the hangers-on* can't mean "the small group were"). That judgment is recorded as a note on the `few` row of the determiner feature.

**The two delivered features**
- **`heads_nominal_after_separate_determiner`** means heading a nominal after a determiner while keeping the word's own quantity or number meaning (CGEL's fused modifier-head).
  - It diverges from the 2021 modifier features at eight sourced words. Every and various modify without heading (CGEL p. 416). Both, some, all and twice head without a modifier use. Little heads but is n on both 2021 modifier features. Sufficient follows CGEL p. 397. That's why it isn't redundant.
  - Caveat for Brett: 56 of its 97 n cells come from one CGEL sentence (p. 429, pronouns "do not permit determiners"). By definition a pronoun can't score y. Without the second feature, the matrix would wrongly say pronouns never head after a determiner (COCA has 350 tokens of *the real me*).
  - Twice (the last twice is mostly British and Irish racing reports) and both (CGEL's %) are coded marginal. Brett may want a value for "found only in some varieties".
- **`secondary_set_denoting_use`**: sourced for he, she, me, you, him, us, singular they and the compounds, with negative results for each, some, all, any, enough, much, once and twice.
  - Nothing reaches the reflexives, the genitives, the wh-forms, I, we, it, the temporal pronouns, or most simple determinatives.
  - The criterion is semantic. A purely formal alternative would split it into "takes plural -s" and "heads after any determiner". The formal version has the same coverage gap for pronouns.

**NA policy.** NA means the form never heads a nominal, not that nobody looked. It covers 24 forms:
- determinatives coded n in 2021 on both `functions_as_fused_determiner_head` and `functions_as_head_of_partitive_construction` (a, the, no, many_a, last, next, such, a_certain, us/we/you_det, what/whatever/which_rel/whichever_rel_det);
- the dependent genitive pronouns (my, your ×2, her_dep, its, our, their ×2, one_s).

`every` isn't NA, because CGEL discusses it explicitly.

**Other items**
- **Restrictor candidate for stage 2:** "takes a single post-head adjective", as in *someone interesting*. It's only half-sourced:
  - The compounds are covered by CGEL p. 423.
  - Brett's 19 Oct judgments put all, much and little on one side and few, some and none on the other.
  - CGEL gives no post-head adjectives for personal pronouns.
- **Missing form:** the matrix has no *whomever* row, though the 17–18 Oct records count it.
- **Confirmed, no change:** every partitive stays n (Brett judged all 67 lines bad). The genitive stays n for once, twice, thrice, few, all and some (one web line, which Brett found questionable). *Very* + every/some/this stays n.

**Records read**
- **In full:** all the dated records from 4–19 Oct except those listed under "skimmed" below, plus every-reading, readings and log.
- **Skimmed** (only the first part, or the SUMMARY line; no matrix forms): whoever-whomever, whenever-suits, superlative-plurals, some-educated, these-rich, scant-ever, bare-material-nouns, partly-material-nouns, the two the-below records, the-in-off-under, whoever-gaps-and-matrix.
- **Grepped only:** HAND-GATHER.
- **Also used:** DECISIONS.md 2026-10-15 to 10-23, the fusion paper's EVIDENCE.md, and fusion drafts mod-head.tex and det-head.tex. CGEL pp. 377, 393, 397, 413, 415–416, 420, 423, 426, 429 and 430 were checked against the PDF.
- **Not read directly:** `corpus/genitive/` and `corpus/premodification/` were outside the authorized list. I used them only through the DECISIONS.md and EVIDENCE.md rows that summarise them; `two_det` depends on this.

Paths in the CSVs are project-relative; fusion-repo paths start at `papers/`. The generator script is in my scratchpad, not the repo.

Files are in /Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/determinatives-as-nouns/analysis/matrix-2026-10/:
- corrections.csv
- new_features.csv
- new_feature_values.csv
