# Matrix 2026-10, stage 1: what needs Brett
<!-- SUMMARY: review sheet for the stage-1 update of the 2021 determinative–pronoun matrix; the corpus-linked changes are built (matrix-2026-10.csv, CHANGELOG.md), and the rest is held until there's corpus evidence or Brett's judgments · status: partly applied · updated: 2026-10-23 -->

**Update, 23 October.** Brett: changes to the matrix must be linked to specific corpus evidence, and he's not offering judgments now. So `build_matrix.py` applied only the corpus-linked corrections:
- *either*, *neither*, *each*, and *two* take the genitive;
- *many* takes the genitive, marginally;
- *every* stands alone, marginally;
- *everybody*, *everyone*, and *somebody* take *poor/lucky/silly*.

It also added a *whomever* row. The other items below are held, along with both new features. See `CHANGELOG.md`.

The proposals are in `corrections.csv`, `new_features.csv`, and `new_feature_values.csv` in this folder. The subagent's report is in `REPORT.md`, saved verbatim. The public 155-feature file is unchanged.

Claude checked two sources against the records: the *either's* and *each's* judgments quoted from the 17 October genitive record, and CGEL p. 430 on *lucky*/*poor*/*silly* with the core personal pronouns. Both match.

## 1. Corrections ready to apply

These have a record plus your recorded judgment, or a CGEL page.

| Form | Feature | 2021 → 2026 | Source |
|---|---|---|---|
| *either* | genitive *'s* | n → y | 17 of 30 COCA lines; you, 17 Oct: "all strike me as perfectly fine" |
| *neither* | genitive *'s* | n → y | 6 of 23 COCA lines, judged fine |
| *each* | genitive *'s* | n → y | 12 of 12 COCA lines; you: "those three each's seem fine to me" |
| *everybody* | *poor/lucky/silly* | n → y | *Poor Val. Poor everybody.* (*New Yorker*), NOW and iWeb lines; you, 21 Oct |
| *somebody* | *poor/lucky/silly* | n → y | you, 21 Oct; Anstey 1884; Binchy 1996 |
| *us* (pronoun) | *poor/lucky/silly* | n → y | CGEL p. 430: the construction goes with "the core personal pronouns"; *me*, *you*, *him*, *her*, and *them* are already y |

**Q1.** Apply all six? (yes / list exceptions)

## 2. Corrections to decide

1. ***everyone***, *poor/lucky/silly* n → y. Attested (*Lucky you. Lucky everyone.*, *Everwood*), but there's no judgment of yours on record. *Lucky everyone!* is fine for you?
2. ***someone***, *poor/lucky/silly* n → y. No line in any corpus; only the analogy with *somebody* (CGEL p. 423 calls ·*body* and ·*one* "wholly equivalent"). *Poor someone!*?
3. ***it***, *poor/lucky/silly* n → y. CGEL p. 430's wording covers the core personal pronouns, but *Poor it!* is odd. Keep n?
4. ***many***, genitive n → marginal. 3 of 76 COCA lines, all web; you found two fine (*to many's surprise*, *out of so many's reach*).
5. ***two***, genitive n → y. *the two's* in 21 of 34 COCA lines, but always after a determiner. Does that count for this feature, which in 2021 seems to be about the word heading the NP?
6. ***every***, standing alone n → marginal. Two published NOW lines (*Every has a story*, *Patch* 2025; *Every has different blocking mechanics*, *Guardian* 2024), both anaphoric with the *each* reading.
7. ***little***, pre-head modifier n → y. CGEL p. 393: *the little money that remains*. *few* and *many* are already y.
8. ***little***, attributive modifier n → y, and 9. ***much***, attributive modifier y → n. The 2021 matrix has no codebook separating "pre-head modifier in nominal" from "attributive modifier in nominal". What was the difference?
10–12. ***sufficient***: standing alone n → y; both modifier features y → n. CGEL p. 397 says *sufficient* occurs "only as determiner … (or fused determiner-head)". But the 2021 y may have coded the adjective (*a sufficient number*). Which did you mean?
13. ***whosoever***, nominative n → y. 30 tokens with a subject gap in the 17 Oct *whoever* counts, never read line by line.

