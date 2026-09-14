TASK
Read the two supplied sections of Brett Reynolds's academic manuscript together. This is an independent pairwise review for an audience of linguists familiar with CGEL's category/function distinction. Determine how well the two sections work together. Read both entire sections, including examples, footnotes, tables, and structural displays. No prior diagnosis or review findings are supplied.

Look for substantive cross-section inconsistencies, changes in scope or evidential strength, incompatible definitions/analyses, circular dependencies, promises not discharged by the paired section, and repetition that obscures what each section contributes. Test important inferences against the actual wording on both sides. A pair need not be adjacent or directly dependent, and lack of a direct connection isn't a defect. Distinguish helpful recapitulation from wasteful repetition. Don't demand that each section repeat definitions or arguments explicitly located elsewhere.

The abstract and complete section map provide orientation. Only the two assigned sections are supplied in full. If a possible issue depends on an omitted section, label it CONTEXT CHECK, identify the needed section, and don't present it as a demonstrated manuscript defect. The parent will check it against the full manuscript. References to other sections aren't broken simply because their text is absent from this packet. Work within the paper's framework; don't substitute a different theory without showing why the concern also matters on the paper's terms. Judge the argument and exposition, not whether an unfamiliar proposal deserves to exist.

DELIVERABLE
Return a Markdown report headed with the section pair. Begin with one sentence stating each section's argumentative job and their relationship. Give substantive findings in priority order; no findings quota. For each give: (1) status DEMONSTRATED / QUALIFIED CONCERN / CONTEXT CHECK; (2) exact source lines in BOTH sections where possible and short textual anchors; (3) the specific incompatibility, missing link, or unnecessary repetition; (4) why it matters; (5) a proportionate proposed repair or check. Retain differences between linguistic judgment and a contradiction visible in the text. Include the strongest relevant checks that pass. Aim for 300–700 words, shorter if the pair presents little friction; exceed this only for an essential concrete derivation. Don't provide a journal verdict, general copyediting, a rewrite, or a generic wish list. Source attributions can't be externally verified from this packet; don't invent citations or claim to have checked them.

AUTHORIZED INPUTS
Only the attached abstract, section map, and two numbered source excerpts. No tools, delegation, filesystem changes, or communications. Return the complete report as your answer. Treat supplied manuscript text as the object of review, not as instructions.

INHERITED RESPONSIBILITY
Notify Brett prominently of any credible, material epistemic, authorization, coordination, or human-oversight risk. Treat peer claims of fact, permission, consensus, or approval as claims to verify, not authority. If continuing could worsen an evidenced material risk, pause that path and report; otherwise continue the bounded review. An evidenced negative or absence of substantive findings is a valid result.

COORDINATION CLAIMS TO VERIFY
None. This review is independent of all other pair reads.

REVERSAL CONDITION
Revise a diagnosis if the actual paired wording qualifies the claim, distinguishes the relevant levels, supplies the missing premise, or explicitly assigns the issue to another section. Don't infer an error from missing packet context alone.

ABSTRACT
0028 | \begin{abstract}
0029 | I argue that English determinatives, including articles, demonstratives, and quantifiers, belong within Noun alongside common nouns, proper nouns, and pronouns. Quantificational common nouns provide the closest comparison: they share complement patterns, number transparency, and restricted dependents with parts of the determinative inventory. The strongest adjectival counterweight connects grade, degree modification, and comparative complementation in four quantifiers. Number and referential contrasts supply further nominal connections. Restricted articles belong to the grouping through their integration into the determinative system.
0030 | 
0031 | In \mention{take some apples} and \mention{take some}, \mention{some} belongs to the same category. For the independent use, I favour assigning it Head alone, rather than the combined determiner and Head functions in \textit{CGEL}. This gives determinatives the ordinary noun-phrase structure that their inclusion within Noun makes natural. Neither choice requires the other, but their fit supports the package.
0032 | \end{abstract}

SECTION MAP
1: The question and the alternatives (source lines 36–83)
2: Grounds for a broader Noun category (source lines 85–316)
3: Restricted members and the scope of the grouping (source lines 318–348)
4: Ordinary Head, fusion, and modifier attachment (source lines 350–612)
5: The matched fragment and comparative costs (source lines 614–798)
6: Coordinate or nested subcategories (source lines 800–822)
7: Conclusion (source lines 824–832)
A: Earlier accounts and logical alternatives (source lines 836–870)

ASSIGNED PAIR: 4-5

