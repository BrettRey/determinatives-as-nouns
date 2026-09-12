from pathlib import Path
import re

p = Path('determinatives-as-nouns.tex')
s = p.read_text()
baseline = Path('notes/snapshots/2026-09-11-consolidation/determinatives-as-nouns.tex').read_text()
assert s == baseline

def replace(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:100])
    s = s.replace(old, new)

def between(start, end, new):
    global s
    a=s.index(start); b=s.index(end,a)
    s=s[:a]+new+s[b:]

# Keep the inventory comparison independent of the disputed pronoun boundary.
replace(r"The determinative inventory includes independent \mention{what} and relative \mention{which}, as explained in §\ref{sec:wh-boundary}.", r"Interrogative and relative examples follow \textit{CGEL}'s inventory; their precise subcategory boundaries aren't at issue here.")
replace(r"Internal modification & Productive", r"Modification & Productive")
replace(r"Relative \mention{who}/\mention{which} supplies another contrast; independent \mention{what} raises a categorization question taken up in §\ref{sec:wh-boundary}.", r"Relative \mention{who}/\mention{which} supplies another contrast.\footnote{Whether independent \mention{what} and relative \mention{which} belong to pronoun or determinative leaves them within the proposed Noun category. I leave that internal boundary open here; \textit{CGEL}'s inventory suffices for the present comparison \citep[397--399]{huddleston2002}.}")
between(r'\subsection{The pronoun boundary:', r'\subsection{Form selection', '')
replace(r'\section{Restricted members and disputed boundaries}', r'\section{Restricted members and wider functions}')
replace(r"The broader grouping must accommodate members that lack its most conspicuous properties. Articles test whether ordinary independent use is necessary; \mention{which} and \mention{what} test the pronoun boundary; \mention{no}/\mention{none} and \mention{enough} test form selection and functions outside NP structure.", r"The broader grouping includes members with restricted distributions. Articles test whether ordinary independent use is necessary; \mention{no}/\mention{none} tests form selection, and \mention{enough} extends the comparison to functions outside NP structure.")
replace(r"The proposed treatment of \mention{what} and relative \mention{which} relocates a boundary within Noun. ", '')
replace(r"Cardinal uses and the lexemes spelled \mention{one} remain within one primary category. Reassigning \mention{what} and relative \mention{which} likewise relocates a boundary inside Noun. These connected consequences of the hierarchy show what its alignment with nominal projection buys once the broader profile supports the grouping.", r"These cardinal expressions and the lexemes spelled \mention{one} retain their distinctions within one primary category. Their grouping is a consequence of the proposed hierarchy, whose support comes from the broader profile comparison.")

# Promote the comparison from the common-noun side and develop agreement.
between('Quantificational common nouns make the connection', 'The adjectival affinities likewise', '')
replace(r"Adverbial premodification is a broad counterweight; grade and comparative complementation connect a smaller set with adjectives.", r"Adverbial premodification distinguishes determinatives distributionally, though peripheral NP attachment limits its force as a primary-category diagnostic (§\ref{sec:payne}). Grade and comparative complementation connect a smaller set with adjectives.")
replace(r'\subsection{Noun phrases in determiner and argument functions}', r'''\subsection{The connection from the common-noun side}\label{sec:quant-nouns}

Quantificational common nouns make the connection more specific than shared quantity meanings. In \mention{a lot of the delegates} and \mention{many of the delegates}, both heads quantify over a partitive domain. But \mention{lot} also permits \mention{a lot of delegates}, whereas \ungram{\mention{many of delegates}} is excluded \citep[349]{huddleston2002}. The comparison links the groups through a shared construction while preserving a specific difference in complementation.

Agreement provides another connection. Compare the constructed \mention{A lot of the people were waiting} and \mention{Some of the people were waiting}, with plural agreement, against \mention{A lot of the work was finished} and \mention{Some of the work was finished}, with singular agreement. The whole subject NP's number depends on the complement of \mention{of}. \textit{CGEL} calls quantificational \mention{lot} \term{number-transparent} \citep[349--350, 411--412]{huddleston2002}.

This pattern connects particular constructions, not every member of either category. Singular \mention{each of the people} doesn't take its number from \mention{people}; nor does ordinary \mention{a photograph of the people}. Number transparency strengthens the comparison between quantificational \mention{lot} and number-neutral \mention{some} without turning complement number into a general rule for Noun.

Restricted dependents also occur on the common-noun side. \textit{CGEL} categorizes quantificational \mention{plenty} as a common noun whose use resists determination and modification; \mention{lot} requires \mention{a} and permits only limited modification \citep[349--350]{huddleston2002}. Established common nouns thus approach the determinative profile as determinatives approach theirs. Ordinary count nouns alone provide an inadequate comparison group.

The connection also extends beyond argument NPs. Quantificational nouns occur in degree modifiers such as \mention{a great deal smaller} and \mention{plenty big enough} \citep[549--550]{huddleston2002}. Section~\ref{sec:enough} compares these with determinative degree modifiers, including the restrictions on their attributive use. Meaning, complementation, agreement, and restricted dependents give the proposed grouping a specific basis within established Noun.

\subsection{Noun phrases in determiner and argument functions}''')

