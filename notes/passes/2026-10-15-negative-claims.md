# Negative claims, 15 October 2026
<!-- SUMMARY: report-only negative-claims pass over determinatives-as-nouns.tex since af63c84, then one full read; 66 negatives examined; 3 wrong as worded against the cited sources (some "has no modifier use"; which/what "neither mark definiteness"; "a common noun that refers to the speaker can't bind a first-person reflexive"), 9 to narrow or evidence, 4 optional carried from 19 Sep, 50 standing · status: report, not applied · updated: 2026-10-15 -->

> Saved verbatim by the parent session from the subagent's final report (Claude Opus 5.5 subagent, general-purpose; subagents cannot write report files). The parent verified W1–W3 against *CGEL* pp. 357, 385, 539 and Halm (52) before presenting.

**Summary.** I examined 66 negatives. I covered every negative in the text changed since `af63c84` first, then read the whole manuscript once, through l.923; that full read is where I stopped. Twelve need action:

- **Three are wrong as worded, measured against sources the paper itself cites:**
  - *some* "has no modifier use" (abstract, Table 4, §4.3, conclusion). *CGEL* p. 385 gives modifier *some*.
  - *which*, *what*, *whichever*, *whatever* "neither mark definiteness" (l.236). *CGEL* p. 357 says the opposite.
  - "A common noun that refers to the speaker can't bind a first-person reflexive" (l.840, l.878). Halm's own (52a) is a counterexample, and Halm restricts the claim to singular imposters.
- **Nine need narrowing or a stated search.** Most are corpus negatives in the footnotes at l.171, l.538, l.836 and l.838; the others are a Reynolds (2024) paraphrase at l.780 and "categorically" at l.137.

Four optional items from 19 September are still open. The other 50 stand as evidenced. The inward novelty search found nothing new: 0 hits in the 241 literature files added since 19 September. The 19 September defects D1, D2, D4, D5 and D6 are all resolved in the current text.

**Provenance.** I read the manuscript at `2e586d1` (MD5 `4b3755cb…`). Three commits from another session landed while I worked: `25d77cf`, `3ea9f66` and `eb5040e`. Their manuscript edits touched only l.171, l.336, l.454 and l.828, and the file is still 923 lines with one paragraph per line, so the line numbers hold. Every "Old" string below was re-checked against MD5 `220eb2ec9f1881567468c44397f1446d` (HEAD `eb5040e`). I edited nothing and wrote no files.

*CGEL* pages were read with `pdftotext -layout -f N+20 -l N+20 literature/00-CGEL.pdf`, at printed pp. 349–350, 356–358, 377, 380, 385, 410, 415–416, 420–421, 423, 426, 429–430, 435, 445, 486, 501–503, 507, 518, 528, 539–540, 549, 827, 920, 1462 and 1466.

## A. Wrong as worded (rewording needed)

### W1. *some* "has no modifier use": l.29, l.528, l.538 (twice), l.878

*CGEL* p. 385 gives *some* a modifier use under the heading "(b) Modifier":

- [43i] *Have you got [some/any more] milk?*, glossed "some and any modify more in a DP";
- %*I'm feeling some better*, as a degree modifier;
- %*She may be oversimplifying some*, in clause structure.

So the bare negative is false by the grammar the paper relies on. The argument survives the narrowing. *CGEL*'s licence for Mod–Head fusion covers determinatives "which can function as internal modifier as well as determiner" (p. 415), and its *both* anomaly is that *both* "cannot occur in internal modifier function" (p. 377). The claim needed is *internal*-modifier use.

There is a second problem at l.538. The p. 410 quotation "occurs with just the determiner function" is *CGEL* describing *some sausages* as an example of an unfused dependent use: "just" means not fused with Head. It doesn't say *some* lacks modifier function, so it is being quoted past its context.

The anchor that does support "no *the some people*" is p. 539, criterion (a): "The clearest members of the determinative category cannot combine with the articles. Thus we have *a good book*, but not \**a this book*." *Some* is in the list [31] that this criterion admits.

Bonus for Brett: criterion (a) is stated without restriction to dependent use. Attested *the some who* is therefore a counterexample to *CGEL*'s own criterion as worded, which strengthens §4.3.

