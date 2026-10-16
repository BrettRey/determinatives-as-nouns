# Genitives on anaphoric and generic fused heads (COCA, 16 Oct 2026)
<!-- SUMMARY: classification of 498 COCA lines for the latter/former/other/poor/rich + 's, gathered by hand by Brett; anaphoric fused heads take the genitive freely and the poor's is attested in edited prose, so a silent head doesn't explain *some's · status: done (two batches); query strings and the many result to confirm · updated: 2026-10-16 -->

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

## Batch 2: the follow-up queries (pasted by Brett, 16 Oct 2026)

**`the few 's`**: 2 lines, both names: *the Few 's SUV* (surname; CNN 2015) and *the FEW 's statement* (the *Französisches Etymologisches Wörterbuch*; *Hispanic Review* 1993). A third line, *the few one's that's right here* (*State Property*, 2002), came with the paste; it has *one's* for *ones*, so it isn't the construction. No genitive on *the few*. Nothing was shown for `the many 's`; whether it returned zero hits is to confirm.

**`each 's`, `either 's`, `neither 's`**: 67 lines. Labels are in `2026-10-16-each-either-neither-few-many.labels.txt`; N = *Mount Either* (a name) or a hyphenated *either-more's* / *either-she's*.

| Form | G | C | N | Of the G lines, in edited written prose (FIC, MAG, NEWS, ACAD) |
|---|---|---|---|---|
| *each 's* | 12 | – | – | 5 |
| *either 's* | 17 | 11 | 4 | 6 |
| *neither 's* | 6 | 17 | – | 2 |

**Examples:**

- *each*: "and especially each 's reliance on " professionalism. "" (COCA source *ArmedForces*, ACAD 1996, l. 58); "the highlight of each 's day" (*Atlantic* 1995, l. 59)
- *either*: "won't substantially increase either 's share of its market" (*TIME* 2000, l. 56); "without reference to either 's sexuality" (*New Republic* 2015, l. 7)
- *neither*: "Neither 's numbers are all that encouraging" (*Washington Post* 2014, l. 10); "Neither 's coaching ability will be affected" (*Houston Chronicle* 1994, l. 63)

**Outcome.** This is the first branch of point 5. The simple determinatives *each*, *either*, *neither* take the genitive in edited prose, so the gap isn't a property of determinative-headed NPs, whether fused, silent-headed or ordinary. *The few* has none (and *the many* none shown). The forms that lack it are the quantity expressions on *CGEL*'s list (*all*, *many*, *few*, *some*; p. 420). The forms that have it are distributive or anaphoric singulars: *each*, *either*, *neither*, *latter*, *former*, *other*. The generic class (*the poor*) is marginal. The two groups differ in two ways at once, quantity against individuation and plural against singular, so these data don't say which factor the gap follows. They do show it isn't category or structure. Every account has to state it, and none derives it from structure. The paper names the set and not the factor.

- **Fusion.** *CGEL*'s case-matching reason fails for fused determiner-heads themselves: *each*, *either*, *neither* are fused determiner-heads in *CGEL*'s analysis, and they take the genitive. That adds to the compounds (p. 479) and *the latter's*.
- **Silent nouns.** The concession in the fusion paper's §10 goes.
- **Ordinary Head.** It gains nothing specific. It states the gap as the other two must.