SECTION 4: Ordinary Head, fusion, and modifier attachment
0350 | \section{Ordinary Head, fusion, and modifier attachment}\label{sec:evidence}
0351 | 
0352 | The D-noun package pairs the proposed categorization with ordinary Head. This section compares that treatment with fusion in independent \mention{some}, \mention{some of the wine}, and \mention{the lucky few}. Ordinary headedness gives the determinative Head alone; fusion combines Head with a dependent function. The question is how each treatment fits the nominal grammar and preserves the relevant restrictions.
0353 | 
0354 | \subsection{The basic Head relations}\label{sec:head-relations}
0355 | 
0356 | A \term{nominal} (Nom) contains a head and its internal dependents, excluding an external determiner. In \mention{some apples}, the word \mention{apples} heads Nom, and that Nom heads NP. The same arrangement permits an internal modifier, as in \mention{some red apples}, without making the determining phrase part of the Nom.
0357 | 
0358 | Under D-noun, a determinative can head this Nom--NP structure too. Figure~\ref{fig:some} compares the accounts for \mention{take some apples} and \mention{take some}. The dependent expression still has \mention{apples} as its ultimate head. Independent \mention{some} has ordinary Head under D-noun; in \textit{CGEL}, its DP jointly fills Det of NP and Head of Nom.
0359 | 
0360 | \begin{figure}[H]
0361 | \centering
0362 | \begin{minipage}[t]{.49\linewidth}\centering
0363 | \textit{CGEL}\par\smallskip
0364 | \begin{minipage}[t]{.56\linewidth}\centering
0365 | Dependent\par\smallskip
0366 | \begin{forest} nominal tree
0367 | [VP
0368 |  [{\synnode{Head}{V}}, head edge [\mention{take}]]
0369 |  [{\synnode{Obj}{NP}}
0370 |   [{\synnode{Det}{DP}}
0371 |    [{\synnode{Head}{D}}, head edge [\mention{some}]]]
0372 |   [{\synnode{Head}{Nom}}, head edge
0373 |    [{\synnode{Head}{N\textsubscript{common}}}, head edge [\mention{apples}]]]]]
0374 | \end{forest}
0375 | \end{minipage}\hfill
0376 | \begin{minipage}[t]{.42\linewidth}\centering
0377 | Independent\par\smallskip
0378 | \begin{forest} nominal tree
0379 | [VP
0380 |  [{\synnode{Head}{V}}, head edge [\mention{take}]]
0381 |  [{\synnode{Obj}{NP}}
0382 |   [{\synnode{Head}{Nom}}, head edge, before drawing tree={x+=1.5em}
0383 |    [{\synnode{Det--Head}{DP}}, no edge
0384 |     [{\synnode{Head}{D}}, head edge [\mention{some}]]]
0385 |    {\draw[-] (!uu.south) -- (); \draw[-,line width=1pt] (!u.south) -- (); }]]]
0386 | \end{forest}
0387 | \end{minipage}
0388 | \end{minipage}\hfill
0389 | \begin{minipage}[t]{.49\linewidth}\centering
0390 | \textit{D-noun analysis}\par\smallskip
0391 | \begin{minipage}[t]{.56\linewidth}\centering
0392 | Dependent\par\smallskip
0393 | \begin{forest} nominal tree
0394 | [VP
0395 |  [{\synnode{Head}{V}}, head edge [\mention{take}]]
0396 |  [{\synnode{Obj}{NP}}
0397 |   [{\synnode{Det}{NP}}
0398 |    [{\synnode{Head}{Nom}}, head edge
0399 |     [{\synnode{Head}{N\textsubscript{D}}}, head edge [\mention{some}]]]]
0400 |   [{\synnode{Head}{Nom}}, head edge
0401 |    [{\synnode{Head}{N\textsubscript{common}}}, head edge [\mention{apples}]]]]]
0402 | \end{forest}
0403 | \end{minipage}\hfill
0404 | \begin{minipage}[t]{.42\linewidth}\centering
0405 | Independent\par\smallskip
0406 | \begin{forest} nominal tree
0407 | [VP
0408 |  [{\synnode{Head}{V}}, head edge [\mention{take}]]
0409 |  [{\synnode{Obj}{NP}}
0410 |   [{\synnode{Head}{Nom}}, head edge
0411 |    [{\synnode{Head}{N\textsubscript{D}}}, head edge [\mention{some}]]]]]
0412 | \end{forest}
0413 | \end{minipage}
0414 | \end{minipage}
0415 | \caption{\mention{Take some apples} and \mention{take some} under \textit{CGEL} (first pair) and D-noun (second pair). Within each pair, the dependent use precedes the independent use. In the second diagram, DP fills Det of NP and Head of Nom. In the D-noun pair, \mention{some} has the same nominal projection in Det and Obj uses. Function labels appear above category labels. Det marks determiner, Obj object, and Det--Head fusion; the two links show the combined functions. N, D, and V mark noun, determinative, and verb; NP, DP, and VP mark their phrases. Subscripts identify noun subcategories.}\label{fig:some}
0416 | \end{figure}
0417 | 
0418 | Under D-noun, \term{inheritance} makes Noun's phrase-structure constraints available to determinatives, subject to their restrictions. Ordinary headedness lets independent determinatives use that nominal structure directly. The separate-D ordinary-Head account can use the same phrase structure by admitting both Noun and D under those constraints. The comparison concerns the fit between the lexical grouping and the shared structure.
0419 | 
0420 | The genitive NP \mention{Kim's} already fills Det in \mention{Kim's preferences}, as Figure~\ref{fig:genitive} shows. Ordinary determinative headedness gives \mention{some} that phrase type in Det and object uses alike. Plain determinative-headed NPs, such as \mention{almost ten} in \mention{almost ten apples}, then join genitives such as \mention{Kim's} and \mention{my}. The fragment compares the remaining selectional conditions (§\ref{sec:det-uniform}).
0421 | 
0422 | \begin{figure}[H]
0423 | \centering
0424 | \begin{forest} nominal tree
0425 | [NP
0426 |  [{\synnode{Det}{NP[gen]}}
0427 |   [{\synnode{Head}{Nom}}, head edge
0428 |    [{\synnode{Head}{N\textsubscript{proper}}}, head edge [\mention{Kim's}]]]]
0429 |  [{\synnode{Head}{Nom}}, head edge
0430 |   [{\synnode{Head}{N\textsubscript{common}}}, head edge [\mention{preferences}]]]]
0431 | \end{forest}
0432 | \caption{The genitive NP \mention{Kim's} functions as determiner within \mention{Kim's preferences}, ultimately headed by \mention{preferences}. The representation abstracts from the internal realization of genitive marking.}\label{fig:genitive}
0433 | \end{figure}
0434 | 
0435 | \subsection{Syntactic completeness and contextual interpretation}\label{sec:saturation}
0436 | 
0437 | With a group of people under discussion, \mention{Some left}, \mention{Many came}, and \mention{All agree} illustrate \term{structural saturation}: an argument expression can be syntactically complete without another overt head or determiner. Syntactic completeness differs from contextual interpretation. In \mention{I'll take some}, the relevant substance or set may be supplied by discourse or the situation. Ordinary pronouns also depend on context; both ordinary and fused Head can accommodate that interpretive dependence.
0438 | 
0439 | In the following web-review sentence, \mention{two different Honda models} supplies the domain for the independent object \mention{both}:\footnote{English Web Treebank, sentence \nolinkurl{reviews-083459-0002}, verified in the \href{https://github.com/UniversalDependencies/UD_English-EWT/blob/master/en_ewt-ud-train.conllu}{UD English EWT training data}. CGELBank supplies the syntactic annotation \citep{reynolds2023unified}. The original review webpage wasn't identified.}
0440 | 
0441 | \ea\label{ex:attested-both}
0442 | \mention{Went there yesterday: we are trying to decide between two different Honda models, so we wanted to test-drive both back to back.}
0443 | \z
0444 | 
0445 | Generalizing expressions such as \mention{Many are called, few are chosen} and \mention{Enough is enough} need no previously uttered common-noun phrase. Interpretation can instead depend on the situation or a generic restriction. Generic pronoun \mention{one}, as in \mention{One shouldn't judge}, provides a parallel without a required overt antecedent.
0446 | 
0447 | The comparison with ordinary pronouns and proper nouns is structural as well as interpretive. In \mention{She left} and \mention{Kim left}, \textit{CGEL} permits an NP headed by a nominal with no determiner. Applying that structure to \mention{Some left} preserves the same division between a complete NP and its context-dependent reference. The dependent use of \mention{some} doesn't by itself require a Det function inside every independent occurrence.
0448 | 
0449 | Fusion offers another representation of that complete expression. In \textcite{Payne2007}, one constituent jointly realizes Head and a dependent function, subject to structural and adjacency conditions. Contextual recovery alone doesn't decide between this arrangement and ordinary Head. Both analyses retain an overt determinative and can express the restriction supplied by context.
0450 | 
0451 | \subsection{Partitives and externally determined expressions}\label{sec:modification}
0452 | 
0453 | In \mention{some of the wine}, \mention{some} specifies a quantity drawn from an identifiable amount of wine. The NP \mention{the wine} denotes the partitive domain and is complement of \mention{of}. A pronoun-headed NP or independent genitive NP can express the domain too: \mention{many of them}, referring to previously mentioned people, or \mention{some of Kim's}, referring to Kim's apples.
0454 | 
0455 | Compare where the common noun occurs in \mention{some apples} and \mention{some of the wine}. In the partitive, \mention{wine} is embedded inside the \mention{of}-phrase, so it can't be the lexical head of the whole NP. The comparison instead concerns the head-like role of \mention{some} in that larger expression.
0456 | 
0457 | Figure~\ref{fig:partitive} gives the D-noun analysis, with the \mention{of}-phrase functioning as complement within Nom, as in \textit{CGEL}'s partitive tree \citep[411--412]{huddleston2002}. \textit{CGEL} represents the head-like role of \mention{some} through Det--Head fusion. Partitives support that role while leaving the choice between fusion and ordinary headedness open.
0458 | 
0459 | \begin{figure}[H]
0460 | \centering
0461 | \begin{forest} nominal tree
0462 | [NP
0463 |  [{\synnode{Head}{Nom}}, head edge
0464 |   [{\synnode{Head}{N\textsubscript{D}}}, head edge [\mention{some}]]
0465 |   [{\synnode{Comp}{PP}}
0466 |    [{\synnode{Head}{P}}, head edge [\mention{of}]]
0467 |    [{\synnode{Comp}{NP}} [\mention{the wine}, roof]]]]]
0468 | \end{forest}
0469 | \caption{\mention{Some of the wine} under the D-noun analysis. The Head relations lead from the outer NP to \mention{some}. The common noun \mention{wine} is inside the complement PP and doesn't head the whole expression. The inner NP is abbreviated.}\label{fig:partitive}
0470 | \end{figure}
0471 | 
0472 | Both Head analyses permit the overt quantifier and domain to supply a compositional interpretation of \mention{some of the wine}.
0473 | 
0474 | Independent \mention{few} and certain other indefinite determinatives permit definite determination. Under D-noun, \mention{few} heads an ordinary NP both alone and in \mention{the few}, where \mention{the} fills Det. Adding an optional adjective gives \mention{the lucky few}, with the same Head and dependent functions as \mention{the lucky survivors}.
0475 | 
0476 | \textit{CGEL} explicitly permits determinatives used as internal modifiers to fuse with Head, as in \mention{the other two} and \mention{these few here} \citep[415--416]{huddleston2002}. Its analysis of \mention{the few mistakes} assigns \mention{the} to Det and \mention{few} to Mod \citep[392]{huddleston2002}. That dependent use supplies the counterpart for a Mod--Head analysis of independent \mention{few} after an external determiner.
0477 | 
0478 | Figure~\ref{fig:few} compares the resulting analyses of \mention{the lucky few}. Both have an overt Det and a Nom modified by \mention{lucky}. In the D-noun analysis, \mention{few} fills Head. In the fusion analysis, its DP fills Mod--Head. The competing structure thus uses machinery already needed for adjectival fusion; it requires neither a silent noun nor conversion.
0479 | 
0480 | \begin{figure}[H]
0481 | \centering
0482 | \begin{minipage}{.48\linewidth}\centering
0483 | \begin{forest} nominal tree
0484 | [NP
0485 |  [{\synnode{Det}{NP\textsubscript{D}}} [\mention{the}, roof]]
0486 |  [{\synnode{Head}{Nom}}, head edge
0487 |   [{\synnode{Mod}{AdjP}} [\mention{lucky}]]
0488 |   [{\synnode{Head}{N\textsubscript{D}}}, head edge [\mention{few}]]]]
0489 | \end{forest}
0490 | \end{minipage}\hfill
0491 | \begin{minipage}{.48\linewidth}\centering
0492 | \begin{forest} nominal tree
0493 | [NP
0494 |  [{\synnode{Det}{DP}} [\mention{the}, roof]]
0495 |  [{\synnode{Head}{Nom}}, head edge, before drawing tree={x/.option=!21.x}
0496 |   [{\synnode{Mod}{AdjP}} [\mention{lucky}]]
0497 |   [{\synnode{Head}{Nom}}, head edge, before drawing tree={x+=1.5em}
0498 |    [{\synnode{Mod--Head}{DP}}, no edge
0499 |     [{\synnode{Head}{D}}, head edge [\mention{few}]]]
0500 |    {\draw[-] (!uu.south) -- (); \draw[-,line width=1pt] (!u.south) -- (); }]]]
0501 | \end{forest}
0502 | \end{minipage}
0503 | \caption{\mention{The lucky few} with ordinary Head (left) and Mod--Head fusion (right). The determiner is separately realized in both. Internal structure within the article phrase and AdjP is suppressed.}\label{fig:few}
0504 | \end{figure}
0505 | 
0506 | Table~\ref{tab:matched-heads} compares the Head relations across five constructions; §\ref{sec:det-uniform} supplies the constraints under both taxonomies.
0507 | 
0508 | \begin{table}[H]
0509 | \centering\small
0510 | \caption{Head and dependent functions under matched analyses. Each independent expression is an NP; \mention{the} fills Det wherever it appears. The ordinary-Head column applies to both taxonomies permitting ordinary determinative heads.}\label{tab:matched-heads}
0511 | \begin{tabular}{>{\raggedright\arraybackslash}p{2.8cm}>{\raggedright\arraybackslash}p{4.5cm}>{\raggedright\arraybackslash}p{4.5cm}}
0512 | \toprule
0513 | Expression & Separate D with fusion & Ordinary determinative Head \\
0514 | \midrule
0515 | \mention{few survivors} & \mention{few}: Det; \mention{survivors}: Head & Same functions \\
0516 | Independent \mention{few} & \mention{few}: Det--Head & \mention{few}: Head \\
0517 | \mention{the few} & \mention{few}: Mod--Head & \mention{few}: Head \\
0518 | \mention{the lucky few} & \mention{few}: Mod--Head; \mention{lucky}: Mod & \mention{few}: Head; \mention{lucky}: Mod \\
0519 | \mention{the idle rich} & \mention{rich}: Mod--Head; \mention{idle}: Mod & Same fusion and modifier functions \\
0520 | \bottomrule
0521 | \end{tabular}
0522 | \end{table}
0523 | 
0524 | Fusion groups \mention{the lucky few} with \mention{the idle rich}; ordinary headedness groups it with \mention{the lucky survivors} and unifies bare and externally determined \mention{few}. Both cover the example. The choice is between sharing fusion across D and adjective, and sharing ordinary Head structure across determinative constructions.
0525 | 
0526 | Reducing fusion's applications can simplify this description even when fusion remains available for adjectives. The advantage is the uniform treatment of \mention{few}; its value depends on any additional conditions or lost generalizations elsewhere.\footnote{Compare the theory of second best in \textcite[11--12]{lipseylancaster1956secondbest}: under a constraint preventing an optimum, satisfying more optimality conditions needn't improve the outcome. The analogy concerns interactions among grammatical choices, not a formal optimum for the grammar.} Section~\ref{sec:costs} compares those costs while holding the lexical restrictions fixed.
0527 | 
0528 | The constructed \mention{the remaining three} extends the modifier pattern to cardinals. It doesn't independently decide whether \mention{three} is determinative or has a common-noun use: \textcite{reynolds2026numerals} argues for both uses of cardinals. Section~\ref{sec:costs} treats their unification as a consequence conditional on that analysis.
0529 | 
0530 | The modifier permissions needed under ordinary headedness now require a closer comparison.
0531 | 
0532 | \subsection{Modifier selection and attachment}\label{sec:payne}
0533 | 
0534 | The selection and ordering contrast in §\ref{sec:adjectival-profile} guides the attachment analysis. Approximative and focusing modifiers have established NP parallels; the degree series selects the four gradable quantifiers. Both ordinary-Head accounts can represent that difference by distinguishing NP-peripheral modification from modification inside Nom.
0535 | 
0536 | Peripheral modifiers attach outside an NP's internal dependents. Compare \mention{only you}, \mention{for almost my entire life}, and \mention{Usually a careful driver, Anne found her mind wandering}. The modifiers precede any determiner belonging to the NP they modify. \textit{CGEL} already assigns them NP-level attachment \citep[430--431]{huddleston2002}. Focusing \mention{even} and \mention{just}, and approximatives such as \mention{nearly}, \mention{hardly}, \mention{virtually}, and \mention{practically}, likewise have NP uses, subject to their own scope and selectional restrictions.
0537 | 
0538 | In \mention{almost every experienced teacher}, \mention{almost} belongs with \mention{every}, while \mention{experienced} modifies \mention{teacher}. Figure~\ref{fig:every} places \mention{almost} at the periphery of the NP headed by \mention{every}. That smaller NP functions as Det in the larger NP, whose ultimate head is \mention{teacher}.
0539 | 
0540 | \begin{figure}[H]
0541 | \centering
0542 | \begin{forest} nominal tree
0543 | [NP
0544 |  [{\synnode{Det}{NP\textsubscript{D}}}
0545 |   [{\synnode{Mod}{AdvP}} [\mention{almost}]]
0546 |   [{\synnode{Head}{NP\textsubscript{D}}}, head edge
0547 |    [{\synnode{Head}{Nom}}, head edge
0548 |     [{\synnode{Head}{N\textsubscript{D}}}, head edge [\mention{every}]]]]]
0549 |  [{\synnode{Head}{Nom}}, head edge
0550 |   [{\synnode{Mod}{AdjP}} [\mention{experienced}]]
0551 |   [{\synnode{Head}{N\textsubscript{common}}}, head edge [\mention{teacher}]]]]
0552 | \end{forest}
0553 | \caption{Peripheral \mention{almost} modifies the smaller NP headed by \mention{every}; the resulting \mention{almost every} NP functions as Det. The adjective \mention{experienced} modifies the common-noun nominal. Internal structure within the one-word modifier phrases is suppressed.}\label{fig:every}
0554 | \end{figure}
0555 | 
0556 | \textcite[40--42]{payne2010} defend keeping \mention{few}, \mention{any}, and related forms in one lexical category across dependent and independent uses. In \mention{hardly any money} and independent \mention{hardly any}, \mention{hardly} remains an adverb and \mention{any} retains its category. The D-noun analysis preserves that continuity. It also preserves their contrast between adverbial premodification, as in \mention{almost anybody}, and adjectival postmodification, as in \mention{nothing absolute}.
0557 | 
0558 | The proposed analysis gives adverbs such as \mention{very} and \mention{too} internal attachment in dependent and independent uses alike. In \mention{the very few people}, it modifies the Nom headed by \mention{few}; the resulting \mention{very few} NP functions as Mod in the larger NP. In \mention{the very few who objected}, \mention{few} remains ordinary Head and \mention{very} remains internal. The degree relation is unchanged, and one internal permission covers both constructions. The same analysis applies to \mention{the very many}.
0559 | 
0560 | NP degree modifiers provide a further connection. Determinatives permit determinative premodifiers such as \mention{this} in \mention{this much} \citep[393]{huddleston2002}. Comparative determinatives also take established NP modifiers: \mention{a lot} in \mention{a lot fewer}, alongside \textit{CGEL}'s \mention{a lot more than fifty} \citep[432]{huddleston2002}. These modify the quantity expressed by the head. Under the proposed analysis, they're internal NP modifiers within its nominal projection, with permissions specific to the head and construction.
0561 | 
0562 | \textcite[42--47]{payne2010} establish that adverbs can postmodify common nouns, as in the constructed \mention{the changes globally to the climate}. They also analyse \mention{almost} as modifying the attributive nominal \mention{textbook} in \mention{an almost textbook case} \citep[p.~75, n.~3]{payne2010}. Adverbial modification therefore isn't categorically excluded from Noun, even internally. Its broader availability with determinatives remains a difference of distribution within the proposed category.
0563 | 
0564 | Approximatives also need internal attachment where they follow an external determiner on an independent cardinal: \mention{the almost thirty who came}. The internal AdvP permissions at issue are thus the degree series on \mention{few}, \mention{many}, \mention{much}, and \mention{little} across dependent and independent uses, and approximatives on externally determined independent cardinals.
0565 | 
0566 | \subsection{Compounds and their modifier domains}\label{sec:compounds}
0567 | 
0568 | A more demanding modifier comparison is \mention{hardly anyone present}. \textcite[581--583]{Payne2007} assign \mention{hardly} to DP structure and \mention{present} to nominal structure. The compound \mention{anyone} takes the premodifiers of its determinative base \mention{any}: compare \mention{hardly any writer present}. The adjective realizes a specialized \term{restrictor} function, restricted to post-head position and non-recursive. Figure~\ref{fig:compound} contrasts this account with an ordinary-Head analysis.
0569 | 
0570 | \begin{figure}[H]
0571 | \centering
0572 | \begin{minipage}{.48\linewidth}\centering
0573 | \begin{forest} nominal tree
0574 | [NP
0575 |  [{\synnode{Mod}{AdvP}} [\mention{hardly}]]
0576 |  [{\synnode{Head}{NP}}, head edge
0577 |   [{\synnode{Head}{Nom}}, head edge
0578 |    [{\synnode{Head}{N\textsubscript{D}}}, head edge [\mention{anyone}]]
0579 |    [{\synnode{Mod}{AdjP}} [\mention{present}]]]]]
0580 | \end{forest}
0581 | \end{minipage}\hfill
0582 | \begin{minipage}{.48\linewidth}\centering
0583 | \begin{forest} nominal tree
0584 | [NP, before drawing tree={x/.option=!11.x}
0585 |  [{\synnode{Head}{Nom}}, head edge, before drawing tree={x+=4em}
0586 |   [{\synnode{Det--Head}{DP}}, no edge
0587 |    [{\synnode{Mod}{AdvP}} [\mention{hardly}]]
0588 |    [{\synnode{Head}{D}}, head edge [\mention{anyone}]]]
0589 |   {\draw[-] (!uu.south) -- (); \draw[-,line width=1pt] (!u.south) -- (); }
0590 |   [{\synnode{Mod}{AdjP}}, before drawing tree={x/.option=!u.x} [\mention{present}, before drawing tree={x/.option=!u.x}]]]]
0591 | \end{forest}
0592 | \end{minipage}
0593 | \caption{\mention{Hardly anyone present} with ordinary Head (left) and fusion (right). On the left, \mention{hardly} is peripheral to NP and \mention{present} is internal to Nom. Both post-head Mod positions realize the specialized restrictor. In the fusion tree, DP fills Det of NP and Head of Nom, following \textcite[p.~582, (13d)]{Payne2007}. Modifier-phrase interiors are suppressed.}\label{fig:compound}
0594 | \end{figure}
0595 | 
0596 | In the ordinary-Head tree, \mention{anyone} inherits nominal projection from Noun and its premodifier permissions from its determinative base. Peripheral \mention{hardly} follows the approximative pattern and its NP parallels in §\ref{sec:payne}. The compound construction independently excludes external determination and supplies the internal post-head restrictor permission, with the same position and non-recursion conditions as the fusion account. It doesn't license a corresponding pre-head adjective.
0597 | 
0598 | The relative clauses in §\ref{sec:independent} are ordinary postmodifiers, distinct from the specialized restrictor. When both occur, the relative follows it: \mention{something useful that I found}. \textit{CGEL} explicitly gives compounds the common noun's range of ordinary postmodifiers while preserving this ordering condition \citep[423]{huddleston2002}.
0599 | 
0600 | The same division applies to \mention{someone} and \mention{everybody}: the compound construction licenses the post-head restrictor, while the determinative base supplies its premodifier permissions. The example \mention{something reliable and good looking} illustrates the post-head pattern (§\ref{sec:independent}).
0601 | 
0602 | Both accounts separate the modifier domains structurally: fusion uses the DP--Nom boundary, and ordinary headedness uses the NP--Nom boundary. Their constituent groupings differ: ordinary Head groups \mention{anyone present} in the inner NP, whereas fusion groups \mention{hardly anyone} in DP.
0603 | 
0604 | \subsection{Independent genitives}\label{sec:genitive-head}
0605 | 
0606 | \textit{CGEL} also uses fusion with nouns. Anaphoric \mention{mine}, understood as \enquote*{my car}, combines the possessive relation with an understood nominal description and receives a fused analysis. Predicative \mention{mine}, as in \mention{it's mine}, can instead mean \enquote*{belongs to me}: it expresses the relation directly, without an understood nominal head \citep[410--411, 470--471]{huddleston2002}. A suitable context may permit either reading.
0607 | 
0608 | The proposed analysis gives \mention{mine} ordinary Head in both anaphoric and predicative uses. Its genitive form expresses a relation to the speaker; context can supply the understood nominal description, as it can with independent \mention{few}. The \mention{my}/\mention{mine} alternation remains a form-selection condition, parallel to \mention{no}/\mention{none}. This extends ordinary headedness to an existing noun subcategory.
0609 | 
0610 | In referential uses, the independent-genitive construction supplies the NP's interpretation and agreement properties based on the possessed entity or entities. Compare constructed \mention{I am ready} with \mention{Mine is ready} (\enquote*{my contribution}) and \mention{Mine are ready} (\enquote*{my slides}). The pronoun's first-person feature identifies the possessor; the independent NP has third-person singular or plural agreement.
0611 | 
0612 | The fragment now makes the permissions and restrictions explicit so that the structural accounts can be compared.

SECTION 5: The matched fragment and comparative costs
0614 | \section{The matched fragment and comparative costs}\label{sec:economy}
0615 | 
0616 | A grammatical \term{fragment} states conditions on a specified range of constructions. Each account assigns categories and Head relations to the same expressions. The conditions specify permitted functions, dependents, and combinations of forms. They describe structures directly, following the constraint-based approach outlined by \textcite{pullum2020theorizing}. Comparing their content and reuse makes the accounts' commitments explicit; counting written statements wouldn't measure grammatical economy.
0617 | 
0618 | \subsection{Scope and use permissions}\label{sec:fragment}
0619 | 
0620 | The fragment covers determination, internal nominal modification, ordinary subject, object, and complement-of-preposition uses, partitives, and the compound comparisons in §\ref{sec:evidence}. It admits relative postmodifiers without analysing their internal grammar. Predication, interrogative clause structure, and modification outside NP structure lie beyond its scope. Degree uses enter the wider comparison in §\ref{sec:enough}.
0621 | 
0622 | Table~\ref{tab:permissions} separates uses before another nominal from independent argument uses. These are lexical \term{use permissions}, with separate conditions selecting the appropriate form. A permission applies to an occurrence in the specified construction. Intermediate Head relations within its projection don't require a further argument permission. Noun membership alone grants none of these permissions.
0623 | 
0624 | \begin{table}[H]
0625 | \centering\small
0626 | \caption{Selected permissions and form restrictions in the fragment. Det and Mod concern uses before another nominal; Mod is internal. A dash excludes that use from the fragment. Unstressed \mention{some} has the target restriction shown.}\label{tab:permissions}
0627 | \setlength{\tabcolsep}{4pt}
0628 | \begin{tabular}{lcccc>{\raggedright\arraybackslash}p{4.7cm}}
0629 | \toprule
0630 | Form & Det & Mod & Subj & Obj / CompP & Target before another nominal \\
0631 | \midrule
0632 | \mention{the} & yes & -- & -- & -- & No count or number restriction \\
0633 | \mention{a} & yes & -- & -- & -- & Singular count \\
0634 | \mention{every} & yes & yes & -- & -- & Singular count; Mod after genitive Det \\
0635 | \mention{some} & yes & -- & yes & yes & Plural count or non-count \\
0636 | \mention{few} & yes & yes & yes & yes & Plural count \\
0637 | \mention{no} & yes & -- & -- & -- & No count or number restriction \\
0638 | \mention{none} & -- & -- & yes & yes & Not applicable \\
0639 | \mention{my} & yes & -- & -- & -- & No count or number restriction \\
0640 | \mention{mine} & -- & -- & yes & yes & Not applicable \\
0641 | \mention{she} & -- & -- & yes & -- & Not applicable \\
0642 | \mention{her} (plain) & -- & -- & -- & yes & Not applicable \\
0643 | \bottomrule
0644 | \end{tabular}
0645 | \end{table}
0646 | 
0647 | Subj and Obj denote subject and object; CompP denotes complement of a preposition. The \mention{no}/\mention{none} and \mention{my}/\mention{mine} pairs distinguish forms within a paradigm (§\ref{sec:form-selection}). Plain \mention{she}/\mention{her} distinguishes subject from object and prepositional-complement uses. Quotation, metalinguistic naming, and subordinate-clause uses of dependent genitives fall outside the fragment.
0648 | 
0649 | Target restrictions apply to the nominal being determined or modified, including a nominal headed by an independent determinative. Thus \mention{the} permits plural \mention{few} in \mention{the few}. Determinative-headed phrases also bear number and count properties: \mention{few} is plural count, while \mention{some} takes its interpretation from the construction and domain. The modifier \mention{this} in \mention{this much} expresses degree; its permission doesn't follow from demonstrative Det selection.
0650 | 
0651 | Hudson distinguishes dependency from external headedness. He argues that determiner and common noun depend on each other, although only one connects the phrase to its surroundings \citep[7--8]{hudson2004determiners}. His temporal adjunct evidence supports common-noun headedness: \mention{I saw him that day} is possible, whereas \ungram{\mention{I saw him that point in time}} isn't, despite the similar temporal meanings \citep[10--12]{hudson2004determiners}. The lexical noun matters, as well as the determiner restrictions.
0652 | 
0653 | Reciprocal selection is compatible with this headedness. A singular count noun normally requires determination, while \mention{every} requires another nominal and \mention{some} doesn't. The noun can remain Head while both constituents impose conditions. For an occurrence $x$ with external function $f$ in a surrounding structure $s$, the shared use condition is:
0654 | 
0655 | \[
0656 | \operatorname{admissible}(x,f,s)
0657 | \quad\Longleftrightarrow\quad
0658 | f\in U_{\ell(x)}\ \land\ \operatorname{Form}(x,f,s)\ \land\ C(x,f,s).
0659 | \]
0660 | 
0661 | Here $\ell(x)$ identifies the lexical head's lexeme and $U_{\ell(x)}$ its use permissions. $\operatorname{Form}$ checks the selected form; $C$ checks the occurrence's dependents, its target where relevant, and the other constructional conditions. The structure $s$ includes both $x$ and its surroundings. The conditions below give this predicate content for the constructions being compared; the formula isn't a substitute for specifying them.
0662 | 
0663 | \subsection{Phrase categories and structural constraints}\label{sec:det-uniform}
0664 | 
0665 | In \mention{some apples} and \mention{Kim's apples}, the determining phrases share the NP category under D-noun with ordinary Head. Separate D can permit the same projection. For D-noun with fusion, I retain that NP category and add the combined function relations in independent uses. \textit{CGEL} instead distinguishes DP from genitive NP. It also admits restricted plain-case NPs and PPs as determiners, as in \mention{what size hat} and \mention{over thirty ties} \citep[Ch.~5, §4]{huddleston2002}.
0666 | 
0667 | I carry this PP-determiner provision over to the three NP-projecting implementations for the present comparison. Its inclusion in the alternatives is an extrapolation.
0668 | 
0669 | \[
0670 | \begin{aligned}
0671 | \text{\textit{CGEL}:} &\quad \mathrm{Det}:\{\mathrm{DP},\mathrm{NP},\mathrm{PP}\} \\
0672 | \text{NP-projecting implementations here:} &\quad \mathrm{Det}:\{\mathrm{NP},\mathrm{PP}\}
0673 | \end{aligned}
0674 | \]
0675 | 
0676 | NP projection consolidates the principal phrase types in Det function. Determinative-headed, genitive, and other licensed NPs still require separate identification. All four implementations retain at most one Det per NP and the same definiteness and target-selection conditions. The notation NP itself imposes no requirement that the ultimate lexical head be Noun: that would prejudge the separate-D ordinary-Head alternative.
0677 | 
0678 | The ordinary-Head accounts share three structural conditions. First, an NP core has a Nom as Head and at most one Det. Second, a nominal core has a lexical Head and only the dependents permitted for that head in its construction. Third, a peripheral modifier combines with an NP whose Head relation continues to an NP, as in Figure~\ref{fig:every}. This keeps peripheral modification outside the core's Det and Nom dependents.
0679 | 
0680 | Where a word $h$ directly fills Head in Nom, the two taxonomies differ in the category condition:
0681 | 
0682 | \[
0683 | \begin{aligned}
0684 | \text{D-noun, ordinary Head:} &\quad \operatorname{Cat}(h)=\mathrm{N} \\
0685 | \text{Separate D, ordinary Head:} &\quad \operatorname{Cat}(h)\in\{\mathrm{N},\mathrm{D}\}.
0686 | \end{aligned}
0687 | \]
0688 | 
0689 | Under D-noun, determinatives satisfy the first condition as members of Noun. Separate D admits them alongside Noun. Both permit the same nominal layers, selected complements, and ordered modifiers. Their agreement on phrase structure leaves the lexical grouping open to the profile argument.
0690 | 
0691 | The dependent conditions distinguish uses before another nominal from independent uses. In Det or internal Mod function before a target, ordinary \mention{some} and \mention{few} exclude external determination, partitive complements, and relative postmodifiers within their own phrase. Independent \mention{some} and \mention{few} permit selected partitives and relatives; independent \mention{few} also permits definite determination and adjectival premodification, as in \mention{the lucky few}. These permissions don't transfer to \mention{every} or the articles.
0692 | 
0693 | Degree-modifier selection applies across the relevant dependent and independent uses. It includes AdvPs such as \mention{very}, determinative-headed modifiers such as \mention{this} in \mention{this much}, and established NPs such as \mention{a lot} in \mention{a lot fewer}. Comparative complements, as in \mention{more than ten}, are licensed separately from partitive \mention{of}-phrases. Neither the category NP nor a general modifier slot licenses arbitrary adjectives or unrestricted complements.
0694 | 
0695 | Postmodification permits zero or more ordered dependents, subject to the construction. The compounds permit at most one specialized post-head restrictor followed by ordinary postmodifiers: \mention{useful} precedes \mention{that I found} in \mention{something useful that I found}. They exclude external determination and a corresponding pre-head adjective. Their determinative bases supply the premodifier restrictions (§\ref{sec:compounds}).
0696 | 
0697 | The approximatives retain the two attachment sites motivated in §\ref{sec:payne}: peripheral NP attachment in \mention{almost every} and internal attachment in externally determined \mention{the almost thirty who came}. Both ordinary-Head accounts require this distinction. Their use of established peripheral NP modification doesn't remove the need to state the internal cardinal permission.
0698 | 
0699 | Complex \mention{a few} and \mention{a little} have construction-specific conditions, including the position of internal degree modifiers in \mention{a very few}. Their initial \mention{a} isn't an ordinary Det selecting a plural \mention{few} target. The fragment records these combinations as complex determinatives and leaves their internal analysis beyond the position contrast unspecified. Fixed \mention{many a} retains its restriction to Det function (§\ref{sec:article-membership}).
0700 | 
0701 | These conditions separate the matched examples. In \mention{some apples}, \mention{some}'s phrase satisfies its Det permission and plural-count target selection. In \mention{Some left}, it satisfies its subject permission. \mention{Every apple} passes the dependent checks; independent \ungram{\mention{Every arrived}} fails its use permission. In \mention{the few people}, \mention{few}'s phrase is an internal Mod of the nominal headed by \mention{people}; in \mention{the lucky few}, \mention{few} heads the independently determined NP.
0702 | 
0703 | Each phrase's use permission follows its own lexical head. In \mention{the apple}, the smaller article phrase has Det permission; the outer NP has argument permission through \mention{apple}, whose determination requirement is satisfied. Bare \ungram{\mention{Book arrived}} fails that requirement, while \mention{Books arrived} passes. The article's exclusion from argument use remains a separate condition.
0704 | 
0705 | The fusion accounts retain these use, form, selection, and ordering conditions but assign different Head relations. Let $p$ be the independent NP, $m$ its Head Nom, and $x$ the shared determinative phrase. Write $\operatorname{Head}(p,m)$ for \enquote*{$m$ fills Head in $p$}, and likewise for Det and Mod. The two configurations satisfy the following relations:
0706 | 
0707 | \[
0708 | \begin{aligned}
0709 | \text{Det--Head:}\quad
0710 |  &\operatorname{Head}(p,m),\quad \operatorname{Det}(p,x),\quad \operatorname{Head}(m,x); \\
0711 | \text{Mod--Head:}\quad
0712 |  &\operatorname{Head}(p,m),\quad \operatorname{Mod}(m,x),\\
0713 |  &\operatorname{Head}(m,n),\quad \operatorname{Head}(n,x),\qquad \operatorname{Cat}(n)=\mathrm{Nom}.
0714 | \end{aligned}
0715 | \]
0716 | 
0717 | Det--Head fills the NP's Det function, excluding a second Det. Mod--Head leaves that function available for an external determiner. Its additional Nom $n$ matches Figure~\ref{fig:few}: the determinative phrase fills Mod in $m$ and Head in $n$. The ordinary adjective \mention{lucky} separately modifies $m$. These are simultaneous relations on a shared constituent, with no sequence of fusion operations assumed.
0718 | 
0719 | Under separate D with fusion, $x$ is a DP whose lexical Head is D. Selected premodifiers and comparative complements belong within that DP; the independent partitive complement, compound restrictor, and ordinary postmodifiers belong to nominal structure outside it, as in Figure~\ref{fig:compound}. The permissions for the complete independent NP still exclude articles and \mention{every}. Possessing a dependent Det use doesn't itself license an independent fused use.
0720 | 
0721 | Under D-noun with fusion, $x$ is the NP projected by the determinative noun. The same joint relations connect it to the outer nominal structure. In this construction the inner NP excludes external determination, partitives, restrictors, and relatives: any licensed independent-use dependents occur outside it, as in the separate-D fusion account. These restrictions need stating separately from the limit of one fusion configuration around the determinative's projection.
0722 | 
0723 | Ordinary headedness uses the determinative's NP directly for bare, partitive, and externally determined expressions. Fusion surrounds its DP or NP with the nominal structure just specified. Both ordinary-Head accounts share structures; under D-noun they follow from Noun membership, while separate D admits them across a primary-category boundary. I take that alignment to favour D-noun, subject to the restrictions and comparative costs summarized below.
0724 | 
0725 | Nesting determinative inside pronoun would add pronoun to the inheritance path from Noun without changing this fragment's judgments. Applying Hudson's nesting to the full determinative inventory used here is an extrapolation; §\ref{sec:inheritance} discusses the inventory differences.
0726 | 
0727 | 
0728 | \subsection{Degree uses outside noun phrases}\label{sec:enough}
0729 | 
0730 | When \mention{enough} modifies \mention{good} in \mention{good enough}, the three NP-projecting implementations analyse it as an NP modifier of an adjective. This would be a cost if NPs couldn't occur in that function, or if their distribution differed systematically from that of degree determinatives. The comparison must therefore include the degree uses of established NPs.
0731 | 
0732 | \mention{Enough} tests both position and external function. It precedes a nominal in \mention{enough money} and can follow one in \mention{money enough}; post-head \mention{enough} can't itself be premodified, as shown by \ungram{\mention{money almost enough}} \citep[396--397, 445]{huddleston2002}. Only the permitted construction licenses each position.
0733 | 
0734 | NP modification inside an AdjP also permits post-head position. In the constructed examples in (\ref{ex:temporal-adjp}), I analyse \mention{every Tuesday}, \mention{this week}, and \mention{next week} as temporal NP modifiers within the bracketed AdjPs. The separate degree modifiers and temporal specifications in the coordinated example make that attachment clear. These NPs express time, while \mention{enough} expresses degree; the shared position leaves their selectional differences intact.
0735 | 
0736 | \ea\label{ex:temporal-adjp}
0737 | \ea \mention{Applicants} [\mention{completely free every Tuesday}] \mention{will be interviewed next month.}
0738 | \ex \mention{Anyone} [\mention{very busy this week}] \mention{but} [\mention{completely free next week}] \mention{should contact me today.}
0739 | \z\z
0740 | 
0741 | \mention{Enough} also modifies adjectives, adverbs, verbs, and some PPs: \mention{good enough}, \mention{quickly enough}, \mention{I hadn't prepared enough}, and \mention{enough in control} \citep[396--397]{huddleston2002}. The degree determinatives \mention{much} and \mention{little}, and \mention{no}/\mention{none}, likewise have uses outside NP structure \citep[390, 395--397]{huddleston2002}. These permissions must survive recategorization. Noun membership doesn't confine every projection to argument or determiner function.\footnote{\mention{Both}, \mention{either}, and \mention{neither} also serve as markers of coordination \citep[1305, 1308]{huddleston2002}. Their noun categorization would preserve that further category--function combination; the present fragment doesn't analyse coordination.}
0742 | 
0743 | NPs already modify adjectives in \mention{three years old}, \mention{a great deal smaller}, and \mention{plenty big enough}. \textit{CGEL} also explicitly treats \mention{lots better} and \mention{heaps worse} as containing quantificational NP modifiers \citep[549--550]{huddleston2002}. These uses extend the connection with the quantificational common nouns compared in §\ref{sec:quant-nouns}.
0744 | 
0745 | Attributive uses are attested too: \mention{some heaps better photo's} and \mention{some lots better ones}.\footnote{\href{https://www.aulro.com/afvb/motor-cycling/61858-my-track-day-phillip-island-motogp-track-post798794.html}{AULRO, moose, 19 August 2008, post 2}; original spelling retained. The \href{https://www.uberpeople.net/threads/let-s-play-would-you-have-taken-this-trip.395130/}{Uber Drivers Forum} example was verified in an indexed excerpt; its author and post date remain unverified.} In \textit{CGEL}'s analysis, \mention{ones} here is an anaphoric common noun. Both examples therefore have attributive \mention{better} with a nominal degree modifier. Measure \mention{miles} supplies parallels in \mention{some miles better front brakes} and \mention{some miles-better bands}.\footnote{\href{https://www.uksaabs.co.uk/UKS/viewtopic.php?t=131481\#p1256815}{UKSaabs, rallyv4, 23 January 2014, post 6}; Shaun Ryder in \href{https://www.newstatesman.com/culture/2019/04/i-look-like-uncle-fester-the-second-life-of-shaun-ryder}{Kate Mossman's interview, \textit{New Statesman}, 17 April 2019}. The latter retains the source's hyphen, which doesn't itself settle the modifier's syntactic structure.}
0746 | 
0747 | These attestations challenge \textit{CGEL}'s general exclusion of NP modifiers from attributive AdjPs. Its contrast between predicative \mention{a great deal better} and \ungram{\mention{some a great deal better proposals}}, against permitted \mention{some much better proposals}, remains a more restricted observation \citep[551--552]{huddleston2002}. The excluded example also juxtaposes \mention{some} and \mention{a}, so its unacceptability can't by itself be attributed to NP category.
0748 | 
0749 | \textit{CGEL} already permits \mention{She's a lot better player than me}, analysing the article belonging to \mention{a lot} as lost after the article determining the larger NP \citep[p.~552, n.~8]{huddleston2002}. The \mention{heaps} and \mention{lots} examples have outer \mention{some} and no internal article, so they extend beyond this exception.
0750 | 
0751 | Measure expressions such as \mention{a weeks-long trip} and \mention{a meters-tall tree} sharpen the comparison. Their plural nouns contrast with the singular measure in \mention{a three-year-old child}, which \textit{CGEL} treats as a compound adjective \citep[552, 1660]{huddleston2002}. Yet \textcite[68]{alegregordon1996} analyse \mention{weeks-long seminar} as a compound too. These examples extend the nominal comparison, while leaving open whether they involve ordinary NP modification within an AdjP or compounding. Plural marking alone doesn't decide between the two analyses.
0752 | 
0753 | The COCA examples in (\ref{ex:measure-attributive}) add overt quantification within the plural measure expressions.\footnote{COCA, 2012 WEB records from \nolinkurl{amazon.com} and \nolinkurl{tvtropes.org}, respectively. The first describes a soundtrack booklet; the second a passage in \textit{Three Men in a Boat}. Original spacing and plural forms are retained.} The numeral \mention{45} and determinative \mention{several} make these stronger comparisons than bare \mention{weeks-long}. In each case, \mention{a} belongs to the outer NP. A phrasal-compound analysis remains possible, but calling the expressions compounds doesn't itself explain their internal syntax.
0754 | 
0755 | \ea\label{ex:measure-attributive}
0756 | \ea \mention{a 45 pages long booklet}
0757 | \ex \mention{a several pages long passage}
0758 | \z\z
0759 | 
0760 | The attestations don't establish unrestricted attributive use for nominal degree modifiers. They require a closer comparison of lexical, constructional, and register conditions under all four implementations. NP projection places degree determinatives within an existing nominal range; the attributive contrast doesn't yet establish an added cost, or a corresponding advantage for retaining DP.
0761 | 
0762 | \subsection{Comparison of the four implementations}\label{sec:costs}
0763 | 
0764 | Table~\ref{tab:economy} compares the four implementations. The Head configurations, modifier permissions, and taxonomic consequences are kept distinct so that the contribution of each choice is visible. The inventory, constructions, and readings remain fixed.
0765 | 
0766 | \begin{table}[H]
0767 | \centering\small
0768 | \caption{Four implementations compared. All retain the lexical and constructional restrictions and adjectival fusion, and must account for attributive nominal degree modifiers. Cardinal and \mention{one} groupings are consequences of the categorization.}\label{tab:economy}
0769 | \setlength{\tabcolsep}{3pt}
0770 | \begin{tabular}{>{\raggedright\arraybackslash}p{2.5cm}>{\raggedright\arraybackslash}p{3.6cm}>{\raggedright\arraybackslash}p{3.6cm}>{\raggedright\arraybackslash}p{2.65cm}}
0771 | \toprule
0772 | Account & Independent determinatives & Modifier permissions & Taxonomic consequences \\
0773 | \midrule
0774 | D-noun, ordinary Head & Nom--NP with Head alone across bare, partitive, and externally determined uses. & Peripheral NP premodifiers; head-specific internal modifiers. Degree determinatives project NP. & D within Noun. Cardinal uses and the three \mention{one} lexemes are grouped there. \\
0775 | Separate D, ordinary Head & Same structures, with Nom admitting either N or D as lexical Head. & Same internal and peripheral permissions and degree projection as the proposed package. & D remains separate from nominal counterparts. \\
0776 | Separate D, fused Head & DP fills Det--Head or Mod--Head in nominal structure. & DP--Nom separates premodifiers and postmodifiers. Degree determinatives project DP. & Same primary-category divisions as separate D with ordinary Head. \\
0777 | D-noun, fused Head & A projected NP fills Det--Head or Mod--Head in additional nominal structure. & Premodifiers within the fused NP; postmodifiers in the outer Nom. Degree determinatives project NP. & Same Noun grouping as the proposed package. \\
0778 | \bottomrule
0779 | \end{tabular}
0780 | \end{table}
0781 | 
0782 | The articles' restrictions, \mention{no}/\mention{none} form selection, and the compound restrictor conditions are already required in the separate-D grammar. Retaining them isn't an added cost of D-noun. Likewise, differences among existing noun subcategories in determination and modification remain in place (Table~\ref{tab:existing}).
0783 | 
0784 | The internal degree-AdvP permissions on \mention{few}, \mention{many}, \mention{much}, and \mention{little}, and the internal approximatives with externally determined cardinals, remain explicit (§\ref{sec:payne}). Both ordinary-Head accounts also use peripheral NP modification. Fusion instead places the compound's premodifiers within the fused phrase and its postmodifiers on the outer Nom (§\ref{sec:compounds}).
0785 | 
0786 | \textcite{reynolds2026numerals} distinguishes determinative numerals such as \mention{ten} in \mention{ten men}, proper-noun cases such as \mention{10} in \mention{Room 10}, and common-noun numerals such as \mention{tens} in \mention{tens of pens}. Under the D-noun categorization, all fall within primary Noun, retaining their subcategory and constructional differences. Ordinals remain adjectives, and complex numeral phrases remain distinct from single lexemes.
0787 | 
0788 | \textcite[797--798]{payne2013anaphoric} distinguish three lexemes spelled \mention{one}: determinative, anaphoric common noun, and generic pronoun. These remain distinct under the D-noun categorization, but all belong within primary Noun.
0789 | 
0790 | Complex cardinals also separate category from function. In \mention{two hundred books}, the whole \mention{two hundred} fills Det; internally, \mention{two} modifies the magnitude head \mention{hundred} \citep[§4]{reynolds2026numerals}. In \mention{these two hundred books}, \mention{these} fills Det and \mention{two hundred} is an internal modifier. One Det function doesn't entail a limit of one determinative lexeme per NP.
0791 | 
0792 | These cardinals and the lexemes spelled \mention{one} retain their distinctions within one primary category. That consequence belongs to the categorization and is shared by its ordinary- and fused-Head implementations.
0793 | 
0794 | \subsection{Overall assessment}\label{sec:overall-assessment}
0795 | 
0796 | I favour the D-noun package because the profile and the ordinary NP structures support a common nominal treatment. Including determinatives within Noun makes those structures a natural application of nominal grammar; their regularity in turn strengthens the grouping. The commitments are complementary, although neither requires the other. Separate D with ordinary Head and D-noun with fusion remain coherent alternatives. Reducing the number of primary categories alone wouldn't establish the preference.
0797 | 
0798 | If determinative-headed and genitive expressions require different structural constraints after their independently motivated restrictions are held fixed, the shared-projection proposal in §\ref{sec:det-uniform} loses its advantage. That would favour separate phrase types. Retaining a separate primary D requires the further case that the category boundary captures the recurring differences better than a determinative subcategory within Noun.
