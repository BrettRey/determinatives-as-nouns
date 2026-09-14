# Audit report: permission separation in the ordinary-Head fragment

Artifact: `RequestProject/Fragment.lean` (standalone, no imports, core only; no
`sorry`, no new axioms — all results depend on `propext` alone).

## What was encoded

§A of the file separates **explicit source constraints** (E1–E9: the permission
table, form selection within the `no/none`, `my/mine`, `she/her` paradigms, the
"intermediate Head relations require no further argument permission" clause, the
target restrictions, the one-Det NP core, and the two Cat conditions),
**consequences of the tree representation** (T1–T2: acyclicity and unique
parentage come free from the datatype and are not audited), and **additional
assumptions** (A1–A5). Constituents are real: `NP.bare`/`NP.det` with a `Nom`
Head and at most one Det, which is itself an NP. No flag stands in for
structure. Modifier geometry is excluded, so nothing is claimed about peripheral
modification or the third structural condition.

## What Lean proves about the encoding

Source-grounded cases, under **both** accounts: `the apple` admitted as
Subj/Obj; `Some left` admitted; `*Every arrived` rejected by use permission;
`*Book arrived` rejected by the determination requirement (and *only* that —
`permitted book Subj = true` is proved separately); `Books arrived` admitted.
Target restrictions bite: `*a apples`, `*every apples`, `*some apple` rejected,
`the few` admitted.

Permission separation holds in the encoding, in both directions. Downwards:
`article_phrase_never_argument` proves for **every** NP headed by `the` that it
is inadmissible as Subj and Obj, so admitting `the apple` confers no independent
argument use on the embedded article phrase; `no_article_leak` confirms this by
enumeration. Upwards: `no_extra_argument_requirement` shows the mother's
argument admissibility is computed from its own head, form, well-formedness and
determination only; `det_daughter_needs_only_det_permission` shows the daughter
is held to its Det permission alone. This is a consequence already explicit in
the compositional definitions, and is reported as such.

Recategorization equivalence (secondary) holds: `catOK` is satisfied by every
form under both accounts, so `admissible` is account-invariant. `my/mine` and
`she/her` are Pronoun and primary Noun in both accounts (executable `#guard`s
plus `pronouns_primary_N_in_both`); only determinatives change primary category.

## Finding: a missing condition elsewhere

An exhaustive search over all depth ≤ 2 trees returns 44 admitted subjects,
including `*few few`, `*the she`, `*my mine`, `*no none`, `*the some`. The
smallest witness is two words. For `*few few` every condition is source-supplied
(`few`: Det permission, target restriction plural count; `few` phrase: plural
count, stated in the source) — no feature value was invented. The gap is not in
permission separation but in the target condition: the fragment constrains a
Det's target by count/number only, and states no condition on the target head's
category. `targetAcceptsDet`/`wfRepaired` formalise the source's own prose
(pronouns take no Det; among determinative-headed targets only `few`, and only
under definite determination) and `repair_effect` proves it removes exactly
these admissions while retaining `the few`, `the apple`, `every apple`,
`some apples`, `my books`.

## Caveat

Lean certifies these facts about the encoding, not that the encoding faithfully
represents the grammar. Faithfulness rests on the E/T/A audit in §A.
