# -*- coding: utf-8 -*-
# Part 1: front-matter, sec:intro
# Tuple order: (id, section_label, expression, construction, status, evidence_type, quote, condition, note)

CLAIMS = [

# ---------------- front-matter ----------------
("fm-001", "front-matter", "quantificational common nouns",
 "complement patterns, number transparency, and restricted dependents shared with determinatives",
 "licensed", "authors_analysis",
 r"they share complement patterns, number transparency, and restricted dependents with parts of the determinative inventory",
 "", "Abstract summary of the nominal connection developed in the body."),

("fm-002", "front-matter", "four gradable quantifiers",
 "grade inflection, degree modification, and comparative complementation",
 "licensed", "authors_analysis",
 r"The strongest adjectival counterweight connects grade, degree modification, and comparative complementation in four quantifiers.",
 "", "Abstract statement of the adjectival profile."),

("fm-003", "front-matter", r"\mention{some}",
 r"dependent determiner use in \mention{take some apples} and independent use in \mention{take some}",
 "licensed", "authors_analysis",
 r"In \mention{take some apples} and \mention{take some}, \mention{some} belongs to the same category.",
 "", "Same lexical category asserted for both uses."),

("fm-004", "front-matter", "articles",
 "membership of the determinative grouping despite restricted occurrence",
 "conditional", "authors_analysis",
 r"Restricted articles belong to the grouping through their integration into the determinative system.",
 "Inclusion rests on integration into the determinative system rather than on independent argument use.", ""),

("fm-005", "front-matter", "independent determinative expressions",
 "ordinary Head relations within NP rather than determiner-Head fusion",
 "licensed", "authors_analysis",
 r"For the independent use, I favour ordinary Head relations within the NP, rather than \textit{CGEL}'s fusion of determiner and Head functions on one constituent.",
 "", ""),

# ---------------- sec:intro ----------------
("int-001", "sec:intro", r"\mention{some}",
 r"determiner function of its phrase before \mention{apples}",
 "licensed", "constructed_illustration",
 r"Before \mention{apples}, its phrase functions as determiner",
 "", ""),

("int-002", "sec:intro", r"\mention{some}",
 r"object function of the whole expression in \mention{take some}",
 "licensed", "constructed_illustration",
 r"without \mention{apples}, the whole expression functions as object",
 "", ""),

("int-003", "sec:intro", r"independent \mention{some}",
 r"partitive dependent, as in \mention{some of the wine}",
 "licensed", "constructed_illustration",
 r"An independent expression can still have dependents of its own, as in \mention{some of the wine}, and rely on context for its interpretation.",
 "", ""),

("int-004", "sec:intro", r"DP headed by independent \mention{some}",
 "joint determiner and Head functions (fusion of functions) in NP",
 "licensed", "cgel_described",
 r"In \textit{CGEL}, the determinative phrase (DP) headed by independent \mention{some} jointly fills determiner and Head, a \term{fusion of functions}",
 "", "Reported as CGEL's analysis, pp. 410-412."),

("int-005", "sec:intro", r"independent \mention{some}",
 "ordinary Head of a nominal (Nom) which heads NP",
 "licensed", "authors_analysis",
 r"The alternative has \mention{some} head a nominal (Nom) directly, with Nom heading NP.",
 "", ""),

("int-006", "sec:intro", r"\mention{the rich}",
 "Mod--Head fusion",
 "licensed", "authors_analysis",
 r"The proposal retains fusion elsewhere, including Mod--Head fusion in \mention{the rich}.",
 "", "Fusion retained for adjectives under the proposal."),

("int-007", "sec:intro", r"\mention{Kim's}",
 "determiner function of an NP within a larger NP",
 "licensed", "constructed_illustration",
 r"An NP can function as determiner, as in \mention{\underline{Kim's} book}",
 "", "Supported by citation to Payne and to Pullum and Miller rather than to CGEL."),

("int-008", "sec:intro", r"\mention{many}",
 "modifier function of a determinative-headed phrase within NP",
 "licensed", "constructed_illustration",
 r"a determinative-headed phrase can function as modifier, as in \mention{the \underline{many} people}",
 "", ""),

("int-009", "sec:intro", r"\mention{some apples}",
 "noun-headed NP rather than D-headed DP",
 "licensed", "authors_analysis",
 r"I retain noun-headed NPs and reject the DP analysis for English",
 "", "Abney's DP hypothesis, under which D heads such expressions, is rejected for English."),

("int-010", "sec:intro", r"\mention{every}",
 r"determiner before a singular count nominal, as in \mention{every apple}",
 "licensed", "constructed_illustration",
 r"\mention{Every apple} is grammatical",
 "", ""),

("int-011", "sec:intro", r"\mention{some}",
 r"independent object, as in \mention{I'll take some}",
 "licensed", "constructed_illustration",
 r"unlike \mention{some} in \mention{I'll take some}",
 "", ""),

("int-012", "sec:intro", r"\mention{every}",
 "independent (object) use without a following nominal",
 "excluded", "constructed_ungrammatical",
 r"\mention{every} can't occur independently in \ungram{\mention{I'll take every}}",
 "", "Marked ungrammatical in the manuscript."),

("int-013", "sec:intro", r"\mention{apples}",
 r"ultimate lexical head of \mention{some apples} under all four accounts",
 "licensed", "authors_analysis",
 r"All keep \mention{apples} as the ultimate lexical head of \mention{some apples}.",
 "", "Table caption for the four-way comparison."),

("int-014", "sec:intro", r"independent \mention{some}",
 "Head through nominal projection under D-noun with ordinary Head",
 "licensed", "authors_analysis",
 r"Ordinary Head through nominal projection",
 "", "Row of the four-account table."),

("int-015", "sec:intro", r"independent \mention{some}",
 "ordinary Head licensed for both Noun and D under separate D",
 "licensed", "authors_analysis",
 r"Ordinary Head, licensed for both Noun and D",
 "", "Row of the four-account table."),

("int-016", "sec:intro", r"independent \mention{some}",
 "joint determiner and Head functions under separate D with fusion",
 "licensed", "authors_analysis",
 r"Separate D, fused Head & A primary category alongside Noun & Joint determiner and Head functions",
 "", "Row of the four-account table."),

("int-017", "sec:intro", r"independent \mention{some}",
 "joint determiner and Head functions under D-noun with fusion",
 "licensed", "authors_analysis",
 r"D-noun, fused Head & A subcategory of Noun & Joint determiner and Head functions",
 "", "Row of the four-account table."),

("int-018", "sec:intro", "the whole independent determinative expression",
 "NP status under both Head analyses",
 "licensed", "authors_analysis",
 r"Both Head analyses give the whole independent expression NP status.",
 "", ""),

("int-019", "sec:intro", "words of category D",
 "NP projection in the separate-D ordinary-Head implementation",
 "licensed", "authors_analysis",
 r"In the separate-D ordinary-Head implementation, words of category D project NP",
 "", ""),

("int-020", "sec:intro", "pronouns",
 "NP functions supporting inclusion within Noun",
 "licensed", "cgel_described",
 r"\textit{CGEL} already includes pronouns within Noun on the basis of their phrases' functions, despite differences from common and proper nouns in inflection and dependents",
 "", "Cited as precedent for a broad category with internally divergent members."),
]
