# Genitive *'s* on determinatives standing alone (17 Oct 2026)
<!-- SUMMARY: COCA hand searches for X 's with X = either, neither, each, all, many, few, some. Genitives: either 17/30, neither 6/23, each 12/12, many 3/76, some 1/24, few 0/22 bare, all 0 bare in 499 displayed lines (display-capped sample). Two labellers agree on every genitive line; either/neither/each counts match the 16 Oct batch. Brett judges all either's, neither's and each's fine, two web many's fine, the other many's and the some's questionable · status: done · updated: 2026-10-17 -->

Brett Reynolds searched COCA by hand on 17 Oct 2026 for each word followed by the token *'s* and pasted the full outputs in chat. CGEL says fused heads "either cannot occur in the genitive at all or do so only very rarely", with \**all's*, \**many's*, \**few's* and \**some's* "completely excluded" and *each's* "occasionally attested but of somewhat questionable status" (Huddleston & Pullum 2002: 420). The structural paper's §3 (fusion repo, `drafts/det-head.tex`) needs to know whether the genitive splits these words.

The raw lines, both sets of labels, the second labeller's report and a manifest with hashes are in the fusion repo at `reviews/corpus-genitive-20261017/` (gitignored, since it holds COCA text). Claude (Opus 5.5) labelled every line. A read-only subagent then labelled them again without seeing those labels. The two runs give **identical sets of genitive lines in all seven files** and differ only in how the non-genitive hits are classified (contraction, dialect, name, garbled).

## Counts

