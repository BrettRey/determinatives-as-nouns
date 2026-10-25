# Designing the category test: an outside-model response

**Superseded in part, 24 Oct 2026 (later):** Brett corrected the prompt (the 2021 search was exhaustive within pronouns and determinatives, not contrast-seeking), and Claude Opus 5.5's triage of this memo against GPT Pro's design (`notes/2026-10-24-category-test-design-triage.md`) established that with adjectives the only outside category the coordinate analysis cannot be positively supported in a covariance framework. See `notes/2026-10-24-category-test-design-muse-addendum.md` for what falls, what stands, and the re-checked algebra. Column counts below predate the word-part restoration in fe3d5ad (now 190 columns, 50 base).

Prepared by Muse Code powered by muse-wonder-full-1.0, in response to `notes/2026-10-24-prompt-for-outside-models.md`. It is a fresh design, not a repair of the 24 October attempt, though it uses that day's findings as constraints. Files read in full unless noted: `planning/codebook.md`, `planning/evidence-ledger.md`, `notes/nesting-tests-2026-10-24.md`, `analysis/tree-recovery-sim/` (`simulate.py`, `real_patterns.py`, and the four result files), `analysis/node-reach-2026-10-24/README.md`, `analysis/noun-sample/draw_sample.py`, plus counts taken directly from `analysis/codebook/forms.csv` (157 rows), `analysis/codebook/columns.csv` (159 columns), and `analysis/matrix-2026-10/matrix-2026-10.csv` (139 rows). Counts quoted below were recomputed, not copied. Method names are given without full references where my memory of the reference is not certain, and each such case is marked. Nothing here codes a new cell.

## Verdict in brief

The single most important finding is this. No test run on the present column set can settle nesting against coordination, however many nouns are added, because the columns were selected in a way that manufactures the nested answer. That is not a caution about power. It is a statement about identification. The 2021 columns exist because they distinguish pronouns from determinatives, so any method that treats them as if sampled will overcount properties on which pronouns and determinatives pattern together against nouns and adjectives, and will find a pronoun-and-determinative node whether or not one earns its keep. The second simulation round shows exactly that, picking the nested tree 97 to 100 times in 100 whatever tree generated the data.

It follows that the next investment is columns, not rows, and a column frame defined before any new cell is judged. Rows matter second, and the model third. With a pre-registered property frame, a lexeme-level held-out test, and a competitor set that includes flat structure and multiple inheritance beside the four named rivals, the question is answerable in a conditional sense I define below. Without the new frame, the honest result is whichever structure the argument from shared generalisations, already in the evidence ledger, supports. The matrix then illustrates. It does not adjudicate.

A second finding qualifies the first simulation round. The competitor set in `simulate.py` contains only three trees, coordinate, nested, and separate. The split analysis and multiple inheritance, two of the structures the memo must weigh, were never generated or fitted. A test that has never seen those structures in simulation cannot be trusted to reject them in data. Any credible design must generate data under them, and under no tree at all, before it touches a real cell.

## 1. The overall approach

### What a category claim predicts

Start from what the rivals disagree about. Each says that some generalisations can be stated once, at some node, instead of twice, at two leaves. Hudson's nesting says that properties of pronouns and determinatives can be stated at an intermediate node inside Noun. Coordination says they must be stated at pronoun and at determinative separately, or at Noun itself. *CGEL*'s separate category says that determinative properties cannot be stated at Noun at all. The split says that one part of the determinative inventory shares its statements with adjectives and the rest with nouns.

So the empirical content of a node is predictive compression. Knowing only that a new lexeme sits under a node should let you predict its properties better than knowing only its parent above that node, by more than chance and by more than function alone predicts. That is Hudson's own criterion, quoted in the ledger, that a category must earn its place by doing work in the grammar. Stated this way, the contest is among statements of generalisation, not among labels.

The design below therefore scores each structure by how well it predicts held-out lexemes and held-out property families, and reports support node by node rather than declaring one winning tree.

That reframing has a consequence the first attempt missed. There are three separable questions, not one four-way choice. First, does Noun including determinatives earn its keep against a separate determinative category? Second, given that it does, does an intermediate pronoun-and-determinative node earn its keep against coordination? Third, is the determinative inventory homogeneous enough for either answer to cover it, or does it split, or cross-classify? A single winner among four trees conflates the three. The primary output should be the estimated predictive gain, with uncertainty, for each disputed node and each disputed placement, under each defensible weighting. A reader who accepts the first node but not the second has learned something. A forced choice hides it.

### The unit problem, and atoms

Neither rows nor columns in the present matrix are the units the rivals classify. The rivals classify lexemes. The matrix rows are forms, and on inspection not only forms. `forms.csv` separates paradigm forms (*he*, *him*), readings of one form (*they*, of one person, against *they*, of several; *their*, singular, against *their*, plural), uses of one form (*her*, as in *I saw her*, against *her*, as in *her book*; *which*, interrogative, against *which*, relative), and multiword rows (*a few*, *a great many*, *many a*, *each other*).

Each split is defensible for coding, and `planning/codebook.md` section 1 defends form rows well. But a split by use or by reading builds part of the answer into the row definition, since *her* in determiner function and *her* in head function are separated before any property is coded. A split by reading makes rows differ by definition on the number columns. Treating all 139 closed rows as independent evidence overstates the sample several times over.

The design therefore introduces one neutral unit below every rival's leaves. Call it the holdout cluster. A holdout cluster groups every row that shares a lexeme or a productive base, so *some*, *someone*, *somebody*, *something*, and *somewhere* sit in related clusters linked by the *some* base, and the whole personal paradigm for one person and number sits in one. The exact clustering is fixed from morphology alone, before results are seen, and published with the design.

