from pathlib import Path
import json
import re

root = Path.cwd()
snap = root / 'notes/snapshots/2026-09-12-reorganization'
units = {int(x['id']): x['text'] for x in json.loads((snap / 'units.json').read_text())}
used = {}
chunks = []


def put(text, *sources):
    chunks.append(text.strip())
    for n in sources:
        used.setdefault(n, []).append(len(chunks))


def keep(n, *replacements):
    text = units[n]
    for before, after in replacements:
        assert before in text, (n, before)
        text = text.replace(before, after)
    put(text, n)


def section(title, label):
    put(r'\section{' + title + r'}\label{' + label + '}')


def subsection(title, label):
    put(r'\subsection{' + title + r'}\label{' + label + '}')


keep(1)
put(r'''\begin{abstract}
I argue that English determinatives, including articles, demonstratives, and quantifiers, belong within Noun alongside common nouns, proper nouns, and pronouns. Quantificational common nouns provide the closest comparison: they share complement patterns, number transparency, and restricted dependents with parts of the determinative inventory. The strongest adjectival counterweight connects grade, degree modification, and comparative complementation in four quantifiers. Number and referential contrasts supply further nominal connections. Restricted articles belong to the grouping through their integration into the determinative system.

A separate comparison asks how determinative expressions are headed. Ordinary Head unifies bare, partitive, and externally determined uses, but is available whether determinative is within Noun or separate. A matched grammatical fragment gives those alternatives equal credit for shared structure and identifies their common costs in degree modification. A final comparison favours coordinate rank alongside pronoun over nesting within it.
\end{abstract}''', 28)
keep(32)

section('The question and the alternatives', 'sec:intro')
keep(36)
keep(38)
keep(40)
put(r'''Compare \mention{take some apples} with \mention{take some}. The word \mention{some} remains determinative in both. Before \mention{apples}, its phrase functions as determiner; without \mention{apples}, the whole expression functions as object. The issue is how these uses fit the lexical taxonomy and the structure of the noun phrase.''', 46)
put(r'''Two decisions need separating. The first is whether determinatives belong within Noun. The second is whether expressions such as independent \mention{some} have an ordinary \term{Head}, the element around which a phrase is built. The D-noun analysis licenses that headedness through Noun membership. A grammar retaining a separate determinative category can license it too. Table~\ref{tab:accounts} identifies the three accounts compared here.''', 44, 106)
put(r'''\begin{table}[H]
\centering\small
\caption{The three accounts compared. All retain one determinative category across dependent and independent uses and keep \mention{apples} as Head in \mention{some apples}.}\label{tab:accounts}
\begin{tabular}{>{\raggedright\arraybackslash}p{3.6cm}>{\raggedright\arraybackslash}p{4.1cm}>{\raggedright\arraybackslash}p{4.4cm}}
\toprule
Account & Place of determinative & Independent \mention{some} \\
\midrule
D-noun, ordinary Head & A subcategory of Noun & Ordinary Head, inherited from Noun \\
Separate D, ordinary Head & A primary category alongside Noun & Ordinary Head, licensed for both Noun and D \\
Separate D, fusion & A primary category alongside Noun & Joint determiner and Head functions \\
\bottomrule
\end{tabular}
\end{table}''')
put(r'''In \textit{CGEL}, independent \mention{some} jointly realizes determiner and Head through a \term{fusion of functions} \citep[410--412]{huddleston2002}. Ordinary headedness assigns it Head alone. Both accounts give the whole independent expression noun-phrase (NP) status. The choice concerns its internal structure; assigning NP status doesn't by itself decide the lexical category of its head.''', 350)
keep(114)
keep(116)
put(r'''Here D abbreviates the lexical category determinative, and DP means \term{determinative phrase}, as in \textit{CGEL}. It is distinct from the DP of the DP hypothesis, where D heads the whole expression \mention{some apples}. The three accounts in Table~\ref{tab:accounts} all retain \mention{apples} as that expression's head.''', 48)
keep(118)
put(r'''Ordinary Head also has costs. Extending NP projection to determinatives used as degree modifiers broadens the permitted range of NP modifiers in adjective phrases. That commitment affects both ordinary-Head accounts (§\ref{sec:enough}). Their shared structural gains and costs leave the category decision to the broader grammatical comparison.''')
keep(42, (r"The question is whether determinatives' combined semantic, syntactic, and morphological profile warrants the corresponding extension of Noun.", r"These precedents motivate comparing the whole grammatical profile, rather than requiring every member to display each nominal property."))
put(r'''The comparison weighs three considerations: how broadly a property occurs, how it recurs across constructions, and how specifically it connects the groups. These considerations apply equally to nominal and adjectival connections. A pattern concentrated in a few words can be substantial evidence; its contribution depends on its grammatical relationships as well as its reach.''', 172)
put(r'''Earlier accounts connect articles with pronouns or give both nominal structure, but differ in their inventories and analytical levels. Appendix~\ref{sec:historical} preserves that comparison. Hudson's nested noun taxonomy is considered in §\ref{sec:inheritance}; Spinillo's redistribution of determinatives in §\ref{sec:articles}. Neither is equivalent to the separate-D ordinary-Head alternative in Table~\ref{tab:accounts}.''', 154)
put(r'''Section~\ref{sec:proposal} compares the grammatical profiles, and §\ref{sec:articles} completes the case for the intended inventory. Section~\ref{sec:evidence} then compares internal structures, which the fragment in §\ref{sec:economy} makes explicit and assesses. The further question of coordinate or nested rank follows in §\ref{sec:inheritance}.''', 108)