# Peripheral modification is available inside an embedded NP. The outer Det is not a test.
replace(r"Shared nominal projection doesn't make modifier permissions uniform. In \mention{almost every experienced teacher} (Figure~\ref{fig:every}), the AdvP \mention{almost} modifies the determinative noun \mention{every}; the AdjP \mention{experienced} modifies the common noun \mention{teacher}, which ultimately heads the outer NP.", r"Shared nominal projection doesn't make modifier permissions uniform. In \mention{almost every experienced teacher}, \mention{almost} belongs with \mention{every}, while \mention{experienced} modifies \mention{teacher}. Figure~\ref{fig:every} gives \mention{almost} peripheral attachment within the smaller determinative-headed NP. That NP functions as Det in the larger NP, whose ultimate head is \mention{teacher}.")
replace(r''' [{\synnode{Det}{NP\textsubscript{D}}}
  [{\synnode{Head}{Nom}}, head edge
   [{\synnode{Mod}{AdvP}} [\mention{almost}]]
   [{\synnode{Head}{N\textsubscript{D}}}, head edge [\mention{every}]]]]''', r''' [{\synnode{Det}{NP\textsubscript{D}}}
  [{\synnode{Mod}{AdvP}} [\mention{almost}]]
  [{\synnode{Head}{NP\textsubscript{D}}}, head edge
   [{\synnode{Head}{Nom}}, head edge
    [{\synnode{Head}{N\textsubscript{D}}}, head edge [\mention{every}]]]]]
'''.rstrip())
replace(r"\caption{Two modifier relations in \mention{almost every experienced teacher}: \mention{almost} modifies \mention{every}, and \mention{experienced} modifies \mention{teacher}. The outer NP has \mention{teacher} as its ultimate head. Internal structure within the one-word modifier phrases is suppressed.}", r"\caption{Peripheral \mention{almost} modifies the smaller NP headed by \mention{every}; the resulting \mention{almost every} NP functions as Det. The adjective \mention{experienced} modifies the common-noun nominal. Internal structure within the one-word modifier phrases is suppressed.}")
between(r"Could \mention{almost} in \mention{almost every}", 'NP modifiers provide a further connection.', r'''These levels remain distinct when one NP is embedded inside another. In \mention{the very few people}, \mention{very few} can be an NP functioning as Mod, with \mention{very} peripheral to the NP headed by \mention{few}. The determiner \mention{the} belongs to the larger NP. Its position before \mention{very} doesn't make \mention{very} internal to the smaller NP.

The same attachment is available in independent \mention{the very few who objected}, with the inner NP realizing Mod--Head fusion. Alternatively, an ordinary-Head analysis can place \mention{very} within the nominal headed by \mention{few}. Nounhood permits both options: it doesn't itself eliminate fusion (§\ref{sec:independent}). The example therefore doesn't establish that internal AdvP modification is unavoidable.

\textit{CGEL} already observes overlap between DP modifiers and peripheral NP modifiers, with some attachment decisions uncertain \citep[431]{huddleston2002}. Replacing DP with NP makes peripheral attachment available within determinative-headed projections. Where an ordinary-Head account instead chooses internal attachment, it needs the corresponding modifier permission. That is a property of the chosen structure, rather than a cost forced by the outer determiner.

''')
replace(r"The resulting comparison is narrower than a contrast between nouns and adverb-modified determinatives. Peripheral modification already belongs to NP grammar; some internal adverbial modification occurs with common nouns too. Determinatives still permit internal modifier patterns that ordinary common-noun heads exclude. Section~\ref{sec:costs} counts the necessary subcategory restrictions in comparing the grammars.", r"The comparison therefore concerns modifier selection as well as attachment. Determinative-headed NPs accept modifiers that other NPs often exclude, but their structural analysis can reuse peripheral modification. The matched ordinary-Head fragment below admits internal attachment too, subject to head-specific permissions. Section~\ref{sec:costs} separates those descriptive choices from the primary-category decision.")

