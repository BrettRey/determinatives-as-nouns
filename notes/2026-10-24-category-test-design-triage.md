# Triage: two outside designs for the category test
<!-- SUMMARY: triage of GPT Pro's and Muse Wonder Full's responses to the outside-model prompt (24 Oct): where they agree, where they differ, what was checked, what to adopt, and the decisions left to Brett · status: for Brett · updated: 2026-10-24 -->

Responses: GPT Pro, pasted by Brett and saved as `notes/2026-10-24-category-test-design-pro.md`; Muse Wonder Full, `notes/2026-10-24-category-test-design-muse.md`. Prompt: `notes/2026-10-24-prompt-for-outside-models.md`. Triage by Claude Opus 5.5. Nothing below is implemented yet.

## Bottom line

Both reject a four-way contest between trees as posed. They converge on the same programme:
- a multilevel model in which each rival supplies a structure for sharing information;
- competitors that include no structure at all and overlapping affiliation;
- a property bank defined and frozen before coding, with the 2021 columns demoted to an exploratory arm;
- applicability modelled as prerequisites, keeping x apart from n;
- lexemes, not forms, as the sampling unit;
- coder error modelled against a blind gold sample;
- a far stronger simulation gate before any confirmatory coding.

They differ on two points. **First, the held-out unit.** Pro withholds a property family and predicts it for the determinatives from a donor panel. Muse holds out lexeme clusters crossed with families. **Second, categories beyond adjectives.** Pro thinks they're needed; Muse wants them kept out of the primary test.

On the second point Pro is right, and it's decisive. With adjectives as the only category outside Noun, the coordinate tree is indistinguishable from no structure, once each property has its own baseline and each node its own variance. The shared Noun node is absorbed into "adjectives differ". I checked this numerically. The centred covariance of the coordinate tree equals that of a star whose extra variance sits on adjectives, while the nested tree's pronoun–determinative node and the separate tree's {common, proper, pronoun} grouping both survive centring. As set up, then, the matrix could count against the rivals but never for the coordinate analysis. A second category outside Noun, verbs or prepositions, makes the nominal partition testable, provided the questions describe that category. Even then, what becomes testable is a partition, not a Noun node with a rank.

This also explains the asymmetry in the 24 October simulations. The coordinate tree was recoverable there only because every node was forced to the same variance.

## Punch list: adopt

1. **Withdraw as requirements** the figures 100 common nouns, 24 proper nouns, and 24 adjectives, and "about 115 columns". Both responses agree on this, and so does running the main test only on columns every category can have, which becomes a sensitivity: filtering on observed patterns selects on the outcome.
2. **Competitor set:** the coordinate, nested, separate, and split analyses; a flat model (no internal node); overlapping or multiple affiliation; and, in simulation only, functional resemblance without category, and a gradient. Report "unresolved" and "none predicts adequately" as possible outcomes. (Both.)
3. **Free, regularized node variances**, with no equal-variance restriction. Check priors on observable contrasts. (Pro.)
4. **A second category outside Noun**, with questions that describe it. Pro's suggestion: pilot verbs and prepositions at matched budgets. (Pro, checked.)
5. **A prospective property bank**, assembled from stated sources. Each question gets metadata before coding (source, domain, frame, prerequisite), and the bank is frozen before confirmation. Beside it sit a targeted-diagnostic bank of each rival's strongest predictions and the legacy bank as exploratory. (Both.)
6. **Prerequisites:** a prerequisite failure enters once, and the questions that depend on it become conditional x. A whole category being n isn't evidence of inapplicability. (Both.)
7. **Weight by mechanism family**, one vote per family. Report alternative weightings, the families driving the result, and the effective number of independent properties. (Both.)
8. **Rows:**
   - A units table separating expression, form, lexeme, use, and base, with holdout clusters fixed from morphology alone.
   - Each rival gets a frozen assignment map for every cluster, and completions beyond what the source covers are labelled as operational extensions.
   - Boundary rows (*today*, *there*, *once*, *last*, the *where* compounds) run in and out. Numerals form their own stratum.
   - The quantity nouns become a challenge set.
   - Rows split by use or reading get collapse sensitivities.

   (Both.)
9. **Noun-draw replacements on mechanical grounds only**: not an English lexeme, a duplicate, a spelling variant, or no codable use. No category judgment. Replaced items are kept and re-entered in a sensitivity. (Muse; `draw_sample.py` needs this change.)
10. **Coder error:**
    - a latent-truth model of each coder;
    - a gold audit drawn at random before proposals are seen;
    - full provenance kept;
    - the 371-in-390 agreement not carried over as an accuracy rate for new rows.

    (Both.)