section('Grounds for a broader Noun category', 'sec:proposal')
put(r'''The existing Noun category contains common nouns, proper nouns, and pronouns with markedly different meanings, inflection, and dependents. Ordinary count nouns alone are an inadequate comparison group. The question is how determinatives connect with that broader range, and how those connections compare with their affinities to adjectives.''')
subsection('Functions and constructional range', 'sec:independent')
put(r'''The external syntax of a phrase concerns the functions it fills in larger constructions. Noun phrases can serve as subjects, objects, and complements of prepositions. Determinatives enter these constructions too, with the lexical restrictions illustrated below.''', 203)
keep(320)
keep(322, (r'The competing analyses assign different internal structures to independent \mention{some}.', r'The comparison concerns the phrases\x27 functions; §\ref{sec:evidence} considers their internal structure.'.replace(r'\x27', "'")))
keep(324)
keep(325)
keep(331)
keep(333)
keep(335, (r'Section~\ref{sec:modification} returns to the fuller adjectival comparison.', r'The broader comparison has to include dependents, inflection, and interpretation as well as external position.'))
put(r'''Determiner function also cuts across the existing noun subcategories. In \mention{my preferences}, \mention{Kim's preferences}, and \mention{people's preferences}, the determiner is an NP ultimately headed by a pronoun, a proper noun, and a common noun respectively \citep[354--355, 470--471]{huddleston2002}.\footnote{\textit{CGEL} assigns these genitives the combined function Subject--Det \citep[472--473]{huddleston2002}. I treat them as Det here, without the additional subject function.}''', 235)
put(r'''The compound determinative \mention{someone}, following the categorization of \textcite[§1.3]{Payne2007}, participates in \mention{someone's preferences}. Plain-case NPs also fill Det: \mention{what size} in \mention{what size shoes}, \mention{that size} in \mention{that size shoes}, and \mention{Sunday} in \mention{Sunday morning} \citep[356]{huddleston2002}.''', 250, 254)
put(r'''Determiner is nevertheless the characteristic function of determinative phrases. This specialization could support a separate primary category. Its tasks are themselves closely connected with nominal reference: Det marks definiteness and often contributes quantification \citep[354--359]{huddleston2002}. The issue is whether that specialization warrants a primary boundary or a distinction within Noun.''', 233)
keep(256, (r'These existing NP determiners give the extension a functional basis.', r'The existing NP determiners provide a positive comparison.'))
keep(258)
keep(205)
put(r'''Relative-clause postmodification supplies a further constructional comparison. Common nouns freely take integrated relatives, as in \mention{people who came}; personal pronouns permit a restricted range, including \mention{we who have read the report} \citep[430]{huddleston2002}. Determinative examples include \mention{few who come ever leave}, \mention{those who came}, \mention{that which remains}, and \mention{something that you need to know}.''', 296)
put(r'''Compounds also permit \mention{anyone who asks} and \mention{everything that matters}. With books under discussion, compare \mention{some that I saw} and \mention{two that I have seen}. \textit{CGEL} describes relative postmodification with demonstratives and compounds \citep[414, 422--423]{huddleston2002}. The shared construction leaves the lexical head's category and internal Head relations to be assessed.''', 436)
put(r'''Compound determinatives also take post-head adjectives. CGELBank attests \mention{I need something reliable and good looking}.\footnote{Sentence \href{https://github.com/nert-nlp/cgel/blob/d0a2c2d8c522b23d5aa879fc9cb94948f4285b2c/datasets/ewt-test_iaa50.cgel\#L179-L181}{\nolinkurl{answers-20111024111513AAAQhAO_ans-0003}} in \nolinkurl{ewt-test_iaa50.cgel}.} The position and interpretation of these modifiers have specialized conditions (§\ref{sec:compounds}). Their occurrence adds to the range of constructions the competing grammars have to accommodate.''', 478)

