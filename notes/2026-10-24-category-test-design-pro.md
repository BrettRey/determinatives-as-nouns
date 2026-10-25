# Designing the category test: GPT Pro's response
<!-- SUMMARY: GPT Pro's two-part response to notes/2026-10-24-prompt-for-outside-models.md (primary design; then the question of adding prepositions or verbs), saved verbatim · status: for Brett · updated: 2026-10-24 -->

Pasted by Brett into the Claude Code session on 24 Oct 2026 and saved verbatim by Claude; model output, unedited. Pro read the repository at commit `d967c4b`. Triage: `notes/2026-10-24-category-test-design-triage.md`.

## Part 1

I’d make the primary analysis a test of **whether a proposed classification supports prediction across independently specified property families**. I wouldn’t yet preregister a four-way competition to recover the correct taxonomy.

The distinction matters because the four classifications don’t, by themselves, specify probability distributions over your cells. A statistical test becomes possible only after adding assumptions about inheritance, exceptions, and the distribution of properties. Those assumptions need to be explicit—and sufficiently defensible that a result would bear on the linguistic proposals.

My recommended design is a Bayesian multilevel measurement model, with the rival classifications supplying alternative structures for sharing information, evaluated by withholding whole lexical-by-property-family blocks. It should include a model without higher category structure and a model allowing overlapping affiliations. *Unresolved* and *none of these models predicts adequately* must be possible outcomes.

I inspected the named branch at commit `d967c4b`. The public files support several substantive corrections to the brief’s interpretation of the simulations. I couldn’t reproduce the empirical applicability counts because the local cell ledger used to construct them isn’t in the public checkout. The proposed sample sizes below are budgeting scenarios, not results of a newly completed power study.

## 1. What this matrix can adjudicate

### The classifications need explicit statistical commitments

Suppose every analysis can assign an unrestricted exception to every lexeme–property combination. Every analysis can then reproduce the same matrix. Nesting, coordination, and separation become distinguishable only when they constrain which exceptions are expected, which generalizations are shared, or how much independent specification is required.

For example, the nested analysis might be operationalized as predicting that, after accounting for morphology, individual lexemes, and construction families, pronouns and determinatives share additional variation across properties. That’s testable. But it’s an additional interpretation of nesting. Nesting alone doesn’t entail that most determinatives have most pronoun properties. Nor does coordination entail equal distances among the coordinate subcategories.

This matters especially for your economy arguments. A covariance model tests one conception of economical organization: how effectively a structure shares statistical information. It doesn’t automatically measure the economy of grammatical rules. If the substantive argument concerns stating one constructional generalization instead of three, the rule formulations and their exceptions still need to be compared directly.

I’d therefore distinguish two claims throughout:

- **Predictive claim:** a specified inheritance model improves prediction of grammatical behaviour in a declared domain.
- **Grammatical interpretation:** that improvement supports treating a particular collection as a lexical category or subcategory.

The first can provide evidence for the second. It doesn’t determine it without further argument.

