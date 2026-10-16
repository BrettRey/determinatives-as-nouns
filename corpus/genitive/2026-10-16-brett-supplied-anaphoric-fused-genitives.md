# Genitives on anaphoric and generic fused heads (COCA, 16 Oct 2026)
<!-- SUMMARY: classification of 498 COCA lines for the latter/former/other/poor/rich + 's, gathered by hand by Brett; anaphoric fused heads take the genitive freely and the poor's is attested in edited prose, so a silent head doesn't explain *some's · status: done; exact query string and totals to confirm; follow-up queries proposed · updated: 2026-10-16 -->

**Source.** COCA concordance pasted by Brett Reynolds on 16 Oct 2026: 500 numbered lines (184 and 474 absent from the paste, so 498), dated 2019 back to 1990, covering the five forms the reading note proposed (`notes/2026-10-16-ellipsis-readings.md` in the fusion repo). The exact query string, and whether the display is a capped sample, are still to confirm. The KWIC lines aren't stored here; the line-by-line labels are in `2026-10-16-anaphoric-fused-genitives.labels.txt` (line number, form, label). Classification by Claude (Opus 5.5), reading each line.

**Labels.** G = genitive on the fused head (head or independent genitive). C = contraction of *is*/*has* (*the other 's a moron*). E = slip for plural *others'* (*the other 's will think*). N = not the construction: the noun *Other* (*the Other 's humanity*) or a name (*Little Sisters of the Poor 's*, *the Rich 's* department store and ship).

| Form | G | C | E | N | Lines |
|---|---|---|---|---|---|
| *the latter 's* | 149 | 2 | – | – | 151 |
| *the former 's* | 31 | 1 | – | – | 32 |
| *the other 's* | 253 | 34 | 5 | 8 | 300 |
| *the poor 's* | 8 | – | – | 1 | 9 |
| *the rich 's* | 3 | – | – | 3 | 6 |

**Examples** (line numbers in the paste):

- *the latter*: "prior to the latter 's U.S. debut" (*Sports Illustrated* 2018, l. 11); independent: "takes the former's threats better than the latter 's" (tfwiki 2012, l. 77)
- *the former*: "with only the former 's descriptions for fuel" (*Ars Technica* 2019, l. 3)
- *the other*: "neither she nor Eisenburg would ever know the other 's actual trade" (*New Yorker* 2019, l. 1); independent: "One contains twice the other 's" (2012, l. 105)
- *the poor*, ACAD and MAG: "the poor 's perception of wealth" (*Studies in the Novel* 2018, l. 14); "the poor 's material well-being has improved" (*Newsweek* 2010, l. 215); "raise all boats--even the poor 's" (*US Catholic* 2012, l. 68); "satisfying the poor 's basic needs" (*Latin American Research Review* 2000, l. 329); "solve all the poor 's problems" (1999 ACAD, l. 351); WEB: ll. 110, 128, 131
- *the rich*, WEB and BLOG only: "take the rich 's money" (l. 93); "with the rich 's money" (l. 136); "protection from the rich 's avarice" (l. 198)

**Bearing.**

1. *Latter* and *former* are the clean cases (180 genitives). They don't pluralize, and *CGEL* names *the former*/*the latter* as fused heads with special interpretation (p. 416, [23ii]). *Other* is weaker evidence: it has a plural, *the others*, so a noun analysis of *the other's* is open to an opponent (how *CGEL* treats *others* not yet located). *CGEL* also treats *the rich*, *the very poor* as fused heads (p. 417).
2. *CGEL* says fused heads "either cannot occur in the genitive at all or do so only very rarely" (p. 420). *The latter's* and *the former's* contradict that. *CGEL* argues the reason from determiner function only (the genitive belongs to the head, not the determiner). Extending it to a fused modifier-head, which would also exclude *the latter's*, is this record's inference, not *CGEL*'s claim.
3. For the silent-noun accounts this is a dilemma, not a refutation. Either *the latter* has a silent head, in which case a silent head doesn't block *'s*, and the silent noun doesn't explain *\*some's*. Or *the latter* falls outside their licensing, in which case it's a counterexample to that licensing. Lobeck rules out *the [e]* because *the* lacks agreement (1995: 88), and nothing in her system licenses *the latter [e]*. Kester allows only [+human, +generic, +plural] (1996: 77). Llombart-Huesca requires *one* after *the* + adjective (2002: 66–67). Only Günther's contrast condition might license it. So the second horn reaches the first three accounts, and the first horn reaches Günther and any account that does license it. The fusion paper's §10 concession to silent nouns rests on the first horn's explanation.
4. Pullum stars *the poor's*: "*The poor's houses aren't as interesting to visit as the rich's" ((6b), 1975: 176, checked in the scan). The five ACAD/MAG lines above attest it in edited prose, against his use of the possessive as a test for "nouniness" (p. 176). It's rare next to *the latter's* (8 to 149 in these lines), and *the rich's* appears only on the web.
5. The gradient *latter's* 149 : *poor's* 8 : *rich's* 3 among adjectival fused heads can't come from category, since all three are adjectives. It fits referentiality: a specific antecedent-identified individual vs a generic class. *CGEL* says *each's* is "occasionally attested" (p. 420). So the next queries are a test with two outcomes: `the few 's`, `the many 's`, `each 's`, `either 's`, `neither 's`.
   - If *each's*, *either's* or *neither's* turn up in edited prose, the gap is referential. Ordinary Head and the silent noun both have to state it, and the concession to silent nouns goes without ordinary Head gaining anything.
   - If they're absent along with *the few's* and *the many's*, the category reading survives: simple determinatives lack the genitive while adjectival fused heads have it.
   - Neither reading goes into the paper on the current data.