subsection('The connection from quantificational common nouns', 'sec:quant-nouns')
keep(221)
keep(223)
keep(225)
keep(227)
keep(229)
put(r'''The comparison is specific to these constructions. Common nouns also permit a wider range of PP and clausal complements, whereas pronouns and primary naming uses of proper nouns have much more restricted dependents \citep[429--430, 439--443, 517--521]{huddleston2002}. Partitives such as \mention{a lot/some of the wine} connect established common nouns with determinatives without making their complement systems identical.''', 211)

subsection('The connected adjectival profile', 'sec:adjectival-profile')
put(r'''The strongest adjectival connection also concerns a restricted group: \mention{few}, \mention{many}, \mention{much}, and \mention{little}. They distinguish plain, comparative, and superlative forms: \mention{few}/\allowbreak\mention{fewer}/\allowbreak\mention{fewest}, \mention{many}/\allowbreak\mention{more}/\allowbreak\mention{most}, and corresponding paradigms for \mention{little} and \mention{much} \citep[391--395]{huddleston2002}. Grade combines with degree-modifier selection and comparative complementation, as in \mention{more than ten}. The three properties form a connected profile.''', 213, 308)
keep(286)
keep(288)
put(r'''Approximative and focusing modifiers have a broader distribution. Compare \mention{almost every}, \mention{nearly all}, \mention{hardly any}, \mention{practically no}, \mention{almost everyone}, and \mention{almost ten}. They have counterparts in established NP modification: \mention{almost the whole class}, \mention{hardly a day}, and \mention{only the best}. In \mention{almost every student}, \mention{almost} approximates the quantity; it doesn't intensify a gradable property of \mention{every}.''', 284)
put(r'''The broad approximative pattern and the degree series thus make different contributions to the profile. The former has parallels in NP grammar; the latter connects the four quantifiers with adjectives. Section~\ref{sec:payne} develops the proposed attachment analysis. That analysis explains the modifier contrast but is available under either ordinary-Head taxonomy.''')
put(r'''Even the gradable forms have syntax distinct from adjectives: \mention{so many mistakes} contrasts with \ungram{\mention{so numerous mistakes}} \citep[392--396, 431--432, 539--540]{huddleston2002}. Their determining, independent, and partitive uses also connect them with other determinatives. The question is how to represent both sets of connections, rather than whether the adjectival properties are real.''')
keep(484)
keep(209)
keep(486)
keep(488)
keep(440)