Every rival assigns each whole cluster to a leaf. No cluster is split across the training and held-out sides, and no rival gets to define the clusters. This generalises the codebook's three group tests in section 9, whole-group holdout, disputed forms, and subgroups, into one scheme. Disputed clusters, the compounds under Hudson, the gradable four under the split, are ordinary clusters whose assigned leaf differs by rival. Holding them out is then the sharpest test, not a special case needing its own machinery.

Two inventory decisions need stating beside this, since completeness is claimed for the closed classes. First, the cardinal part of the inventory is a sample, *one*, *two*, *three*, and *zero*, from an open numeral system. Numerals should be treated as a sampled stratum in scoring, or set aside as deferred, as the ledger already defers their placement. Counting them as a complete inventory while sampling nouns mixes two designs. Second, boundary rows such as *today* and *there* among pronouns, and *once*, *twice*, *last*, *next*, and the *where* compounds among determinatives, reflect one analysis of the inventory edge.

The analysis runs with boundary rows in and out, as it already runs the quantity nouns in and out. Neither point is a criticism of the 2021 choices. Both affect what a count over 73 determinatives means.

### The primary method

Recommend one primary method. Fit one hierarchical model family in which each rival structure, plus flat structure, plus multiple inheritance, is a different prior covariance over holdout clusters. Each property then has a cluster-level tendency, clusters under a shared node tend alike, and the size of that tendency at each node is estimated from the data rather than fixed. Compare structures by expected log predictive density for held-out clusters and held-out property families, using a proper scoring rule, and report stacking weights and node-wise gains with standard errors, not only a winner.

Stacking, in the sense of weighting rival predictive distributions so their combination predicts best, suits this problem because the truth is likely none of the named trees, as the four-gamete conflicts already suggest. I am confident stacking and leave-one-out predictive comparison are standard in the Bayesian workflow literature the project already cites, Gelman and colleagues 2020. I am less certain of exact references for stacking weights and would verify Yao and colleagues before citing by year.

Multiple inheritance enters this family without new machinery. A cluster that inherits from two parents, as the compounds might from pronoun and from determinative, has its tendency drawn toward both, in proportions the model estimates or the analysis fixes in advance and varies. That yields a direct estimate of the desk count's suggestion in `analysis/node-reach-2026-10-24/`, that pronoun-like properties reach only 21 of 73 determinative forms in four small subgroups. If those subgroups carry a second inheritance and the rest of the inventory does not, neither pure nesting nor pure coordination is right, and the paper should say so. A design that forces a tree cannot discover that. It can only misreport it as weak support for one tree.

The flat competitor matters as much. Under flat structure, clusters share only a root, and any resemblance among them is functional or accidental. If no tree beats flat structure out of sample, no node earns its keep on this property set, and that is a publishable answer about the limits of distributional evidence. Equally, a saturated competitor, in which each cluster's profile is free, bounds how much prediction any structure could achieve. The gap between a tree and the saturated fit measures structure left unexplained. The gap between a tree and flat structure measures structure earned.

Scoring needs two holdouts, crossed. Holding out clusters tests whether a node predicts a new lexeme's known properties, which is where the rivals differ. Holding out whole property families, the super-columns, tests whether a node predicts a known lexeme's new properties, which is what stating a generalisation once promises. The hard test holds out one cluster and one family together, so the model must predict an unseen lexeme on an unseen mechanism from node membership alone.

Leave-one-form-out, which the evidence already shows cannot separate the trees, stays only as a calibration check that within-cluster fit is sane. Reporting all four tells the reader which kind of generalisation, if any, the node buys.

What this assumes should be plain. It assumes that resemblance in coded possibilities tracks shared grammatical statement, that the property frame defined in section 2 represents the population of statements the paper cares about, and that coder error can be modelled well enough that it does not mimic structure. It does not assume descent, independent characters, a single true tree, or that distance in this space is category membership. It estimates predictive compression relative to a stated property population. That conditionality is the price of honesty, and the paper should carry it in its claims.

### Why not the alternatives as primary

Each alternative named in the prompt has a use, and each fails as the primary test for a statable reason. Phylogenetic comparative methods contribute the discipline of section 1 of `notes/nesting-tests-2026-10-24.md`, group only on shared properties absent elsewhere, and count conflict rather than explaining it away. But grammatical properties do not descend on a tree, polarity, which state counts as derived, has no outgroup justification independent of the grammars under test, and convergence through shared function, partitives after quantity words of several categories, is ordinary grammar rather than noise. Borrow the descriptive table and the conflict count. Do not borrow the inference.

Latent-class and mixture models discover clusters. They do not test named structures, their classes need not correspond to any rival's categories, and with five or six leaves and strong column correlation their solutions are typically unstable under restarts, as the 2021 clustering audit already found. Item-response models assume that items measure a small number of latent traits, usually one, on which forms sit. Category membership is not a trait amount, and a form is not more or less nominal in the sense such a model needs, whatever the rhetoric of typicality. A multifactor version could describe property correlation usefully, as part of the column model below. It cannot adjudicate nodes.

Estimating a distance matrix among groups and comparing it with each tree's implied distances throws away cell-level uncertainty, coder disagreement, and the difference between a property that cannot arise and one that never does. It also double counts correlated columns, since one mechanism spread over five columns moves the distance five times. As a descriptive figure, with uncertainty from the fitted model projected into distances, it is valuable. As the test, it discards exactly the information that decides this question.

