# Paper plan — Determinatives as nouns

## Target, length, conventions

- **Target journal:** *English Language and Linguistics* (Reynolds 2026 numerals appeared here; CGEL-friendly; English-only fits). Secondary: *Glossa*.
- **Length:** 7,500-8,500 words.
- **Title:** "Determinatives as nouns" (working).
- **Style:** project-local rules in `.house-style/style-rules.yaml` (preamble in `.house-style/preamble.tex`); full guide at `../../.house-style/style-guide.md` (central). Key constraints listed below.

## Thesis in one sentence

English determinatives are a subtype of the lexical category Noun, alongside common nouns, proper nouns, and pronouns, with sub-cluster-specific combinatorics explaining their distinctive surface distribution.

## Style discipline (read before drafting)

- No openings that lead with an example for rhetorical effect; state the claim directly.
- No metacommentary frames (no "a potential worry", "one might object", "it's worth noting"). Just say the thing.
- No corrective "not X but Y" framing. State what something is.
- Banned: *crucially*, *must* (use *have to*), *moreover*, *furthermore*, *nevertheless*, *however* (use *but*).
- Contractions preferred. ~60-word paragraphs, 100 max.
- 5-7 major sections, no `\subsubsection{}` if avoidable.
- No bold labels in argument sequences. Use ordinal markers.
- *Data* is singular. Avoid *wh-* terminology.
- Categories: `\term{}` for concepts (small caps); `\mention{}` for forms (italics); `\olang{}` for object language; `\enquote{}` for quotations.
- Citations: `\citep{}` parenthetical, `\textcite{}` textual.
- Examples: `\ea ... \z` (langsci-gb4e), no `exe` environment.

## Argumentative spine

Following Brett's review of v1, the spine is:

> claim → category criteria → two payoffs → hardest objection (*the/a*) → compressed prior-art differentiation → residual cleanup → conclusion.

Aux-as-V is *nearest precedent for the kind of taxonomic move*, not the argument; it sits at the end of §2 behind the bridge evidence.

## Two planning assets (drafted before prose)

- `notes/diagnostic-table.md` — what counts as evidence for nounhood, applied to all four sub-categories.
- `notes/objection-matrix.md` — falsification conditions for the central claim.

## Sections (7)

### §1 Introduction (~700 words)
First sentence: the proposal. English has four sub-categories of `\term{noun}`: common, proper, pronoun, and determinative.

Brief framing: the move extends Spinillo (2000, 2004) and Van Eynde (2003), which dissolve the determinative class on independent grounds, by adding the architectural commitment those papers stop short of. The paper preserves CGEL's category/function distinction and the N-headed NP analysis (it isn't Abney 1987's DP).

Brief statement of the membership criterion: the standard nounhood test is canonical NP-headedness — items that head NPs filling subject, object, or PrepC function — and the paper argues determinatives meet it once the fused-head construction is reanalysed. §3 makes that case.

Seed the *the/a* answer in two sentences: the central articles never stand alone, so they're the worst case. They're the maximally grammaticalised limit of the determinative sub-cluster, parallel to defective members of the proper noun sub-cluster (`\mention{the Hague}`, `\mention{*the Paris}`). §4 develops this answer.

Preview the structure briefly.

### §2 Bridge from Noun to Determiner (~900 words)
Two CGEL-internal facts that make the proposal less radical than it sounds. §2 is *bridge evidence*, not a test of the membership criterion (which is in §3). The point is that the determiner system already draws on the noun system in two distinct ways, so the question §3 takes up is about extending that fact, not creating it.

Stage A — paradigmatic relatedness across the determinative/pronoun split. CGEL classifies the dependent possessive set (`\mention{my, your, his, her, our, their, its}`) as determinatives and the independent possessive set (`\mention{mine, yours, his, hers, ours, theirs, its}`) as pronouns. The two sets are paradigmatically aligned: same person, number, gender, and possessive semantics, differing only in syntactic function. The current taxonomy splits a single inflectional paradigm across two distinct primary lexical categories. Reynolds 2013 (p. 10) and 2014 (p. 90) already note the oddity. The split is unexplained on the CGEL view; natural under the present proposal (sub-categories of Noun sharing inflectional resources).