subsection('Number, genitive marking, and reference', 'sec:inflection')
keep(302)
keep(304)
keep(438, (r'The demonstrative number contrasts in §\ref{sec:inflection} remain visible in independent uses.', r'The demonstrative number contrasts remain visible in independent uses.'))
keep(306)
keep(197)
keep(199)
keep(201)
keep(207)
put(r'''Inflection and reference provide partial connections, with different reach. Demonstrative number directly compares forms of determinative lexemes with nominal number paradigms; compound genitives may depend on their nominal component. The \mention{no}/\allowbreak\mention{none} alternation concerns form selection, discussed with restricted membership in §\ref{sec:form-selection}. None of these properties is a necessary condition for every member of Noun.\footnote{Derivations such as \mention{nothingness} and \mention{oneness} are weaker category diagnostics: \mention{-ness} also attaches to adjectives and other bases \citep[Ch.~19, §5.7.2(i)]{huddleston2002}. Numeral morphology likewise needs its inputs distinguished. \textcite[§§5.4--5.5]{reynolds2026numerals} derives fractional nouns from cardinal nouns and treats \mention{two thousand and twenty-seventh} as a coordination whose final coordinate is adjectival. Neither process independently establishes determinative nounhood.}''', 310, 312)

subsection('Weighing the profiles', 'sec:membership')
put(r'''Table~\ref{tab:existing} summarizes the comparison. Functions concern phrases, while inflection concerns word forms. The modification rows also identify the proposed analysis of determinative attachment; those structural assignments are explained in §\ref{sec:payne}. The rows are not equally weighted tests, and several properties belong to a single connected pattern.''')
profile = units[174]
rows = profile.split(r'\midrule', 1)[1].split(r'\bottomrule', 1)[0].strip().splitlines()
assert len(rows) == 11
order = [1, 7, 8, 10, 9, 2, 4, 5, 6, 3, 0]
rows = [rows[i] for i in order]
rows[2] = rows[2].replace(r'Degree AdvP on four quantifiers; NP modifiers; \mention{the lucky few}; relatives', r'\mention{the lucky few}; relatives; internal degree AdvP and NP modifiers under the proposed analysis')
rows[4] = rows[4].replace(r'\mention{almost every}; \mention{hardly any}; \mention{almost ten}', r'\mention{almost every}, \mention{hardly any}, \mention{almost ten}: proposed NP attachment')
profile = profile.split(r'\midrule',1)[0] + '\\midrule\n' + '\n'.join(rows) + '\n\\bottomrule' + profile.split(r'\bottomrule',1)[1]
profile = profile.replace('Representative profiles. Functions concern phrases; internal and peripheral modification concern Nom and NP respectively. Interrogative and relative forms follow', 'Profile summary. Internal and peripheral attachment in the determinative column are analytical commitments, not independent diagnostics. Interrogative and relative forms follow')
put(profile, 174)
put(r'''Both the nominal and adjectival connections are unevenly distributed. Quantificational common nouns supply a connected comparison involving quantity, complements, agreement, and restricted dependents. The four gradable quantifiers supply a connected adjectival profile. Concentration in a subgroup doesn't make either comparison negligible. Their significance depends on how each pattern connects with the rest of the inventory.''')
put(r'''I give greater weight to the recurring nominal profile. Argument and determiner functions, partitives, relative postmodification, and number and referential contrasts connect determinatives with established parts of Noun. Within this range, the gradable quantifiers retain their determining and independent uses alongside the degree pattern. Keeping them within determinative expresses those connections while locating the grade and degree restrictions in a narrower group.''', 215)
put(r'''This supports including determinative within Noun while preserving its distinctive profile. It leaves two tasks: establishing why the proposed inventory includes articles and other restricted members, and assessing the ordinary-Head implementation. Shared nominal projection can then express the grouping through inheritance; its availability under separate D remains part of the structural comparison.''', 217)

section('Restricted members and the scope of the grouping', 'sec:articles')
put(r'''The category-level argument draws on constructions that many determinatives enter. Articles lack ordinary independent uses, so their inclusion needs a further argument: they belong to the determinative system whose broader profile supports Noun membership. The \mention{no}/\mention{none} paradigm raises a related question about restrictions on forms.''', 512)
subsection('Articles within the determinative system', 'sec:article-membership')
keep(516)
keep(518)
keep(520)
keep(522)
keep(524)
keep(164, (r'Section~\ref{sec:articles} assesses this cluster against the connections each member retains with the wider inventory.', r'The issue is whether this cluster warrants separating the trio from the wider determinative system.'))
keep(526)
keep(528)
keep(166)
keep(530)
keep(532)
subsection('Dependent and independent forms', 'sec:form-selection')
keep(536)
put(r'''The broader grouping therefore preserves two distinctions: between members' permitted constructions, and between the forms selected within a paradigm. A successful structural account has to respect both. The following section compares the Head relations once an expression's use is licensed.''')

