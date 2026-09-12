This is an independent simulated scholarly review of a theoretical English grammar paper for readers of Journal of Linguistics. It is not a real scholar's opinion or a journal decision. Read the complete article and its two accompanying supplements below. The objective is to test whether its argument is clearly and adequately supported, and identify concrete revisions where it is not.

You receive no earlier review or revision history. Work from the artifact itself. Understand the argument before criticizing it. State the strongest relevant alternative, then identify exact assumptions and consequences on which your judgment depends. Generate possible remedies where needed; no remedy has been supplied for you to approve. Do not assume that superior empirical coverage, minimum description length or causal homeostasis is the author's claim: assess what the paper actually undertakes, and justify any additional standard you think it must meet. Equally, do not accept a preference merely because it is carefully qualified. Protect the difference between a central idea worth pursuing and its present exposition or support.

The supplied persona comes from a standing board; any section pointers refer to an older draft. Locate the corresponding passage in this draft. Treat bibliographical/persona background as orientation, not independently verified evidence. Do not invent quotations, page numbers, findings or examples attributed to a source. Flag any source-dependent challenge you cannot verify from the supplied material. A source's presence in the reference list does not mean you have read it.

Return a complete review of about 700–1100 words:
1. One-sentence summary of the main claim.
2. Two or three specific strengths.
3. Two or three substantive weaknesses, with section/example and the exact inference or descriptive claim at issue; state severity and propose alternatives.
4. A key question for the author.
5. Accept / Revise and Resubmit / Reject, with a brief reason. Distinguish required repairs from optional research extensions.

No external actions or edits are authorized. Read only this prompt and its included materials. Do not read other reviewers or create further agents. Report a credible material epistemic or authorization problem if encountered. Images are intentionally outside this reading task; structural tree source is supplied.

RESEARCH PERSPECTIVE TO SIMULATE: Christopher Lyons
- **Expertise:** Lyons 1999 *Definiteness* (Cambridge). Authority on cross-linguistic typology of articles and grammaticalization endpoints.
- **Persona:** Sympathetic to the grammaticalization backstop in §4 but concerned about scope. Will push on whether the English-only restriction is principled or evasive, and whether the cross-linguistic typology (Scandinavian suffixal articles, article-less languages) is handled or waved away.
- **Watch for:** Does §4 correctly characterize article diachrony and the cross-linguistic picture? Is the scope limitation principled? Does the paper respect the distinction between free-standing articles (English) and bound articles (Scandinavian, Balkan)?

