# -*- coding: utf-8 -*-
# Part 10: sec:costs, sec:overall-assessment, sec:inheritance, sec:conclusion, sec:historical

EC_ROW1 = r"D-noun, ordinary Head & Nom--NP with Head alone across bare, partitive, and externally determined uses. & Peripheral NP premodifiers; head-specific internal modifiers. Degree determinatives project NP."
EC_ROW2 = r"Separate D, ordinary Head & Same structures, with Nom admitting either N or D as lexical Head. & Same internal and peripheral permissions and degree projection as the proposed package."
EC_ROW3 = r"Separate D, fused Head & DP fills Det--Head or Mod--Head in nominal structure. & DP--Nom separates premodifiers and postmodifiers. Degree determinatives project DP."
EC_ROW4 = r"D-noun, fused Head & A projected NP fills Det--Head or Mod--Head in additional nominal structure. & Premodifiers within the fused NP; postmodifiers in the outer Nom. Degree determinatives project NP."

CLAIMS = [

# ---------------- sec:costs ----------------
("cost-001", "sec:costs", "independent determinatives under D-noun with ordinary Head",
 "Nom--NP with Head alone across bare, partitive, and externally determined uses",
 "licensed", "authors_analysis", EC_ROW1, "", "Implementation comparison table row."),

("cost-002", "sec:costs", "modifiers of determinatives under D-noun with ordinary Head",
 "peripheral NP premodifiers and head-specific internal modifiers; degree determinatives project NP",
 "conditional", "authors_analysis", EC_ROW1,
 "Internal modifiers are head-specific.", "Implementation comparison table row."),

("cost-003", "sec:costs", "independent determinatives under separate D with ordinary Head",
 "the same structures, with Nom admitting either N or D as lexical Head",
 "licensed", "authors_analysis", EC_ROW2, "", "Implementation comparison table row."),

("cost-004", "sec:costs", "modifiers of determinatives under separate D with ordinary Head",
 "the same internal and peripheral permissions and degree projection",
 "licensed", "authors_analysis", EC_ROW2, "", "Implementation comparison table row."),

("cost-005", "sec:costs", "independent determinatives under separate D with fusion",
 "DP filling Det--Head or Mod--Head in nominal structure",
 "licensed", "authors_analysis", EC_ROW3, "", "Implementation comparison table row."),

("cost-006", "sec:costs", "modifiers of determinatives under separate D with fusion",
 "premodifiers and postmodifiers separated by the DP--Nom boundary; degree determinatives project DP",
 "licensed", "authors_analysis", EC_ROW3, "", "Implementation comparison table row."),

("cost-007", "sec:costs", "independent determinatives under D-noun with fusion",
 "a projected NP filling Det--Head or Mod--Head in additional nominal structure",
 "licensed", "authors_analysis", EC_ROW4, "", "Implementation comparison table row."),

("cost-008", "sec:costs", "modifiers of determinatives under D-noun with fusion",
 "premodifiers within the fused NP; postmodifiers in the outer Nom; degree determinatives project NP",
 "licensed", "authors_analysis", EC_ROW4, "", "Implementation comparison table row."),

("cost-009", "sec:costs", "independent genitives under ordinary Head",
 "a constructional agreement condition",
 "conditional", "authors_analysis",
 r"Extending ordinary Head to independent genitives adds a constructional agreement condition",
 "A constructional agreement condition is required.", "Table caption."),

("cost-010", "sec:costs", "both ordinary-Head accounts",
 "distinguishing peripheral NP modifiers from internal degree and cardinal approximative permissions",
 "licensed", "authors_analysis",
 r"Both ordinary-Head accounts distinguish peripheral NP modifiers from the internal degree and cardinal approximative permissions",
 "", ""),

("cost-011", "sec:costs", r"\mention{few} in the ordinary-Head accounts",
 "heading Nom, with Nom heading NP, across bare, partitive, and externally determined uses",
 "licensed", "authors_analysis",
 r"In the ordinary-Head accounts, \mention{few} heads Nom and Nom heads NP across bare, partitive, and externally determined uses.",
 "", ""),

("cost-012", "sec:costs", r"the phrase headed by \mention{few} in the fusion accounts",
 "Det--Head in bare and partitive uses",
 "licensed", "authors_analysis",
 r"In the fusion accounts, its DP or NP fills Det--Head in bare and partitive uses and Mod--Head with an external determiner",
 "", ""),

("cost-013", "sec:costs", r"the phrase headed by \mention{few} in the fusion accounts",
 "Mod--Head with an external determiner",
 "licensed", "authors_analysis",
 r"In the fusion accounts, its DP or NP fills Det--Head in bare and partitive uses and Mod--Head with an external determiner",
 "", ""),

("cost-014", "sec:costs", "all four accounts in the matched examples",
 "Nom as the NP's immediate Head",
 "licensed", "authors_analysis",
 r"In these matched examples, all have Nom as the NP's immediate Head.",
 "", ""),

("cost-015", "sec:costs", r"\mention{ten} in \mention{ten men}",
 "determinative numeral use",
 "licensed", "not_determinable",
 r"\textcite{reynolds2026numerals} distinguishes determinative numerals such as \mention{ten} in \mention{ten men}, proper-noun cases such as \mention{10} in \mention{Room 10}, and common-noun numerals such as \mention{tens} in \mention{tens of pens}.",
 "", "Attributed to the companion work on numerals."),

("cost-016", "sec:costs", r"\mention{10} in \mention{Room 10}",
 "proper-noun numeral use",
 "licensed", "not_determinable",
 r"\textcite{reynolds2026numerals} distinguishes determinative numerals such as \mention{ten} in \mention{ten men}, proper-noun cases such as \mention{10} in \mention{Room 10}, and common-noun numerals such as \mention{tens} in \mention{tens of pens}.",
 "", "Attributed to the companion work on numerals."),

("cost-017", "sec:costs", r"\mention{tens} in \mention{tens of pens}",
 "common-noun numeral use",
 "licensed", "not_determinable",
 r"\textcite{reynolds2026numerals} distinguishes determinative numerals such as \mention{ten} in \mention{ten men}, proper-noun cases such as \mention{10} in \mention{Room 10}, and common-noun numerals such as \mention{tens} in \mention{tens of pens}.",
 "", "Attributed to the companion work on numerals."),

("cost-018", "sec:costs", "ordinals",
 "adjective category membership",
 "licensed", "not_determinable",
 r"Ordinals remain adjectives, and complex numeral phrases remain distinct from single lexemes.",
 "", ""),

("cost-019", "sec:costs", r"the three lexemes spelled \mention{one}",
 "determinative, anaphoric common noun, and generic personal pronoun uses",
 "licensed", "not_determinable",
 r"\textcite[797--798]{payne2013anaphoric} distinguish three lexemes spelled \mention{one}: determinative, anaphoric common noun, and generic personal pronoun.",
 "", "Attributed to Payne, Pullum, Scholz and Berlage."),

("cost-020", "sec:costs", r"\mention{two hundred} in \mention{two hundred books}",
 "Det function of the whole complex cardinal",
 "licensed", "not_determinable",
 r"In \mention{two hundred books}, the whole \mention{two hundred} fills Det; internally, \mention{two} modifies the magnitude head \mention{hundred}",
 "", ""),

("cost-021", "sec:costs", r"\mention{two} in \mention{two hundred}",
 r"internal modifier of the magnitude head \mention{hundred}",
 "licensed", "not_determinable",
 r"In \mention{two hundred books}, the whole \mention{two hundred} fills Det; internally, \mention{two} modifies the magnitude head \mention{hundred}",
 "", ""),

("cost-022", "sec:costs", r"\mention{these} in \mention{these two hundred books}",
 "Det function",
 "licensed", "authors_analysis",
 r"In \mention{these two hundred books}, \mention{these} fills Det and \mention{two hundred} is an internal modifier.",
 "", ""),

("cost-023", "sec:costs", r"\mention{two hundred} in \mention{these two hundred books}",
 "internal modifier function",
 "licensed", "authors_analysis",
 r"In \mention{these two hundred books}, \mention{these} fills Det and \mention{two hundred} is an internal modifier.",
 "", ""),

("cost-024", "sec:costs", "an NP",
 "more than one determinative lexeme",
 "licensed", "authors_analysis",
 r"One Det function doesn't entail a limit of one determinative lexeme per NP.",
 "", ""),

# ---------------- sec:overall-assessment ----------------
("oa-001", "sec:overall-assessment", "determinatives in the proposed grammar",
 "the Noun condition on lexical Heads in Nom",
 "licensed", "authors_analysis",
 r"Within the proposed grammar, determinatives then meet the same Noun condition on lexical Heads in Nom as the existing subcategories",
 "", ""),

("oa-002", "sec:overall-assessment", "separate D with ordinary Head",
 "licensing the same structures by admitting N or D",
 "licensed", "authors_analysis",
 r"Separate D with ordinary Head licenses the same structures by admitting N or D.",
 "", ""),

("oa-003", "sec:overall-assessment", "determinative-headed and genitive expressions",
 "a shared structural projection",
 "conditional", "authors_analysis",
 r"If determinative-headed and genitive expressions require different structural constraints after their independently motivated restrictions are held fixed, the shared-projection proposal in §\ref{sec:det-uniform} loses its advantage.",
 "The shared projection holds only if no further differing structural constraints are required.", ""),

# ---------------- sec:inheritance ----------------
("inh-001", "sec:inheritance", "Hudson's determiner category",
 "valency permitting the relevant common-noun dependent",
 "licensed", "not_determinable",
 r"what he calls a determiner is a pronoun whose \term{valency} permits the relevant common-noun dependent",
 "", "Hudson's Word Grammar taxonomy."),

("inh-002", "sec:inheritance", "a determiner word in Hudson's account",
 "constant category across independent and dependent uses",
 "conditional", "not_determinable",
 r"The word's category remains constant across independent and dependent uses, which differ in their permitted dependents.",
 "The uses differ in their permitted dependents.", ""),

("inh-003", "sec:inheritance", "Hudson's determiners",
 "licensing a singular count common noun, with mutual exclusion in that use",
 "conditional", "not_determinable",
 r"Hudson's criteria centre on licensing a singular count common noun and on mutual exclusion in that use.",
 "Mutual exclusion in that use.", ""),

("inh-004", "sec:inheritance", r"\mention{all}",
 "Hudson's determiner criteria",
 "not_stated", "not_determinable",
 r"He sets aside \mention{all}, cardinal numerals, and quantifiers restricted to plural or non-count nouns",
 "", "Its place in the taxonomy remains unsettled by those criteria."),

("inh-005", "sec:inheritance", "cardinal numerals",
 "Hudson's determiner criteria",
 "not_stated", "not_determinable",
 r"He sets aside \mention{all}, cardinal numerals, and quantifiers restricted to plural or non-count nouns",
 "", "Their place in the taxonomy remains unsettled by those criteria."),

("inh-006", "sec:inheritance", "quantifiers restricted to plural or non-count nouns",
 "Hudson's determiner criteria",
 "not_stated", "not_determinable",
 r"He sets aside \mention{all}, cardinal numerals, and quantifiers restricted to plural or non-count nouns",
 "", "Their place in the taxonomy remains unsettled by those criteria."),

("inh-007", "sec:inheritance", "pronouns and determinatives",
 "gender-sensitive and interrogative or relative forms",
 "licensed", "authors_analysis",
 r"Pronouns and determinatives both have closed inventories, and both include gender-sensitive forms and interrogative or relative forms.",
 "", ""),

("inh-008", "sec:inheritance", r"\mention{she}/\mention{it}",
 "contrast encoded by the lexical head",
 "licensed", "authors_analysis",
 r"The contrasts \mention{she}/\mention{it} and \mention{somebody}/\mention{something} are encoded by the lexical head, whereas descriptions and names shape referent construal",
 "", ""),

("inh-009", "sec:inheritance", r"\mention{somebody}/\mention{something}",
 "contrast encoded by the lexical head",
 "licensed", "authors_analysis",
 r"The contrasts \mention{she}/\mention{it} and \mention{somebody}/\mention{something} are encoded by the lexical head, whereas descriptions and names shape referent construal",
 "", ""),

("inh-010", "sec:inheritance", r"the \mention{my}/\mention{mine} paradigm",
 "dependent and independent form distinction in ordinary NP uses",
 "licensed", "authors_analysis",
 r"In ordinary NP uses, both distinguish dependent and independent forms.",
 "", ""),

("inh-011", "sec:inheritance", r"the \mention{no}/\mention{none} paradigm",
 "dependent and independent form distinction in ordinary NP uses",
 "licensed", "authors_analysis",
 r"In ordinary NP uses, both distinguish dependent and independent forms.",
 "", ""),

("inh-012", "sec:inheritance", "personal pronouns",
 r"adjectival modification, as in \mention{poor old me}",
 "conditional", "cgel_described",
 r"Personal pronouns permit restricted adjectival modification, as in \mention{poor old me}",
 "Restricted.", ""),

("inh-013", "sec:inheritance", r"determinative \mention{the lucky few}",
 "adjectival modification",
 "licensed", "authors_analysis",
 r"compare determinative \mention{the lucky few}",
 "", ""),

("inh-014", "sec:inheritance", "pronouns and determinatives",
 "peripheral NP modifiers",
 "conditional", "authors_analysis",
 r"Both groups permit peripheral NP modifiers, subject to lexical selection",
 "Subject to lexical selection.", ""),

("inh-015", "sec:inheritance", "the four gradable quantifiers",
 "internal degree-AdvP series",
 "licensed", "authors_analysis",
 r"The four gradable quantifiers also permit the internal degree-AdvP series discussed in §\ref{sec:adjectival-profile}.",
 "", ""),

("inh-016", "sec:inheritance", "personal pronouns",
 "free determination",
 "excluded", "cgel_described",
 r"Personal pronouns and primary naming uses of proper nouns both resist free determination",
 "", ""),

("inh-017", "sec:inheritance", "primary naming uses of proper nouns",
 "free determination",
 "excluded", "cgel_described",
 r"Personal pronouns and primary naming uses of proper nouns both resist free determination",
 "", ""),

("inh-018", "sec:inheritance", r"\mention{the few}",
 "external definite determination of a determinative",
 "conditional", "authors_analysis",
 r"Determinatives allow \mention{the few}, \mention{the two}, and \mention{these three}, with item-specific conditions",
 "Item-specific conditions.", ""),

("inh-019", "sec:inheritance", r"\mention{the two}",
 "external definite determination of a determinative",
 "conditional", "authors_analysis",
 r"Determinatives allow \mention{the few}, \mention{the two}, and \mention{these three}, with item-specific conditions",
 "Item-specific conditions.", ""),

("inh-020", "sec:inheritance", r"\mention{these three}",
 "external determination of a determinative",
 "conditional", "authors_analysis",
 r"Determinatives allow \mention{the few}, \mention{the two}, and \mention{these three}, with item-specific conditions",
 "Item-specific conditions.", ""),

("inh-021", "sec:inheritance", r"\mention{these few here}",
 "external determination with a post-head modifier",
 "licensed", "cgel_described",
 r"\textit{CGEL} gives \mention{these few here} and \mention{the many who did}",
 "", ""),

("inh-022", "sec:inheritance", r"\mention{the many who did}",
 "external determination with a relative postmodifier",
 "licensed", "cgel_described",
 r"\textit{CGEL} gives \mention{these few here} and \mention{the many who did}",
 "", ""),

("inh-023", "sec:inheritance", "both inheritance paths (coordinate and nested)",
 "the fragment's Noun condition",
 "licensed", "authors_analysis",
 r"Both inheritance paths meet the fragment's Noun condition (§\ref{sec:det-uniform}), and nesting remains a coherent alternative.",
 "", ""),

# ---------------- sec:conclusion ----------------
("con-001", "sec:conclusion", "quantificational common nouns",
 "selected complements, number transparency, restricted dependents, and degree uses",
 "licensed", "authors_analysis",
 r"their selected complements, number transparency, restricted dependents, and degree uses connect with parts of the determinative inventory",
 "", "Concluding summary of the nominal connection."),

("con-002", "sec:conclusion", "the four gradable quantifiers",
 "the connected adjectival profile",
 "licensed", "authors_analysis",
 r"The connected adjectival profile of the four gradable quantifiers deserves weight on the same terms.",
 "", ""),

("con-003", "sec:conclusion", "articles",
 "contrasts in definiteness, quantity, and count selection",
 "licensed", "authors_analysis",
 r"Articles participate in its contrasts in definiteness, quantity, and count selection",
 "", ""),

("con-004", "sec:conclusion", r"\mention{no}/\mention{none}",
 "form-selection conditions within the paradigm",
 "conditional", "authors_analysis",
 r"\mention{no}/\mention{none} retains its form-selection conditions",
 "The dependent and independent forms are selected by construction.", ""),

("con-005", "sec:conclusion", "the independent determinative under ordinary Head",
 "heading Nom, with Nom heading NP, in bare, partitive, and externally determined expressions",
 "licensed", "authors_analysis",
 r"The ordinary-Head analysis uses the same chain in bare, partitive, and externally determined expressions: the word heads Nom, and Nom heads NP.",
 "", ""),

("con-006", "sec:conclusion", "attributive degree modification",
 "lexical, constructional, and register conditions",
 "not_stated", "authors_analysis",
 r"Attributive degree modification still requires a fuller account of lexical, constructional, and register conditions.",
 "", "Left open by the manuscript."),

# ---------------- sec:historical ----------------
("his-001", "sec:historical", "determinative adjectives",
 "grouping with pronouns",
 "licensed", "not_determinable",
 r"\textcite[24]{palmer1924} proposed placing \enquote{determinative adjectives} with pronouns.",
 "", "Palmer's proposal, reported by the manuscript."),

("his-002", "sec:historical", "qualifying adjectives",
 "predicative use, comparison, and adverbial modification",
 "licensed", "not_determinable",
 r"He contrasted them with qualifying adjectives, which permit predicative use, comparison, and adverbial modification.",
 "", "Palmer's contrast."),

("his-003", "sec:historical", "most determinatives",
 "use as pronouns or as modifiers of nouns",
 "licensed", "not_determinable",
 r"Most determinatives, he observed, can \enquote{be used indifferently as pronouns or as modifiers of nouns}.",
 "", "Palmer's observation, quoted."),

("his-004", "sec:historical", "articles, demonstratives, and personal pronouns",
 "shared definiteness and deictic contrasts",
 "licensed", "not_determinable",
 r"\textcite[279]{lyons1968} adds a semantic connection: articles, demonstratives, and personal pronouns share definiteness and deictic contrasts.",
 "", "A semantic rather than distributional connection."),

("his-005", "sec:historical", r"\mention{we men}",
 "article--pronoun combination",
 "licensed", "not_determinable",
 r"\textcite{postal1966} develops the article--pronoun connection through English reflexives and combinations such as \mention{we men}.",
 "", "Postal's evidence, at intermediate and underlying levels."),

("his-006", "sec:historical", "surface pronouns in Postal's account",
 "derivative Noun status",
 "conditional", "not_determinable",
 r"article segments occur at intermediate stages, their deepest counterparts are features of nouns, and surface pronouns can receive derivative Noun status",
 "Depends on representational level.", ""),

("his-007", "sec:historical", "the definite article and personal pronouns",
 "underlying NP structure",
 "licensed", "not_determinable",
 r"\textcite[197--203]{sommerstein1972} argues in the opposite direction, giving the definite article and personal pronouns underlying NP structure.",
 "", "At the level of underlying representation."),

("his-008", "sec:historical", r"anaphoric \mention{one}",
 "reference to a quantity of a substance (count restriction)",
 "excluded", "not_determinable",
 r"His English comparison includes the count restriction on anaphoric \mention{one}, whereas \mention{it} can refer to a quantity of a substance.",
 "", "Count restriction reported from Sommerstein."),

("his-009", "sec:historical", r"\mention{it}",
 "reference to a quantity of a substance",
 "licensed", "not_determinable",
 r"His English comparison includes the count restriction on anaphoric \mention{one}, whereas \mention{it} can refer to a quantity of a substance.",
 "", ""),

("his-010", "sec:historical", r"anaphoric \mention{one}",
 "common count noun use, distinct from the determinative and pronoun lexemes",
 "licensed", "not_determinable",
 r"\textcite[797--798]{payne2013anaphoric} analyse anaphoric \mention{one} as a common count noun, distinct from determinative \mention{one} and personal pronoun \mention{one}.",
 "", "Footnote."),

("his-011", "sec:historical", r"\mention{the}, \mention{a}, and \mention{every}",
 "retention as articles under Spinillo's recategorization",
 "licensed", "not_determinable",
 r"Spinillo & Determinatives redistributed; \mention{the}, \mention{a}, and \mention{every} retained as articles.",
 "", "Row of the rival-accounts table."),

("his-012", "sec:historical", "the modern determinative inventory",
 "surface taxonomy settled by the earlier accounts",
 "not_stated", "authors_analysis",
 r"These predecessors challenge a fundamental article--pronoun separation but don't settle the full modern determinative inventory's surface taxonomy.",
 "", ""),
]
