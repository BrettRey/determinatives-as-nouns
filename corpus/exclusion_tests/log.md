# Corpus Screen: exclusion_tests

## Gathering Log

Site hit rate limit after 4+ queries within 5 minutes. Requested 1-2 minute wait before resuming.

### Completed:

- 2026-09-17: every_was.jsonl — 141 hits, 96 rows saved
- 2026-09-17: every_has.jsonl — 73 hits, 74 rows saved

### Blocked by Rate Limit:

- every_will — 82 hits (query returned but KWIC page blocked by rate limit)
- take_every — 24,479 hits (query returned but KWIC page blocked by rate limit)
- very_every
- very_some
- very_this
- so_every

**Status:** Site blocks automated access. After initial rate limiting (4+ queries in 5 minutes), attempt to resume with paced queries triggered automation detection. Message: "It looks like you might be trying to use some type of tool to automate access to the corpora, which is strongly discouraged. Please close the browser and start again."

Remaining queries are gathered by hand (Brett runs the query and saves the lines); no session or IP workaround is to be used.

## COCA hand-gathered (Brett, 2026-09-17)
Zero hits on COCA: every [v*z*], every [v*d*], every [vm*], every [y*], take every [y*], very a few, a quite few, no of the (files not saved). List counts: special someone 282, certain someone 120; so this 19,835, so some 1,732, so every 1,371 (discourse *so*; KWIC not saved). List counts in the exports: each of them is 146, has 140, was 103, have 46, are 23, were 9 (plural 17%); each of the [nn2*] was 151 vs were 73 over 173 strings. Files screened: art_adj_compound 496 lines, art_compound 494, each_of_them_v 75, each_of_the_pl_v 46, so_numerous_nn 4, too_numerous_nn 4, very_every_some_this 7; every [v*] 1,095 (every.odt). Raw exports in raw/.

## 2026-09-17, plural compound determinatives (COCA List, Brett)
somethings 590, nothings 416, nobodies 318, somewheres 178, somebodies 115, anywheres 51, nowheres 44, anythings 38, anybodies 20 (total 1,770). Caveats: *nothings* is largely *sweet nothings*; *somewheres/anywheres/nowheres* are dialectal adverb forms, not plurals; *somethings* includes *thirty-somethings* (CGEL p. 1716). Plural inflection on the set-denoting compound is attested; the §4.5/§5.5 clause stands, with these counts to be footnoted.

## 2026-09-17, opportunity comparison (COCA List, Brett)
each has 1,578; each was 1,005; each will 507; every will 12; every has 8; every was 3 (total 3,113). Independent each before a finite verb is about 134 times as frequent as every; the every hits are the surnames and slips read in every-reading.md.
