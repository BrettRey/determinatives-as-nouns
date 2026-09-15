# -*- coding: utf-8 -*-
# Part 5: sec:membership, sec:articles, sec:article-membership, sec:form-selection, sec:evidence

ROW_ARG = r"Argument / Det functions & NP arguments; genitive and restricted plain Det & NP arguments; genitive and restricted plain Det & NP arguments; genitive Det & NP arguments; plain and genitive Det"
ROW_DET = r"Accepts determination & Broad contrasts; singular count arguments normally require it & Restricted in primary naming uses & Normally excluded & Lexically restricted: \mention{the few}, \mention{these three}"
ROW_MOD = r"Internal modification & Productive AdjP and nominal premodifiers, including determinative-headed phrases; relatives & Restricted AdjP and nominal premodifiers; embellishments & Restricted AdjP premodifiers and relative postmodifiers & Degree AdvP on four quantifiers; approximatives on cardinals; NP and determinative-headed modifiers; \mention{the lucky few}; relatives"
ROW_COMP = r"Complemen\-tation & Selected PPs and clauses & Not characteristic of primary naming uses & Normally absent & Partitive \mention{of}-PPs; comparative \mention{than}-phrases"
ROW_PERI = r"Peripheral modifiers & \mention{only the book} & \mention{even Kim} & \mention{only you}; \mention{all we who signed up} & \mention{almost every}; \mention{hardly any}; \mention{almost ten}"
ROW_ADJ = r"Modifier / adjunct functions & \mention{dog houses}; \mention{that day} & \mention{Canada Day}; \mention{Sunday} & Emphatic reflexives in both functions & \mention{the few people}; degree adjuncts"
ROW_INFL = r"Inflection & Number and genitive & Genitive; restricted number & Case, including genitive; reflexive forms & Number; grade; genitive; \mention{no}/\mention{none}"
ROW_INT = r"Interrogative / relative constructions & Through another constituent, e.g.\ \mention{which book} & Through another constituent & \mention{who}, \mention{whose} & \mention{which}, \mention{what}, and \mention{-ever} forms"