Bayesian model comparison by marginal likelihood over the same structures is legitimate, and close in spirit to the recommendation. Its weakness here is prior sensitivity. With few clusters at the disputed nodes, the marginal likelihood can turn on the prior for node spread more than on the data. Held-out predictive scoring is less sensitive in that way and matches the earn-its-keep criterion directly, so it leads. Report a Bayes factor as a sensitivity, with priors varied, if a reviewer asks.

## 2. The columns

### The population a column set must represent

There is no sampling frame of grammatical properties in nature. Anyone who claims to sample properties at random has smuggled the frame in. The remedy is not to pretend otherwise. It is to construct the frame openly, before coding, from sources no rival controls, and to state every conclusion as relative to that frame. I propose three sources, crossed. First, the diagnostic lists *CGEL* itself gives for nouns in chapter 5 and adjectives in chapter 6, already partly harvested, taken whole rather than cherry-picked, including the negative properties.

Second, a systematic grid built from functions and dependents, so that each combination of a function a form might bear, head, determiner, modifier, complement, and a dependent type it might take or license generates a candidate column whether or not anyone expects it to vary. Third, the semantic and morphological dimensions the codebook already names, quantification, definiteness, deixis, gender, number, case, grade, again taken in full sets rather than by single promising members.

Each candidate column gets design metadata before any form is coded on it. The metadata records its source, its domain, its frame, and its scope condition, meaning what a form must be able to do for the question to arise at all. Columns are then included by a stated rule over the metadata alone, stratified by source and domain so that no chapter and no domain dominates, with the stratum sizes fixed in advance. A column that turns out constant still counts, and counts against whatever structure predicted variation.

That is what sampling buys. It converts absence of a noun-only property from an accident of never having looked into evidence, because the design looked in the places such properties would live, in the noun chapter's own diagnostics.

The legacy columns cannot be repaired into this frame by weighting. Their selection rule is known in outline, chosen in 2021 to distinguish pronouns from determinatives, then added to for good local reasons. Weighting corrects selection only when the selection probability given the column's pattern is known. Here it is not, and no analysis of the observed columns can recover it, since the columns that were never considered left no trace. The legacy set therefore becomes an exploratory arm, reported in full, with a tipping-point sensitivity that asks how strongly column choice would have to favour pronoun-and-determinative patterns to produce the observed result under coordination.

The confirmatory arm runs on the new frame. If the two arms agree, the paper is strong. If they disagree, the confirmatory arm governs and the disagreement itself documents the selection effect. That division must be declared before the new columns are coded, or it is just another fork chosen after seeing answers.

### Properties that cannot vary for a whole category

The codebook's distinction between n, never, and x, cannot arise, is the right foundation, and the design builds on it rather than collapsing it. Model every column in two layers. The first layer is applicability, whether the scope condition is met for this cluster, coded from the column definition and one or two presupposed abilities, not from the y and n pattern itself. The second layer is the value given applicability. An x is data in the first layer and absent in the second.

A category that is n throughout on an applicable column shares a negative generalisation, which is evidence of the ordinary kind. A category that is x throughout shares the absence of a presupposition, which is evidence about that presupposition, stated once at whatever node governs it, and not again at every column that presupposes it.

This matters for the counts that decided the second simulation round. On the 77 columns with coded noun and adjective rows, 22 have no category constant at n, 11 vary only among pronouns and determinatives, and none varies only among common and proper nouns. Two details in how that count was produced deserve recording, since the design must not inherit them. In `real_patterns.py`, coder x values for nouns and adjectives were recoded to n before patterns were counted, and proper nouns were given the common nouns' pattern outright, there being only two proper noun rows.

Both choices are understandable in a quick simulation. Both inflate the very pattern under study, by counting inapplicability as shared absence and by assuming the two noun subcategories agree. The confirmatory analysis keeps x distinct and codes proper nouns on their own rows.

When, then, is a pronoun-and-determinative-only property evidence for a shared node? Under three conditions, all checkable. The property is applicable to the other categories, so their n is a finding rather than a presupposition failure. The column reached the set by the pre-registered rule, not because it showed that pattern. And the property is not one face of a mechanism already counted, in the sense defined next. Interrogative and relative members shared by *which* and *who* forms, carried gender contrasts, and the dependent and independent alternation in *no* and *none* against *my* and *mine* are the ledger's candidates.

Each may well pass. What they cannot do is pass on the strength of a column set assembled by looking for pronoun and determinative behaviour. Shared absence needs the same scrutiny as shared presence, by the way. Two categories that both fail to take some complement may share a node, or may fail for unrelated reasons, one for want of the function and one by lexical restriction. The applicability layer is what separates those cases, imperfectly but explicitly.

### Correlated columns and the unit of counting

The 159 columns in `columns.csv` comprise 102 possibility claims, 19 base columns, 13 facts of form, 8 facts of the lexeme, 10 superseded, 3 derived, 2 universal claims awaiting reversal, 1 analysis label, and 1 unclear. They sit in 31 super-columns, of which the largest, base, holds 19 columns and records which morphological base a compound contains. Three decisions follow. Derived and superseded columns and the analysis label stay out of scoring, as the codebook already provides.

Base columns stay out of the primary arm too, and run as a stated sensitivity, since grouping compounds by construction and then discovering that compounds resemble each other proves nothing about category. Form and lexeme facts enter at their own level, once per form or once per lexeme, never replicated across a paradigm. These are the codebook's positions, adopted.

One mechanism behind several columns is the central counting problem, and super-columns are necessary but not sufficient. Gradability surfaces as grade inflection, comparative complements, and degree modification, three super-columns by the present grouping, one mechanism for counting purposes. The design adds a mechanism grouping above the super-column, fixed in advance on grammatical grounds and published, and then does two things with it. In the model, columns are pooled within super-columns and super-columns within mechanisms, with the correlation that remains across mechanisms carried by a small number of column factors if the fit supports them.

