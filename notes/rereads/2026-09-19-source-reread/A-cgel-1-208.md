# Source reread A: CGEL citations, manuscript lines 1–208
<!-- SUMMARY: source-reread of every huddleston2002 citation and uncited CGEL attribution in ll. 1-208 · status: complete · updated: 2026-09-19 -->

**Summary.** 44 citation contexts: 36 SUPPORTED, 4 NUANCE (ll. 131, 137, 141, 149), 4 PAGE (ll. 97, 109, 186, 190), no OVERSTATED, MISATTRIBUTED or UNVERIFIED. Of the 10 uncited attributions to *CGEL* checked, one is NUANCE (l. 137, main text). One flag sits outside the verdict scheme: CGEL p. 421 considers and rejects the ordinary-Head option for determinatives, and the manuscript never cites that passage.

## Source and method

- Manuscript: `determinatives-as-nouns.tex`, SHA-256 `2c6c7953c659274969e88599c6d86369313bb0212fd57df0e3b0cb2480158afe` (matches dispatch). Read only.
- Source: Huddleston & Pullum 2002, text layer split one file per printed page, `scratchpad/cgel-pages/pNNNN.txt` (printed page = filename; PDF offset +20, as verified by the dispatcher). The running heads and page numbers inside each file were checked against the filename for every page quoted below.
- Bibliography entry `huddleston2002` (central bib, line 6659): Huddleston, Rodney and Pullum, Geoffrey K., *The Cambridge Grammar of the English Language*, CUP, 2002. Consistent with the source.
- Every cited page was read in full. Where a page did not carry the content, the whole page set was searched with `grep` (the strings are given under each item).

## Citation contexts

**#1, l. 42.** Framework adopted from *CGEL*. No page claim. **SUPPORTED.** (Formatting only: l. 42 sets the title in sentence case, *The Cambridge grammar of the English language*, while the abstract at l. 29 uses title case.)

**#2, l. 50.** In *CGEL* the DP headed by independent *some* jointly fills determiner and Head, a fusion of functions (410–412). p. 410: "Fused-head NPs are those where the head is combined with a dependent function that in ordinary NPs is adjacent to the head, usually determiner or internal modifier"; p. 412, heading "9.2 Fusion of determiner and head", tree [7a] "Det-Head: D few". **SUPPORTED**, with a note. CGEL's diagrams put a bare D (not a DP) in the fused position, but CGEL allows either one: p. 330 says Det "can be filled by a determinative (or a phrase headed by a determinative, i.e. a DP)", and p. 424 has "not everyone and hardly anything are DPs functioning as determiner-head". "Fusion of functions" is the manuscript's own term. CGEL's nearest wordings are "functional fusion" (p. 419) and "syntactic fusion of the two functions" (p. 423).

**#3, l. 54 fn.** *CGEL* discusses the limits of ellipsis as a general account (420–421). p. 420: "Ellipsis does not provide a general solution either." **SUPPORTED.** See the flag at the end: the same page, 421, goes on to the ordinary-Head alternative.

**#4, l. 87.** Pronouns are in Noun on the basis of their phrases' functions, despite differences in inflection and dependents (327–328). p. 327: "They differ inflectionally from prototypical nouns and permit a narrower range of dependents, but they qualify as nouns by virtue of heading phrases which occur in the same functions as phrases headed by nouns in the traditional sense". **SUPPORTED** (the decisive text is on 327).

**#5, l. 95.** *a lot of delegates* is fine but \**many of delegates* is not (349). p. 349 [54ii] "[A lot of people] complained" [non-partitive]; [55ii] "∗[Many of delegates] complained." **SUPPORTED.**

**#6, l. 97.** *CGEL* calls quantificational *lot* number-transparent (349–350, 411–412). p. 349: "we will say that lot is number-transparent in that it allows the number of the oblique to percolate up to determine the number of the whole NP." **PAGE (partial).** The term appears on 349–350 and again on 501–503, where p. 503 has "The clear cases of number-transparent singular nouns are lot, number, and couple". Pages 411–412 cover partitives (p. 412: quantificational nouns as head in "a lot of the meat") but never use the term. Search: `grep -i transparent` over pp. 300–599. Repair: `\citep[349--350, 501--503]{huddleston2002}`, or move 411–412 to the partitive point it supports.

**#7, l. 101.** *plenty* resists determination and modification; *lot* requires *a* and allows only limited modification (349–350). p. 350: "Singular lot takes a as determiner, and allows a very limited amount of premodification"; "Plenty is singular in form but does not permit any determiner or modifier". **SUPPORTED.** (Optional: "resists" is weaker than CGEL's "does not permit any". The wording "excludes determination and modification" would match the source.)

