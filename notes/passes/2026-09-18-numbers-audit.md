# Numbers audit, 18 September 2026

<!-- SUMMARY: every corpus, analysis, and audit number in the manuscript and the hand-written prose of two supplements traced to its file; all located; two wording findings · status: findings, awaiting Brett · updated: 2026-09-18 -->

Text audited: `determinatives-as-nouns.tex` at commit 240b1db, plus the hand-written prose of `coverage-audit.tex` and `claim-register.tex`. Out of scope, as the registry entry allows: page numbers inside citations, years, URLs and post ids, the ORCID, LaTeX layout numbers, and the model names in the AI-use note.

## Who did what

The registry asks for a second model, not the one that wrote the numbers. Codex, the usual choice, was out of credits until 19 September 06:31 (`ERROR: You've hit your usage limit`). On Brett's instruction the audit ran as follows:

1. **Retrieval and arithmetic in code** (this session, Claude Fable 5.1): every number-bearing sentence was extracted from the manuscript and each number searched, as a string, across `corpus/`, `analysis/`, and the supplements (6,978 files, cache excluded); derived quantities were recomputed from the located sources; every quoted corpus line was searched for verbatim in its saved file.
2. **Comparison by a second model**: qwen3.8:27b through the Ollama HTTP API (`think: false`, `format: json`, temperature 0, `num_ctx` 8192) received eleven packets, each a manuscript passage beside the verbatim source excerpt, and returned a verdict per number. The packets are in the session scratchpad (`numbers-packets.json`); the verdicts are appended below.

The independence is partial: the second model judged packets this session assembled, so a wrong or stale source in a packet is something it could not catch. The retrieval is recorded here so that it can be checked. A fully independent run (Codex, reading the files itself) should be made before submission, when the numbers are final; this pass will have gone stale by then in any case.

## Every number, its source, and the code verdict

| Number(s) | Where | Source | Verdict |
|---|---|---|---|
| *each has* 1,578; *each was* 1,005; *each will* 507; *every will* 12; *every has* 8; *every was* 3 | §1 footnote | `corpus/exclusion_tests/log.md` (COCA List, 17 Sept, Brett) | MATCH |
| "over a hundred times as frequent" | §1 | (1,578 + 1,005 + 507) / (12 + 8 + 3) = 3,090 / 23 = 134 | MATCH |
| 618 COCA lines with *every* before a verb; 164 NOW lines | §1 footnote | `every-reading.md`: 1,095 lines of which 618 contain *every*; 164 NOW lines for *every was/has* | MATCH |
| "nearly eight hundred COCA and NOW lines" | §1 | 618 + 164 = 782 | MATCH |
| *each of them* + is/has/was 389, + have/are/were 78; *each of the* + N + was 151, + were 73; 173 strings | §2.2 footnote | `corpus/exclusion_tests/readings.md`, `log.md` | MATCH |
| "about a sixth"; "about a third" | §2.2 | 78 / 467 = 0.167; 73 / 224 = 0.326 | MATCH |
| *be much* 81; *there is little* 23; *became too much to* 45; *seemed too/so much to* 46; *seemed a lot to* 15; *be a lot to* 2,394 (List) | §2.7 footnote | `corpus/independent_argument/2026-09-18-brett-supplied-be-much-there-is-little.md` (ENTRIES: 81, 23, 45, 46, 15; List 2,394 with breakdown) | MATCH; breakdown sums: 1,493 + 571 + 205 + 82 + 17 + 17 + 4 + 4 + 1 = 2,394 |
| "89 of 94 NOW lines for *few would*" | §4.2 footnote | `few_would.report.md`: 94 lines; 89 carry the screener label `generic_or_unrestricted`, 5 `antecedent_in_context` | MATCH on the count; see finding 2 on what it counts |
| *special someone* 282; *certain someone* 120 | §4.5 footnote | `corpus/exclusion_tests/log.md` (List, 17 Sept) | MATCH |
| *somethings* 590, *nothings* 416, *nobodies* 318, *somebodies* 115, *anythings* 38, *anybodies* 20; *-wheres* left out | §4.5 footnote | `log.md` line 29 (also lists *somewheres* 178, *anywheres* 51, *nowheres* 44, which the footnote excludes as stated) | MATCH |
| 103 cells; 35 lexical in all four; 32 derivations through the disjunct | §5.5 | `analysis/generated/coverage-summary.tex`; recomputed from `analysis/coverage-audit.json`: 103 cells, 35 all-L cells, I2 Dn = 32 | MATCH |
| 138 word forms; 232-feature working matrix; 155-feature public file; 76 singleton columns and one all-zero column | §6 footnote | `matrix-audit.tex` ("77 removed columns (76 singleton features and one all-zero feature)"); `analysis/README.md` (138 forms, 155 features, 138-by-232 block) | MATCH |
| Audit prose: inner-phrase condition, nine cells; NP/DP rules twelve cells, four rules; 32 Dn | `coverage-audit.tex` results | recomputed from the JSON: 9 I3 cells under `inner_phrase_restriction`; I3 D2 = 12; 4 distinct duplicated rules | MATCH |
| Audit prose: under the report's principles "I1, I3, and I4 come out level on cells", I2 trails by its Dn cells, disjunct at zero brings I2 level | `coverage-audit.tex` results | sensitivity tables: I1 54 D / 43 L / 6 S; I3 54 / 42 / 7; I4 55 / 43 / 5; I2 29 D + 25 Dn / 43 / 6; at zero I2 = 54 / 43 / 6 | MATCH for I2; "level" for I1, I3, I4 is within one cell (54/54/55 D, 6/7/5 S). See finding 3 |
| Claim-register macros: 658 census, 7 withdrawn, 651 live, 135 taxonomic, 6 other, 79 lexemeless-only, 431 retained, 44 of 51 keyed, 237 of 252 TypeSafe | `claim-register.tex` via `claim-counts.tex` | 658 − 7 = 651; 135 + 6 + 79 + 431 = 651; 44 ≤ 51; 237 ≤ 252 | MATCH |
| "22-item catalogue" | `claim-register.tex` | `census-normalized.json` constructions: 22 | MATCH |

