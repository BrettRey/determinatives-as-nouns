from pathlib import Path

root = Path.cwd()
path = root / 'determinatives-as-nouns.tex'
text = path.read_text()


def change(before, after):
    global text
    assert text.count(before) == 1, (text.count(before), before)
    text = text.replace(before, after)


change('A grammar retaining a separate determinative category can license it too.',
       'A grammar retaining a separate determinative category (D) can license it too.')
change(r'''Here D abbreviates the lexical category determinative, and DP means \term{determinative phrase}, as in \textit{CGEL}. It is distinct from the DP of the DP hypothesis, where D heads the whole expression \mention{some apples}. The three accounts in Table~\ref{tab:accounts} all retain \mention{apples} as that expression's head.''',
       r'''Here DP means \term{determinative phrase}, as in \textit{CGEL}. This differs from the DP-hypothesis usage just described.''')
change('Extending NP projection to determinatives used as degree modifiers broadens the permitted range of NP modifiers in adjective phrases.',
       'Treating determinatives used as degree modifiers as NP heads broadens the permitted range of NP modifiers in adjective phrases (AdjPs).')
change(r'''Earlier accounts connect articles with pronouns or give both nominal structure, but differ in their inventories and analytical levels. Appendix~\ref{sec:historical} preserves that comparison. Hudson's nested noun taxonomy is considered in §\ref{sec:inheritance}; Spinillo's redistribution of determinatives in §\ref{sec:articles}. Neither is equivalent to the separate-D ordinary-Head alternative in Table~\ref{tab:accounts}.''',
       r'''Earlier accounts connect articles with pronouns or give both nominal structure, at different analytical levels (Appendix~\ref{sec:historical}). Hudson's nested noun taxonomy is considered in §\ref{sec:inheritance}; Spinillo's redistribution of determinatives in §\ref{sec:articles}.''')
change('Determiner is nevertheless the characteristic function of determinative phrases.',
       'Determiner remains the characteristic function of determinative phrases.')
change(' The shared construction leaves the lexical head\'s category and internal Head relations to be assessed.', '')
change(r'''CGELBank attests \mention{I need something reliable and good looking}.''',
       r'''CGELBank, a treebank annotated in the \textit{CGEL} framework \citep{reynolds2023unified}, attests \mention{I need something reliable and good looking}.''')
change(' Their occurrence adds to the range of constructions the competing grammars have to accommodate.', '')
change(r'''The broad approximative pattern and the degree series thus make different contributions to the profile. The former has parallels in NP grammar; the latter connects the four quantifiers with adjectives. Section~\ref{sec:payne} develops the proposed attachment analysis. That analysis explains the modifier contrast but is available under either ordinary-Head taxonomy.''',
       r'''The broader approximative pattern supplies NP parallels distinct from the four quantifiers' adjectival profile. Section~\ref{sec:payne} develops an attachment analysis of that contrast, available under either ordinary-Head taxonomy.''')
change(' Their determining, independent, and partitive uses also connect them with other determinatives. The question is how to represent both sets of connections, rather than whether the adjectival properties are real.', '')
change(r'''Table~\ref{tab:existing} summarizes the comparison. Functions concern phrases, while inflection concerns word forms. The modification rows also identify the proposed analysis of determinative attachment; those structural assignments are explained in §\ref{sec:payne}. The rows are not equally weighted tests, and several properties belong to a single connected pattern.''',
       r'''Table~\ref{tab:existing} summarizes the comparison. Functions concern phrases, while inflection concerns word forms. AdjP and AdvP denote adjective and adverb phrases. The modification rows identify proposed determinative attachments, explained in §\ref{sec:payne}. The rows aren't equally weighted tests, and several properties belong to one connected pattern.''')
change(r'''This supports including determinative within Noun while preserving its distinctive profile. It leaves two tasks: establishing why the proposed inventory includes articles and other restricted members, and assessing the ordinary-Head implementation. Shared nominal projection can then express the grouping through inheritance; its availability under separate D remains part of the structural comparison.''',
       r'''The broader Noun grouping still needs an account of restricted members. Their inclusion depends on how they participate in the determinative system.''')
change(r'''The D-noun analysis retains the shared determining profile and records the absence of independent use in lexical permissions. The articles' nounhood depends on their membership in that broader system. They don't individually exhibit the full evidence that supports the parent category.

''', '')
change(r'''The D-noun analysis preserves this relation. Ordinary Head structure licenses \mention{none of the students}; it doesn't license \ungram{\mention{no of the students}}.''',
       r'''The partitive \mention{none of the students} requires the independent form; \ungram{\mention{no of the students}} is excluded.''')