In scoring, the headline number is the mean over mechanisms of the within-mechanism mean score, so a mechanism with nine columns and a mechanism with two each cast one vote. The analysis also reports the effective number of independent properties, a standard summary of how much independent information a correlated set carries. I am confident such summaries exist in several forms, from eigenvalue-based counts in genetics onward, but I would not cite a source from memory.

If the effective count is near the number of mechanisms, roughly thirty at present, then claims calibrated on a hundred columns are miscalibrated however the cells come out, and the sample-size reasoning in section 3 follows the mechanism count.

Frames multiply columns without multiplying mechanisms, so frame splits are repeated measures of one property, not new votes. A determiner taken in an argument NP, in a predicative, and in the set-denoting use is one mechanism observed under three conditions. That is an argument for modelling frame as a within-property effect with its own interactions, and against letting a heavily split property outvote an unsplit one. It is also why the frame list must be frozen before judging, as the codebook requires. A frame proposed after seeing that it separates two groups is a column selected on its outcome, back at the original sin.

Two kinds of control column complete the design. Negative controls are columns no grammatical mechanism should organise by category, such as the shape columns recording initial sounds. If a tree predicts held-out clusters on shape columns as well as on grammatical ones, the signal is morphological or historical resemblance leaking through the clusters, and the grammatical result is suspect. Positive controls are columns where the structure is not in doubt, plural inflection across noun subcategories, say.

A method that cannot find structure there cannot be trusted where structure is disputed. Controls cost little, since most already exist, and they convert a methods argument into an observation.

## 3. The rows

### What sampling buys, and what it cannot

The closed inventories carry no sampling error, given the inventory decisions noted in section 1. The open classes are samples from populations so large that the sample, not the population, sets the precision of every noun and adjective profile. The first simulation round showed the asymmetry this creates. At the current 10 common-noun forms, 2 proper nouns, and 6 adjectives in `forms.csv`, the model-based group test recovered the coordinate tree in only about a third of datasets generated under it, while recovering the nested and separate trees almost always.

Noisy noun-side profiles make determinatives look closer to the precisely measured pronouns. That bias is a property of the verdict, not of any single estimate, which is why unbiased estimates did not prevent it on 24 October.

The sampling unit must be the lexeme, with all its paradigm forms coded as rows beneath it, singular and plural for common nouns, plain and graded forms where they exist for adjectives. Sampling forms directly would sample plural forms of frequent nouns and singular forms of rare ones in proportions no population justifies, and would split paradigms across any later holdout. The order already drawn in `analysis/noun-sample/frame-order.csv` samples lemmas, which is right, and its rule that any prefix of a stratum's random order is itself a random sample is exactly what a simulation-set size needs.

Keep the draw, the seed, and the file. Change what gets coded per draw, the whole paradigm as found in the frame, and the status of replacements, as follows.

### Frame, strata, and replacements

SUBTLEX-UK dominant part of speech is a defensible frame if it is treated as a frame, a way of listing candidate lexemes, and not as a classification the design endorses. The estimand then reads, lexemes whose dominant corpus use is nominal, adjectival, or name-like, at Zipf 2 and above. That is a population a reader can picture. Frequency band is a proper stratum, known for every unit before coding, and the band belongs in the model, as the draw script already argues from design principles.

Nothing that is itself a coded property, or a close cousin of one, may stratify the sample. Countability is the named example from 24 October. Animacy, concreteness, and gradability raise the same problem in milder form, since each correlates with columns in the set. If the paper wants statements about count and non-count nouns separately, it gets them by modelling the coded property, not by sampling on it.

Replacements need tightening. The present rule replaces a drawn lemma that is not a noun in its dominant use, judged a tagging error. Whoever judges that imports a classification into the frame, the very move the design exists to avoid, and imports it invisibly if only the replacement is logged. Replace instead only on mechanical grounds statable without a category decision, not an English lexeme, a duplicate of a lexeme already drawn, a spelling variant of one, or no codable use at all.

Log every replacement with its reason, keep the replaced items in a file, and run one sensitivity in which borderline replaced items re-enter as unassigned clusters the model places by their properties. The top of the present order shows why this matters. The highest proper-noun draws in the top band are *english*, *hi*, and *nick* in lower case, and the top adjective draw is *biggest*, a graded form standing as its own lemma. A design that quietly swaps such draws for cleaner ones reports precision it did not earn.

A design that codes them, or replaces them on stated mechanical grounds, reports the frame it actually used. I flag that I have not checked what uses underlie those three name entries in SUBTLEX-UK, and the point stands either way, since the rule, not the items, is at issue.

Proper nouns deserve a sentence of their own, because the name stratum of a subtitle corpus overrepresents people and places that get talked about, in forms that take plurals and articles in headline-like ways rarely true of names at large. The design accepts that limit in the estimand wording, frequent proper nouns, and adds one safeguard that does not select on grammar. Person, place, and other name types are recorded from an external gazetteer or name list where one exists, as design metadata gathered before coding, and reported as a breakdown of the sample.

If one type dominates, the paper says its proper-noun claims concern mostly that type. What it must not do is hand-pick names of each type to balance the sample by judgment, since that reintroduces selection by the analyst. The two present rows, *Kim* and *Toronto*, stay as anchors outside the sample, like *dog* and *water*.

### How many, and which other categories