=== COMPLETE ARTICLE SOURCE ===
\documentclass[12pt]{article}
\input{.house-style/preamble.tex}
\usepackage{forest}
\usepackage{xurl}
\usepackage{float}
\useforestlibrary{linguistics}
\setlength{\headheight}{14pt}
\clubpenalty=10000
\widowpenalty=10000
\AtBeginBibliography{\emergencystretch=1em}
\setcounter{biburlnumpenalty}{100}
\newcommand{\tablebody}[1]{\csname @@input\endcsname #1 }
\newcommand{\synnode}[2]{\shortstack{\scriptsize #1\\#2}}
\forestset{nominal tree/.style={for tree={align=center, parent anchor=south, child anchor=north, l sep=5mm, s sep=4mm, inner sep=1.5pt}}}
\hypersetup{pdftitle={Determinatives as nouns in English},pdfkeywords={determinatives, nouns, lexical categories, noun phrases, English}}
\title{Determinatives as nouns in English}
\author{Brett Reynolds \orcidlink{0000-0003-0073-7195}%
\thanks{Contact: \href{mailto:brett.reynolds@humber.ca}{brett.reynolds@humber.ca}}\\
Humber Polytechnic \& University of Toronto}
\date{Draft, September 2026}
\begin{document}
\maketitle

\begin{abstract}
I argue that English determinatives belong within Noun, preferably as a fourth coordinate subcategory alongside common nouns, proper nouns and pronouns. The argument extends the grounds on which \textit{The Cambridge grammar of the English language} already includes pronouns despite their distinctive inflection and restricted dependents. A matched comparison of independent uses, partitives, modification and a compound construction supports shared nominal organization while preserving lexical restrictions, including those of articles. Ordinary headedness is a further proposal: a separate-D grammar can also permit it. The taxonomic choice is between inheritance through Noun and a projection rule spanning separate noun and determinative categories. The coordinate arrangement remains provisional: the fragment's judgments don't distinguish it from nesting determinative within pronoun.
\end{abstract}

\noindent\textbf{Keywords:} determinatives, nouns, lexical categories, noun phrases, English

\section{The question}\label{sec:intro}

What is the categorial relationship among words such as \mention{some}, \mention{me}, \mention{apple} and \mention{Brett}? I argue that all four are nouns. I call this the \term{determinative-noun} or \term{D-noun analysis}.

I adopt the general framework of \textit{The Cambridge grammar of the English language} (\textit{CGEL}; \citealt{huddleston2002}). Unlike \textit{CGEL}, I include determinatives within Noun. The claims concern synchronic English lexical categories.

I use \term{determinative} for the category containing articles, demonstratives and quantifiers such as \mention{the}, \mention{this}, \mention{some}, \mention{every} and \mention{many}.\footnote{For a fuller inventory, see the online \href{https://www.cambridge.org/highereducation/api/resources/2AC8DF5CA558F8A6FCDFACD0EAF8EA08}{\enquote{List of determinatives in English}} accompanying \textcite{Huddleston2021}.} I reserve \term{determiner} for a syntactic function within the noun phrase. This distinction separates what kind of word \mention{some} is from what its phrase does. Capitalized Noun names the proposed superordinate category containing common nouns, proper nouns, pronouns and determinative nouns.

\textit{CGEL} already places common nouns, proper nouns and pronouns within Noun. It expressly justifies pronoun membership by the functions of pronoun-headed phrases, despite differences in inflection and dependents \citep[327--328]{huddleston2002}. The question is whether determinatives meet comparable grounds for inclusion. Differences from common nouns alone can't settle that question: the accepted noun subcategories already differ from one another. The inclusion of auxiliaries within Verb supplies a precedent for this kind of extension: a closed category can retain its distinctive syntax within a broader lexical category \citep{pullumwilson1977}.

Inclusion within Noun is the principal thesis. I provisionally favour four coordinate subcategories, pending evidence that an intermediate category captures further generalizations. Ordinary headedness is a further proposal, not a consequence of that inclusion: a grammar retaining primary D can also give determinatives ordinary nominal projection.

Figure~\ref{fig:some} compares \textit{CGEL} with the ordinary-Head variant of the D-noun analysis for \mention{take some apples} and \mention{take some}. Both keep \mention{some} in one lexical category across uses. In \textit{CGEL}, independent \mention{some} jointly fills determiner and head functions, a \term{fusion of functions} \citep[410--412]{huddleston2002}. In the ordinary-Head variant, \mention{some} always heads its own NP through a \term{nominal} (Nom): the phrase level below NP, containing the head and internal dependents but excluding an external determiner.

\begin{figure}[H]
\centering
\textit{CGEL}\par\smallskip
\begin{minipage}{.60\linewidth}\centering
\begin{forest} nominal tree
[VP
 [{\synnode{Head}{V}} [\mention{take}]]
 [{\synnode{Obj}{NP}}
  [{\synnode{Det}{DP}}
   [{\synnode{Head}{D}} [\mention{some}]]]
  [{\synnode{Head}{Nom}}
   [{\synnode{Head}{N\textsubscript{common}}} [\mention{apples}]]]]]
\end{forest}
\end{minipage}\hfill
\begin{minipage}{.38\linewidth}\centering
\begin{forest} nominal tree
[VP
 [{\synnode{Head}{V}} [\mention{take}]]
 [{\synnode{Obj}{NP}}
  [{\synnode{Head}{Nom}}, before drawing tree={x+=1.5em}
   [{\synnode{Det--Head}{DP}}, no edge
    [{\synnode{Head}{D}} [\mention{some}]]]
   {\draw[-] (!uu.south) -- (); \draw[-,line width=1pt] (!u.south) -- (); }]]]
\end{forest}
\end{minipage}

\medskip
\textit{Ordinary-Head variant of the D-noun analysis}\par\smallskip
\begin{minipage}{.60\linewidth}\centering
\begin{forest} nominal tree
[VP
 [{\synnode{Head}{V}} [\mention{take}]]
 [{\synnode{Obj}{NP}}
  [{\synnode{Det}{NP}}
   [{\synnode{Head}{Nom}}
    [{\synnode{Head}{N\textsubscript{D}}} [\mention{some}]]]]
  [{\synnode{Head}{Nom}}
   [{\synnode{Head}{N\textsubscript{common}}} [\mention{apples}]]]]]
\end{forest}
\end{minipage}\hfill
\begin{minipage}{.38\linewidth}\centering
\begin{forest} nominal tree
[VP
 [{\synnode{Head}{V}} [\mention{take}]]
 [{\synnode{Obj}{NP}}
  [{\synnode{Head}{Nom}}
   [{\synnode{Head}{N\textsubscript{D}}} [\mention{some}]]]]]
\end{forest}
\end{minipage}
\caption{\mention{Take some apples} (left) and \mention{take some} (right) under \textit{CGEL} (top) and the ordinary-Head variant of the D-noun analysis (bottom). In the upper-right tree, DP fills Det of NP and Head of Nom. In the lower pair, \mention{some} heads an NP through the same nominal projection; that NP functions as Det on the left and Obj on the right. Function labels appear above category labels. Det marks determiner, Obj object, and Det--Head fusion; the two links show the combined functions. N, D and V mark noun, determinative and verb; NP, DP and VP mark their phrases. Subscripts identify noun subcategories.}\label{fig:some}
\end{figure}

The D-noun analysis keeps \mention{apples} as the ultimate head of \mention{some apples}. This differs from the DP hypothesis, where functional D heads the whole expression \citep{abney1987}.

Earlier unifications include Palmer's grouping of determinatives with pronouns, Postal's underlying article analysis of pronouns, and Sommerstein's underlying NP analysis of articles and pronouns \citep{palmer1924,postal1966,sommerstein1972}. Hudson places the words he calls determiners within pronoun and pronoun within noun \citep{hudson2004determiners,hudson2010wordgrammar}. Section~\ref{sec:related} compares these proposals; Table~\ref{tab:rivals} locates the taxonomic alternatives.

I first distinguish the competing analyses, then establish what the existing noun subcategories share and how determinatives compare. Independent uses, partitives and modification identify the constructions to be explained. The matched fragment in §\ref{sec:fragment} holds the judgments and lexical restrictions fixed while varying taxonomy and headedness. The comparison concerns whether shared nominal structure is better stated for Noun or licensed across categories, not whether only the D-noun analysis can cover the examples.

\section{Classification, headedness and function}\label{sec:alternatives}

\subsection{Category, function and phrase structure}

Lexical categories and syntactic functions cut across one another. An NP can function as determiner, as in \mention{Kim's book}, and a determinative-headed phrase can function as modifier, as in \mention{the many people} \citep{payne2010,pullummiller2022nps}. Including determinatives within Noun preserves this distinction: the NP headed by \mention{some} functions as determiner in \mention{take some apples} and as object in \mention{take some} (Figure~\ref{fig:some}).

Two questions about headedness also need separating. \textcite{bruening2020nominal} supplies a generative defence of N-headed rather than D-headed nominals, drawing on selection and conventionalized expressions. Such arguments concern the head of expressions such as \mention{some apples}; they don't by themselves assign determinatives to Noun. Whether independent \mention{some} has ordinary Head or a fused function is a further question. Including determinatives within Noun leaves both available (§\ref{sec:fragment}).

Category membership doesn't remove lexical restrictions either. \mention{Every apple} is grammatical, but \ungram{\mention{I'll take every}} isn't an ordinary way to accept apples. Making \mention{every} a noun doesn't give it the full range of uses available to \mention{some}. Section~\ref{sec:fragment} states structural rules and lexical restrictions separately so their contributions can be assessed.

\subsection{Taxonomic and structural alternatives}\label{sec:related}

Keeping a word in one category across dependent and independent uses leaves its taxonomic position open. As \textcite[232--235]{lyons1968} observes, distribution can be compared at different levels of categorization: two expressions may belong together at one level and differ at a more specific level. Table~\ref{tab:rivals} sets out selected arrangements, from three separate primary categories to successive inclusion. Common and proper nouns remain within Noun throughout. The D-noun analysis differs from \textit{CGEL} by including determinative within Noun, and from Hudson by placing it alongside pronoun.

\begin{table}[H]
\centering\small
\caption{Selected taxonomic arrangements. Noun contains common and proper nouns in every row; its other members vary. The Hudson row abstracts from differences in lexical inventory explained in the text.}\label{tab:rivals}
\begin{tabular}{>{\raggedright\arraybackslash}p{8.7cm}>{\raggedright\arraybackslash}p{3cm}}
\toprule
Relation among Noun, pronoun and determinative & Account or status \\
\midrule
Noun, pronoun and determinative are separate primary categories. & Logical comparison \\
Pronoun is within Noun; determinative is a separate primary category. & \textit{CGEL} \\
Determinative is within Noun; pronoun is a separate primary category. & Logical comparison \\
Pronoun and determinative are coordinate subcategories of Noun. & D-noun analysis \\
Determinatives belong within pronoun, which is within Noun. & Hudson \\
Pronoun is within determinative, which is within Noun. & Reverse nesting for comparison \\
\bottomrule
\end{tabular}
\end{table}

\textcite[24]{palmer1924} proposed placing determinatives with pronouns, citing disagreement about their classification and most members' ability to \enquote{be used indifferently as pronouns or as modifiers of nouns}. \textcite[279]{lyons1968} also emphasizes the shared definiteness and deictic contrasts of articles, demonstratives and personal pronouns. The D-noun analysis retains determinatives and pronouns as distinct subcategories of Noun.

Hudson includes the determining words within pronoun. His noun category has the subcategories common noun, proper noun and pronoun \citep[253--254]{hudson2010wordgrammar}. In his terminology, a determiner is a pronoun whose \term{valency} permits the relevant common-noun dependent \citep[9--10]{hudson2004determiners}. Identifying these words by their permitted dependents doesn't require another category node.

\textit{CGEL} and Hudson classify different inventories. Hudson's criteria in the 2004 paper centre on licensing a singular count common noun and on mutual exclusion in that use. He sets aside \mention{all}, cardinal numerals and quantifiers restricted to plural or non-count nouns. \textit{CGEL}'s determinative category is broader, so the comparison requires checking which words and constructions each covers.

\textcite{anderson1997notional} draws the boundary of the nominal category differently. He groups names, pronouns and determining words as a notional \{N\} category, with common nouns represented separately. His \{N\} differs from the inclusive Noun proposed here and falls outside Table~\ref{tab:rivals}.

Taxonomic inclusion doesn't settle the structural analysis. Hudson separates dependency from phrase headedness: his 2004 account permits mutual dependency between determiner and common noun, with different constructions selecting different external heads \citep[7--9]{hudson2004determiners}. In \mention{We met that day}, the temporal adjunct depends on the temporal meaning of \mention{day}. Such restrictions support a common-noun head for temporal adjuncts \citep[10--12]{hudson2004determiners}.

Other unifications concern underlying representation. \textcite{postal1966} unifies personal pronouns and articles through an underlying article analysis. \textcite[197--203]{sommerstein1972} reverses the direction, assigning underlying NP structure to the definite article and personal pronouns, with relative-clause structures contributing further descriptive material. These structures don't by themselves place the surface lexical categories in Table~\ref{tab:rivals}. \textcite{dechainewiltschko2002} distinguish pro-DP, pro-$\phi$P and pro-NP, connecting different pronominal projections with distribution and binding. Their proposal adds differences in pronominal projection to the comparison.

Rejecting a separate primary D needn't preserve a unified determinative subcategory. \textcite{spinillo2004reconceptualising} proposes redistribution among existing categories, retaining \mention{the}, \mention{a} and \mention{every} as an expanded article category. That proposal makes the restricted members a separate category; the D-noun analysis retains them inside the wider determinative subcategory.

For demonstratives and forms such as \mention{some} and \mention{all}, \textcite[140--144]{spinillo2004reconceptualising} rejects switching between determiner and pronoun categories according to whether a noun follows. She compares the alternation with verbs and prepositions used with or without a complement. The D-noun analysis agrees that the two uses needn't involve different lexical categories. It differs in retaining determinative as the subcategory across those uses.

\textcite{vaneynde2003determiner} likewise rejects a separate determiner category, but assigns determining expressions to adjective or noun on morphological and agreement evidence, chiefly from Italian and Dutch. His analysis separates lexical category from the features governing determination. A noun-headed NP account therefore needn't unify every determining expression as nominal.

Independent nominal use may support inclusion within Noun without selecting the pronoun subcategory. The demonstratives' deictic properties make a pronominal grouping plausible; the question is how far that grouping captures the wider inventory's syntax. The comparisons below address modifier profiles (§\ref{sec:payne}), the determinative--pronoun boundary (§\ref{sec:inheritance}), and the positive connections linking restricted \mention{every} to other quantifiers (§\ref{sec:articles}). Redistribution must be assessed against those connections as well as independence. The starting point is \textit{CGEL}'s existing grounds for including distinct subcategories within Noun.

\section{The D-noun analysis}\label{sec:proposal}

\subsection{The existing standard of nounhood}\label{sec:membership}

The starting category is Noun as \textit{CGEL} already constitutes it. Its discussion of pronouns makes the reasoning explicit: they differ from prototypical nouns in inflection and permitted dependents, but qualify because the phrases they head have the functions of common- and proper-noun-headed phrases \citep[327]{huddleston2002}. Table~\ref{tab:existing} sets out some of the variation already accepted within that category.

\begin{table}[H]
\centering\small
\caption{Contrasts already accommodated within \textit{CGEL}'s Noun. These are typical profiles, with further restrictions and exceptions within each subcategory \citep[327--328, 425--430, 517--520]{huddleston2002}.}\label{tab:existing}
\begin{tabular}{>{\raggedright\arraybackslash}p{2.3cm}>{\raggedright\arraybackslash}p{3.15cm}>{\raggedright\arraybackslash}p{3.15cm}>{\raggedright\arraybackslash}p{3.15cm}}
\toprule
Dimension & Common noun & Proper noun & Pronoun \\
\midrule
Inventory & Open & Open to new names & Closed \\
Inflection & Number and genitive & Genitive; restricted plural uses & Case paradigms in personal pronouns \\
Determination & Broad contrasts; singular count arguments normally require it & Restricted in primary naming uses & Normally excluded \\
Internal modification & Productive AdjP and nominal modification & Restricted embellishments & Restricted, as in \mention{poor old me} \\
\bottomrule
\end{tabular}
\end{table}

Common nouns supply the most familiar profile, but they don't supply an entry test that every noun subcategory has to pass unchanged. Pronouns remain nouns despite their closed inventory and restricted modification; proper nouns remain nouns despite their distinct naming uses. An argument that excludes determinatives on these grounds therefore needs to explain why comparable differences warrant a primary-category boundary in this case.

Meaning and reference also vary within Noun. \mention{Apple} conveys a descriptive classification; \mention{Kim}, in its primary naming use, identifies through a name; \mention{she} supplies limited descriptive content and depends on context. The quantificational or deictic contribution of a determinative therefore needs to be assessed alongside its grammar, rather than measured against common-noun semantics alone.

The distributional comparison follows \textit{CGEL}'s pronoun argument: a range of determinatives occurs in subject, object and complement-of-preposition positions without another overt nominal head. The pattern recurs across lexemes and appropriate contexts, establishing systematic nominal use without deciding between fusion and ordinary headedness. The examples in §\ref{sec:independent} compare all four proposed subcategories in the same positions.

External distribution alone is insufficient: adjectival constructions such as \mention{the rich} also fill those positions. The further comparison concerns the breadth of independent use, determination, partitives and internal modification. Together these properties support a nominal subcategory profile. Restrictions on particular lexemes or readings remain part of the description, just as they do within the existing Noun category; §\ref{sec:predication} examines the predicative restrictions.

Extending the analysis to restricted members carries a separate burden. Pronoun forms themselves don't all pass the argument-position test: dependent genitives such as \mention{my} have positive support from their paradigms. For determinatives, the argument likewise needs to establish both a broadly nominal constructional profile and the restricted members' integration into that category. Section~\ref{sec:articles} supplies the latter argument.

The distinction at issue is thus one of taxonomic level. A closed inventory, reduced descriptive content or unusual modifier selection can establish a distinctive subcategory without establishing exclusion from Noun. The decisive comparison is whether the shared nominal behaviour and local differences are better captured by extending existing nominal structure or by preserving a separate primary D. Section~\ref{sec:fragment} holds the lexical restrictions fixed to make that comparison explicit.

The D-noun analysis captures shared properties through \term{inheritance}: a property stated for a superordinate category is available to its subcategories, subject to stated restrictions. It extends the division of labour already used within Noun: general rules supply nominal projection, subcategory rules constrain combinatorics, and lexical entries distinguish such forms as independent \mention{some} and dependent-only \mention{every}.

\subsection{Noun phrases in determiner and argument functions}\label{sec:bridge}

Determiner function already cuts across the existing noun subcategories. Compare \mention{my book}, \mention{Kim's book} and \mention{the king's book}. The determiner is an NP ultimately headed by a pronoun, a proper noun and a common noun respectively \citep[354--355, 470--471]{huddleston2002}.\footnote{\textit{CGEL} assigns these genitives the combined function Subject--Det \citep[472--473]{huddleston2002}. I treat them as Det here, without the additional subject function. Their determining role supplies the relevant comparison; accepting the further subject analysis would leave the nounhood argument intact.} In the last example, \mention{the} determines \mention{king} inside the genitive NP, while that whole NP determines \mention{book}. Figure~\ref{fig:genitive} illustrates the proper-noun case: \mention{Kim's} fills Det, while \mention{book} ultimately heads the larger NP.

\begin{figure}[H]
\centering
\begin{forest} nominal tree
[NP
 [{\synnode{Det}{NP[gen]}}
  [{\synnode{Head}{Nom}}
   [{\synnode{Head}{N\textsubscript{proper}}} [\mention{Kim's}]]]]
 [{\synnode{Head}{Nom}}
  [{\synnode{Head}{N\textsubscript{common}}} [\mention{book}]]]]
\end{forest}
\caption{The genitive NP \mention{Kim's} functions as determiner within \mention{Kim's book}, ultimately headed by \mention{book}. The representation abstracts from the internal realization of genitive marking.}\label{fig:genitive}
\end{figure}

Together, these genitives establish more than the possibility of a noun-headed phrase in Det function. All three admitted noun subcategories already contribute phrases to that function, subject to the genitive construction's restrictions. The D-noun analysis extends this nominal pattern to determinative-headed phrases.

The ordinary-Head variant gives the two D-noun structures in Figure~\ref{fig:some}. In \mention{take some apples}, the NP headed by \mention{some} fills Det, as \mention{Kim's} does in \mention{Kim's book}; \mention{apples} heads the larger NP. In \mention{take some}, \mention{some} heads the whole object NP. The lexeme retains its subcategory and nominal projection across these uses, while the NP it heads changes function.

Shared projection doesn't imply unrestricted interchangeability. The determiner construction selects a determinative-headed phrase, a suitable genitive NP, or another licensed expression. Number, countability and other selectional conditions further distinguish the determining expressions. Section~\ref{sec:fragment} includes these restrictions in the comparison of grammars.

\subsection{Modifier selection and taxonomic level}\label{sec:payne}

Shared nominal projection doesn't make modifier permissions uniform. In \mention{almost every experienced teacher} (Figure~\ref{fig:every}), the AdvP \mention{almost} modifies the determinative noun \mention{every}; the AdjP \mention{experienced} modifies the common noun \mention{teacher}, which ultimately heads the outer NP.

\begin{figure}[H]
\centering
\begin{forest} nominal tree
[NP
 [{\synnode{Det}{NP\textsubscript{D}}}
  [{\synnode{Head}{Nom}}
   [{\synnode{Mod}{AdvP}} [\mention{almost}]]
   [{\synnode{Head}{N\textsubscript{D}}} [\mention{every}]]]]
 [{\synnode{Head}{Nom}}
  [{\synnode{Mod}{AdjP}} [\mention{experienced}]]
  [{\synnode{Head}{N\textsubscript{common}}} [\mention{teacher}]]]]
\end{forest}
\caption{Two modifier relations in \mention{almost every experienced teacher}: \mention{almost} modifies \mention{every}, and \mention{experienced} modifies \mention{teacher}. The outer NP has \mention{teacher} as its ultimate head. Internal structure within the one-word modifier phrases is suppressed.}\label{fig:every}
\end{figure}

\textcite[40--42]{payne2010} defend keeping \mention{few}, \mention{any} and related forms in one lexical category across dependent and independent uses. In \mention{hardly any money} and independent \mention{hardly any}, \mention{hardly} remains an adverb and \mention{any} retains its category. The D-noun analysis preserves that continuity. It also preserves their contrast between adverbial premodification, as in \mention{almost anybody}, and adjectival postmodification, as in \mention{nothing absolute}.

\textcite[60--61]{payne2010} also argue that distribution alone can't decide whether adjectives and adverbs are inflectional variants of one category or derivationally related members of different categories. The D-noun analysis preserves distinct lexical subcategories and makes no inflectional-variant claim. Their methodological constraint still applies: shared positions alone don't settle category status.

Modifier selection supports distinguishing determinatives from pronouns and common nouns. The further question is the taxonomic level of that distinction. Within the proposed Noun, the determinative subcategory licenses \mention{hardly any} and \mention{almost every}; the common-noun subcategory licenses \mention{experienced teacher}. Neither \ungram{\mention{experienced every}} nor \ungram{\mention{almost teacher}} follows. The existing modifier profiles remain, while their relation to the broader category changes; §\ref{sec:costs} considers the cost explicitly. Section~\ref{sec:evidence} assesses the fuller constructional profile against the grounds on which \textit{CGEL} already includes distinct subcategories within Noun.

\section{Evidence for nominal structure}\label{sec:evidence}

Independent uses, partitives and modification show a recurring nominal pattern. These observations overlap: \mention{Some left} illustrates both external distribution and syntactic completeness. Fusion and ordinary headedness can cover this pattern. The comparisons below distinguish the shared observations from the analyses of their internal structure; §\ref{sec:fragment} assesses the resulting organization of the grammar.

\subsection{Breadth of independent use}\label{sec:independent}

Independent use is widespread within the determinative inventory. \textit{CGEL} discusses such uses for demonstratives and quantifiers including \mention{some}, \mention{all}, \mention{both}, \mention{many}, \mention{few}, \mention{several}, \mention{each}, \mention{either}, \mention{neither}, \mention{much} and \mention{enough}, while recording lexical restrictions and the separate forms \mention{no}/\mention{none} \citep[371--372, 410--424]{huddleston2002}. The generalization concerns the availability of independent constructions across a lexical category, not unrestricted acceptability in every sentence frame.\footnote{Material before a determiner falls outside the independent-use comparison. \textit{CGEL} treats \mention{all}/\mention{both} in \mention{all/both the books} as predeterminer modifiers, \mention{quite}/\mention{rather} before \mention{a good idea} as peripheral modifiers, and \mention{such}/exclamative \mention{what} before \mention{a disaster} as adjectives \citep[433--437]{huddleston2002}. The fixed \mention{many a} is a complex determinative restricted to Det function \citep[394]{huddleston2002}. The \mention{half} in \mention{half a cake} is a common noun used as a predeterminer modifier \citep[434]{huddleston2002}. These constructions don't add evidence for independent determinative heads.}

The pattern extends beyond a few compounds or a single lexicalized expression. For this closed category, \term{productivity} concerns the availability of independent use among established members under appropriate conditions, rather than the licensing of new lexical items.

In the constructed examples in (\ref{ex:external}), compare the positions occupied by the bracketed NPs: subject, object and complement of a preposition. Assume that a woman named Kim and a group of people are already under discussion. These positions admit NPs containing words from each proposed noun subcategory; the competing analyses assign different internal structures to independent \mention{some}.

\begin{samepage}
\ea\label{ex:external}
\ea \mention{[People] left.}\qquad \mention{I see [people].}\qquad \mention{with [people]}
\ex \mention{[Kim] left.}\qquad \mention{I see [Kim].}\qquad \mention{with [Kim]}
\ex \mention{[She] left.}\qquad \mention{I see [her].}\qquad \mention{with [her]}
\ex \mention{[Some] left.}\qquad \mention{I see [some].}\qquad \mention{with [some]}
\z\z
\end{samepage}

Adjectival independent uses prevent a simple inference from these positions to nounhood. \mention{The rich} and \mention{the poor} can fill nominal argument positions. Comparative and superlative adjectives also head expressions without a human-class interpretation: \textit{CGEL}'s \mention{the most important of her criticisms} is an NP containing a partitive \mention{of}-phrase \citep[332--333, 416--423]{huddleston2002}.

Independent \mention{some} can form a one-word NP, whereas an NP with \mention{rich} as fused head normally requires a determiner on the human-class reading. That is a local contrast: argument NPs headed by singular count common nouns also need determination. Section~\ref{sec:modification} returns to the fuller adjectival comparison.

\subsection{Structural saturation and interpretation}

With a group of people under discussion, \mention{Some left}, \mention{Many came} and \mention{All agree} illustrate \term{structural saturation}: an argument expression can be syntactically complete without another overt head or determiner. Syntactic completeness differs from contextual interpretation. In \mention{I'll take some}, the relevant substance or set may be supplied by discourse or the situation. That dependence doesn't establish a deleted common noun: ordinary pronouns also depend on context.

In the following attestation from the CGELBank treebank, \mention{two different Honda models} supplies the domain for the independent object \mention{both}:\footnote{CGELBank \citep{reynolds2023unified}, sentence \href{https://github.com/nert-nlp/cgel/blob/d0a2c2d8c522b23d5aa879fc9cb94948f4285b2c/datasets/ewt.cgel\#L651-L654}{\nolinkurl{reviews-083459-0002}}.}
\ea\label{ex:attested-both}
\mention{Went there yesterday: we are trying to decide between two different Honda models, so we wanted to test-drive both back to back.}
\z

Generalizing expressions such as \mention{Many are called, few are chosen} and \mention{Enough is enough} need no previously uttered common-noun phrase. They rule out a mandatory overt-antecedent requirement, but a silent-noun account could supply a generic restriction. Such examples don't decide whether the restriction belongs in semantics or syntax.

The comparison with ordinary pronouns and proper nouns is structural as well as interpretive. In \mention{She left} and \mention{Kim left}, \textit{CGEL} permits an NP headed by a nominal with no determiner. Applying that structure to \mention{Some left} preserves the same division between a complete NP and its context-dependent reference. The dependent use of \mention{some} doesn't by itself require a Det function inside every independent occurrence.

Fusion supplies the competing analysis. In \textcite{Payne2007}, one constituent jointly realizes Head and a dependent function, subject to structural and adjacency conditions. In \textit{CGEL}'s analysis of independent \mention{some}, the DP headed by \mention{some} fills Det of NP and Head of Nom. The word retains the determinative category it has in \mention{some apples}, while the independent expression is an NP. Ordinary headedness replaces this relation with nominal projection; lexical restrictions on independence and form selection remain.

Nounhood remains compatible with fusion. \textit{CGEL} analyses \mention{mine} as fused Det--Head when it stands for a possessed entity in an anaphoric context, but as pure Head in the predicative possessive use \mention{it's mine} \citep[410--411]{huddleston2002}. That comparison blocks an objection from fusion to nounhood. The positive case for ordinary headedness instead extends the structure available to \mention{she} and \mention{Kim}.

Saturation therefore clarifies the distributional comparison without independently selecting either internal structure.

\subsection{Partitives locate the quantificational head}

In \mention{some of the wine}, \mention{some} specifies a quantity drawn from an identifiable amount of wine. The NP \mention{the wine} denotes the partitive \term{domain}: the whole from which that quantity is drawn. This NP is complement of \mention{of}. A pronoun-headed NP or independent genitive NP can express the domain too: \mention{many of them}, referring to previously mentioned people, or \mention{some of Kim's}, referring to Kim's apples.

Compare where the common noun occurs in \mention{some apples} and \mention{some of the wine}. In the partitive, \mention{wine} is embedded inside the \mention{of}-phrase, so it can't be the lexical head of the whole NP. The comparison instead concerns the head-like role of \mention{some} in that larger expression.

Figure~\ref{fig:partitive} gives the ordinary-Head D-noun analysis, with the \mention{of}-phrase functioning as complement within Nom, as in \textit{CGEL}'s partitive tree \citep[411--412]{huddleston2002}. \textit{CGEL} represents the head-like role of \mention{some} through Det--Head fusion. Partitives support that role while leaving the choice between fusion and ordinary headedness open.

\begin{figure}[H]
\centering
\begin{forest} nominal tree
[NP
 [{\synnode{Head}{Nom}}
  [{\synnode{Head}{N\textsubscript{D}}} [\mention{some}]]
  [{\synnode{Comp}{PP}}
   [{\synnode{Head}{P}} [\mention{of}]]
   [{\synnode{Comp}{NP}} [\mention{the wine}, roof]]]]]
\end{forest}
\caption{\mention{Some of the wine} under the ordinary-Head D-noun analysis. The Head relations lead from the outer NP to \mention{some}. The common noun \mention{wine} is inside the complement PP and doesn't head the whole expression. The inner NP is abbreviated.}\label{fig:partitive}
\end{figure}

The overt quantifier and domain already supply a compositional interpretation of \mention{some of the wine}. A silent common noun would need to explain something further, such as a restriction on interpretation or modification that the overt-head account misses. The construction itself supplies no such requirement. I therefore prefer an overt-head analysis over an otherwise equivalent null-head analysis; fusion remains compatible with that preference.

The ordinary-Head analysis treats \mention{some} and \mention{some of the wine} as sharing nominal projection, with an added domain phrase in the partitive. Modification provides a further comparison of internal structure.

\subsection{Modification tests the internal analysis}\label{sec:modification}

The pair \mention{the lucky survivors}/\mention{the lucky few} supplies a comparison involving both external determination and adjectival modification. \textit{CGEL} explicitly permits determinatives used as internal modifiers to fuse with Head, as in \mention{the other two} and \mention{these few here} \citep[415--416]{huddleston2002}. Its analysis of \mention{the few mistakes} assigns \mention{the} to Det and \mention{few} to Mod \citep[392]{huddleston2002}. That dependent use supplies the counterpart for a Mod--Head analysis of independent \mention{few} after an external determiner.

Figure~\ref{fig:few} compares the resulting analyses of \mention{the lucky few}. Both have an overt Det and a Nom modified by \mention{lucky}. In the ordinary-Head D-noun analysis, \mention{few} fills Head. In the fusion analysis, its DP fills Mod--Head. The competing structure thus uses machinery already needed for adjectival fusion; it requires neither a silent noun nor conversion.

\begin{figure}[H]
\centering
\begin{minipage}{.48\linewidth}\centering
\begin{forest} nominal tree
[NP
 [{\synnode{Det}{NP\textsubscript{D}}} [\mention{the}, roof]]
 [{\synnode{Head}{Nom}}
  [{\synnode{Mod}{AdjP}} [\mention{lucky}]]
  [{\synnode{Head}{N\textsubscript{D}}} [\mention{few}]]]]
\end{forest}
\end{minipage}\hfill
\begin{minipage}{.48\linewidth}\centering
\begin{forest} nominal tree
[NP
 [{\synnode{Det}{DP}} [\mention{the}, roof]]
 [{\synnode{Head}{Nom}}
  [{\synnode{Mod}{AdjP}} [\mention{lucky}]]
  [{\synnode{Head}{Nom}}, before drawing tree={x+=1.5em}
   [{\synnode{Mod--Head}{DP}}, no edge
    [{\synnode{Head}{D}} [\mention{few}]]]
   {\draw[-] (!uu.south) -- (); \draw[-,line width=1pt] (!u.south) -- (); }]]]
\end{forest}
\end{minipage}
\caption{\mention{The lucky few} with ordinary Head (left) and Mod--Head fusion (right). The determiner is separately realized in both. Internal structure within the article phrase and AdjP is suppressed.}\label{fig:few}
\end{figure}

Table~\ref{tab:matched-heads} compares four constructions. Separate D with ordinary headedness can assign \mention{few} the same Head relations as the D-noun analysis while retaining D as its lexical category; §\ref{sec:fragment} supplies that alternative's rules.

\begin{table}[H]
\centering\small
\caption{Head and dependent functions under matched analyses. Each independent expression is an NP; \mention{the} fills Det wherever it appears. The ordinary-Head column applies to both taxonomies permitting ordinary determinative heads.}\label{tab:matched-heads}
\begin{tabular}{>{\raggedright\arraybackslash}p{2.8cm}>{\raggedright\arraybackslash}p{4.5cm}>{\raggedright\arraybackslash}p{4.5cm}}
\toprule
Expression & Separate D with fusion & Ordinary determinative Head \\
\midrule
\mention{few survivors} & \mention{few}: Det; \mention{survivors}: Head & Same functions \\
Independent \mention{few} & \mention{few}: Det--Head & \mention{few}: Head \\
\mention{the lucky few} & \mention{few}: Mod--Head; \mention{lucky}: Mod & \mention{few}: Head; \mention{lucky}: Mod \\
\mention{the idle rich} & \mention{rich}: Mod--Head; \mention{idle}: Mod & Same fusion and modifier functions \\
\bottomrule
\end{tabular}
\end{table}

Fusion groups \mention{the lucky few} with \mention{the idle rich}, whereas ordinary headedness groups it with \mention{the lucky survivors}. Ordinary headedness unifies \mention{few} across its bare and externally determined uses, without alternating Det--Head and Mod--Head. Neither account gains coverage from this example alone. The comparison is between sharing a fusion construction across D and adjective, and sharing ordinary nominal headedness across determinative constructions.

The constructed \mention{the remaining three} extends the modifier pattern to cardinals. It doesn't independently decide whether \mention{three} is determinative or has a common-noun use: \textcite{reynolds2026numerals} argues for both uses of cardinals. Section~\ref{sec:costs} treats their unification as a consequence conditional on that analysis.

Why retain adjective outside Noun? The adjectival construction is restricted to particular lexical and interpretive groups, with additional determiner restrictions: compare the human-class \mention{the rich} with \ungram{\mention{these very poor}} \citep[416--417]{huddleston2002}. Determinative independent use extends across demonstratives and quantifiers with varied domains and determining contrasts. This difference favours organizing nominal projection at the determinative-subcategory level while retaining constructional licensing for adjectival fusion. It supplies a comparative reason, not a necessary-and-sufficient membership test.

\subsection{Compounds and modifier domains}\label{sec:compounds}

A more demanding modifier comparison is \mention{hardly anyone present}. \textcite[581--583]{Payne2007} assign \mention{hardly} to DP structure and \mention{present} to nominal structure. The compound \mention{anyone} takes the premodifiers of its determinative base \mention{any}: compare \mention{hardly any writer present}. The adjective realizes a specialized \term{restrictor} function, restricted to post-head position and non-recursive. Figure~\ref{fig:compound} contrasts this account with an ordinary-Head analysis.

\begin{figure}[H]
\centering
\begin{minipage}{.48\linewidth}\centering
\begin{forest} nominal tree
[NP
 [{\synnode{Head}{Nom}}
  [{\synnode{Mod}{AdvP}} [\mention{hardly}]]
  [{\synnode{Head}{N\textsubscript{D}}} [\mention{anyone}]]
  [{\synnode{Mod}{AdjP}} [\mention{present}]]]]
\end{forest}
\end{minipage}\hfill
\begin{minipage}{.48\linewidth}\centering
\begin{forest} nominal tree
[NP
 [{\synnode{Head}{Nom}}, before drawing tree={x+=4em}
  [{\synnode{Det--Head}{DP}}, no edge
   [{\synnode{Mod}{AdvP}} [\mention{hardly}]]
   [{\synnode{Head}{D}} [\mention{anyone}]]]
  {\draw[-] (!uu.south) -- (); \draw[-,line width=1pt] (!u.south) -- (); }
  [{\synnode{Mod}{AdjP}} [\mention{present}]]]]
\end{forest}
\end{minipage}
\caption{\mention{Hardly anyone present} with ordinary Head (left) and fusion (right). Both post-head Mod positions realize the specialized restrictor. In the fusion tree, DP fills Det of NP and Head of Nom, following \textcite[582, (13d)]{Payne2007}. Modifier-phrase interiors are suppressed.}\label{fig:compound}
\end{figure}

In the ordinary-Head D-noun analysis, \mention{anyone} inherits nominal projection from Noun and its premodifier permissions from its determinative base. The compound construction supplies the post-head restrictor permission, with the same position and non-recursion conditions as the fusion account. It doesn't license a corresponding pre-head adjective. The compound's ordinary argument use and exclusion of external determination are further lexical conditions; the premodifier and restrictor slots aren't unrestricted Nom dependents.

This division extends to \mention{someone} and \mention{everybody}: the compound family licenses nominal argument use and post-head restrictors, while each base supplies its own premodifier permissions. It doesn't follow that \mention{hardly} modifies every compound. CGELBank attests the post-head pattern in \mention{I need something reliable and good looking}.\footnote{Sentence \href{https://github.com/nert-nlp/cgel/blob/d0a2c2d8c522b23d5aa879fc9cb94948f4285b2c/datasets/ewt-test_iaa50.cgel\#L179-L181}{\nolinkurl{answers-20111024111513AAAQhAO_ans-0003}} in \nolinkurl{ewt-test_iaa50.cgel}.}

Fusion reuses the DP--Nom boundary to separate the two modifier domains. Ordinary headedness reuses nominal projection, locating both domains within Nom and assigning their restrictions to the determinative base and compound construction. Both accounts need the specialized restrictor condition. The trade-off concerns where the restrictions are stated, not whether they can be removed.

\subsection{Predicative uses and their restrictions}\label{sec:predication}

The argument-use patterns above don't extend uniformly to predicative complementation. \textit{CGEL} records \mention{Its advantages are several} and \mention{Their enemies were many}, describing the latter pattern as uncommon and formal \citep[392, 395--396]{huddleston2002}. Predicative use is available to only part of the determinative inventory; \mention{every} and the articles remain excluded from these frames.

The comparison also depends on what the predication expresses. \mention{She is a doctor} ascribes a property, whereas \mention{That is Kim} identifies a person. \textit{CGEL} excludes specifying \mention{be} clauses from its noun--adjective diagnostic because phrases from other categories occur in them too \citep[536]{huddleston2002}. Merely placing an expression after \mention{be} therefore provides no uniform nounhood test.

Nominal grammar already licenses some expressions predicatively while restricting their argument uses. A bare-role NP such as \mention{president} is licensed in \mention{I'd like to be president}, but requires determination in the corresponding object use \mention{I'd like to meet the president} \citep[328]{huddleston2002}. Predicative and argument uses thus need separate conditions within Noun itself. The determinative asymmetries belong in that comparison; they don't establish exclusion merely by departing from a common-noun substitution frame.

\subsection{What the combined pattern supports}\label{sec:cumulative}

Independent uses, partitives and modification establish a systematic range of nominal constructions. They support extending the comparison with existing noun subcategories beyond \mention{Some left}. Both fusion and ordinary headedness cover this range, while retaining the lexical and constructional restrictions illustrated above.

I favour ordinary headedness because it gives bare, partitive and externally determined uses the Head relation already available to nouns. Fusion instead relates them to dependent counterparts and distinguishes Det--Head from Mod--Head. That machinery is already needed for adjectives and genitives, and the compound comparison shows a benefit of retaining its structural domains.

This structural preference leaves the taxonomic question open: a separate-D grammar can also permit ordinary determinative heads. The pronoun precedent favours inheritance through Noun, while separate D preserves the modifier contrast as a primary-category distinction. Section~\ref{sec:fragment} compares both headedness choices under both taxonomies, making explicit what the distributional pattern leaves undecided. The next two sections consider the hierarchy within Noun and the membership of its restricted forms.

\section{Coordinate subcategories and inheritance}\label{sec:inheritance}

Should determinatives and pronouns be coordinate subcategories within Noun, or should determinatives belong inside pronoun? \textcite{reynolds2021} compares determinative and pronoun profiles; its matrix contains no common or proper nouns. Distributional separation between the supplied groups doesn't determine their taxonomic rank or test the proposed superordinate category. Even perfect recovery of the distinction would be compatible with shared nounhood. The original discussion likewise leaves a nested nominal analysis open.\footnote{The accompanying \href{run:matrix-audit.pdf}{\textit{Replication audit of the English determinative--pronoun feature matrix}} documents the discrepancy between the reported 232 features and the public 155-feature file, an extra feature dropped by the published clustering code, and sensitivity to initialization and feature selection. The archived public file is retained unchanged.}

The pronoun inventory in that study follows \textit{CGEL}'s classification, whereas Hudson's pronoun category includes the words he calls determiners. Comparing these hierarchies requires aligning their lexical inventories and asking which generalizations can be stated for each superordinate category.

An intermediate pronoun-plus-determinative category would be useful if it collected generalizations otherwise repeated. Within the proposed grammar, nominal projection rules apply to all four subcategories, so they can be stated for Noun as a whole. The intermediate category would need additional generalizations. Different property profiles alone don't favour coordination: a subtype can differ sharply from the rest of its superordinate category. Core personal pronouns' case, reflexive and person contrasts, and determinatives' quantificational and modifier patterns, support local distinctions under either hierarchy.

Reduced descriptive content and contextual interpretation are shared by many pronouns and determinatives. The coordinate analysis can record these interpretive properties through features or cross-classification; they don't by themselves require an intermediate lexical category.

Pro-form gender supplies a more specific interpretive comparison. \textcite{reynolds2025proformgender} proposes a personhood-based system spanning pronouns and determinatives. Personal reference links pronouns such as \mention{she} with compound determinatives such as \mention{somebody}; non-personal reference links \mention{it} with \mention{something}. These constraints concern how the referent is construed. They provide a shared generalization for nominal pro-forms, but don't decide between coordinate and nested noun subcategories. The broader pro-form system also includes non-nominal expressions, so gender alone doesn't delimit Noun.

Restrictions on determination and attributive modification provide syntactic candidates, but they also occur outside the proposed grouping. In their primary use, proper names don't select freely from the determiner system, and their adjectival embellishments are restricted \citep[517, 519--520]{huddleston2002}. These properties distinguish more than pronouns and determinatives from common nouns.

Determination also differs within the proposed intermediate category. Determinatives permit external determination in a range of independent quantificational constructions: \mention{the few}, \mention{the many}, \mention{the two}, \mention{these three}. The permissions vary by item and often require further modification; \textit{CGEL} gives \mention{these few here} and \mention{the many who did} \citep[415--416]{huddleston2002}. Pronouns admit external determination only marginally, and internal premodification is restricted, as in \mention{poor old me} \citep[429--430]{huddleston2002}. These restrictions thus cross-cut the proposed grouping and vary within it.

I retain the coordinate classification as a provisional organizational preference. It preserves \textit{CGEL}'s determinative/pronoun distinction while extending nominal structure across both. The fragment in §\ref{sec:fragment} doesn't distinguish coordination from nesting by its judgments. Hudson's intermediate category would be preferable if further syntactic generalizations over the aligned inventory reduced otherwise repeated restrictions. Section~\ref{sec:articles} turns from the position of determinative within Noun to the membership of its restricted forms.

\section{The articles and other restricted members}\label{sec:articles}

Why classify the articles \mention{the} and \mention{a} as nouns if they can't stand independently? Independent uses motivate the D-noun analysis of \mention{some}, \mention{this} and \mention{many}, but the articles require a different argument. \mention{Every} is restricted too, while \mention{no} has the distinct independent form \mention{none} \citep[371--372, 410--411]{huddleston2002}.\footnote{The restriction concerns ordinary argument use. In \mention{the bigger the better}, \textit{CGEL} analyses \mention{the} as a modifier within a comparative phrase \citep[1131--1132, 1135--1136]{huddleston2002}. This dependent use outside Det leaves the restriction on ordinary argument use intact.}

\textit{CGEL}'s treatment of \mention{my} supplies a precedent for restricted membership within Noun \citep[470--471]{huddleston2002}. The pronoun's paradigm supports its membership despite its lack of \mention{mine}'s independent distribution. For articles, the corresponding positive evidence is integration into determinative; their nounhood depends on the category-level argument.

Retaining a restricted member requires three kinds of support. First, it should be paradigmatically integrated with independently identified members. Second, it should participate in the category's characteristic semantic and grammatical contrasts. Third, its missing uses should form a local restriction while the positive connections remain. Calling an item \term{defective} summarizes that pattern; it doesn't supply an argument for membership by itself.

The articles meet these conditions within determinative. First, they contrast with demonstratives and quantifiers before common-noun nominals: \mention{the/a/this/every book}. Second, they participate in the same system of definiteness, number and count restrictions: \mention{the} permits singular, plural and non-count targets, while \mention{a} selects a singular count target. Third, their lack of ordinary independent uses leaves that determining pattern intact. These connections support determinative membership, rather than establishing nounhood independently.

\mention{Every} has further connections beyond the restricted article set proposed by \textcite{spinillo2004reconceptualising}. Like \mention{each}, it expresses universal quantification and selects singular count nominals: \mention{every teacher}, \mention{each teacher}. Unlike \mention{each}, it lacks ordinary independent use. It also permits modification by \mention{almost} and \mention{nearly}. These connections support retaining \mention{every} with the quantifiers.

The argument for retaining the articles is synchronic. Grammaticalization supplies background: \textcite[331--336]{lyons1999} discusses the development of definite articles from demonstratives and of articles expressing cardinality from numerals. These histories can explain changes in content and use, but don't establish the synchronic classification.

A separate article category would gain support from a cluster of synchronic restrictions shared by \mention{the}, \mention{a} and \mention{every}, absent elsewhere in Noun, and otherwise requiring repeated exceptions. Lack of independent argument use alone doesn't supply that cluster. The comparison concerns the allocation of generalizations; an additional restriction needn't by itself overturn the membership analysis. All the grammars compared in §\ref{sec:fragment} retain the articles' restriction on ordinary argument use.

\section{Shared projection and grammatical economy}\label{sec:economy}

\subsection{A shared phrase type in determiner function}\label{sec:det-uniform}

In \mention{some apples} and \mention{Kim's apples}, the phrases headed by \mention{some} and \mention{Kim} fill the same determiner function. \textit{CGEL} assigns them different phrase types, DP and genitive NP. It also admits a restricted range of plain-case NPs and PPs as determiners, as in \mention{what size hat} and \mention{over thirty ties} \citep[Ch.~5, §4]{huddleston2002}. The D-noun analysis reduces this phrase-type inventory:
\[
\begin{aligned}
\text{\textit{CGEL}:} &\quad \mathrm{Det}:\{\mathrm{DP},\mathrm{NP},\mathrm{PP}\} \\
\text{D-noun analysis:} &\quad \mathrm{Det}:\{\mathrm{NP},\mathrm{PP}\}
\end{aligned}
\]

The gain is one shared nominal projection for the determinative and genitive cases. Selection still distinguishes determinative-headed, genitive and other licensed NPs; PP determiners remain. Reclassification doesn't derive definiteness or the single-Det restriction: \textit{CGEL} already states their common determining behaviour functionally. Independent \mention{some} and \mention{Kim's} are already NPs in both accounts. Giving \mention{some} ordinary headedness is a further change; genitive fusion remains available. Section~\ref{sec:fragment} compares these changes separately and shows how a separate-D grammar can also reduce the phrase-type inventory.

\subsection{A matched descriptive fragment}\label{sec:fragment}

A grammatical \term{fragment} is a set of rules for a specified range of constructions. Here it covers determination, ordinary subject and object uses, partitives, and the modifier and compound comparisons in §\ref{sec:evidence}. Four accounts cross separate versus nominal D with fusion versus ordinary Head. All receive the same lexical restrictions and constructed judgments. The predicative constructions in §\ref{sec:predication} fall outside the fragment.

Table~\ref{tab:permissions} records \term{use permissions}: whether a form, on a given reading, can head a phrase in determiner, subject or object function. \term{Argument use} covers the subject and object NPs in examples such as \mention{Some left} and \mention{I saw some}. Quotation, metalinguistic naming and subordinate-clause uses of dependent genitives fall outside the fragment. Noun membership doesn't itself grant a use permission.

\begin{table}[H]
\centering\small
\caption{Shared permissions in the fragment. For \mention{some}, the target column concerns its unstressed use before a noun. The inventory is deliberately limited to the displayed constructions.}\label{tab:permissions}
\begin{tabular}{lcc>{\raggedright\arraybackslash}p{6.2cm}}
\toprule
Form & Det use & Argument use & Target in the Det construction \\
\midrule
\mention{the} & yes & no & Singular or plural; count or non-count \\
\mention{a}, \mention{every} & yes & no & Singular count nominal \\
\mention{some} & yes & yes & Plural count or non-count nominal \\
\mention{few} & yes & yes & Plural count nominal \\
\mention{my} & yes & no & No number/count restriction in this fragment \\
\mention{she} & no & yes & None \\
\bottomrule
\end{tabular}
\end{table}

Further constructional restrictions apply: \mention{she} is a subject form, whereas the corresponding ordinary object form is \mention{her}. The target restrictions concern the common-noun nominal being determined: \mention{a} requires a singular count target such as \mention{book} in \mention{a book}.

Table~\ref{tab:economy} locates the four accounts. The ordinary-Head accounts differ in the categories admitted to nominal projection; the fusion accounts differ in the category of the phrase realizing the fused functions.

\begin{table}[H]
\centering\small
\caption{Taxonomy and headedness varied separately. All four accounts retain the permissions in Table~\ref{tab:permissions}, the modifier restrictions and the compound conditions.}\label{tab:economy}
\begin{tabular}{>{\raggedright\arraybackslash}p{3.1cm}>{\raggedright\arraybackslash}p{3.9cm}>{\raggedright\arraybackslash}p{4.7cm}}
\toprule
Account & Primary taxonomy & Simple independent determinative \\
\midrule
Nominal D, ordinary Head & D inside Noun & N--Nom--NP projection with Head function \\
Separate D, ordinary Head & D outside Noun & D--Nom--NP through cross-category projection \\
Separate D, fusion & D outside Noun & NP distribution through Det--Head \\
Nominal D, fusion & D inside Noun & NP distribution through Det--Head \\
\bottomrule
\end{tabular}
\end{table}

The ordinary-Head variant of the D-noun analysis combines two projection rules with a use-permission condition. In the schemata below, $h$ identifies the lexical head throughout its projection; parentheses mark optional dependents. The subscripts on Mod distinguish pre-head and post-head positions of the same modifier function. The head's entry and construction restrict every dependent.
\[
\begin{aligned}
\mathrm{Nom}_{h} &\to (\mathrm{Mod}_{\mathrm{pre}})\quad \mathrm{Head}:\mathrm{N}_{h}\quad (\mathrm{Comp})\quad (\mathrm{Mod}_{\mathrm{post}}) \\
\mathrm{NP}_{h} &\to (\mathrm{Det})\quad \mathrm{Head}:\mathrm{Nom}_{h} \\
\operatorname{licensed}(\mathrm{NP}_{h},f,c)\quad &\Longleftrightarrow\quad f\in U_h\ \land\ C_h(f,c)
\end{aligned}
\]
Here $U_h$ is the head's set of use permissions, $f$ is the NP's function, and $C_h$ checks the lexical and constructional conditions in context $c$. For Det use, these include compatibility with the target nominal; for an argument headed by a singular count common noun, they include required determination. Optionality in the second rule doesn't override those conditions.

In \mention{some apples}, \mention{some} heads an NP whose Det permission and plural-count target requirement are satisfied. \mention{Apples} heads the outer Nom, which heads the NP. In \mention{Some left}, \mention{some} heads an NP whose argument permission is satisfied. \mention{Every apple} passes the Det and singular-count checks; ordinary independent \ungram{\mention{Every left}} fails the argument-permission check. \mention{The apple} and \ungram{\mention{The left}}, with \mention{left} as a verb, differ in the same way.

Each NP's use permissions follow its own head. In \mention{the apple}, the article's Det permission licenses the dependent NP headed by \mention{the}. The outer NP takes its argument permission from \mention{apple}, whose requirement for determination is satisfied by the article.

A singular count common noun such as \mention{book} faces a different restriction from an article. In \mention{a book}, its requirement for determination is satisfied; bare \ungram{\mention{Book arrived}} leaves that requirement unsatisfied. \mention{Books arrived} has no such requirement. Requiring determination for a common noun doesn't itself block an article-headed NP from argument use. An article's exclusion from argument use must still be stated separately.

Partitives and modifiers require further lexical conditions. \mention{Some} and \mention{few} permit a partitive \mention{of}-phrase within their nominal projection. \mention{Almost} can modify \mention{every} in \mention{almost every teacher}; that permission doesn't license \mention{experienced} as a modifier of \mention{every}. The construction \mention{the lucky few} permits the external determiner and adjectival modifier shown in Figure~\ref{fig:few}. None of these permissions transfers automatically to every determinative noun.

Keeping ordinary headedness while retaining primary D gives the strongest separate-D alternative. It retains the NP and use-permission rules, but replaces the lexical-head restriction in Nom with:
\[
\mathrm{Nom}_{h}\to(\mathrm{Mod}_{\mathrm{pre}})\quad\mathrm{Head}:\{\mathrm{N}_{h},\mathrm{D}_{h}\}\quad(\mathrm{Comp})\quad(\mathrm{Mod}_{\mathrm{post}})
\]
This projection applies to dependent as well as independent determinatives, eliminating DP from the fragment while retaining primary D. Determiner selection still identifies D-headed NPs and suitable genitives. In \mention{the lucky few}, \mention{few} is D in ordinary Head function. In \mention{hardly anyone present}, the determinative base and compound construction supply the same modifier restrictions as the D-noun account. Adjectival Mod--Head fusion remains available in both.

The fusion accounts instead relate independent determinatives to their dependent counterparts. The separate-D fusion grammar already needs nominal projection for other nouns. It adds DP projection and permits a DP to realize a fused function in nominal structure. The partitive complement and compound restrictor belong to Nom, following the trees in \textit{CGEL} and \textcite[582]{Payne2007}:
\[
\begin{aligned}
\mathrm{DP}_{h} &\to (\mathrm{Mod}_{\mathrm{pre}})\quad \mathrm{Head}:\mathrm{D}_{h}\quad (\mathrm{Comp}) \\
\mathrm{Nom}_{h} &\to (\mathrm{Mod}_{\mathrm{pre}})\quad F:\mathrm{DP}_{h}\quad (\mathrm{Comp})\quad (\mathrm{Mod}_{\mathrm{post}}) \\
F&\in\{\mathrm{Det\text{--}Head},\mathrm{Mod\text{--}Head}\}
\end{aligned}
\]
The ordinary NP rule embeds this Nom. Det--Head jointly realizes Det of NP and Head of Nom, excluding a second Det; Mod--Head fills an internal modifier's function and Head of Nom, allowing external determination. Lexical and constructional conditions select the fused function and permitted dependents. These schemata cover independent \mention{few}, \mention{few of them}, \mention{the lucky few} and \mention{hardly anyone present}. The nominal-D fusion variant replaces DP here with $\mathrm{NP}_{D}$, retaining the fused relations.

The separate-D ordinary-Head account thus shares the D-noun ordinary-Head account's reduced phrase-type inventory and Head relations. Those benefits don't uniquely favour inclusion within Noun. Neither account removes the selectional alternatives, and dependent determinatives acquire a Nom layer. Their economy concerns reuse of grammatical organization, not uniformly smaller trees or fewer conditions.

A grammar with Hudson's nested classification can use the same permissions and projection rules. Holding those rules fixed, an added pronoun category between Noun and determinative leaves the fragment's judgments unchanged. Agreement on these judgments leaves the broader pronoun category open; it doesn't establish equivalence between the full analyses.

\subsection{Existing restrictions, additional costs and consequences}\label{sec:costs}

The remaining taxonomic choice is between inheritance through Noun and a projection rule spanning N and D. Separate D preserves the modifier contrast as a primary-category distinction while licensing nominal projection across that boundary. D-noun makes projection an inherited property and states the modifier contrast within Noun.

The cost of this change needs separating from restrictions already present in the grammar. Common nouns, proper nouns and pronouns already differ in determination and permitted modifiers (Table~\ref{tab:existing}). Preserving those conditions is no additional cost of including determinatives. Likewise, the separate-D grammar already restricts adverbial modification and independent use within D. Moving those restrictions inside Noun doesn't create them.

\textcite[75, n.~3]{payne2010} analyse \mention{almost} as a modifier of the attributive noun \mention{textbook} in \mention{an almost textbook case}. The D-noun analysis extends such premodification to a systematic noun subcategory, including \mention{hardly any} and \mention{almost every}. Its cost is stating the usual modifier contrast at that subcategory boundary. In compounds, the inherited premodifier permissions must also be distinguished from the post-head restrictor construction (§\ref{sec:compounds}). These are explicit qualifications on shared projection.

Why should systematic nominal projection warrant inclusion for pronouns but require cross-category licensing for determinatives? I favour placing the recurring external and structural profile at Noun, with modifier and use restrictions at the subcategories and constructions that distinguish them. This applies the existing membership rationale consistently. The auxiliary-as-verb precedent illustrates the same separation between a shared category and specialized syntax; the nominal evidence supplies the justification here.

This preference gives shared nominal organization more weight than primary rank for the modifier boundary. The compound and adjectival comparisons expose the costs of that choice. The fragment demonstrates how the accounts allocate the generalizations, rather than proving a unique minimum description length.

Cardinals illustrate a consequence of broadening Noun. \textcite{reynolds2026numerals} distinguishes determinative uses such as \mention{ten men}, proper-noun uses such as \mention{Room 101}, and common-noun uses such as \mention{tens of pens}. Under the D-noun analysis, these uses fall within one superordinate category, with their differences retained at the subcategory and construction levels. This recasts the cardinal alternation without eliminating it. The argument doesn't extend to ordinals, which that study analyses as adjectives, or turn complex numeral phrases into single lexemes.

Complex cardinals also separate category from function. In \mention{two hundred books}, the whole \mention{two hundred} fills Det; internally, \mention{two} modifies the magnitude head \mention{hundred} \citep[§4]{reynolds2026numerals}. In \mention{these two hundred books}, \mention{these} fills Det and \mention{two hundred} is an internal modifier. Including determinatives within Noun preserves these relations. One Det function doesn't entail a limit of one determinative lexeme per NP.

The shared projection proposed in §\ref{sec:det-uniform} would lose its claimed economy if determinative-headed and genitive NPs required different projection rules after their independently motivated feature restrictions were held fixed. Such a result would favour retaining the separate phrase types.

\section{Conclusion}\label{sec:conclusion}

The comparisons support including determinative within Noun in English. Across independent uses, partitives and modification, the analysis gives determinatives shared nominal structure while retaining their lexical and constructional restrictions, including those of the articles. \textit{CGEL} already admits pronouns on comparable grounds despite differences in inflection and dependents. The D-noun analysis extends that membership rationale.

Within Noun, coordination remains provisional: the fragment's judgments don't distinguish it from Hudson's nesting. An intermediate category would be preferable if it captured further generalizations otherwise repeated.

Ordinary headedness remains a further proposal. It unifies bare, partitive and externally determined uses under Head; fusion instead captures correspondences with dependent uses and separates modifier domains structurally in compounds. A separate-D grammar can also share nominal projection. The comparison therefore concerns inheritance through Noun versus cross-category licensing, not coverage alone. I favour inheritance: it extends \textit{CGEL}'s rationale for pronoun membership, at the cost of reformulating the modifier contrast within Noun. Shared nominal structure belongs at the superordinate category; the differing permissions remain at subcategory and construction levels.

\section*{Data and analysis materials}

The accompanying supplements are \href{run:matrix-audit.pdf}{\textit{Replication audit of the English determinative--pronoun feature matrix}} and \href{run:corpus-documentation.pdf}{\textit{CGELBank concordance and extraction notes}}. The \texttt{analysis/} directory preserves their input files, provenance records, scripts, numerical outputs and sentence concordance. Its README identifies the files and reproduction procedures.

\vspace{0.5\baselineskip}
\noindent\textsc{Acknowledgements.} For the September 2026 revision, GPT-6 (Astra), Claude Opus~5, Claude Haiku~4.5 and GLM-5.3-Flash assisted drafting, source retrieval, script development or critical review; GPT-5.6 (Sol) checked numerical outputs. The accompanying materials record the tools and their uses. Responsibility for the analysis is mine.

\clearpage
\printbibliography
\end{document}


=== ARTICLE REFERENCE LIST (PDF TEXT) ===

References
Abney, S. P. (1987). The English noun phrase in its sentential aspect [Doctoral dissertation, Massachu-
         setts Institute of Technology].
Anderson, J. M. (1997). A notional theory of syntactic categories. Cambridge University Press. https:
         //doi.org/10.1017/CBO9780511519734
Bruening, B. (2020). The head of the nominal is N, not D: N-to-D movement, hybrid agreement,
         and conventionalized expressions. Glossa: a journal of general linguistics, 5(1), Article 15. ht
         tps://doi.org/10.5334/gjgl.1031
Déchaine, R.-M., & Wiltschko, M. (2002). Decomposing pronouns. Linguistic Inquiry, 33(3), 409–
         442. https://doi.org/10.1162/002438902760168554
Huddleston, R., & Pullum, G. K. (2002). The Cambridge grammar of the English language. Cam-
         bridge University Press. https://doi.org/10.1017/9781316423530
Huddleston, R., Pullum, G. K., & Reynolds, B. (2022). A student’s introduction to English grammar
         (2nd ed.). Cambridge University Press. https://doi.org/10.1017/9781009085748
Hudson, R. (2004). Are determiners heads? Functions of Language, 11(1), 7–42. https://doi.org/10
         .1075/fol.11.1.03hud
Hudson, R. (2010). An introduction to Word Grammar. Cambridge University Press.
Lyons, C. (1999). Definiteness. Cambridge University Press. https://doi.org/10.1017/cbo9780511
         605789
Lyons, J. (1968). Introduction to theoretical linguistics. Cambridge University Press. https://doi.org
         /10.1017/CBO9781139165570
Palmer, H. E. (1924). A grammar of spoken English on a strictly phonetic basis. W. Heffer & Sons Ltd.
Payne, J., Huddleston, R., & Pullum, G. K. (2007). Fusion of functions: The syntax of once, twice
         and thrice. Journal of Linguistics, 43(3), 565–603. https://doi.org/10.1017/S00222267070
         0477X
Payne, J., Huddleston, R., & Pullum, G. K. (2010). The distribution and category status of adjectives
         and adverbs. Word Structure, 3(1), 31–81. https://doi.org/10.3366/E1750124510000486
Postal, P. M. (1966). On so-called “pronouns” in English. In F. P. Dinneen (Ed.), Report of the seven-
         teenth annual round table meeting on linguistics and language studies (pp. 177–206). Geor-
         getown University Press.
Pullum, G. K., & Miller, P. (2022). NPs versus DPs: Why Chomsky was right [Working paper. Eng-
         lish version of Miller & Pullum 2022, Revue CORELA HS-37]. https://lingbuzz.net/lingb
         uzz/006845
Pullum, G. K., & Wilson, D. (1977). Autonomous syntax and the analysis of auxiliaries. Language,
         53(4), 741–788. https://doi.org/10.2307/412911
Reynolds, B. (2021). Quantifying the differences between lexical categories: The case of pronouns
         and determinatives in English. Cadernos de Linguística, 2(3), Article e399. https://doi.org
         /10.25189/2675-4916.2021.V2.N3.ID399
Reynolds, B. (2025). Personhood and pro-forms: A hierarchical analysis of gender in Modern English
         [Manuscript submitted to Folia Linguistica].
Reynolds, B. (2026). The lexicon–syntax boundary in English numerals: Cardinals, ordinals, and
         fractionals [Published online 4 February 2026]. English Language and Linguistics, 1–19. ht
         tps://doi.org/10.1017/S1360674325100518
REFERENCES                                                                                          24


Reynolds, B., Arora, A., & Schneider, N. (2023). Unified syntactic annotation of English in the
        CGEL framework. In J. Prange & A. Friedrich (Eds.), Proceedings of the 17th linguistic an-
        notation workshop (LAW-XVII) (pp. 220–234). Association for Computational Linguistics.
        https://doi.org/10.18653/v1/2023.law-1.22
Sommerstein, A. H. (1972). On the so-called definite article in English. Linguistic Inquiry, 3(2), 197–
        209. https://www.jstor.org/stable/4177701
Spinillo, M. G. (2004). Reconceptualising the English determiner class [PhD thesis]. University Col-
        lege London. https://discovery.ucl.ac.uk/id/eprint/10101595/
Van Eynde, F. (2003). On the notion “determiner”. In S. Müller (Ed.), Proceedings of the 10th Inter-
        national Conference on Head-Driven Phrase Structure Grammar (pp. 391–396). CSLI Pub-
        lications. https://doi.org/10.21248/hpsg.2003.22


=== MATRIX AUDIT SUPPLEMENT ===
\documentclass[12pt]{article}
\input{.house-style/preamble.tex}
\usepackage{xurl}
\usepackage{float}
\setlength{\headheight}{14pt}
\clubpenalty=10000
\widowpenalty=10000
\emergencystretch=1em
\AtBeginBibliography{\emergencystretch=1em}
\setcounter{biburlnumpenalty}{100}
\newcommand{\tablebody}[1]{\csname @@input\endcsname #1 }
\hypersetup{pdftitle={Replication audit of the English determinative--pronoun feature matrix}}
\title{Replication audit of the English determinative--pronoun feature matrix}
\author{Brett Reynolds}
\date{Supplementary material, September 2026}
\fancyhead[L]{\small\scshape Determinative--pronoun matrix audit}
\begin{document}
\maketitle

\section{Scope of the audit}

This supplement audits the numerical analysis reported by \textcite{reynolds2021} and the publicly available feature matrix \citep{reynolds2021matrixpublic}. It preserves the reporting discrepancies, implementation findings and sensitivity results separately from the grammatical argument in \textit{Determinatives as nouns in English}.

The matrix compares 73 determinative forms and 65 pronoun forms. Each row represents a form, and each binary column records a morphological, phonological, semantic or syntactic property. Cells record whether a form may exhibit the property. Most feature definitions follow \textit{The Cambridge grammar of the English language} (\textit{CGEL}; \citealt{huddleston2002}); the coding also draws on other sources and the author's judgments.

There are no common or proper nouns. The analysis can therefore compare the supplied profiles, but can't test their inclusion within a superordinate Noun category. Even perfect recovery of the determinative--pronoun distinction would be compatible with shared nounhood; the original discussion likewise leaves a nested nominal analysis open.

DISCO compares the supplied partition with shuffled partitions. The k-groups procedure searches for clusters without using the supplied category assignments. The audit distinguishes recovery of the published numerical decomposition from recovery of a clustering result whose original random state wasn't recorded.

\section{Inputs and provenance}

The article by \textcite{reynolds2021} and the LingBuzz description of its matrix report 232 features, but the public file contains 155 \citep{reynolds2021matrixpublic}. The reanalysis preserves that file with its checksum and compares it with a recovered local 232-feature working matrix. The working matrix isn't authenticated as the published input. The public file reproduces the published DISCO decomposition: between-group component 30.58286, within-group component 356.41607 and total 386.99893, giving $F=11.670$ to the reported precision.
% Source: analysis/results/disco-sensitivity.csv, public155; published Table 3.



The public CSV was retrieved on 7 September 2026 and is retained unchanged as \nolinkurl{analysis/data/matrix155-lingbuzz.csv}. Its SHA-256 is \nolinkurl{a15af082a6bc5dbe24bcf57475c35cad1b00c2dc7e17af584db1841bf7abddf7}. The source manifest records the retrieval and the matching previously held file. The recovered working input and its original source hash are recorded separately in \nolinkurl{analysis/data/source-manifest.json}.

The two matrices differ by 77 removed columns (76 singleton features and one all-zero feature), 11 changed cells in \nolinkurl{Start_with_hw}, and two normalized row names. One singleton feature remains in the public file. An earlier draft of \textit{Determinatives as nouns} incorrectly claimed that removing singleton features leaves between-form distances unchanged. The lineage report, removed-feature list and coding-change table preserve the exact comparison.

\section{Procedures and sensitivity results}

DISCO and k-groups use Euclidean distances between unscaled binary rows: the square root of the number of feature mismatches. Columns receive equal weight, so correlated diagnostics affect the geometry. DISCO uses \textit{CGEL}'s determinative/pronoun partition. Runs with 999 permutations and seed 20260907 give \mbox{$p=.001$} across the representations in Table~\ref{tab:matrix}, the minimum attainable value. The observations are coded word forms; the tests concern separation within this inventory.

Here the permutation results describe comparison with shuffled partitions of these rows. They aren't population-level inference under a defended exchangeability assumption. Paradigmatic relations and repeated compound material connect word forms; removing word-component columns doesn't remove those relations among rows. The reported values show how the supplied partition compares with the shuffled partitions under this representation, without treating the forms as independent samples from a linguistic population.

The published k-groups code records a single random start and no seed. After removing the name column, it removes the first remaining feature during clustering. The reanalysis therefore tests both the public 155-feature input and that 154-feature implementation. For each representation, 100 single-start fits use seeds 1--100 and the published limit of ten iterations. A separate fit uses 100 starts and a limit of 100 iterations, selecting the best objective~-- the clustering criterion being minimized~-- among those starts.

\begin{table}[H]
\centering\small
\caption{Exploratory sensitivity of the matrix analysis. The range is agreement out of 138 across 100 single-start fits. The last column is agreement for the best-objective fit among a separate set of 100 starts, not the maximum agreement observed. All displayed DISCO runs give \mbox{$p=.001$} with 999 permutations.}\label{tab:matrix}
\begin{tabular}{>{\raggedright\arraybackslash}p{5.1cm}rrrr}
\toprule
Representation & Features & DISCO $F$ & Range & Best objective \\
\midrule
\tablebody{analysis/generated/matrix-table.tex}
\bottomrule
\end{tabular}
\end{table}

Cluster labels are oriented after fitting to maximize agreement with \textit{CGEL}'s classification. Eight public-matrix single-start fits reproduce the published count of 129 matches; the 100-start fit yields 125. The 154-feature implementation also varies across starts. Selecting the best clustering objective doesn't select the closest match to \textit{CGEL}'s labels. Reducing the feature set can increase agreement in the fit selected by that objective, but the increase doesn't independently support the taxonomy: the feature representation has changed.

Removing 50 word-component columns changes best-objective agreement to 131/138. The 50 syntactic columns yield 120/138; removing four explicit analysis labels yields 97/138. Those labels concern fused determiner-head function, partitive head function, subject-determiner function and coordination with non-fused determiners. This is a limited sensitivity check: the remaining judgments still reflect the descriptive framework. Complete scripts, feature changes, seed schedules and outputs accompany the paper.

\section{Reproduction files and correction record}

The accompanying \nolinkurl{analysis/README.md} describes the inputs and reproduction commands. The scripts \nolinkurl{analysis/recover_matrix.py} and \nolinkurl{analysis/reproduce_matrix.R} preserve the recovery and analysis procedures. The run used R 4.6.1 and \texttt{energy} 1.7-12; \nolinkurl{analysis/results/R-session-info.txt} records the environment. The seed schedules and full outputs include the 154-feature implementation and the unauthenticated recovered working matrix, beyond the selected representations in Table~\ref{tab:matrix}.

The within-category checks record both the determinative split implemented in the published appendix and the pronoun split described in its prose. Neither is treated as a taxonomic-rank test. The legacy distance audit records selected-group distances used in an archived draft; those groups don't supply a justified measure of prototype centrality.

An independent review reran the matrix and corpus analyses and reproduced their outputs byte for byte; a separate numerical check found no discrepancies. Their records are preserved in \nolinkurl{reviews/review-board-20260907-rebuild/corpus.md} and \nolinkurl{reviews/review-board-20260907-rebuild/numbers-second-model.md}. Computational assistance is documented in \nolinkurl{analysis/ai-assistance.txt}.

The prepared notice \nolinkurl{analysis/public-matrix-correction.txt} identifies the public-file discrepancy and clustering issues. It has not been posted to the original resource. Neither the public CSV nor the earlier article has been silently replaced. The recovered 232-feature matrix remains a distinct, unauthenticated working input. This supplement makes the correction trail available with the present paper; updating the original public records is a separate action.

\printbibliography
\end{document}


=== CORPUS DOCUMENTATION SUPPLEMENT ===
\documentclass[12pt]{article}
\input{.house-style/preamble.tex}
\usepackage{xurl}
\usepackage{float}
\setlength{\headheight}{14pt}
\clubpenalty=10000
\widowpenalty=10000
\emergencystretch=1em
\AtBeginBibliography{\emergencystretch=1em}
\setcounter{biburlnumpenalty}{100}
\newcommand{\tablebody}[1]{\csname @@input\endcsname #1 }
\hypersetup{pdftitle={CGELBank concordance and extraction notes}}
\title{CGELBank concordance and extraction notes}
\author{Brett Reynolds}
\date{Supplementary material, September 2026}
\fancyhead[L]{\small\scshape CGELBank concordance and extraction notes}
\begin{document}
\maketitle

\section{Scope and source}

This supplement preserves the CGELBank concordance, extraction procedure and annotation counts accompanying \textit{Determinatives as nouns in English}. The article uses selected sentences as attestations of the constructions under discussion. The inventory doesn't estimate productivity or test the competing taxonomies.

CGELBank contains English sentences annotated using categories and functions developed from \textit{The Cambridge grammar of the English language} \citep{reynolds2023unified}. D labels the determinative category; Det and Mod label determiner and modifier functions. The sentences provide inspectable examples. The category and fusion labels encode analytical decisions and can't independently confirm those analyses or their replacements.

The source is the \href{https://github.com/nert-nlp/cgel/tree/d0a2c2d8c522b23d5aa879fc9cb94948f4285b2c}{CGELBank repository} at revision \nolinkurl{d0a2c2d8c522b23d5aa879fc9cb94948f4285b2c}, licensed CC BY 4.0. The inventory includes four top-level gold datasets: \nolinkurl{twitter.cgel}, \nolinkurl{ewt.cgel}, \nolinkurl{ewt-test_pilot5.cgel} and \nolinkurl{ewt-test_iaa50.cgel}. Trial material, one-off examples and duplicate versions from the annotation study are excluded. The source manifest records each file's checksum.

\section{Extraction and annotation counts}

The inventory contains 220 sentence trees and 3,390 lexical nodes with overt text. Of those nodes, 387 are annotated D. Multiword lexical nodes count once. Overt source errors and deleted source tokens remain, with the corpus's correction information retained. Lemmas follow the supplied correction or lemma where available and are lowercased. These are annotation-token counts, not whitespace-word counts.

For each D node, extraction follows Head relations upwards to the first non-Head relation, identifying the local function of its projection. The resulting counts are Det (297), Mod (18), Det--Head (65), Marker (1), Flat (4) and Coordinate (2). Det--Head combines determiner and head functions. The concordance records each local phrase, its nearest containing noun phrase (NP) and that NP's function, and the source sentence. Following the projection avoids counting a determiner embedded in a partitive domain as its outer quantifier.

Table~\ref{tab:corpus} compares selected forms. These are counts of annotated uses, not estimates of a lexeme's capacity for independent use.

\begin{table}[H]
\centering\small
\caption{Selected forms by local function in CGELBank. Compare forms attested in both Det and Det--Head uses with forms restricted to Det in this sample. Other includes all remaining functions. Counts group forms by corpus lemma, including singular and plural demonstratives.}\label{tab:corpus}
\begin{tabular}{lrrrr}
\toprule
Form & Total & Det & Det--Head & Other \\
\midrule
\tablebody{analysis/generated/corpus-table.tex}
\bottomrule
\end{tabular}
\end{table}

The full inventory contains 65 Det--Head occurrences, all inspected in their source sentences. They include ordinary arguments, partitives, compounds such as \mention{something}, floating quantifiers, degree and frequency expressions, numerical fragments and age supplements. In \mention{about 30 seconds}, for example, the numeral's nominal projection is embedded in the determiner \mention{about 30}. Reporting all 65 as independent argument uses would therefore conflate different constructions.

The sample has no determinative tokens of bare \mention{few}, \mention{either} or \mention{neither}. Its gaps don't establish ungrammaticality. The inventory provides no representative productivity estimate or controlled test of modifier contrasts.

\section{Attestations and identifiers}

Two attestations illustrate independent quantifiers with a recoverable discourse domain:
\ea\label{ex:attested-quantifiers}
\ea \mention{Went there yesterday: we are trying to decide between two different Honda models, so we wanted to test-drive both back to back.}
\ex \mention{I rarely listen to the news or to what politicians or lawyers say because so many tell lies that none have credibility so what's the point?}
\z\z

In (a), \mention{both} refers to the two Honda models. In (b), \mention{politicians or lawyers} supplies a domain for \mention{many} and \mention{none}. These are examples of independent use with contextual interpretation, not evidence of an antecedent-free reading.

Example (a) is sentence \href{https://github.com/nert-nlp/cgel/blob/d0a2c2d8c522b23d5aa879fc9cb94948f4285b2c/datasets/ewt.cgel\#L651-L654}{\nolinkurl{reviews-083459-0002}} in \nolinkurl{ewt.cgel}. Example (b) has identifier \nolinkurl{newsgroup-groups.google.com_INTPunderground_b2c62e87877e4a22_ENG_20050906_165900-0074}. Both resolve in \nolinkurl{analysis/results/corpus-concordance.csv} and \nolinkurl{analysis/results/corpus-det-head-review.csv}.

CGELBank also attests \mention{I need something reliable and good looking}, sentence \href{https://github.com/nert-nlp/cgel/blob/d0a2c2d8c522b23d5aa879fc9cb94948f4285b2c/datasets/ewt-test_iaa50.cgel\#L179-L181}{\nolinkurl{answers-20111024111513AAAQhAO_ans-0003}} in \nolinkurl{ewt-test_iaa50.cgel}. The original text has \mention{good looking}; the normalized annotation has \mention{good-looking}. The article retains the source wording. This example documents postmodification of a compound determinative; it doesn't test premodification in \mention{the lucky few}.

\section{Reproduction files}

Run \nolinkurl{analysis/corpus_inventory.py} against a checkout at the recorded revision. The script rejects a different Git commit. Its parser requires \texttt{pylatexenc} (audit version 2.11). Commands and environment details are retained in \nolinkurl{analysis/README.md}.

The file \nolinkurl{analysis/results/corpus-manifest.json} records the source revision, dataset checksums, totals and function counts. The concordance and Det--Head review preserve the extracted expressions and their sentence contexts. The selected-form table remains generated from the recorded outputs. An independent review reproduced the extraction outputs and inspected all 65 Det--Head contexts; its report is \nolinkurl{reviews/review-board-20260907-rebuild/corpus.md}.

\printbibliography
\end{document}