## 3. The new feature that's ready: heading a nominal after a determiner

This means heading a nominal after a separate determiner while keeping the word's own quantity, number, or ordinal meaning: *the few*, *the many*, *the little that remains*, %*the both of us*, *the last twice*, *the some who*. It's CGEL's fused modifier–head with a determinative, or ordinary Head's determinative heading a nominal after a determiner.

It parts from the 2021 modifier features at eight sourced words. *every* and *various* modify without heading. *both*, *some*, *all*, and *twice* head without a modifier use. *little* and *sufficient* are the other two. Its 97 "n" cells include 56 pronouns, all from CGEL p. 429 ("do not permit determiners"); see design choice D below.

These 30 cells need you.

**Q3a. Proposed n, with no source** (Claude's reasoning). Agree, or flag any that should be y or marginal:
*another*, *certain*, *each*, *either*, *neither*, *none*, *somewhat*, *that*, *these*, *this*, *those*, interrogative *which* and *whichever*, *a great many*, *less*, *more*.

**Q3b. Proposed y, with no source:**
- *least* (*the least I can do*)
- *most* (*the most I can say*)

Are these the use, keeping the word's quantity meaning after *the*?

**Q3c. Proposed marginal:**
- *all* (*the all of me that's broken*, 3 lines)
- *both* (CGEL's %*the both of us*)
- *some* (5 clear COCA lines, *the some will become the many*)
- *twice* (*the last twice*, NOW, mostly British and Irish racing reports)
- *fewer*, *fewest*, *several* (CGEL pp. 415–416's general licence only)

**Q3d. Proposed n, from CGEL:**
- *a few* and *a little* (p. 393: "cannot occur as modifiers")
- *something* (p. 423)

**Q3e. Left blank:**
- *thrice* (one NOW token of *the last thrice*, not read)
- the zero determinative (doubtful)

## 4. Design choices

**A. A third value.** Some cells are graded: web-only, one edited line, marginal. Code them "marginal" and run the analyses with marginal counted as y, then as n? Recommended: yes.

**B. Varieties.** *the both of us* (CGEL's %) and *the last twice* (British and Irish racing) are found only in some varieties. Code them "marginal", or give them a fourth value? Recommended: "marginal", with a note.

**C. The secondary-use feature isn't ready.** For *a he or a she*, *two mes*, *a new everything*, and the rest, 88 of 138 cells have no source, so 64% would be guesses. The records reach *he*, *she*, *me*, *you*, *him*, *us*, singular *they*, and the compounds, with negative results for *each*, *some*, *all*, *any*, *enough*, *much*, *once*, and *twice*. They reach none of the reflexives, the genitives, the *wh*-forms, *I*, *we*, *it*, the temporal pronouns, or most simple determinatives. The options:
- (a) leave it out of stage 1;
- (b) you judge the 88 cells, about 20 minutes with a frame such as *a ___* or *two ___s* in a descriptive sense;
- (c) split it into two formal features, plural *-s* and heading after any determiner, which leaves the same gap for pronouns.

Recommended: (a) now, and (b) if the category paper wants it.

**D. Pronouns on the determiner feature.** All 56 pronoun cells are n by definition, from CGEL p. 429. Yet COCA has 350 tokens of *the real me*. That's a secondary use, not the feature's use, so it belongs to feature C. Without C, the matrix says pronouns never head after a determiner. That's another reason to do (b) eventually.

**E. Rejected candidates** (the subagent's reasons; Claude agrees):
- A restrictive adjective requiring a determiner. *instant everything* has an adjective and no determiner, so *everything* would need two values. The feature also repeats C and the determiner feature.
- A bare group use. Only *few* is sourced. Your *Few were the hangers-on* judgment is noted on the *few* row instead.

**F. Missing row.** The matrix has no *whomever*, though the October records count it. Add it?