Size follows from the simulation gate in section 5, and any number offered now is a planning figure to be confirmed there. The reasoning runs as follows. What needs precision is each leaf's profile averaged over mechanisms, because that is what node prediction uses. With binary possibilities, one property in one leaf is estimated to within about 20 points at 24 lexemes, 15 at 40, 12 at 64, and 10 at 100, at the worst case.

Averaged over some thirty mechanisms, if they were independent, those widths shrink fivefold. They are not independent, so the truth lies between. On that basis, and on the recovery figures already in hand, plan to code 80 common-noun lexemes, 32 proper-noun lexemes, and 48 adjective lexemes, drawn down the existing random orders in proportion to band size, with the gate free to demand the large arm, 100, 48, and 64, or to accept the pilot arm, 40, 16, and 24, with wider intervals honestly reported.

The seven quantity noun forms and the other reference rows remain a labelled boundary set, run in and out, never pooled into the noun profile. A set chosen for sitting near the determinatives would pull the noun leaf toward them by construction, which is selection on the outcome at the row level.

Adjectives stay as the one outgroup in the primary test, because the split analysis cannot be tested without them and because they share enough NP-internal territory for many columns to apply. Prepositions, adverbs, and verbs stay out of the primary test. The reason is not that their boundaries are disputed, though the note in the decision log about traditional taggers filing *away*, *abroad*, and *downstairs* as adverbs shows they are. The reason is that including them changes the question.

A test over the whole lexicon needs a property frame that describes verbs as richly as nouns, at which point the determinative question is one contrast among hundreds and the design is a different and much larger project. On the present columns those categories would be n or x throughout, and the second simulation round's withdrawn outgroup run shows what happens when a simulation pretends otherwise. If polarity for a shared-derived argument is ever needed, a small preposition set, defined by a stated rule over a published list and coded on a handful of named columns, can serve that narrow purpose in the supplement. It cannot rescue the main test, and section 7 says what follows if the paper needs rescuing there.

One row-level check from the codebook should be kept and strengthened. Duplicating the noun rows tenfold must not move the verdict. In the present design the check is sharper, duplicating whole lexemes, and splitting one paradigm's forms across folds, must both leave the node-wise gains inside their original intervals. A method that fails either check is counting copies, not evidence, and its results do not get read.

## 4. The model

### Values, frames, and variety

The y, m, n scale mixes two claims, as the codebook's revision already recognised by reserving m for degradation alone. Possibility is the paper's currency. A form either can occur in the frame, and one admissible instance settles it, or the claim is that it never does. Degradation says something real but different, that speakers find the admitted use poor, and its boundary moves with search effort and coder temperament in ways possibility does not.

The primary analysis is therefore binary at the possibility layer, y and m together against n, with degradation modelled second, as the chance that a possible use is degraded, and reported as its own result. The ordinal analysis, n below m below y, and the strict analysis, m with n, run as named sensitivities. That ordering matters. The arm least movable by uneven search effort, the m-as-y arm the codebook already singles out, should be the headline, since the determinatives have been searched harder than the nouns for a companion paper and every extra m found there flatters the structures that group them with whatever they marginally resemble.

Frames enter as conditions on the possibility claim, with the frozen frame list treated as repeated measures within a property, as section 2 set out. Two frames need explicit handling because they carry argument in the ledger. The set-denoting use runs in and out in full, not as a value tweak, since whether *a he or a she* and *a special someone* are the same lexeme at work is one of the paper's claims rather than a coding premise.

The echo-question frame likewise runs as its own condition. If a node's support depends on either inclusion, the paper has learned that the node rests on a construction, and should say which and argue it on linguistic grounds, with the matrix in support rather than in charge.

Variety needs a target before it needs a rule. I propose the primary estimand be possibility in at least one major standard variety of English, with the variety recorded per cell as now, and two sensitivities, possibility in the analyst's own variety, and possibility in every recorded variety, which will mostly be uninformative. What the design must avoid is an estimand that grows with effort, where a form becomes y because someone looked in one more variety for it than for its neighbours. The adversarial search protocol, applied evenly, is the safeguard, and the variety field is what makes unevenness auditable after the fact.

### Lexemes, bases, and disputed forms

Lexeme and base structure enter as crossed grouping factors. A form's tendency on a property draws on its lexeme, its lexeme draws on its assigned leaf and any second inheritance, and compound bases contribute their own grouped effect where the design holds base clusters out whole. Facts of the lexeme, that a paradigm has a genitive form, enter the likelihood once per lexeme. Facts of form enter once per form. Nothing enters once per paradigm mate.

This is the model counterpart of the holdout clusters in section 1, and the two must agree, since a model that pools by lexeme while the holdout splits a paradigm leaks exactly the information the holdout exists to withhold.

Disputed forms need no special value. They are clusters whose leaf assignment differs across competitors, and each competitor is scored on them under its own assignment, having been fitted without them. Two further sensitivities cover genuine doubt about the coding unit itself. Collapsing use-split rows, *her* dependent and independent into one lexeme observed in two function conditions, tests whether row construction drives the result. Collapsing reading-split rows, singular and plural *they*, tests the same for number.

If a node's gain survives both collapses, row construction is not its source. If it does not, the paper's claim is about uses, not categories, and needs restating before it needs more data.

### Who coded what, and coder error

Treat every value, the 2021 judgments included, as a noisy observation of a latent possibility, with error rates that differ by value, by coder, and by property family. The asymmetry is structural. A false y needs a mistaken instance, a coercion or a different lexeme let through. A false n needs only an incomplete search. So the model estimates, for each coder family and for the 2021 record, the chance of reporting each value given each latent value, pooled over mechanisms, using the cells where coders overlap and the cells Brett judges.

