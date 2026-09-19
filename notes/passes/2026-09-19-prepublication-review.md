# Pre-publication source review

The introduction and conclusion consistently describe the paper now on the page. Keep both. The sequential read supports the present section order, and I found no numerical drift in the checked counts and saved results. The repairs below concern local precision, evidence descriptions, and supplement consistency. They don't require another reorganization or new analyses.

Reviewed directly by GPT-6 (Astra): the complete main source in order, the five supplement wrappers, and the source files behind the numerical claims. The [baseline](2026-09-19-prepublication-baseline.json) identifies the versions reviewed. The [verification record](2026-09-19-prepublication-checks.json) contains recomputed counts, ranges, hashes, and citation-key results. No source changes or PDF work have been made during this review. The final proofreading sweep follows the accepted repairs.

## Introduction and conclusion, paired with each section

Each cell below reports a separate comparison, rather than relying on the paper's general consistency.

| Section | Paired with the introduction | Paired with the conclusion |
|---|---|---|
| §2: Grounds for a broader Noun category | Consistent. Supplies the promised taxonomic argument through nominal and adjectival comparisons, without requiring ordinary Head as a premise. | Consistent. The conclusion accurately gives quantificational common nouns the strongest positive role and gives the gradable four's adjectival profile weight. Its wording “parts of the determinative inventory” correctly limits the shared profile. |
| §3: Restricted members and scope | Consistent. Completes the promised inclusion of articles and other restricted members; distinguishes lexical membership, construction, and form selection. | Consistent. System integration supports article membership; *no/none* keeps its restrictions; peripheral *a* and predeterminer *many* support the stated decomposition. |
| §4: Ordinary Head, fusion, and attachment | Consistent. Takes up the independently announced structural choice after the taxonomy has been argued for. Both alternatives give the complete independent expression NP status. | Consistent. Establishes the word–Nom–NP chain and compares it with the fused structures. The conclusion does not claim that fusion denies NP status or that nounhood logically entails ordinary Head. |
| §5: Four implementations and economy | Consistent. Supplies the promised matched fragment and coverage comparison, including both taxonomies with both Head analyses. | Consistent. Explicitly admits that the inherited-feature alternative can express the shared nominal domain. The conclusion makes no strict description-length claim. |
| §6: Consequences and taxonomic choices | Consistent. Delivers the three-input secondary-use schema and the separately announced coordinate-versus-nested comparison. | Consistent. Names, compounds, and cardinals are exactly the three inputs summarized. Coordinate rank remains a further preference; the limited matrix cannot establish taxonomic rank or superordinate Noun. |
| Appendix: Earlier accounts | Consistent. Substantiates the introduction's qualified novelty claim by distinguishing scope and representational level. | Consistent. The conclusion claims the present grouping and analysis without denying the earlier article–pronoun connections or collapsing underlying structure into surface taxonomy. |

**Introduction ↔ conclusion:** consistent. The two independent commitments remain distinct, their mutual support is stated at the same strength, and coordinate rank remains a further choice. The title and abstract also fit the body. The headings now present the argument in its working order.

The suspected matrix tension is not a defect. The published study places the articles inside its determinative cluster; *a*, *the*, and *every* also remain in that cluster in all seven saved best-objective fits. Variation in the overall clustering does not contradict this specific membership claim. Keep §3.1's article claim and §6.2's limitations.

## Proposed repairs

### 1. State the agreement rate as a query proportion

In §2.1, “after *each of the* with a plural noun in about a third” is stronger than the evidence. The footnote already acknowledges that some counted verbs agree with another head; the saved readings identify this problem directly. The arithmetic, 73/(151+73), is correct, but it isn't a verified agreement rate. The *each of them* figures are also counts for the specified queries, rather than all occurrences of the phrase.

Replace the two-rate sentence with:

> Plural agreement after *each of them* is well attested; plural verb forms account for about a sixth of the relevant COCA query hits. Plural agreement also occurs after *each of the* with a plural noun, including in edited prose.

Keep the counts, examples, and caveat in the footnote. This preserves the usage evidence and the grammatical distinction between variation with singular *each* and number-neutral *some*.

### 2. Keep phrase level and lexical category distinct

In §2.4, replace “Fused-head adjective phrases (AdjPs) fill the same positions” with:

> NPs containing fused-head adjective phrases (AdjPs) fill the same positions.

The displayed subject, object, and preposition-complement positions are occupied by NPs, including *the rich*. The sentence following the present wording already recognizes that distinction.

In §5.2, `Cat(h)` is defined for a word's primary lexical category, but later `Cat(n)=Nom` applies it to a phrase. Declare “Let *n* be the additional Nom in the Mod–Head configuration” in the introducing prose and remove `Cat(n)=Nom` from the formula. Keep all Head, Det, and Mod relations.

