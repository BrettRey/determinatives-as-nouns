# Terminological hygiene, 18 September 2026

<!-- SUMMARY: the paper's local contrasts traced through the whole text at commit e972fd9; one real drift (permission for dependent conditions) and four smaller ones repaired; canon terms clean · status: applied · updated: 2026-09-18 -->

Procedure: the registry's `terminological-hygiene` entry. Mechanical layer (`check-terms.py --gate`), then the judgment layer over every occurrence of each working term. Model: Claude Fable 5.1.

## Mechanical layer

The gate flagged four terms as unglossed at first use: *dependent*, *quantifier*, *projection*, *profile*. *Dependent* and *quantifier* are glossed in the body (§1, §2.2) and flagged only because the abstract uses them first; *projection* and *profile* had no gloss anywhere. Repairs: *profile* glossed in apposition at its first body use in §1 ("the functions, dependents, forms, and meanings a category's members show"), *projection* likewise ("the phrase it heads"). A ledger at `planning/terms.md` now records the four as free with the reason, and the gate passes with `--ledger planning/terms.md`.

## The paper's local contrasts

| Contrast | Where set | Verdict |
|---|---|---|
| determinative (category) / determiner (function) | §1 | Honoured throughout. *Determiner* as a category word occurs only for Hudson's and Van Eynde's categories, each marked as theirs. |
| dependent use / independent use (with or without a nominal target) | §1 | Honoured. Two uses of *independent* in the ordinary sense ("the independent case") sat next to the technical one in §5.5 and were reworded ("the separate case", "the prior case"). |
| D-noun categorization (taxonomy) / D-noun analysis (taxonomy plus ordinary Head) | §1 | Honoured, with two leaks. Bare *D-noun* (16 uses) consistently means the categorization; §1 now says "D-noun for short". *Package* (6 uses, undefined) was a third name for the analysis; replaced by *analysis*. |
| ordinary Head / fusion (the two Head analyses) | §1 | Honoured. Two lowercase *fused head* brought into line with the function capitalization (*fused Head*); the hyphenated modifier *fused-head* stays lowercase, as in *CGEL*. |
| use permission (which functions a lexeme's phrase may fill) / condition (what its dependents and target must satisfy) | §5.1, and the formula's U against C | **The one real drift.** §§3.1, 4.4, 4.5, 5.4, and 5.5, and Table 4's header, called dependent conditions "permissions" (modifier permissions, premodifier permissions, the restrictor permission, one internal permission, one permission covers ...). Twelve uses repaired to *condition*; *permission* is now reserved for the lexical use permissions of §5.1. |
| category condition (§5.2: Cat(h) = N against Cat(h) ∈ {N, D}) | §5.2 | The abstract and the conclusion, written this week, called the same thing a "disjunctive head condition". Both now say "a disjunct in its category condition". |
| Nom / NP; ultimate lexical head / immediate Head | §4.1 | Honoured. *Lexical head* (the word) against *lexical Head* (the function a word fills) is consistent, if quiet. |
| peripheral / internal (modifier attachment) | §4.4 | Honoured. |
| secondary use (within a category) / conversion (category change) | §4.5, §5.5 | Honoured; the contrast is *CGEL*'s and the argument depends on it. |
| complex determinative | §3.1 | Every use is attributed to *CGEL*; the paper itself posits none. |
| grouping / categorization / taxonomy / reclassification | throughout | Variation, not drift: *grouping* is the informal name for the inclusion, *categorization* the named claim, *taxonomy* the hierarchy, *reclassification* the act. Left. |

## Canon terms

No *word class*, *mass*, *predicate* (for predicator), *subjunctive*, or *aspect*. *Determinative* is the category and *determiner* the function throughout. *DP* is defined in §1 as *CGEL*'s determinative phrase and never means Abney's.

## Imported terms

*Fusion of functions*, *predeterminer modifier*, *number-transparent*, *restrictor* (Payne and Huddleston 2007), *valency* (Hudson), *functor* and *MARKING* (Van Eynde), *adjectives of quantity* (Solt), *Big Mess construction*: each used in its author's sense and attributed at first use. Van Eynde calls the *such* of *such a mess* "demonstrative"; the paper calls it degree *such*, which is a categorization difference, not a borrowed term misused.

## Repairs applied

25 substitutions in the manuscript; ten census claims and six evidence spans re-pointed in `amendments.json`; the claim set resolves. No claim moved.
