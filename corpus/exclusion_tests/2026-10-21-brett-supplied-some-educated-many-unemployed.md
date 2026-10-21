# *Some educated* and *many*/*some unemployed* with no noun: NOW, 21 October 2026
<!-- SUMMARY: "unemployed" heads the nominal after many, some, how many, too many, and so many in all 34 NOW lines the display returned (its numbering skips 5 rows, a display glitch per Brett), many in edited US, British, and Commonwealth news (Reuters, Washington Post, Politico, Guardian); "educated" does so after some in 3 distinct utterances, all outside Britain and the US, and 9 lines are attributive "educated guesses"; with the these-rich record, the determiners the rich type takes vary by adjective; against CGEL p. 417 · status: record; labels Claude's · updated: 2026-10-21 -->

**Source.** Brett Reynolds ran two NOW searches by hand on 21 October 2026 and pasted the displays into the Claude session. Brett confirmed both query strings afterwards.
- **First display:** query *many/some educated [v\*]*, confirmed by Brett; it includes the two *many educated* lines already recorded in `2026-10-21-brett-supplied-these-rich.md`. Rows 9 and 12 are absent from the site's display (Brett confirms he pasted everything returned).
- **Second display:** query *many/some unemployed [v\*]*, confirmed by Brett. The hits include *how many*, *too many*, and *so many*, which contain *many*. Rows 7, 11, 12, 18, and 24 are absent from the site's display (Brett confirms he pasted everything returned).

Raw lines and per-line labels are kept privately in the fusion repo (`reviews/corpus-these-rich-20261021/`, gitignored; raw-educated-unemployed.txt sha256 bc6bfb0f…, labels-educated-unemployed.tsv sha256 591df08a…). Labels are by Claude (Opus 5.5), in one pass.

**Why it was run.** These searches follow `2026-10-21-brett-supplied-these-rich.md`. *CGEL* says NPs of the *rich* type "are determined by the definite article" (p. 417), and it lists *the unemployed* in that type. Glass (2019: 7) cites *Some fired say …* and *Many educated are far from role models* from the web.

**Result, *educated*.** Of 15 rows:
- **9 are attributive**: *educated guesses* (8) and *educated forecasting* (1).
- **6 have *educated* heading the nominal.**
  - Two are *many educated*, already recorded.
  - Four are *some educated*, three distinct utterances:
    - *It is like some educated are now becoming backward thinkers*: quoted speech in *Pulse*, Ghana, 2021, and quoted again by *PinkNews*, Britain;
    - *Some educated behave as if they lack wisdom*: a headline quoting a speaker, timesnownews.com, India, 2020;
    - *which some educated are not*: a reader's comment, dawn.com, Pakistan, 2019.

**Result, *unemployed*.** All 34 lines the display returned have *unemployed* heading the nominal. The numbering runs to 39, but rows 7, 11, 12, 18, and 24 are absent from the site's display itself; Brett confirms he pasted everything returned. The determiners:

| Determiner | Lines | Example |
|---|---|---|
| *many* | 18 | *many unemployed say they are having trouble getting hired* (*Washington Post*, 2021) |
| *some* | 7 | *some unemployed will have to do unpaid work* (*Daily Mail*, 2010, reported speech) |
| *how many* | 7 | *How many unemployed are there in Australia?* (*Bendigo Advertiser*, 2020) |
| *too many* | 1 | *Too many unemployed remain on the sidelines* (*Forbes*, 2021) |
| *so many* | 1 | *with so many unemployed looking for jobs* (*Guardian*, Britain, 2015) |

Two rows (*Hereford Times* and wpxi.com) carry the same wire text, so 33 texts are distinct.

The sources are mostly edited news:
- US: Reuters, the *Washington Post*, Politico, *Forbes* (2), SFGate;
- Britain: the *Guardian*, the *Daily Mail*;
- Australia, New Zealand, and Canada: the *Brisbane Times*, *Canberra Times*, Stuff, Newshub, The Spinoff, News1130;
- outer-circle news from India, Malaysia, the Philippines, South Africa, and Nigeria.

One line has a singular verb: *how many unemployed is worth one death* (theguardian.com, 2020, inside a quoted remark).

**Parsing.**
- *Unemployed* and *educated* keep their adjective status by *CGEL*'s tests (p. 417): they have no plural ending, and they take adverbs (*the chronically unemployed*, *the highly educated*).
- They are not post-head restrictors after a bare *many* or *some*, because neither adjective follows a noun on its own the way *present* does (\**people unemployed want jobs*).

**Bearing.**
- The determiners that the *rich* type takes vary by adjective.
- *Unemployed* takes *many* and *some* freely, in edited inner-circle news. *Rich* takes *these* and *educated* takes *some* or *many* only rarely, and outside Britain and the United States.
- *CGEL*'s "determined by the definite article" (p. 417) is wrong for *unemployed*, one of the words it lists, and too strict for the others.
- On both fusion and ordinary Head the range is stated word by word, so the comparison is unchanged. The result strengthens that phrasing in the fusion paper (`mod-head.tex`, Table 1).