**#8, l. 103.** Quantificational nouns occur in degree modifiers such as *a great deal smaller* and *plenty big enough* (549–550). p. 549 [38ii–iii] lists both; p. 550: "the others are quantificational NPs (see Ch. 5, §3.3)". **SUPPORTED.**

**#9, l. 105.** Common nouns take a wider range of PP and clausal complements; pronouns and primary naming uses of proper nouns are much more restricted (429–430, 439–443, 517–521). p. 439: "Post-head complements have the form of PPs or clauses"; p. 429: "Pronouns usually constitute whole NPs by themselves, but some allow a very limited range of modifiers"; p. 520: "In their primary use proper names are inherently definite, and for this reason their heads do not select from the determiner system in the same way as ordinary heads". **SUPPORTED.**

**#10, l. 109.** Plain, comparative and superlative forms of *few, many, little, much* (391–395). p. 393: "The degree determinatives many, much, few, little. These form a distinct group of determinatives in that they inflect for grade." **PAGE (minor).** Grade is on 393–395. Pages 391–392 cover *another*, *a few/a little*, *several*, *various/certain*. Repair: `[393--395]`.

**#11, l. 109.** *CGEL* treats *more/less* before adjectives and adverbs as adverbs (395, 1123). p. 395: "More and less modify adjectives, adverbs, etc., but we take these to be degree adverbs, rather than comparative forms of much and little"; p. 1123: "more_a does not enter into any such contrast with much". **SUPPORTED.** p. 1123 is the explicit denial of contrast that the manuscript refers to.

**#12, l. 111.** The degree series selects the four determinatives that inflect for grade (393–395, 431–432). p. 431: "The degree determinatives many, much, few, and little are the ones that are most like adjectives, and in particular they take a very similar range of degree modifiers to gradable adjectives, including very, so, too, how". **SUPPORTED.** The stars on *very every* etc. are the author's own judgements and are not attributed to CGEL.

**#13, l. 111 fn.** Completeness modifiers *marginally enough*, *absolutely all* (432). p. 432: "Adverbs denoting degrees of completeness such as fully, totally, completely, marginally, and partially can modify the sufficiency quantifiers enough and sufficient … absolutely occurs with universal all and every and negative no". **SUPPORTED.**

**#14, l. 113.** Internal *very* in *a very few mistakes* vs peripheral *quite* in *quite a few mistakes* (392, (61)). p. 392: "The only internal expansion permitted for a little is the addition of very … They can also combine with the peripheral modifier quite", then [61] "a. [a very few] mistakes b. quite [a few] mistakes". **SUPPORTED.** The stars on the reversed orders come after the semicolon and are the author's.

**#15, l. 121.** Specifying *be* clauses are excluded from the noun–adjective diagnostic (536). p. 536: "we should exclude, for diagnostic purposes, clauses headed by be in its specifying sense, since phrases of any major category can occur as subject or predicative complement in clauses of this type." **SUPPORTED.**

**#16, l. 125.** Bare-role *president* is fine in *I'd like to be president* but needs a determiner in object use (328). p. 328 [8]: "I'd like to be president. / I'd like to meet ∗president / the president." **SUPPORTED.**

**#17, l. 131.** *Kim isn't much of an actor* is given as an instance of "a quantity NP in predicative function" (395). p. 395 [70iiic] does list the example, as a "special" fused head. **NUANCE.** CGEL's own analysis is on p. 415: "Plain much, comparative more and less, and sufficiency enough are used as degree quantifiers for properties expressed in predicative NPs … Much here is strongly non-affirmative: compare ∗Ed is much of a husband." So CGEL treats it as quantifying the degree to which a property holds, restricted to non-affirmative contexts. It isn't a quantity NP, and it has no degree modifier. The paragraph is about when the amount-subject condition lapses, so the non-affirmative restriction matters. Repair: "… and \textit{CGEL}'s non-affirmative \mention{Kim isn't much of an actor}, where \mention{much} quantifies the degree to which a property holds \citep[395, 415]{huddleston2002}."

**#18, l. 137 fn.** "subjects needn't be NPs" (236). p. 236: "The prototypical subject has the form of an NP … Subordinate clauses can also function as subject … Other categories appear as subject only under very restrictive conditions." **NUANCE.** The manuscript drops CGEL's restriction. It uses the page to license a bare comparative (AdjP?) subject in an ascriptive clause, but CGEL's one AdjP-subject example is in a specifying *be* clause (p. 536: "In Rather more humble is how I'd like him to be … the subject is an AdjP"). Repair: "subjects needn't be NPs, though \textit{CGEL} admits other categories there only under restrictive conditions \citep[236, 536]{huddleston2002}."

