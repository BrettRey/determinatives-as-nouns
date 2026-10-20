# *Whoever* / *whomever* + two words: case in fused relatives (17 Oct 2026)
<!-- SUMMARY: COCA whoever/whomever counts. With the matrix function held constant (object of a preposition), whomever has 395/802 (49%) before a pronoun subject (non-subject gap) but 352/2,458 (14%) before a verb (subject gap); the head-plus-bare-relative analysis predicts no difference. Earlier uncontrolled lists (whoever/whomever * [v*]) superseded for the paper · status: controlled test done · updated: 2026-10-17 -->

Two frequency lists pasted by Brett Reynolds, 17 Oct 2026: `whomever * [v*]` (top 100 types shown, no total given) and `whoever * [v*]` (total 7,748 tokens, 2,098 types; top 100 shown). Corpus COCA, and the search strings, confirmed from Brett's English-Corpora search history (pasted 17 Oct 2026); an earlier version of this record gave them as `WHOMEVER * *` and `WHOEVER * *`. These are counts of three-word strings with no left context, so the external function of the fused relative can't be read from them. Classification by Claude (Opus 5.5).

## Same right context, both forms

| Right context | Gap | *whoever* | *whomever* | *whomever* share |
|---|---|---|---|---|
| *you want* | object | 229 | 58 | 20% |
| *they want* | object | 82 | 51 | 38% |
| *I want* | object | 77 | 34 | 31% |
| *he wants* | object | 42 | 22 | 34% |
| *you choose* | object | 16 | 16 | 50% |
| *is elected* | subject | 54 | 6 | 10% |
| *would listen* | subject | 25 | 5 | 17% |
| *is running* | subject | 26 | 3 | 10% |
| *is playing* | subject | 15 | 4 | 21% |
| *wins will* | subject; the whole NP is also subject | 37 | 3 | 7.5% |
| *it is* | predicative complement | 555 | 26 | 4.5% |
| *it was* | predicative complement | 512 | 20 | 3.8% |
| *you think* | embedded clause (gap's function not visible) | 14 | 3 | (18%) |

Other *whomever* lines with a subject gap: *will listen* 8, *might be* 5, *is chosen* 4, *may be* 4, *will be* 4, *is selected* 3, *has decided* 2, *has set* 2, *else is* 6, and *whomever , is* / *whomever ) is* 3 each. Other relevant *whomever* lines: *you believe* 3 and *they feel* 4, which may have embedded subject gaps (*whomever they feel is best*) and need context.

## Reading

- ***Whoever* is the default form.** It occurs even with object gaps (80% of *you want*).
- **The gap's function still affects the form.** *Whomever* takes 20–50% with object gaps and 7–21% with subject gaps. In CGEL's terms, that's the internal effect, as a preference. Provisional: the external function isn't held constant in these counts (see "To read by hand").
- **The *it is* / *it was* rows are probably not fused relatives.** *Whoever it is, ...* is most likely an exhaustive conditional adjunct, which CGEL treats as an interrogative (p. 1072 n. 15). Don't use the predicative-complement figure (about 4%) until the lines are read.
- ***Whomever* with subject gaps is attested at real rates.** CGEL marks this configuration "at best very questionable" (*?She lunches with whomever is going her way*, p. 1074). Where the external function is accusative (after a preposition or as object), the form follows the external case. In *whomever wins will* the whole NP is a subject too, so neither function calls for accusative, and the form is a register choice (hypercorrection).
- **Bearing on the analysis.** Payne et al.'s strict matching ("the pronoun has to satisfy the case requirements of both", CGEL p. 1073) is a normative idealization. Usage shows a graded internal preference, external effects, and register-driven *whomever*. Fusion's double case assignment predicts the clash cases to be bad, and they're attested, so the case argument favours fusion rather than forcing it. The positional preference doesn't explain the profile without a prenucleus. CGEL p. 467 [40] gives the two factors for an embedded subject: *who* "is subject of a finite content clause" (Dialect A's factor) and *who* "is in prenuclear position preceding the subject of the relative clause" (Dialect B's). For Dialect B it adds that "the crucial distinction is therefore between relative clause subject and non-subject". Both factors presuppose that the wh-word stands in the relative clause. Under the head-plus-bare-relative alternative it stands outside the clause, so neither rule reaches it, and its case would follow its external function alone. (Corrected 17 Oct 2026: an earlier version of this bullet claimed the positional preference accounted for the profile without a prenucleus.)