Clarify the third structural condition as:

> Third, peripheral modification forms an NP with the modifier as dependent and another NP as Head, as in Figure [every].

In the coverage supplement's primitives table, call the row “Category condition on words directly heading Nom” and change I3 from “N or D” to “N”. Add that I3's D heads a DP, which fills Head in the further nominal structure. I2 retains “N or D”. This aligns the table with the main fragment and figures.

### 3. Remove conversion from the proper-name coverage entry

`analysis/coverage-audit.json` assigns `secondary_use_rule+conversion_rule` to `secondary|proper` under I2 and I3. The main text correctly says that proper names already belong to Noun. Change those two entries to `secondary_use_rule`; compounds and cardinals retain conversion under the stated separate-D implementations. Regenerate the coverage output. The cell codes and the inventory of distinct conditions remain unchanged, since conversion is still required elsewhere.

### 4. Make two local scopes explicit

In §2.6, “the four carry the partitive, transparency, and dependent patterns” can suggest that all four plain forms have *some*'s number transparency. §2.1 establishes that specific connection for *lot/some*. Replace the list with:

> the four carry the partitive, restricted-dependent, and degree-use connections with quantificational common nouns as well.

In §3.2, “No adjectival property remains: neither word …” follows a paragraph discussing *many*, *such*, and *what*. Name the intended pair:

> Neither degree *such* nor exclamative *what* has grade or degree modification …

Retain the existing examples and the following predicative-use clause. This prevents the sentence from accidentally denying *many*'s grade. Give *how long a bridge* at the first mention of “Big Mess” in §2.7, using the example already supplied in §3.2.

### 5. Match the corpus supplement to the saved batches

The predicative records have correct totals but overly narrow descriptions. The saved 45-entry batch includes *became/become too much to*; the 46-entry batch includes forms of *seem*, both *too/so*, and both *much/little*. The 15-entry *seem … a lot to* batch likewise contains several verb forms and includes *to me*. Describe these as supplied batches and broaden the labels accordingly. The original exact query strings for the first 81- and 23-entry batches weren't recorded; don't present their descriptive labels as exact queries. Keep the examples, totals, and unscreened-batch qualification.

The exclusion table describes all 22,938 *so* List hits as discourse uses, although their KWIC contexts weren't saved. In `analysis/exclusion-checks.json`, change that part of the Hits field to:

> 22,938 (List) for *so*; contexts not retained for review

Keep the seven read *very* lines distinct from that List total, and limit the screened-result description accordingly. Regenerate the table. No new search is needed.

### 6. Restore the remaining attestation's source pointer

§2.4 still uses *I need something reliable and good looking*. The corpus supplement supplies its exact CGELBank sentence ID and source link, but the main sentence has no source pointer. The introduction says unsourced examples are constructed.

Add a short footnote pointing to the CGELBank attestation documented in the corpus supplement. Update the analysis README's current description from two retained attestations to one; preserve its September 9 historical account as historical. The removed Honda example stays removed.

### 7. Finish the small documentation corrections

- Give the claim-register PDF metadata its actual title; it currently says “Quantificational controls”.
- In the claim-register method, say “the 51 keyed claims paired with census claims”; 44/51 is the saved paired comparison, while five further keyed claims have no pairing. The values remain unchanged.
- Update the exclusion-source pointers for *every* and *no of the* to their present sections, and the typicality source note for *such/what* from §3.1 to §3.2.

## Verification and limits

The numerical checks recovered the census arithmetic (658 original, 9 withdrawn, 649 live, 426 retained, 440 claim–lexeme pairs), the paired-key and TypeSafe comparisons (44/51 and 235/250), the 103-cell coverage totals and sensitivity recodings, the matrix's 138 forms and 155/232 features with the exact lineage differences, the saved clustering ranges and selected-fit agreement, and the CGELBank counts (220 trees, 3,390 lexical nodes, 387 D tokens). The tables checked against those records agree. Corpus totals likewise match their saved logs and readings; the defects above concern their descriptions and denominators.

All 32 citation keys used across the six live documents resolve without duplicate active entries or missing basic fields. This is a key-integrity check, not a new authoritative-source audit of all references. The earlier source audits remain in place; no new citations are proposed. No analysis was rerun and no model was asked to recode the data. Proofreading and source-level house style remain the final step after these decisions; minor PDF defects remain outside this round.

## Completion

The proposed repairs were applied after Roughdraft review. The final source proofread is recorded in [the proofreading review](2026-09-19-prepublication-proofread.md), including Brett’s instruction to split only egregiously long paragraphs. Only the two supplement methods paragraphs over 200 words were split. All 649 live census quotations now match the manuscript; all three generated-table checks and `git diff --check` pass. The introduction and conclusion are unchanged. Numerical totals and coverage codes are unchanged. PDF work remains deferred.
