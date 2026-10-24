# *Whoever* / *whomever*: the gap audit, the matrix-subject and verb-object cells, and register (18 Oct 2026)
<!-- SUMMARY: KWIC follow-up to the 17 Oct case counts. (1) Gap audit of the after-preposition, before-pronoun row: removing embedded subjects, predicatives and clause-subject tokens raises the whomever share from 49% to about 52%. (2) Sentence-initial cells: as main-clause subject, whomever is 8 of about 51 with a non-subject gap (about 16%) and 32 of about 2,100 with a subject gap (under 2%). (3) Object of a lexical verb: about 37% with a non-subject gap, 6% with a subject gap; content-clause subjects replicate the main-clause cells (about 2%). In both gap columns: preposition > verb > subject. (4) Register: the same order inside speech/scripts and inside writing · status: record; labels Claude's, checked by Brett · updated: 2026-10-18 -->

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

Both functions move the form, by similar amounts. Where both call for accusative, *whomever* is about half; where both call for nominative, under 2%; and the two clashes come out alike, 14% and about 16%. That's the double requirement fusion states (CGEL p. 1073), as a preference, with neither function winning a clash. The smallest cell has only 8 *whomever* tokens, so its share is rough; the ordering of the four cells is what the counts support. (Section 3 below adds the object of a verb: the first clash is lower there, 6%, so "alike" holds for prepositions only.)

The EC row (no main-clause function, non-subject gap) is low, about 10%. That fits CGEL's interrogative analysis of the conditional, since interrogative *whom* is rare in usage too, but the row isn't a clean "internal function only" cell.

Line labels: B1 (after Brett's check) MS 1, 3, 9, 10, 11, 14, 16, 17; EC with a non-subject gap 2, 4, 5, 6, 7, 8, 18, 22, 23; EC with a predicative gap 12, 13, 15, 19, 20, 21 (7, 13, 18, and 21 are fragments). B3 EC 2, 18, 25, 29, 31, 36, 37; X 1 (genitive *whomever's*), 7 (garbled), 35 (truncated); the rest MS. B2 and B4 labels are in the private run (`labels_case.py`).

## 3. The verb-object cells (the fused relative as object of a lexical verb)

