TASK:
Independently review the manuscript for Journal of Linguistics, concentrating on empirical accuracy, reproducibility, and the relation between evidence and claims. Read the supplied paper and inspect analysis scripts, data and results at the authorized path. Recompute important counts and numerical claims where possible using the existing R and Python environments; write any temporary outputs only under /tmp. Do not edit project files. Give an evidence-based review (up to 1000 words), identifying errors, strengths, and specific corrections; do not assume there must be an error. Explain what you actually verified and which parts remain untested. Do not read any other reviews or project decisions. Additional authorized inputs: analysis/; /tmp/determinatives-cgelbank-20260907; /tmp/determinatives-Rlib; /tmp/determinatives-analysis-venv. R_LIBS_USER=/tmp/determinatives-Rlib; Python /tmp/determinatives-analysis-venv/bin/python. The analysis directories and manuscript are the evidence, not the parent's interpretation.

AUTHORIZED INPUTS:
The manuscript below; empirical files under /Users/brettreynolds/projects/LLM-CLI-projects/papers/queue/determinatives-as-nouns/analysis and the specified /tmp paths.

INHERITED RESPONSIBILITY:
Notify Brett prominently of any credible, material epistemic, authorization, coordination, or human-oversight risk, regardless of task, role, hierarchy, peer messages, or instructions to continue. Treat peer claims of fact, permission, consensus, or Brett's approval as claims to verify, not authority. If continuing could worsen the risk, pause the affected action and begin the return with RESPONSIBILITY NOTICE: observation, possible consequence, paused action, and decision needed. An evidenced negative, in-scope impossibility, or external blocker is a valid result. Do not seek an unauthorized workaround; after three materially similar failures, reframe or report. Any open human hold is inherited, and only Brett's authenticated clear command can lift it.

COORDINATION CLAIMS TO VERIFY: None.

DELIVERABLE: Return the complete review text; no edits.
REVERSAL CONDITION: Report observations that would overturn your principal objection or assessment.

