# Corrected Aristotle prompt

Run one bounded audit of the ordinary-Head fragment in `fragment.tex`. The previous audit's Lean file compiled, but its linguistic encoding was inaccurate. Start afresh from the source and the explicit constraints below. Do not use the previous encoding as your specification.

## Question

Does the fragment correctly keep the external use permissions of a whole NP separate from those of its embedded determining phrase? Seek a concrete countermodel or missing condition. Recategorization equivalence is only a secondary consistency check: proving equality after all other conditions have been held fixed is not the principal objective.

## Ground truth and scope

The relevant lexical assignments are:

| Lexemes/forms | D-noun account | Separate-D account |
|---|---|---|
| the, a, every, some, few, no/none | Determinative within primary Noun | Primary D |
| my/mine, she/plain her | Pronoun within primary Noun | Pronoun within primary Noun |
| apple/apples, book/books | Common noun within primary Noun | Common noun within primary Noun |

Preserve the common-noun, pronoun, and determinative distinctions when changing the primary classification. Include executable checks that my/mine remain primary Noun in BOTH accounts. Keep lexeme identity and surface form separate; no/none and my/mine each constitute one paradigm, with different forms selected for different functions.

Lexical and constructional restrictions are explicitly held fixed. Do not present that stipulation as an undisclosed assumption. Do not add a primary-category rule whose applicability changes under recategorization and call the resulting divergence a counterexample to the stipulated comparison.

The determination requirement illustrated by bare `Book arrived` concerns the ordinary singular-count common-noun argument construction. It is not a universal requirement on everything within primary Noun. Singular agreement does not establish count status. Keep the count/number properties of a determining expression distinct from those it selects in its target. Do not assign a feature value to obtain a desired witness without grounding that value in the supplied specification.

## Required analysis

1. Before proving anything, list the relevant source constraints and their proposed representation. Separate explicit constraints, consequences of the stated tree representation, and additional assumptions. A grammatical tree already supplies acyclicity and unique parentage in this ordinary-Head fragment; do not rediscover those as omissions merely because they are not repeated in every formula.
2. Encode actual NP/Nom constituents and their Head/Det relations for a small fragment. Do not replace structural properties with unconstrained flags such as `peripheralOK`. Modifier geometry may be excluded to keep the task small; if excluded, make no claim to have verified it.
3. Keep permissions on the appropriate phrase occurrence. Intermediate Head relations must not create additional argument-permission requirements. Check these source-grounded cases: `the apple` as an argument; `Some left`; rejection of independent `Every arrived`; rejection of bare `Book arrived`; acceptance of `Books arrived`. Also check, within the stated ordinary-use scope, that allowing `the apple` as an argument does not give the embedded article phrase an independent argument use. Exclude quotation, metalinguistic naming, and other exceptional uses as the fragment does.
4. Seek the smallest unintended admitted tree or unintended rejection satisfying all the specified lexical/form constraints. Show every relevant condition on a proposed witness. If none is found in the encoded scope, say so. An underspecified case is not an established English counterexample.

Return one standalone Lean 4 file using core/Std only, plus a report of at most 500 words. Use no `sorry`, `admit`, new unproved axioms, or assumptions that simply assert the desired result. Local checking uses Lean 4.33.1. Distinguish what Lean proves about the encoding from whether the encoding faithfully represents the grammar.

Limit this to ten minutes of active work. Do not expand to the whole grammar, investigate fusion or genitive agreement, search for English data, or revise the manuscript. If the check reduces to consequences already explicit in the definitions, report that outcome plainly and stop.
