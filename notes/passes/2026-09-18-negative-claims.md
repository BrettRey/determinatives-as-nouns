# Negative claims, 18 September 2026

<!-- SUMMARY: every explicit and implicit negative in the manuscript at commit e3a5709 found and given one of the three outcomes; one novelty claim narrowed, two grammatical absences turned into judgments, one left open; inward search shown · status: applied · updated: 2026-09-18 -->

Procedure: the registry's `negative-claims-audit` entry. Explicit forms searched (`no one has`, `nobody has`, `has not been`, `there is no`, `the literature`, `remains unexplored`, `to my knowledge`, `the first to`, `novel`, `new here`, `unlike`, `no existing`, `no account`, `none of / shows`, `not attested`, `never`, `no such / pattern / adjectival / complex / corresponding`, `contains no`, `don't settle`, `doesn't apply / settle / determine / establish`, `neither`, `leaves open`, `haven't tested`, `predecessors`, `earlier accounts`) over the abstract and body; 38 sentences returned; each read for an implicit negative as well. The 9 September pass (`2026-09-09-sources-quotations-charity-negatives.md`) had found no literature-wide claim; the sentences below were added since.

## Inward search

Before anything outward, Brett's own literature was searched for any prior proposal of determinatives as a subcategory of Noun. Query over `literature/*.md`: the regex `determin(er|ative)s? … (sub-?class|sub-?categor|subtype|kind|species|type) of (noun|pronoun)`, its mirror, and `determin(er|ative)s? (are|as) (noun|pronoun)s`. Hits: Hudson 2000, 2004, 2010 (determiners as pronouns, pronouns a kind of noun; all cited and discussed in §6), Reynolds 2021 (mentions Hudson's nesting), and two false positives on "any kind of noun" (Chierchia in Rothstein 1998). `lit co-cited hudson2004determiners` returns Abney 1987, *CGEL*, Palmer 1924, Postal 1966, Spinillo 2000 and 2004, Van Eynde 2003, Payne and Huddleston 2007, all in the paper. Nothing in the corpus proposes the coordinate subcategory; no outward search was run, because the claim is narrowed below to the accounts the paper surveys rather than to the literature at large.

## The negatives and their outcomes

| Negative | Kind | Outcome |
|---|---|---|
| §1 "What's new here is the scope and the pairing: the full inventory ... one coordinate subcategory ... ordinary Head ... the four combinations" | Novelty over the literature at large (added this week) | **Narrowed**: "Relative to those accounts, what's new is ..." The accounts are the ones named in the same paragraph and in Appendix A. |
| §1 "Unlike *CGEL*, I include determinatives within Noun" | Claim about a named source | Stands; *CGEL* pp. 327–328 and Ch. 5 cited. |
| §1 *every*: "never stands as an ordinary fused Head" across 618 COCA and 164 NOW lines | Corpus absence | Stands as evidenced: queries, List counts, line counts, and the residue are in the footnote and under `corpus/exclusion_tests/`. |
| §2.7 Van Eynde "doesn't apply it" (his criterion, to English) | Claim about a named source | **Narrowed and checked**: his 2003 paper applies the inflection-and-agreement criterion to Italian and Dutch and cites English only for the MARKING contrast (possessives; *each* against *every*). Now reads "(he applies it to Italian and Dutch, and cites English only for the marking contrast)". |
| §3.1 *such*, *what*: "neither word has grade or degree modification, and exclamative *what* has no predicative use" | Grammatical absence with no evidence stated | **Evidenced as judgments**: starred forms added (\**sucher*, \**a very such mess*), which is the form §2.3's evidential paragraph gives a judgment. |
| §3.1 "no complex determinatives remain in this account" | Claim about the paper's own account | Stands; checkable against §3.1 and the audit's primitives table. |
| §4.2 *few would*: 82 of 94 lines with no set supplied | Corpus absence | Stands as evidenced: the reading and the screener's labels are both stated; lines under `corpus/independent_argument/`. |
| §4.5 "The articles, *every*, and the personal pronouns aren't attested in [the set-denoting use]" | Corpus absence with no search recorded; and doubtful for pronouns (*a he*, *the hes and shes*) | **Cut and restated**: "The articles and *every* have no such use (\**an every*); whether the personal pronouns do (*the hes and shes*) I leave open." No search was ever run for this; the *every* and article cases are judgments, and the pronoun case is now an open question rather than a negative. |
| §4.5 footnote "a judgment I haven't tested" (the post-head restrictor in the set-denoting use) | Marked gap | Stands; it is already the honest form. |
| §5.5 "a feature earns its place only by cross-cutting the categories, which in this fragment none does" | Claim about the fragment | Stands; checkable against the audit. |
| §6 "the study contains no common or proper nouns" (Reynolds 2021) | Claim about a named source | Stands; checked in the matrix audit against the input file. |
| Appendix "These predecessors challenge a fundamental article–pronoun separation but don't settle the full modern determinative inventory's surface taxonomy" | Claim about five named sources | Stands; each is characterized in Table 6 with its level, and the claim is about them, not the literature. |

The remaining sentences returned by the search are grammatical negations about examples (starred forms, "can't be the ultimate lexical head", "no corresponding singular–plural alternation") or method statements, not negative claims about coverage.

## What this pass does not establish

No outward search was run. The novelty claim as now worded is a claim about the accounts the paper names, and the inward search above is the search behind it. If a referee names a further prior proposal of determinatives as a coordinate noun subcategory, Appendix A's table is where it goes.