**#19, l. 141.** Demonstratives distinguish *this/these*, *that/those* (373, 521). p. 373: "Both inflect for number … compare singular this book with plural these books, or singular that book with plural those books." **NUANCE (placement).** Page 521 is about proper names, [6iv] "Shall we invite [the Smiths]?", so it supports the previous sentence. Repair: put `\citep[521]{huddleston2002}` after *the Smiths* and leave `[373]` on the demonstratives sentence.

**#20, l. 143.** Singular and plural *you* are distinct lexemes, differing overtly only in *yourself/yourselves* (486). p. 486: "We assume that there are two pronouns you, a singular one with yourself as its reflexive form and a plural one with yourselves as reflexive form. As the distinction is marked only in the reflexive …" **SUPPORTED.**

**#21, l. 145.** Generic human *the rich* is a plural NP whose adjective lacks number inflection and takes adverb modifiers, e.g. *the very rich* (418). p. 418: "the rich and the very poor are plural NPs with no inflectional plural marking on the head … Rich and poor, by contrast, take adverbs as modifier, as in the extremely rich and the very poor". **SUPPORTED.** (CGEL's own examples are *the extremely rich* and *the very poor*; *the very rich* is modelled on them.)

**#22, l. 147.** Head genitives *everyone's*, *Edward's*, marked by "the inflection of the head noun"; phrasal genitives *everyone else's*, *somebody local's*, *the King of England's* (479). p. 479: "Genitive NPs are usually marked as such by the inflection of the head noun: we refer to these as head genitives." [63] has exactly these pairs. **SUPPORTED.** The quotation is exact.

**#23, l. 149.** "Many determinatives also have pro-form uses. They range from deictic *this* to quantitative *many* and universal *every*" (358–360, 370–405, 425–428, 515–521). **NUANCE, two parts.** (a) *They* most naturally picks up "many determinatives [with] pro-form uses", but CGEL denies *every* any independent use. p. 379: "Every has only a dependent use, requiring a following head"; p. 412: "The two articles and every do not occur in head function at all". (b) Pages 425–428 (pronouns: "characteristically used deictically or anaphorically", p. 425) and 515–521 (proper names) support the previous sentences about *she* and *Kim*, not the determinative range. Repair: "Determinative meanings range from deictic \mention{this} to quantitative \mention{many} and universal \mention{every} \citep[358--360, 370--405]{huddleston2002}", with `[425--428, 516--521]` moved to the *Kim*/*she* sentence.

**#24, l. 153 fn.** *CGEL*'s inventory suffices for the pronoun/determinative boundary of *what/which* (397–399). p. 398: "The what that occurs as head in NP structure is a pronoun"; p. 399: "the head which is a pronoun." **SUPPORTED.** (pp. 421–422, "just four items that belong in both categories: what, which, we, and you", could be added.)

**#25, l. 163.** Independent uses of demonstratives and the listed quantifiers, with lexical restrictions and *no/none* (371–372, 410–424). Checked: p. 371 (*the* "completely excluded from fused-head function"), p. 372 (*a* not in fused heads), p. 410 [3] "no / none", p. 413 (*either, neither, both, certain*; list incl. *several, many, much, few*), p. 414 (*few, many, all, some*; *much, little, enough*; singular demonstratives). **SUPPORTED.**

**#26, l. 163 fn.** *all/both* as predeterminers, *quite/rather* as peripheral modifiers, *such*/exclamative *what* as adjectives (433–437). p. 433 [2] "all the books … both the houses"; p. 435: "The adjectives such and exclamative what occur as external rather than internal modifier in construction with a"; p. 437: "rather/∗absolutely a good idea … quite a good idea (approximation: "fairly good")". **SUPPORTED.**

**#27, l. 163 fn.** Complex determinative *many a* (394). p. 394: "Many combines with a to form two kinds of complex determinative: [66] i [Many a man] …" **SUPPORTED.**

**#28, l. 163 fn.** *half* in *half a cake* is a common noun used as a predeterminer (434). p. 434: "Predeterminers expressing fractions have the form of NPs. Half, quarter, third, etc., are nouns"; "only undetermined half can occur before indefinite a: half a day". **SUPPORTED**, with a note. Strictly, CGEL says the predeterminer is an NP headed by the noun *half*. CGEL itself uses the looser wording on p. 419 ("the predeterminer is respectively a nominal and a noun"), so this is not a finding.

