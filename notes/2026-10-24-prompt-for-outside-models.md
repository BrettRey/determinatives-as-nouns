# Prompt for outside models: designing the category test
<!-- SUMMARY: a self-contained brief for another model to design, from first principles, the analysis that adjudicates between rival classifications of English determinatives, with the data, what has been established, and what went wrong on 24 Oct · status: for Brett to send · updated: 2026-10-24 -->

*Brett: paste everything below the line. The repository is public; the branch named there holds the files it points to.*

---

Thank you for taking this on. I'm a linguist working in the framework of *The Cambridge Grammar of the English Language* (Huddleston & Pullum 2002; *CGEL* below). I need a statistical design that can decide between rival classifications of English word categories, using a feature matrix of word forms by grammatical properties. A first attempt, built with another model over one long day, went wrong in several ways, listed below so you don't repeat them. I'd like your own design from first principles, not a repair of that one. If you think the question can't be answered with data of this kind, say so and say why: that's a useful answer.

## The repository

Public: <https://github.com/BrettRey/determinatives-as-nouns>, branch `feature-matrix-2026-10-24`. The files that matter:

- `analysis/matrix-2026-10/matrix-2026-10.csv`: the 2021 feature matrix (also LingBuzz 005747): 139 pronoun and determinative forms by 105 columns, values y, n, and a handful marginal, judged by me in 2021.
- `analysis/codebook/forms.csv`: all 157 rows (the 139 plus 18 added nouns and adjectives), with category and a plain label.
- `analysis/codebook/columns.csv` and `definitions.csv`: the 159 columns as now defined, each typed (possibility claim, fact of form, fact of the lexeme, base morphology, derived, superseded) and grouped into 31 property families ("super-columns").
- `planning/codebook.md`: the coding rules (values, frames, polarity, blind coding, provenance, analysis commitments). Sections 9 and 11 hold the analysis plan and the open questions.
- `analysis/tree-recovery-sim/`: the simulation code and results described below (`simulate.py`, `real_patterns.py`, and the `.md` result files).
- `notes/nesting-tests-2026-10-24.md`: methods from other fields considered for telling nested from sibling categories.
- `planning/evidence-ledger.md`: what each rival analysis predicts for particular observations.
- `DECISIONS.md`: the dated decision log, 24 October entries especially.

Not in the repository: the blind coders' outputs and review files, kept local. The 18 added rows exist so far only as model-coded proposals.

## The question

Four classifications of English determinatives (*the*, *a*, *some*, *every*, *few*, *this*, *which*, *someone*, and so on) are in play. Keep category and function apart: "determinative" is a lexical category; "determiner" is a syntactic function, the function *the* has in *the dog*, which is an NP with a determinative phrase in determiner function. None of the analyses below is Abney's DP hypothesis.

1. **Separate category** (*CGEL*): determinative is a lexical category of its own, beside noun, verb, adjective, and the rest; pronoun is a subcategory of noun.
2. **Nested** (Hudson 2000, 2004): determinatives are pronouns, and pronoun is a subcategory of noun.
3. **Coordinate** (my proposal): Noun has four coordinate subcategories, common noun, proper noun, pronoun, and determinative.
4. **Split** (Van Eynde 2003, stated for English): determinatives divide between adjective and noun.

A desk count over the 2021 matrix also suggested multiple inheritance: pronoun-like properties confined to a few small subgroups of determinatives (the compounds *someone*, *nothing*; the demonstratives; the wh-forms; *we*, *us*, *you* before a noun).

The rivals don't share all their subcategories. Hudson counts the compound determinatives as pronouns, *CGEL* as determinatives; Van Eynde splits the determinatives. A test must not build in any one rival's assignments.

## The data

