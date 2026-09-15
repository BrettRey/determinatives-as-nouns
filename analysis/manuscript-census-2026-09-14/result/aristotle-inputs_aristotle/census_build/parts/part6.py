# -*- coding: utf-8 -*-
# Part 6: sec:head-relations, sec:saturation, sec:modification

MH_ROW1 = r"\mention{few survivors} & \mention{few}: Det; \mention{survivors}: Head & Same functions"
MH_ROW2 = r"Independent \mention{few} & \mention{few}: Det--Head & \mention{few}: Head"
MH_ROW3 = r"\mention{the few} & \mention{few}: Mod--Head & \mention{few}: Head"
MH_ROW4 = r"\mention{the lucky few} & \mention{few}: Mod--Head; \mention{lucky}: Mod & \mention{few}: Head; \mention{lucky}: Mod"
MH_ROW5 = r"\mention{the idle rich} & \mention{rich}: Mod--Head; \mention{idle}: Mod & Same fusion and modifier functions"

CLAIMS = [

# ---------------- sec:head-relations ----------------
("hr-001", "sec:head-relations", r"\mention{apples}",
 r"Head of Nom, which heads NP, in \mention{some apples}",
 "licensed", "authors_analysis",
 r"In \mention{some apples}, the word \mention{apples} heads Nom, and that Nom heads NP.",
 "", ""),

("hr-002", "sec:head-relations", r"\mention{red}",
 r"internal modifier within Nom, as in \mention{some red apples}",
 "licensed", "authors_analysis",
 r"The same arrangement permits an internal modifier, as in \mention{some red apples}, without making the determining phrase part of the Nom.",
 "", ""),

("hr-003", "sec:head-relations", r"\mention{some}",
 "ultimate lexical head of the independent expression, under both accounts",
 "licensed", "authors_analysis",
 r"Both accounts also have \mention{some} as the ultimate lexical head of independent \mention{some}.",
 "", ""),

("hr-004", "sec:head-relations", "determinatives",
 "heading the Nom--NP structure under D-noun",
 "licensed", "authors_analysis",
 r"Under D-noun, a determinative can head this Nom--NP structure too.",
 "", ""),

("hr-005", "sec:head-relations", r"\mention{apples}",
 r"ultimate head of the dependent expression \mention{some apples}",
 "licensed", "authors_analysis",
 r"The dependent expression still has \mention{apples} as its ultimate head.",
 "", ""),

("hr-006", "sec:head-relations", r"independent \mention{some}",
 "ordinary Head under D-noun",
 "licensed", "authors_analysis",
 r"Independent \mention{some} has ordinary Head under D-noun; in \textit{CGEL}, its DP jointly fills Det of NP and Head of Nom.",
 "", ""),

("hr-007", "sec:head-relations", r"DP headed by independent \mention{some}",
 "joint Det of NP and Head of Nom",
 "licensed", "cgel_described",
 r"Independent \mention{some} has ordinary Head under D-noun; in \textit{CGEL}, its DP jointly fills Det of NP and Head of Nom.",
 "", ""),

("hr-008", "sec:head-relations", r"\mention{some}",
 r"Head of D within DP filling Det in \mention{take some apples} (CGEL tree)",
 "licensed", "cgel_described",
 r"[{\synnode{Det}{DP}}",
 "", "Worked tree in Figure fig:some, CGEL dependent-use panel."),

("hr-009", "sec:head-relations", r"\mention{apples}",
 "Head N(common) of Nom in the object NP (both trees)",
 "licensed", "authors_analysis",
 r"[{\synnode{Head}{N\textsubscript{common}}}, head edge [\mention{apples}]]",
 "", "Worked tree in Figure fig:some."),

("hr-010", "sec:head-relations", r"\mention{some}",
 "Head N(D) of Nom within an NP filling Det (D-noun tree)",
 "licensed", "authors_analysis",
 r"[{\synnode{Head}{N\textsubscript{D}}}, head edge [\mention{some}]]",
 "", "Worked tree in Figure fig:some, D-noun dependent-use panel."),

("hr-011", "sec:head-relations", "the DP in the fusion diagram",
 "Det of NP and Head of Nom simultaneously",
 "licensed", "cgel_described",
 r"In the second diagram, DP fills Det of NP and Head of Nom.",
 "", "Figure caption."),

("hr-012", "sec:head-relations", r"\mention{some}",
 "the same nominal projection in Det and Obj uses under D-noun",
 "licensed", "authors_analysis",
 r"In the D-noun pair, \mention{some} has the same nominal projection in Det and Obj uses.",
 "", "Figure caption."),

("hr-013", "sec:head-relations", "subcategories of Noun",
 "inheritance of constraints stated for Noun",
 "conditional", "authors_analysis",
 r"\term{inheritance} applies constraints stated for Noun to its subcategories, subject to their lexical and constructional restrictions",
 "Subject to lexical and constructional restrictions.", ""),

("hr-014", "sec:head-relations", "a separate-D ordinary-Head grammar",
 "licensing the same Nom--NP structure by admitting both Noun and D",
 "licensed", "authors_analysis",
 r"A separate-D ordinary-Head grammar can license the same structure by admitting both Noun and D.",
 "", ""),

("hr-015", "sec:head-relations", r"\mention{Kim's}",
 r"Det in \mention{Kim's preferences}",
 "licensed", "authors_analysis",
 r"The genitive NP \mention{Kim's} already fills Det in \mention{Kim's preferences}",
 "", ""),

("hr-016", "sec:head-relations", r"\mention{almost ten}",
 r"plain determinative-headed NP as Det in \mention{almost ten apples}",
 "licensed", "authors_analysis",
 r"Plain determinative-headed NPs, such as \mention{almost ten} in \mention{almost ten apples}, then join genitives such as \mention{Kim's} and \mention{my}.",
 "", ""),

("hr-017", "sec:head-relations", r"\mention{preferences}",
 r"ultimate lexical head of \mention{Kim's preferences}",
 "licensed", "authors_analysis",
 r"The genitive NP \mention{Kim's} functions as determiner in the larger NP \mention{Kim's preferences}, whose ultimate lexical head is \mention{preferences}.",
 "", "Figure fig:genitive caption."),

# ---------------- sec:saturation ----------------
("sat-001", "sec:saturation", r"\mention{Some}",
 r"complete argument expression as subject, as in \mention{Some left}",
 "licensed", "constructed_illustration",
 r"\mention{Some left}, \mention{Many came}, and \mention{All agree} illustrate \term{syntactic completeness}",
 "A group of people must be under discussion.", ""),

("sat-002", "sec:saturation", r"\mention{Many}",
 r"complete argument expression as subject, as in \mention{Many came}",
 "licensed", "constructed_illustration",
 r"\mention{Some left}, \mention{Many came}, and \mention{All agree} illustrate \term{syntactic completeness}",
 "A group of people must be under discussion.", ""),

("sat-003", "sec:saturation", r"\mention{All}",
 r"complete argument expression as subject, as in \mention{All agree}",
 "licensed", "constructed_illustration",
 r"\mention{Some left}, \mention{Many came}, and \mention{All agree} illustrate \term{syntactic completeness}",
 "A group of people must be under discussion.", ""),

("sat-004", "sec:saturation", r"\mention{some}",
 r"object with contextually supplied domain, as in \mention{I'll take some}",
 "licensed", "constructed_illustration",
 r"In \mention{I'll take some}, the relevant substance or set may still be supplied by discourse or the situation.",
 "Interpretation supplied by discourse or situation.", ""),

("sat-005", "sec:saturation", r"\mention{both}",
 "independent object with an antecedent-supplied domain",
 "licensed", "retained_attestation",
 r"\mention{two different Honda models} supplies the domain for the independent object \mention{both}",
 "", "Attested web-review sentence from the English Web Treebank."),

("sat-006", "sec:saturation", r"\mention{both}",
 "independent object in the attested sentence",
 "licensed", "retained_attestation",
 r"\mention{Went there yesterday: we are trying to decide between two different Honda models, so we wanted to test-drive both back to back.}",
 "", "The attested example itself, verified in UD English EWT."),

("sat-007", "sec:saturation", r"\mention{Many are called, few are chosen}",
 "generalizing subject use without a previously uttered common-noun phrase",
 "licensed", "constructed_illustration",
 r"Generalizing expressions such as \mention{Many are called, few are chosen} and \mention{Enough is enough} need no previously uttered common-noun phrase.",
 "", ""),

("sat-008", "sec:saturation", r"\mention{Enough is enough}",
 "generalizing subject and predicative use without a previously uttered common-noun phrase",
 "licensed", "constructed_illustration",
 r"Generalizing expressions such as \mention{Many are called, few are chosen} and \mention{Enough is enough} need no previously uttered common-noun phrase.",
 "", ""),

("sat-009", "sec:saturation", r"generic pronoun \mention{one}",
 r"subject without a required overt antecedent, as in \mention{One shouldn't judge}",
 "licensed", "constructed_illustration",
 r"Generic pronoun \mention{one}, as in \mention{One shouldn't judge}, provides a parallel without a required overt antecedent.",
 "", ""),

("sat-010", "sec:saturation", r"\mention{She}",
 "NP headed by a nominal with no determiner",
 "licensed", "cgel_described",
 r"In \mention{She left} and \mention{Kim left}, \textit{CGEL} permits an NP headed by a nominal with no determiner.",
 "", ""),

("sat-011", "sec:saturation", r"\mention{Kim}",
 "NP headed by a nominal with no determiner",
 "licensed", "cgel_described",
 r"In \mention{She left} and \mention{Kim left}, \textit{CGEL} permits an NP headed by a nominal with no determiner.",
 "", ""),

("sat-012", "sec:saturation", r"\mention{Some left}",
 "NP headed by a determiner-less nominal",
 "licensed", "authors_analysis",
 r"Applying that structure to \mention{Some left} preserves the same division between a complete NP and its context-dependent reference.",
 "", ""),

("sat-013", "sec:saturation", r"independent \mention{some}",
 "a Det function inside every independent occurrence",
 "excluded", "authors_analysis",
 r"The dependent use of \mention{some} doesn't by itself require a Det function inside every independent occurrence.",
 "", ""),

("sat-014", "sec:saturation", "one constituent in Payne's fusion analysis",
 "joint realization of Head and a dependent function",
 "conditional", "not_determinable",
 r"In \textcite{Payne2007}, one constituent jointly realizes Head and a dependent function, subject to structural and adjacency conditions.",
 "Subject to structural and adjacency conditions.", ""),

# ---------------- sec:modification ----------------
("mod-001", "sec:modification", r"\mention{the wine}",
 r"complement of \mention{of} denoting the partitive domain",
 "licensed", "authors_analysis",
 r"The NP \mention{the wine} denotes the partitive domain and is complement of \mention{of}.",
 "", ""),

("mod-002", "sec:modification", r"\mention{many of them}",
 "pronoun-headed NP expressing the partitive domain",
 "licensed", "constructed_illustration",
 r"A pronoun-headed NP or independent genitive NP can express the domain too: \mention{many of them}, referring to previously mentioned people, or \mention{some of Kim's}, referring to Kim's apples.",
 "", ""),

("mod-003", "sec:modification", r"\mention{some of Kim's}",
 "independent genitive NP expressing the partitive domain",
 "licensed", "constructed_illustration",
 r"A pronoun-headed NP or independent genitive NP can express the domain too: \mention{many of them}, referring to previously mentioned people, or \mention{some of Kim's}, referring to Kim's apples.",
 "", ""),

("mod-004", "sec:modification", r"\mention{wine}",
 r"ultimate lexical head of \mention{some of the wine}",
 "excluded", "authors_analysis",
 r"In the partitive, \mention{wine} is embedded inside the \mention{of}-phrase, so it can't be the ultimate lexical head of the whole NP.",
 "", ""),

("mod-005", "sec:modification", r"\mention{some}",
 "ultimate lexical head of the partitive NP under both analyses",
 "licensed", "authors_analysis",
 r"The Head relations in both analyses lead instead to \mention{some}.",
 "", ""),

("mod-006", "sec:modification", r"the partitive \mention{of}-phrase",
 "complement within Nom",
 "licensed", "cgel_described",
 r"Figure~\ref{fig:partitive} gives the D-noun analysis, with the \mention{of}-phrase functioning as complement within Nom, as in \textit{CGEL}'s partitive tree",
 "", "Matches CGEL's partitive tree, pp. 411-412."),

("mod-007", "sec:modification", r"DP headed by \mention{some}",
 "Det--Head in the partitive",
 "licensed", "cgel_described",
 r"In \textit{CGEL}, the DP headed by \mention{some} fills Det--Head.",
 "", ""),

("mod-008", "sec:modification", r"\mention{of}",
 "Head of the complement PP in the partitive tree",
 "licensed", "authors_analysis",
 r"[{\synnode{Head}{P}}, head edge [\mention{of}]]",
 "", "Worked tree in Figure fig:partitive."),

("mod-009", "sec:modification", r"independent \mention{few} and certain other indefinite determinatives",
 "definite determination",
 "conditional", "authors_analysis",
 r"Independent \mention{few} and certain other indefinite determinatives permit definite determination.",
 "Limited to certain indefinite determinatives.", ""),

("mod-010", "sec:modification", r"\mention{few}",
 "Head of an ordinary NP when bare",
 "licensed", "authors_analysis",
 r"Under D-noun, \mention{few} heads an ordinary NP both alone and in \mention{the few}, where \mention{the} fills Det.",
 "", ""),

("mod-011", "sec:modification", r"\mention{the}",
 r"Det of the NP headed by \mention{few} in \mention{the few}",
 "licensed", "authors_analysis",
 r"Under D-noun, \mention{few} heads an ordinary NP both alone and in \mention{the few}, where \mention{the} fills Det.",
 "", ""),

("mod-012", "sec:modification", r"\mention{lucky}",
 r"adjectival modifier in \mention{the lucky few}",
 "licensed", "authors_analysis",
 r"Adding an optional adjective gives \mention{the lucky few}, with the same Head and dependent functions as \mention{the lucky survivors}.",
 "", ""),

("mod-013", "sec:modification", r"\mention{the lucky survivors}",
 "the same Head and dependent functions as the determinative case",
 "licensed", "authors_analysis",
 r"Adding an optional adjective gives \mention{the lucky few}, with the same Head and dependent functions as \mention{the lucky survivors}.",
 "", ""),

("mod-014", "sec:modification", r"\mention{two} in \mention{the other two}",
 "internal modifier fused with Head",
 "licensed", "cgel_described",
 r"\textit{CGEL} explicitly permits determinatives used as internal modifiers to fuse with Head, as in \mention{the other two} and \mention{these few here}",
 "", ""),

("mod-015", "sec:modification", r"\mention{few} in \mention{these few here}",
 "internal modifier fused with Head",
 "licensed", "cgel_described",
 r"\textit{CGEL} explicitly permits determinatives used as internal modifiers to fuse with Head, as in \mention{the other two} and \mention{these few here}",
 "", ""),

("mod-016", "sec:modification", r"\mention{few} in \mention{the few mistakes}",
 "Mod function, with the article as Det",
 "licensed", "cgel_described",
 r"Its analysis of \mention{the few mistakes} assigns \mention{the} to Det and \mention{few} to Mod",
 "", ""),

("mod-017", "sec:modification", r"\mention{few} in \mention{the lucky few}",
 "direct Head of Nom under the D-noun analysis",
 "licensed", "authors_analysis",
 r"In the D-noun analysis, the lexical word \mention{few} directly heads Nom.",
 "", "Figure fig:few, left tree."),

("mod-018", "sec:modification", r"DP headed by \mention{few}",
 "Mod--Head fusion under the competing analysis",
 "licensed", "authors_analysis",
 r"In the fusion analysis, its DP fills Mod--Head.",
 "", "Figure fig:few, right tree."),

("mod-019", "sec:modification", r"\mention{the lucky few}",
 "an overt Det and a Nom modified by the adjective, under both analyses",
 "licensed", "authors_analysis",
 r"Both have an overt Det and a Nom modified by \mention{lucky}.",
 "", ""),

("mod-020", "sec:modification", "the fusion analysis of independent determinatives",
 "a silent noun or conversion",
 "excluded", "authors_analysis",
 r"it requires neither a silent noun nor conversion",
 "", ""),

("mod-021", "sec:modification", r"\mention{few} in \mention{few survivors}",
 "Det function (both analyses)",
 "licensed", "authors_analysis", MH_ROW1, "", "Matched-heads table row."),

("mod-022", "sec:modification", r"\mention{survivors}",
 "Head function (both analyses)",
 "licensed", "authors_analysis", MH_ROW1, "", "Matched-heads table row."),

("mod-023", "sec:modification", r"independent \mention{few}",
 "Det--Head under separate D with fusion",
 "licensed", "authors_analysis", MH_ROW2, "", "Matched-heads table row."),

("mod-024", "sec:modification", r"independent \mention{few}",
 "Head under ordinary determinative Head",
 "licensed", "authors_analysis", MH_ROW2, "", "Matched-heads table row."),

("mod-025", "sec:modification", r"\mention{few} in \mention{the few}",
 "Mod--Head under separate D with fusion",
 "licensed", "authors_analysis", MH_ROW3, "", "Matched-heads table row."),

("mod-026", "sec:modification", r"\mention{few} in \mention{the few}",
 "Head under ordinary determinative Head",
 "licensed", "authors_analysis", MH_ROW3, "", "Matched-heads table row."),

("mod-027", "sec:modification", r"\mention{few} in \mention{the lucky few}",
 "Mod--Head under separate D with fusion, with the adjective as Mod",
 "licensed", "authors_analysis", MH_ROW4, "", "Matched-heads table row."),

("mod-028", "sec:modification", r"\mention{few} in \mention{the lucky few}",
 "Head under ordinary determinative Head, with the adjective as Mod",
 "licensed", "authors_analysis", MH_ROW4, "", "Matched-heads table row."),

("mod-029", "sec:modification", r"\mention{rich} in \mention{the idle rich}",
 "Mod--Head fusion, with the adjective as Mod",
 "licensed", "authors_analysis", MH_ROW5, "", "Matched-heads table row."),

("mod-030", "sec:modification", r"\mention{rich} in \mention{the idle rich}",
 "the same fusion and modifier functions under the ordinary-Head column",
 "licensed", "authors_analysis", MH_ROW5,
 "", "Matched-heads table row; adjectival fusion is retained in both columns."),

("mod-031", "sec:modification", "each independent determinative expression in the matched set",
 "NP status, with the article phrase filling Det",
 "licensed", "authors_analysis",
 r"Each independent expression is an NP; the phrase headed by \mention{the} fills Det wherever it appears.",
 "", "Matched-heads table caption."),

("mod-032", "sec:modification", r"\mention{the remaining three}",
 "modifier pattern extended to cardinals",
 "licensed", "constructed_illustration",
 r"The constructed \mention{the remaining three} extends the modifier pattern to cardinals.",
 "", ""),

("mod-033", "sec:modification", "cardinals",
 "both determinative and common-noun uses",
 "licensed", "not_determinable",
 r"\textcite{reynolds2026numerals} argues for both uses of cardinals",
 "", "Attributed to the companion work on numerals."),
]
