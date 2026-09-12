# Independent numerical check

**Model:** `gpt-5.6-sol`  
**Scope:** Read-only comparison of the current empirical passages in `main.tex` with the analysis scripts, source matrices, result CSVs, and generated tables. I did not read prior reviews and did not rerun R.

No numerical discrepancies found.

The public matrix has 138 rows and 155 binary features; the recovered working matrix has 138 rows and 232 binary features. The scripted reference split is 73/65. For the public matrix, the saved DISCO components satisfy

\[
30.582860830185+356.416065635533=386.998926465718
\]

and independently give

\[
F=(30.582860830185/1)/(356.416065635533/136)=11.669701435845,
\]

which rounds to the manuscript's 11.670. Applying the same formula to the other displayed variants gives 12.654266076950 (105 features), 9.681704427326 (50), and 7.192247140229 (46), matching the table's 12.654, 9.682, and 7.192. The output records `p=.001` for all displayed variants (999 permutations); this check did not reproduce the permutation draws.

Independent aggregation of the 100 single-start rows reproduces all displayed ranges: public 155, 75--132 (eight runs at 129); no-word-component 105, 75--131; syntax 50, 69--133; syntax-minus-four 46, 69--117. Agreement counted directly from the saved best-fit assignments is respectively 125/138, 131/138, 120/138, and 97/138, matching both summary CSV and generated table. The appendix-154 output is also internally consistent: range 75--132, six runs at 129, best fit 125/138.

Summing `corpus-denominators.csv` gives 220 trees, 3,390 overt lexical nodes, and 387 D tokens. Directly counting the 387 concordance rows gives Det 297, Mod 18, Det--Head 65, Marker 1, Flat 4, Coordinate 2. Recomputed table tuples `(Total, Det, Det--Head, Other)` are: the (129,129,0,0), a (90,89,0,1), every (3,3,0,0), this (28,21,7,0), that (12,5,7,0), some (5,3,2,0), all (11,3,5,3), both (4,2,1,1), many (3,0,1,2), a few (2,1,1,0), each (2,0,1,1), enough (6,2,1,3). All match the generated table.