| Search | Lines | Genitive on the bare word | Other hits |
|---|---|---|---|
| `either 's` | 30 | 17 | 11 contractions (*Either's fine*); 2 the place name *Mount Either* |
| `neither 's` | 23 | 6 | 17 contractions (*Neither's the president*) |
| `each 's` | 12 | 12 | none |
| `many 's` | 76 | 3 | 69 contractions, mostly the frozen *many's the time*; 4 the museum association MANY |
| `some 's` | 24 | 1 | contractions, titles (*Everybody Wants Some's*), a nickname, 1 mention of the word |
| `few 's` | 22 | 0 | 21 names (Mark Few, Chris Few, William Few, FEW Spirits, the Chosin Few, the *FEW* dictionary); 1 genitive with a determiner, *the first few's salty freshness* (Ploughshares 1996), a Mod–Head case for §4 |
| `all 's` | 499 | 0 | 9 genitives on *you all* / *your all* (*you all's church*), a pronoun phrase, not bare *all*; the rest contractions (*all's well*), dialect *all's* = "all (that)" (*All's I know is*), titles, names (*Health Care for All's*), and garbled or tokenization lines |

The counts are raw. They aren't normalised for how often each word stands alone. The `many 's` list skips line 29 and the `all 's` list skips line 179 in the paste. The 500 lines for `all 's` were COCA's display limit, not the total (Brett: "there were many more hits"), so the `all` row is a sample of unknown ordering: it says nothing about genitive *all's* in the lines not displayed.

**Replication.** The same three searches for *each*, *either* and *neither* on 16 Oct (`corpus/genitive/2026-10-16-brett-supplied-anaphoric-fused-genitives.md`, batch 2) gave the same genitive counts, 12, 17 and 6, and the same edited-prose counts (FIC, MAG, NEWS, ACAD): *each* 5, *either* 6, *neither* 2. The 16 Oct KWIC lines weren't stored, so the match is in counts, not checked line by line. Today's genitives of *many* and *some* are all WEB.

## The genitive lines

- **either (17):** *no denying either's influence* (cleveland.com 2019); *recognize either's gear* (MilitaryHist 2015); *without reference to either's sexuality* (NewRepublic 2015); *crown prince in either's reigns* (CSMonitor 2015); *if either's cover was ever blown* (conservapedia 2012); *didn't even see either's face* (tvtropes 2012); *the stories from either's cultures* (blog 2012); *love on either's side* (tor.com 2012); *over either's head* (blog 2012); *because of either's "just a good friend"* (blog 2012); *ruining either's chances* (blog 2012); *in either's best interest* (bloodhorse 2012); *both in either's powers* (*The Tempest*, film 2010); *increase either's share of its market* (TIME 2000); *never see either's children* (Geraldo 1994); *in either's recollection* (Atlanta 1994); *within either's range* (SeaQuest 1994).
- **neither (6):** *Neither's numbers are all that encouraging* (WashPost 2014); *a certainty that neither's evidence warrants* (web 2012); *neither's predicament or conflict is resolved* (goodreads 2012); *neither's record is anything but drenched in blood* (blog 2012); *Neither's performance validates the claims* (blog 2012); *Neither's coaching ability will be affected* (Houston 1994).
- **each (12):** *around each's neck* (FantasySciFi 2014); *what each's strengths and weaknesses are* (entrepreneur.com 2012); *each's unique flows* (amazon.com 2012); *How does each's being differ* (scientificamerican.com 2012); *the breaks from each's story* (goodreads 2012); *finish each's sentences* (huffingtonpost 2012; = *each other's*); *to each's own* (blog 2012; perhaps reduced *to each his own*); *weighted by each's contribution* (climateaudit 2012); *discover each's whereabouts* (FantasySciFi 2007); *a strong sense of each's thoughts* (FantasySciFi 2007); *especially each's reliance on "professionalism"* (ArmedForces, ACAD 1996); *the highlight of each's day* (Atlantic 1995).
- **many (3), all web:** *pricing itself out of so many's reach* (poems.com 2012); *to many's suprise he won* (bleacherreport 2012); *promoted by many's parents* (jewschool 2012).
- **some (1), web:** *I don't blame all white people for some's ignorance* (politico 2012).

## Judgments

- Brett, 17 Oct 2026: the ten *either's* lines from cleveland.com, MilitaryHist, NewRepublic, conservapedia, tvtropes, tor.com, bloodhorse, TIME, Atlanta and SeaQuest "all strike me as perfectly fine".
- Brett, 17 Oct 2026, answering five follow-ups:
  - *each's*: "those three each's seem fine to me" (*especially each's reliance on "professionalism"*, ACAD 1996; *the highlight of each's day*, *Atlantic* FIC 1995; *what each's strengths and weaknesses are*, entrepreneur.com 2012).
  - *many's* / *some's*: "bleacher and poems seem fine": *to many's suprise he won* (bleacherreport.com) and *out of so many's reach* (poems.com). "jewschool and politico seem questionable": *promoted by many's parents* and *for some's ignorance*.
  - The seven *either's* genitives not on his list of ten: "they weren't on my list; they seem fine". So all 17 are fine to him.
  - *neither's*: fine ("yes", to *Neither's numbers are all that encouraging* and *Neither's coaching ability will be affected*).
  - `all 's`: "no there were many more hits"; 500 was the display limit.
- **Bearing.** *Each* joins *either* and *neither* as a simple fused determiner-head that takes the genitive acceptably, against CGEL's "of somewhat questionable status" (p. 420). For *many* the gap isn't absolute: two web genitives are fine to Brett, in frames like *to X's surprise* and *out of X's reach*. CGEL's requirement is graded ("for full acceptability", p. 420), so the structural paper doesn't rest anything on those two; it reports them in the counts footnote. The division between the two sets matches the one the 16 Oct record found (singular distributives against the quantity words), and that record's decision stands: the paper names the set, not the factor.

**Human check (18 October 2026).** Brett Reynolds checked the 18 genitive lines of *neither* (6) and *each* (12), which he hadn't judged before, and 10 non-genitive lines drawn at random (seed 18) from *either*, *neither*, *many*, and *some*. He agreed with every label. With his earlier judgments of the *either* lines and the *many*/*some* genitives, every genitive the counts rest on has now been read by a person. Spot-check file: fusion repo, private `reviews/corpus-case-adj-20261018/SPOT-CHECK.md`.