- **l.29.** Old: `\mention{some} has no modifier use for a fused head to build on`. New: `\mention{some} has no internal-modifier use for a fused head to build on`.
- **l.528 (table).** Old: `\mention{some}: Mod--Head, with no modifier use`. New: `\mention{some}: Mod--Head, with no internal-modifier use`.
- **l.538.**
  - Old: `In dependent use it \enquote{occurs with just the determiner function} \citep[410]{huddleston2002}, with no \mention{the some people} to match \mention{the few people}.`
  - New: `In dependent use it has no internal-modifier function: \textit{CGEL} lists it among the determinatives that \enquote{cannot combine with the articles} \citep[539, (31)]{huddleston2002}, and there's no \mention{the some people} to match \mention{the few people}.`
- **l.538.** Old: `As a fused Mod--Head, \mention{some} would have no modifier use to license it`. New: `As a fused Mod--Head, \mention{some} would have no internal-modifier use to license it`.
- **l.878.** Old: `although \mention{some} has no modifier use to license a fused head`. New: `although \mention{some} has no internal-modifier use to license a fused head`.

### W2. l.236: the wh-determinatives "neither mark definiteness nor quantify"

*CGEL* p. 357, on the inventory the paper cites at p. 356: "the items in [xiv] are indefinite as interrogatives, definite as relatives". Item [xiv] is *which, what, whichever, whatever*. So the definiteness half contradicts the cited source. This holds whichever way l.234 is read, since it defines the role as "mark the NP definite or indefinite".

The quantification half has no *CGEL* statement behind it. *CGEL* p. 358 says only that demonstrative *this* and *that* don't quantify. The *who* half is supported by p. 1462: "Clear cases of pronouns that are not anaphors are interrogative *who* and *what*."

- Old: `interrogative \mention{who} is no pro-form, and the interrogative and relative determinatives \mention{which}, \mention{what}, \mention{whichever}, and \mention{whatever} \citep[356]{huddleston2002} neither mark definiteness nor quantify.`
- New: `interrogative \mention{who} is no pro-form \citep[1462]{huddleston2002}, and the interrogative and relative determinatives \mention{which}, \mention{what}, \mention{whichever}, and \mention{whatever} \citep[356]{huddleston2002} don't quantify, though they mark the NP indefinite as interrogatives and definite as relatives \citep[357]{huddleston2002}.`

"Don't quantify" then stands as Brett's claim. If he wants only sourced outliers, the determinative-side outliers are the demonstratives (p. 358), and "The outliers line up" needs rethinking.

### W3. l.840 and l.878: "A common noun that refers to the speaker can't bind a first-person reflexive"

Halm (2021), at the page the paper cites (PDF p. 19, ex. (52)), has two relevant examples:

- (52a) *In this reply, [the present authors]₁ attempt to defend ourselves₁/themselves₁*;
- (52c) *Daddy₁ is enjoying \*myself₁/himself₁*.

He states the limit himself: "One exception is exemplified in (52c): singular imposters cannot be antecedents of first person reflexive (certainly in English)." So a plural common-noun NP referring to the speakers can bind a first-person reflexive, and the paper's unrestricted negative is false by its own source. The contrast with *the 12-year-old me* survives with "singular".

*CGEL* p. 518 supports calling *Daddy* a common noun: kin terms used as names "have the status of proper names, though they belong syntactically to the category of common nouns".

Search: `grep -n -i -E "imposter|ourselves|themselves|Daddy|myself|kicking|17 year|stages|Table 1"` over `literature/halm_2021_virtual_performatives_modified_pronouns.md`, plus `pdftotext` of PDF pp. 18, 19, 29 and 30.

- **l.840.** Old: `A common noun that refers to the speaker can't bind a first-person reflexive`. New: `A singular common noun that refers to the speaker can't bind a first-person reflexive`.
- **l.878.** Old: `where a common noun that refers to the speaker can't`. New: `where a singular common noun that refers to the speaker can't`.

## B. Narrow or evidence

### N1. l.538 footnote: "Its 53 hits for the some people have none in such a frame: of the 50 displayed"

Only 50 lines were read (record: nos. 18, 27, 28, 39, 41 and 49 absent from the 56-numbered display), so "none" is asserted of 3 unread hits.

- Old: `Its 53 hits for \texttt{the some people} have none in such a frame: of the 50 displayed, \mention{the} stands for`
- New: `Of its 53 hits for \texttt{the some people}, the 50 displayed have none in such a frame: \mention{the} stands for`

The record's classification matches the footnote: 15 *that*, 2 *same*, 24 plain indefinite, 9 titles or garbled, totalling 50. Record: `corpus/exclusion_tests/2026-10-15-brett-supplied-an-each-the-some.md`, section "The deciding comparison".