11. **The framing check, broken down by category and family.** The prompt gave only the totals (670 against 663 n's). The paired discordance (71 cells one way, 64 the other) is already in DECISIONS. What's unchecked is cancellation within categories or families. (Pro, adapted.)
12. **The simulation:**
    - Organize it by aims, data-generating mechanisms, estimands, methods, and performance measures (ADEMP).
    - Run about 200 replications for screening and 1,000 for any decision; the 24 October runs used 30 to 40.
    - The generators need correlated families, prerequisites, lexeme structure, coder error, and column selection.
    - The whole analysis pipeline runs inside the loop, and the estimator never sees the true masks or memberships.
    - Check the computation by simulation-based calibration.

    (Both.)
13. **Controls:** negative controls (the shape columns) and positive controls (plural inflection across the noun subcategories). (Muse.)
14. **Keep the predictive claim apart from the grammatical interpretation.** A covariance model measures statistical sharing. Economy of grammatical statement is a separate argument, made by comparing rule formulations. (Pro; Muse similar.)
15. **A smallest effect that matters, fixed in advance.** Against Hudson's tree, the coordinate analysis can win only by showing that the pronoun–determinative node is negligible, since a nested model can always shrink that node to zero. So the smallest node effect worth counting must be declared before any data are seen, either in predictive units or as a share of between-subcategory variation. A near-zero estimate then counts as equivalence, not as "unresolved". Against *CGEL*'s separate category, positive evidence is possible once a second category outside Noun is in. (Side agent; Pro mentions it in passing.)
16. **Rows stay forms; lexemes belong to each rival** (Brett: "there's a valid question about whether my is a determiner (Hudson) or a pronoun (CGEL), so lexemes can't work"; and shared-base clusters "can't deal with suppletion though or the relationship between I, my, and mine").
    - Each rival supplies its own lexeme map.
    - Holdout clusters are the union of every rival's links, so *I*, *me*, *my*, *mine*, and *myself* are held out together and no rival gains from leakage.
    - The lexeme-level columns built on 24 October assume *CGEL*'s paradigms, so they need a version under each rival's map or must leave the comparison.

    This replaces Muse's lexeme clusters.
17. **The 2021 columns came from an exhaustive search within pronouns and determinatives** (Brett: "I tried to be exhaustive and include every property I could find"), not from selecting columns that contrast them. The imbalance comes from where the search looked, so the remedy is the same search over nouns, adjectives, and any outside categories, which is close to both responses' prospective bank.

## Adapt

- **Held-out unit:** run both. Pro's family transfer is primary for the determinative question, and Muse's clusters crossed with families is a second arm. Pro says they answer different predictive questions, so this is a multiverse, not a choice.
- **Value scale:** Muse puts possibility (m with y) as the headline, because the determinatives were searched harder; Pro wants an ordinal likelihood. Run both; the headline is Brett's call.
- **Muse's lead claim**, that the present columns "manufacture the nested answer", is overstated. It rests on my masking simulation, which converted x to n and overwrote the generated cells (Pro's critique, also Muse's own in section 2). The worry about how the columns were chosen stands; the 97-to-100% figure doesn't measure it.

## Reject

- **Muse's attribution** to Hudson of a criterion that a category must "earn its place", "quoted in the ledger": I couldn't find it in `planning/evidence-ledger.md`. Don't cite it without the source.
- **Muse's exclusion of other categories from the primary test**: it conflicts with the identification result above.

## Defer: Brett's decisions

1. **Which second category:** verbs, prepositions, or both (Pro: pilot both at matched budgets). For prepositions, which list: Simple English Wiktionary (Brett's suggestion), *CGEL* ch. 7, or the union of a tagger's labels (Pro)?
2. **The gold audit:** Pro proposes 600 random cells plus 200 hard ones, judged independently by two people; Muse proposes about 400 random cells judged by Brett. Is there a second human judge? `diagnostic-validity` named Pullum as a candidate.
3. **Headline value scale:** possibility or ordinal.
4. **Budget and order:** Pro's staged route (identification checks, clean simulations, a pilot of about 11,000 cells, realistic simulations, freeze, then collection), or Muse's target arm (about 37,000 cells). Both call their figures planning numbers, not power results.
5. **Whether to proceed at all**, given that both name, as a live outcome, "the matrix illustrates but doesn't adjudicate", with the ledger's argument from economy of statement carrying the conclusion.