section('Ordinary Head, fusion, and modifier attachment', 'sec:evidence')
put(r'''The category comparison and membership argument leave a structural choice. How should a grammar represent independent \mention{some}, \mention{some of the wine}, and \mention{the lucky few}? All are overt expressions with nominal uses. Ordinary headedness gives their determinatives Head; fusion combines Head with a dependent function. Each analysis preserves some generalizations and requires particular restrictions.''', 316, 492)
subsection('The basic Head relations', 'sec:head-relations')
put(r'''A \term{nominal} (Nom) contains a head and its internal dependents, excluding an external determiner. In \mention{some apples}, the word \mention{apples} heads Nom, and that Nom heads NP. The same arrangement permits an internal modifier, as in \mention{some red apples}, without making the determining phrase part of the Nom.''')
put(r'''Under D-noun, a determinative can head this Nom--NP structure too. Figure~\ref{fig:some} compares the accounts for \mention{take some apples} and \mention{take some}. The dependent expression still has \mention{apples} as its ultimate head. Independent \mention{some} has ordinary Head under D-noun; in \textit{CGEL}, its DP jointly fills Det of NP and Head of Nom.''')
keep(50)
put(r'''The proposed hierarchy makes this structure available through \term{inheritance}: properties stated for Noun apply to its subcategories, subject to their restrictions. The separate-D ordinary-Head account can use the same structures by admitting both Noun and D into the projection rule. Figure~\ref{fig:some}'s structural contrast therefore concerns ordinary Head and fusion, rather than a benefit unique to the broader taxonomy.''')
put(r'''The genitive NP \mention{Kim's} already fills Det in \mention{Kim's preferences}, as Figure~\ref{fig:genitive} shows. Ordinary determinative headedness gives \mention{some} that phrase type in Det and object uses alike. Plain determinative-headed NPs, such as \mention{almost ten} in \mention{almost ten apples}, then join genitives such as \mention{Kim's} and \mention{my}. The fragment compares the remaining selectional conditions (§\ref{sec:det-uniform}).''', 252)
keep(237)

subsection('Syntactic completeness and contextual interpretation', 'sec:saturation')
keep(339)
keep(341)
keep(342)
keep(346)
keep(348)
put(r'''Fusion offers another representation of that complete expression. In \textcite{Payne2007}, one constituent jointly realizes Head and a dependent function, subject to structural and adjacency conditions. Contextual recovery alone doesn't decide between this arrangement and ordinary Head. Both analyses retain an overt determinative and can express the restriction supplied by context.''')
subsection('Partitives and externally determined expressions', 'sec:modification')
keep(360)
keep(362)
keep(364)
keep(366)
keep(379)
keep(383)
keep(385)
keep(387)
keep(413)
keep(415)
keep(430)
keep(432)
keep(434)
put(r'''The preferred analysis thus unifies bare, partitive, and externally determined determinatives under ordinary Head. It retains fusion for adjectives such as \mention{rich}. The choice has a structural benefit, but its value depends on the modifier permissions and other conditions needed elsewhere.''', 442)

subsection('Modifier selection and attachment', 'sec:payne')
put(r'''The selection and ordering contrast in §\ref{sec:adjectival-profile} guides the attachment analysis. Approximative and focusing modifiers have established NP parallels; the degree series selects the four gradable quantifiers. Both ordinary-Head accounts can represent that difference by distinguishing NP-peripheral modification from modification inside Nom.''')
keep(282)
keep(262, (r'Two premodifier patterns need distinguishing: approximative and focusing adverbs, and the degree series exemplified by \mention{very} and \mention{so}. ', ''))
keep(264)
keep(280)
keep(290)
keep(292)
keep(294)
keep(298)