change('The broader grouping therefore preserves two distinctions:',
       'The broader grouping preserves two distinctions:')
change(r'''The proposed hierarchy makes this structure available through \term{inheritance}: properties stated for Noun apply to its subcategories, subject to their restrictions. The separate-D ordinary-Head account can use the same structures by admitting both Noun and D into the projection rule. Figure~\ref{fig:some}'s structural contrast therefore concerns ordinary Head and fusion, rather than a benefit unique to the broader taxonomy.''',
       r'''Under D-noun, \term{inheritance} makes Noun's projection rules available to determinatives, subject to their restrictions. The separate-D ordinary-Head account can use the same trees by admitting both Noun and D into those rules.''')
change(r'''Ordinary Head now provides a common representation across the determinative constructions, with a bounded extension to genitives already within Noun. The remaining question is whether the shared structure is economical once all permissions and restrictions are explicit.''',
       r'''The fragment now makes the permissions and restrictions explicit so that the structural accounts can be compared.''')
change(r'''A grammatical \term{fragment} states rules for a specified range of constructions. Here the three accounts receive the same judgments and lexical restrictions. The comparison asks what structures and conditions each needs to describe that range. Agreement with the shared inputs establishes coverage within the fragment; it isn't a further independent test of the taxonomy.''',
       r'''A grammatical \term{fragment} states rules for a specified range of constructions. The three accounts receive the same judgments and lexical restrictions. Comparing the rules needed for coverage makes their commitments explicit; it doesn't test them against new data.''')
change(r'''In the present phrase-structure analysis, the noun can remain Head while both constituents impose such conditions. Including determinatives within Noun neither explains away the selection facts nor requires mutual headedness; it concerns the selecting words' superordinate category.''',
       r'''The noun can remain Head while both constituents impose these conditions.''')
change(r'''Keeping ordinary headedness while retaining primary D gives the strongest separate-D alternative. It retains the NP and use-permission rules, but replaces the lexical-head restriction in Nom with:''',
       r'''Under separate D with ordinary Head, the NP and use-permission rules are the same. Its Nom rule admits either Noun or determinative as lexical head:''')
change(r'''The ordinary-Head accounts share nominal projection and Head relations. Once a member's use is licensed, its nominal structure follows from the shared rules; lexical and constructional conditions still determine the available functions and dependents. Dependent determinatives acquire a Nom layer in both. One account supplies these common structural expectations through inheritance from Noun, the other through a rule admitting both N and D.

The disjunction $\{\mathrm{N},\mathrm{D}\}$ groups the same heads for nominal projection. Expressing that grouping in the lexical hierarchy gives the D-noun analysis a point of \term{harmony} between taxonomy and phrase structure. This earns no extra credit for shared rules: both ordinary-Head accounts state them. The preference for including D within Noun rests on the broader profile, as the comparison below makes explicit.''',
       r'''Both ordinary-Head accounts give dependent determinatives a Nom layer. The disjunction $\{\mathrm{N},\mathrm{D}\}$ admits the same heads that inherit projection under D-noun. Putting the grouping in the lexical hierarchy produces \term{harmony} between taxonomy and phrase structure, but earns no additional credit for rules both accounts share.''')
change(r'''I favour the broader Noun category because it places the recurring nominal structure at the shared level and preserves the determinative distinctions where their restrictions apply. The alternative retains a primary boundary and crosses it in the projection rule. Both are coherent grammars. The choice turns on whether the shared profile warrants that parent category, with the modifier commitments compared at the levels they affect; reducing the number of primary categories alone wouldn't suffice.''',
       r'''I favour the broader Noun category because the profile comparison supports placing the shared nominal structure at that level. Determinative restrictions remain within it. Separate D crosses a primary boundary in its projection rule; that is a coherent alternative. Reducing the number of primary categories alone wouldn't establish the preference.''')
change(r'''The fragment doesn't distinguish those inheritance paths: either can supply its nominal structures (§\ref{sec:det-uniform}). The preference for coordinate rank concerns the more specific grammatical profile. A reader can accept the broader Noun grouping and ordinary Head while preferring Hudson's additional level.''',
       r'''Both inheritance paths supply the fragment's structures (§\ref{sec:det-uniform}). The coordinate preference rests on the more specific profile; accepting Noun membership and ordinary Head leaves this further choice open.''')

path.write_text(text)
print('Reader-facing consolidation applied.')