# Keep an internally attached compound tree as an explicit matched option, not a forced analysis.
replace(r"In the D-noun analysis, \mention{anyone} inherits nominal projection from Noun and its premodifier permissions from its determinative base.", r"In the ordinary-Head tree shown here, \mention{anyone} inherits nominal projection from Noun and its premodifier permissions from its determinative base.")
replace(r"Fusion reuses the DP--Nom boundary to separate the two modifier domains. Ordinary headedness locates both within Nom, assigning their restrictions to the determinative base and compound construction. Both accounts need the specialized restrictor condition.", r"Fusion reuses the DP--Nom boundary to separate the two modifier domains. The displayed ordinary-Head tree locates both within Nom, assigning their restrictions to the determinative base and compound construction. Peripheral NP attachment for \mention{hardly} is another possibility (§\ref{sec:payne}); either structure retains the compound's post-head restrictor condition.")

# Compress derivation and history without removing comparisons that feed the argument.
between(r'\subsection{Word formation and category boundaries}', r'\section{Evidence for nominal structure}', r'''Derivation supplies a weaker category diagnostic. Determinatives enter common-noun formations such as \mention{nothingness} and \mention{oneness}, but \mention{-ness} also attaches to adjectives and other bases \citep[Ch.~19, §5.7.2(i)]{huddleston2002}. Such outputs don't establish a uniformly noun-selecting rule. The inflectional comparisons above bear more directly on the proposed grouping.\footnote{Numeral morphology also needs the input category distinguished from the output. \textcite[§§5.4--5.5]{reynolds2026numerals} derives fractional nouns from cardinal nouns and treats \mention{two thousand and twenty-seventh} as a coordination whose final coordinate is adjectival. Neither process independently establishes determinative nounhood.}

''')
replace(r"\textcite{postal1966} develops the article--pronoun connection through English reflexives and combinations such as \mention{we men}. His morphological evidence for the noun \mention{self} includes \mention{selfish}, \mention{selfless}, and the plural alternation \mention{self}/\mention{selves}; he analyses the preceding pronominal material as an article. The categorization depends on representational level: article segments occur at intermediate stages, their deepest counterparts are features of nouns, and surface pronouns can receive derivative Noun status.", r"\textcite{postal1966} develops the article--pronoun connection through English reflexives and combinations such as \mention{we men}. His category assignments depend on representational level: article segments occur at intermediate stages, their deepest counterparts are features of nouns, and surface pronouns can receive derivative Noun status. This differs from a proposal about the lexical taxonomy of the surface words.")
replace(r" He also observes that noun status for \mention{self} doesn't decide whether the preceding element is an article or a genitive pronoun.", '')
replace(r"Number supplies a further distinction between determinatives and adjectives. Independent \mention{this}/\allowbreak\mention{these} and \mention{that}/\allowbreak\mention{those} retain overt singular--plural contrasts. The generic human \mention{the rich}, by contrast, is a plural NP whose adjective lacks nominal number inflection and still takes adverb modifiers: \mention{the very rich} \citep[418]{huddleston2002}. The strongest morphological evidence comes from the demonstrative paradigms. The singular and plural specifications of \mention{each} and \mention{several} concern lexical restrictions; NP number alone doesn't distinguish the categories. Other determinatives, such as plural or non-count \mention{some}, remain number-neutral.", r"The demonstrative number contrasts in §\ref{sec:inflection} remain visible in independent uses. Generic human \mention{the rich}, by contrast, is a plural NP whose adjective lacks number inflection and still takes adverb modifiers: \mention{the very rich} \citep[418]{huddleston2002}. The difference concerns overt paradigms, rather than the mere possession of a number value by the whole NP.")
replace(r'\enquote{my car}', r'\enquote*{my car}')
replace(r'\enquote{belongs to me}', r'\enquote*{belongs to me}')

