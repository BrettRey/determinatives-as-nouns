# Genitive *'s* on bare *many*, *some*, *all*, *few* in NOW (20 Nov 2026)
<!-- SUMMARY: NOW hand searches with the noun fixed: many's 39 before six surprise-type nouns and at least 41 before seven attention-type nouns; some 3, all 2, few 0 before the surprise-type nouns; before seven radar/list/hands/mind nouns, many people's 2,264 against many's 6, few people's (no a) about 20 against few's 0 (six hits, all the surname). Brett's judgments: to many's surprise fine (17 Oct); the some's and all's sentences 5/7 and 3/7; on many's/few's radar 3/7, changed many's/few's minds 2/7. Supersedes the 17 Oct record's note that the paper rests nothing on many's · status: done · updated: 2026-11-20 -->

Brett Reynolds searched NOW (english-corpora.org) by hand on 20 November 2026 and pasted the displays into a Claude Code session. The open search `many 's [nn*]` timed out, so every search below fixes the following noun. The searches show where the genitive occurs; they can't show how its uses are distributed across nouns.

The raw displays are in the fusion repo at `reviews/corpus-now-genitive-20261120/` (gitignored), extracted verbatim from the session transcript, with a manifest and hashes. Claude (Opus 5.5) labelled the lines in one pass. A read-only Claude subagent then recounted every number and checked every quoted line against the displays, without seeing the labels' reasoning, and found them correct (its report: fusion repo, private `reviews/genitive-now-20261120/batch1/independent-read-2026-11-20.md`). Brett checked none of the labels by hand. Since the noun is fixed, a hit can't be a contraction (*many's the time*), so the labels mostly separate genitives on the bare determinative from names and garbled lines.

## Counts

| Search | Hits | Genitive on the bare word | Other |
|---|---|---|---|
| `many 's surprise\|dismay\|delight\|chagrin\|disappointment\|relief` | 39 | 39 | none; one *too many's relief* (a slip for *to*); surprise 27, dismay 6, delight 3, disappointment 2, relief 1 |
| `many 's attention\|eyes\|minds\|mind\|expectations\|sentiments\|hearts` | at least 45 (KWIC numbered 1–45; 41 lines pasted) | all 41 read | one *so many's eyes*; one quotation reported by two outlets; attention 19, eyes 11, expectations 4, hearts 4, minds 3 |
| `some 's` + the six surprise-type nouns | 3 | 3 | none |
| `all 's` + the six surprise-type nouns | 3 | 2 texts | one Den of Geek article in two editions |
| `few 's` + the six surprise-type nouns | 0 | 0 | (reported by Brett; no display) |
| `many people 's radar\|radars\|list\|lists\|hands\|minds\|mind` | 2,264 | n/a | minds 1,644, lists 150, radar 120, hands 98, list 94, mind 84, radars 74 (the interface's totals) |
| `many 's` + the same seven nouns | 7 | 6 | *Man of Many's list* (a website); one of the six is *as many's hands as possible* (quoted speech) |
| `few people 's` + the same seven nouns | 72 lines pasted (1–73, 17 absent) | n/a | about 20 with no *a* before *few* (15 bare, 5 with *very*, *too* or *so*); about 52 *a few*, *quite a few*, *more than a few*, *a select few*; one garbled line |
| `few 's` + the same seven nouns | 6 | 0 | all the surname Few (Mark Few ×5, Christopher Few) |

**Rates.** The six surprise-type nouns gave 39 *many's* in NOW, which is about 32 billion words by its country table. COCA's 3 bare *many's* came from an unrestricted search of a far smaller corpus. The two rates are of the same order; NOW is larger, not different.

**What the zero for *few* means.** Before the seven radar-type nouns, *many's* is about 1 in 380 of *many people's*. At that ratio, about 20 *few people's* predicts well under one *few's*, so the zero is uninformative. The surprise-type nouns are odd for *few* anyway, since *few* is negative.

**NOW and GloWbE, `many 's [nn*]` (Brett, in review comments, 20 Nov).** NOW's quick list gave *surprise* 25 and *attention* 20 (total 45). It's partial: the interface offers "see full list (slower; may time out)". Limiting the search to any NOW section returned 0 hits, which looks like a glitch. GloWbE gave 22 tokens over 17 nouns:

- opinion, introduction, rejection, chagrin, eggs: 2 each
- charter, view, top, *suprise*, standards, reach, programs/services, parents, husbands, heart, eyes, expectations: 1 each

Most of these fall outside the surprise and attention types. No GloWbE lines were displayed, so none are labelled or cited.

## Lines relied on in the structural paper (§3)

- *To many 's surprise, the preseason No. 2 Huskies have struggled so far this season.* (*Sports Illustrated*, 2022-01-05)
- *the Black Pumas song " Colors " is the first thing that grabs many 's attention.* (CBS News, 2021-03-09)
- *The Jets, to some 's surprise, are the stiffest team in the league.* (au.sports.yahoo.com, 2019-12-10)
- *But to all 's surprise, the U.S. dollar isn't the strongest currency* (*Forbes*, 2023-05-06)
- *he played right into Mark Few 's hands* (spokesman.com, 2023-03-08), the surname
- Also checked, not quoted:
  - *much to others' surprise and many 's disappointment* (PBS, 2020-06-12)
  - *a legend in so many 's eyes and mine* (birminghammail.co.uk, 2022-08-04)
  - *capture many 's eyes ... captures the hearts of many people* (tuko.co.ke, 2020-07-13)

## Judgments

- Brett, 17 Oct 2026, from the earlier record: *to many's suprise he won* (bleacherreport) and *out of so many's reach* fine; *promoted by many's parents* and *for some's ignorance* questionable.
- Brett, 20 Nov 2026, on a 7-point scale:
  - *The Jets, to some's surprise, are the stiffest team in the league* 5/7
  - *But to all's surprise, the U.S. dollar isn't the strongest currency* 3/7
  - on sentences Claude constructed: *The proposal was on few's radar at the time* 3/7 and *Her testimony changed few's minds* 2/7; the same sentences with *many's*, 3/7 and 2/7 ("yes, my rating", in review)
- In the paper, 5/7 is rendered "a little less natural" and 3/7 "questionable" (Brett: "fine", in review).

## Bearing

- **CGEL.** It calls *all's*, *many's*, *few's* and *some's* "completely excluded" (Huddleston & Pullum 2002: 420). That fails for *many*, *some* and *all*: all three occur in edited news, and *to many's surprise* is fine to Brett.
- **Many against few.** Before the same nouns, *many's* and *few's* rate alike to him, and both poorly. The corpus can't show whether *few's* is excluded or only rare.
- **The paper's §3** now:
  - cites these searches;
  - keeps the number generalization in a narrowed form (singular words take the genitive freely, plural and non-count ones rarely, if at all);
  - states that the contexts in which *many's* is fine would still need a statement.
- **The 17 Oct record** said the paper "doesn't rest anything on" the fine *many's* genitives. That's superseded: the dilemma for CGEL's argument from case now includes *to many's surprise*.