- **Rows are word forms**, not lexemes: *he*, *him*, *his*, *himself* are separate rows, and so are *dog* and *dogs*. Many properties hold of the lexeme and repeat across its forms.
- **The closed classes are complete**: the 139 pronoun and determinative forms are the whole inventory, so they carry no sampling error. The open classes are samples: so far 10 common-noun forms (seven of them quantity nouns chosen because they sit near the determinatives: *lot*, *number*, *numbers*, *plenty*, *dozen*, *dozens*, *majority*), 2 proper nouns, and 6 adjectives. A random sample by frequency band from SUBTLEX-UK has been drawn but not coded.
- **Values**: y (can), m (only degraded), n (never), x (the property can't arise). Variety and register are a separate field, not a value. Some columns are split by construction ("frames"): a determiner in an argument NP against a predicative or fixed-PP use, a set-denoting secondary use (*the Smiths*, *ten mes*, *somethings*), echo questions, arithmetic (*twice two*).
- **Who coded what**: the 2021 cells are my judgments. Other cells are proposals from blind coders (three model families, given plain labels and never the hypothesis), which I then judge, or accept by rule when all three agree.
- **The columns weren't sampled from any frame.** The 2021 columns were chosen to tell pronouns from determinatives; others were added on 24 October from *CGEL*'s diagnostics for nouns and adjectives, from morphology, and from a redesign.

## What has been established, with the evidence

1. **Holding out one form at a time can't separate the trees.** The rivals differ only above the subcategory level, so a held-out determinative is predicted from the other seventy whichever tree is used. A simulation confirmed it: recovery of the generating tree was erratic and margins near zero.
2. **The score mustn't use any rival's subcategories**, since the rivals don't share them. The plan reports accuracy for the closed inventory and the open-class samples separately, plus their combination under each defensible weighting.
3. **Holding out a whole group, predicted from the plain mean of its sibling groups, is biased** toward whichever tree gives the held-out group more siblings. Predicting it through the tree's covariance, with the between-node spread estimated from the data, removes that bias.
4. **Open-class sample size changes the verdict.** With few nouns, proper nouns, and adjectives, their noisy profiles make the determinatives look closer to the precisely measured pronouns. In simulation the coordinate tree was recovered about one time in three with the current open-class rows, and 19 times in 20 at 100 common nouns, 24 proper nouns, and 24 adjectives.
5. **The column set decides the test.** On the 77 columns with coded noun and adjective rows: 22 can vary for every category; 11 vary only for pronouns and determinatives (nouns and adjectives n throughout); none varies only for common and proper nouns. Simulated with that pattern, the group-out test picked the nested tree 97 to 100% of the time whatever tree generated the data. Restricted to columns every category can have, the bias disappeared and recovery reached 0.90 or more for all three trees, but only with about 115 such columns. The matrix has about 22.
6. **About the coders**: showing them my 2021 value as a claim made no detectable difference against a neutral framing (on 1,153 identical cells, 670 n's against 663). Two runs of the same model disagreed on about 15% of those contested cells. Where all three families agreed, they matched my 2021 cells 371 times in 390, an upper bound because some prompts named the forms.

These simulations generated binary cells from the same model family the test then fitted, so they are best cases.

## What went wrong on 24 October

So you can check your own design against the same mistakes:

- Answering a quantitative design question ("does the number of nouns matter?") by argument, as no, before running the simulation that showed yes.
- Equating "doesn't bias the estimates" with "doesn't change the outcome": noisy but unbiased estimates still bias the verdict.
- Proposing to stratify the noun sample by countability, which is one of the properties being measured.
- Planning to weight scores by subcategory, which assumes the classification under test.
- Simulating added categories (prepositions, adverbs, verbs) as if the columns described them as well as they describe nouns. They don't: on most of these columns such categories are n throughout. That produced a spurious gain, since withdrawn.
- Recording values as my judgments when I had ruled only on what a column means.

## What I'd like from you

1. **The overall approach.** Is comparing trees by held-out predictive accuracy right at all? Weigh it against alternatives such as phylogenetic comparative methods, latent-class or mixture models, item-response models with category structure, estimating a between-group distance matrix and comparing it with each tree's implied structure, Bayesian model comparison over structured covariances, and models that allow multiple inheritance. Recommend one primary method and say what it assumes.
2. **The columns.** What population of properties should the test draw on, and how should columns be sampled or weighted so that no rival's favoured properties dominate? How should properties that can't vary for a whole category be treated: as informative n's, as missing, or as a separate layer of structure? When are properties only pronouns and determinatives can have evidence of a shared node, and when an artefact of column choice? How should correlated columns (one mechanism behind several properties) be counted?
3. **The rows.** How many open-class words, from what frame, stratified how? Whether to add prepositions, adverbs, or verbs. If so, how to define their samples without assuming one grammar's boundaries (a traditional tagger files many of *CGEL*'s intransitive prepositions, *away*, *abroad*, *downstairs*, as adverbs), and what columns they would need.
4. **The model.** How to handle the y/m/n scale, variety, frames, lexeme-level facts that repeat across forms, disputed forms, and the mix of my judgments with model-coded cells.
5. **A simulation plan** that would show your design recovers a known structure under realistic conditions, with what "realistic" has to include: applicability patterns, correlated columns, lexeme structure, coder error. Say what it must show before any real data are coded.
6. **What to collect next**, with sizes and a rough cost in coded cells.
7. **Failure conditions**: results that would show the question can't be settled with this kind of data.

## Ground rules

- Cite methods only where you're confident of the reference, and mark anything uncertain. Don't invent citations or figures.
- Keep linguistic examples to forms whose behaviour you're sure of, and flag any judgment you're unsure of.
- Terms: "lexical category" (not "word class"); "tensed" and "non-tensed" clauses (not "finite"); keep categories (determinative, noun) apart from functions (determiner, head); "proper noun" is the category, "proper name" the meaning.
- Prose, not bullet fragments, for your reasoning. Lists are fine for the deliverables.
