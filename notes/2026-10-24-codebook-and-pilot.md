# Codebook and blind-coding pilot, 24 October 2026
<!-- SUMMARY: the codebook, column table, definitions, forms table, cell ledger, and blind coding of 24 Oct (pilot, wave 2, wave 3, and the y-to-m grading of the 2021 y cells), what each found, and what Brett decides first · status: for Brett · updated: 2026-10-24 -->

Brett asked, before leaving for about ninety minutes: "Write the code book and get started." This note is what happened, written to be read cold. Everything here is Claude's work (Claude Opus 5.5) unless a coder is named; nothing is committed.

## What exists now

- **The codebook**, `planning/codebook.md`. It sets out the rules agreed today:
  - y, m, n, with m kept for degraded acceptability only;
  - variety as a separate field, and a construction or reading that licenses a use as a frame;
  - "not applicable" and "unjudged" as statuses, not values;
  - every column as a possibility claim, the "must" columns reversed;
  - the absence of a property coded only where its presence can be obligatory, with three joint states (must, must not, either), not four;
  - frames open to blind coders and frozen before Brett judges;
  - merging only on logical entailment;
  - blind coding by several model families, and the analysis commitments.

  It ends with five forks for Brett.
- **The column table**, `analysis/codebook/columns.csv`: all 119 columns under 28 super-columns (115 at first; Brett's review added 4). Each row gives the type of claim (98 possibility claims, 10 facts of form, 6 "must" claims to reverse, 1 derived column, 1 analysis label, and 3 columns whose sense needs Brett's definition), the action, the absence partner where there is one, the frame treatment, and *CGEL*'s diagnostic polarity where *CGEL* states one.
- **Definitions**, `analysis/codebook/definitions.csv`: a plain definition with anchor examples for every column (87 sure, 22 with inferred senses, 3 depending on the gender fork, 3 unclear).
- **The forms table**, `analysis/codebook/forms.csv`: all 157 rows (the matrix's 139 plus 18 nouns and adjectives), each with a plain label for blind coders that carries no category name.
- **The cell ledger**, `analysis/cell-ledger/`. A builder merges every source into one row per cell with its provenance: Brett's 2021 cells (judged), the nine record-backed 2026-10 changes, the 19 proposed corrections, the 2026-10 added column, Claude's on-hold draft, and the blind coders' proposals. A quote checker rejects any quotation that isn't an exact match in its cited file. Because the coders' notes are raw model output, the ledger files built from them are gitignored until Brett decides.

## The pilot

Three coders worked independently on 35 forms and 18 columns: Codex (GPT-6.1 Sol), Muse Wonder 1.0, and a Claude subagent with no file access. The forms were 17 nouns and adjectives and 18 pronouns and determinatives. The columns covered the determiner in four frames, both "may take one" and "may lack one", plus gender, number, unstressed objects after a particle, pre-head adjectives, relatives, post-head adjectives, *-ly* adverbs, and partitives.

Each coder saw plain descriptions of the forms (*which*, interrogative, as in *Which book?*), never the matrix's category-bearing names or the hypothesis, and worked in an empty directory outside the repository. Raw outputs, the packet, the manifest, and the comparison are in `reviews/external-blind-coding-20261024-141034/` (gitignored).

**Agreement.** All three agree on 501 of the 630 cells. The splits concentrate in post-head adjectives, determiner-less argument uses, relatives, and the predicative and set-denoting frames.

**Calibration against Brett's 2021 cells.** The overlap is 108 cells: gender, number, the particle column, and partitives on the 18 pronoun and determinative forms. Codex matches 85, Muse 87, Claude 85.

- Gender accounts for 15 or 16 of each coder's mismatches. The pilot's packet defined gender by the pro-forms a form selects when it refers, so the coders gave *few*, *some*, *each*, and plural *they* personal and non-personal gender. The 2021 coding evidently treats gender as a contrast fixed in the word, which those forms lack. The mismatch therefore comes from the definitions, not from coder error, and the pilot's gender cells aren't evidence either way. (A side agent flagged the same point.) Wave 2 codes gender under both definitions.
- Leaving gender aside, the coders match the 2021 cells on 92 to 95% of what's left.
- The real disagreements are few: *this* and *these* as unstressed objects after a particle (coders y or m, 2021 n), *something* heading a partitive (coders n, 2021 y), and plural reference for *every* (coders not applicable, 2021 y).

**The determiner, by frame.** This is the most informative result so far. In the argument frame (subject, object, complement of a preposition), by majority of the three coders:

| Pattern | Forms |
|---|---|
| must take a determiner | *dog*, *lot*, *number*, *dozen*, *majority* (singular count common nouns) |
| either | *dogs*, *water*, *plenty*, *dozens*; and *few*, *many*, *all* |
| can't take one | *she*, *her*, *it*, *they*; and *some*, *each*, *this*, *these*, *someone*, *something*, interrogative *which* |
| neither (never heads alone) | *the*, *a*, *every* |

So in this frame the determinatives split. The quantifiers *few*, *many*, and *all* pattern with plural and non-count common nouns; the others pattern with the pronouns. The earlier desk count over the 2021 matrix found the same division by a different route (pronoun-like properties in the compounds, demonstratives, wh-forms, and *we*/*us*/*you* before a noun; determinative-only properties in the quantifiers). Two independent indications of one split is worth weighing before the structure review.

**One cell where Brett's data should overrule the coders.** All three give *some* an n for taking a determiner, but the COCA record has *the some will become the many* (*Foreign Affairs*, 1999) and *the some who say it* (*ABC Nightline*, 1990), in `corpus/exclusion_tests/2026-10-15-brett-supplied-an-each-the-some.md`. That makes it at least an m, licensed by a frame (a set already identified). The pass that maps corpus records onto cells is meant to catch exactly this.

**Frames the coders proposed.** Codex proposed 16 new frames or readings, Muse 4, and Claude 14; the codebook allows this until Brett freezes the list.
- **All three:** idiomatic and measure preposition phrases that are neither institutional nor means (*in all*, *in dozens*, *by water*, *food in plenty*).
- **Two of three:**
  - the generic bare singular (*Dog is man's best friend*: Codex, Muse);
  - a kinds or units reading of a non-count noun (*three waters*, *a water*: Codex, Muse), which is Brett's kinds reading (*thousands of fishes*);
  - a mass reading of a count noun (*We ate dog*: Codex, Claude);
  - post-head focusing *alone* (*She alone remained*: Codex, Claude);
  - names and pronouns in the set-denoting use with other dependents (*the young Kim*, *the Toronto that I remember*: Codex, Claude);
  - a characterizing use of a name or pronoun (*That outfit is remarkably Kim*: Codex, Claude);
  - metonymy of a place name (*Toronto elected a new mayor*: Codex, Claude).
- **One coder only:** among Claude's, headlines (*Dog bites man*, which is register and belongs in the variety field), bare coordination (*Rich and poor alike*), identifying as against describing *be* (*That's Kim*), and superlative-licensed partitives (*the tallest of them*).

The comparison file lists them all.

## Wave 2

The 18 reference rows, plus 8 pronoun and determinative forms for calibration, on the 89 remaining columns, in three packets, each coded by all three coders: nine runs. Gender is coded twice, by reference and as fixed in the word, so the fork can be settled without recoding. Parse with `python3 analysis/cell-ledger/parse_wave.py reviews/external-blind-coding-wave2-20261024` (gitignored).

**Interim, Codex and Muse only** (the three Claude coders were still running when this was added):
- **Calibration.** On the 8 pronoun and determinative forms, against Brett's 2021 cells, Codex matches 569 of 640 and Muse 537 of 615. One Muse row (*someone*, packet 1) had 31 values for 30 columns and is left out.
- **The mismatches are concentrated.** 16 of the 80 calibrated columns account for most of them; without those 16, the two coders match on 951 of 1,007 cells (94%).
  - Nine of the 16 are columns whose definition Claude had to infer: coordination with independent and dependent genitives, the determiner of a measure genitive (*a few days' time*), pro-form, genitive forms in the paradigm, coordination with other determiners, *else*/*more*, and attributive modifier.
  - Others are probably scope: Claude defined *not*, *at least*, and *quite* as modifying "it or the NP it heads". If the 2021 coding meant the word alone, the coders and the 2021 cells are answering different questions.
- So the calibration mainly shows where the codebook's definitions differ from Brett's 2021 senses. Those columns need Brett's definitions before the full run.

**Correction: the anchors leaked answers.** Some columns' definitions and anchor examples named forms that were being coded ("Yes: *she*", "No: *this*", "\**almost some*"), so on those cells the coders were partly handed the answer. A side agent flagged this as well. Recounted without those cells, wave 2's calibration is:

| Coder | Clean cells | Cells whose anchors named the form |
|---|---|---|
| Codex | 489 of 556 (88%) | 80 of 84 (95%) |
| Muse | 460 of 534 (86%) | 77 of 81 (95%) |
| Claude | 472 of 556 (85%) | 80 of 84 (95%) |

So the overall figures above are inflated by a point or two; the clean ones (85 to 88%, before the definition fixes) are the ones to use. The pilot had 6 such cells per coder. From wave 3 on, the packet maker screens out any anchor naming a form being coded. *A*, *I*, and *the* stay allowed inside definitions' examples, where they're rarely the form being illustrated, but are screened out of anchors. The few remaining cells where a definition still shows what *the* does (the definite column's *the dog*, and *quite the scholar* in the head rule) are excluded from calibration.

**m is underused.** Codex never used it (0 of 2,944 cells); Muse used it in 4% of cells and Claude in 5%; no cell is unanimous m; and Brett's 2021 matrix has 2 marginal cells in 21,545. Comparing m-coded new rows with near-binary old rows would turn a coding difference into an apparent category difference. Hence:
- **Wave 3**: the 20 columns Brett revised and the 4 he added, recoded blind on the new definitions, with a firmer instruction to use m.
- **The y-to-m pass**: Brett's 2021 y cells in the 62 columns whose definitions are settled (1,941 cells), graded y, m, or n by Muse and Claude.

The Claude coders in these two runs were file-reading subagents told to read their packet and nothing else. Their transcripts were checked afterwards: each read only its own packet.

## Wave 3 and the y-to-m pass (results)

**Wave 3.** All three coders agree on 448 of the 624 cells, fewer than in wave 2, as expected for the columns that needed revising. Codex used m this time (17 cells, against none before); Muse and Claude used it 61 times each. The most split columns are *hardly*, *more* after the form, *not*, pro-form, and *quite*. Raw outputs and the comparison are in `reviews/external-blind-coding-wave3-20261024/` (gitignored).

Calibration against the 2021 cells is weaker evidence here, because those cells answer the old definitions: Codex matches 122 of 155, Muse 119, Claude 129. More useful are the 12 cells where all three coders agree against the 2021 cell:
- **pro-form**: y for *each*, *few*, *some*, and *this*, against 2021 n. This is the miscoding Brett identified.
- **deictic**: n for interrogative *which*, as Brett proposed in his review.
- **non-count quantity** for *this*, **lower-bound *at least*** for *she*, and ***quite*** for *this*: n, against 2021 y. These follow from the revised definitions. The 2021 y for *she* is now covered by the focusing *at least* column, where all three give y.
- ***almost*** for *each*: all three m (*almost each day*), against 2021 n.
- *few* with *not*, with lower-bound *at least*, and in *in a few days' time*: all three y, against 2021 n. At least one coder took the label *few* to cover *a few*: Claude's note for *almost* tests *almost a few*. The 2021 matrix has *a few* as a separate row, so these three cells probably record *a few*. The blind label for *few* needs an example that excludes it (*Few people came*).

Two splits come from how the coders read headedness, not from the forms. In *a lot more people*, Codex and Muse count *more* as a dependent of *lot*, while Claude takes *a lot* to modify *more*, as *CGEL* does (ch. 5 §11, p. 432: *more* takes pre-head modifiers realized by an NP such as *a lot*). And in *A number were injured*, Claude counts *number* as a pro-form, while Codex and Muse treat the phrase as an NP with its *of* phrase left unexpressed.

**The y-to-m pass.** Muse and Claude graded all 1,941 of Brett's 2021 y cells in the 62 settled columns. Both said y for 1,478. Both said n for 112 and both m for 59. They split on the rest: m and y 157, n and y 74, m and n 61. Brett's short sheet is `reviews/external-ym-pass-20261024/YM-FOR-BRETT.md`, with only the decisions; the full listing is `YM-REVIEW.md` beside it (both gitignored, since they quote coder notes). The full listing sorts the flagged cells four ways:
1. **Sense questions** (80 of the 112 cells where both said n). They fall in nine columns, and within each column the coders reject the 2021 y for one shared reason, so the disagreement is over the column's meaning:
   - the three head-selection columns ("requires a plural head" and its two siblings). "Requires" fits every 2021 cell except the dependent genitives (*my*, *our*, *your*, *her*, *their*), determinative *what*, and *enough*. A "may take" reading would instead make the 2021 n for *the*, *all*, *any*, *some*, and *no* wrong;
   - non-affirmative and free choice, where 2021 has y for the wh-forms;
   - existential, where 2021 has y for *no*, *nobody*, *nothing*, and dummy *it*;
   - the two columns for following *twice* or *half*, where 2021 has y for *him*, *me*, and *them*;
   - combining with a count singular, where 2021 has y for the compound pronouns (*anyone*, *someone*) but n for *everyone*.

   For each, the sheet shows the 2021 y and n lists, the definition the coders saw, and a guess at the 2021 sense.
2. **Candidate 2021 slips**: the other 32 cells where both said n (for instance, dummy *it* coordinated with an NP, and *neither* as semantically plural).
3. **Candidate m's.** Of the 59 cells where both coders said m, both coders' notes cite register, variety, or rarity for 20, and one coder's note does for 16 more. By the codebook, register and variety are y with a variety note; rarity isn't on the scale. Of the 23 left, 8 are in meaning columns (*few* in the existential column, for instance), where m records a reading that can be cancelled, not a degraded one. That leaves 15 candidates for degraded acceptability, mostly wh-forms in coordination (*which and whose*). Across all grades, 124 of the 336 m's cite register or rarity (by a word list, so approximate). So m, as the coders use it, still often means something other than degradation.
4. **Splits**, listed in full.

One codebook defect came out of this: the four head-selection columns are "must" claims and had been typed as possibilities. They're now typed as claims to reverse into possibility form, as the two other "must" columns already were.

## What Brett decides first

Settled since this note was first written: gender is coded under both definitions and run as two arms of the analysis, and the *no*/*none* alternation is coded as inflection, with its own column as well.

1. **The nine sense questions** in the y-to-m sheet: what each column meant in 2021. Until then, its cells can't be judged or recoded.
2. **The m's that cite register or rarity**: whether to apply the codebook's rule mechanically (register and variety become y with a variety note; rarity becomes y). The sheet lists every such cell, so any of them can be overridden.
3. **The codebook's remaining forks** (section 11): whether to keep *multiple*, *countless*, and *poor*; the three columns whose sense can't be recovered (`proportional`, `distributive`, `joint`); and *oneself*, which is n for reflexive though it has the *-self* form.
4. **The frame list**: which proposed frames to admit before any cell is judged. Wave 3 added 26 proposals.
5. **Whether to grade the 2021 n cells as well** (6,676 cells in the same 62 columns). A side agent pointed out the imbalance: this pass let a 2021 y become m, but never a 2021 n, while the new rows can get m from either side.
6. **Whether to run the full blind coding.** The full run is the 18 reference rows on all columns (waves 2 and 3 cover most of this) plus the ten added columns for all 139 forms.

## Not done

- Mapping the corpus records onto cells.
- Regenerating the review sheet from the codebook.
- Rerunning the nine sense-question columns once Brett has said what each meant in 2021, and recoding *few* with a label that excludes *a few*.

The first two wait on the forks above.
