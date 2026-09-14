# Bounded audit: recategorization of determinatives (D-noun vs. separate D)

## Outcome

Equivalence holds for the encoded fragment, but it is **essentially definitional**,
and it holds only under an invariance assumption the prose does not state. The
audit found one concrete underspecification: the fragment does not say whether
conditions other than the head-category condition are indexed by the *primary*
category or by the noun *subcategory*. Under the primary-category reading of one
condition the fragment does state — "A singular count noun normally requires
determination" — the two accounts come apart, and the divergence is proved.

## Scope checked (`DetTaxonomy.lean`, core Lean 4 only)

Encoded: the fragment's lexeme inventory from Table 1; lexeme-level use
permissions `U` (Det, Mod, Subj, Obj/CompP); form selection kept separate from
permissions, so *no*/*none* and *my*/*mine* are one lexeme each with two forms
distributed by function (likewise *she*/plain *her*); the two `Cat` assignments
(`cat1` constant `N`; `cat2` sending determinatives to `D`) and the two head
conditions `Cat(h) = N` versus `Cat(h) ∈ {N, D}`; the at-most-one-Det
restriction; a flag for the internal/peripheral modifier boundary; and `C`
(target and remaining dependent conditions) as an opaque parameter.

The two grammars use *different* head-category predicates over different `Cat`
functions; their agreement (`headOK_agree`) is proved, not assumed. Not
encoded, deliberately: tree geometry, partitives, comparatives, compounds,
approximative attachment sites, complex *a few*, the fusion analyses, and the
independent-genitive agreement issue.

## Assumptions added

1. **Invariance.** Both grammars use the same `uses`, `formOK`, `structuralOK`
   and the same parameter `C`; i.e. every condition except the head-category
   condition is indexed by lexeme or noun subcategory, never by primary
   category. This is a modelling assumption, not a stated condition.
2. The determinative/non-determinative split is the only classification the two
   taxonomies treat differently, and pronouns are nouns in both.
3. `Obj` collapses object and complement-of-preposition (one table column).

## The missing condition

Given assumption 1, `adm1 = adm2` pointwise: the D-noun condition `Cat(h) = N`
and the separate-D condition `Cat(h) ∈ {N, D}` are both satisfied by every
lexeme in the fragment, so neither does any discriminating work — all
discrimination comes from `U`, form selection and `C`.

Drop assumption 1 for a single condition and equivalence fails.
`divergence_general` proves: any undetermined singular-count occurrence with a
determinative head that passes the shared checks is admitted by separate D and
rejected by D-noun, once the determination requirement is read as applying to
primary-category N. Witness: independent subject *some* construed as singular
with no Det of its own (`Some was left`). Under separate D its head is a D, so
the requirement is inapplicable; under D-noun the head is an N and the phrase is
wrongly excluded. This is *not* a violation admitted by both grammars — it is a
genuine asymmetry between them.

The precise missing statement the fragment should add: **every condition stated
over the category Noun — in particular the determination requirement on
singular count nouns — is indexed by the noun subcategory excluding
determinatives, not by the primary category N.** Whether English supplies a
determinative-headed phrase that is both singular count and independently usable
is not settled by the fragment; the fragment does assert that
determinative-headed phrases bear number and count properties, and it does not
exclude such a case, which is what makes the gap real rather than hypothetical.

## Does the formalisation add value?

Modestly. The equivalence is definitional once recategorization is set up, and
should be presented as such, not as independent support for either taxonomy.
What the formalisation adds is the load-bearing assumption: encoding forces
every condition to declare whether it is indexed by primary category or
subcategory, and that is exactly where the prose is silent.