Every quoted corpus line in the manuscript's footnotes (26 checked: the *few*, *lucky few*, *every*, compound, and *be much / little / a lot* lines) was found verbatim in its saved file, and the seven NOW dates cited (20 Oct 2022, 4 Mar 2022, 27 Sep 2021, 3 Oct 2022, 11 Feb 2021, 11 Sep 2020, 1 Sep 2022) match the line stamps (22-10-20, 22-03-04, 21-09-27, 22-10-03, 21-02-11, 20-09-11, 22-09-01). One exception is finding 1.

Numbers with no source: none. Red-flag shapes: none; every figure is a List count, an entry count, or a recomputed cell count, and none is round.

## Findings

1. **A quotation normalized without saying so.** §2.7 footnote gives "\$26 is a lot to pay for a topping" (*Atlanta Journal-Constitution*, 2014). The saved line reads "$26 is a lot to pay for a ' topping, '": COCA's display carries quotation marks around *topping*. The article drops them. Repair: restore them as single quotes inside the `\enquote`, or note the normalization once for the hand-pasted sets.
2. **"In 89 of 94 NOW lines for *few would*, nothing in the visible context supplies the set" states a screener label as an observation.** The 89 is the count of lines that TypeSafe (jev-latest) labelled `generic_or_unrestricted` to the domain question; no one has read the 94 lines, and the report file and the 17 September decision both call them candidates for a human reading. The number is right; its status isn't stated. Repair, one of: read the 94 lines (short; a quarter of an hour) and keep the sentence as a reading; or reword to "the screening model finds no antecedent in the visible context for 89 of 94 NOW lines". The manuscript's own evidential-standard paragraph (§2.3) would want the first.
3. **"Level" in the audit's sensitivity prose is a one-cell approximation.** I1, I3, and I4 differ by one cell in D and in S under the report's principles. The prose says "come out level on cells". Repair: "within one cell of each other".
4. **"81 lines"** (and 23, 45, 46, 15) counts KWIC entries as the display headed them ("ENTRIES: 81"); the *be a lot to* batch separately distinguishes 483 KWIC texts from the List count of 2,394 tokens, and the article states that one correctly. No change needed unless "lines" is meant to be read as tokens.

The paper is in LaTeX, and this is the pass that exists because LaTeX numbers can drift. The audit and claim-register counts are already generated at build time (`claim-counts.tex`, `coverage-summary.tex`) and cannot drift; the corpus counts in the footnotes are hand-written and can.

## Second-model verdicts (qwen3.8:27b)

Packets and raw verdicts: `analysis/numbers-audit-2026-09-18/` (`numbers-packets.json`, `numbers-audit-qwen.json`; the Codex brief that could not run is kept beside them). Eleven packets, 50–178 s each.

| Packet | Qwen verdict | What it flagged | Assessment |
|---|---|---|---|
| P1 *every* counts and ratios | MISMATCH (label only) | Its note: every count matches, 782 and "about 134 times" supported | Agrees with the code; the label contradicts its own checks |
| P2 *each* agreement | MATCH | | Agrees |
| P3 *be much*, *there is little* and the rest | MISMATCH | 81 and 23 "lines" against the display's "ENTRIES: 81 TEXTS" | Finding 4 above; it rates the unit mismatch higher than the code did |
| P4 *few would* 89 of 94 | MATCH | Notes that 89 is the screening model's label | Agrees; finding 2 stands on the status of the count, not its value |
| P5 §5.5 audit numbers | MATCH | | Agrees |
| P6 audit prose counts | MATCH | | Agrees |
| P7 sensitivity prose | MISMATCH | I1, I3, I4 not identical (54/54/55 D; 6/7/5 S); reads "I2 trails only by Dn" literally, since I2's D is 29 against I1's 54 | Finding 3 stands. The second point is a misreading: Dn cells are D cells recoded, and 29 + 25 = 54, so "trails only by its Dn cells" is correct as the audit defines Dn; no change |
| P8 plural compounds | MATCH | Notes the *-wheres* counts omitted, which the footnote says it omits | Agrees |
| P9 matrix columns | MISMATCH (label only) | Its note: 77 = 76 + 1 confirmed | Agrees with the code |
| P10 *topping* quotation | MATCH | Missed the dropped quotation marks | The code caught it (finding 1); the model did not |
| P11 claim-count arithmetic | MISMATCH (label only) | Arithmetic holds; wanted the definitions in the source | Agrees with the code |

Net: the second model confirmed every count the code located and added one grading (the "texts" against "lines" unit, P3). It missed the one textual discrepancy (P10) and mislabelled three packets whose own checks all passed. Its value here was as a check on the code's comparisons, not as a finder; the finder was the retrieval, which remains this session's.
