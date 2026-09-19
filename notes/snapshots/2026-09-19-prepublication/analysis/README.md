# Supplementary matrix audit and corpus documentation

This directory separates a reproduction of Reynolds (2021) from a descriptive inventory of CGELBank. Neither analysis tests whether determinatives must be a primary category, a coordinate noun subclass, or part of a broader pronoun class.

The standalone [matrix audit](../matrix-audit.pdf) ([LaTeX source](../matrix-audit.tex)) brings together the reporting discrepancy, implementation issue, methods, sensitivity results and correction trail. The [corpus documentation](../corpus-documentation.pdf) ([LaTeX source](../corpus-documentation.tex)) preserves the inventory table, annotation cautions and sentence identifiers. Build both PDFs from the project root with `make supplements`.

On 9 September 2026, this material was moved out of the article's empirical section and replication appendix. The article retains two sourced attestations in its grammatical discussion and a short account of the earlier matrix study's taxonomic limits, with a footnote identifying the audit's findings. All input data, analysis scripts, generated tables and numerical outputs were preserved unchanged. The earlier manuscript is retained in `../notes/snapshots/2026-09-09-empirical-relocation/`.

## Matrix provenance and reproduction

`data/matrix155-lingbuzz.csv` is the public file downloaded from [LingBuzz 005747](https://ling.auf.net/lingbuzz/005747) on 7 September 2026. Its SHA-256 matches the previously held central CSV and `Documents/Rdata/73-65full.csv`. It contains 138 word forms and 155 binary features, although the landing page and the 2021 article describe 232 features.

`data/wordlist-first-cut-source.csv` is an older local working file. `recover_matrix.py` extracts its rectangular 138-by-232 block, preserving all binary values. The extracted file is a **recovered working matrix, not an authenticated copy of the published analysis input**. Its source path and hashes are recorded in `data/source-manifest.json`.

The files differ by 77 removed columns (76 singleton features and one all-zero feature), 11 changed cells in `Start_with_hw`, and two normalized row names. One singleton feature remains in the public file. An earlier draft of *Determinatives as nouns* incorrectly claimed that removing singleton features leaves between-form distances unchanged. Exact comparisons are in `results/matrix-lineage.json`, `removed-features.csv`, and `coding-changes.csv`.

Run:

```sh
python3 analysis/recover_matrix.py
Rscript analysis/reproduce_matrix.R
```

The R run requires `energy` (audit version 1.7-12). Full R and platform details are in `results/R-session-info.txt`. This session used R 4.6.1 and a temporary library at `/tmp/determinatives-Rlib`; use `R_LIBS_USER=/tmp/determinatives-Rlib` if reproducing in this same workspace. A future machine should install the recorded package versions in its own environment.

The public 155-feature matrix reproduces the published DISCO decomposition to the displayed precision: between 30.58286, within 356.41607, total 386.99893, F 11.670. These are energy-analysis components, not simple average Hamming distances. Both procedures use Euclidean distances on unscaled binary rows (the square root of the mismatch count), with equal column weights. The new permutation run uses seed 20260907 and 999 permutations, yielding p = .001, the minimum attainable value under the implemented calculation. It is a new seeded permutation run, not recovery of the original unrecorded random state.

The published appendix removes the first feature again for k-groups after removing the names column. The audit reports both the 155-feature matrix and that 154-feature implementation. For each variant it runs 100 separate single-start fits, with seeds 1–100, `iter.max=10` and `nstart=1`; it also reports one 100-start fit at seed 20260907 and `iter.max=100`. Cluster labels are oriented after fitting to maximize agreement with the 73/65 reference partition. The reported 129/138 result is attainable but is not a uniquely reproducible classification. The 100-start fit is the best objective among those starts, not a proof of a global optimum.

Sensitivity variants remove the first 50 word-component columns, retain the 50 syntactic columns, or remove four explicit analysis labels from those syntactic columns. These are exploratory changes to the representation, not independent recodings. The remaining syntactic judgments are still theory informed. The recovered working matrix is also analysed, without identifying it as the published input. The within-category audit reports both the determinative split found in the appendix and the pronoun split described in the prose; neither is used as a taxonomic-rank test.

`legacy-distance-audit.csv` records exact selected-group distances used in the archived manuscript. The comparison groups were selected for that manuscript and are not a justified measure of prototype centrality. Those numerical claims have no role in the rebuilt argument.

## CGELBank inventory

Source: [nert-nlp/cgel](https://github.com/nert-nlp/cgel), commit `d0a2c2d8c522b23d5aa879fc9cb94948f4285b2c`. The source is licensed CC BY 4.0. The inventory includes four top-level gold files: `twitter.cgel`, `ewt.cgel`, `ewt-test_pilot5.cgel`, and `ewt-test_iaa50.cgel`. Trial files, one-off examples and duplicate annotation-study files are excluded. File hashes are in `results/corpus-manifest.json`.

Run against a checkout at that commit:

```sh
python3 analysis/corpus_inventory.py /path/to/cgel
```

The parser requires `pylatexenc` (audit version 2.11). The script rejects a different Git commit. This session's checkout is `/tmp/determinatives-cgelbank-20260907` and its Python environment is `/tmp/determinatives-analysis-venv`.

The denominator is 220 trees and 3,390 lexical nodes with overt text, including source errors. There are 387 overt nodes annotated D. A D node's local function is found by following Head edges upward until the first non-Head edge. This avoids counting a determiner embedded in a partitive domain as its outer quantifier. Lemmas follow the corpus's supplied correction/lemma where available and are lowercased. Deleted source tokens are retained and explicitly labelled; multiword lexical nodes remain one node. Thus these are annotation-token counts, not whitespace-word counts.

The resulting local functions are Det 297, Mod 18, Det–Head 65, Marker 1, Flat 4 and Coordinate 2. All 65 Det–Head contexts were read in their retained sentence context. They include compounds, partitives, floating quantifiers, degree and frequency expressions, numeral fragments, age supplements and the numeral inside `about 30 seconds`. They must not be reported as 65 ordinary independent argument uses. `corpus-det-head-review.csv` supplies the local phrase, nearest NP function and full retained sentence for inspection.

The corpus supplies, for example, `test-drive both` following `two different Honda models`, `so many tell lies` after `politicians or lawyers`, and `something reliable and good looking`. The first two have available restrictions in the retained sentence; they are not evidence of an antecedent-free reading. The third attests postmodification of a compound, not the disputed premodification in `the lucky few`. The sample contains no D-token occurrence of bare `few`, `either` or `neither`. Its gaps cannot establish ungrammaticality, and it does not estimate productivity across the full determinative inventory.

CGELBank's recorded categories and fusion analyses are the objects being inventoried. They cannot independently confirm those analyses or their proposed replacements. The article cites two sentences in their grammatical contexts. The annotation inventory and its limitations remain in this documentation and the corpus supplement.

## Publication status

These analyses accompany the working paper as separate supplements. Model-assisted numerical review is complete: an independent GPT-6 (Astra) auditor reran all matrix and corpus scripts, reproduced their outputs byte for byte, and separately recomputed the DISCO components and corpus counts. The complete audit is in `../reviews/review-board-20260907-rebuild/corpus.md`; a separate GPT-5.6 (Sol) numerical check is in `../reviews/review-board-20260907-rebuild/numbers-second-model.md`. No preregistration, independent judgment study, representative corpus sample or held-out category-classification experiment is claimed.

The prepared `public-matrix-correction.txt` remains unposted. The archived public CSV and its checksum are unchanged; the recovered 232-feature working file remains separately identified and unauthenticated as the published input. Relocating the audit has not updated the original article or the public resource.

## Claim set and census (September 2026)

`expanded-json-2026-09-14/` holds the accepted 110-claim extraction that generates Table 1 of the quantifier supplement (`make check-quant-table`); `evidence-type-2026-09-14/` its keyed evidence labels; `claims/claims-enriched.json` the merged layer. `manuscript-census-2026-09-14/` holds the 658-claim census of the manuscript's participation claims and, since 16 September, its normalized layer (`census-normalized.json`, `make census`) with the derived cross-tab and corpus worklist in `generated/`. `make check-claims` verifies every quotation in all of them against the live manuscript and supplement. See each directory's README; no proportion from any of them is a finding about the paper.

## Coverage audit (2026-09-18)

`coverage-audit.json` holds the hand-classified grid (construction family × lexeme group × implementation, codes D/D2/L/S/U with a note and section per cell); `tools/coverage_audit.py` generates `generated/coverage-audit.tex` and `generated/coverage-summary.tex` for the supplement `coverage-audit.tex`, attaching register claim counts to each cell; `check` mode verifies the committed files.