**#29, l. 178.** *the most important of her criticisms* is an NP with a partitive *of*-phrase (332–333, 416–423). p. 333: "The most important of her criticisms ([12ia]) is a partitive NP"; p. 416 [22] covers superlatives and comparatives as fused heads. **SUPPORTED.**

**#30, l. 180.** Fused-head *rich* requires *the* on the generic human reading (417–418). p. 417: "The NPs are determined by the definite article – we couldn't even substitute a demonstrative: ∗these very poor." **SUPPORTED.**

**#31, l. 182.** In *There are several*, the quantifier is in displaced-subject position and *there* is the subject (1391–1393). p. 1391: "in [b] the subject function is filled by there … We accordingly analyse several windows as a displaced subject". **SUPPORTED.**

**#32, l. 184.** In *my/Kim's/people's preferences* the determiner is an NP headed by a pronoun, a proper noun and a common noun (354–355, 470–471). p. 355 [3ii] subject-determiners "genitive NPs … my tie … the boy's shoes"; p. 471: "my and mine are both pronouns … As pronouns, they are heads of NPs". **SUPPORTED.**

**#33, l. 184 fn.** Subject–Det (472–473). p. 472: "Type i genitives combine the syntactic functions of determiner and subject." **SUPPORTED.**

**#34, l. 186.** Plain-case NPs fill Det: *what size shoes*, *that size shoes*, *Sunday morning* (356). **PAGE.** Page 356 has none of this; it covers uses of determinatives and the [5] inventory. The content is on p. 357: "The determiner function can also be filled by a narrow range of plain-case NPs and PPs … [What size hat] … They don't stock [that size shoes] … Sunday morning". The p. 355 table [3iii] has "what colour tie / this size shoes". Search: `grep "size shoes\|Sunday morning\|Minor determiners"`, with hits on pp. 355 and 357 only. Repair: `[355, 357]`. Also note: *what size shoes* is a blend of CGEL's *what size hat* and *that size shoes*, and CGEL adds that for *that size shoes* "there is a strongly preferred alternant … shoes that size".

**#35, l. 188.** Det marks definiteness and often contributes quantification (354–359). p. 355: "one general function of all determiners is to add a specification of definiteness … or indefiniteness"; p. 358: "the basic ones characteristically express quantification." **SUPPORTED.**

**#36, l. 190.** PPs as a restricted alternative: *up to twenty minutes*, *between fifty and sixty tanks* (356). **PAGE.** Both examples are in p. 357 [6] ("between fifty and sixty tanks … up to twenty minutes"). The restriction is stated on p. 433: "a restricted range of PPs can function as determiner". Neither is on p. 356. Repair: `[357, 433]`.

**#37, l. 192.** Emphatic *herself* as a clause adjunct in *The manager detected the error herself* (1496–1497). p. 1496 [50ii] gives that sentence as "[end position]", with "in [ii–iv] it is an adjunct in clause structure". **SUPPORTED.**

**#38, l. 194.** Personal pronouns take a restricted range of integrated relatives: *we who have read the report* (430). p. 430: "Personal pronouns with human denotation may be modified by integrated relative clauses: [14] i I/We who have read the report …" **SUPPORTED.**

**#39, l. 196.** Relative postmodification with demonstratives and compounds (414, 422–423). p. 414 [14i] "Those who break the rules"; p. 423: "The compound determinatives take the same range of post-head modifiers as common nouns, for example PPs and relative clauses". **SUPPORTED.** (l. 194's *something that you need to know* is CGEL's own p. 423 example, and this citation covers it.)

**#40, l. 202.** *so many mistakes* vs \**so numerous mistakes* (539–540). p. 540 [34i] "He made [so many mistakes]. / ∗He made [so numerous mistakes]." **SUPPORTED.**

**#41, l. 204.** *certain/various*: *of*-phrases hardly omissible; speaker and register restrictions (392–393, 411–413). p. 413: "With certain the of phrase is hardly omissible, and the same applies to various"; p. 393: "Certain occurs (in relatively formal style) as head in a partitive … The same applies, for some speakers, primarily AmE, to various". **SUPPORTED.**

**#42, l. 204.** *Its advantages are several*; *Their enemies were many*, the latter uncommon and formal (392, 395–396). p. 392: "several can function … as predicative complement: its several advantages; Its advantages are several"; p. 395: "The degree determiners can also function directly as predicative complement: Their enemies were many. This, however, is a relatively uncommon and formal construction". **SUPPORTED.**