This is the standard latent-truth approach to multiple imperfect raters. I am confident it descends from Dawid and Skene's 1979 model, but I have not verified that reference for this memo and it should be checked before citation. Agreement-based acceptance then changes character. Unanimous cells are very probably right, 371 in 390 against the 2021 record in wave 2, itself an upper bound for reasons the codebook gives. In the model they are not certain, and their small residual error, concentrated presumably in false n, is estimated rather than assumed away.

That estimation needs a gold sample drawn for the purpose, and the design should adopt the seeded random gold sample the codebook's fork 7 already borrows from the diagnostic-validity project. Draw cells at random, stratified by design stratum and mechanism, before coder proposals are seen for them, and have Brett judge that sample blind to the proposals. A sample near 400 cells estimates a 10 percent error rate to within about 3 points, and, more to the purpose, estimates it separately for y and n proposals and for each leaf's rows, which is where differential error would mimic structure.

Every other cell Brett judges in the ordinary flow still counts. The gold sample's job is to be unselected, so that error measured on it transports to the cells nobody hand-picked. Contested cells, where coders split or Brett's ruling went against a proposal, carry their disagreement into the model as posterior uncertainty over the latent value, and one sensitivity drops contested cells entirely. A node whose support lives in contested cells is a finding about coders.

Two calibration results from 24 October should be built into expectations. Showing coders the 2021 value as a claim made no detectable difference on 1,153 identical cells, 670 n values against 663, which licenses pooling those passes with a coder-pass effect in the model rather than discarding them. Two runs of one model disagreed on about 15 percent of contested cells, which sets a floor under single-coder reliability and argues for keeping coder identity in the data rather than majority-voting it away before analysis.

Search effort belongs in the data too, at least as a record per cell of what supports an n, on the codebook's existing scale from a *CGEL* statement down to two coder families finding no y. In the model that record predicts false-n risk. In the report it lets a reader see whether the nodes rest on strong n values or on absence of looking.

## 5. A simulation plan

### What the existing simulations establish, and what they cannot

The two rounds in `analysis/tree-recovery-sim/` established three things solidly. Leave-one-form-out cannot separate the trees. A held-out group predicted from the plain mean of its siblings favours whichever tree gives it more siblings, and the covariance-based predictor removes that mechanical bias. And the real columns' applicability pattern, copied into simulated data, makes that same predictor choose the nested tree almost always, whatever generated the data, while filtering to columns that apply everywhere removes the bias at the cost of keeping only about 22 real columns, far below the roughly 115 at which recovery reached nine in ten. Those results stand, and the design above accepts them as constraints.

What the rounds cannot establish is that any estimator will behave on real data, because generator and estimator share a model family, as the prompt notes. Reading `simulate.py` makes the gap concrete, and the new plan is built to close each item on this list. Columns are independent given node effects, so no mechanism ever produces a block of correlated columns, though the real codebook groups columns into 31 super-columns precisely because they do. Cells vary independently within a form, so no lexeme, paradigm, or base structure exists to leak or to pool over.

Every category can vary on every column in the first round, and in the second, inapplicability is imposed by forcing cells to n, which conflates the two layers the analysis must separate. Coder error does not exist, so unanimity and adjudication never arise. Column selection does not exist, so the one process known to have shaped the real columns is absent. The competitor set omits the split and multiple inheritance entirely. And the calibration target itself, four summaries of the pronoun and determinative cells, is matched only loosely, with the chosen parameters putting an effect at every node in every column, which flatters structured models against flat ones.

None of this invalidates the three findings above. All of it means recovery rates from that code are upper bounds under friendly conditions, exactly as its authors record.

### Generators that break the model's assumptions

The new simulation generates data under at least eight structures. The three trees already present. The split, with the gradable clusters assigned to adjectives and the rest nominal. Multiple inheritance, with the four pronoun-like subgroups from the desk count drawing on a second parent in varying strength, including zero, so the design must detect its absence as well as its presence. Flat structure, with no node below the root earning anything. Functional resemblance without category, in which clusters that share a function, occurring as determiner, say, or heading a partitive, resemble each other whatever their category, because that is the standing alternative explanation for every shared property in this debate.

And a gradient structure, in which resemblance falls off with an underlying distance that no tree represents, included so the method can be seen failing gracefully, by spreading weight across structures, rather than confidently choosing a wrong tree.

Realistic, for this problem, has to include six further ingredients, each varied over a plausible range rather than fixed at a friendly value. First, correlated columns, generated by mechanisms, so that one latent mechanism switches a block of columns together within a leaf, with block sizes and strengths bracketing what the super-column groupings suggest. Second, a two-layer applicability process, in which a column first requires a presupposed ability, itself varying by cluster and only imperfectly observed, and takes a value only where the ability holds, with x recorded noisily as coders will record it.

Third, column selection mimicking the legacy process, in which candidate columns enter the legacy arm with probability rising in how well they separate pronouns from determinatives, at strengths from none to strong, so the tipping-point sensitivity can be calibrated against known selection. Fourth, lexeme and paradigm structure, forms within a lexeme sharing most of their tendencies and compounds sharing base effects, with row splits by use and by reading reproduced as in the real table.

Fifth, coder error, asymmetric between false y and false n, differing across three simulated coder families, with an adjudicator who is better but not perfect, and with search effort higher for determinative rows in some scenarios. Sixth, sampling of open-class lexemes down a frequency-stratified order, with the boundary quantity set available to be wrongly pooled, so that the cost of pooling it can be measured rather than asserted.

