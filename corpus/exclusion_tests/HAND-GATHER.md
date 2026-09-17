# Hand-gather sheet: exclusion tests
<!-- SUMMARY: strings Brett runs himself on NOW, with the file each should be saved as; the screen runs on the saved files · status: waiting on Brett · updated: 2026-09-17 -->

Run each string on NOW (KWIC, 100 lines is enough; 500 if cheap), SAVE or copy the rows, and drop them as `corpus/exclusion_tests/<file>` (any of: the SAVE export, pasted rows `n date country source text`, or JSONL). Then `/corpus-screen screen exclusion_tests`. The two count-only strings need only the hit count, written into `log.md`.

| String | File | Claim under test | Note |
|---|---|---|---|
| every will | every_will.jsonl | independent *every* | 82 hits seen |
| take every | take_every.jsonl | independent *every* (#I'll take every) | 24,479 hits, mostly *take every opportunity*; the screen will sort them |
| very every | very_every.jsonl | #very every | |
| very some | very_some.jsonl | #very some | |
| very this | very_this.jsonl | #very this | expect *very this-or-that*; screen sorts |
| so every | so_every.jsonl | degree so on every | |
| very a few | very_a_few.jsonl | #very a few | |
| a quite few | a_quite_few.jsonl | #a quite few | |
| so numerous | so_numerous.jsonl | #so numerous mistakes (attributive) | |
| no of the | no_of_the.jsonl | #no of the students | |
| special someone | special_someone.jsonl | compounds exclude a pre-head adjective | |
| certain someone | certain_someone.jsonl | same | |
| a something | a_something.jsonl | compounds exclude external determination | |
| each of them were | each_of_them_were.jsonl | number transparency in *each of the people* | |
| each of them was | each_of_them_was.jsonl | same, singular baseline | |
| each was | count only | rate comparison for *every was* (141) | hit count into log.md |
| each has | count only | rate comparison for *every has* (73) | hit count into log.md |
