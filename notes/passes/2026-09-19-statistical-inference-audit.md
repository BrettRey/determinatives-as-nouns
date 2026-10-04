# Statistical-inference audit, 19 September 2026

<!-- SUMMARY: no interval, test, or resampling result in the article; the matrix supplement's permutation results are unchanged since the 9 September audit (26 analysis files hash-identical) and remain scoped as non-population comparisons · status: clean · updated: 2026-09-19 -->

Text: `determinatives-as-nouns.tex` after commit af63c84 with the 19 September quote-audit repair, and the five supplements. Procedure: the registry's `statistical-inference-audit` entry, run against the analysis outputs. Model: Claude Opus 5.

## What inference exists

A search of the article and all supplements for p-values, permutations, intervals, significance, standard errors, bootstraps, test statistics, and agreement coefficients (`grep -i -E "\bp *[=<]|permutation|confidence|interval|significan|standard error|bootstrap|chi|test statistic|\bF *=|kappa|agreement rate|agreed on"`) finds:

- **The article: none.** Its numbers are counts of corpus hits and saved lines, a count of hand-read lines (*few would*, 82/5/7), and counts of audit cells. None is offered as an estimate for a population with an interval or test. The board's "a number changed" trigger is the rewording of the *each*/*every* comparison (now 3,090 against 23 string hits) and of the *each of them* rate; both are descriptive, and their measurement is taken up in the measurement-construction audit of the same date.
- **The matrix supplement:** the DISCO permutation results (999 permutations, seed 20260907, all at the .001 floor) and the k-groups agreement ranges. The 26 analysis files behind them match their 9 September SHA-256 checksums (26 unchanged, 0 changed, 0 missing; baseline `notes/snapshots/2026-09-09-empirical-relocation/analysis-checksums.json`), and the only commit touching them since, a9228f1 (12 September), added them to version control. The supplement still says the permutation results "describe comparison with shuffled partitions of these rows" and "aren't population-level inference under a defended exchangeability assumption" (`matrix-audit.tex` l. 45). The 9 September verdicts on dependence, resampling unit, multiplicity, post-selection, and arithmetic stand.
- **The claim register:** agreement between the labelling model and the keyed claims, reported as counts. It is descriptive and makes no inferential claim.

## Dependence note for the corpus counts

The corpus proportions (the *each of them* rate) are shares of query hits, with texts as the real dependence unit: one text can contribute several hits, and the plural *each of them* lines are concentrated by genre (BLOG 19, SPOK 19, WEB 18 of the 75 saved; MAG 7, NEWS 5, ACAD 3, FIC 2, MOV 1, TV 1). The article draws no inference from the proportion, so nothing needs a clustered interval. If a rate is later compared across registers or corpora, it should be computed per text, not per hit.

## Verdict

Clean. No wording downgrade is required by this pass.