Every estimator step that will touch real data runs inside the simulation loop, in the same order, with the same rules. That includes the mechanism-balanced scoring, any filtering to generally applicable columns if that arm is kept, the acceptance rule for unanimous cells, and the gold-sample correction. A filtering step applied in analysis but not in simulation invalidates the gate, since filtering on an observed pattern is itself an estimator with its own bias, as the general-only round's weak recovery at realistic column counts, 37 to 67 percent at about 21 kept columns, already hints.

### The gate: what must be shown before real coding

Fix the decision rule and its thresholds now, while nothing rides on them. I propose the gate have four clauses, all to pass at the planned sample and column sizes before the confirmatory wave is coded. Under flat structure and under functional resemblance, the procedure declares a node earned, by the pre-stated margin, in at most one dataset in twenty. Under each of the coordinate, nested, separate, and split structures, it assigns that structure the largest stacking weight, or reports its disputed node as earned or not earned correctly, in at least four datasets in five, with interval coverage near its stated level.

Under multiple inheritance at moderate strength, it prefers the inheritance model to both pure trees in at least three datasets in four, and estimates which subgroups carry the second inheritance with stated accuracy. And under the gradient structure, it declines to crown a tree, spreading weight or reporting no earned node, in at least three datasets in four. Margins matter beside win rates, since a method can win often by amounts smaller than coder noise. Report the distribution of the score difference per mechanism, and compare it with the difference the same data produce under permuted cluster labels.

If the gate fails at planned sizes, the simulation itself says which resource buys recovery, mechanisms, lexemes, or coder agreement, by the same factorial logic the first round used for nouns and columns. Code more of whichever it is, down the random orders, and rerun the gate. If it still fails at the largest feasible size, section 7 applies. Under no circumstances does the confirmatory analysis proceed on a procedure whose false-node rate under flat structure is unknown.

That single rule would have prevented most of 24 October's wasted motion, since each mistaken proposal that day was an analysis choice whose behaviour under a known truth had not been checked.

## 6. What to collect next

The steps below are ordered so that no expensive coding happens before the design decisions it depends on are frozen. Cell counts use the present codebook's 104 codable possibility and universal columns, 102 plus 2, and the sample sizes proposed in section 3. A coded cell means one adjudicated or accepted value. Raw coder judgments run at three per cell under the present three-family protocol, before adjudication.

1. **Freeze the units, costing no cells.** Publish the holdout clusters over the 157 present rows, the mechanism grouping over the super-columns, the competitor set with each rival's assignment of every cluster, and the row-collapse sensitivities. Publish the applicability scope condition for every existing column, coded from definitions alone. This is analyst time, perhaps two days, and it gates everything else.

2. **Build and run the simulation gate, costing no cells.** Implement the generators and the full estimator pipeline from section 5. Confirm or revise the sample and column targets. No confirmatory coding starts until the gate passes or the project accepts a downgraded claim in writing.

3. **Build the confirmatory column frame, then code it for the rows already in hand.** Enumerate candidates from the three sources in section 2, attach design metadata, and select by the stated rule to add roughly 40 to 60 new possibility columns organised as about 15 to 20 new mechanisms, since mechanisms, not columns, are the bottleneck. Coding 50 new columns for the 157 present rows is 7,850 cells, about 23,550 raw judgments. Coding them later for the full row set costs the balance then, so nothing is coded twice.

4. **Code the sampled open-class lexemes on the full column set.** The target arm, 80 common-noun lexemes at about two forms each, 32 proper nouns, and 48 adjectives, adds roughly 240 forms. At 104 present columns that is 24,960 cells, and at 50 further confirmatory columns a further 12,000, for about 37,000 cells and about 111,000 raw judgments in the target arm. The pilot arm, 40, 16, and 24 lexemes, adds roughly 120 forms and about half those counts. The large arm, 100, 48, and 64, adds roughly 312 forms and about 48,000 cells on the full set. These are planning figures to the nearest thousand, since forms per lexeme vary, and they exclude the fact columns drafted by rule, which the ledger already produces cheaply, 3,737 cells for the present rows on the codebook's count.

5. **Judge the gold sample.** Draw about 400 cells at random across design strata and mechanisms, with a fixed seed, before proposals are seen, for Brett to judge blind. That is 400 judgments by Brett, the highest-value judging in the whole design, since it calibrates every accepted cell. Brett's remaining judging goes where it already goes, to splits, m values, frame notes, and flagged cells, a load the acceptance rule exists to keep feasible.

6. **Recode what the redefinitions require, no more.** The 16 columns whose definitions departed from their 2021 senses, the reversed universals, the split columns from the October redesigns, and gender under both definitions are already queued. Code them inside steps 3 and 4 rather than as separate waves, with packet wording checked against current definitions by the rule the project adopted after accepted cells fell from 1,429 to 285 on stale wording. That episode is the cheapest available lesson in why wording versions belong in the cell ledger.

Two things not to collect are worth naming, since each was live on 24 October. Do not collect preposition, adverb, or verb rows for the primary test, for the reasons in section 3. And do not collect more forms of lexemes already densely coded, further members of the personal paradigms, say, since copies add cells without adding clusters, and the whole design runs on clusters and mechanisms.

## 7. Failure conditions

A design that cannot fail cannot succeed either, so here are the results that would show the question cannot be settled with data of this kind, stated before any of them can be observed. Each names the observation and what the paper should then do.

- **The gate cannot pass.** At the largest feasible sample and column frame, simulated recovery for one or more rivals stays below the threshold, or the false-node rate under flat structure stays above it. The matrix approach then cannot adjudicate, and the paper proceeds on the ledger's stated-generalisations argument, with the matrix as a descriptive supplement and the failed gate reported in a methods note. That note is a contribution, not an embarrassment. It tells the next researcher where the evidential ceiling sits.

