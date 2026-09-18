You are auditing the numbers in a LaTeX manuscript for numerical drift. You have read-only access to the project directory. Do not edit anything; report only.

Manuscript: determinatives-as-nouns.tex (the main paper). Also audit the hand-written prose counts in coverage-audit.tex and claim-register.tex (the supplements), which are separate LaTeX files that pull generated tables from analysis/generated/.

TASK. For every numeric claim in the manuscript prose and footnotes (counts, frequencies, corpus line totals, cell counts, feature counts), find the file it should come from, compare exactly, and give a verdict. Out of scope: page numbers inside \citep / \textcite / \citealp citations, years, LaTeX layout numbers (column widths, penalties), and the ORCID.

The numeric lines in determinatives-as-nouns.tex are roughly these (line numbers may be off by a few; use grep):
- line 79 (footnote on *every*): COCA List counts each has 1,578, each was 1,005, each will 507, every will 12, every has 8, every was 3; 618 COCA lines for every before a verb; 164 NOW lines. Sources: corpus/exclusion_tests/ (every_has.jsonl, coca_every_v.jsonl, *.report.md, log or README files there), analysis/generated/exclusion-table.tex, quantifier-controls.tex.
- line 142: agreement counts (389, 78, 151, 73, 173, "17"). Sources: corpus/exclusion_tests/each_of_the_nn2_was_were.report.md, each_of_them_was_were_is_are_has_have.report.md, and the jsonl files there.
- line 180: numbers 417, 8, 10 near "Bare colour expressions". Check whether these are corpus counts or citation pages; if corpus counts, find the source.
- line 245 (§2.7 footnote): COCA be much 81 lines; NOW there is little 23 lines; became too much to 45; seemed too/so much to 46; seemed a lot to 15; be a lot to 2,394 tokens (List count). Source: corpus/independent_argument/2026-09-18-brett-supplied-be-much-there-is-little.md.
- line 386: numbers 20, 27, 89, 94 near "Some left, Many came". Identify and source.
- line 421: 11, 11, 17 near "Independent few ... permit definite determination". Identify and source (likely corpus/independent_argument/*.report.md or corpus/exclusion_tests/).
- line 541: 282, 120, 17, 17, 590, 416, 318, 115, 38, 20 (compound counts footnote: at_j_someone..., coca_art_compound, coca_art_adj_compound). Source: corpus/exclusion_tests/*.report.md and *.jsonl.
- line 694: 61858, 19, 395130 near "nominal heaps and lots" (possibly COCA text ids or counts). Identify.
- line 724: "ten" numerals numbers 10, 10.
- line 734 (§5.5): "Of 103 cells, 35 are lexical facts identical in all four accounts"; "32 of its derivations go through the disjunct". Sources: analysis/generated/coverage-summary.tex, analysis/generated/coverage-audit.tex, analysis/coverage-audit.json, analysis/tools/coverage_audit.py (you may run: python3 analysis/tools/coverage_audit.py check, read-only).
- line 752: 138 word forms; 232-feature working matrix; public 155-feature file omits 76 singleton columns and one all-zero column. Sources: matrix-audit.tex, analysis/generated/matrix-table.tex, and the matrix data files under analysis/ (find them).
- coverage-audit.tex Results prose: "one condition on the fused inner phrase (nine cells)", "rules stated once for NPs and again for DPs (twelve cells, four rules)", "the 32 derivations", and the sensitivity claims (I1, I3, I4 level on cells; I2 trails only by its Dn cells; pricing the disjunct at zero brings I2 level). Sources: analysis/generated/coverage-summary.tex and coverage-audit.tex, analysis/coverage-audit.json.
- claim-register.tex method paragraph: it uses macros from analysis/generated/claim-counts.tex; check that every number stated literally in the prose (if any) matches those macros, and check the macros' internal arithmetic (withdrawn + live = census; keyed agreement <= keyed).

Also check DERIVED numbers: totals that should equal sums of parts; the same N stated in two places; percentages against counts.

Also FLAG the red-flag shapes: round numbers, plausible-sounding ranges, statistics that look borrowed rather than computed.

OUTPUT. A Markdown report with:
1. A header line stating which model ran this audit (your model name and version as you know it).
2. One table row per number: number | manuscript location (file:line and the phrase) | source file and the value found there | verdict (MATCH / MISMATCH: source says X / NO SOURCE FOUND / OUT OF SCOPE).
3. A list of derived-number checks with results.
4. A short list of anything that needs a human decision.
Name every number with no source individually. Do not summarize; be exhaustive. If a source file is too large to read fully, say how you searched it (the command) and what it returned.
