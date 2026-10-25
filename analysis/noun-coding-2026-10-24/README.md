# Noun coding: draft for Brett's judgment
<!-- SUMMARY: Claude's draft coding of a reference set of nouns and adjectives (12 lexemes plus 3 category rows) on the feature matrix, with 10 features added from CGEL's own lists of noun and adjective properties and coded for all 139 existing forms; for the ledger's noun-reference-set row; nothing here is judged yet · status: on hold, superseded by the codebook (to be regenerated) · updated: 2026-10-24 -->

**On hold (24 Oct, later the same day): don't judge these cells yet.** The coding design changed after this draft: properties are coded per frame (argument NP, bare-role predicative, fixed PP, and so on), "must" columns become "may" columns, the y/m/n scale gets a codebook, noun rows become word forms (*dog* and *dogs* separately), and the external logic review (`reviews/external-logic-20261024-135944/`) changes the joint states and m. The sheet will be regenerated from the codebook. Big questions such as gender carry over.

Drafted 24 Oct 2026 at Brett's request ("draft the noun coding"), by Claude Opus 5.5. Every value is a proposal. Review in `REVIEW.md`, which lists, feature by feature, the rows proposed as y or marginal (everything else is n).

## What was coded

**Fifteen new rows** on the matrix's 105 syntactic and semantic columns and on ten added columns:
- quantity common nouns *lot*, *number*, *plenty* (the quantificational senses of *CGEL* pp. 349–350), *dozen*, and *majority*;
- ordinary common nouns *dog* (count) and *water* (non-count);
- proper nouns *Kim* and *Toronto* (primary naming uses);
- adjectives *numerous*, *rich*, and *tall*;
- three **category rows**, CN, PN, and ADJ, saying whether any common noun, proper noun, or adjective may show the feature.

The twelve lexemes are a reference set chosen for the comparison, not a sample: Reynolds (2021) notes that comparing with an open category needs "a defensible sampling procedure". So claims that a category lacks a property rest on the category rows, which are sourced to *CGEL* where they can be.

