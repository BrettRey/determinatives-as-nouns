# Corrected Aristotle trial: assessment

14 September 2026 · Codex

**Outcome: a more faithful, locally checked model confirms permission separation in the small encoded fragment. No new manuscript defect is established.**

The second job completed successfully. The returned `RequestProject/Fragment.lean` passes local Lean 4.33.1 checking; its audited theorems depend only on `propext`. It uses actual NP/Nom constituents, correctly keeps *my/mine* and *she/her* within Pronoun and primary Noun in both accounts, separates form selection from lexeme permissions, and excludes modifier geometry explicitly.

The positive result is useful as a limited consistency check: *the apple* is admitted as an argument while every article-*the*-headed NP is excluded from independent subject/object use. The article daughter is checked in Det function, not in the mother's argument function. The specified *Some left*, *Every arrived*, *Book arrived*, and *Books arrived* cases have the intended outcomes. Recategorization equivalence remains essentially definitional under fixed restrictions.

The claimed missing target condition is an omission from the initial encoding. The manuscript explicitly says that C checks both dependents and the target (§5.1), that a nominal has only dependents permitted for its head and construction (§5.2), and that independent *few* permits definite determination (§5.2). The initial `wf` implements the determiner's count/number selection but omits the target's restrictions on its own dependents. Its admission of *few few* therefore doesn't satisfy all the stated source conditions. The report itself quotes the source material used for its repair.

That repair also remains incomplete. A local `#guard` confirms that `wfRepaired` admits a structure with an externally determined *the few* phrase filling Det of a larger NP headed by *apples*. The source expressly excludes external determination within dependent *few*. This is a counterexample to the completeness of the returned implementation, not to the source grammar. The ordinary surface string *the few apples* has a different intended analysis, with *the* as the outer Det and *few* as internal Mod.

Lean certifies the results about these definitions. It doesn't establish that the initial or repaired definitions include all the manuscript's conditions. No manuscript edit follows from this trial, and no third job was submitted.

Artifacts: [Aristotle report](result/REPORT.md), [Lean file](result/RequestProject/Fragment.lean), [local compiler check](lean-check.txt).
