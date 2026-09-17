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
Zero hits on COCA: every [v*z*], every [v*d*], every [vm*], every [y*], take every [y*], very a few, a quite few, no of the (files not saved). List counts: special someone 282, certain someone 120; so this 19,835, so some 1,732, so every 1,371 (discourse *so*; KWIC not saved). each/every was/has/will counts: see the pasted List if saved. Files screened: art_adj_compound 496 lines, art_compound 494, each_of_them_v 75, each_of_the_pl_v 46, so_numerous_nn 4, too_numerous_nn 4, very_every_some_this 7; every [v*] 1,095 (every.odt). Raw exports in raw/.
