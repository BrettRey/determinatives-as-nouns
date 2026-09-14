# Aristotle trial: assessment

14 September 2026 · Codex

**Outcome: limited value; no manuscript change warranted.** One Aristotle job produced a small Lean encoding, a proof of equivalence under shared restrictions, and a claimed divergence after adding a primary-category determination condition.

The returned `DetTaxonomy.lean` passes local Lean 4.33.1 checking. The checked theorems depend only on standard Lean axioms (`propext`, and for the divergence results `Classical.choice` and `Quot.sound`); no `sorry` or new unproved axiom completes them. The service itself reported `COMPLETE_WITH_ERRORS`; local checking establishes the validity of this standalone file, not the correctness of its linguistic interpretation.

The equivalence is essentially definitional: both head-category predicates accept every lexeme in this small inventory, and the remaining conditions are shared. Actual tree geometry and modifier attachment are not encoded; `peripheralOK` is a Boolean flag. This does not independently verify preservation of the full structural analysis.

The alleged counterexample has three problems:

- `Lexeme.isDeterminative` incorrectly includes `myL`, the lexeme covering *my/mine*. These are pronoun forms within Noun in both accounts. The report's assertion that pronouns remain nouns in both is therefore inconsistent with its code.
- The witness sets `sgCount := true` for *Some was left*. Its singular agreement does not establish the count part, and the report supplies no justification for that feature assignment.
- The divergence introduces `detReqPrim`, a blanket requirement indexed by primary N. Its applicability changes under recategorization. This does not refute the stipulated equivalence with lexical and constructional restrictions held fixed; it also strengthens the excerpt's qualified statement that singular count nouns “normally” require determination.

The proposed repair requiring every Noun condition to exclude determinatives is too broad: the paper deliberately shares nominal constraints across the superordinate category. The useful lesson is the ordinary need to distinguish primary-category constraints from subcategory and lexical restrictions. The trial supplies no sound counterexample to the intended comparison. No further Aristotle job was submitted.

Artifacts: [Aristotle report](result/REPORT.md), [returned Lean file](result/DetTaxonomy.lean), [local compiler check](lean-check.txt).