subsection('Compounds and their modifier domains', 'sec:compounds')
keep(446)
keep(448)
keep(474)
keep(476)
put(r'''The same division applies to \mention{someone} and \mention{everybody}: the compound construction licenses the post-head restrictor, while the determinative base supplies its premodifier permissions. The attested \mention{something reliable and good looking} illustrates the post-head pattern (§\ref{sec:independent}).''')
keep(480)

subsection('Independent genitives', 'sec:genitive-head')
keep(352)
keep(354)
keep(356)
put(r'''Ordinary Head now provides a common representation across the determinative constructions, with a bounded extension to genitives already within Noun. The remaining question is whether the shared structure is economical once all permissions and restrictions are explicit.''')

section('The matched fragment and comparative costs', 'sec:economy')
put(r'''A grammatical \term{fragment} states rules for a specified range of constructions. Here the three accounts receive the same judgments and lexical restrictions. The comparison asks what structures and conditions each needs to describe that range. Agreement with the shared inputs establishes coverage within the fragment; it isn't a further independent test of the taxonomy.''', 564)
subsection('Scope and use permissions', 'sec:fragment')
put(r'''The fragment covers determination, ordinary subject and object uses, partitives, and the modifier and compound comparisons in §\ref{sec:evidence}. It admits relative clauses as postmodifiers but doesn't analyse their internal grammar. Predication, interrogative clause structure, and modification outside NP structure lie beyond its scope. Degree uses enter the wider accounting in §\ref{sec:enough}.''', 566)
keep(568)
keep(570)
keep(587)
keep(160, (r'Hudson also distinguishes dependency from external headedness.', r'Hudson distinguishes dependency from external headedness.'))
keep(162, (r'(§\ref{sec:fragment})', ''))

subsection('Shared phrase types and projection rules', 'sec:det-uniform')
keep(552)
keep(553)
keep(560)
keep(589)
keep(591)
keep(593)
keep(594)
keep(601)
keep(603, (r'discussed by Hudson (§\ref{sec:related})', r'discussed by Hudson'))
keep(605)
keep(607)
keep(609)
keep(611)
keep(613)
keep(615)
keep(616)
keep(619)
keep(621)
keep(622)
keep(629)
keep(631)
keep(633)
keep(635)

subsection('Degree uses outside noun phrases', 'sec:enough')
put(r'''The fragment's NP constructions leave a further cost to be assessed. Determinatives also modify expressions outside NP structure. Giving these uses NP projection affects which kinds of phrase the grammar admits as degree modifiers.''')
keep(538)
keep(540)
keep(542)
keep(544)
keep(546)

subsection('The comparative judgment', 'sec:costs')
put(r'''Table~\ref{tab:economy} separates shared structure, internal permissions, existing restrictions, the additional degree-use cost, and taxonomic consequences. The last row groups consequences of the same recategorization rather than counting them as separate gains. The comparison holds the inventory, constructions, and readings fixed.''', 639)
economy = units[641]
start, tail = economy.split(r'\midrule',1)
end = tail.split(r'\bottomrule',1)[1]
rows = r'''Shared structure & Nom--NP and ordinary Head across bare, partitive, and externally determined uses. Adjectival fusion retained. & Same projection and Head relations as D-noun. Adjectival fusion retained. & DP plus nominal structure; Det--Head or Mod--Head for independent determinatives. Fusion shared with adjectives. \\
Internal permissions & Internal degree AdvP on \mention{few}, \mention{many}, \mention{much}, \mention{little}; approximatives after Det with independent cardinals. & Same internal permissions, stated for primary D; same peripheral NP modification. & DP and Nom separate the premodifier and nominal postmodifier domains. \\
Existing restrictions & Article-use permissions, \mention{no}/\mention{none} selection, and compound restrictor order and non-recursion retained. & Same lexical and constructional restrictions retained. & Same lexical and constructional restrictions retained. \\
Additional degree-use cost & NP degree modifiers require a broader permission in attributive AdjPs, preserving the remaining exclusions. & Same extension when NP projection includes degree uses. & DP--NP distinction retains the degree contrast, including exceptional NP constructions. \\
Taxonomic consequences & One fewer primary category. Cardinal uses and the three lexemes spelled \mention{one} fall within Noun; internal distinctions remain. & D remains separate. Determinative cardinals and determinative \mention{one} remain primarily separate from nominal counterparts. & Same primary-category divisions as separate D with ordinary Head. \\
'''
put(start + '\\midrule\n' + rows + r'\bottomrule' + end, 641)
keep(658)
put(r'''The ordinary-Head accounts tie on shared structure. Both use peripheral NP modification and the same internal modifier permissions (§\ref{sec:payne}); both incur the further degree-use cost (§\ref{sec:enough}). D-noun expresses the shared projection through inheritance, while separate D states a rule applying to both primary categories. The preference between them depends on the profile comparison in §\ref{sec:proposal}.''', 660, 662)
keep(664)
keep(666)
keep(668)
keep(670)
keep(672)
keep(674)

