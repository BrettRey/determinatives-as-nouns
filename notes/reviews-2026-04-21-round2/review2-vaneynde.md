# Review of "Determinatives as nouns"

**Reviewer:** Frank Van Eynde (KU Leuven)
**Journal:** *English Language and Linguistics*
**Recommendation:** Major revision

---

## Summary of the paper's claim

The author argues that English determinatives (*the, a, this, some, every*, etc.) are a fourth sub-category of the lexical category Noun, alongside common nouns, proper nouns, and pronouns. The argument keeps CGEL's category/function distinction and the N-headed NP (rejecting Abney's DP). It runs in two stages: (i) partitives (*some of mine*) show that determinatives can head matrix NPs; (ii) simple cases (*Some left*; *I'll take some*) are reanalysed as ordinary head-of-NP function rather than fusion of Det and Head, on three discriminators (paradigm productivity, structural saturation, internal modification). Two simplifications follow: the noun-headed Det disjunction (DP-or-genitive-NP) collapses to NP, and most CGEL fused-head cases drop out. Articles are treated as defective members of the determinative sub-category.

I'll start where I agree, then turn to what needs work.

---

## 1. What the paper gets right

Three things the author has done well, and which I want to acknowledge before pushing back.

**(a) The Pullum & Wilson (1977) precedent is well used.** The auxiliaries-as-verbs analogy is the right reference point for what the paper is trying to do. CGEL's absorption of AUX into V is a clean case of a closed functional class being incorporated into an open lexical category without losing the closed class's distinctive sub-cluster profile. The author is right that the architectural move is independently motivated and the paper isn't asking the framework to do anything it hasn't already done. This is exactly the precedent I cite in Van Eynde (2003) for the same reason, and I'm pleased to see it foregrounded.

**(b) The two-stage architecture (partitives vs. simple cases) is the right move.** Separating the headhood question from the fusion question is genuinely useful. CGEL's fused-head analysis covers two empirically separable sets: the partitives, where the determinative is unambiguously the pivot, and the simple anaphoric cases, where the analysis is contested. By making the partitive argument first and independently of the fusion question, §3 isolates a result that doesn't depend on resolving the fusion controversy. I'd accept the partitive headhood point on its own, even if the §3.2 reanalysis didn't go through.

**(c) The three discriminators in §3.1 are specific and falsifiable.** Productivity (broad within determinatives, narrow within Mod-Head adjectives), saturation (*Some left* vs. *\*Rich get richer*), and internal modification (*the lucky few*) target three distinct alternative analyses, not one composite alternative. This is much better than the usual rhetorical move of asserting that fused-head is "stipulative" without specifying what's better. I learned something from the internal-modification argument in particular: the linear-position argument against silent-N analyses is stronger than I'd appreciated.

I should also note that the author is explicit and careful about Spinillo, Hudson, Postal, and Anderson (Table 2). The taxonomy of nearby proposals is honest about where the present paper agrees and disagrees with each.

---

## 2. Substantive concerns

Three issues, in declining order of severity.

### 2.1 Cross-linguistic evidence is sidelined, not engaged

The paper's scope declaration ("synchronic English") appears in the abstract and is repeated three times (§1, §4 close, §7 close). I take the disclaimer in good faith. But the paper rejects my A-side split for English (§5: "English lacks the rich prenominal agreement morphology that drives Van Eynde's split") and that rejection has cross-linguistic consequences the author doesn't engage with.

My argument in Van Eynde (2003) is that determiners as a primary category fail because the items the tradition has lumped together pattern with two different categories: some inflect adjectivally (Italian *quel*, *quello*, *quella*, *quei*, *quegli*, *quelle*, with full gender/number concord matching adjectives, not nouns; Dutch *deze/dit*, *die/dat*) and some pattern nominally. The distributional evidence is morphological: where adjectives show agreement that nouns don't, the relevant determiner-class items pattern with adjectives. This is not a stipulation; it's the same kind of distributional argument the present paper uses for English.

The author's rejoinder is that English lacks the relevant morphology, so the split doesn't apply. Fine. But two points need to be made explicit:

**(i) The English case can't be sealed off from cross-linguistic evidence.** If the same items (demonstratives, possessives, *some/all/every*) split categorially in Italian and Dutch on agreement evidence, then either (a) the cross-linguistic class is a heterogeneous label and English happens not to expose the heterogeneity, or (b) the English class is genuinely uniform and the Italian/Dutch agreement patterns are surface morphology orthogonal to category. The author needs to take a position. The current treatment leaves the cross-linguistic data as a problem for "separate work" while making a claim that has obvious cross-linguistic implications: if determinatives are nouns in English, what are the Italian *quel*-series in *quei libri belli*?

**(ii) The §3.1 discriminators don't survive the cross-linguistic move cleanly.** Take the productivity discriminator. In Italian, a substantial subset of the determiner-class items inflect with full adjectival concord (4-form paradigm: M.SG, M.PL, F.SG, F.PL, plus elision allomorphs). They appear as fused heads as productively as English *some* does (*Quelli sono i miei* "those are mine"). On the productivity discriminator, that's a clean win for nounhood — but on agreement morphology, the same items are unambiguously adjectival in Romance terms. The discriminator and the agreement evidence point in opposite directions for the same items. Which wins, and why?

The honest answer might be: in English, the agreement evidence isn't available, so the productivity/saturation/modification cluster carries the categorial weight; in Italian, the agreement evidence is available and trumps the productivity facts. If that's the position, say so. But it would have implications for what the discriminators are actually diagnosing — perhaps not nounhood as such, but a property that correlates with nounhood when agreement morphology is absent and with adjectivehood when it isn't.

I don't expect the paper to solve the cross-linguistic problem. I do expect it to engage with the fact that the discriminators it relies on may be language-particular signals of a more general property, not language-neutral diagnostics for noun categoryhood.

### 2.2 The §3.2 NP:Det uniformity claim under HPSG selection mechanisms

The paper claims (§3.2) that the noun-headed Det disjunction (DP or genitive-NP) collapses to NP under the proposal, and that this is a "concrete" simplification rather than a notational one. The argument has three sub-claims (definiteness contribution, one-Det-per-NP, fused-head licensing) and ends with the line that "the head N of the outer NP still selects its Det-functioning NP by features (definite versus indefinite, count versus non-count, number agreement)" (line 180).

This is the place where I want to push hardest, because the simplification looks much smaller once you specify the selection mechanism.

**The collapse is at the phrasal label, but the selection feature still needs the disjunction.** Suppose the head N of the outer NP has a SPR (or DET) feature that selects its Det-functioning NP. The selection has to discriminate among:

- definite-article NPs (*the*-headed)
- indefinite-article NPs (*a*-headed)
- demonstrative NPs (*this/that*-headed)
- quantifier NPs (*some/every/each/all/most*-headed)
- genitive pronoun NPs (*my*-headed, with case-marked head)
- genitive common-noun NPs (*Kim's*-headed, with phrasal -*s*)
- numeral NPs (*three*-headed)
- PPs (*about twenty*)

In CGEL the categorial label DP vs NP-genitive carried part of this discrimination. Under the proposal, the label is uniformly NP, and the discrimination has to be done by features on the head N (or head sub-cluster). So the selection feature has to encode, at minimum: SUB-CATEGORY (determinative vs. common vs. proper vs. pronoun), CASE (genitive vs. plain) for the noun-headed cases, and DEFINITENESS (definite, indefinite, demonstrative, quantificational, etc.). That's a richer feature bundle on N than CGEL needs, because CGEL gets some of the discrimination free from the categorial label.

The author may respond: "Yes, but the feature bundle is needed anyway, regardless of whether the phrase is labelled DP or NP." That's true for some of the features (definiteness has to be computed from the head either way). But the categorial split DP vs. NP-genitive is doing real work in CGEL that NP-as-uniform-label has to recover via features. The simplification at the phrasal level reintroduces a disjunction at the feature level. Whether the trade is favourable depends on which level you think the disjunction belongs at — and the paper doesn't argue for the feature-level placement, it just asserts that the simplification is "concrete."

In HPSG terms, what was a SPR specification of `[SPR <DP[…]> ∨ <NP[CASE gen]>]` becomes `[SPR <NP[HEAD-FEATURES …]>]`. The HEAD-FEATURES constraint has to encode what the categorial split previously encoded. The disjunction hasn't disappeared; it's been pushed into the feature structure. This may still be a win — feature-level disjunction is often cleaner than category-level disjunction — but it's not a free lunch, and the paper presents it as one.

**A concrete request:** §3.2 should specify the SPR (or equivalent) feature-bundle the head N selects under the proposal, and compare it to the CGEL specification it replaces. If the feature-level disjunction is genuinely simpler, show it. If it's roughly equivalent in complexity, acknowledge that the gain is in placement (features vs. categories) rather than in eliminating the disjunction. The current §3.2 ("the parallelism isn't coincidental ... derives it from a single phrase type", line 182) overstates the case.

A related point: the §3.2 claim about "definiteness contribution" is empirically right but theoretically thin. Both *the book* and *Kim's book* are definite. This isn't because both are NPs; it's because both have a head that contributes a [+def] feature (the article in one, the genitive marking in the other). The structural sameness (both are NPs) doesn't predict the definiteness sameness — a uniform-NP structure could just as well admit indefinite genitive NPs (which do exist in some analyses, e.g., predicative *a friend of John's*). The definiteness facts need a feature-level account regardless of the phrasal label.

### 2.3 The Italian/Dutch determiners and the §3.1 discriminators

Picking up from §2.1 above, but with concrete cases.

**Productivity:** Italian *questo* (this) inflects as a 4-form adjectival paradigm and serves as a fused head productively (*Questi sono i migliori* "these are the best"). Dutch *deze/dit* same (*Deze zijn van mij* "these are mine"). Productivity discriminator: nounhood. Agreement morphology: adjectivehood. Conflict.

**Saturation:** Italian *Quelli sono partiti* "Those left" is a fully saturated NP. *I poveri sono partiti* "the poor left" requires the article *i*, parallel to *the rich* in English. Saturation discriminator: nounhood for *quelli*, Mod-Head fusion for *poveri*. So the saturation cut works in Italian roughly as in English. But in Italian, *quelli* also exhibits adjectival agreement morphology — and *poveri* does too. The saturation cut and the agreement cut don't pick out the same partition.

**Internal modification:** *I pochi fortunati* "the lucky few" — same structure as English. *Pochi* is the head, *fortunati* is the modifier. But *pochi* shows adjectival concord (M.PL agreement with *fortunati*, with a covert plural masculine human referent). On the present paper's logic, this is internal modification of the determinative-noun *pochi*. On the agreement evidence, *pochi* is adjectival. Same conflict.

The point isn't that the discriminators are wrong. It's that they're not English-specific in their applicability — Italian has the same patterns — but the conclusions they support are language-particular. In English, where adjectives don't show concord, the discriminators converge on nounhood. In Italian, where adjectives do show concord, the discriminators support nounhood and the agreement evidence supports adjectivehood. Either the discriminators are imperfect proxies for nounhood (and we shouldn't rely on them in English either, since English doesn't expose the disconfirming evidence), or the conclusion is genuinely language-particular (in which case the §3.1 argument is weaker than it looks).

This is the place where Allegranza (1998) and the wider HPSG nominal literature would be useful. Allegranza's analysis of Italian determiners as functors of varying syntactic category is one model for how the same item can occupy a determiner-like function from different categorial bases. The paper doesn't have to adopt Allegranza's framework, but it should acknowledge that the question "what category is *quel*?" has been answered in HPSG in ways that bear on the English question.

---

## 3. Smaller points

**§3.1, structural saturation:** The contrast between *Some left* and *\*Rich get richer* is good but slightly overdrawn. *Rich* on a generic-bare-plural reading isn't grammatical (correct). But on a count-noun reading with a covert plural, it's also not grammatical, which is the parallel case to *some*. The discriminator works, but the explanation is that *rich* requires a determiner because it's not lexically a noun and can't head an NP without one — whereas *some* can. Make sure the comparison is between like uses (NP-as-argument), not between mass-generic *rich* and count-anaphoric *some*.

**§3.1, internal modification, lines 113-120:** The argument against null-head and silent-NP analyses is good but the exposition is dense. Two paragraphs of prose argue that the AdjP attachment target has to be the determinative, but the structural diagram or a tree fragment would carry the point more economically. Consider a small tree.

**§4, line 198, *every*:** The defence of *every* as a quantifier rather than an article is convincing for me. But the parenthetical "*Every of the students is bad*" should be *"\*Every of the students*" with a clearer judgement. As stated, the example sentence is a complete clause with *every of the students* as subject and a defective copula; the asterisk is on the partitive *every of the students*, not on the whole clause. Clarify.

**Table 1, "via fusion" for Adjective row:** The table puts adjective Mod-Head as "via fusion." Under the present paper's reanalysis, fusion is preserved for the Mod-Head residue. So the row is correct under the proposal. But the table caption ("does not satisfy the criterion") is slightly misleading — it suggests adjectives fail the criterion in some general sense, when really they fail it because their Head function is via fusion under the present paper's narrowed application of fusion. Tighten the caption.

**§5, Van Eynde 2003 row in Table 2:** "Det split across A and N" is accurate but compressed. The split isn't symmetric: the A-side captures items that show adjectival inflection in Romance/Germanic; the N-side captures items that don't. For a CGEL-style English audience, a sentence in the prose explaining what evidence drives the split would help readers who don't know the HPSG literature.

**§5, line 236:** "English lacks the rich prenominal agreement morphology that drives Van Eynde's split, and the article-specific move doesn't generalize to the demonstratives and quantifiers." The first clause is right; the second is right about Herslund. But "the article-specific move doesn't generalize" is doing more rhetorical work than the cited material can support. Some article-as-pronoun analyses do generalize to demonstratives in their original sources. Be precise about which version of Herslund you're rejecting.

**§6, sub-cluster differences:** The reynolds2021 result (93% correspondence with CGEL sub-categories on energy-distance clustering) is described as confirming the sub-cluster distinctness. It's strong evidence for the distinctness. But it's evidence that pulls in two directions: the same result was originally framed as evidence that pronouns and determinatives are categorially distinct (separate primary categories). The paper should acknowledge that the same data has been read against the present proposal, and explain why the sub-category-within-Noun reading is preferred. This isn't fatal — distributional distance is compatible with both readings — but the rhetoric ("doesn't dispute that distinctness ... locates it at the sub-category level") is too smooth.

**§6, cardinal numerals:** The cardinals discussion is interesting and the simplification (cross-category becomes cross-sub-category) is genuine. But the citation \citet{reynolds2026numerals} appears with a lowercase "c" (\citet rather than \textcite), inconsistent with house style elsewhere in the paper. Trivial but worth fixing.

---

## 4. What I'd want to see in revision

In order:

1. **Engage Italian/Dutch directly in §3.1 or §5.** A subsection on cross-linguistic implications of the discriminators. Either argue that the discriminators are language-particular and that's fine, or argue that the agreement evidence in Romance/Germanic is orthogonal to category. The current "for separate work" disclaimer doesn't do enough.

2. **Specify the SPR/Det selection feature in §3.2.** Show that the simplification at the phrasal level isn't paid for by complexity at the feature level. If it is paid for, acknowledge the trade.

3. **Cite Allegranza (1998) and the wider HPSG nominal literature.** Not because the paper has to adopt the HPSG framework, but because the question of how the same item can fill determiner function from different categorial bases has been engaged seriously, and the paper currently treats my 2003 paper as the only HPSG point of contact.

4. **Soften §3.2's "concrete simplification" claim** to match what's actually shown. The paper has earned a phrasal-uniformity claim; it hasn't earned an end-of-disjunction claim.

5. **Tighten the *every* and *the rich* discussions** as noted in §3 above.

I'd be happy to see this paper in print after these revisions. The two-stage architecture is genuinely good, the discriminators are an advance over the prior literature, and the Pullum & Wilson precedent is well used. The cross-linguistic and HPSG-selection issues need real engagement, not just a scope disclaimer — but the core claim is defensible if the paper does that work.

---

*Frank Van Eynde*
*KU Leuven*