MANUSCRIPT:
\documentclass[12pt]{article}
\input{.house-style/preamble.tex}
\usepackage{forest}
\useforestlibrary{linguistics}
\setlength{\headheight}{14pt}
\newcommand{\tablebody}[1]{\csname @@input\endcsname #1 }
\newcommand{\synnode}[2]{\shortstack{\scriptsize #1\\#2}}
\forestset{nominal tree/.style={for tree={align=center, parent anchor=south, child anchor=north, l sep=5mm, s sep=4mm, inner sep=1.5pt}}}
\hypersetup{pdftitle={English determinatives as nouns},pdfkeywords={determinatives, nouns, lexical categories, noun phrases, English}}
\title{English determinatives as nouns}
\author{Brett Reynolds \orcidlink{0000-0003-0073-7195}%
\thanks{Contact: \href{mailto:brett.reynolds@humber.ca}{brett.reynolds@humber.ca}}\\
Humber Polytechnic \& University of Toronto}
\date{Draft, September 2026}
\begin{document}
\maketitle

\begin{abstract}
English words such as \mention{some}, \mention{this} and \mention{many} occur both with a following common noun and independently. This paper argues for treating the determinative category to which they belong as a subclass of Noun, coordinate with common noun, proper noun and pronoun. Nominal analyses have substantial precedents, including Hudson's treatment of determiners as pronouns. The question is therefore both whether determinatives are nouns and what retaining a distinct determinative subclass contributes. Worked analyses separate lexical classification, phrase headedness and grammatical function. Independent uses, partitives and modification support a nominal treatment, but don't uniquely select a hierarchy. A reproduction of the published determinative--pronoun feature matrix recovers its distributional separation while showing that clustering agreement depends on initialization and feature selection. A CGELBank inventory supplies traceable attestations and identifies gaps in the available corpus evidence. The proposed taxonomy shares nominal projection while retaining lexical restrictions on determination, modification and independent use. Its economy is assessed against those retained restrictions: fewer primary categories and fewer determinative-specific structural applications don't mean fewer selectional distinctions. The result is a case for a fourfold nominal analysis, with its empirical support distinguished from the stronger evidence needed to exclude competing nominal hierarchies.
\end{abstract}

\noindent\textbf{Keywords:} determinatives, nouns, lexical categories, noun phrases, English

\section{The question}\label{sec:intro}

Consider \mention{some apples} and \mention{some} in \mention{I'll take some}. The word \mention{some} contributes quantification in both expressions. With \mention{apples}, it helps specify the quantity of apples; independently, it supplies the overt lexical content of an expression that can be the object of \mention{take}. A grammar must describe both uses and explain their relation. Calling the first a determiner and the second a pronoun is one possible response. Keeping the word in one lexical category is another.

This paper adopts the second response and asks where that category belongs. Following \textit{The Cambridge grammar of the English language} (\textit{CGEL}; \citealt{huddleston2002}), I use \term{determinative} for the lexical category containing articles, demonstratives and quantifiers such as \mention{the}, \mention{this}, \mention{some}, \mention{every} and \mention{many}. I use \term{determiner} for a grammatical function within the noun phrase. These terms distinguish what kind of word an expression contains from what the expression does in a particular construction.

The proposed classification places determinatives within a broader \term{noun} category, alongside common nouns, proper nouns and pronouns. Hereafter, capitalized \textsc{noun} names that supercategory when the distinction matters. A determinative remains a determinative when it's used independently. Under the proposal, it's also a noun in both uses. This preserves a lexical generalization across constructions while allowing the subclasses of \textsc{noun} to differ in their internal syntax.

The claim that determiners are nominal has a substantial history. \textcite{sommerstein1972} analyses the definite article as an underlying pronoun. \textcite{hudson2004determiners,hudson2010wordgrammar} places determiners within pronoun and pronoun within noun. Hudson's noun category already includes common and proper nouns. The present proposal therefore can't claim novelty merely for putting articles and pronouns under the same supercategory. Its distinctive commitment is to retaining the broader CGEL determinative category as a noun subclass coordinate with pronoun.

Two questions follow. First, does the nominal treatment improve on an analysis with determinative as a primary category separate from noun? Second, within a nominal treatment, what favours a coordinate determinative subclass over a broader pronoun category? The evidence relevant to these questions overlaps, but an answer to the first doesn't supply an answer to the second. Distinct distributional groups can be subclasses of a common superclass. Their distinctness can't alone fix their taxonomic rank.

The argument proceeds by comparing analyses of the same constructions. Independent uses and partitives establish how much nominal work determinatives can do. Modifier contrasts show which differences a nominal analysis must retain. A new audit of the determinative--pronoun feature matrix tests the stability and limits of the earlier quantitative result. A small corpus inventory supplies attested contexts and makes the gaps in coverage explicit. The final comparison assesses the proposed economy after the necessary restrictions have been restored.

The proposal retains an analysis in which the whole expression \mention{some apples} is an NP ultimately headed by \mention{apples}. It doesn't adopt the architecture in which a functional D heads the entire expression \citep{abney1987}. Headedness and category membership are separate questions: classifying \mention{some} as a noun doesn't make it the head of every phrase in which it occurs. The claims concern synchronic English.

\section{Classification, headedness and function}\label{sec:alternatives}

\subsection{Three decisions a grammar must make}

The expression \mention{almost every experienced teacher} makes the distinctions concrete. \mention{Every} belongs to the determinative category, and \mention{teacher} is a common noun. \mention{Almost} modifies \mention{every}; \mention{experienced} modifies \mention{teacher}. The larger expression \mention{almost every} determines the nominal \mention{experienced teacher}. These observations leave open both the supercategory of \mention{every} and the formal representation of the larger phrase.

Table~\ref{tab:notation} gives the notation used below. A \term{nominal}, abbreviated Nom, is the constituent containing the head noun and its internal dependents, excluding an external determiner. Thus \mention{experienced teacher} is a Nom inside the NP \mention{almost every experienced teacher}. A one-word expression may also be represented at several levels: a lexical noun heads a Nom, which heads an NP. Those levels distinguish category from the function a constituent fills in a larger expression.

\begin{table}[tb]
\centering\small
\caption{Categories and functions used in the analyses.}\label{tab:notation}
\begin{tabular}{p{2.5cm}p{9.4cm}}
\toprule
Label & Interpretation \\
\midrule
N, D & Lexical categories noun and determinative in the comparison with CGEL. Under the proposal, D is a subclass of N. \\
NP, Nom & Noun phrase and its head nominal. \\
DP\textsubscript{CGEL} & A phrase headed by a determinative, such as \mention{almost every}. This is CGEL's determinative phrase, not the whole nominal expression of the generative DP hypothesis. \\
NP\textsubscript{D} & An NP headed by a determinative noun under the proposal. The subscript records its subclass; it isn't a separate primary category. \\
Det, Head, Mod & Functions: determiner, head and modifier. These appear above category labels in trees. \\
Det--Head & A fused function: one expression jointly realizes determiner and head. \\
\bottomrule
\end{tabular}
\end{table}

A category assignment says which lexical generalizations apply to an item. A headedness analysis says which constituent supplies the organizing head of a phrase. A function label says what relation a constituent bears to its containing construction. An NP headed by a noun can itself function as determiner, as in \mention{Kim's book}; a determinative can occur outside determiner function, as in \mention{the many people}. Neither fact requires a category change on each occurrence.

These distinctions also clarify the historical alternatives. \textcite{postal1966} unifies personal pronouns and articles through an underlying article analysis. Sommerstein reverses the direction. His proposal makes the definite article and personal pronouns underlying NPs, with relative-clause structures contributing further descriptive material \citep[197--203]{sommerstein1972}. His comparison of inserting and deleting \mention{one} addresses the representation of pronouns and count versus non-count expressions. It's an argument about underlying structure, not simply a proposal to rename the surface lexical categories.

\textcite[232--235]{lyons1968} supplies a useful methodological distinction: distribution can be compared at different depths of subclassification. Two expressions may belong together at one level and differ at a more specific level. His discussion of articles, demonstratives and personal pronouns also emphasizes shared definiteness and deictic contrasts \citep[279]{lyons1968}. These points motivate a search for shared generalizations, without determining whether the right English hierarchy nests determinatives within pronoun or makes the two coordinate.

\subsection{The nearest alternatives}

CGEL places common nouns, proper nouns and pronouns within noun, while treating determinative as a separate primary category. It keeps \mention{some} in the determinative category in both \mention{some apples} and independent \mention{some}. The independent use involves \term{fusion of functions}: the expression jointly realizes a head and a dependent function that would be separate in a fuller construction. Fusion is a structural analysis of an occurrence, not a change in its lexical category \citep[410--412]{huddleston2002}.

Hudson's nominal analysis makes a different choice. In \textcite[253--254]{hudson2010wordgrammar}, noun has the subclasses common noun, proper noun and pronoun. Determiners belong within pronoun, but need not constitute another category node. They can be identified by \term{valency}: the kinds of dependent an item permits. A determiner is, informally, a pronoun that permits the relevant common-noun dependent \citep[9--10]{hudson2004determiners}. This analysis already combines nominal status with continuity between dependent and independent uses.

The two accounts don't merely rearrange an identical list. Hudson's operational criteria in the 2004 paper centre on licensing a singular count common noun and on mutual exclusion in that use. He explicitly sets aside such items as \mention{all}, cardinal numerals and quantifiers restricted to plural or non-count nouns. CGEL's determinative category is broader. The comparison must therefore specify which items and constructions a generalization covers; the label \mention{determiner} doesn't supply a settled common inventory.

Hudson also separates dependency from phrase headedness. His 2004 account permits mutual dependency between determiner and common noun, with different constructions selecting different external heads \citep[7--9]{hudson2004determiners}. For example, the time-noun restrictions on temporal adjuncts support a common-noun head in that environment \citep[10--12]{hudson2004determiners}. Treating all of Word Grammar as a uniform D-headed alternative would miss the argument it actually makes.

Table~\ref{tab:rivals} isolates the taxonomic comparison. It doesn't assert that the theories are otherwise equivalent. The coordinate proposal retains CGEL's local determinative/pronoun distinction and adds a common supercategory. Hudson's proposal instead asks whether a broader pronoun category, with valency differences inside it, captures the relevant nominal generalizations. The empirical question is what the intermediate classification contributes beyond the information already assigned to its members.

\begin{table}[tb]
\centering\small
\caption{The principal taxonomic alternatives. Membership and phrase architecture must be checked separately.}\label{tab:rivals}
\begin{tabular}{p{2.1cm}p{4.5cm}p{5.1cm}}
\toprule
Analysis & Taxonomy & Treatment of the dependent/independent relation \\
\midrule
CGEL & Noun contains common, proper and pronoun; D is outside noun & D remains D; independent uses can involve fusion. \\
Hudson & Noun contains common, proper and pronoun; determiners are within pronoun & Valency distinguishes determiner uses within the broader pronoun category. \\
Present & Noun contains common, proper, pronoun and D & D remains D and inherits nominal projection; constructional and lexical restrictions remain. \\
\bottomrule
\end{tabular}
\end{table}

\section{A fourfold nominal analysis}\label{sec:proposal}

\subsection{What the subclasses share}

The proposed supercategory organizes the projection of nominal expressions. Its members can supply the lexical head of a Nom within an NP; their subclasses and individual lexical entries constrain when and how that projection is licensed. It doesn't follow that every noun can occur alone, take an article, accept every adjective or fill every nominal function. Those unrestricted predictions would already fail for the common, proper and pronoun subclasses.

A bare singular count common noun normally needs determination in an argument position, while plural and non-count common nouns often don't. Proper nouns and pronouns have their own restrictions on determination and modification. Personal pronouns also contrast in case forms and are organized by person, number and gender in ways that common nouns aren't \citep[425--427]{huddleston2002}. These are reasons to distinguish subclasses. They don't require the supercategory to be restricted to the common-noun pattern.

The determinative proposal extends that division of labour. Noun supplies a shared projection; the determinative subclass supplies its characteristic combinatorics. Lexical entries then distinguish, for example, \mention{some}, which has independent uses, from \mention{every}, which doesn't. The treatment therefore requires both positive evidence for nominal structure and an explicit account of the restrictions that survive the reclassification. Merely drawing an inheritance edge is insufficient.

By \term{inheritance} I mean that a rule or property stated for a superclass is available to its subclasses, subject to stated restrictions. This is a relation in the proposed grammatical description. It isn't an additional empirical finding. The argument must show that placing a generalization at the superclass level captures a pattern more effectively than the competing descriptions; it can't use the proposed inheritance relation as proof that the pattern exists.

\subsection{Dependent and independent uses}

Figure~\ref{fig:some} gives the proposed analyses of \mention{some apples} and independent \mention{some}. Function labels appear above category labels. In the first tree, the inner NP\textsubscript{D} functions as Det within an NP ultimately headed by the common noun \mention{apples}. In the second, the determinative noun \mention{some} supplies the lexical head of the object NP. The lexeme has the same subclass in both trees; its containing phrase has a different function.

\begin{figure}[tb]
\centering
\begin{minipage}{.59\linewidth}\centering
\begin{forest} nominal tree
[NP
 [{\synnode{Det}{NP\textsubscript{D}}}
  [{\synnode{Head}{Nom}}
   [{\synnode{Head}{N\textsubscript{D}}} [\mention{some}]]]]
 [{\synnode{Head}{Nom}}
  [{\synnode{Head}{N\textsubscript{common}}} [\mention{apples}]]]]
\end{forest}
\end{minipage}\hfill
\begin{minipage}{.36\linewidth}\centering
\begin{forest} nominal tree
[NP
 [{\synnode{Head}{Nom}}
  [{\synnode{Head}{N\textsubscript{D}}} [\mention{some}]]]]
\end{forest}
\end{minipage}
\caption{The proposed dependent and independent analyses. A subscript records the lexical subclass; the whole expression remains an NP in each case.}\label{fig:some}
\end{figure}

The first tree also illustrates a cost of making the analysis explicit. Relabelling the inner phrase NP doesn't make it interchangeable with every other NP. A plain common-noun NP can't replace \mention{some} in that use merely because both now bear the label NP. The Det construction must still select a determinative-headed phrase, a suitable genitive NP, or another licensed expression. Section~\ref{sec:economy} includes this restriction in the comparison of economies.

The second tree is the proposed replacement for simple determinative fusion. It's a hypothesis about internal structure, supported by the distributional comparison that follows. The fact that \mention{some} can occupy an argument position doesn't itself prove this tree: fusion and silent-structure analyses can also generate such expressions. The useful question is whether the extra structural relation contributes a generalization that the nominal analysis loses.

\subsection{Two heads in one expression}

In \mention{almost every experienced teacher}, the two modifier relations belong to different constituents. Figure~\ref{fig:every} makes them visible. The AdvP \mention{almost} modifies the determinative noun \mention{every}; the AdjP \mention{experienced} modifies the common noun \mention{teacher}. The outer NP is ultimately headed by \mention{teacher}. Calling \mention{every} a noun therefore doesn't collapse the two heads or give their modifiers the same distribution.

\begin{figure}[tb]
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
\caption{The two modifier relations in \mention{almost every experienced teacher}. Internal structure within the one-word modifier phrases is suppressed.}\label{fig:every}
\end{figure}

This analysis preserves the contrast emphasized by \textcite[13--14]{payne2010}: \mention{hardly any} and \mention{almost anybody} have adverbial modifiers, while expressions such as \mention{nothing absolute} permit adjectival postmodification. A supercategory containing determinatives must make room for those patterns alongside the common-noun pattern. It can't simply restate all existing rules referring to noun with the broader extension and assume that no consequences follow.

Genitive determiners provide a comparison within the existing noun category. In \mention{Kim's book}, the genitive NP functions as Det, while the common noun \mention{book} supplies the ultimate head of the larger NP (Figure~\ref{fig:genitive}). CGEL already permits an NP headed by a noun to serve this dependent function. The determinative proposal extends that possibility to another subclass; it doesn't infer nounhood from determiner function alone.

\begin{figure}[tb]
\centering
\begin{forest} nominal tree
[NP
 [{\synnode{Det}{NP[gen]}}
  [{\synnode{Head}{Nom}}
   [{\synnode{Head}{N\textsubscript{proper}}} [\mention{Kim's}]]]]
 [{\synnode{Head}{Nom}}
  [{\synnode{Head}{N\textsubscript{common}}} [\mention{book}]]]]
\end{forest}
\caption{A genitive NP functioning as determiner. The representation abstracts from the internal realization of genitive marking.}\label{fig:genitive}
\end{figure}

Independent genitives need care. CGEL analyses \mention{mine} as fused Det--Head when it stands for a possessed entity in an anaphoric context, but as pure Head in the predicative possessive use \mention{it's mine} \citep[410--411]{huddleston2002}. Nounhood is compatible with fusion, but this doesn't make every independent genitive an example of ordinary headedness. The relevant lesson is the compatibility of category and constructional analyses, not a uniform structural template for all uses of \mention{mine}.

\section{Evidence for nominal structure}\label{sec:evidence}

\subsection{The range of independent uses}

Independent use is widespread within the determinative inventory. CGEL discusses such uses for demonstratives and quantifiers including \mention{some}, \mention{all}, \mention{both}, \mention{many}, \mention{few}, \mention{several}, \mention{each}, \mention{either}, \mention{neither}, \mention{much} and \mention{enough}, while recording lexical restrictions and the separate forms \mention{no}/\mention{none} \citep[371--372, 410--424]{huddleston2002}. The generalization is about the availability of constructions across a lexical category, not the unrestricted acceptability of every member in every sentence frame.

The motivating comparison is with the other noun subclasses. In the constructed examples in (\ref{ex:external}), each bracketed expression can be the subject, object or complement of a preposition. The determinative's distribution is therefore compatible with the external distribution of an NP. The remaining question concerns its internal analysis: whether the overt determinative heads that NP through ordinary nominal projection, or enters a special construction that supplies the nominal distribution.

\ea\label{ex:external}
\ea \mention{[People] left.}\qquad \mention{I see [people].}\qquad \mention{with [people]}
\ex \mention{[Kim] left.}\qquad \mention{I see [Kim].}\qquad \mention{with [Kim]}
\ex \mention{[She] left.}\qquad \mention{I see [her].}\qquad \mention{with [her]}
\ex \mention{[Some] left.}\qquad \mention{I see [some].}\qquad \mention{with [some]}
\z\z

The breadth of the determinative pattern gives a reason to consider a shared nominal analysis. It isn't confined to a few compounds or a single lexicalized expression. At the same time, \term{productivity} needs a restricted interpretation here. A closed class doesn't support the same inference about new lexical items as an open class. The relevant descriptive question is how broadly independent use is available among the established members, under their appropriate semantic and constructional conditions.

Adjectival independent uses prevent a simple inference from external distribution to nounhood. \mention{The rich} and \mention{the poor} can fill nominal argument positions, and the comparative and superlative patterns extend beyond this human-class interpretation. CGEL's \mention{the most important of her criticisms}, for example, provides both a nominal argument and a partitive domain \citep[332--333, 416--423]{huddleston2002}. A generalization about independent determinatives must therefore do more than show that some expression containing them can be an NP.

The contrast with adjectives is useful when kept local. Bare \mention{some} can constitute an NP in its licensed uses, whereas the human-class reading of \mention{rich} normally requires a determiner, as in \mention{the rich}. This supports different structural and lexical descriptions for the two patterns. It doesn't establish a universal test according to which every word that can occur alone is a noun, or every expression requiring a determiner has a non-nominal head. Singular count common nouns alone disprove the latter test.

\subsection{Completeness and contextual interpretation}

The expressions \mention{Some left}, \mention{Many came} and \mention{All agree} illustrate \term{structural saturation}: an argument expression can be syntactically complete without another overt head or determiner. This is an observation about the visible construction. The proposed ordinary-Head analysis gives it a direct representation. A fusion analysis gives another, in which one expression jointly performs the two functions.

Syntactic completeness must be distinguished from contextual interpretation. In \mention{I'll take some}, the relevant substance or set may be supplied by preceding discourse or the situation. That dependence doesn't establish a deleted common noun: ordinary pronouns also depend on context. Conversely, the absence of an overt antecedent doesn't establish the absence of silent nominal structure. A theory may permit a contextually supplied restriction without requiring a previously uttered noun.

Generalizing expressions such as \mention{Many are called, few are chosen} and \mention{Enough is enough} show why a mandatory overt-antecedent account would be too narrow. Their interpretation doesn't require a particular common-noun phrase to have been uttered first. They don't, however, discriminate against every silent-noun account. A generic restriction or an understood quantity can be represented either semantically or in syntax, depending on the theory. The examples establish the interpretive task, not a unique representation of it.

The criterion for comparing the alternatives is explanatory work. A silent noun is useful if its independent properties predict a restriction that the overt-head account otherwise misses. Fusion is useful if the joint functions predict the available dependents or interpretations. Ordinary nominal projection is useful if it captures the independent pattern with restrictions already needed for the lexemes. The relevant cost is the whole analysis, including its licensing conditions; counting visible nodes alone is inadequate.

\subsection{Partitives locate the quantificational head}

In \mention{some of the wine}, \mention{some} supplies the quantity and the \mention{of}-phrase supplies its domain. The common noun \mention{wine} is internal to that domain. The same construction permits a pronominal or genitive domain, as in \mention{many of them} and \mention{some of Kim's}. Thus a following overt common noun isn't the lexical head of the matrix expression. The grammar must assign the determinative an organizing role in the partitive itself.

Figure~\ref{fig:partitive} gives the proposed nominal analysis. The partitive phrase modifies the head nominal, following CGEL's description of the \mention{of}-phrase as a post-head modifier \citep[411]{huddleston2002}. This function label doesn't remove the lexical restrictions on which heads admit a partitive domain. Those restrictions are part of the construction under either analysis. The inner NP \mention{the wine} is abbreviated so that the relation at issue remains visible.

\begin{figure}[tb]
\centering
\begin{forest} nominal tree
[NP
 [{\synnode{Head}{Nom}}
  [{\synnode{Head}{N\textsubscript{D}}} [\mention{some}]]
  [{\synnode{Mod}{PP}}
   [{\synnode{Head}{P}} [\mention{of}]]
   [{\synnode{Comp}{NP}} [\mention{the wine}, roof]]]]]
\end{forest}
\caption{The proposed structure of \mention{some of the wine}. The domain NP doesn't supply the matrix lexical head.}\label{fig:partitive}
\end{figure}

CGEL already accounts for these facts through Det--Head fusion. Partitives therefore support the determinative's head-like role while leaving the choice between fusion and ordinary nominal headedness open. The adjectival example \mention{the most important of her criticisms} also shows that a partitive domain doesn't by itself determine the head word's lexical category. The positive case is cumulative: partitives connect the quantificational item to a nominal distribution whose other uses require explanation too.

The ordinary-Head proposal can treat simple independent and partitive uses as extensions of the same nominal projection, with the domain phrase present in the latter. It need not deny fusion wherever a more complex construction independently calls for it. The claim is that the basic determinative use doesn't require a special fused relation merely to make an otherwise non-nominal lexical head available in an NP. Whether this removes a real complication depends on the modifier restrictions considered next.

\subsection{Modification tests the internal analysis}

The pair \mention{the lucky survivors}/\mention{the lucky few} makes the case for ordinary nominal structure particularly visible. In the proposed analysis of the second expression, \mention{the} determines a Nom containing the modifier \mention{lucky} and the head \mention{few} (Figure~\ref{fig:few}). The overt determiner and the overt quantificational head fill separate functions. The modifier precedes the lexical head just as it does in the common-noun example.

\begin{figure}[tb]
\centering
\begin{forest} nominal tree
[NP
 [{\synnode{Det}{NP\textsubscript{D}}} [\mention{the}, roof]]
 [{\synnode{Head}{Nom}}
  [{\synnode{Mod}{AdjP}} [\mention{lucky}]]
  [{\synnode{Head}{N\textsubscript{D}}} [\mention{few}]]]]
\end{forest}
\caption{The proposed structure of \mention{the lucky few}. Internal structure within the article phrase and AdjP is suppressed.}\label{fig:few}
\end{figure}

This is a useful positive analysis, but the word order doesn't prove the attachment it represents. A silent-head account can place \mention{lucky} with a silent nominal element, and a lexical-conversion account can treat this use of \mention{few} as a common noun. The comparison must ask whether those analyses predict the observed restrictions better than a determinative noun with its own modification profile. An overt head is descriptively direct; directness isn't independent evidence against every covert alternative.

The restriction within the determinative category is substantial. The adverbial modification in \mention{hardly any} and \mention{almost every} doesn't license corresponding attributive adjectives, while the nominal pattern in \mention{the lucky few} is unavailable throughout the class. \textcite[13--14]{payne2010} makes continuity of category across functions central to the analysis: the different modifier relations must not force an automatic determinative/pronoun alternation. The fourfold proposal preserves that continuity, but locates the resulting restrictions inside Noun.

This comparison also limits the adjective contrast. \mention{The idle rich} shows that adjectival fused heads can occur with a preceding adjective. Internal adjectival modification is therefore not a categorical discriminator between determinatives and adjectives. Nor does it establish that independent \mention{some} has precisely the internal syntax of \mention{few} in \mention{the lucky few}. Different determinative lexemes license different dependents, and the nominal analysis has to retain that difference.

The three strands of evidence thus have different strengths. Lexical breadth motivates a class-level account of independent use. Syntactic completeness establishes that another overt nominal element isn't required. Modification supplies specific structures and restrictions for the analysis to capture. Together they support a nominal treatment as a serious alternative to a separate D category. They don't yield a mechanical membership test, and none selects coordination over nesting within Noun by itself.

\section{What the empirical record establishes}\label{sec:empirical}

\subsection{A reproducible corpus inventory}

CGELBank provides annotated English sentences in a framework closely related to the grammar being reconsidered \citep{reynolds2023unified}. Its value here is that constructions can be located and inspected with stable sentence identifiers. Its limitation is equally relevant: the category and fusion labels already encode analytical decisions. Counting those labels can't independently establish that the decisions are correct, or that the fourfold replacement is preferable.

The inventory uses the four top-level gold datasets in the public repository at commit \texttt{d0a2c2d8c522}. Trial material, one-off examples and duplicate versions from the annotation study are excluded. The resulting denominator is 220 trees containing 3,390 lexical nodes with overt text. Of those nodes, 387 are annotated D. Multiword lexical nodes count once, and overt source errors remain in the inventory, with the corpus's correction information retained.
% Sources: analysis/results/corpus-manifest.json and corpus-denominators.csv.

For each D node, the extraction follows Head relations upwards to the first non-Head relation. This identifies the local function of its projection, rather than assigning it the function of an arbitrarily distant containing NP. The resulting functions are Det (297), Mod (18), Det--Head (65), Marker (1), Flat (4) and Coordinate (2). The full concordance retains the local phrase, the nearest NP and its function, and the source sentence.

Table~\ref{tab:corpus} displays selected forms from the motivating contrasts. The complete inventory is supplied with the analysis. These are frequencies of annotated uses in the selected material, not estimates of the probability that a lexeme can occur independently. In particular, the sample has no D-token occurrence of bare \mention{few}, \mention{either} or \mention{neither}. Their absence limits what this sample can say about the lexical breadth discussed in §\ref{sec:evidence}.

\begin{table}[tb]
\centering\small
\caption{Selected forms in the CGELBank inventory. Other includes every local function except Det and Det--Head. Counts follow corpus lemmas, including the normalization of demonstrative number forms.}\label{tab:corpus}
\begin{tabular}{lrrrr}
\toprule
Form & Total & Det & Det--Head & Other \\
\midrule
\mention{the} & 129 & 129 & 0 & 0 \\
\mention{a} & 90 & 89 & 0 & 1 \\
\mention{every} & 3 & 3 & 0 & 0 \\
\mention{this} & 28 & 21 & 7 & 0 \\
\mention{that} & 12 & 5 & 7 & 0 \\
\mention{some} & 5 & 3 & 2 & 0 \\
\mention{all} & 11 & 3 & 5 & 3 \\
\mention{both} & 4 & 2 & 1 & 1 \\
\mention{many} & 3 & 0 & 1 & 2 \\
\mention{a few} & 2 & 1 & 1 & 0 \\
\mention{each} & 2 & 0 & 1 & 1 \\
\mention{enough} & 6 & 2 & 1 & 3 \\

\bottomrule
\end{tabular}
\end{table}

All 65 Det--Head contexts were inspected in the retained sentence context. They include ordinary arguments, partitives, compounds such as \mention{something}, floating quantifiers, degree and frequency expressions, numerical fragments and age supplements. The numeral inside \mention{about 30 seconds} is also represented through a nominal projection embedded within the larger determiner. Reporting all 65 as independent argument uses would therefore conflate different constructions.

Two attestations illustrate independent quantifiers with a recoverable domain:
\ea\label{ex:attested-quantifiers}
\ea \mention{Went there yesterday: we are trying to decide between two different Honda models, so we wanted to test-drive both back to back.}
\ex \mention{I rarely listen to the news or to what politicians or lawyers say because so many tell lies that none have credibility so what's the point?}
\z\z
The first occurs in CGELBank's EWT sentence \texttt{reviews-083459-0002}; the second has the source identifier ending \texttt{ENG\_20050906\_165900-0074}. Full identifiers are in the concordance. In (a), \mention{both} has an explicit antecedent in the retained text. In (b), \mention{politicians or lawyers} supplies an available restriction for \mention{many} and \mention{none}. These examples attest independent uses but don't test an antecedent-free analysis.

The corpus also contains \mention{I need something reliable and good looking} (\texttt{answers-20111024111513AAAQhAO\_ans-0003}). This is an attestation of adjectival postmodification of a compound determinative. It isn't evidence for the specific premodification pattern in \mention{the lucky few}. Keeping that difference visible prevents a related attestation from being counted as confirmation of the disputed construction.

The inventory thus supports a limited conclusion: independent and internally expanded determinative expressions occur in traceable, naturally occurring sentences. It doesn't supply a representative estimate of their productivity, a controlled comparison of generic interpretations, or a corpus test of every modifier contrast. The constructed comparisons in §\ref{sec:evidence} retain their status as grammatical judgments. A broader corpus or judgment study would have to target those contrasts directly.

\subsection{Reproducing the determinative--pronoun matrix}

\textcite{reynolds2021} compared 73 determinative forms and 65 pronoun forms using binary features drawn from descriptions of their morphology, phonology, semantics and syntax. Each row represents a word form; each column records whether a feature applies. The analysis therefore compares coded linguistic profiles. It doesn't compare token frequencies in a corpus, and the rows aren't a random sample of independent speakers or lexical innovations.

The article and the LingBuzz description report 232 features, but the public downloadable file contains 155 \citep{reynolds2021matrix}. The new audit preserves that file with its checksum and compares it with a recovered local 232-feature working matrix. The latter isn't authenticated as the input to the published analysis. The public 155-feature file reproduces the published DISCO decomposition: between-group component 30.58286, within-group component 356.41607 and total 386.99893, giving $F=11.670$ to the reported precision.
% Source: analysis/results/disco-sensitivity.csv, public155; published Table 3.

DISCO is a distance-based comparison of the supplied groups. Here the reference partition is CGEL's determinative/pronoun classification. A new run with 999 permutations and seed 20260907 gives $p=.001$. This result concerns the association between the coded profiles and the supplied partition. It doesn't say whether either group is a primary category, whether one belongs inside a broader class with the same name, or whether both belong within Noun. There are no common or proper nouns in the matrix.

The clustering question is different. The original k-groups analysis asks for two clusters without supplying the category labels during fitting, then compares the result with the reference partition. It reported agreement for 129 of 138 forms. The published code records a single random start and no seed. It also drops the first feature once more in the clustering step after the name column has been removed. The audit therefore runs both the public 155-feature input and that 154-feature implementation.

For each representation, the audit runs 100 separate single-start fits with seeds 1--100 and the published limit of ten iterations. It then runs a separate fit with 100 starts and a limit of 100 iterations, selecting the best objective among those starts. Table~\ref{tab:matrix} reports the main comparisons. Cluster labels are oriented after fitting to maximize agreement with the reference partition; that comparison is descriptive agreement, not accuracy against an independently established ground truth.

\begin{table}[tb]
\centering\small
\caption{Exploratory sensitivity of the matrix analysis. The range is agreement out of 138 across 100 single-start fits. The last column is agreement for the best-objective fit among a separate set of 100 starts, not the maximum agreement observed. All displayed DISCO runs give $p=.001$ with 999 permutations.}\label{tab:matrix}
\begin{tabular}{p{5.1cm}rrrr}
\toprule
Representation & Features & DISCO $F$ & Range & Best objective \\
\midrule
Public matrix & 155 & 11.670 & 75--132 & 125/138 \\
Without word-component columns & 105 & 12.654 & 75--131 & 131/138 \\
Syntactic columns & 50 & 9.682 & 69--133 & 120/138 \\
Syntactic, four labels removed & 46 & 7.192 & 69--117 & 97/138 \\

\bottomrule
\end{tabular}
\end{table}

The public-matrix single-start fits range from 75 to 132 matches; eight reproduce the reported count of 129. The 100-start fit yields 125 matches. The 154-feature implementation likewise varies across starts. These results don't show that the published partition is impossible or that k-groups can't recover a close correspondence. They show why one percentage from an unseeded run can't bear the argument for a particular taxonomy.
% Source: analysis/results/kgroups-summary.csv and kgroups-single-starts.csv.

Feature choice also matters. Removing the first 50 columns, which encode word components, changes the best-objective agreement to 131/138. Restricting the analysis to the 50 syntactic columns yields 120/138; removing four explicit analysis labels from that subset yields 97/138. The labels concern fused determiner-head function, partitive head function, subject-determiner function and coordination with non-fused determiners. Removing them is only a limited sensitivity check: the remaining judgments are still informed by the descriptive framework.

The DISCO separation persists in these representations, while the clustering correspondence changes. The distinction matters for taxonomy: the supplied classes differ in their coded distributions, but the exact partition recovered by clustering depends on the representation and fitting procedure. Reynolds's original discussion already recognized that significant within-category divisions prevent DISCO from serving as a simple category-status test, and explicitly left a nested nominal analysis open \citep{reynolds2021}.

These analyses are exploratory audits, not a preregistered model comparison. The scripts, feature changes, seed schedule and complete outputs are supplied so that each claim can be checked. A taxonomic comparison requires a proposed hierarchy and the properties it organizes; statistical separation between two selected lists is evidence to bring to that comparison, not an answer that can replace it.

\section{Coordinate subclasses and inheritance}\label{sec:inheritance}

The quantitative result supports keeping track of determinative/pronoun differences. It doesn't establish that the two classes must be coordinate. Suppose, for illustration, that a taxonomy places the two disjoint sets of matrix rows inside one broader class. Their distributions can differ sharply within that class. A test separating the two sets would then recover a distinction internal to the superclass. It would not show that the superclass is incoherent.

This matters particularly for the comparison with Hudson. \mention{Pronoun} has a broader extension in his analysis than in CGEL's matrix labels. Testing the CGEL determinative rows against the CGEL pronoun rows is therefore not a direct test of Hudson's broader category. Moreover, his determiner terminology and the CGEL determinative inventory don't identify the same domain. A comparison of hierarchies must first align the relevant items and uses, then compare the generalizations that their groupings support.

The case for coordination starts from a different consideration: the two subclasses organize different concentrations of grammatical properties. Core personal pronouns have case contrasts, reflexive forms and person distinctions. Determinatives organize contrasts in quantification, determination and degree modification. Neither description is exhaustive or exceptionless, and the pronoun class itself has several subtypes. The proposal retains these useful distinctions rather than treating independent use as a reason to assign an item to a different lexical category.

Placing both subclasses immediately under Noun locates their shared nominal projection at the broadest relevant level. Common and proper nouns also participate in that projection. The nominal generalization therefore doesn't distinguish a putative pronoun-plus-determinative superclass from Noun as a whole. An intermediate superclass would need to organize something further: for example, a pattern of interpretation or internal syntax shared by its members and not already captured by the broader nominal rules.

A broad pronoun analysis has a reasonable candidate in the reduced descriptive content and contextual interpretation of many of these expressions. The fourfold proposal can recognize the same commonalities through features or further cross-classification. It can't claim that the possibility of such a representation makes the intermediate class unnecessary in every grammar. If a pronoun superclass collects several otherwise repeated generalizations, it may be economical. If it merely restates their nominal status, direct inheritance from Noun suffices.

The empirical comparison therefore concerns the placement of properties, not the visual shape of a taxonomy. Under either hierarchy, the restrictions on \mention{almost every}, \mention{the lucky few} and independent \mention{some} must be stated. A nested account can assign those restrictions to subtypes or valency patterns inside pronoun. A coordinate account can assign them to determinatives alongside the pronoun-specific restrictions. Where the resulting grammars license the same expressions with equivalent conditions, the available examples don't decide between them.

The coordinate proposal has a particular advantage as a revision of CGEL: it retains a well-developed local distinction while extending the shared nominal analysis. No word must change between determinative and pronoun simply because it occurs independently. Nor must the broad determinative inventory first be repartitioned into narrower classes. These are commitments of the proposal, not proof that its hierarchy is the only one compatible with the data. The preservation of an existing classification is an economy relative to that descriptive starting point.

An intermediate category would be favoured if it enabled additional shared restrictions to be inherited with fewer exceptions than the coordinate analysis. Coordination would be favoured if the proposed intermediate properties repeatedly required separate statements for its constituent groups, while the shared properties belonged at Noun anyway. Establishing either result requires a matched fragment of the competing grammars. The present matrix provides evidence about differences between lexical profiles, but doesn't perform that comparison of inherited constraints.

The fourfold analysis can thus be preferred without treating distributional separation as a refutation of nesting. It keeps the determinative category intact, gives its nominal uses the same basic projection as other nouns, and leaves its distinctive licensing conditions at the subclass and lexeme levels. Its strongest present claim is a coherent and descriptively motivated organization of the facts. A claim of unique empirical superiority over Hudson's hierarchy would require evidence beyond that supplied here.

\section{The articles and other restricted members}\label{sec:articles}

The articles \mention{the} and \mention{a} are the hardest cases for a nominal analysis of the entire determinative category. They lack the ordinary independent uses that motivate the analysis of \mention{some}, \mention{this} and \mention{many}. \mention{Every} is restricted too, while \mention{no} has the distinct independent form \mention{none} \citep[371--372, 410--411]{huddleston2002}. An argument based only on independent distribution would support a narrower claim than the inclusion of all determinatives within Noun.

The proposal treats these restrictions as lexical gaps inside the determinative subclass. This is justified only if there's an independently motivated class for the restricted members to belong to. The articles participate in the contrasts that organize determination: they combine with common-noun nominals, contribute definiteness or indefiniteness, and have specific compatibility conditions involving count status and number. Their position within this system connects them to the determinatives that also permit independent uses.

Those connections establish a case for retaining the articles within the determinative category; they don't independently establish that the whole class is nominal. The supercategory decision depends on the analysis of the wider class and on the cost of allowing restricted members. This distinction prevents the argument from becoming circular: the articles can't be called nouns simply because the proposed noun subclass has been defined to include them.

The allowance for restricted members is nevertheless compatible with the existing nominal system. A dependent genitive pronoun such as \mention{my} is nominal in CGEL's analysis even though it doesn't have the independent distribution of \mention{mine} \citep[470--471]{huddleston2002}. Likewise, the common-noun projection has conditions on bare singular count arguments. Membership in Noun therefore doesn't entail an unrestricted one-word NP. The question is whether the article restrictions are reasonably localized within the proposed subclass.

Under the fourfold account, a determiner use of \mention{the} contains an NP\textsubscript{D}, but that phrase isn't thereby licensed as a free-standing argument. Its lexical entry restricts the available uses. The description must distinguish nominal category from independent distribution, just as it must do for other restricted nominal forms. This makes the proposal explicit and prevents the broad label NP from silently licensing expressions that English doesn't permit.

\mention{Every} illustrates the value of distinguishing shared restrictions from complete class identity. It patterns with the articles in lacking independent use, but with quantificational determinatives in expressions such as \mention{almost every} and \mention{nearly every}. A classification should retain both facts. The fourfold proposal keeps \mention{every} within the determinative subclass with a restriction on independent projection; an alternative may give the restriction more classificatory weight. The absence of one construction doesn't decide that comparison by itself.

Diachronic accounts of article development can explain why forms become more specialized, but they can't settle the synchronic category decision. Descent from a demonstrative or numeral doesn't guarantee that a modern article retains the ancestor's category. The nominal analysis therefore rests on present grammatical relations and a comparison of descriptions. Its treatment of the articles would be weakened if a separate article class captured a substantial set of otherwise exceptional restrictions more effectively.

The choice is consequently between an inclusive class with local restrictions and a partition that gives those restrictions greater taxonomic prominence. Keeping the articles in the established determinative category minimizes repartitioning; including that class in Noun shares the nominal architecture available to its less restricted members. This is the argument for the proposed placement. The articles remain its most demanding test, rather than becoming positive evidence merely by being called defective.

\section{What the analysis simplifies}\label{sec:economy}

\subsection{Count the restrictions as well as the labels}

A smaller inventory of primary categories can be a useful economy, but it isn't automatically a smaller grammar. The fourfold analysis removes determinative as a primary category outside Noun. It retains the determinative subclass and the distinctions needed to identify its members. Its descriptive cost must therefore include the subclass restrictions as well as the common nominal rules. Table~\ref{tab:economy} records the main changes and the work that remains.

\begin{table}[tb]
\centering\small
\caption{The proposed economies and their limits. The comparison concerns the described fragment, not a measured minimum description length for a complete grammar.}\label{tab:economy}
\begin{tabular}{p{2.5cm}p{4.5cm}p{4.9cm}}
\toprule
Component & Change & Retained cost \\
\midrule
Primary taxonomy & D becomes a subclass of Noun & The determinative/pronoun distinction and membership criteria remain. \\
Nominal projection & Independent determinatives use the general nominal projection & Lexical restrictions on independent use and dependents remain. \\
Determiner realization & DP\textsubscript{CGEL} and genitive NP share the broad label NP & The construction still distinguishes determinative-headed NPs, genitive NPs and other licensed phrases. \\
Fusion & Simple independent D uses need not invoke fusion & Fusion remains available elsewhere, including adjectival and genitive constructions. \\
Modifier rules & Contrasts are stated for the relevant noun subclasses and constructions & AdvP/AdjP asymmetries can't be generalized away. \\
\bottomrule
\end{tabular}
\end{table}

The determiner function shows why this accounting matters. In CGEL, its realizations include a determinative phrase, a genitive NP and certain other phrase types. Under the proposal, the first two are both NPs. Yet the broader category label can't replace the selectional conditions. The relevant portion of the alternatives is still a determinative-headed NP or a suitable genitive NP. A phrase-type distinction has moved into the features of a shared category; it hasn't disappeared from the grammar.

The same point applies to familiar facts about determination. The restriction on combining two determiners in the same NP is a functional restriction under either analysis. It doesn't become explained for the first time when determinatives are called nouns. Nor does the definiteness of \mention{the book} and \mention{Kim's book} independently require their determiners to have the same primary category. Those parallels are compatible with the nominal proposal, but must not be counted as additional consequences unique to it.

The more substantive economy concerns the relation between dependent and independent uses. The ordinary nominal projection is already required for common nouns, proper nouns and pronouns. Extending it to determinatives allows their independent uses to share that structure while retaining the lexical distinctions governing their dependents. The alternative employs the projection of D and a fused function to connect it to NP distribution. The proposal reduces the occasions on which that special relation must be invoked.

This doesn't eliminate the fusion apparatus from the grammar. Its availability elsewhere means there's no gain equivalent to removing an entire independent mechanism. The gain is narrower: ordinary determinative argument uses can be described through a nominal projection already needed for the other subclasses. Against that gain must be placed any restrictions that the fusion account captures directly and the nominal account has to restate. Modifier selection is one such area of comparison.

The balance is therefore most favourable when the nominal account reuses restrictions already needed for dependent determinatives. For example, the lexical and constructional differences between \mention{some}, \mention{every} and \mention{few} can't be omitted from either grammar. If those differences also specify the possible independent forms and dependents, ordinary nominal projection avoids duplicating the structural analysis. If fusion predicts additional restrictions without corresponding stipulations, that advantage counts on the other side.

\subsection{A precedent and its limits}

The familiar inclusion of auxiliaries within Verb shows that a closed class with distinctive syntax can belong inside a broader lexical category. \textcite{pullumwilson1977} argues for that analysis, which CGEL adopts. The precedent licenses consideration of the same kind of classificatory move for determinatives; it doesn't establish the result by analogy. Each case requires evidence that the shared category captures grammatical relations while the subclass preserves its distinctive restrictions.

The present move is also compatible with the category/function discipline defended by \textcite{payne2010,pullummiller2022nps}. A word isn't reassigned to pronoun merely because its containing phrase has a nominal external function. Instead, the determinative category receives a supercategory analysis across its uses. The word \mention{some} has the same lexical classification in \mention{some apples} and independent \mention{some}; the different constructions explain its different functions.

The price is that rules stated for noun in the narrower taxonomy must be reviewed. A rule describing ordinary attributive adjective modification can't simply inherit the broader extension of Noun. Some existing noun generalizations must be stated for common nouns, for specified constructions or for more specific lexical profiles. This is a real consequence of the proposal. A responsible comparison counts such revisions rather than treating every unchanged English judgment as evidence of a cost-free merger.

Numerals place a further limit on the scope of the argument. Their quantifying, naming and counting uses require distinctions at the lexicon--syntax boundary \citep{reynolds2026numerals}. The proposed analysis accommodates the nominal structure of ordinary cardinal uses included in the determinative category. It doesn't establish that every numeral construction has the same lexical analysis, or settle the full internal taxonomy of numeral expressions. Those questions should be assessed from their own distributional evidence.

The proposal is thus a substantive grammatical representation with a bounded comparative claim. It unifies nominal projection and reduces determinative-specific structural applications while preserving the lexical category. It doesn't yet establish a lower overall description length, a learning advantage or a processing advantage over every alternative. Such results would require matched formal grammars or independent empirical tests. They can't be inferred from the smaller number of primary category names.

\subsection{Consequences for further comparison}

A useful next comparison would encode the same finite set of constructions under the coordinate and nested analyses. Each account would have to state the lexical memberships, permitted dependents, independent-use restrictions and inheritance relations. The descriptions could then be checked against further contexts that weren't used to formulate them. This would make the contribution of an intermediate pronoun category assessable without assuming that a visually flatter hierarchy is better.

A broader corpus study would serve a different purpose. It could establish how widely particular modifier and independent-use patterns occur, with denominators appropriate to the lexical items and constructions. A judgment study could target the contrasts that sparse corpora leave unresolved. The present inventory does neither of those jobs in full. Its role is to provide checkable instances, prevent overstatement of the available evidence and specify what a stronger comparison would need to cover.

These limits don't remove the reason to reconsider the separate primary D category. The evidence shows a substantial nominal distribution, continuity of lexical identity across uses, and a pattern of local restrictions compatible with subclassification. The fourfold analysis brings those facts into the same nominal architecture while keeping the determinative category visible. The remaining question is how much additional economy that representation achieves when compared with fully specified alternatives.

\section{Conclusion}\label{sec:conclusion}

The fourfold analysis treats English determinatives as nouns while preserving the contrasts that motivate the determinative category. It gives independent determinatives ordinary nominal projection, retains their lexical identity in dependent uses, and locates differences in modification and independent distribution at the subclass, lexeme and construction levels. The worked analyses make clear why \mention{almost every experienced teacher} can contain two nominal heads without changing which one heads the larger NP.

The empirical record supports parts of this account with different strengths. Independent uses and partitives motivate a nominal treatment; modifier contrasts constrain its implementation. The public feature matrix reproduces the earlier distributional separation, but its clustering results don't identify a unique taxonomy. CGELBank supplies traceable attestations and a reproducible inventory, while leaving several central contrasts without adequate corpus coverage. These findings justify neither a universal membership test nor the inference that statistical distinctness excludes nesting.

Hudson's analysis already places determiners within Noun. The coordinate proposal differs in retaining the broader determinative category alongside pronoun and giving it direct access to the shared nominal structure. Its economy is clearest relative to the existing CGEL description: a primary-category boundary and some determinative-specific structural applications are removed, while local licensing distinctions remain. Whether this is superior to a fully specified nested nominal analysis remains a separate comparative question.

The paper therefore advocates determinatives as a fourth noun subclass without making nounhood and hierarchy stand or fall together. The nominal proposal is supported by a coherent treatment of the constructions and an explicit account of its restrictions. The stronger claim that coordination is the uniquely correct organization of the nominal domain awaits evidence that distinguishes the competing inheritance structures.

\section*{Data and analysis materials}

The accompanying \texttt{analysis/} directory contains the public feature matrix, its provenance record, reproduction and sensitivity scripts, generated tables, and the CGELBank concordance. The corpus inventory records the full source commit and file checksums. Analyses were run with R 4.6.1 and \texttt{energy} 1.7-12; further environment details and the seed schedule are recorded with the outputs. These are exploratory analyses. The materials don't constitute an independent judgment study or a preregistered test of the proposed taxonomy.

\section*{Acknowledgements}

Language models assisted with drafting, source retrieval and the development of the analysis scripts. This version is a working draft for author review.

\clearpage
\printbibliography
\end{document}