CLAIMS = [

# ---------------- sec:membership ----------------
("mem-001", "sec:membership", "proper names",
 r"nominal premodifiers, as in \mention{architect Norman Foster}",
 "licensed", "cgel_described",
 r"Proper names permit nominal premodifiers such as \mention{architect Norman Foster}",
 "", ""),

("mem-002", "sec:membership", r"\mention{all}",
 r"peripheral modifier in \mention{all we who signed up}, not internal pronoun modifier",
 "licensed", "cgel_described",
 r"\mention{all} in \mention{all we who signed up} is peripheral, rather than an internal pronoun modifier",
 "", "Internal-modifier status is excluded."),

# Table tab:existing, row by row and column by column.
("mem-003", "sec:membership", "common nouns",
 "NP arguments; genitive and restricted plain Det",
 "conditional", "authors_analysis", ROW_ARG,
 "Plain-case Det use is restricted.", "Profile table row."),

("mem-004", "sec:membership", "proper nouns",
 "NP arguments; genitive and restricted plain Det",
 "conditional", "authors_analysis", ROW_ARG,
 "Plain-case Det use is restricted.", "Profile table row."),

("mem-005", "sec:membership", "pronouns",
 "NP arguments; genitive Det",
 "licensed", "authors_analysis", ROW_ARG, "", "Profile table row."),

("mem-006", "sec:membership", "determinatives",
 "NP arguments; plain and genitive Det",
 "licensed", "authors_analysis", ROW_ARG, "", "Profile table row."),

("mem-007", "sec:membership", "common nouns",
 "determination of the NP",
 "conditional", "authors_analysis", ROW_DET,
 "Broad contrasts; singular count arguments normally require determination.", "Profile table row."),

("mem-008", "sec:membership", "proper nouns",
 "determination of the NP",
 "conditional", "authors_analysis", ROW_DET,
 "Restricted in primary naming uses.", "Profile table row."),

("mem-009", "sec:membership", "pronouns",
 "determination of the NP",
 "excluded", "authors_analysis", ROW_DET,
 "Normally excluded.", "Profile table row."),

("mem-010", "sec:membership", "determinatives",
 r"determination of the NP, as in \mention{the few}, \mention{these three}",
 "conditional", "authors_analysis", ROW_DET,
 "Lexically restricted.", "Profile table row."),

("mem-011", "sec:membership", "common nouns",
 "internal modification: productive AdjP and nominal premodifiers, including determinative-headed phrases; relatives",
 "licensed", "authors_analysis", ROW_MOD, "", "Profile table row."),

("mem-012", "sec:membership", "proper nouns",
 "internal modification: AdjP and nominal premodifiers; embellishments",
 "conditional", "authors_analysis", ROW_MOD,
 "Restricted.", "Profile table row."),

("mem-013", "sec:membership", "pronouns",
 "internal modification: AdjP premodifiers and relative postmodifiers",
 "conditional", "authors_analysis", ROW_MOD,
 "Restricted.", "Profile table row."),

("mem-014", "sec:membership", "determinatives",
 r"internal modification: degree AdvP on four quantifiers; approximatives on cardinals; NP and determinative-headed modifiers; \mention{the lucky few}; relatives",
 "conditional", "authors_analysis", ROW_MOD,
 "Item-specific: the degree AdvP series applies to the four gradable quantifiers, approximatives to cardinals.",
 "Profile table row; these attachments are analytical commitments of the manuscript."),

("mem-015", "sec:membership", "common nouns",
 "complementation by selected PPs and clauses",
 "licensed", "authors_analysis", ROW_COMP, "", "Profile table row."),

("mem-016", "sec:membership", "proper nouns",
 "complementation",
 "excluded", "authors_analysis", ROW_COMP,
 "Not characteristic of primary naming uses.", "Profile table row."),

("mem-017", "sec:membership", "pronouns",
 "complementation",
 "excluded", "authors_analysis", ROW_COMP,
 "Normally absent.", "Profile table row."),

("mem-018", "sec:membership", "determinatives",
 r"complementation by partitive \mention{of}-PPs and comparative \mention{than}-phrases",
 "licensed", "authors_analysis", ROW_COMP, "", "Profile table row."),

("mem-019", "sec:membership", "common nouns",
 r"peripheral modifiers, as in \mention{only the book}",
 "licensed", "authors_analysis", ROW_PERI, "", "Profile table row."),

("mem-020", "sec:membership", "proper nouns",
 r"peripheral modifiers, as in \mention{even Kim}",
 "licensed", "authors_analysis", ROW_PERI, "", "Profile table row."),

("mem-021", "sec:membership", "pronouns",
 r"peripheral modifiers, as in \mention{only you} and \mention{all we who signed up}",
 "licensed", "authors_analysis", ROW_PERI, "", "Profile table row."),

("mem-022", "sec:membership", "determinatives",
 r"peripheral modifiers, as in \mention{almost every}, \mention{hardly any}, \mention{almost ten}",
 "licensed", "authors_analysis", ROW_PERI, "", "Profile table row."),

("mem-023", "sec:membership", "common nouns",
 r"modifier and adjunct functions, as in \mention{dog houses} and \mention{that day}",
 "licensed", "authors_analysis", ROW_ADJ, "", "Profile table row."),

("mem-024", "sec:membership", "proper nouns",
 r"modifier and adjunct functions, as in \mention{Canada Day} and \mention{Sunday}",
 "licensed", "authors_analysis", ROW_ADJ, "", "Profile table row."),

("mem-025", "sec:membership", "pronouns",
 "modifier and adjunct functions through emphatic reflexives",
 "licensed", "authors_analysis", ROW_ADJ, "", "Profile table row."),

("mem-026", "sec:membership", "determinatives",
 r"modifier and adjunct functions, as in \mention{the few people} and degree adjuncts",
 "licensed", "authors_analysis", ROW_ADJ, "", "Profile table row."),

("mem-027", "sec:membership", "common nouns",
 "number and genitive inflection",
 "licensed", "authors_analysis", ROW_INFL, "", "Profile table row."),

("mem-028", "sec:membership", "proper nouns",
 "genitive inflection; restricted number inflection",
 "conditional", "authors_analysis", ROW_INFL,
 "Number inflection is restricted.", "Profile table row."),

("mem-029", "sec:membership", "pronouns",
 "case inflection, including genitive, and reflexive forms",
 "licensed", "authors_analysis", ROW_INFL, "", "Profile table row."),

("mem-030", "sec:membership", "determinatives",
 r"number, grade, and genitive inflection, and the \mention{no}/\mention{none} alternation",
 "conditional", "authors_analysis", ROW_INFL,
 "Item-specific: number on demonstratives, grade on the four gradable quantifiers, genitive on compounds.",
 "Profile table row."),

("mem-031", "sec:membership", "common nouns",
 r"interrogative and relative constructions through another constituent, e.g.\ \mention{which book}",
 "conditional", "cgel_described", ROW_INT,
 "Only through another constituent.", "Profile table row; interrogative and relative forms follow CGEL's inventory."),

("mem-032", "sec:membership", "proper nouns",
 "interrogative and relative constructions through another constituent",
 "conditional", "cgel_described", ROW_INT,
 "Only through another constituent.", "Profile table row."),

("mem-033", "sec:membership", "pronouns",
 r"interrogative and relative forms \mention{who}, \mention{whose}",
 "licensed", "cgel_described", ROW_INT, "", "Profile table row."),

("mem-034", "sec:membership", "determinatives",
 r"interrogative and relative forms \mention{which}, \mention{what}, and \mention{-ever} forms",
 "licensed", "cgel_described", ROW_INT, "", "Profile table row."),

("mem-035", "sec:membership", "the four gradable quantifiers",
 "the wider range of nominal constructions alongside their adjectival pattern",
 "licensed", "authors_analysis",
 r"The gradable quantifiers participate in this wider range alongside their adjectival pattern.",
 "", ""),

("mem-036", "sec:membership", "determinatives",
 "specialization in determination and distinctive dependent patterns within Noun",
 "licensed", "authors_analysis",
 r"Determinative retains its specialization in determination and its distinctive dependent patterns within Noun, just as pronouns retain their differences from common nouns.",
 "", ""),

# ---------------- sec:articles ----------------
("art-001", "sec:articles", "articles",
 "ordinary independent argument uses",
 "excluded", "authors_analysis",
 r"Articles lack ordinary independent argument uses, so their inclusion needs a further argument",
 "", ""),

("art-002", "sec:articles", "articles",
 "membership of the determinative system whose profile supports Noun membership",
 "licensed", "authors_analysis",
 r"they belong to the determinative system whose broader profile supports Noun membership",
 "", ""),

# ---------------- sec:article-membership ----------------
("am-001", "sec:article-membership", r"\mention{the}",
 "independent argument NP",
 "excluded", "cgel_described",
 r"Why categorize the articles \mention{the} and \mention{a} as nouns if they can't form independent argument NPs?",
 "", ""),

("am-002", "sec:article-membership", r"\mention{a}",
 "independent argument NP",
 "excluded", "cgel_described",
 r"Why categorize the articles \mention{the} and \mention{a} as nouns if they can't form independent argument NPs?",
 "", ""),

("am-003", "sec:article-membership", r"\mention{every}",
 "independent argument use",
 "excluded", "cgel_described",
 r"\mention{Every} is restricted too",
 "", ""),

("am-004", "sec:article-membership", r"\mention{no}",
 "independent use, which requires the distinct form",
 "conditional", "cgel_described",
 r"while \mention{no} has the distinct independent form \mention{none}",
 r"The independent use requires \mention{none}.", ""),

("am-005", "sec:article-membership", r"\mention{my}",
 "dependent use within one pronoun paradigm",
 "licensed", "cgel_described",
 r"Dependent \mention{my} and independent \mention{mine} belong to one pronoun paradigm.",
 "", ""),

("am-006", "sec:article-membership", r"\mention{mine}",
 "independent use within one pronoun paradigm",
 "licensed", "cgel_described",
 r"Dependent \mention{my} and independent \mention{mine} belong to one pronoun paradigm.",
 "", ""),

("am-007", "sec:article-membership", r"\mention{My}",
 "ordinary NP construction",
 "conditional", "cgel_described",
 r"\mention{My} remains a noun even though, in the ordinary NP construction, it requires a following nominal.",
 "Requires a following nominal.", ""),

("am-008", "sec:article-membership", r"\mention{the}",
 r"Det position in \mention{the/a/this/every book}",
 "licensed", "cgel_described",
 r"In \mention{the/a/this/every book}, they occupy the same Det position and contribute to the interpretation of the NP.",
 "", ""),

("am-009", "sec:article-membership", r"\mention{a}",
 r"Det position in \mention{the/a/this/every book}",
 "licensed", "cgel_described",
 r"In \mention{the/a/this/every book}, they occupy the same Det position and contribute to the interpretation of the NP.",
 "", ""),

("am-010", "sec:article-membership", r"\mention{this}",
 r"Det position in \mention{the/a/this/every book}",
 "licensed", "cgel_described",
 r"In \mention{the/a/this/every book}, they occupy the same Det position and contribute to the interpretation of the NP.",
 "", ""),

("am-011", "sec:article-membership", r"\mention{every}",
 r"Det position in \mention{the/a/this/every book}",
 "licensed", "cgel_described",
 r"In \mention{the/a/this/every book}, they occupy the same Det position and contribute to the interpretation of the NP.",
 "", ""),

("am-012", "sec:article-membership", r"\mention{The}",
 "Det with singular, plural, and non-count targets",
 "licensed", "cgel_described",
 r"\mention{The} permits singular, plural, and non-count targets",
 "", ""),

("am-013", "sec:article-membership", r"\mention{a}",
 "Det with a singular count target",
 "conditional", "cgel_described",
 r"\mention{a} selects a singular count target and contributes individuation",
 "Singular count target only.", ""),

("am-014", "sec:article-membership", r"\mention{the}",
 r"degree modifier of comparative AdjPs, as in \mention{the bigger the better}",
 "licensed", "cgel_described",
 r"In \mention{the bigger the better}, it modifies comparative AdjPs",
 "", ""),

("am-015", "sec:article-membership", r"\mention{much}",
 r"degree modifier of a comparative, as in \mention{much bigger}",
 "licensed", "cgel_described",
 r"as other determinatives do in \mention{much bigger} or \mention{no better}",
 "", ""),

("am-016", "sec:article-membership", r"\mention{no}",
 r"degree modifier of a comparative, as in \mention{no better}",
 "licensed", "cgel_described",
 r"as other determinatives do in \mention{much bigger} or \mention{no better}",
 "", ""),

("am-017", "sec:article-membership", r"\mention{a}",
 r"complex determinative \mention{a few}",
 "licensed", "cgel_described",
 r"\mention{A} also enters the complex determinatives \mention{a few}, \mention{a little}, and \mention{many a}.",
 "", ""),

("am-018", "sec:article-membership", r"\mention{a}",
 r"complex determinative \mention{a little}",
 "licensed", "cgel_described",
 r"\mention{A} also enters the complex determinatives \mention{a few}, \mention{a little}, and \mention{many a}.",
 "", ""),

("am-019", "sec:article-membership", r"\mention{a}",
 r"complex determinative \mention{many a}",
 "licensed", "cgel_described",
 r"\mention{A} also enters the complex determinatives \mention{a few}, \mention{a little}, and \mention{many a}.",
 "", ""),

("am-020", "sec:article-membership", r"\mention{many a}",
 "Det function only, as a syntactically fixed complex determinative",
 "conditional", "cgel_restricted",
 r"\textit{CGEL} treats \mention{many a} as syntactically fixed and restricted to Det function",
 "Restricted to Det function.", ""),

("am-021", "sec:article-membership", r"ordinary \mention{a}",
 "free acceptance of modifiers",
 "not_stated", "authors_analysis",
 r"it doesn't establish that ordinary \mention{a} freely accepts modifiers",
 "", r"The manuscript declines to infer modifier permissions for ordinary \mention{a}."),

("am-022", "sec:article-membership", r"\mention{the}, \mention{a}, and \mention{every}",
 "occurrence without a following nominal",
 "excluded", "not_determinable",
 r"Her grounds include dependence on a following nominal, lack of predicative and partitive uses, and limited descriptive content.",
 "A following nominal is required.", "Grounds attributed to Spinillo's expanded article category."),

("am-023", "sec:article-membership", r"\mention{the}, \mention{a}, and \mention{every}",
 "predicative uses",
 "excluded", "not_determinable",
 r"Her grounds include dependence on a following nominal, lack of predicative and partitive uses, and limited descriptive content.",
 "", "Grounds attributed to Spinillo."),

("am-024", "sec:article-membership", r"\mention{the}, \mention{a}, and \mention{every}",
 "partitive uses",
 "excluded", "not_determinable",
 r"Her grounds include dependence on a following nominal, lack of predicative and partitive uses, and limited descriptive content.",
 "", "Grounds attributed to Spinillo."),

("am-025", "sec:article-membership", "the three exclusions of bare, predicative, and partitive use",
 "independent evidence for a primary article category",
 "excluded", "authors_analysis",
 r"The exclusions of bare, predicative, and partitive uses all limit occurrence without a following nominal; they aren't three independent reasons for a primary category.",
 "", ""),

("am-026", "sec:article-membership", r"\mention{each}",
 "independent use with universal quantification and singular count selection",
 "licensed", "authors_analysis",
 r"\mention{Every} connects with independent \mention{each} through universal quantification and singular count selection.",
 "", ""),

("am-027", "sec:article-membership", r"\mention{every}",
 r"modification by \mention{almost}",
 "licensed", "authors_analysis",
 r"It also permits \mention{almost}/\mention{nearly} and occurs after genitives in \mention{her every move}.",
 "", ""),

("am-028", "sec:article-membership", r"\mention{every}",
 r"modification by \mention{nearly}",
 "licensed", "authors_analysis",
 r"It also permits \mention{almost}/\mention{nearly} and occurs after genitives in \mention{her every move}.",
 "", ""),

("am-029", "sec:article-membership", r"\mention{every}",
 r"position after a genitive determiner, as in \mention{her every move}",
 "licensed", "authors_analysis",
 r"It also permits \mention{almost}/\mention{nearly} and occurs after genitives in \mention{her every move}.",
 "", ""),

("am-030", "sec:article-membership", r"\mention{some}",
 r"occurrence before a nominal, as in \mention{some teachers}",
 "licensed", "not_determinable",
 r"occurrence before a nominal (\mention{some teachers}) alternates with occurrence without one (\mention{some left})",
 "", "Reported as part of Spinillo's complement-omission analogy."),

("am-031", "sec:article-membership", r"\mention{some}",
 r"occurrence without a following nominal, as in \mention{some left}",
 "licensed", "not_determinable",
 r"occurrence before a nominal (\mention{some teachers}) alternates with occurrence without one (\mention{some left})",
 "", "Reported as part of Spinillo's complement-omission analogy."),

("am-032", "sec:article-membership", r"\mention{all}",
 "alternation between dependent and independent occurrence",
 "licensed", "not_determinable",
 r"For demonstratives and quantifiers such as \mention{some} and \mention{all}, occurrence before a nominal",
 "", "Reported as part of Spinillo's complement-omission analogy."),

("am-033", "sec:article-membership", "the restricted members (articles)",
 "retention within the determinative category",
 "licensed", "authors_analysis",
 r"I retain the restricted members within determinative because these connections preserve a broader system without granting unrestricted use to any member.",
 "No unrestricted use is granted to any member.", ""),

# ---------------- sec:form-selection ----------------
("fs-001", "sec:form-selection", r"\mention{no}",
 r"dependent use, as in \mention{no students}",
 "licensed", "cgel_described",
 r"dependent \mention{no students} contrasts with independent \mention{none}",
 "", ""),

("fs-002", "sec:form-selection", r"\mention{none}",
 "independent use",
 "licensed", "cgel_described",
 r"dependent \mention{no students} contrasts with independent \mention{none}",
 "", ""),

("fs-003", "sec:form-selection", r"\mention{no}",
 r"modification by \mention{almost}",
 "licensed", "cgel_described",
 r"while both permit \mention{almost}",
 "", ""),

("fs-004", "sec:form-selection", r"\mention{none}",
 r"modification by \mention{almost}",
 "licensed", "cgel_described",
 r"while both permit \mention{almost}",
 "", ""),

("fs-005", "sec:form-selection", r"\mention{none}",
 r"partitive, as in \mention{none of the students}",
 "conditional", "cgel_described",
 r"The partitive \mention{none of the students} requires the independent form",
 "The independent form is required.", ""),

("fs-006", "sec:form-selection", r"\mention{no}",
 "partitive construction",
 "excluded", "constructed_ungrammatical",
 r"\ungram{\mention{no of the students}} is excluded",
 "", "Marked ungrammatical."),

# ---------------- sec:evidence ----------------
("ev-001", "sec:evidence", r"independent \mention{some}",
 "ordinary Head versus fusion in the independent construction",
 "licensed", "authors_analysis",
 r"This section compares that treatment with fusion in independent \mention{some}, \mention{some of the wine}, and \mention{the lucky few}.",
 "", "Section preview identifying the three constructions compared."),

("ev-002", "sec:evidence", r"\mention{some of the wine}",
 "partitive construction analysed with ordinary Head or fusion",
 "licensed", "authors_analysis",
 r"This section compares that treatment with fusion in independent \mention{some}, \mention{some of the wine}, and \mention{the lucky few}.",
 "", ""),

("ev-003", "sec:evidence", r"\mention{the lucky few}",
 "externally determined and modified independent determinative",
 "licensed", "authors_analysis",
 r"This section compares that treatment with fusion in independent \mention{some}, \mention{some of the wine}, and \mention{the lucky few}.",
 "", ""),
]