section('Coordinate or nested subcategories', 'sec:inheritance')
keep(496, ('leaves a second question', 'leaves a further question'))
keep(156)
keep(158)
keep(498)
keep(500)
keep(502)
keep(504)
keep(506)
keep(508)
put(r'''The fragment doesn't distinguish those inheritance paths: either can supply its nominal structures (§\ref{sec:det-uniform}). The preference for coordinate rank concerns the more specific grammatical profile. A reader can accept the broader Noun grouping and ordinary Head while preferring Hudson's additional level.''')

section('Conclusion', 'sec:conclusion')
put(r'''I propose including English determinatives within Noun. The strongest positive comparison comes from quantificational common nouns: their selected complements, number transparency, restricted dependents, and degree uses connect with parts of the determinative inventory. The connected adjectival profile of the four gradable quantifiers deserves weight on the same terms. Broader constructional and referential connections, with partial inflectional corroboration, favour the nominal grouping.''', 678)
put(r'''The grouping includes restricted members through their integration into the determinative system. Articles needn't independently exhibit the whole profile, and \mention{no}/\mention{none} retains its form-selection conditions. The argument for membership thus concerns a category with internal differences, rather than unrestricted use by every form.''', 680)
put(r'''Ordinary Head provides a uniform structure for bare, partitive, and externally determined determinatives. Both D-noun and separate D can license it, and both incur the additional degree-modifier cost. I prefer the broader taxonomy because the profile supports placing the shared structure within Noun. Coordinate rank alongside pronoun is a further preference: the present comparisons don't establish the additional shared rules that nesting would express.''', 682)

put(r'\appendix')
section('Earlier accounts and logical alternatives', 'sec:historical')
put(r'''Keeping a word in one category across dependent and independent uses leaves its taxonomic position open. As \textcite[232--235]{lyons1968} observes, distribution can be compared at different levels: two expressions may belong together at one level and differ at a more specific level. Table~\ref{tab:rivals} distinguishes the selected authors' proposals, their analytical levels, and further logical alternatives.''', 122)
keep(124)
keep(148)
keep(150)
keep(152)
put(r'''These predecessors challenge a fundamental article--pronoun separation but leave the full determinative inventory uncategorized. Its contrasts in grade, modification, complementation, and restricted independent use extend beyond their proposals. Hudson's explicit nesting and Spinillo's redistribution are assessed in §§\ref{sec:inheritance} and~\ref{sec:articles}, respectively.''')
keep(684)
keep(686)
keep(688)
keep(691)

text = '\n\n'.join(chunks) + '\n'
text = text.replace(r'conditions .', 'conditions.')
(root / 'determinatives-as-nouns.tex').write_text(text)
(snap / 'movement-map.json').write_text(json.dumps({'source_units_used': used, 'unused_units': {n: t for n, t in units.items() if n not in used}}, indent=2, ensure_ascii=False) + '\n')
print('Wrote reorganized manuscript:', len(chunks), 'blocks')
print('Unused prose units:', [n for n in units if n not in used and not units[n].startswith(r'\section') and not units[n].startswith(r'\subsection')])