**Ten added columns**, coded for the fifteen new rows and for the 139 existing pronoun and determinative forms. The 105 features were chosen in 2021 to compare pronouns with determinatives, so nouns would score n on many of them by construction, and that would favour nesting for no reason but the feature selection (a side agent's note, relayed by Brett, 24 Oct). Nine of the ten come from *CGEL*'s own lists, so that each category's defining properties are represented; the non-partitive complement is my addition, motivated by the quantity nouns' *of*-complements and adjectives' complements:

| Added feature | Source |
|---|---|
| heads a nominal after a separate determiner (reused from matrix-2026-10) | ch. 5 §1 [2iii] |
| takes a restrictive pre-head AdjP (*good news*, *the lucky few*) | ch. 5 §1 [2iii] |
| takes an integrated relative clause | ch. 5 §1 [2iii]; p. 430 for pronouns |
| takes a non-partitive complement (of-PP, other PP or clause, *than*-phrase) | not on *CGEL*'s lists; pp. 349–350 for the quantity nouns |
| its NP is complement of a preposition | ch. 5 §1 [6i] |
| its NP modifies an AdvP (*a whole day late*, *much later*) | ch. 5 §1 [6v] |
| its NP modifies a PP (*a mile under the sea*, *all over*) | ch. 5 §1 [6vi] |
| takes a post-head AdjP (*someone nice*, *the people present*) | ch. 6 §2 [1i] |
| analytic comparative (*more numerous*) | ch. 6 §2 [1ii] |
| modified by a degree or evaluative *-ly* adverb (*remarkably few*) | ch. 6 §2 [1iii]; p. 538 (nouns "are modified by adjectives, not adverbs") |

*CGEL*'s list also has the supplement function (ch. 5 §1 [6viii]). It's left out because nearly every NP can be one, so the column would carry no information.

## Conventions

- y means "may exhibit the feature" and n "never does", as in Reynolds (2021); marginal as in the matrix; blank means not coded.
- **Restrictive pre-head AdjPs only.** Names in their primary use take non-restrictive adjectives (*young Isaac Newton*, *CGEL* pp. 520–521), a wider range than the pronouns' *lucky*/*poor*/*silly*; both are left to the existing exclamative column, so names and pronouns are coded alike here.
- **Primary uses only.** The secondary set-denoting use (*the real me*, *the Kim I knew*) is excluded; otherwise every pronoun and name would take determiners and adjectives.
- Case features are coded for the plain form (*dog*, not *dog's*); the paradigm features carry the genitive.
- Features coded for pronouns at NP level (*almost*, *at least*, *not*) are coded the same way for nouns (*almost a dozen*).

## Judgments that need Brett

1. **Gender.** The five gender columns are coded on *CGEL*'s terms: a noun's head selects *who* or *which*, *he* or *she*, so *Kim* and the CN row get personal gender. On Reynolds (2025), descriptions and names shape referent construal, while pronouns and determinatives carry the contrast in the word. On that view nouns would be n, and gender becomes a property only pronouns and determinatives share, which is evidence for nesting. This is the most consequential single choice in the coding.
2. **Some columns are left blank.** The semantic number and countability columns are blank for *tall* and the adjective row, since for adjectives they depend on the noun. Three semantic columns are blank for every new row: `proportional` (coded y for *a*, *that*, *these*, and the cardinals, n for *all*, *each*, and *the*), `distributive`, and `joint` (y for *his* and *mine*). Their senses can't be recovered from the coded forms.
3. **Two sense inferences**: `existential` (n only for wh-forms, generic *one*, dummy *there*, and *zero*) is read as "can carry existential import"; `has_corresponding_word` as "has a homonym in another category".
4. **A matrix inconsistency**: the compounds are n for `paradigm_has_genitive_form` but y for `inflects_for_case`. *CGEL* gives *dog's* as a form of *dog* (ch. 5 §1 [3]), so the nouns are coded y; the compounds should probably match.
5. **Two columns that can't be told apart**, `functions_as_prehead_modifier_in_nominal` and `functions_as_attrib_modifier_in_nominal`, are coded alike for the new rows.
6. **Smaller flags**, marked FOR BRETT in `feature-notes.csv`: *dozen* as numeral-like (cardinal, selecting plural heads); quantity nouns' compatibility with count and non-count NPs, coded through the *of*-complement; coordination with independent genitives; *all Toronto*.
7. **The reused determiner column** still has 30 cells awaiting Brett from the matrix-2026-10 work (its `needs_brett` flag), two of them blank (*thrice*, *zero*).

## Files

| File | SHA-256 |
|---|---|
| `draft_coding.py` (all values and their bases) | 3372da71195344c5b1a20a3e1e0cc4e102a1c62b2bda2a10fbc78143332e0f77 |
| `make_review.py` | 6c3f869538799e039b9ebd902dd8a6f85d29b1b3f1e0904dc0e6c3334a1f052b |
| `proposed-new-rows.csv` (15 rows by 115 columns) | 7840c581e8596836b76475b3f3b6573ffcc067c88b3552e4d8731d2a3a47f6bd |
| `proposed-new-columns.csv` (139 forms by 10 columns) | 5b4830bf794ea9cc657451ea027f55c85f94a5cb3512c6a442cd6ea7c62adfa5 |
| `feature-notes.csv` | d071ee441e8f54d020a4522b6bfacd2495f60f0d80cb434a2b973f0ac94563f9 |
| `features-added.csv` | be92dd4427d583e33720af8ac04d426cbd421ce5bc6a3cf1291a410913a3e26b |
| `REVIEW.md` | c7b4204f95533d16cd5d0798fcb450c66de959c1173fc9ce7cd0d04be18f862f |
| input: `../matrix-2026-10/new_feature_values.csv` | 4f7ca1debcd34bffc1a882c6e71e5000c9d0d1532ab0a58fab609b35c6762256 |

Input matrix as in `../node-reach-2026-10-24/README.md`. Regenerate with `python3 analysis/noun-coding-2026-10-24/draft_coding.py && python3 analysis/noun-coding-2026-10-24/make_review.py`.

## Not done yet, deliberately

None of the tests in `notes/nesting-tests-2026-10-24.md` has been run on these values. Results computed on unjudged cells could steer the judging, so they wait until Brett has been through the review sheet.
