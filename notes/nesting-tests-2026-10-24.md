# Testing a nested category against sibling categories: methods from other fields
<!-- SUMMARY: answer to Brett's 24 Oct question about how other sciences tell a nested group from sibling groups, with what each method needs from this paper's data; citations marked as read in literature/ or from memory and unchecked · status: note, for the structure review · updated: 2026-10-24 -->

Brett's question (24 Oct 2026): "What techniques have other sciences used to discriminate nesting from sibling categories?" The paper's version: is there an intermediate category of pronouns and determinatives inside Noun (Hudson's nesting), or are the two coordinate subcategories?

Sources marked **[lit]** are in `literature/`, and the quoted or described passage was read today unless the entry says otherwise; **[memory]** means the reference is from memory and unchecked, so read it before citing. All the tests run on English data only, in keeping with Brett's point that data about lexemes and lexical categories in one language tell us little about another.

## 1. Group only on shared derived characters

In phylogenetic systematics a nested group is supported only by characters its members share and other groups lack (synapomorphies). Shared states that are simply ancestral or general support nothing, and characters acquired independently in separate branches (homoplasy) count against a grouping. **[memory]** Hennig (1966). Doyle (2022) uses this vocabulary for cell-type taxonomy, contrasting a lineage where "transcriptomic signatures are perfectly correlated with cell lineage" (two synapomorphies, no homoplasy) with one where they are incongruent **[lit]** (`bio_doyle_2022_cell_types_as_species_metaphor.md`). Historical linguistics has the same rule for subgrouping languages: only innovations shared exclusively by a subgroup define it **[memory]** (the principle usually credited to Leskien and to Brugmann).

For the paper: the pronoun-and-determinative node needs properties present in both and absent from common nouns, proper nouns, and an outgroup such as adjectives. A property the two share with other closed categories (a closed inventory, which coordinators also have) doesn't support it. Properties determinatives share with common nouns and not pronouns count against it.

## 2. Count the conflict

Characters that cut across a proposed grouping are counted, not explained away. Two measures: the consistency index of characters on a tree **[memory]** (Kluge & Farris 1969); and the pairwise compatibility or four-gamete test, under which two binary characters fit one tree without homoplasy only if the taxa don't show all four combinations of their values **[memory]** (Le Quesne 1969; in population genetics, Hudson & Kaplan 1985, a different Hudson). The four-gamete test has been run on the determinatives already: 5 of 20 pairs of pronoun-like and quantity-like characters conflict (`analysis/node-reach-2026-10-24/README.md`).

## 3. Test whether the data are hierarchical at all

Cluster the forms, then correlate the distances the dendrogram implies with the original dissimilarities (the cophenetic correlation). A 2026 *Cognition* folk taxonomy of magic reports 0.87 and notes that "datasets that do not display hierarchical structure typically have correlations below 0.5", citing Sokal & Rohlf (1962) and Rohlf & Fisher (1968) **[lit]** (`A-folk-taxonomy-of-magic_2026_Cognition.md`). Split networks (NeighborNet) and delta scores show conflicting signal as boxes instead of forcing a tree, and have been applied to language data **[memory]** (Holland et al. 2002; Bryant & Moulton 2004; Gray, Bryant & Greenhill 2010).

## 4. Ask whether the intermediate category improves prediction

Category utility measures how much knowing that something belongs to a category raises the predictability of its features; a level of a taxonomy is worth having where its utility is highest **[memory]** (Gluck & Corter 1985; Corter & Gluck 1992). Applied here, the pronoun-and-determinative node earns a place if knowing a word is in it predicts its properties better than knowing only its subcategory and that it's a noun. This is a quantitative form of Hudson's own criterion that every category "must earn its place by doing some work in the grammar" **[lit]** (Hudson 2000, §2). Cue validity, a related measure, is discussed by Lakoff (1987) **[lit]**, not read today.

## 5. Compare nested and flat models by fit

In psychometrics a higher-order factor over correlated first-order factors is compared with a model in which the first-order factors simply correlate; Carroll's (1993) three-stratum model of cognitive abilities is built this way **[lit]**, passage not read today. With binary grammatical features the analogue would be a latent-class or hierarchical mixture model compared by likelihood or cross-validation. That needs many more coded forms than the matrix has.

## 6. Allow more than a tree

Word Grammar allows multiple inheritance: "the organization allows any concept, whether exemplar or category, to belong to more than one taxonomy" (Hudson 2010, §2.4.1, with 'pet canary' inheriting from 'pet' and from 'canary', Figure 2.6) **[lit]**. Hudson (2010, §3.3) also treats features and cross-classification **[lit]**, table of contents only. On such a structure the compounds could inherit from both pronoun and determinative. The paper needs a position on this third option either way.

## What fits the paper

For an ELL paper of 9,000 words: tests 1 and 2, as one table of properties by group (common noun, proper noun, pronoun, determinative, with adjectives as outgroup) and a count of the properties that support or conflict with each grouping. They need only coded data and are easy to explain to an English grammarian. Tests 3 and 4 could go in a supplement. All of them first need the reference set of nouns and adjectives coded on the matrix's syntactic columns, with Brett judging the cells (ledger row `noun-reference-set`).
