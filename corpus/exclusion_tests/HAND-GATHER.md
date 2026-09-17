# Hand-gather sheet: exclusion tests on COCA (NOW as fallback)
<!-- SUMMARY: copy-paste query strings for the counterexample searches, with mode, file name, and what the KWIC sample will and won't show · status: waiting on Brett · updated: 2026-09-17 -->

Paste each string into the COCA search box. COCA is fast, edited and genre-balanced, and its attestations carry more weight with a referee than NOW's news-and-comment register, which supplied most of the noise in the *every* lines. Use NOW only where a rare probe returns under about ten hits on COCA, and prefix that file `now_`; prefix COCA files `coca_`. **List** mode shows one row per alternative with its frequency (one query); clicking a row loads its KWIC (one more). **KWIC** mode loads a mixed sample of all alternatives at once (one query plus one load) but draws the 100 or 500 lines in proportion to frequency, so a rare alternative can vanish behind a common one. The rule below: alternatives of similar frequency go in one KWIC; anything expected to be rare is queried on its own or read from the List counts first. Save each KWIC as the file named, in `corpus/exclusion_tests/` (SAVE export, or the rows copied `n date country source text`, or JSONL). Then `/corpus-screen screen exclusion_tests`; the screen tells alternatives apart from the line itself.

Two count-only strings need no KWIC: write the List counts into `log.md`.

## Independent *every* (manuscript: #*I'll take every*, #*Every arrived*)

| Paste | Mode | Save as | Why this shape |
|---|---|---|---|
| `every [v*z*]` | KWIC, 500 | `coca_every_vz.jsonl` | *every* + third-person-singular present verb (*is, has, does, goes*); the finite-verb shape independent subject *every* needs |
| `every [v*d*]` | KWIC, 500 | `coca_every_vd.jsonl` | *every* + past-tense verb (*was, were, had, did, arrived*) |
| `every [vm*]` | KWIC, 100 | `coca_every_vm.jsonl` | *every* + modal (*will, can, would*) |
| `every [y*]` | KWIC, 100 | `coca_every_punct.jsonl` | *every* before punctuation: the *take every.* shape, sentence-final independent use |
| `take every [y*]` | KWIC, 100 | `coca_take_every_punct.jsonl` | the manuscript's own starred example; `take every` alone is 24,479 hits of *take every opportunity* |
| `each/every was/has/will` | List only | counts to `log.md` | rate comparison, six counts in one query; on NOW *every was* was 141 and *every has* 73, so the COCA counts will be small but the ratio to *each* is the point |

## Degree adverbs on non-gradable determinatives (#*very every*, #*very some*, #*very this*)

| Paste | Mode | Save as | Why |
|---|---|---|---|
| `very every/some/this` | List, then KWIC of any row over ~30 | `coca_very_every_some_this.jsonl` | three probes at once; *very this* will be mostly *the very this-and-that*; the screen's question is whether *very* grades the determinative |
| `so every/some/this` | List, then KWIC of any row over ~30 | `coca_so_every_some_this.jsonl` | same with *so*; expect *so every day*-type splits |

## Order inside the complex determinative (#*very a few*, #*a quite few*)

| Paste | Mode | Save as | Why |
|---|---|---|---|
| `very a few` | KWIC, all | `coca_very_a_few.jsonl` | rare; read everything; if COCA gives under ten, repeat on NOW as `now_very_a_few.jsonl`. Register question flags non-native text |
| `a quite few` | KWIC, all | `coca_a_quite_few.jsonl` | same, with the same NOW fallback |

## Attributive *so numerous* (#*so numerous mistakes*)

| Paste | Mode | Save as | Why |
|---|---|---|---|
| `so numerous [nn*]` | KWIC, 100 | `coca_so_numerous_nn.jsonl` | the noun tag selects attributive position directly; predicative *were so numerous that* is excluded by the query |
| `too numerous [nn*]` | KWIC, 100 | `coca_too_numerous_nn.jsonl` | same test with *too*; *too numerous to mention* is excluded by the tag |

## Partitive *no* (#*no of the students*)

| Paste | Mode | Save as | Why |
|---|---|---|---|
| `no of the` | KWIC, all | `coca_no_of_the.jsonl` | rare; expect typos for *none/one* and *No.* abbreviations; NOW fallback if empty |

## Compounds with a pre-head adjective or external determiner (manuscript: the compound construction excludes both)

| Paste | Mode | Save as | Why |
|---|---|---|---|
| `[at*] [j*] someone/somebody/something` | KWIC, 500 | `coca_art_adj_compound.jsonl` | article + adjective + compound: *a special someone, that certain something, the right somebody*. The general shape, not two idioms |
| `[at*] someone/somebody/something` | KWIC, 100 | `coca_art_compound.jsonl` | article + compound with no adjective: *a something*, *the somebody*; expect *a something-or-other* and *the something* in titles |
| `special/certain someone` | List only | counts to `log.md` | the two idioms' raw frequency, for the paper's footnote if the shape above is attested at volume |

## Number transparency in *each of the people* (manuscript: singular *each of the people* doesn't take its number from *people*)

| Paste | Mode | Save as | Why |
|---|---|---|---|
| `each of them was/were/is/are/has/have` | List, then KWIC of the plural rows | `coca_each_of_them_v.jsonl` | the List counts are the result: singular against plural agreement after *each of them*. KWIC only the plural rows (*were, are, have*), which are the claim-relevant ones |
| `each of the [nn2*] was/were` | List, then KWIC of the *were* row | `coca_each_of_the_pl_v.jsonl` | plural noun in the partitive, then the verb; *were* lines are the transparency cases |

## Notes on the syntax (from the site's help page, help/word-phrase.asp)

**Excluding a mis-tagged word.** There is no AND inside one slot: `-` negates a whole slot (the help's example is `pretty -NOUN`, *pretty* followed by a non-noun), so `every [v*] -inch` would be a three-word search. Two ways round it. Narrow the tag instead: *every inch* is mis-tagged as a base-form verb (VV0), so the finite sub-families `[v*z*]`, `[v*d*]`, `[vm*]` above exclude it and every other base-form mis-tag, and finite verbs are what the test needs anyway. Or run the broad `every [v*]` in List mode, where each string is a row, tick the rows you want and open the KWIC for the selection, leaving *every inch* unticked.


`/` alternates single words only; a phrase alternative needs separate queries. `[v*]`, `[nn*]`, `[nn2*]`, `[j*]`, `[at*]`, `[y*]` are the CLAWS tag families (verb, noun, plural noun, adjective, article, punctuation); tagging errors are common around *every* and the compounds, which is one more reason the screen reads the line rather than trusting the tag. Lowercase searches are case-insensitive. Keep the file names above so the screen's spec finds the right question for each string.