There’s also a coverage issue. Your [evidence ledger](https://github.com/BrettRey/determinatives-as-nouns/blob/d967c4b164e334cb199657b115322b38a6469442/planning/evidence-ledger.md) records that Hudson sets aside some relevant forms, and that the English adjective/noun split is an extrapolated hypothesis based on Van Eynde’s criteria. Before comparison, each operational model needs a complete, frozen assignment map for the common evaluation set. Where a source is silent, either restrict a historical comparison to its covered domain or label the completion as your operational extension. Different models can’t earn comparable scores on different subsets.

### A specific limitation of the current five-group comparison

There’s a further identification problem that isn’t merely a question of sample size.

Consider common nouns, proper nouns, pronouns, determinatives, and adjectives. In an additive tree-covariance model, a shared node contributes variation to all its descendants. After removing each property’s overall level, variation shared by the four nominal groups is indistinguishable from variation specific to the sole adjective group in the opposite direction.

Consequently, with freely varying terminal effects, the coordinate model’s all-nominal node can be absorbed into adjective-specific variation. For these five groups, its relative covariance structure is equivalent to a star without that nominal node.

That doesn’t make all three trees equivalent:

| Operational structure | Nontrivial grouping that can remain in relative profile variation |
|---|---|
| Separate | Common nouns, proper nouns, and pronouns together, against determinatives and adjectives |
| Nested | Pronouns and determinatives together, against the other groups |
| Coordinate | No corresponding nontrivial split among these five groups |

A sufficiently strong internal effect can distinguish the first two from the star. But a star-like result doesn’t positively establish the coordinate Noun parent. It might simply indicate that neither alternative split is supported.

A second informative nonnominal reference group—verbs, for example—would make the proposed nominal grouping a nontrivial contrast against adjectives and verbs together. That’s a reason to consider another reference group. It only helps if the property bank describes its behaviour meaningfully.

### What the existing simulations actually establish

Three qualifications are particularly consequential.

First, [the main generator](https://github.com/BrettRey/determinatives-as-nouns/blob/d967c4b164e334cb199657b115322b38a6469442/analysis/tree-recovery-sim/simulate.py) gives every node the same effect variance. Nesting therefore automatically increases the marginal variability of pronouns and determinatives; separation automatically reduces the determinatives’ tree-induced variability. These variance signatures aren’t consequences of the linguistic classifications. Recovery tests topology together with those additional restrictions.

Second, [the applicability simulation](https://github.com/BrettRey/determinatives-as-nouns/blob/d967c4b164e334cb199657b115322b38a6469442/analysis/tree-recovery-sim/real_patterns.py) converts *x* to *n*, infers category-wide restrictions from all-negative samples, assigns proper nouns the common nouns’ restriction pattern, and then overwrites whole blocks of simulated cells with zeros. The resulting observed distribution generally no longer follows the original generating tree. Near-universal selection of the nested model demonstrates domination by the imposed pattern; it doesn’t establish a calibrated rate of bias against a known observed structure.

Third, weak discrimination under form holdout isn’t an impossibility theorem. The implemented predictions still differ across trees through their pooling. The defensible conclusion is that abundant information from other members of the same narrow group can make higher structure contribute very little. Wang and Gelman’s study of multilevel model comparison provides a closely relevant demonstration of how predictive differences can become difficult to detect. [sites.stat.columbia.edu](https://sites.stat.columbia.edu/gelman/research/published/final_sub.pdf?utm_source=chatgpt.com)

I’d retain the simulations as exploratory evidence about sensitivity. I wouldn’t carry forward either *100/24/24* or *115 columns* as an established design requirement.

## 2. The primary method: conditional transfer across property families

### The prediction task

The central question should be:

> When we learn about a grammatical property in a reference panel, which proposed classification best predicts its extension to the disputed items?

That gives the hierarchy something substantive to do. It also avoids completely removing the very group whose relationship you need to estimate.

A concrete evaluation fold would work as follows.

1. **Withhold a whole property family.** Include its related frames, logical derivatives, and near-duplicate diagnostics.
2. **Fit the structural model on the other families.** Determinatives contribute evidence here about their relation to the reference items.
3. **Reveal the withheld family only for a predetermined donor panel.** These observations establish the family’s baseline and how it behaves in the reference items.
4. **Predict the withheld family for the target panel.** For the main determinative comparison, withhold the relevant family from the entire predetermined determinative target set, including related forms.
5. **Score exactly the same target observations under every rival.**

The target and donor panels are frozen lists of item identities. Their use doesn’t declare that their traditional category labels are correct.

This design also avoids an otherwise serious problem with withholding an entire family: without any observations describing that family, a model might have no basis for predicting its direction or baseline. The donor observations supply that information while leaving its extension to the targets unobserved.

Conversely, withholding determinatives on every property creates a different difficulty. Under the nested model, the proposed pronoun–determinative node then has only pronouns represented in training. With unrestricted branch variances, its contribution can’t be separated from pronoun-specific variation. Learning from other property families provides information that complete group removal discards.

These are different predictive questions, not competing technical implementations of one question. The conditional-versus-marginal distinction in latent-variable model comparison is directly relevant here. [arxiv.org](https://arxiv.org/abs/1802.04452?utm_source=chatgpt.com)

### The model’s structural component

I’d use a multilevel model whose latent property profiles have covariance constrained by each hypothesis. Schematically:

**Covariance = contributions from shared nodes + subgroup-specific variation + lexeme-specific variation.**

Each internal node gets an estimable, regularized contribution. Terminal variation can differ among groups. An extra node must be allowed to contribute negligibly.

The main assumptions would be:

- Property-family profiles are sufficiently comparable, within the declared domains, for sharing learned from some families to inform others.
- The proposed category structure constrains that sharing.
- Residual dependence from lexemes, morphological bases, frames, and measurement is represented adequately.
- Exceptions are constrained enough for the structure to make predictions.

I’d check priors on observable profile contrasts, rather than assigning identical priors to every edge and assuming that makes the hypotheses comparable. Different depths and numbers of edges otherwise induce different amounts of prior variability.

A continuous prior on a nonnegative variance gives probability one to a positive value. Thus, *the posterior probability that the shared-node variance exceeds zero* would be an unhelpful evidence measure. Assess whether its magnitude or predictive contribution exceeds a declared meaningful threshold, or explicitly compare a zero-contribution model.

### Scores and uncertainty

Use predictive probabilities, with mean log score as the primary measure and an ordinal probability score as a sensitivity check. Percentage correct discards too much information about uncertainty. Proper scoring rules provide the relevant foundation. [sites.stat.washington.edu](https://sites.stat.washington.edu/raftery/Research/PDF/Gneiting2007jasa.pdf?utm_source=chatgpt.com)

For the primary target of individual grammatical predictions, average scores within each predetermined lexeme and property family, then combine them using fixed design weights. Report the uniform-form version too. If joint property patterns are themselves the target, additionally evaluate joint predictive probabilities; a sum of marginal scores doesn’t fully assess predicted dependence.

Keep the closed panel, probability-sampled reference items, and deliberately selected boundary items separately visible. Any combined score needs explicit mixture weights.

Uncertainty should reflect property families, sampled lexemes, and measurement. Thousands of cells don’t supply thousands of independent replications. Nor should the closed inventory be bootstrapped as though it were a random sample from an unspecified population of additional determinatives.

### How I’d use the alternatives

| Approach | Role in this study |
|---|---|
| Phylogenetic methods | Borrow covariance and contrast mathematics. Evolutionary ancestry and change processes don’t follow from a synchronic lexical taxonomy. |
| Latent classes or mixtures | Test whether a proposed split produces memberships that predict other families. Ordinary mixtures impose exclusive membership and don’t establish hierarchy. |
| Multidimensional item-response models | Useful measurement architecture, provided family dependence is modeled. There’s no reason to impose one dimension of *nounness*. |
| Distances and tree fitting | Descriptive checks of the fitted profiles and their uncertainty. Distances alone lose information about prerequisites, polarity, and measurement. |
| Bayesian marginal-likelihood comparison | Secondary sensitivity analysis, after specifying defensible priors on exceptions, branch strengths, and membership. |
| Overlapping-feature models | Essential competitors to a single tree. They can represent several affiliations for the same item. |

Kemp and Tenenbaum’s *The discovery of structural form* is a relevant precedent for comparing forms of organization rather than assuming that the answer must be a tree. Their particular observation model shouldn’t simply be imported here. [PNAS](https://www.pnas.org/doi/10.1073/pnas.0802631105?utm_source=chatgpt.com)

For multiple affiliation, I’d start with a small, regularized latent-feature model. An Indian buffet process offers a more general framework, but its flexibility is unnecessary for the first implementation. A successful overlapping model would support overlapping predictive organization; it wouldn’t uniquely identify a directed multiple-inheritance grammar. [jmlr.org](https://jmlr.org/papers/v12/griffiths11a.html?utm_source=chatgpt.com)

## 3. The columns: define the domain of projection

### There’s no neutral uniform population of grammatical properties

The universe of possible properties can be expanded indefinitely by conjunction, negation, increasingly specific frames, and alternative descriptions of one mechanism. Uniform sampling from that universe isn’t available.

I’d define a bounded bank of grammatical tasks and operations, organized before confirmatory coding. It should cover the domains relevant to your claim: external distribution, complementation and selection, dependent licensing, morphological paradigms, agreement and reference, binding and polarity, and relevant phonological behaviour.

Use several grammatical sources to enumerate candidates. Preserve source provenance, but formulate questions without requiring a source’s category analysis as the answer. A proposed structure such as fused headship shouldn’t itself become an independently observed property.

I’d distinguish three bodies of evidence.

The **prospective bank** supplies the primary transfer test. Its families, questions, admissible frames, and selection rules are frozen before the confirmatory outcomes are inspected.

The **targeted diagnostic bank** contains each rival’s strongest specific predictions. Targeted evidence is legitimate: a counterexample to a stated restriction doesn’t become irrelevant because someone deliberately searched for it. Its evidential role differs from estimating how prevalent a pattern is across grammatical properties.

The **legacy bank** supplies exploratory patterns and descriptive coverage. It can inform model construction, but its hand-selected columns don’t support design-based generalization to unspecified properties.

Freezing frames before you personally judge their cells doesn’t make the frame selection outcome-independent. Coders who propose frames after examining lexical behaviour have already used outcomes. Hypothesis blinding helps with demand effects; it doesn’t remove feature-selection effects. Develop frames during the pilot, then freeze them for confirmation.

### Weight families, while acknowledging that the weights express a target

A defensible primary specification is equal weight per prospectively defined mechanism family. Within each family, distribute its weight among its declared questions and frames. Also report equal-domain weighting, because otherwise a domain with many named families acquires more influence.

Neither scheme is uniquely neutral. The useful robustness question is whether the substantive contrast survives a range of justified weights. Report which families drive it and how much reweighting reverses it.

The current 31 super-columns are candidates for this organization, not a certificate of 31 independent mechanisms. Audit logical dependencies and shared prerequisites. Preserve distinct correlated phenomena: their correlation may be precisely what requires explanation.

### Treat applicability through prerequisites

I’d use the following distinction.

| Situation | Representation |
|---|---|
| The grammatical operation can coherently be attempted, and fails | Informative *n* |
| A follow-up question presupposes an operation that isn’t available | An observed prerequisite failure, followed by conditional *x* |
| The evidence hasn’t settled the question | Unknown, with its reason |

For example, whether a lexeme has a comparative paradigm can be a meaningful question across a broad inventory. Questions about the shape of its comparative presuppose that such a paradigm exists. Absence of the paradigm should enter once; it shouldn’t create several independent negative observations about its internal structure.

Similarly, several questions about what an expression can accompany in determiner function may share one licensing prerequisite. As composite possibility claims, they might all legitimately receive *n*. Statistically, their common cause needs representation. A model of the prerequisite plus conditional behaviour preserves the evidence without multiplying it.

An all-negative sample doesn’t establish a logical prerequisite failure. Even under independent sampling, if 10% of a population had a property, six sampled negatives would occur with probability about 0.53. That’s an illustration, not an estimate for your nouns; the dependence and purposeful selection in the current sample make the inference still less straightforward.

**I wouldn’t restrict the main analysis to properties that vary in every category.** That selects on the observed outcome and may delete exactly the category-restricted evidence under investigation. Use such a subset as a sensitivity analysis, with its restricted target clearly stated.

### When restricted properties support a shared node

A property confined to pronouns and determinatives supports a shared capacity. Its evidential force for a shared node increases when the proposed grouping predicts other, independently assessed capacities.

It doesn’t follow that the property must reflect that node. Shared morphology, a construction, or an overlapping semantic affiliation may explain the same distribution. Several manifestations of one mechanism provide less independent evidence than several mechanisms.

Nor can the proportion of such properties in the legacy bank estimate their prevalence among all grammatical properties. Ascertainment corrections work when the selection rule is specified. Lewis’s treatment of variable morphological characters is instructive precisely because it conditions on a known selection rule; it doesn’t solve unknown theory-guided selection. [Oxford Academic](https://academic.oup.com/sysbio/article-abstract/50/6/913/1628902?utm_source=chatgpt.com)

## 4. The rows: sample lexemes, preserve forms and uses

The [current row inventory](https://github.com/BrettRey/determinatives-as-nouns/blob/d967c4b164e334cb199657b115322b38a6469442/analysis/codebook/forms.csv) includes *a few*, *a great many*, and *many a*, alongside separate entries for uses of *we*, *you*, and *which*. It’s therefore a mixture of forms, expressions, and form–use records.

That’s manageable, but it needs explicit representation. I’d retain stable record identities and distinguish:

- expression and form;
- lexeme or disputed lexeme linkage;
- stipulated use or frame;
- morphological base and paradigm relationships.

Where rivals disagree about whether two records instantiate one lexeme, run their alternative mappings. Don’t resolve that disagreement silently during data cleaning.

The closed panel can be complete for the stipulated inventory while still containing measurement, variety, and frame uncertainty. I’d describe it as the fixed enumerated panel rather than rely on an unrestricted census claim.

For the open classes, sample **lexemes**, then obtain the forms needed by the selected questions. Preserve form-specific observations. Store lexeme-level facts once: merely adding a random intercept doesn’t justify entering the same paradigm fact repeatedly as though independently observed.

The existing frequency-band sampling idea is sensible. Use random prefixes of a frozen sampling order, record inclusion probabilities and replacements, and state the corpus coverage. If the estimand is an equal-lexeme average over the eligible frame, unequal sampling fractions across bands require corresponding weighting or poststratification.

Keep the purposely chosen quantity nouns as a boundary challenge set. Their selection makes them useful for testing difficult projections, but unsuitable for estimating the ordinary common-noun profile.

I wouldn’t stratify this study on countability. That would require preliminary coding of an outcome and give one diagnostic a special design role. Outcome-related stratification isn’t intrinsically invalid if its probabilities are known, but it adds avoidable complications here.

Two duplication checks need different expectations. Copying the same record shouldn’t create evidence. Sampling additional independent lexemes that happen to have identical profiles can legitimately improve precision and change a decision. An invariant scoring weight doesn’t imply an invariant verdict as information increases.

### Additional categories

I’d include a small verb reference panel once the prospective bank contains meaningful cross-category questions. That addresses the single-outgroup limitation described above.

I’d defer substantial preposition and adverb coding. If subsequently included, draw from the union of relevant source tags—preposition, adverb, particle, and other necessary labels—and retain those tags as sampling metadata. Each rival then maps the same sampled items according to its analysis.

Adding categories also requires new questions for the existing rows. A larger panel evaluated on almost exclusively nominal diagnostics won’t provide the desired comparison.

## 5. The measurement model

### Values and evidence are separate

For graded licensing questions, use an ordinal likelihood for *n*, *m*, and *y*, with estimated ordered thresholds. Don’t assign *m* a fixed numerical midpoint. Binary or categorical facts of form and paradigm should use appropriate separate likelihoods.

The latent predictor should include the proposed shared category effects, lexeme-by-family variation, form and frame deviations, and relevant variety effects. Within-family dependence needs explicit representation. Start with the simplest model that captures these sources, then expand it in response to predictive failures.

Keep epistemic uncertainty separate from marginality. Disagreement between coders doesn’t turn a cell into *m*. A difficult search doesn’t turn it into *n*.

Also distinguish the probability assigned to a cell’s status from the frequency of a construction. A prediction of 0.7 for *y* needn’t mean that 70% of attempted utterances are grammatical. Your cells concern scoped possibility claims, not token frequencies.

For *can* claims, one admissible positive instance can settle availability within the declared scope. Negative conclusions have a different evidential basis. Standardize search effort, retain the strongest attempted counterexample, and record opportunity and evidence type. A corpus absence and an expert rejection shouldn’t become indistinguishable observations.

### Variety and frames

Estimate behaviour within declared variety and register scopes. A broad claim that a use occurs somewhere in the included varieties is possible, but it’s a different target from availability in a particular variety.

Running all variety-sensitive cells once as *y* and once as *n* is a stress test. It doesn’t estimate a population mixture unless weights over varieties have been specified.

Frames developed during exploration can enter the final bank. They shouldn’t also count as untouched confirmation. Withhold related frames together when their shared mechanism would otherwise leak information.

### Coder error

Retain the full provenance distinctions: historical judgment, current judgment, rule-derived fact, model proposal, consensus acceptance, and adjudication. Clarifying a definition doesn’t constitute judging its cells.

A hierarchical confusion model is possible, following the general approach introduced by Dawid and Skene. But three model families don’t identify truth under unrestricted correlated error. Albert and Dodd show why misspecified dependence can bias estimated accuracy even when competing dependence models are difficult to distinguish empirically. [Oxford Academic](https://academic.oup.com/jrsssc/article/28/1/20/6953573?utm_source=chatgpt.com)

I’d therefore use human-audited cells for the primary evaluation and treat model coding as assisted measurement. Audit consensus cells as well as disagreements. A probability-selected audit estimates error over the target; an enriched difficult-cell audit diagnoses failure modes. Report them separately or use their known selection probabilities.

The reported 371/390 is agreement with the 2021 judgments in that selected set. It shouldn’t be transported as a general accuracy rate to new noun or adjective cells. Likewise, the marginal totals of 670 versus 663 *n*s don’t alone establish negligible anchoring: paired changes could cancel. Examine paired transitions and category-by-family differences.

## 6. The simulation study

I’d separate computational validation, identification, and realistic design performance. Gelman and colleagues’ workflow is useful here because simulation and model checking serve several distinct purposes. [sites.stat.columbia.edu](https://sites.stat.columbia.edu/gelman/research/unpublished/Bayesian_Workflow_article.pdf?utm_source=chatgpt.com)

### Before coding new cells

First, establish analytically which observable contrasts distinguish the operational models. Check zero-edge equivalences, root ambiguities, and whether the proposed holdout removes the information needed to estimate a contrast.

Then run clean simulations across broad plausible ranges. These must show that the implementation recovers identifiable, sufficiently strong structure and refrains from decisive conclusions when structures coincide.

Use simulation-based calibration to check the Bayesian computation. That validates inference under the specified model; it doesn’t establish robustness to a misspecified linguistic model. [arxiv.org](https://arxiv.org/abs/1804.06788?utm_source=chatgpt.com)

Only after those checks would I code the measurement pilot. Its role is to estimate plausible error, dependence, and workload ranges. Before bulk coding, rerun the design simulations using those ranges and freeze the confirmatory protocol.

### What realistic generation must include

| Component | Required variation |
|---|---|
| Organization | Each operational rival; zero and weak internal effects; unequal terminal variation; overlapping affiliations; continua; conflicting structures across domains |
| Applicability | True negative outcomes, explicit prerequisites, uncertain prerequisites, and limited observation opportunities |
| Property selection | Prospectively selected banks and banks preferentially selecting each rival’s favourable patterns |
| Dependence | Correlated families, shared prerequisites, exact duplicates, and logical derivatives |
| Lexical units | Multiple forms per lexeme, shared bases, disputed lexeme mappings, and fixed closed-panel identities |
| Measurement | Ordinal responses, variety effects, coder-specific errors, correlated errors, consensus mistakes, and selective adjudication |

The generator must retain the truth appropriate to the whole observed process. If applicability is a linguistic component, include it in the structure being evaluated. If it’s treated as a nuisance observation process, represent that distinction in both generation and fitting.

Apply the entire intended analysis to each dataset: family selection rules, assignments learned from training data, donor conditioning, scoring weights, and the decision rule. The estimator mustn’t receive the simulator’s true masks or memberships.

Morris, White, and Crowther’s ADEMP framework—aims, data-generating mechanisms, estimands, methods, and performance measures—is a suitable organizing template. [arxiv.org](https://arxiv.org/abs/1712.03198?utm_source=chatgpt.com)

### Performance targets

Report correct decisive conclusions, wrong decisive conclusions, unresolved results, and rejection of all candidates separately.

As explicit design choices, I’d aim for:

- Wrong decisive conclusions below about 5% in the registered null and difficult scenarios.
- At least 80–90% correct decisive conclusions for effects judged substantively useful.
- Appropriate uncertainty coverage and frequent abstention near indistinguishable structures.
- Stability across the declared defensible weighting range.

These are targets to assess, not guarantees supplied by Bayesian inference.

Use roughly 200 replications for exploratory screening, then at least 1,000 for the scenarios determining the collection decision. At 90% recovery, 1,000 replications give a Monte Carlo standard error of about 0.0095. The current 30–40 replications are useful for debugging; they provide much less precise recovery estimates.

Vary independent lexemes, property families, and within-family questions separately. Otherwise, an apparent benefit of more columns may simply reflect additional copies of the same mechanism.

## 7. What I’d collect next

I’d begin with a modest measurement pilot after the clean identification checks, followed by a larger collection only if the realistic simulations support it.

Here’s a concrete budget. The verb panel is conditional on constructing useful cross-category questions.

| Stage | New reference lexemes | Property/frame questions | Baseline target cells |
|---|---|---:|---:|
| Measurement pilot | 32 common nouns, 16 proper nouns, 24 adjectives, 16 verbs | 48 across about 24 families | (139 + 88) × 48 = **10,896** |
| Larger planning scenario | 100 common nouns, 32 proper nouns, 48 adjectives, 32 verbs, in total | 72 across about 30 families | (139 + 212) × 72 = **25,272** |

The first allocation permits equal numbers within four frequency bands. The larger allocation is a scenario to evaluate, not a recommendation that these counts have sufficient power.

These counts use one baseline record per new lexeme. Additional form-specific tasks increase the total; conditional questions skipped after prerequisite failures reduce it. Repeated lexeme facts shouldn’t increase it.

Retaining all 18 existing reference forms as a separate challenge panel adds at most 864 pilot cells or 1,296 cells at the larger scale, before accounting for overlap.

Three model-family ratings per baseline cell would mean 32,688 pilot ratings or 75,816 at the larger scale. Those are coding counts, not independent observations.

For the pilot, I’d budget human review of approximately **600 probability-selected cells plus 200 enriched difficult cells**, ideally independently judged by two people before adjudication. That’s 800 audited cells and 1,600 initial human judgments. It’s a budget for learning the error structure, not for estimating a separate confusion matrix for every category and family.

Reserve a prospective set of questions or families for final evaluation after model development. Closed-inventory items can remain the same; their independently assessed behaviour on those tasks supplies the new evidence. If the bank can’t yield enough defensible distinct families, don’t manufacture additional ones to satisfy a numerical column target.

## 8. Conditions under which the matrix won’t settle the question

I’d preregister the following as substantive failure outcomes.

**The theories don’t yield distinguishable predictions without unacceptable additions.** If separation, coordination, and nesting remain compatible with the same observations once their legitimate exceptions are represented, additional cells won’t resolve the taxonomy.

**The apparent distinction depends on arbitrary variance restrictions.** If a winner disappears when terminal variances differ or internal effects approach zero, the original result concerned the imposed covariance signature.

**The coordinate result remains equivalent to a star.** Failure to support the other groupings won’t establish a shared Noun parent.

**Reasonable property targets support different organizations.** That would support domain-relative projectibility. A global taxonomy would require a further argument about why one domain or weighting governs the classification.

**Overlapping or domain-specific models predict better.** The evidence would then favour several intersecting organizations over one inheritance tree for this task.

**The result is carried by duplicated mechanisms or provenance.** A ranking that vanishes after accounting for paradigms, shared bases, coder dependence, or feature-selection history isn’t adequate taxonomic evidence.

**Information plateaus at the family level.** More nouns may estimate profiles more precisely while leaving too few independent mechanisms to distinguish their organization.

**Independent assessment fails to reproduce the advantage.** Successful prediction of historical judgments or model consensus alone is insufficient.

The study’s strongest attainable conclusion would be something like: *Across this declared bank of grammatical tasks, this specified grouping supports additional transferable predictions, beyond lexical, morphological, and constructional dependencies, while these alternative groupings don’t.* That would give your category argument an identifiable empirical contribution. Whether it also warrants the proposed taxonomic nesting should remain an explicit linguistic inference.

## Part 2: adding prepositions or verbs

**Adding either prepositions or verbs can make a previously unidentifiable comparison testable. Adding both gives us a way to check whether the result depends on which reference category we use.** Neither addition guarantees better recovery: that depends on what the columns measure and how the additional categories behave on them.

There are two separate changes to track: what becomes identifiable in the statistical model, and what additional information the actual observations supply.

## 1. One additional category changes the structure of the comparison

At present, the groups are common nouns, proper nouns, pronouns, determinatives, and adjectives. Your coordinate proposal puts the first four under Noun, leaving adjectives as the only outside reference.

In the additive covariance model, after allowing each property its own overall level, these two explanations are indistinguishable:

- The four nominal groups share an additional pattern.
- Adjectives have an additional pattern distinguishing them from everything else.

More adjective lexemes estimate that adjective profile more precisely, but they don’t remove the ambiguity.

Adding verbs gives us two outside reference groups. A pattern shared by common nouns, proper nouns, pronouns, and determinatives can then differ from the independent peculiarities of adjectives and verbs. Adding prepositions instead has the same formal effect.

| Reference categories outside the proposed Noun grouping | What becomes possible |
|---|---|
| Adjectives only | The shared nominal effect remains confounded with adjective-specific variation. |
| Adjectives + verbs | A nominal-versus-outside partition becomes distinguishable from independent variation specific to each reference group. |
| Adjectives + prepositions | The same identification improvement, using a different comparison. |
| Adjectives + verbs + prepositions | Several comparisons can establish whether the inferred partition survives changing the reference groups. |

There’s a qualification to my earlier wording about *identifying nominal cohesion*. What becomes identifiable is a **partition**. A common effect on the nominal side and a complementary common effect on the outside groups can still generate the same relative covariance. Interpreting the partition as a Noun node, with a particular direction of inheritance and taxonomic rank, remains a linguistic inference.

## 2. We can distinguish two questions that the current setup partly conflates

Under the proposed covariance model, we’d like to estimate separately:

1. Does determinative participate in a broader pattern shared with the undisputed noun subcategories?
2. Is there an additional pattern specifically shared by determinative and pronoun?

Adding a second outside reference directly helps with the first question. It doesn’t automatically settle the second.

Here’s a concrete illustration. Let C denote the common-noun profile, D the determinative profile, A the adjective profile, and V the verb profile. These are latent profiles across grammatical properties, after accounting for measurement and the other dependencies.

Consider:

**Cov(C − A, D − V).**

This asks whether properties that distinguish common nouns from adjectives also tend to distinguish determinatives from verbs.

In the simplest additive model, with independent terminal variation, that covariance isolates the broad shared contribution linking C and D. Each category’s own terminal variation drops out because the two contrasts involve four different groups.

We can separately examine:

**Cov(pronoun − common noun, determinative − proper noun).**

That contrast removes the broadly nominal contribution and isolates an additional pronoun–determinative contribution.

The idealized expectations are:

| Operational model | Broad contribution linking determinatives with common nouns | Additional pronoun–determinative contribution |
|---|---|---|
| Separate | Absent | Absent |
| Coordinate | Present, if the Noun node has an observable effect | Absent |
| Nested | Present, if the Noun node has an observable effect | Present, if the intermediate node has an observable effect |

These are expectations of the **specified additive inheritance models**, not consequences of the category labels alone. Zero or very small effects can leave the models indistinguishable.

For the split hypothesis, we’d apply the corresponding predictions to the items assigned to the adjective and nominal branches. We couldn’t treat all determinatives as an indivisible D group while claiming to test whether they divide.

The covariance expressions are illustrations of what the model can estimate. I wouldn’t calculate them directly from arbitrary numerical encodings of the raw *y/m/n/x* cells.

## 3. Prepositions and verbs are formally interchangeable here, but empirically different

The algebra doesn’t privilege verbs over prepositions. Either can provide the second outside reference. Which gives more useful evidence depends on the property bank.

A verb panel might be particularly informative about morphology, complementation, agreement relations, and distribution. A preposition panel might provide useful comparisons involving complementation, modification, independent use, and distribution. Those are possibilities for constructing the bank, not assumptions that all those properties will discriminate the proposed taxonomies.

We should also allow an unexpected outcome: the added category might reveal that a property currently interpreted as nominal is more widely distributed. That would weaken its support for a nominal grouping. The value of adding categories includes exposing that possibility.

For prepositions, the sampling boundary needs care. We shouldn’t let a traditional tagger exclude items merely because it calls them adverbs, particles, or conjunctions. We can use a broad union of source labels to obtain candidates, retain the source labels as metadata, and let the operational analyses assign the same items their categories.

Adding both categories supplies a useful robustness test. For a given pair of nominal groups, we can compare their relationship using:

- adjectives and verbs as the outside references;
- adjectives and prepositions;
- verbs and prepositions.

If these comparisons support the same partition, it’s less likely that the result is being driven by one peculiar reference category. If they disagree, that’s evidence that a single tree may fit poorly, or that the inferred organization depends on the grammatical domain.

It’s still not three independent replications: the comparisons share observations and property families.

## 4. The columns determine whether the new categories supply useful information

We shouldn’t require prepositions or verbs to vary on every property. **A reliable *n* can be informative.** If an independently justified operation is available to nominal items and unavailable to verbs, that contributes evidence about their distribution.

The problems arise when:

- questions are undefined for the added items but their *x*s are converted to *n*s;
- several negative answers follow from one prerequisite failure and are counted independently;
- the bank was selected to describe nominal behaviour, but the resulting contrast is generalized to grammatical properties overall.

For example, a verb’s inability to occur in a particular nominal function might explain a whole set of subsequent failures involving dependents in that function. Those failures don’t constitute a corresponding number of independent reasons to place the verb outside Noun.

Conversely, simply appending verb-specific diagnostics won’t necessarily help distinguish the determinative analyses. If every nominal group receives the same answer on those diagnostics, they may establish that verbs differ while contributing little to the placement of determinatives among the nominal candidates.

We need a bank that contains **several independently motivated mechanisms whose distributions bear on the relationships under investigation**. It needn’t make every question equally informative about every category.

## 5. Adding categories also changes fitting and scoring

In the fitted model, prepositions and verbs would receive their own estimated profiles and terminal variation. They shouldn’t inherit the old simulation’s requirement that every edge contribute the same variance.

In the family-transfer evaluation, they’d join the donor panel. We’d observe their behaviour on the withheld family, along with the other reference items, before predicting that family’s behaviour for the determinative targets.

The primary score should stay on the **same target items and questions** when we ask whether the additions help. Otherwise, a large number of easily predicted verb cells could improve the overall score without improving our predictions about determinatives.

I’d therefore distinguish:

- improvement in predicting the original targets after adding reference observations;
- improvement from introducing additional property families;
- performance on the expanded inventory as a whole.

Those are all legitimate outcomes, but they answer different questions.

## 6. The existing outgroup simulation doesn’t settle this

There’s already an [outgroup simulation in the repository](https://github.com/BrettRey/determinatives-as-nouns/blob/d967c4b164e334cb199657b115322b38a6469442/analysis/tree-recovery-sim/outgroups.py). In its masked conditions, [the reported results select the nested model throughout](https://github.com/BrettRey/determinatives-as-nouns/blob/d967c4b164e334cb199657b115322b38a6469442/analysis/tree-recovery-sim/OUTGROUPS.md), including after adding categories.

That doesn’t establish that prepositions or verbs are unhelpful. The script assumes that verbs are all-negative on 85% of the original columns and gives prepositions the adjective all-negative rate of 62%. It then overwrites simulated observations with zeros. These are imposed observation patterns, not measured verb or preposition profiles. It also adds prepositions and adverbs together, and introduces verbs only alongside both, so it doesn’t isolate the alternatives in your question.

The appropriate comparison would use four panels—current, plus prepositions, plus verbs, plus both—under both the existing bank and a prospectively broadened bank. It should retain the same determinative evaluation targets, allow unequal terminal variation, model prerequisites explicitly, and include unresolved outcomes.

**I’d include at least one additional reference category in the next pilot, and compare small verb and preposition panels at matched coding budgets.** One can remove the single-reference identification limitation; both can show whether the inferred grouping survives a change of reference. We can establish that structural benefit now. We can’t yet say which addition will produce the greater predictive gain, or whether either will favour your coordinate analysis.