## To read by hand

- Left context for the subject-gap *whomever* lines (*is elected*, *will listen*, *would listen*, *wins will*, *is chosen*), to separate external accusative (*to/for/with whomever*) from hypercorrection.
- The *whomever you think / you believe / they feel* lines, to see whether the gap is an embedded subject (*whomever you think is best*). That's the Dialect B configuration: positional accusative where the gap's function would call for nominative.

## Controlled test: the matrix function held constant (17 Oct 2026)

Brett ran two COCA searches by hand. Search strings `[i*] who*ever [p*]` and `[i*] who*ever [v*]` (confirmed by Brett). In both lists the fused relative is the complement of a preposition, so the matrix function is the same in every token, and only the function inside the relative clause varies. The raw lists are in the fusion repo, gitignored: `reviews/corpus-whoever-prep-20261017/` (list 1 transcribed in full, 189 rows summing to its total of 1,013; list 2 rows 1–319 transcribed, and rows 320–1000, all frequency 1, tallied by form in two independent passes, for a total of 2,506).

| Following word | Gap in the relative clause | *whoever* | *whomever* | *whomever* share |
|---|---|---|---|---|
| pronoun subject other than *it* (*with whomever they*) | non-subject | 407 | 395 | 49% |
| *it* (*for whoever it*) | mixed: predicative complement (*whoever it is*) or object | 145 | 35 | 19% |
| verb (*to whomever is*) | subject | 2,106 | 352 | 14% |

**Robustness checks:**
- Leaving out *than*, *as*, *like*, *unlike*, *plus*, *times*, *alone*, *save* and the odd token, where pronoun case varies anyway, changes nothing: 393/793 (50%) against 350/2,399 (15%).
- The verb list shows only its 1,000 most frequent types, so its counts are lower bounds. Its frequency-1 tail runs about 20% *whomever* (132 of 662). Even a large missing tail at that rate leaves the subject-gap share far below 49%.
- The archaic forms split the same way. *Whomsoever* and *whosoever* have 21 and 2 tokens before a pronoun, and 12 and 30 before a verb.

**Reading:** with the matrix function constant, the form tracks the function inside the relative clause, as a strong preference rather than a rule. The head-plus-bare-relative analysis puts *whomever* outside the clause and predicts the same share in both rows. The positional rule (CGEL p. 467, Dialect B) would give the same split, but it is stated over prenuclear position inside the relative clause. That's what fusion assigns.

## Baseline: subject *whom* in ordinary relatives (17 Oct 2026)

**Searches** (COCA, Brett by hand), whole-corpus counts from the section charts:
- `[nn*] who [v*]`: 449,450 tokens.
- `[nn*] whom [v*]`: 390 tokens, of which 321 are in BLOG and WEB.

So *whom* fills under 0.1% of subject-gap ordinary relatives. CGEL p. 467 n. 62 treats subject *whom* in an ordinary relative as a hypercorrection.

**Against that baseline,** subject-gap *whomever* after a preposition (14%) is about 160 times as frequent. Most of those tokens owe their accusative form to something outside the relative clause: the matrix function (object of a preposition), a general preference for *whomever* as the formal variant, or both.

**What the data can't separate:** the matrix function's share. The one count where neither function calls for accusative, *whomever wins will* (3 of 40, from the first lists), is too small to estimate a function-free *whomever* rate.

**For the paper:** the matrix function's effect rests on CGEL's judgment of *?Whomever he marries will have to be very tolerant* (p. 1074). The baseline appears only in the search footnote.

(Also in Brett's paste: a `[nn*] who* [v*]` list showing only its 1,000 most frequent types, total 360,225. Not used.)

**Clause-taking prepositions in the before-verb list (added 18 October 2026).** A preposition that can introduce a clause (*until whoever you're waiting for gets here*) would put the fused relative in subject function, not in a preposition's object. In the 319 most frequent rows of the `[i*] who*ever [v*]` list (1,825 of its 2,506 tokens), 43 tokens have such a word before them, all *whoever*: *like* 27, *after* 8, *until* 4, *before* 2, *as* 2 (some of them may still be ordinary prepositional objects). The 681 frequency-1 rows were tallied by form, not by preposition, so they aren't covered. Removing the 43 changes the *whomever* share from 14.3% to 14.6%. Counted by Claude (Opus 5.5) from the private transcription (fusion repo `reviews/corpus-whoever-prep-20261017/`).
