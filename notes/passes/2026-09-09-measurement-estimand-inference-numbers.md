# Measurement, target quantities, inference and numbers

Completed 9 September 2026 on the relocated matrix and corpus supplements and the remaining empirical claims in the article. The earlier independent reproduction and second-model numerical audit are reused, as the agreed sequence specifies. A fresh comparison of all 26 analytical-file hashes against the relocation baseline found no changes. Output arithmetic and agreement aggregation were checked again without rerunning R or changing any data.

## Measurement and construction

| Object | Source, unit and construction | Validation and scope |
|---|---|---|
| Binary feature rows | Public LingBuzz file retrieved September 7; 138 forms, partitioned 73/65. Cells code whether a form may exhibit a property. Features concern morphology, phonology, semantics and syntax. All cells are y/n; no missing-value imputation. | Reynolds 2021 §2.2 describes author judgments informed by grammatical sources and sometimes corpus queries. The audit validates file lineage and computations, not an independent recoding. The coding rule is now explicit in the supplement. |
| Recovered working matrix | Rectangular 138-by-232 block extracted from the held earlier CSV; extraneous header/trailing empty cells removed without inferring feature values. Row aliases aligned explicitly. | This remains an unauthenticated working input. Its relationship to the public matrix is checkable; its identity with the publication input is not established. |
| Distances and DISCO components | Unscaled binary vectors, Euclidean metric, equal column weights; fixed 73/65 reference partition. | Correlated/repeated diagnostics shape distances. Components are not average Hamming distances or measures of nounhood. No common/proper-noun comparison exists. |
| Clustering agreement | Two clusters fitted without category labels; labels oriented afterwards to maximize matches to the supplied partition. | Agreement is with an analysis-coded reference, not an independent ground truth. Best objective and best agreement are different selection criteria. The fragment's rank question is outside this measurement. |
| Corpus annotation counts | Pinned CGELBank revision, four gold files; overt lexical nodes count once, including multiword nodes and source errors. Head edges followed to the first non-Head relation; corpus lemmas/corrections retained and lowercased. | Independent extraction reproduction and inspection of all 65 Det–Head contexts already exist. The measured objects are annotations, not independently validated grammatical categories. Trial, one-off and duplicate annotation-study files are excluded explicitly. |
| Constructed grammatical judgments | Examples and permissions in the article's matched fragment; ordinary argument frames distinguished from predicatives and other constructions. | No participant experiment, acceptability scale, reliability coefficient or population estimate is claimed. These are the common judgments supplied to competing descriptions. |

The corpus has no time-based rate denominator or representative sampling claim. Zero observations of bare few/either/neither remain sample-specific. The 65 Det–Head cases include several constructions and are not relabelled as 65 ordinary arguments. No new validation study is needed to describe the existing annotation inventory; using it to estimate actual construction prevalence would require a different design.

## Target quantities and inference

The matrix supplement's targets are the saved decomposition, finite-inventory separation under specified feature representations, and clustering agreement across specified starts. The corpus target is the count of annotations under a pinned extraction. None estimates an effect, prevalence in English, category rank or superordinate nounhood.

The statistical script contains seven whole-matrix DISCO comparisons and two within-category comparisons. Each uses 999 permutations at seed 20260907. All return .001, the attainable floor of the implemented calculation. The main sensitivity table displays four of the seven representations; the others remain in the output files. No familywise-error or corrected-significance claim is made, and none is warranted by this exploratory suite.

| Inference issue | Verdict and consequence |
|---|---|
| Dependence and exchangeability | Word forms share paradigms and compound material. The script shuffles rows; no randomized assignment or defended population exchangeability is available. The supplement explicitly treats the p-values as comparisons with shuffled partitions, not population inference. |
| Crossed dependence, few clusters and resampling | No cluster-robust or bootstrap interval is reported. Removing component columns does not remove relations among rows. No unreported repair is implied. |
| Representation and post-selection | Feature removal changes the object being clustered. The exploratory sensitivity results are not independent confirmation of the taxonomy. |
| Fitted criterion versus reference agreement | A multi-start fit is selected by its objective; it need not maximize label agreement and is not a certified global optimum. The table and prose make this clear. |
| Generated uncertainty | Binary judgments have no quantified coding-error model. The audit retains that limit and does not treat their computational reproducibility as annotation validity. |
| Arithmetic | Saved between/within/total components and degrees of freedom reproduce every reported F. No population probability is inferred from the permutation floor. |