Stage B — genitive NPs in determiner function. Genitive NPs headed by common or proper nouns fill determiner function (`\mention{Kim's book}`, `\mention{the king's every whim}`, `\mention{that man next door's car}`). The genitive NP is structurally an NP, headed by a noun (Payne, Huddleston & Pullum 2007: 2). So the determiner function already admits items headed by nouns.

Together, the two stages show that the determiner function is already drawing on the noun system in CGEL's existing taxonomy. What §3 takes up is whether the remaining determinatives — non-paradigmatically-related, non-genitive items like `\mention{the, a, this, every, some}` — also fit the noun system. (Cardinals are out of scope: Reynolds 2026 absorbs them into existing sub-categories.)

End of §2: the auxiliary precedent. Pullum & Wilson 1977 dissolved AUX into V; CGEL preserves this. The kind of taxonomic move the paper makes for determinatives — taking a closed functional class to be a sub-category of an existing open lexical category — has a published precedent in the verbal domain. The precedent isn't an argument from analogy; it's a sanity check that the move has been made elsewhere in the same descriptive framework.

(No table in §2. The Stage A paradigm split can be illustrated inline as a numbered linguistic example showing the dependent-vs-independent forms; no comparison table is needed for the bridge case.)

### §3 The category-membership argument (~2,200 words)
One direct argument (§3.1) and one downstream simplification (§3.2).

State the membership criterion at the start: a lexical category C is a sub-category of Noun iff items of C can head NPs (i.e., serve as Head N within NP structure) where those NPs fill subject, object, or PrepC functions, and where this Head function is part of the category's profile rather than reached via fusion of another function with Head. The criterion respects CGEL's phrasal architecture: lexical items head phrasal categories; phrasal categories serve syntactic functions.

Category membership is determined at the sub-category profile level. A sub-category qualifies if its items canonically head NPs as part of the sub-category's profile; individual lexically defective members are admitted on paradigmatic grounds. Compare proper nouns: most head NPs canonically (`\mention{Kim}`, `\mention{Toronto}`); `\mention{the Hague}` and similar place names are defective in requiring an article; all belong to the proper noun sub-category. The same allowance covers `\mention{the}` and `\mention{a}` within the determinative sub-category — defective members of a sub-category whose profile satisfies the criterion. §4 develops this point.

Adjectives in `\mention{the rich}` head NPs only via genuine Mod-Head fusion. Adjectives don't head NPs as part of their lexical-category profile; they head AdjPs, which canonically fill modifier function within NP and predicative complement function within clauses. Mod-Head fusion is the exceptional case in which an AdjP is reanalysed as occupying NP Head function. Adjectives don't satisfy the criterion.

Items occupying Predeterminer function deserve a separate note. Most CGEL "predeterminer" items (`\mention{all, both, half}`) are also classified as determinatives in their non-Predet uses; their fused-head occurrences are simple fused-head under the proposal, subsumed by §3.1 below. A small residue of Predet-only items (`\mention{such, what a, many a, quite a, rather a}`) is structurally bound to a following Det+N sequence and cannot head NPs at all, fused or otherwise. Either way, no Predet-Head residue threatens the criterion.

§3.1 *The fused-head reanalysis* (~1,400 words). The direct category-membership argument. CGEL §5.9 treats fused heads as a deviation from canonical NP structure, realised by fusion of functions of Det (or Mod, or Predeterminer) with Head. Payne, Huddleston & Pullum 2007 develop fusion of functions as a first-class theoretical construct with six defining properties.

The asymmetry between simple fused-head (determinatives) and the residue (Mod-Head, Predet-Head) needs a positive discriminator, not just a parsimony argument. Two independent facts ground the asymmetry:

(a) **Paradigm productivity.** Fused-head use is a broadly productive pattern within the determinative class. The set of determinatives that admit it includes `\mention{some, all, both, many, few, several, most, this/these, that/those, each, either, neither, much, enough}`. CGEL (371-2) and PHP (2007: 22-23) identify a small set of lexically defective members: `\mention{the}` and `\mention{a}` lack fused-head use entirely, `\mention{every}` doesn't appear as a fused head, and `\mention{no}` is restricted to the suppletive `\mention{none}`. The defective set is small and independently noted; the pattern remains broadly productive across the rest of the class. (Cardinals are out of scope per Reynolds 2026.) Adjective Mod-Head fusion, by contrast, is lexically restricted to a small set (`\mention{the rich, the poor, the elderly, the dead, the unemployed, the unobtainable}`), mostly adjectives describing classes of people. The pattern is broadly productive within determinatives and narrowly lexicalised within adjectives.

(b) **Structural saturation.** Simple fused-head NPs require no additional structure: `\mention{some left}`, `\mention{many came}`, `\mention{all agree}` are full NPs with the determinative as sole element. Mod-Head fusion requires a determiner: `\mention{the rich}` is a full NP, but `\mention{*rich}` alone (referring to a class of rich people) isn't. The Mod-Head AdjP can't saturate the NP on its own; the simple fused-head determinative can. Predet-only items (`\mention{such, what a}`) are even more bound — they require Det+N to follow and never head NPs.

(a) and (b) distinguish the simple fused-head case from the residue independently of the categorial conclusion. Determinatives behave like full Heads paradigmatically and structurally; AdjPs in Mod-Head use need the Det position filled and are lexically restricted; Predet-only items can't head NPs at all.

If the reanalysis is right, the determinative sub-category satisfies the membership criterion: its items head NPs in subject, object, and PrepC functions, and the Head function is part of the sub-category's profile rather than reached via fusion. The supercategory Noun thus admits all four sub-categories.

**Table 1** (in §3, after §3.1): four-way diagnostic. Rows show that all four sub-categories satisfy the membership criterion under the §3.1 reanalysis. Columns are the sub-categories with example forms.

§3.2 *Determiner function uniformly filled by NP* (~700 words). A downstream simplification, not an independent ground for nounhood. Once §3.1 is granted and determinatives are nouns, the determiner function — already filled by genitive NPs (Stage B in §2) — is now uniformly filled by NPs across the board. The disjunctive "Det = DP or genitive NP" specification collapses to "Det = NP."

The simplification has bite: it explains why genitive NPs and determinative-headed NPs pattern alike in the determiner slot (definite reference contribution, blocking of articles, fused-head licensing). They pattern alike because they're the same kind of constituent. But §3.2 doesn't independently establish nounhood for determinatives; it cashes out a consequence of having established it.

### §4 The articles (~750 words)
The compact answer to the hardest objection. Articles `\mention{the}` and `\mention{a}` never stand alone. CGEL (371-2) and PHP (2007: 22-23) already mark this defectiveness as a lexical property of specific items, not a category-level fact (compare `\mention{every}`'s resistance to fused head and `\mention{no}`'s suppletive `\mention{none}`). Lyons 1999 supplies the diachronic and typological context: articles are grammaticalised from demonstratives and the numeral `\mention{one}`; phonologically weak; semantically minimal; cross-linguistically non-universal.

The defective limit of the determinative sub-cluster is parallel to the defective limit of the proper noun sub-cluster (`\mention{*the John}`; `\mention{the Hague}` requires the article and resists pluralisation). Defectiveness within a sub-category is familiar.

### §5 Nearby proposals (~1,200 words)
Compressed. Table 2 (from `notes/objection-matrix.md` Table B and `notes/phase2a-differentiations.md`) summarises seven proposals along three dimensions: unification direction, common noun status, English applicability. Then four short paragraphs:

The dissolve-Det tradition. Spinillo 2000, 2004 dissolves the determinative class for English without committing to a positive taxonomy. Van Eynde 2003 splits determinatives between adjective and noun on Italian and Dutch agreement morphology. The present paper extends Spinillo's negative case with the specific fourfold-Noun architecture, and diverges from Van Eynde because English lacks the agreement evidence his split relies on.

Pronoun-determinative unification, opposite directions. Hudson 2004 makes determiners a subset of pronouns; Postal 1969 derives pronouns from underlying [+Pro] nouns plus articles; Anderson 1997 groups names, pronouns, and determinatives as the {N} category and leaves common nouns separate. The present paper keeps all four as coordinate sub-categories under Noun.

