# Numbers audit, 15 October 2026

<!-- SUMMARY: numbers-audit pass run by GPT-6 via Codex (second model) on determinatives-as-nouns.tex at 2e586d1; 80 grouped entries; 2 mismatches and 1 missing record confirmed, 4 uncertain items resolved or narrowed; proposed fixes await Brett · status: fixes 1, 2, 5 (item 7), 6 (item 8) applied 2026-10-15; items 3 and 5 (data) open · updated: 2026-10-15 -->

Auditor: GPT-6 through `tools/codex/bin/codex-readonly`, as the registry procedure requires (a model other than the one that wrote the numbers). The raw output, prompt and manifest are in `reviews/external-codex-numbers-20261015/` (kept local, not published). Codex checked 80 grouped entries: every number added since `af63c84` (19 September) and, by its own account, essentially all other numerical claims in prose and footnotes. Table cells checked by `quant_table.py` and `exclusion_table.py` were out of scope. Claude (this session) verified each non-MATCH item against the manuscript and records.

All other entries are MATCH, including every count added in October:
- *a bit much* 454/434/96;
- *too little, too late* 403/199/120;
- *the some* 197/10/53/50 with 15 + 2 + 24 + 9;
- the pronoun counts 350/129/124/352, 99 of 100 and 193 of 198;
- *all the better* 90;
- CGEL's ten degree determinatives.

Codex also rechecked the 13 *each of them* exclusions behind the new 62-of-75 figure and confirmed them (eight untensed *have*, five other subjects).

## Findings, verified

**1. MISMATCH, line 336: "single determinatives spelled as two words".** *A great many* is three words. Confirmed.

> {~~spelled as two words~>spelled as more than one word~~}

**2. MISMATCH, line 171 footnote: "12 more predicate it of an object".** Confirmed against the 12 lines in the *too little, too late* record:
- 8 are complements of *as*: lines 51, 98, 139, 150, 155, 157, 186, 190, including two passives (*was seen as*, *were regarded as*) and *came as*;
- 3 are complex-transitive complements without *as*: 60 *makes*, 158 *called*, 168 *consider*;
- 1 is a verbless supplement: 61 *though too little, too late*.

Only 8 of the 12 predicate the phrase of an object.

> and 12 more {~~predicate it of an object~>are predicative in other frames, 8 of them complements of \mention{as}~~} (\mention{derided the move as too little, too late})

**3. NO SOURCE, line 161 footnote: the two *become those* lines** (*JournalEcumenical*, ACAD 2015; *CBS 48 Hours*, SPOK 2007). They entered with the 19 September commit (`af63c84`). The only traces are `notes/rd-review-2026-09-19*.md` and the snapshots, and no corpus record holds the lines. Fix: Brett re-runs `[become] those who` and `[become] those that` in COCA and pastes the two lines, so they get a record. Until then the footnote's source labels and years stand unverified.

**4. UNCLEAR, line 171 footnote: "198 texts".** The record's interface header says 198 texts and the saved display has 199 rows. A text can hold two hits, and the footnote says "texts". No manuscript change. The record could note the 199 rows.

**5. UNCLEAR, line 171: "the commoner *a bit much*".** Codex is right that the comparison isn't matched. 454 is verb + *a bit much* anywhere; 69 is `[be] a little much` sentence-final only. A matched figure: *be*-forms + *a bit much* = 370 (from the 454 list), against *be* + *a little much* without the sentence-final restriction, which hasn't been searched. **Data needed:** Brett runs `[be] a little much` as a frequency list. If it comes back well under 370, "commoner" stands on a matched comparison and the footnote can give both numbers.

**6. UNCLEAR, line 175 footnote: "November 2025" for the Stanford CS329X slides.** Resolved. The PDF at the cited URL was fetched today. Its title page reads "Alice Oh … Nov 2025" and its internal title is "Copy of 20251109 Codeswitching LLMs". MATCH.

**7. UNCLEAR, line 454 footnote: "5 have it" (*few would*).** Confirmed. Brett's own marks in `few_would.reading.md` are `[x]` for lines 35, 57, 87 and `[x]?` for 7 and 69.

> 82 have nothing in the visible context that supplies the set, {~~5 have it~>3 have it and 2 probably do~~} (…), and 7 can't be decided

**8. UNCLEAR, line 828 footnote: plural compound counts.** The six counts are raw form counts. `corpus/exclusion_tests/log.md` (17 September) records that *nothings* is largely *sweet nothings* and that *somethings* includes *thirty-somethings* (CGEL p. 1716). The footnote already drops the *-wheres* forms, so its caveats should be restored too.

> The plural forms are common{++, though these are unscreened form counts (\mention{nothings} is largely \mention{sweet nothings}, and \mention{somethings} includes \mention{thirty-somethings})++}: COCA List counts …

## Outcome

- Two confirmed mismatches, fixes 1 and 2.
- One missing record, item 3, which needs a COCA search.
- One unmatched comparison, item 5, which needs a COCA search.
- Two wording precisions, items 7 and 8.
- One item resolved, the slide date.
- One item needing no change, the 198 texts.

Nothing is applied yet.

## Applied, 15 October (Brett: "apply 1, 2, 5, 6")

Brett's numbering follows the chat list, which maps to this note as: chat 1 = item 1, chat 2 = item 2, chat 5 = item 7, chat 6 = item 8. All four are applied. Item 8's caveat went after the counts, as its own sentence ("These are unscreened form counts: …"), not after "common", so that "these" has something to refer to. Still open: item 3 (the *become those* record) and item 5 (matched *a little much* count), both waiting on COCA searches.