**#43, l. 208.** Indefinite ordinal *a second* (416). p. 416 [24iii] "I didn't want [a second]"; "there appears to be no constraint against the NP being indefinitely determined." **SUPPORTED.** (*There was a second* is the author's example.)

**#44, l. 208.** *the rich* is plural with an uninflected adjective (418). The p. 418 quotation is under #21. **SUPPORTED.**

## Uncited attributions to *CGEL* (ll. 1–208)

Swept with `awk 'NR<=208 && /CGEL|Huddleston|Pullum/'`.

- **l. 42** "Unlike *CGEL*, though, I include determinatives within Noun." p. 326: the chapter covers "two lexical categories … nouns and determinatives". **SUPPORTED.**
- **l. 71** "*CGEL*'s determinative category, articles included". p. 356 [5i] lists "the, a" as "articles". **SUPPORTED.**
- **l. 79** "DP means determinative phrase, as in *CGEL*". p. 23 [5viii] "determinative phrase … DP"; p. 330. **SUPPORTED.**
- **l. 99** "number-transparent in *CGEL*'s sense". This applies the p. 349 definition. **SUPPORTED.**
- **l. 119** "Both *the people* and *the rich* are NPs in *CGEL*, though only the former has a noun as lexical head". p. 326 [1ii]; p. 332 [12ib]; p. 418. **SUPPORTED.**
- **l. 137 (main text)** "*CGEL*'s *Henrietta likes red shirts, and I like blue* permits reduction licensed by coordination." **NUANCE.** CGEL gives the example (p. 417 [25i]) as a fused modifier-head of type "(d) Modifiers denoting colour, provenance, and composition". It argues against ellipsis for such NPs, noting that gapping "is in general restricted to coordinative constructions" whereas "there is … no such restriction on the fused-head NP construction" (p. 421). A reader will likely take "reduction licensed by coordination" as CGEL's analysis, but it is the author's. Repair: "\textit{CGEL}'s \mention{Henrietta likes red shirts, and I like blue}, a fused modifier-head there (p.~417), occurs in a coordinated contrast, which may license the reduction."
- **l. 137 fn** "The *blue*, *old*, and *small* examples on *CGEL* p. 417 all occur in coordinated contrasts." p. 417 [25i] "… and I like [blue]"; [27i–ii] "… but I prefer [old]/[small]". **SUPPORTED** (page right).
- **l. 147** "On *CGEL*'s categorization the head of *everyone's* is a determinative". p. 423 [41ii] lists *everyone* among compound determinatives. **SUPPORTED.**
- **l. 204** "*CGEL* … includes *several* among determinatives and treats … *certain* and *various* as marginal members, partly on the evidence of partitives." p. 392: "somewhat marginal members of the determinative category"; p. 393: the partitive use "makes certain and various more like the clear determinatives", with the generic-interpretation test as the other ground (hence "partly" is right); p. 539 [33] admits *several, certain, various* by the partitive criterion. **SUPPORTED.**
- **l. 29 (abstract)** "the determinative inventory of *The Cambridge Grammar*". No specific claim.

Not checked (other keys): the `Huddleston2021` "List of determinatives in English" (l. 44 fn) and every non-CGEL citation.

## Flag outside the verdict scheme: CGEL p. 421 is not engaged

CGEL p. 421 goes on directly from the ellipsis discussion cited at l. 54, under the heading "A third approach: change of function without change of category". It sets out the ordinary-Head analysis for determinatives: "[38ii] … [Many] would agree with you … [determinative as head] … It would involve saying that in [ii] many belongs to the same category, determinative, in both cases, but functions as determiner in [iia], head in [iib]." It rejects the analysis because "it does not handle cases like: [39] i I prefer cotton shirts to [nylon] … ii … Mary earns [double]".

This is the "Separate D, ordinary Head" row of Table 1, and the grammar the paper adopts considered it in print. Search of the manuscript for `421`, `nylon`, `cotton`, `double`, `third approach`, `change of function`, `Many would`, and `without change of category`: the only hit is l. 54's `420--421`, cited for ellipsis alone. In §4, l. 478 ("even when fusion remains available for adjectives") answers the substance of CGEL's objection, but not as a reply to CGEL. Suggested repair: extend the l. 54 footnote, or the l. 50 sentence introducing ordinary Head, to note that *CGEL* considers this option and sets it aside because it doesn't cover modifier and predeterminer fusion (p. 421). §4 can then answer that fusion is kept for those cases. That satisfies Rapoport's rules and heads off a referee from the CGEL camp. The novelty sentence at l. 71 (limited to "those accounts") would still stand.
