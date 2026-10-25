# Desk count: how far the pronoun-like properties reach across the determinatives
<!-- SUMMARY: desk count for the evidence ledger's pronoun-node-reach row, from the 2026-10 feature matrix: pronoun-like properties sit in four small subgroups of determinatives, the determinative-only properties in the quantifiers and cardinals; 5 of 20 character pairs conflict with any one tree of the forms; no nouns are coded, so nesting against coordination is not yet tested · status: done, preliminary · updated: 2026-10-24 -->

Run 24 Oct 2026 at Brett's request ("sure", to running the count before the structure review). Script and outputs by Claude Opus 5.5. Reproduce with `python3 analysis/node-reach-2026-10-24/node_reach.py`.

## Inputs and outputs

| File | SHA-256 |
|---|---|
| `analysis/matrix-2026-10/matrix-2026-10.csv` (input) | 2e329c171a5b50ec3dd8b90a90c378dd8dfba837665fb192195fa9c5aa5951bf |
| `analysis/data/word-mapping.csv` (input: *CGEL* category per form) | a08083fcce4980145fabf3ca4e5423ceb552ebdf0aafedeee792fe477291190d |
| `node_reach.py` | 48492e7c2d3bf8bd20f471f2c1aa1a9d11a2523e10a4f7f2af2477b5a5b6b5b4 |
| `node-reach.csv` (per feature: counts among determinatives, pronouns, and groups A, B, C) | f139f8ac195db1c92c120119083f11aaf02dc7d2d725b4959099a6288852692b |
| `compatibility.csv` (four-gamete test, 25 pairs) | aaca043df4e02e39e6466460187d272d18c536810d999a9f24b65e427baafda1 |

The inventory is Reynolds (2021)'s 138 forms plus *whomever*: 73 determinative and 66 pronoun forms by *CGEL*'s categories. It isn't *CGEL*'s inventory (p. 356). It includes *today*, *there*, *somewhat*, *last*, and *next*, and it counts forms, not lexemes (*fewer* and *fewest*, relative and interrogative *which*, count separately). Only the 105 syntactic and semantic columns are used; the 50 word-component columns are skipped. The features are theory-informed, and 13 proposed corrections still await Brett (`analysis/matrix-2026-10/REPORT.md`). There are no common or proper nouns in the matrix.

## Results

**The pronoun-like properties sit in four small subgroups.** Personal gender as head occurs in 11 determinative forms (the eight *-one* and *-body* compounds and *we*, *us*, *you* before a noun); interrogative in 6 (the forms of *which*, *what*, *whichever*, *whatever*); person deixis in 3 (*we*, *us*, *you*); stress as object after a particle in 5 (the four demonstratives and interrogative *which*). Together these mark 21 of the 73 forms (group A): the compounds with a personal base, the demonstratives, the wh-determinatives, and the personal determinatives. Hudson (2000, Table 2) lists all four kinds among his pronouns (as compound, demonstrative, interrogative, and personal).

**The determinative-only properties sit in the quantifiers and cardinals.** Group B is defined by heading a partitive (35 forms that aren't in A), so the partitive itself says nothing here. The informative features are the ones used to define neither group. Among the 35 B forms, 21 A forms, and 17 others (C):

| Feature (none in pronouns unless stated) | B | A | C |
|---|---|---|---|
| comparative and superlative forms | 10 | 0 | 0 |
| degree meaning | 10 | 0 | 0 |
| degree modifier in an AdjP | 10 | 2 | 2 |
| independent use in existentials (*there's some on the table*) | 29 | 4 | 6 |
| coordinates with other determiners | 25 | 4 | 4 |
| followed by adjective *such* | 25 | 5 | 2 |

The feature "functions as fused determiner-head" is *CGEL*'s analysis label, not a property of form, and is left out of the argument (the reproduction of Reynolds 2021 already treats it as an analysis label). "Proportional" codes *a* and the demonstratives as proportional and isn't used either.

**Some pronoun-like and quantity-like characters conflict.** Two binary characters fit one tree of the forms without homoplasy only if the forms don't show all four combinations of their values (the four-gamete or pairwise compatibility test). Of 25 pairs, 10 show all four. Five of those come from one feature, "takes *else* or *more* as a post-head dependent", which conflates the compounds' *else* with comparative *more* after *all*, *little*, and *much*; set aside, 5 of 20 pairs conflict. Each rests on a familiar fact: personal compounds in existentials (*there's somebody at the door*; *nobody*, *no one*, *somebody*, *someone*), interrogative *which* and *whichever* heading partitives (*which of them*), and the demonstratives as degree modifiers (*that big*) and in coordination with other determinatives.

## What it shows, and what it doesn't

It shows that the properties pronouns and determinatives share don't reach most of the determinative inventory: they mark four small subgroups. And it shows that some characters conflict with any single tree of the forms, so a strict tree of categories won't record all the shared properties without restating some.

It doesn't test nesting against coordination. Both need to know which of these properties common and proper nouns have, and the matrix codes no noun. It doesn't show that determinative fails to be one category either, for the same reason and because the features are theory-informed.

It does show that nesting and coordination aren't the only structures to compare. Word Grammar, Hudson's own framework, allows multiple inheritance: "the organization allows any concept, whether exemplar or category, to belong to more than one taxonomy" (Hudson 2010, §2.4.1; 'pet canary' inherits from both 'pet' and 'canary', Figure 2.6). On that structure the compounds, say, could inherit from both pronoun and determinative. The paper needs a position on cross-classification either way: whether the pronoun-like properties are features that cross subcategories, as gender does, or evidence for a node.

## Next

Code a reference set of nouns, with an adjective outgroup, on the 105 syntactic and semantic columns, with Brett judging the cells. Candidates: quantity common nouns (*lot*, *number*, *plenty*, *dozen*, *majority*), ordinary count and non-count nouns (*dog*, *water*), proper nouns (*Kim*, *Toronto*), and adjectives (*numerous*, *rich*, *tall*). That makes possible the tests in `notes/nesting-tests-2026-10-24.md`: which characters the pronoun-and-determinative grouping alone shares, how many characters conflict with it, whether the distances fit a hierarchy at all, and whether the intermediate category improves prediction of features.
