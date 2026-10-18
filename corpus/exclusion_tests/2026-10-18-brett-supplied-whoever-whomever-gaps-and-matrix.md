# *Whoever* / *whomever*: the gap audit and the matrix-subject cells (18 Oct 2026)
<!-- SUMMARY: KWIC follow-up to the 17 Oct case counts. (1) Gap audit of the after-preposition, before-pronoun row: nearly all tokens have a non-subject gap; removing embedded subjects, predicatives and clause-subject tokens raises the whomever share from 49% to about 52%. (2) Sentence-initial cells, with Brett's totals: as main-clause subject, whomever is 8 of about 51 tokens with a non-subject gap (about 16%) and 32 of about 2,100 with a subject gap (under 2%). Four cells: both functions accusative about 52%, both nominative under 2%, the two clashes 14% and about 16% · status: record; labels Claude's, checked by Brett · updated: 2026-10-18 -->

**Source.** COCA, six KWIC searches run by hand by Brett Reynolds on 18 October 2026, after the external reviews of the structural paper (GPT Pro's points 4 and 5). The query strings are confirmed from Brett's english-corpora.org search history (all dated 18 October 2026). The raw lines, labels, scripts, and a manifest with hashes are kept privately in the fusion repo (`reviews/corpus-case-adj-20261018/`, gitignored). Labels by Claude (Opus 5.5), one pass, reading each line; counts computed by script from the labels.

| Set | Query | Lines | Coverage |
|---|---|---|---|
| A1 | `[i*] whomever [p*]` | 198 | display of 430 tokens (395 + 35 with *it*, 17 Oct counts) |
| A2 | `[i*] whoever [p*]` | 199 | display of 552 tokens (407 + 145 with *it*) |
| B1 | `. whomever [p*]` | 23 | all hits |
| B2 | `. whoever [p*]` | 498 | 500-line sample of 644 hits |
| B3 | `. whomever [v*]` | 42 | all hits |
| B4 | `. whoever [v*]` | 500 | 500-line sample of 2,606 hits |

The displays run from 2019 back to 1990 with the 2012 web and blog block in place, so they look like samples across the corpus, not the first hits.

## 1. The gap audit (after a preposition, before a pronoun)

The 17 Oct row (395 *whomever* / 802, 49%) came from frequency lists, so the gap was never seen. GPT Pro's worry: some tokens have an embedded-subject gap (*with whomever she thinks is right*). Labels: NS (non-subject gap: object, stranded preposition, embedded non-subject, elided complement), ES (embedded subject), PR (predicative complement), MN (the [i*] word introduces a clause, as *until*, *before*, *till*, *like*, and the fused relative is that clause's subject: *until whoever you're waiting for gets here*), X (metalinguistic, garbled).

| Lines with a pronoun other than *it* | NS | ES | PR | MN | X |
|---|---|---|---|---|---|
| *whomever* (A1, 182) | 181 | 1 | 0 | 0 | 0 |
| *whoever* (A2, 148) | 131 | 4 | 7 | 5 | 1 |

Applying each sample's NS proportion to the 17 Oct counts gives about 393 *whomever* and 360 *whoever* with a clean non-subject gap: **about 52%**, against 49% before the audit. So the 49% is conservative, as GPT Pro guessed, but not because of embedded subjects. They're rare (5 of 330 lines), and they go mostly with *whoever* (4 of 5), as subject gaps do. What *whoever* has and *whomever* lacks is predicative gaps (*with whoever she is*) and clause-subject tokens.

The *it* row (17 Oct: 35 *whomever* / 180, "mixed") splits as expected. Non-subject gaps (*spy on whomever it wants*) are 10 of 16 *whomever* lines and 4 of 51 *whoever* lines, about two-thirds *whomever* by the same estimate. Two of the ten are *to whomever it may concern*. Predicative gaps (*with whoever it was*) are 5 of 16 and 42 of 51, about 8%.

Line labels (A1): ES 111; PR 15, 35, 51, 129, 185; X 30 (metalinguistic); the rest NS. (A2): ES 17, 36, 91, 129, 133; PR 7, 8, 63, 70, 140, 185, 197 and the *it* lines except 100, 102, 135, 146 (NS); MN 29, 43, 48, 83, 121, 153, 177, 181, 196; X 23 (truncated).

## 2. The sentence-initial cells (the fused relative as main-clause subject)

The 17 Oct record said the matrix function's effect "rests on CGEL's judgment of *?Whomever he marries will have to be very tolerant*". A sentence-initial fused relative is usually the main-clause subject (MS): *Whomever I chose for this experiment should be close to the mean* (*Southern Review*, 2015). It can also be an exhaustive conditional or a left-dislocated phrase with a resumptive (EC): *Whomever we hire, we will have to keep a very close eye on them*. CGEL treats the conditional as an interrogative clause (p. 1072 n. 15), not a fused relative. Other labels: FRAG (fragment), TOP (topicalized object), Q (*Whoever heard of …?*, interrogative *who ever*), X.

| Gap | Label | *whomever* (all hits) | *whoever* in the sample | *whoever*, estimated total | *whomever* share |
|---|---|---|---|---|---|
| non-subject | MS | 8 | 33 of 498 | 43 | about 16% |
| non-subject | EC + FRAG | 9 | 61 of 498 | 79 | about 10% |
| subject | MS | 32 | 400 of 500 | 2,085 | under 2% |
| subject | EC | 7 | 60 of 500 | 313 | about 2% |
| predicative | all | 6 | 394 of 498 | 510 | about 1% |

The *whoever* totals scale the sample counts by the frequency-list totals (644 and 2,606). With a non-subject gap, *whomever* is about half the tokens after a preposition (52%) and about a sixth where the fused relative is the main-clause subject (8 of about 51). So the matrix function shows in usage too, not only in CGEL's judgment.

Read with the 17 Oct counts, the four cells are:

| | subject gap | non-subject gap |
|---|---|---|
| object of a preposition | 14% (352 / 2,458) | about 52% |
| main-clause subject | under 2% (32 / about 2,100) | about 16% (8 / about 51) |

Both functions move the form, by similar amounts. Where both call for accusative, *whomever* is about half; where both call for nominative, under 2%; and the two clashes come out alike, 14% and about 16%. That's the double requirement fusion states (CGEL p. 1073), as a preference, with neither function winning a clash. The smallest cell has only 8 *whomever* tokens, so its share is rough; the ordering of the four cells is what the counts support.

The EC row (no main-clause function, non-subject gap) is low, about 10%. That fits CGEL's interrogative analysis of the conditional, since interrogative *whom* is rare in usage too, but the row isn't a clean "internal function only" cell.

Line labels: B1 (after Brett's check) MS 1, 3, 9, 10, 11, 14, 16, 17; EC with a non-subject gap 2, 4, 5, 6, 7, 8, 18, 22, 23; EC with a predicative gap 12, 13, 15, 19, 20, 21 (7, 13, 18, and 21 are fragments). B3 EC 2, 18, 25, 29, 31, 36, 37; X 1 (genitive *whomever's*), 7 (garbled), 35 (truncated); the rest MS. B2 and B4 labels are in the private run (`labels_case.py`).

## Caveats

- Labels by Claude, one pass, then checked by Brett Reynolds on 18 October 2026 on 106 lines: all 23 B1 lines, the 24 hard calls in A1 and A2 (ES, PR, MN, X), a random 30 from B2 and B3, and 28 lines from the 17 Oct genitive set. He changed five B1 labels, all to EC (4 fragments he reads as exhaustive conditionals, and l. 5, which Claude had excluded), and agreed with the other 101. None of the changes touches the main-clause-subject cell (8 against 33) or the 52% estimate.
- The before-pronoun estimates assume the displays are representative of the frequency-list rows.
- Sentence-initial position catches main-clause subjects but also headings, quotations (Bible and Tao Te Ching lines in B3 and B4), and scripts; these are kept, labelled by function.

**Totals (Brett, 18 Oct):** `. whoever [p*]` 644 (it 219, you 166, he 108, they 67, she 45, I 28, we 10, who 1); `. whoever [v*]` 2,606 (448 verb types). Raw lists in the private run (`raw/G1…`, `raw/G2…`).
