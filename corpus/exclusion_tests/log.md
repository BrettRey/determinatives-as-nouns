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

**Status:** Site rate-limited after 4+ queries within 5 minutes. Message: "You have done 4 queries or more in the last 5 minutes, which have taken a long time to run. Please wait 1-2 minutes before doing more searches."

The site blocks access to KWIC pages when query rate exceeds limit. Additional manual queries or a longer wait period (several hours) needed to complete remaining 6 searches.