The public input reproduces the published decomposition; the new seeded permutation run does not recover the original unrecorded random state. The published code's extra feature removal is tested separately. The supplement preserves all these distinctions.

## Numerical correspondence

The independent second model was **GPT-5.6 (Sol)**, recorded in `reviews/review-board-20260907-rebuild/numbers-second-model.md`. A separate auditor reran all scripts in an isolated copy and reproduced outputs byte for byte (`corpus.md` in the same directory). Those audits remain applicable to the unchanged inputs, scripts, outputs and generated tables. This pass checked the relocated prose against them and independently reaggregated the saved outputs; it does not claim a new model run.

| Numeric claim | Source | Result |
|---|---|---|
| 138 forms, 73 determinatives, 65 pronouns; 155 public / 232 working features | Source matrices, word mapping, lineage JSON | Exact. |
| 77 removed columns = 76 singletons + 1 all-zero; 11 changed cells; 2 row aliases; 1 retained singleton | Lineage JSON, removed-features and coding-changes CSVs | Exact. |
| 30.58286 + 356.41607 = 386.99893 at displayed precision; F 11.670 | `disco-sensitivity.csv`, public155 | Exact rounding; F = (between/1)/(within/136). |
| Public 155: F 11.670; range 75–132; selected fit 125/138; eight starts at 129 | DISCO, single-start, summary and assignment CSVs | Exact. |
| Remove 50 components → 105: F 12.654; range 75–131; selected fit 131/138 | Same outputs, no-word-component variant | Exact. |
| Syntax 50: F 9.682; range 69–133; selected fit 120/138 | Same outputs, syntax50 | Exact. |
| Remove four labels → 46: F 7.192; range 69–117; selected fit 97/138 | Same outputs, syntax-without-four variant | Exact. |
| Extra-drop implementation 154 features; 100 single starts (seeds 1–100), ten-iteration limit; 100-start fit, 100-iteration limit | Published appendix and preserved R script | Exact. The original state remains unrecovered. |
| 999 permutations, seed 20260907, p=.001 | R script, output and environment record | Exact. All seven full-input and two split results retain their exploratory scope. |
| 220 sentence trees; 3,390 overt lexical nodes; 387 D tokens | Corpus denominators and manifest | Exact sums. |
| Det 297, Mod 18, Det–Head 65, Marker 1, Flat 4, Coordinate 2 | Direct aggregation of 387 concordance rows | Exact; sums to 387. |
| Four gold datasets; three retained sentence identifiers | Manifest, pinned checkout and concordance | Exact. The article uses two of the three attestations. |
| R 4.6.1; energy 1.7-12; parser dependency pylatexenc 2.11 | Environment and prior reproduction record | Matches the recorded audit environment, not a claim about current software releases. |

Every selected corpus-table tuple `(Total, Det, Det–Head, Other)` agrees with the independently verified outputs: the `(129,129,0,0)`; a `(90,89,0,1)`; every `(3,3,0,0)`; this `(28,21,7,0)`; that `(12,5,7,0)`; some `(5,3,2,0)`; all `(11,3,5,3)`; both `(4,2,1,1)`; many `(3,0,1,2)`; a few `(2,1,1,0)`; each `(2,0,1,1)`; enough `(6,2,1,3)`.

The quantitative supplements remain in LaTeX. Their two numerical tables are included from generated files; hand-written prose numbers were checked explicitly. No format migration was made. No discrepancy called for rerunning the unchanged analyses.
