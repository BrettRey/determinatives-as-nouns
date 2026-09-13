# Review through §5: your edits and Fable’s audit
I’ve checked all 10 comments and 18 remaining suggestions in the [annotated reading copy](../notes/determinatives-as-nouns-review-2026-09-12-quantifier-controls.md), including changes outside explicit markup, against the current source and [Fable’s complete audit](./fable-section-5-2026-09-13/fable-audit.md). The reading copy predates the last introduction/§5.3 repair; those source changes remain the baseline.

My recommendation is to retain the four-way comparison and its explicit structural commitments, but present §5 as a **constraint-based fragment**. Your additions strengthen the modifier comparison. Fable identifies useful omissions, but several of its diagnoses and proposed fixes need qualifying.
## “Rules” and the alternatives — your comment c8
There are two issues: how a linguistic description is formalized, and whether its formal statements are things the language or its speakers literally possess or execute. Production notation alone doesn't commit an analysis to a psychological sentence-production algorithm. Keeping the present schemata is therefore defensible. Their practical disadvantage here is that arrows, derivations, and “rules” invite a generative reading and encourage counting productions, while the important restrictions sit elsewhere in the prose.

Pullum’s model-theoretic alternative treats grammatical statements as constraints evaluated on individual structures. Formal explicitness survives; construction by successive operations is unnecessary. That is the relevant distinction for this paper, without needing a broader argument about what counts as a rule. See [Pullum (2020), especially §§1 and 3](https://cadernos.abralin.org/index.php/cadernos/article/view/279), DOI 10.25189/2675-4916.2020.v1.n1.id279.

| Approach | What it offers | Main drawback here |
| --- | --- | --- |
| Retain the arrows, explicitly interpreting them as descriptions of local configurations | Smallest change; familiar, compact notation; preserves the worked comparisons | Readers must keep overriding the usual rewriting interpretation; much still depends on unexpressed conditions |
| State constraints on labelled structures — recommended | Makes Head, dependent functions, selection, and fusion explicit without derivations; brings the restrictions into the comparison | Requires a bounded rewrite of §5.2 and a check that its statements match the diagrams |
| Use prose and diagrams alone | Easiest to read; removes most notation | Makes the omissions Fable found easier to leave unresolved; weakens the promised explicit comparison |

I recommend the {==second approach==}{>>agreed<<}{id="c1" by="user" at="2026-09-13T13:23:40.099Z"}, at the level of a small descriptive fragment. A complete axiomatization or a new section defending model-theoretic syntax would exceed what this argument needs. Use labelled structures rather than insisting on ordinary trees: fusion assigns two functions to one constituent.

A possible replacement opening is:

> The fragment states conditions on the constructions being compared. Each account assigns categories and Head relations to the same expressions. The conditions specify permitted functions, dependents, and combinations of forms; they don't describe a sequence of operations for constructing an expression. Comparing the accounts makes their commitments explicit, without treating the number of written statements as a measure of grammatical economy.

The revised presentation should then state the following conditions concretely:

- **Head category:** where a word directly fills Head in Nom, the ordinary-Head accounts admit Noun under D-noun, or Noun and D under separate D. Keep nominal cores and peripheral NP layers distinct.
  
- **Function and form:** specify Det, internal Mod, subject, object, and complement-of-preposition permissions for the relevant entries. Distinguish lexical permissions from selection of forms such as _no/none_ and _she/her_.
  
- **Structure and selection:** write the condition as `C(x, f, s)`, where `x` is the phrase occurrence, `f` its function, and `s` the surrounding structure, including its target. This makes internal dependents and target compatibility available explicitly.
  
- **Construction-specific dependents:** distinguish ordinary Det/internal-Mod uses before another nominal from independent uses with partitives, relatives, or external determination. Retain licensed NP and determinative degree modifiers, including _a lot fewer_ and _this much_, and distinguish partitive from comparative complements.
  
- **Fusion:** state the shared constituent’s two function relations and its permitted dependents directly. Keep these configurations consistent with the diagrams, including the additional nominal layer in Mod–Head fusion.
  

This change makes the comparison inspectable. It doesn't itself establish an economy advantage: the content, distribution, and reuse of the conditions still have to be compared.
## Your prose and table edits
| Location / suggestions | Recommended treatment |
| --- | --- |
| §2.1, s1: “four noun groups” | Accept. It makes the intended comparison explicit. |
| §2.4, s3–s7: _very, so,_ and _too_ | Accept the broader degree series and varied examples. Change the following “It also excludes” to “These degree modifiers also exclude” so the paragraph remains coherent. |
| §2.4, s8: “NP grammar” | Accept. “Nominal” risks being read as the constituent Nom, whereas this contrast concerns whole NPs in predicative and argument functions. |
| §2.5, s9: pro-forms | Include the connection, phrased as “Many determinatives also have pro-form uses.” This locates the property in uses without making every occurrence pro-formal. |
| Table 3, s10–s17: nominal and DP modifiers | Add the missing modifier types, but distinguish category, attachment, and function as explained below. |
| §4.4, s18–s19: adverbs such as _very_ and _too_ | Accept; retain the existing _very_ examples as illustrations of the broader class. |

The table needs a targeted correction rather than the same addition in every column. Proper names do have nominal premodifiers, as in _architect Norman Foster_ (CGEL, 519–520). For pronouns, CGEL normally excludes internal pre-head dependents apart from restricted adjectives such as _poor_ and _lucky_. It places _all_ in _all we who have signed up_ outside the NP’s internal structure (429–430). That example belongs in the peripheral row. I wouldn't add internal nominal premodifiers to the pronoun cell without a supporting example and analysis.

Use **determinative-headed phrases** where the table needs to remain neutral between DP and NP analyses. Demonstratives used as determiners of names, such as _this Penelope_, also belong under determination, rather than automatically becoming internal modifiers. The modifier evidence should be included at the attachment level it actually supports.
## Your comments on examples, evidence, and figures
| Comment | Assessment and recommended action |
| --- | --- |
| c1: abrupt introduction paragraph and _weeks-long/meters-tall_ | Already addressed in the source: the introduction paragraph is removed and the significance is explained in §5.3. Your new COCA material warrants extending that repair. |
| c2: citation for _something reliable and good looking_ | Agreed. Use it as an ordinary illustrative example without the CGELBank citation or sentence-ID footnote. Its provenance can remain in the supplement; attestation isn't doing argumentative work here. |
| c3: unresolved cells | I left 14 cells without sufficient evidence. These are gaps in my collection, not evidence of marginality. The table currently mixes documented uses and grammatical descriptions in a way that makes those gaps too easy to misread. Complete the targeted checks before treating it as a distribution table supporting a cline. Until then, identify it explicitly as an {==incomplete evidence inventory==}{>>why not complete the inventory?<<}{id="c2" by="user" at="2026-09-13T13:25:27.921Z"}; simply changing `?` to a different symbol wouldn't complete the work. |
| c4: four trees in one row | Yes, they should fit at the present text size. Their combined text widths are about 341 PDF points within the 450-point text block, leaving room for separation. Group the first pair under CGEL and the second under D-noun, with compact dependent/independent labels. The arranged figure still needs a final visual check. |
| c5: deeper Honda source | It is an EWT web-review sentence, not GUM. I verified the exact sentence as `reviews-083459-0002`, document `reviews-083459`, in the [upstream UD English EWT training data](https://github.com/UniversalDependencies/UD_English-EWT/blob/master/en_ewt-ud-train.conllu). Cite that textual source; reserve CGELBank attribution for the annotation. The original review webpage wasn't identified. |
| c6: branch south, not southwest | Confirmed in the PDF: the fusion tree’s Nom-to-Mod:AdjP edge still slopes southwest. Place the _present_ branch directly beneath Nom and make that edge vertical. The diagonal Head relation to the fused DP is a separate edge and should remain. |
| c7: parentheses around `Mods_post` | Its definition already permits an empty sequence, so the current notation doesn't require a postmodifier. But the visible inconsistency with the other optional dependents is avoidable. In the revised constraints, say “zero or more ordered postmodifiers”; if the slot notation remains, use parentheses and define the enclosed sequence as non-empty. |
### The new §5.3 evidence — c9 and c10
Your COCA examples are stronger than the earlier bare plural compounds because they include overt numerals and _several_: _a 45 pages long booklet_, _a several pages long passage_, and _a 10 feet long cord_. Retain representative examples with the supplied year, register, and source metadata. They challenge an unqualified exclusion of plural measure expressions in this attributive position. A compound analysis remains possible, but merely relabelling them compounds doesn't settle the syntax. The indefinite article belongs to the outer NP; its presence doesn't make _several pages_ an article-bearing modifier.

The temporal examples make a different point. On your analysis, _every Tuesday_, _this week_, and _next week_ are post-head NP modifiers inside AdjPs. The separately modified coordinates in _Anyone [very busy this week] but [completely free next week]_ make the intended attachment particularly clear. Include this comparison: NP modification of an adjective phrase needn't be pre-head. Keep the semantic distinction visible, since these are temporal modifiers, whereas _enough_ expresses degree.

Together, these additions support a broader comparison of function, position, and modifier meaning. They don't establish that all nominal degree modifiers have the same distribution.
## How I would use Fable’s findings
| Finding | Assessment |
| --- | --- |
| 1. Hidden restrictions / overgeneration | Make the restrictions explicit and compare their costs. “Demonstrated overgeneration” is too strong while the existing prose leaves `C_h` open. Fable’s proposed restriction to AdvP modifiers is itself too narrow: it would exclude the manuscript’s _a lot fewer_. Its conclusion that projection economy disappears is also premature without an explicit comparison. |
| 2. Missing internal-Mod permission | Accept the repair. The prose already uses this function, but the permission display doesn't record it. A partial table doesn't prove that `U_h` contains only two permissions; it does leave the formal presentation incomplete. |
| 3. Two approximative attachment sites | Accept as a cost to acknowledge. Retain the current attachment analysis provisionally and state the complication. Changing all determinative approximatives to Nom-internal attachment would need independent justification, not just a shorter description. |
| 4. Phrase-label “cost” | Don't adopt a new premise that an NP must have a lexical N head. That would prejudge the separate-D ordinary-Head alternative. The distinction between inherited Noun structure and structure admitted across a primary-category boundary can remain a fit argument, without treating the abbreviation as evidence. |
| 5. Target number/count | State relevant target features and remove the unnecessary “common-noun” limitation. But _the few_ isn't shown to fail merely because _few_’s features aren't listed: _the_ has no count/number restriction. Nor is _this_ in _this much_ automatically a determiner. |
| 6. Predicate signature and form selection | Accept the clarifications: make the inspected phrase and structure explicit, include the relevant PP-complement uses, and distinguish forms from lexemes. These are repairs to explicitness, not major theoretical failures. |
| 7. Complex determinatives | State their treatment or the fragment’s scope boundary explicitly. _A few_ cannot simply be treated as ordinary article _a_ determining plural _few_. Keep the modifier facts in _a very few_ connected to the earlier discussion. |
| 8. Degree uses | Retain the qualified conclusion, strengthened by your new examples. Distinguish post-head temporal NP modification from _enough_’s post-head degree use. Keep the fragment’s formal scope separate from the wider distributional comparison. |
| 9. Fusion representation | Align the structural descriptions with the figures. Separate “fusion applies once” from restrictions on the inner phrase’s dependents: the former doesn't by itself enforce the latter. |

The resulting revision would preserve the paper’s case while making its qualifications and comparative commitments easier to assess. No manuscript changes have been applied during this reconciliation.