### N2. l.538 footnote: "The page's other hits are typos for same, approximate numbers …, titles, and a stray the"

This is an exhaustive classification, so it is a negative, and the record doesn't support it as worded. The record's 197 lines also include:

- 81 *the some of* lines, "mostly disfluent or non-native", the largest class;
- spam, *somewhat*, *soma* and *some college*;
- five *the some* + noun lines with a contrast reading, which bear on the paper's own negative. Examples: zerohedge.com, "funded by taking from all, even though the some users might benefit more then others"; maddowblog, "a swear word to the some people". The record's own wording is: "They still mean the sample can't support a flat claim that *some* never modifies after *the*."

The iWeb comparison is what answers those five lines, so the footnote should say so.

- Old: `The page's other hits are typos for \mention{same}, approximate numbers with the adverb \mention{some} \enquote{approximately} \citep[385]{huddleston2002}, titles, and a stray \mention{the}.`
- New: `The page's other hits are typos for \mention{same}, approximate numbers with the adverb \mention{some} \enquote{approximately} \citep[385]{huddleston2002}, disfluent or non-native \mention{the some of the}, titles, and spam; five \mention{the some} + noun lines can be read as a contrast (\mention{even though the some users might benefit more then others}, zerohedge.com) or as a stray \mention{the}, which the iWeb comparison below tests.`

### N3. l.538 and l.838 footnotes: the reader isn't stated

Both records mark the readings as Claude's and not yet Brett's:

- `2026-10-15-brett-supplied-an-each-the-some.md` (SUMMARY "readings Claude's, not yet Brett's"; iWeb section headed "Claude's reading");
- `2026-10-15-brett-supplied-the-adj-pronoun.md` ("Classification is Claude's").

These footnotes carry corpus negatives ("none in such a frame", "*are* in none"). l.454 names the reader for *few would* ("Brett Reynolds read all 94"), and the 19 September pass raised the same issue for *every* (D6, point 2). Either Brett reads the 50 iWeb lines and the 14 agreement lines, or the footnotes say how the lines were classified.

### N4. l.838 footnote: "a page of 14 lines has is or 's in 10 and are in none"

