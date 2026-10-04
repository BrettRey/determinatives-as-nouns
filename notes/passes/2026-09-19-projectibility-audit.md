# Projectibility audit, 19 September 2026

<!-- SUMMARY: projectibility-first audit of the rebuilt manuscript: no world-side overclaim anywhere; two warrant findings new since 9 September (l. 52 credits structural regularity to the taxonomy after §5 concedes it to separate D; the secondary-use schema's input class is a list, so it projects nothing and dodges its own counterexample); the every exclusion is the paper's one real projection and its failure trigger has been met by three unread NOW lines · status: findings for Brett, no manuscript change · updated: 2026-09-19 -->

Text: `determinatives-as-nouns.tex` after commit af63c84 with the 19 September quote-audit repair (14,950 words). Skill: `check-projectibility`. Model: Claude Opus 5, whole file read in order. Baseline: the 9 September audit (`2026-09-09-warrant-and-figures.md`), whose verdicts are rechecked against the rebuilt text (6,830 words added since). Per DECISIONS 2026-04-20, HPC is not load-bearing here; this audit asks what the argument warrants, and doesn't ask the paper to adopt a projectibility frame.

## Table

| Check | Status | Evidence |
|---|---|---|
| Declaration | GREEN for the descriptive task | Synchronic English (l. 42, 289), language-specific categories (l. 42 n.), two independent claims separated (l. 50–54, 73), the fragment's scope stated (l. 588). |
| Inquiry/use, warrant plan, revision rule | GREEN / YELLOW | The evidence-type paragraph (l. 91) is new and good: *CGEL* descriptions, starred forms, attestations, and bounded searches "establish different things", and absence "supports an exclusion in proportion to the opportunity". Revision conditions are stated for phrase structure (l. 706, 742) and nesting (l. 772). None is stated for the central taxonomic claim beyond the comparative one at l. 742. |
| Non-trivial projection | YELLOW | As on 9 September: no held-out category prediction. New since then: the secondary-use schema and the complex-determinative reanalysis are offered as consequences outside the diagnostics, and l. 734 says so honestly ("additional consequences, not tests set in advance"). But the schema's input class is enumerated, so it projects to no unexamined lexeme (finding P2). |
| Warrant vs world-side | GREEN, one local inconsistency | No causal, mechanism, or kindhood claim anywhere (`grep` for homeostat, mechanism, projectib, natural kind, stabil: none; *cluster* only for the 2021 statistical clustering). But l. 52 credits the structural regularity to the grouping, which §5.6 withdraws (finding P1). |
| World-side order | Not applicable | No stability, causal-order, maintenance, or control claim. |
| Stabilizer vs controller | Not applicable | No homeostatic or corrective vocabulary. |
| Level and mereology | GREEN | "A grammar can keep D separate" names a description, not an agent. Formal licensing, judgments, corpus counts, and matrix statistics stay at their own levels; l. 774 blocks the rank inference from the matrix. |
| Scope and field-relativity | GREEN | English only; the synchronic argument is kept apart from article history (l. 289); no appeal to usefulness as truth. |
| Prospective revision | YELLOW, one RED instance | The *every* exclusion is argued as a projection with a stated warrant (opportunity-weighted absence, l. 91, 281). Its failure evidence is in the project's own saved lines and has been reclassified as residue without a human reading (finding P3). |
| Positioning and conclusion | GREEN with a limit now explicit | The conclusion claims a grouping supported by the profile and concedes the inherited-feature alternative (l. 794). The advantage over that alternative is stated as representational ("states the domain directly", l. 734), with no projection that distinguishes them (finding P4). |

## Findings

### P1. l. 52 credits the taxonomy with a regularity §5 gives to both taxonomies

l. 52: "Noun membership makes ordinary nominal structure a natural treatment; that structural regularity strengthens the case for the grouping." Against this: l. 54 "a grammar can keep determinative (D) separate while assigning ordinary Head"; l. 740 "These generalizations are available under either ordinary-Head taxonomy"; l. 734 the audit "doesn't establish a strict description-length advantage over the feature formulation"; and the abstract "separates the structural saving from the taxonomic choice". After today's admission of the inherited-feature alternative, the structural regularity is evidence for ordinary Head, not for Noun membership. The warrant for the grouping is the profile comparison (§2.6), which l. 734 and l. 794 now say.

Proposed repair: "Noun membership makes ordinary nominal structure a natural treatment, though a separate category can adopt it too (§\ref{sec:overall-assessment})." or cut the second clause of l. 52. Either keeps the introduction consistent with §5.6 and the abstract.

### P2. The secondary-use schema's input class is a list, not a property

l. 758 states the rule over "a Noun lexeme whose primary use identifies or quantifies over individuals, a name, a compound determinative, or a cardinal". Read by its property, the rule covers *every* and *each* (they quantify over individuals) and the personal pronouns (they identify individuals). l. 760 then excludes *every* and the articles (\ungram{\mention{an every}}) and leaves the pronouns open. Read as a list, the rule covers exactly the three cases already observed and says nothing about any other lexeme. Either way the schema doesn't project: the property over-generates and the list is fitted to the data (the compound case entered after the 17 September COCA counterexamples, DECISIONS 17 September).

The paper's own glosses point to a property that would project: each input supplies its own description of the individuals ("the bearers of the name, the persons or things of the quantifier's description, the groups of the cardinal's size", l. 758). The compounds carry *-one/-body/-thing*; *every*, *each*, and the articles have no description without a following nominal. Stated that way, the schema:

- excludes *an every* and *an each* for a reason rather than by listing;
- predicts that personal pronouns, which carry person and gender, have the use (*the hes and shes*), turning the question l. 760 leaves open into a test with a stated outcome;
- predicts the restrictor question in the l. 760 footnote (*a certain someone special*) only if the restrictor belongs to the compound construction, which §4.5 says it does, so the set-denoting use should lose it. That is a checkable consequence.

This is the one place the paper could gain a projection without new theory. Whether *the hes and shes* is attested isn't established here (no search was run), and nothing should be written about it until one is.

### P3. The *every* exclusion is a projection whose failure evidence was reclassified unread

l. 91 and l. 281 argue the *every* exclusion in projective form: where the opportunity for independent use is frequent (independent *each* before a finite verb, 3,090 string hits), a licensed use would show up, so its absence licenses the exclusion. That is the paper's clearest projective claim, with a stated warrant and an implicit failure trigger: attested ordinary fused-head *every* in the screened lines.

The saved NOW lines contain three such cases in edited prose, each with an antecedent set, the configuration §4.2 treats as ordinary fused-head use for *some* ("the relevant substance or set may still be supplied by discourse"): *Every has its strengths* (wheels24, 2020), *Every has a story* (patch.com, 2025), *Every has different blocking mechanics* (Guardian, 2024). They are listed in `corpus/exclusion_tests/every-reading.md`, whose status line says "read by Claude, not yet by Brett" and whose conclusion is "A categorical exclusion is too strong as stated". The footnote at l. 281 says "None of ... 164 NOW lines ... shows an ordinary fused-head use" and describes the residue as ellipsis and binomials.

In projectibility terms this is the signature move the audit exists to catch: the failure trigger was met, and the claim survived because the misses were placed outside the declared population ("ordinary") after the fact. The honest options are Brett's: (a) read the three lines and, if they're fused heads, restate the exclusion as a rate (three in 164 NOW lines, all with an antecedent set, none antecedent-free), which the opportunity argument still supports and which keeps #*Every arrived*; or (b) argue that an antecedent in the preceding sentence makes these ellipsis, and then say why the same doesn't hold for *each has its strengths*. Full detail in `2026-09-19-measurement-construction-audit.md`, M1. **No manuscript change made.**

### P4. What distinguishes Noun membership from the inherited feature is now representational

With l. 732–734, the separate-D feature alternative shares the head condition, head-genitive definition, and secondary-use schema. The paper's remaining reason for Noun is that "the profile comparison independently supports that grouping" and "the category then states the domain of the shared grammar directly". No projection is offered on which the two differ, and the paper doesn't claim one, so this isn't an overclaim. It does mean the taxonomic conclusion rests entirely on the §2.6 weighing, and a referee who weighs the grade/degree profile more heavily has nothing else to be persuaded by. If a differentiating projection exists, it's likely in P2's direction (whether Noun membership predicts which determinatives acquire common-noun secondary uses), not in the fragment, where the two are equivalent by construction. Nothing to repair unless Brett wants that argument.

## Is projectibility structural or decorative?

Neither, by design: the paper makes a descriptive taxonomic and structural proposal and doesn't use projectibility vocabulary. The 9 September verdict holds: the category earns a descriptive role (shared projection, restrictions placed as lexical conditions), with no held-out prediction. What's new is that two parts of the argument are projective in form without saying so, the *every* exclusion (P3) and the secondary-use schema (P2); the first has met its failure trigger and the second is stated in a form that can't fail.

## World-side commitment reached

None claimed, none needed. The evidence reaches a stated distributional profile and a grammar fragment that covers the matched cases. No sentence upgrades that to stability, causal order, maintenance, or control.

## What would change structurally

1. Make the *every* argument's evidence match its conclusion (P3): a restriction stated as a rate with a reading-dependent exception, or an explicit ellipsis analysis applied to *each* as well.
2. State the secondary-use schema by the property its glosses already name (P2), so it excludes *every* for a reason and makes a prediction about pronouns and the post-head restrictor.
3. Stop the introduction crediting the grouping with the structural regularity (P1), so the taxonomy rests where §§2.6 and 5.6 put it.