- **No structure beats flat.** On real data, flat structure predicts held-out clusters and mechanisms as well as every tree, within uncertainty. Distributional resemblance on this property population then carries no categorial signal beyond the leaves, and claims for or against any node must rest on other evidence, headedness and the secondary-use schema among the ledger's rows.

- **Function explains the resemblance.** A model whose clusters resemble each other by shared function, determiner occurrence, partitive heading, predicative use, predicts as well as or better than every category structure. The shared properties are then constructional, and the category question is underdetermined by distribution, however the forms cluster.

- **The confirmatory and legacy arms disagree, and the tipping point is weak.** If mild column selection, weaker than the selection the 2021 history plausibly imposed, suffices to flip the legacy arm's verdict in simulation, then no result on legacy columns can be quoted for the nesting question at all, and if the confirmatory arm is itself inconclusive, the question stays open on matrix evidence.

- **Support concentrates in one mechanism, one frame, or contested cells.** If removing the gradability mechanism, or the set-denoting frame, or the cells coders split on, removes a node's gain, the node is a fact about that mechanism, frame, or disagreement set. The paper should report it at that scope and argue the general claim, if at all, on linguistic grounds.

- **Multiple inheritance wins and the tree question dissolves.** If second inheritances for a few small subgroups absorb the pronoun-like signal, with the bulk of the inventory clearly placed, then asking which single tree is right was the wrong question. The paper's finding becomes the cross-classification itself, which the desk count already suggests is a live possibility, and coordination with stated exceptions may be its best expression.

- **Coder error is differential by leaf.** If the gold sample shows false-n rates differing across leaves by enough to move node gains across their thresholds under correction, the data cannot support the comparison at the achieved reliability. The remedy is better evidence per cell, corpus-bounded searches for the decisive n values, not more cells of the same kind.

- **Predictions fail where the ledger says they must hold.** The matrix result, whichever way it falls, makes claims about particular rows in the evidence ledger, the secondary use covering pronouns and compounds under one schema, determiners occurring on determinatives, bare *few* against bare quantity adjectives. If the winning structure's node-wise predictions contradict the attested record on rows marked as excluding an analysis, the property population has missed the relevant generalisations, and the ledger governs. A statistical winner that predicts *the real you is* should pattern with ordinary third-person reflexives, against the record, has failed a posterior predictive check that matters more than its score.

None of these outcomes would show that determinatives are or are not nouns. Several would show that a form-by-property matrix, coded as possibilities, cannot decide it, which is the possibility the prompt explicitly invites. The paper already has an argument that does not depend on the matrix, economy of statement plus the headedness and secondary-use rows. The worst outcome of this design is therefore not a wrong answer. It is clear knowledge of which evidence carries the conclusion. The worst outcome of skipping the design is a confident answer manufactured by column choice, indistinguishable from inside the result from a real one.

## Appendix A. Check against the mistakes of 24 October

- Answering a quantitative question by argument before simulating. The gate in section 5 forbids reading any confirmatory result from a procedure untested under known truths, and every size in section 3 is labelled a planning figure for the gate to confirm.

- Equating unbiased estimates with an unbiased verdict. Margins and win rates, not only estimates, are simulated, since the verdict is a nonlinear function of noisy profiles and inherits their asymmetries.

- Stratifying on a measured property. Countability and its cousins are excluded as strata in section 3, and column selection on observed patterns is excluded by the metadata-only rule in section 2. The same principle governs rows, columns, and frames.

- Weighting scores by a rival's subcategories. Scores are kept apart by design stratum and averaged over mechanisms. Clusters are defined below every rival's leaves, from morphology, so no rival supplies the scoring units.

- Simulating added categories as if the columns described them. Applicability is a generated layer in every simulation, x is never recoded to n in the confirmatory path, and categories the columns cannot describe stay out of the primary test.

- Recording values as Brett's judgments when he ruled only on a column's sense. The gold sample separates judging cells from ruling on senses by construction, and coder identity and evidence strength stay in the data through to the model, so provenance cannot be laundered by aggregation.

## Appendix B. Competitor set, stated exactly

For the preregistration, each competitor is a function assigning every holdout cluster to a leaf, plus a tree or inheritance graph over the leaves. Leaves are sets of clusters. The set to generate under, fit, and score is as follows.

- Separate: determinative clusters under no Noun node.

- Nested: determinative and pronoun clusters under an intermediate node inside Noun. Compound clusters are assigned as Hudson assigns them in his own scoring run and as *CGEL* assigns them in a sensitivity, since Hudson's published set is partial and the extension to the full inventory is itself a claim to state.

- Coordinate: the four subcategories under Noun with no intermediate node.

- Split: gradable determinative clusters with adjectives and the remainder nominal. The split's membership is fixed from grade morphology before fitting, not fitted to the outcome.

- Multiple inheritance: coordinate plus second parents for named subgroups, compounds, demonstratives, wh clusters, and the personal forms before a noun. Each second parent is removable by the fit.

- Flat: no internal node. Saturated: free cluster profiles, as the ceiling.

Hudson's set-aside items, *all*, the numerals, and the plural and non-count restricted words on the ledger's account, are scored for every competitor but excluded from the nested competitor's training fit in one arm and included in another, so that the paper tests Hudson's claim as published and its natural extension separately, and says which is which.

Cardinal clusters form their own scoring stratum in every arm, as section 1 provides. Boundary clusters, the *where* compounds, *today*, *there*, *last*, *next*, *once* and its kin, are flagged in the cluster table, and every headline result is reported with them in and out. If a headline changes when flags flip, the flagged result is the headline.