# Keep the clear hierarchy explanation; concentrate the matrix contribution in one paragraph.
between(r'\textcite{reynolds2021} investigates their similarity', 'The grammatical case for nesting needs', r'''\textcite{reynolds2021} compares 138 word forms through properties recorded as present or absent, such as accepting \mention{almost}. Its unsupervised clustering groups forms by these similarities without being given their category labels. The groups broadly resemble the pronoun and determinative inventories, though the outcome varies with initialization and feature selection.\footnote{The study reports 232 properties, whereas the public file contains 155. The accompanying \href{run:matrix-audit.pdf}{\textit{Replication audit of the English determinative--pronoun feature matrix}} documents the discrepancy, reproduces the published statistical decomposition, and examines sensitivity. The public file is preserved unchanged.} But the study contains no common or proper nouns. Distinguishing the two groups therefore establishes neither their taxonomic rank nor the proposed superordinate category.

''')

# The degree restriction already has an NP exception and affects both NP-projecting accounts.
replace(r"These include the quantificational common nouns compared in §\ref{sec:membership}.", r"These include the quantificational common nouns compared in §\ref{sec:quant-nouns}.")
replace(r"The D-noun analysis must preserve that difference between two kinds of NP modifier. It expands NP's range of degree-modifier uses while restricting their positions by head and construction. The resulting cost is that the existing ban on pre-head NP modifiers within attributive AdjPs becomes a narrower condition. Nominal projection alone doesn't license \mention{enough}'s full distribution.", r"This restriction already has an exception involving a quantificational common noun. \textit{CGEL} permits \mention{She's a lot better player than me}, analysing the article belonging to \mention{a lot} as lost after the article determining the larger NP \citep[p.~552, n.~8]{huddleston2002}. The general restriction on NP modifiers in attributive AdjPs is therefore qualified in the baseline grammar." + '\n\n' + r"Extending determinative NP projection to degree uses admits a broader range in those positions. Both ordinary-Head accounts then need to identify the permitted determinative-headed NPs while retaining exclusions such as \ungram{\mention{some a great deal better proposals}}. This cost favours keeping DP against both NP-projecting alternatives; it doesn't independently favour primary D over a determinative subcategory of Noun.")