Four more COCA KWIC searches, run by hand by Brett Reynolds on 18 October 2026 after the second-round reviews of the structural paper (Fable: is the matrix function's effect only an effect of prepositions?). The query strings are as Claude requested them; they aren't yet confirmed from Brett's search history. Raw lines, labels (`labels_vo.py`), script (`tally_vo.py`, output `tally_vo.json`), and hashes are in the same private run.

| Set | Query | Lines | Total (frequency list or chart) |
|---|---|---|---|
| J1 | `[vv*] whomever [p*]` | 199 (l. 77 not in the paste) | 227 (*it* 14) |
| J2 | `[vv*] whoever [p*]` | 199 (l. 79 not in the paste) | 555 (*it* 119) |
| J3 | `[vv*] whomever [v*]` | 71 | 71 (all hits) |
| J4 | `[vv*] whoever [v*]` | 200 | 1,372 (genre chart) |

The chart was pasted without its query; it's taken to belong to J4 from its place in the paste, and the J4 sample's genre mix matches it within three points on every genre (fiction 20% against 17%, the largest gap).

Labels (Claude, one pass, every line read; checked by Brett Reynolds on 18 October 2026, who found them good and changed none). NS: object of the verb, non-subject gap, including indirect objects and the object of a catenative (*let whomever I was taking home that night buy me*). VS: object of the verb, subject gap. PR: predicative gap, clefts included (*find whoever it is you're looking for*). ES: embedded subject. CC: the fused relative is the subject of the verb's content-clause complement (*I think whoever did this to her wants to slow down her maturity*), split by gap as CCN, CCP, CCS. EC, MP (*become whoever …*), X (metalinguistic; vocative *Miss whomever you are*; genitive *whoever's*; *whomever* with no relative clause, as in *making whomever sleep*).

| Label | J1 *whomever* | J2 *whoever* | | Label | J3 *whomever* | J4 *whoever* |
|---|---|---|---|---|---|---|
| NS | 187 | 123 | | VS | 60 | 132 |
| PR | 7 | 42 | | CCS | 9 | 57 |
| CCN | 1 | 8 | | EC | 0 | 4 |
| CCP | 0 | 9 | | X | 2 | 7 |
| ES, EC, MP, X | 2, 0, 0, 2 | 2, 11, 3, 1 | | | | |

Line labels. J1: PR 1, 18, 50, 88, 126, 130, 194; ES 100, 151; CCN 102; X 11, 36; the rest NS. J2: PR 1, 5, 6, 9, 10, 11, 16, 21, 40, 43, 44, 48, 49, 53, 69, 88, 91, 94, 96, 101, 103, 107, 110, 112, 114, 115, 116, 121, 129, 133, 138, 148, 153, 159, 171, 181, 184, 185, 188, 194, 197, 198; CCP 2, 18, 24, 87, 108, 150, 160, 186, 195; CCN 12, 27, 46, 55, 85, 90, 95, 173; EC 4, 14, 22, 23, 71, 80, 155, 177, 179, 193, 200; ES 73, 86; MP 144, 192, 196; X 72; the rest NS. J3: CCS 3, 14, 24, 29, 33, 35, 39, 43, 61; X 15, 53; the rest VS. J4: CCS 2, 3, 5, 10, 11, 17, 24, 29, 30, 36, 38, 40, 41, 44, 51, 66, 67, 70, 71, 74, 79, 89, 90, 92, 94, 95, 96, 97, 101, 102, 111, 114, 123, 124, 127, 131, 134, 135, 146, 149, 150, 152, 155, 162, 163, 170, 173, 175, 179, 180, 182, 188, 190, 194, 195, 197, 199; EC 61, 122, 129, 167; X 9, 43, 64, 113, 115, 119, 148; the rest VS.

Estimates scale each sample's proportion to the query total, as in §§1–2. The non-subject cell uses lines with a pronoun other than *it*, as the 52% did: about 206 *whomever* and 356 *whoever*, **about 37%** (38% with the *it* lines). The subject cell: 60 *whomever* against about 906 *whoever*, **6%**. Unlabelled ratios would mislead here: 29% before a pronoun and 5% before a verb, because verbs of thinking and saying take clauses whose subject is the fused relative (57 of the 200 *whoever* lines before a verb).

The content-clause tokens replicate the main-clause-subject cells. With a subject gap (both functions nominative), *whomever* is 9 against about 391 (about 2%, against under 2% as main-clause subject). With a non-subject gap there's one *whomever* line (*I guarantee whomever you're into actually sucks*) against 8 *whoever* lines in the sample, too few for a share.

The six cells:

| | subject gap | non-subject gap |
|---|---|---|
| object of a preposition | 14% (352 / 2,458) | about 52% (393 / 753) |
| object of a verb | 6% (60 / about 970) | about 37% (206 / 562) |
| main-clause subject | under 2% (32 / about 2,100) | about 16% (8 / about 51) |

In both columns the order is preposition, verb, subject. Prepositions and verbs both call for accusative, so the step between those rows isn't one of matrix function; in writing alone it narrows to 65% against 58% (§4), so part of it is register. (An earlier version of this sentence cited CGEL p. 465, "the accusative is normally the only option"; that remark is about a fronted preposition, and CGEL adds that where the preposition phrase is post-verbal, as in these tokens, *who* "is acceptable in informal style" (pp. 465–466). Withdrawn 18 October 2026.) The matrix function's effect is the contrast between the object rows and the subject row, and it holds after verbs as after prepositions. In the clash cells *whomever* is 6% where only the matrix function (a verb's object) is accusative and about 16% where only the gap is; this record first read that as the gap counting for more, but the two cells have different matrix functions and the second is 8 tokens of about 51, so the comparison doesn't measure the relative weight of the two functions (correction prompted by muse and GPT Pro, 18 October 2026). Read from the table, *whoever* is the default form, and *whomever* comes close to half only where both functions call for the accusative.

## 4. Register: the cells by genre

A check suggested in the round-1 reviews: *whomever* is mostly a form of edited prose, so a cell drawn mostly from TV and film scripts would look low for that reason alone. Each cell with KWIC lines is split into speech and scripts (SPOK, TV, MOV) and writing (everything else), with each group's lines scaled to the query total. The preposition-object cell with a subject gap (14%) comes from frequency lists, with no KWIC lines, so it's outside the check.

| Cell | speech and scripts | writing |
|---|---|---|
| object of a preposition, non-subject gap | 27% (31 *whomever* : 66 *whoever* lines) | 65% (150 : 65) |
| object of a verb, non-subject gap | 11% (25 : 76) | 58% (155 : 44) |
| main-clause subject, non-subject gap | 1 *whomever* line : 20 *whoever* lines | 29% (7 : 13) |
| object of a verb, subject gap | 2% (9 : 56) | 9% (51 : 76) |
| main-clause subject, subject gap | 0.5% (5 : 206) | 3% (27 : 194) |

The order is the same inside each group, and *whomever* is several times rarer in speech and scripts throughout. Register accounts for part of the gap between prepositions and verbs (65% against 58% in writing): more of the verb cell's *whoever* lines are from scripts (76 of 120, against 66 of 131). The grouping is coarse (fiction carries dialogue, and the web and blog texts are informal), so this is a check, not a finding.

## Caveats

- Labels by Claude, one pass, then checked by Brett Reynolds on 18 October 2026 on 105 lines: all 23 B1 lines, the 24 hard calls in A1 and A2 (ES, PR, MN, X), a random 30 from B2 and B3, and 28 lines from the 17 Oct genitive set. He changed five B1 labels, all to EC (4 fragments he reads as exhaustive conditionals, and l. 5, which Claude had excluded), and agreed with the other 100. None of the changes touches the main-clause-subject cell (8 against 33) or the 52% estimate.
- The before-pronoun estimates assume the displays are representative of the frequency-list rows.
- The verb-object labels (§3) were checked by Brett on 18 October 2026, after the 105-line check of the earlier sets, with no changes.
- Sentence-initial position catches main-clause subjects but also headings, quotations (Bible and Tao Te Ching lines in B3 and B4), and scripts; these are kept, labelled by function.

**Totals (Brett, 18 Oct):** `. whoever [p*]` 644 (it 219, you 166, he 108, they 67, she 45, I 28, we 10, who 1); `. whoever [v*]` 2,606 (448 verb types). Raw lists in the private run (`raw/G1…`, `raw/G2…`).

**Correction, 19 October 2026.** The spot-check was 105 lines, not 106 (23 + 24 + 28 + 30, counted from the check file `SPOT-CHECK.md`); the arithmetic slip was caught by GPT Pro's fourth review. The paper's data note is corrected to match.

**Provenance check, 23 October 2026 (Claude, Opus 5.5, from the private raw files; no new searches).** This answers the open questions about Table 2: which queries the verb-object cells came from, and whether the displays are samples.
- **J1–J3 queries, confirmed from the data.** Each frequency list sums to the total given above: 227 over 172 types for J1, 555 over 349 for J2, and 71 over 71 for J3. Every type has the query's shape:
  - J1 and J2: a verb, then *whomever* or *whoever*, then a pronoun (*marry whomever they*, *call whoever you*);
  - J3: a verb, then *whomever*, then a verb (*ask whomever runs*).
- **J4's total of 1,372 belongs to J4.**
  - It isn't the total of any other query in the batch (227, 555, 71, 644, 2,606).
  - The 200 displayed J4 lines all have a verb, then *whoever*, then a verb.
  - Their genre mix fits the chart's: χ² = 3.1 on 7 df, p ≈ 0.88, with TV and movies merged as the chart has them.
  - The chart's five-year columns sum to 1,109, which is 1,372 less its 263 web and blog tokens. The corpus dates all web and blog texts to 2012.
- **The displays are samples spread across the corpus, not the first hits.** Every display that shows fewer lines than its query's total runs from 1990 to 2019: J1, J2, J4, B2, and B4. J4's spread by period and genre matches its chart. First hits in date order would cluster at the 2019 end.
- These checks rest on the pasted displays and frequency lists. Brett's search history for the J searches wasn't pasted, so the strings themselves are confirmed by what the searches returned, not from the history.

**Source check, 23 October 2026 (Claude, Opus 5.5, from the private raw files; no new searches).** This asks whether the small *whomever* cells could come from one prolific text. They don't.
- **Main-clause subject, non-subject gap (8 tokens, B1 lines 1, 3, 9, 10, 11, 14, 16, 17):** eight different sources. *New Yorker* (2018), *Southern Review* (2015), and *Southwest Review* (2005), all fiction; the film *Alex Rider: Operation Stormbreaker* (2006); and four web and blog sites (gameskidsplay.net, caucusforamerica.com, slog.thestranger.com, soxpride.mlblogs.com; all 2012, COCA's date for its web and blog texts).
- **Subject of a verb's content clause, subject gap (9 tokens, J3 lines 3, 14, 24, 29, 33, 35, 39, 43, 61):** nine different sources. cleveland.com (2018), eatocracy.cnn.com, six blogs (blog.timesunion.com, theheckler.com, getrichslowly.org, a wordpress journalism blog, typophile.com, balloon-juice.com; all 2012), and NPR *Morning Edition* (1997). Seven of the nine are web or blog, which fits hypercorrection in informal writing.