This is EVIDENCED by the record ("Agreement check: `the real you` + *is*/*are*", 10 to 0; the other 4 lines aren't agreement with *the real you*). But the paper gives no query string. Add it once Brett confirms it from his search history. The same record says the `the ADJ me/you` strings were "inferred … Brett to confirm".

### N5. l.836 footnote: "the spelling he's and she's can't be separated from the contraction in COCA's tokenization"

No record contains this search. The record `2026-10-04-brett-supplied-a-he-or-a-she.md` has `hes and shes` ("no matches") only. Either evidence it (the string run and its result) or narrow it:

- Old: `the spelling \mention{he's and she's} can't be separated from the contraction in COCA's tokenization.`
- New: `the spelling \mention{he's and she's}, which coincides with the contraction, wasn't searched.`

### N6. l.171 footnote: "The only usable bare lines after seem and become are non-affirmative"

This is EVIDENCED by `corpus/independent_argument/2026-10-04-brett-supplied-modified-much.md`, but the "only" rests on three lines from two queries the footnote doesn't name.

- Old: `The only usable bare lines after \mention{seem} and \mention{become} are non-affirmative:`
- New: `The only usable bare lines after \mention{seem} and \mention{become} (\texttt{[seem] much .}, 2 lines, one an artefact; \texttt{[become] much .}, 1 line) are non-affirmative:`

### N7. l.171 footnote: "of 96 lines displayed for is a bit much, none is negated"

This is EVIDENCED as a clause-level count (`2026-10-15-brett-supplied-a-bit-much.md`: "Negated: none"). The same screen, though, has 10 questions or tags, "mostly *don't you think X is a bit much?*". Questions are non-affirmative contexts on *CGEL*'s polarity account, and the footnote is backing an "affirmatively" claim at l.169.

- Old: `of 96 lines displayed for \mention{is a bit much}, none is negated,`
- New: `of 96 lines displayed for \mention{is a bit much}, none is negated, though 10 are questions or tags (mostly \mention{don't you think} \ldots\ \mention{is a bit much?}),`

### N8. l.780: Reynolds (2024) "with no pattern that sets any of them apart as an adverb"

This is pre-existing text, missed on 19 September. The source's negative is about *more* and *less* only:

- l.25: "argues that MORE and LESS do not pattern distinctly from other determinatives";
- l.240: "the distributional data do not single out MORE as exceptional";
- l.242: "no distributional pattern clearly identifies MORE as belonging to a distinct category";
- l.274: "no clear pattern emerges suggesting that MORE alone is an adverb".

The "idiosyncratic" half holds (l.211, citing Bolinger: "Intensifier distribution in adjective phrases is notoriously idiosyncratic"). Search: `grep -n -i -E "idiosyncra|lexeme by lexeme|intensifier|enough|a little|\ball\b|pattern"` over `literature/reynolds2024-more-less-never-adverbs.md`.

- Old: `with no pattern that sets any of them apart as an adverb;`
- New: `with no pattern that sets \mention{more} or \mention{less} apart as an adverb;`

### N9. l.137: "ordinary a photograph of the people takes it categorically"

This is pre-existing and was missed before. "Categorically" asserts that no plural verb ever occurs. No search was run, and the same paragraph documents attraction plurals after *each of the* + plural noun. I couldn't run a search, since corpus access is by hand.

- Old: `and ordinary \mention{a photograph of the people} takes it categorically, so neither`
- New: `and ordinary \mention{a photograph of the people} takes it as well, so neither`

## C. Provenance attached to negatives (not counted)

- **Query strings stated as run but recorded as inferred.** Four records say the string wasn't pasted and was inferred from the output ("Brett to confirm"):
  - the verb tag + `a bit much` (l.171);
  - `[be] all the better` (l.780 footnote);
  - `the ADJ me/you` (l.838 footnote);
  - `the some` (l.538 footnote).
  
  Brett can confirm all four from his COCA search history in one sitting.
- **l.171 footnote, "A sentence-final be much batch of 81 entries (18 September 2026)".** Its string is still unrecorded. `2026-10-04-brett-supplied-be-much.md` re-ran it as `[be] much .`: 81 lines, and line 6 is the *CBS This Morning* "There hasn't been much" line. Cite the 4 October run instead. The NOW `there is little` batch (23 entries) also has no recorded string; the supplement already says so.

## D. Carried from 19 September, still open (optional)

1. **l.137** "with some of the people … plural agreement is the only option". Unstarred; a star could be added (\**Some of the people was waiting*).
2. **l.342** "several … excludes peripheral a". Unstarred; *CGEL* p. 392 doesn't state \**a several*.
3. **l.358** "Neither many a nor what a has an independent use". *CGEL* p. 394 ("Like *a*, *many a* always functions as determiner") could be quoted for *many a*; *what a* remains a bare judgment.
4. **l.358** \**most the books*. Unsearched; a register scope is possible.

## E. Standing (evidenced)

| Line | Negative | Basis |
|---|---|---|
| 29, 149, 177 | grade/degree profile confined to the four; "no more of the inventory" | carried: *CGEL* 393–395, 431–432; COCA check in the supplement |
| 29, 834–836 | four secondary uses the grammar states separately | *CGEL* 385 (cardinals), 423 n.43 (*a nobody*, conversion), 429 n.46 (*a he*), 521 (proper nouns) |
| 96 | novelty "relative to those accounts" | see F |
| 133 | \**many of delegates* | *CGEL* 349 [55ii] |
| 139 | *plenty* resists determination and modification | *CGEL* 350: "does not permit any determiner or modifier" |
| 149 fn, 151 | degree-series exclusions; \**very a few*, \**a quite few* | carried (COCA zero hits, `exclusion_tests/log.md`) |
| 167 | Solt stars negated non-amount subjects | Solt (76)–(77), carried |
| 169 | restriction is polarity, not subject | `modified-much.md`; `be-much.md` l.68 ("Organization is not everything, but it is much"); *CGEL* 827 quotation verified |
| 171 fn | `[be] a little much .` 69 lines, none negated | `modified-much.md`: "every line is affirmative" |
| 171 fn | *too little, too late*: one predicative line negated | `too-little-too-late.md` (line 78) |
| 171 fn | Shakespeare line not counted as present-day | `not-be-much.md` (lines 2, 15, 17, 25) |
| 173, 175 fn | Payne et al. 61; *CGEL* 417 coordinated | carried |
| 183 | *you*'s number marked "only in the reflexive" | *CGEL* 486; *youse* p. 1466 n.9 |
| 191 | reflexives lack genitives | *CGEL* 426: "There are thus no genitive reflexives" |
| 224 | *rich* needs *the* (generic) | carried, 417–418 |
| 234 | *this*/*that* don't quantify; Det "need not be realised by a determinative" | *CGEL* 358 |
| 236 | interrogative *who* no pro-form | *CGEL* 1462 (cite suggested in W2) |
| 250 | \**so numerous mistakes* | *CGEL* 540 [34ib] |
| 291 | English adjectives don't agree | *CGEL* 528: adjectives "don't inflect for number" |
| 293 | Van Eynde's English examples don't test the criterion | carried (D3) |
| 329 | *every* normally dependent; anaphoric cases acknowledged | `every-reading.md` correction; D6 resolved |
| 340, 344 | *a great many* modifier obligatory; *CGEL* 621 | carried |
| 352 | exclamative *what* fails criteria (a)–(c) | *CGEL* 540: "It fails all of the determinative criteria (a)–(c)" |
| 360 | exclamative *what* has no predicative use | *CGEL* 920: "What occurs only as modifier in NP structure"; D4 resolved |
| 360 | lacks the predicative function of central adjectives | *CGEL* 528 [1i] |
| 364 | determinative *such* only in legal register | *CGEL* 435 n.52 (also 356 n.16) |
| 368, 818 | none of the four remains a complex determinative; *a certain* set aside | *CGEL* 393; D1 applied |
| 454 fn | *few would*: 82 with no set | Brett's reading; now 3 + 2 after `25d77cf` |
| 538 | *both* "cannot occur in internal modifier function" | *CGEL* 377, verbatim |
| 538 fn | iWeb *the some who*: most take up no earlier *some* | `an-each-the-some.md`, iWeb section |
| 574 | one adverb premodifies a noun; adverbial modification not categorically excluded | Payne et al. 2010 n.3, p. 75 (md l.1021) |
| 608, 737 | compounds exclude external determination and a pre-head adjective | carried |
| 630 | gapping excluded outside coordination | *CGEL* 420–421 [37] |
| 634 | *CGEL* rejects ordinary Head as a general replacement | *CGEL* 421 [38]–[39] |
| 701 | \**I saw him that point in time* | Hudson 2004, carried |
| 771 | \**money almost enough* | *CGEL* 445 |
| 780 | *CGEL* "lists ten determinatives" | *CGEL* 549 [37], ten items; *CGEL* says "illustrated", so "illustrates with ten" would be more exact |
| 808 | audit doesn't measure genitive-restriction costs | `analysis/coverage-audit.json` l.1409 |
| 808, 816 | *CGEL* states number transparency and degree modifiers separately for NPs and DPs | nouns 349–350, 501–503 vs fused determinative heads 507 (*any*, *none*, *either*, *neither*); degree: 549 [37] determinatives vs [38] NPs. Optional: cite 507. |
| 814 | secondary use and complex determinatives weren't §2 diagnostics | §2 read; holds |
| 836 fn | `hes and shes` returns nothing; other `mes/yous` hits classified | `a-he-or-a-she.md` ("no matches"); `mes-yous.md` |
| 836 | *he*/*she* "are common nouns, not pronouns" | *CGEL* 429 n.46, verbatim |
| 838 fn | *the new me* 99/100; *the real you* 193/198 | `the-adj-pronoun.md` screens |
| 844 | articles and *every* have no set-denoting use (\**an every*) | carried; the one COCA *an every* is an attributive compound |
| 856 | the 2021 study contains no common or proper nouns | carried |
| 362 | Van Eynde: *what*/*such* "invariably lexical", "lexically select …" | `VanEynde_2007_BigMess.md` l.706, l.725 (§5) |

## F. Inward search behind the novelty claim (l.96)

The claim stays narrowed to the accounts the paper surveys ("Relative to those accounts"), so I ran no outward search.

Rerun: `find literature -maxdepth 1 -name "*.md" -newer notes/passes/2026-09-19-negative-claims.md` gives 241 files. Over those I grepped `grep -l -i -E` for the 19 September regexes:

- `determin(er|ative)s? (are|as) (a )?(noun|pronoun)s?\b`
- `determin(er|ative)s?[^.]{0,40}(sub-?class|sub-?categor|subtype|kind|species|type) of (noun|pronoun)`
- `(noun|pronoun)s?[^.]{0,20}(include|including|comprise)[^.]{0,30}determin(er|ative)s`
- `determiners? (are|is) (a )?(kind|type|sort) of noun`
- `quantifiers? (are|as) (a )?nouns`

Result: 0 files.

The 19 September lead on Anderson (1997, notional grammar) is still unverified: the work isn't held in `literature/`.

## G. Unresolved

None blocking. The "don't quantify" half of W2 has no *CGEL* source either way; it is Brett's call whether to keep it as his own claim.