# Consolidate the accounts in one comparison table, placed after the worked rules.
between(r'Table~\ref{tab:economy} locates the three accounts.', 'The D-noun analysis applies nominal projection', r'''Comparing the ordinary-Head accounts holds projection fixed while varying taxonomy. Comparing the separate-D accounts holds taxonomy fixed while varying headedness. Table~\ref{tab:economy} summarizes their consequences after the rules have been specified.

''')
replace(r"Predication, the disputed wh forms, and modification outside NP structure fall outside this small fragment;", r"Predication, interrogative and relative constructions, and modification outside NP structure fall outside this small fragment;")
replace(r"The subscripts on Mod distinguish pre-head and post-head positions of the same modifier function. The head's entry and construction restrict every dependent. $\mathrm{Mod}_{\mathrm{periph}}$ adds the peripheral premodifier discussed in §\ref{sec:payne}; the compact rule leaves any further NP layering implicit.", r"The head's entry and construction restrict every dependent. $\mathrm{Mod}_{\mathrm{periph}}$ adds the peripheral premodifier discussed in §\ref{sec:payne}; the compact rule leaves further NP layering implicit." + '\n\n' + r"$\mathrm{Mods}_{\mathrm{post}}$ denotes a possibly empty, constructionally ordered sequence of postmodifiers. For compounds, this permits one specialized restrictor followed by ordinary postmodifiers: \mention{useful} precedes \mention{that I found} in \mention{something useful that I found}. It doesn't permit unrestricted repetition of the restrictor. The same sequence notation and ordering conditions apply under all three accounts.")
old = r'(\mathrm{Mod}_{\mathrm{post}})'
assert s.count(old)==3
s=s.replace(old,r'\mathrm{Mods}_{\mathrm{post}}')
replace(r"\mention{Almost} can modify \mention{every} in \mention{almost every teacher}; that permission doesn't license \mention{experienced} as a modifier of \mention{every}.", r"Peripheral \mention{almost} can modify the NP headed by \mention{every}; this doesn't license \mention{experienced} as its modifier.")
replace(r"The disjunction $\{\mathrm{N},\mathrm{D}\}$ groups the same heads for nominal projection. The D-noun analysis expresses this grouping in its lexical hierarchy, giving a point of \term{harmony} between taxonomy and phrase structure. Shared projection supports considering the grouping; its taxonomic rank depends on the broader profile comparison.", r"The disjunction $\{\mathrm{N},\mathrm{D}\}$ groups the same heads for nominal projection. Expressing that grouping in the lexical hierarchy gives the D-noun analysis a point of \term{harmony} between taxonomy and phrase structure. This earns no extra credit for shared rules: both ordinary-Head accounts state them. The preference for including D within Noun rests on the broader profile, as the comparison below makes explicit.")
between('I compare the shared structural core,', r'\textcite{reynolds2026numerals} distinguishes determinative numerals', r'''Table~\ref{tab:economy} compares five criteria across the three accounts, holding the inventory, constructions, and readings fixed. Existing restrictions are distinguished from changes required by the chosen projection rules. Shared rules receive equal credit whether stated through inheritance or a disjunction of categories.

\begin{table}[H]
\centering\small
\caption{Comparative accounting. These are descriptive commitments, not numerical scores. The degree-use comparison extends the ordinary-Head accounts beyond the fragment's NP-internal constructions.}\label{tab:economy}
\setlength{\tabcolsep}{3pt}
\begin{tabular}{>{\raggedright\arraybackslash}p{2.2cm}*{3}{>{\raggedright\arraybackslash}p{3.45cm}}}
\toprule
Criterion & D-noun, ordinary Head & Separate D, ordinary Head & Separate D, fusion \\
\midrule
Shared structural core & Nom--NP and ordinary Head across bare, partitive, and externally determined uses. Adjectival fusion retained. & Same projection and Head relations as D-noun. Adjectival fusion retained. & DP plus nominal structure; Det--Head or Mod--Head for independent determinatives. Fusion shared with adjectives. \\
Primary categories & Determinative inside Noun: one fewer primary category. & Determinative separate from Noun. & Determinative separate from Noun. \\
Internal differences & Modifier permissions stated for subcategories. Internal attachment, where chosen, narrows Noun generalizations. Compound restrictor order and non-recursion retained. & Same modifier permissions and compound conditions, stated for primary D. & DP and Nom separate modifier domains. Same compound restrictor order and non-recursion. \\
Related forms and uses & Cardinal determinatives and cardinal nouns fall within Noun, as do the three lexemes spelled \mention{one}. Internal distinctions retained. & Determinative cardinals and determinative \mention{one} remain primarily separate from nominal counterparts. & Same primary-category divisions as separate D with ordinary Head. \\
Restrictions required & Article-use permissions and \mention{no}/\mention{none} selection retained. Degree uses extend the already qualified restriction on NP modifiers in attributive AdjPs. & Same retained permissions and form selection. Same degree-related extension when NP projection includes these uses. & Same article permissions and form selection. DP--NP distinction retains the degree contrast, including exceptional NP constructions. \\
\bottomrule
\end{tabular}
\end{table}

The articles' restrictions, \mention{no}/\mention{none} form selection, and the compound restrictor conditions are already required in the separate-D grammar. Retaining them isn't an added cost of D-noun. Likewise, differences among existing noun subcategories in determination and modification remain in place (Table~\ref{tab:existing}).

Modifier structure offers choices rather than a single taxonomic test. Peripheral attachment can reuse NP grammar, including inside a smaller NP in Mod function (§\ref{sec:payne}). Where the ordinary-Head description uses internal AdvP attachment, it needs corresponding permissions within Nom. The cost of generalizing NP degree modification is firmer: it applies to both ordinary-Head accounts and extends an existing restriction with an existing \mention{a lot} exception (§\ref{sec:enough}).

On shared structure, the ordinary-Head accounts tie. D-noun reduces the number of primary categories by one, retaining determinative as a subcategory. The preference for that grouping depends on the semantic, syntactic, and morphological comparison, especially the common-noun connections in §\ref{sec:quant-nouns}.

''')
replace(r"The choice turns on whether the shared profile warrants that parent category, with the modifier restrictions counted against it;", r"The choice turns on whether the shared profile warrants that parent category, with the modifier commitments compared at the levels they affect;")
replace(r"Quantificational common nouns make the connection especially clear: their selected partitives and restricted dependents already occupy part of the grammatical territory associated with determinatives.", r"Quantificational common nouns make the connection especially clear: their selected complements, number transparency, and restricted dependents already occupy part of the grammatical territory associated with determinatives.")

assert 'sec:wh-boundary' not in s
assert 'sec:word-formation' not in s
assert 'the existing ban' not in s
assert 'Internal cases such as' not in s
assert s.count(r'\begin{table}')==5
assert s.count(r'\begin{forest}')==11
p.write_text(s)
print('Consolidated source:',len(s),'characters')