Pronoun decomposition. Déchaine & Wiltschko 2002 fragment the pronoun category into pro-DP, pro-φP, pro-NP. The present paper keeps pronoun as one sub-category.

The DP hypothesis as foil. Abney 1987 uses the same `\term{determinative}`-`\term{modal}` analogy to argue for D-headedness. The split is whether modals head a separate functional category Infl or are a sub-cluster of V. Chomsky 2020 has retracted the DP hypothesis; Bruening 2020 and Pullum & Miller 2022 give the modern case for N-headedness.

### §6 Sub-cluster combinatorics (~600 words)
One residual phenomenon: the modifier-selection asymmetry. Determinatives take AdvP modifiers (`\mention{almost every}`, `\mention{hardly any}`); common nouns take AdjP modifiers (`\mention{a genuine professional}`). The asymmetry is sub-cluster-specific and consistent with PHP 2010: 13-14, which treats determinatives that alternate between Det and Mod functions (`\mention{few doctors}` vs `\mention{the few doctors}`) as the same lexeme in two functions.

Reynolds 2021's energy-distance k-groups result (93% correspondence with CGEL's categorisation of determinatives and pronouns) confirms sub-cluster distinctness empirically. The supercategory claim is at a higher level and isn't threatened by sub-cluster distance.

The stacking restriction is functional, not categorial: one Determiner function per NP is consistent with multiple determinative-category items per NP (`\mention{the many people}`, with `\mention{the}` as Det and `\mention{many}` as Mod).

### §7 Conclusion (~400 words)
The fourfold Noun extends the dissolve-Det tradition with a specific architectural commitment, parallels the established treatment of auxiliaries as verbs, and simplifies two pieces of CGEL Ch 5 machinery (fusion of functions, the disjunctive determiner-slot filler). Sub-cluster distinctions are preserved at the level the empirical work shows them; the supercategory claim is at the level of NP projection and external distribution. Cross-linguistic generalisation is left for separate work.

## Notes → section mapping

| Section | Source notes |
|---------|--------------|
| §1 | `grist.md`, `prior-art-search.md` (framing) |
| §2 | `prior-work-consolidation.md`, `prior-art-search.md` (aux-as-V); paradigm split as inline example |
| §3 | `diagnostic-table.md` (criterion + Table 1), `phase3-phenomena-reads.md` (i for §3.1, iii for §3.2) |
| §4 | `phase3-phenomena-reads.md` (steelman) |
| §5 | `phase2a-differentiations.md`, `objection-matrix.md`, `abney-foil.md` |
| §6 | `phase3-phenomena-reads.md` (ii, iv), `prior-work-consolidation.md` (Reynolds 2021), `reynolds2026-close-read.md` |
| §7 | synthesis |

## Figures and tables

1. **Figure 1** (in §1 or §3). Tree of the fourfold Noun taxonomy. Annotation: cardinals span three sub-clusters per Reynolds 2026.
2. **Table 1** (in §3, after §3.1). Four-way diagnostic showing all sub-categories satisfy the membership criterion under the §3.1 reanalysis. From `notes/diagnostic-table.md`.
3. **Table 2** (in §5). Compressed comparison of nearby proposals from `notes/objection-matrix.md` Table B.

(§2 has no table; the Stage A paradigm split is illustrated as a numbered linguistic example.)

## Open questions and risks

- Title. "Determinatives as nouns" is programmatic. Revisit once draft exists.
- Length. If §3 runs long, cut §6 further (push to footnote).
- Lyons 1999 is a DP-hypothesis defender. Use his diachronic and typological observations only, not his framework.
- Glossa vs ELL. Decide after §3 draft.

## Drafting sequence

Per Brett's review:

1. §3.1 and §3.2 first (the central empirical case)
2. §3 criterion + Table 1 — state the criterion and write the diagnostic table to fit what §3.1 actually establishes
3. §4 articles (compact answer)
4. §6 sub-cluster combinatorics
5. §5 nearby proposals (compressed, after positive case is built)
6. §1 introduction (preview reflects the actual draft)
7. §7 conclusion
8. Abstract (last)
