# AdjPs in predeterminer function before *the*; *x-fold* (COCA, 17 Oct 2026)
<!-- SUMMARY: Brett's COCA searches for AdjPs functioning as predeterminer before definite determiners: none before the, the demonstratives, or any genitive pronoun (`[be] [j*] th*/my/... + measure noun`); `PUNC [j*] the [n*]` gave only mis-tagged *only*; one marginal x-fold line (*this is 400-fold the amount of …*, COCA BLOG 2012) of undetermined category; AdjPs do so only before *a* (Big Mess); supports *double* heading an NP in *double the cost* · status: recorded · updated: 2026-10-17 -->

Searches run by hand by Brett Reynolds on 17 Oct 2026, reported in the Claude Code session. Classification by Claude (Opus 5.5).

**Question.** In CGEL, the predeterminer modifiers before *the* are NPs or determinatives: fractions (*two thirds the price*), multipliers (*twice*, *three times*), *all*, *both* (p. 331). AdjPs function as predeterminer only "before the indefinite article" (p. 435: *such a*, *how large a piece*). Does any AdjP function as predeterminer before *the*? If none does, *double* in *double the cost* heads an NP, so it's a noun there, as CGEL says (pp. 418, 421).

## Searches

| Corpus | String | Result (as Brett reported it) |
|---|---|---|
| COCA | `PUNC [j*] the [n*]` | The only hits had *only* (e.g. *only the top*). CGEL treats that *only* as a focusing adverb functioning as NP-peripheral modifier, so these are a tagging artefact, not adjectives. *Double the …* didn't appear, probably because the tagger doesn't give *double* `jj` in that position. Note that the `PUNC` slot limits the search to positions right after punctuation. |
| COCA | a *-fold* + *the* search (exact string not pasted) | One relevant line (below). |
| COCA | `[be] [j*] th* size/amount/price/cost/volume/weight/height/length/time` | Nothing relevant. The `th*` slot covers *the*, the demonstratives (*this*, *that*, *these*, *those*) and genitive *their*, after *be*, which is where multiplier predeterminers usually occur (*is double the size*, *is twice the amount*). No AdjP functions as predeterminer in any line. As with the first search, *double* itself isn't tagged `jj` here, so the query tests for other adjectives, not for *double*. |
| COCA | `[be] [j*] my/your/his/her/our/its/their size/amount/price/cost/volume/weight/height/length/time/salary/age` | Nothing relevant. This covers every genitive pronoun determiner, in the same predicative frame (where *is three times his age* and *is half my salary* would occur). No AdjP functions as predeterminer in any line. |

## The *x-fold* line

| Source | Sentence | Reading |
|---|---|---|
| BLOG: biotechnologyforbiofuels.com/content/5/1/40, 2012 (a journal article in *Biotechnology for Biofuels*, filed under BLOG in COCA) | "In terms of carbon, the fossil fuels consumed in one year release 44? x? 10 18 g of carbon, and this is 400-fold the amount of annual carbon fixed during net primary productivity by the global biota" | A real predeterminer use. *400-fold the amount of …* is one NP functioning as predicative complement of *is*, parallel to *400 times the amount of …*. Not an adjunct followed by a postposed object, which *be* doesn't allow. The *?* marks and spacing are conversion artefacts in the source. |

**Bearing.**
- **CGEL gives *x-fold* both categories.** It lists *three-fold* among adjective–adverb pairs "where there is little if any difference in meaning" (p. 568): adjective in *a threefold increase* and *the increase was threefold*, adverb in *rose threefold*.
- **The line can't settle which *400-fold* is.** As an adjective, this is a marginal exception to "no AdjP as predeterminer before *the*". As an adverb, it's in the position CGEL gave adverb *twice* (*twice the amount*, p. 434). Payne, Huddleston & Pullum (2007, p. 596) reassigned *twice* because *two times* "can replace it in both functions" and "is uncontroversially an NP in both cases".
- **By that substitution, *x-fold* behaves like an NP in two uses.** *400 times the amount* replaces the predeterminer use, and *increased 400 times* replaces the adjunct use. *X-fold* keeps its adjective uses, which *400 times* lacks (*a 400-fold increase*). So *x-fold* may split the way *double* does, rather than being a pure adjective control.
- **Caution.** Brett (2024, JL, following Payne, Huddleston & Pullum 2010) holds that distributional differences alone shouldn't settle category. The substitution test, and the argument from predeterminer distribution that *double* is a noun there, are suggestive, not decisive.
- **Before *a* it's different.** AdjPs do function as predeterminer before indefinite *a*, in the Big Mess construction: *how large a piece*, *so good a bargain* (CGEL p. 435; Van Eynde 2007, who also gives \**How serious some problem is it?*).
- **Net.** Before definite determiners (*the*, the demonstratives, every genitive pronoun), predeterminer phrases are NPs (searches above). *Double* functions there routinely and *x-fold* only marginally (this one line, in technical prose, probably formed on the model of *400 times the*).
