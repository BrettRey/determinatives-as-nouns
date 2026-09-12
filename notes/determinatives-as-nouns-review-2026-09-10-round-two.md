# Determinatives as nouns in English
Brett Reynolds — 10 September 2026 working draft

Revised after the second author round: the fourfold proposal, parsimony and cardinal overlap. Trees and schemata are shown as text; footnotes appear beside their paragraphs. The LaTeX source remains the manuscript master. [Typeset PDF](../determinatives-as-nouns.pdf).
# Abstract
I argue that English determinatives belong within Noun as a fourth coordinate subcategory alongside common nouns, proper nouns and pronouns. The argument extends the grounds on which _The Cambridge grammar of the English language_ already includes pronouns despite their distinctive inflection and restricted dependents. Independent uses, number, genitives, partitives and modification support a shared nominal profile. As nouns, determinatives inherit the nominal structure for heading NPs, with lexical and constructional restrictions preserved, including those of articles. A matched grammatical fragment compares this analysis with separate-D grammars using ordinary heads or fusion. The taxonomic choice concerns inheritance through Noun versus projection licensed across separate noun and determinative categories.

**Keywords:** determinatives, nouns, lexical categories, noun phrases, English
# 1 The question
What is the categorial relationship among words such as _some_, _me_, _apple_ and _Brett_? I argue that all four are nouns, and that determinatives form a coordinate subcategory alongside common nouns, proper nouns and pronouns. I call this fourfold proposal the determinative-noun or D-noun analysis.

I adopt the general framework of _The Cambridge grammar of the English language_ (_CGEL_; Huddleston and Pullum (2002)). Unlike _CGEL_, though, I include determinatives within Noun. The claims concern synchronic English lexical categories.

I use determinative for the category containing articles, demonstratives and quantifiers such as _the_, _this_, _some_, _every_ and _many_. I reserve determiner for a syntactic function within the noun phrase. This distinction separates what kind of word _some_ is from what syntactic relationships its phrase participates in. Capitalized Noun names the proposed superordinate category containing common nouns, proper nouns, pronouns and determinative nouns.

> Note 1. For a fuller inventory, see the online [“List of determinatives in English”](https://www.cambridge.org/highereducation/api/resources/2AC8DF5CA558F8A6FCDFACD0EAF8EA08) accompanying Huddleston et al. (2022).

_CGEL_ already places common nouns, proper nouns and pronouns within Noun. It expressly justifies pronoun membership by the functions of pronoun-headed phrases, despite differences in inflection and dependents (Huddleston and Pullum 2002, 327–28). The question here is whether determinatives meet comparable grounds for inclusion. Differences from common nouns alone can’t settle that question: the accepted noun subcategories already differ from one another. The inclusion of auxiliaries within Verb supplies a precedent for this kind of extension: a closed category can retain its distinctive syntax within a broader lexical category (Pullum and Wilson 1977).

Classifying determinatives as nouns gives them the nominal projection rules of Noun. A determinative therefore heads a nominal (Nom), which heads an NP{++, exactly like pro-, common, and proper nouns do++}{id="s1" by="user" at="2026-09-10T15:22:59.143Z"}. Nom contains the head and its internal dependents, excluding an external determiner. Lexical restrictions govern which uses are available.

Figure 1 compares _CGEL_ with the D-noun analysis for _take some apples_ and _take some_. Both keep _some_ in one lexical category across uses. In _CGEL_, independent _some_ jointly fills determiner and head functions, a fusion of functions (Huddleston and Pullum 2002, 410–12). As a syntactic representation, fusion of functions appears to have seen little adoption outside work based on _CGEL_. In the D-noun analysis, _some_ heads its own NP through a Nom in both uses.

Here DP abbreviates determinative phrase, as in _CGEL_, not to be confused with the DP of the DP hypothesis, where D heads the whole expression _some apples_ ((Abney 1987); §2.1). The D-noun analysis keeps _apples_ as that expression’s ultimate head.

CGEL: take some apples {++[dependent _some_]++}{id="s2" by="user" at="2026-09-10T15:27:02.771Z"}

```text
VP
├── Head: V
│   └── take
└── Obj: NP
    ├── Det: DP
    │   └── Head: D
    │       └── some
    └── Head: Nom
        └── Head: N_common
            └── apples
```

CGEL: take some {++[independent some]++}{id="s3" by="user" at="2026-09-10T15:27:16.931Z"}

```text
VP
├── Head: V
│   └── take
└── Obj: NP ─────────────────┐
    └── Head: Nom            │
        └── Det–Head: DP ◄───┘
            └── Head: D
                └── some
```

D-noun analysis: take some apples

```text
VP
├── Head: V
│   └── take
└── Obj: NP
    ├── Det: NP
    │   └── Head: Nom
    │       └── Head: N_D
    │           └── some
    └── Head: Nom
        └── Head: N_common
            └── apples
```

D-noun analysis: take some

```text
VP
├── Head: V
│   └── take
└── Obj: NP
    └── Head: Nom
        └── Head: N_D
            └── some
```

Figure 1: _Take some apples_ (first and third trees) and _take some_ (second and fourth trees) under _CGEL_ (first pair) and the D-noun analysis (second pair). In the second tree, DP fills Det of NP and Head of Nom. In the third and fourth trees, _some_ heads an NP through the same nominal projection; that NP functions as Det in the third tree and Obj in the fourth tree. Function labels appear above category labels. Det marks determiner, Obj object, and Det–Head fusion; the two links show the combined functions. N, D and V mark noun, determinative and verb; NP, DP and VP mark their phrases. Subscripts identify noun subcategories.

Earlier unifications include Palmer’s grouping of determinatives with pronouns against the traditional adjectival classification, Postal’s underlying article analysis of pronouns, and Sommerstein’s underlying NP analysis of articles and pronouns (Palmer 1924; Postal 1966; Sommerstein 1972). Hudson places the words he calls determiners within pronoun and pronoun within noun (Hudson 2004, 2010). Section 2.2 compares these proposals; Table 1 locates the taxonomic alternatives.

The motivation is parsimony. First, including determinative within Noun removes a separate primary lexical category and its phrasal projection, replacing DP with NP. Second, it gives independent determinatives ordinary Head structure in the NP, unifying the bare, partitive and externally determined uses that _CGEL_ divides between Det–Head and Mod–Head fusion. Third, it brings the determinative, common-noun and proper-noun uses of cardinals within one primary category. Section 7 compares these reductions with the changes required in stating modifier and use restrictions.

I first distinguish the competing analyses, then establish what the existing noun subcategories share and how determinatives compare. Independent uses, partitives and modification identify the constructions to be explained. The matched fragment in §7.2 holds the judgments and lexical restrictions fixed while varying taxonomy and headedness.
# 2 Classification, headedness and function
## 2.1 Category, function and phrase structure
Lexical categories and syntactic functions cut across one another. An NP can function as determiner, as in _Kim’s book_, and a determinative-headed phrase can function as modifier, as in _the many people_ (Payne et al. 2010; Pullum and Miller 2022). Including determinatives within Noun preserves this distinction: the NP headed by _some_ functions as determiner in _take some apples_ and as object in _take some_ (Figure 1).

The question of lexical classification is distinct from the headedness question associated with the DP hypothesis of Abney (1987). Under that hypothesis, D heads expressions such as _some apples_. I retain noun-headed NPs and reject the DP analysis for English, following the arguments of Pullum and Miller (2022) and Bruening (2020).

Category membership doesn’t remove lexical restrictions. _Every apple_ is grammatical, but *_I’ll take every_ isn’t an ordinary way to accept apples. Making _every_ a noun doesn’t give it the full range of uses available to _some_. Section 7.2 states structural rules and lexical restrictions separately so their contributions can be assessed.
## 2.2 Taxonomic and structural alternatives
Keeping a word in one category across dependent and independent uses leaves its taxonomic position open. As Lyons (1968, 232–35) observes, distribution can be compared at different levels of categorization: two expressions may belong together at one level and differ at a more specific level. Table 1 sets out selected arrangements, from three separate primary categories to successive inclusion. Common and proper nouns remain within Noun throughout. The D-noun analysis differs from _CGEL_ by including determinative within Noun, and from Hudson by placing it alongside pronoun.

Table 1: Selected taxonomic arrangements. Noun contains common and proper nouns in every row; its other members vary. The Hudson row abstracts from differences in lexical inventory explained in the text.

| Relation among Noun, pronoun and determinative | Account or status |
| :--- | :--- |
| Noun, pronoun and determinative are separate primary categories. | Logical comparison |
| Pronoun is within Noun; determinative is a separate primary category. | _CGEL_ |
| Determinative is within Noun; pronoun is a separate primary category. | Logical comparison |
| Pronoun and determinative are coordinate subcategories of Noun. | D-noun analysis |
| Determinatives belong within pronoun, which is within Noun. | Hudson |
| Pronoun is within determinative, which is within Noun. | Reverse nesting for comparison |

Palmer (1924, 24) proposed placing {++"++}{id="s4" by="user" at="2026-09-10T15:29:05.501Z"}determinative {++adjective++}{id="s5" by="user" at="2026-09-10T15:29:07.788Z"}s{++"++}{id="s6" by="user" at="2026-09-10T15:29:10.903Z"} with pronouns, citing disagreement about their classification and most members’ ability to “be used indifferently as pronouns or as modifiers of nouns”. Lyons (1968, 279) also emphasizes the shared definiteness and deictic contrasts of articles, demonstratives and personal pronouns. The D-noun analysis retains determinatives and pronouns as distinct subcategories of Noun.

Hudson includes the determining words within pronoun. His noun category has the subcategories common noun, proper noun and pronoun (Hudson 2010, 253–54). In his terminology, a determiner is a pronoun whose valency permits the relevant common-noun dependent (Hudson 2004, 9–10). Identifying these words by their permitted dependents doesn’t require another category node.

_CGEL_ and Hudson classify different inventories. {==Hudson==}{>>My recollection is that he's handwavy and very selective in his arguments, what Croft calls "methodological opportunism" or Gelman calls the garden of forking paths.<<}{id="c1" by="user" at="2026-09-10T15:35:31.962Z"}’s criteria in the 2004 paper centre on licensing a singular count common noun and on mutual exclusion in that use. He sets aside _all_, cardinal numerals and quantifiers restricted to plural or non-count nouns. _CGEL_’s determinative category is broader, so the comparison requires checking which words and constructions each covers.

{==Anderson==}{>>Is this a general generativist argument, or and argument about English? Same question throughout.<<}{id="c2" by="user" at="2026-09-10T15:37:05.105Z"} (1997) draws the boundary of the nominal category differently. He groups names, pronouns and determining words as a notional {N} category, with common nouns represented separately. His {N} differs from the inclusive Noun proposed here and falls outside Table 1.

Taxonomic inclusion doesn’t settle the structural analysis. Hudson separates dependency from phrase headedness: his 2004 account permits mutual dependency between determiner and common noun, {++a complication that also hasn't received general uptake,++}{id="s7" by="user" at="2026-09-10T15:39:58.446Z"} with different constructions selecting different external heads (Hudson 2004, 7–9). In _We met that day_, the temporal adjunct depends on the temporal meaning of _day_. Such restrictions support a common-noun head for temporal adjuncts (Hudson 2004, 10–12).

Other unifications concern underlying representation. Postal (1966) unifies {==personal pronouns and articles==}{>>outside of N?<<}{id="c3" by="user" at="2026-09-10T15:42:10.532Z"} through an underlying article {==analysis==}{>>the generative theories of the time have all been superceded, and it's hard to know how to judge this, but I'd say it overlooked much that CGEL accounts for, and fails for that reason.<<}{id="c4" by="user" at="2026-09-10T15:42:22.325Z"}. {==Sommerstein==}{>>again, I don't think this accounts for many known phenomena<<}{id="c5" by="user" at="2026-09-10T15:44:03.225Z"} (1972, 197–203) reverses the direction, assigning underlying NP structure to the definite article and personal pronouns, with relative-clause structures contributing further descriptive material. These structures don’t by themselves place the surface lexical categories in Table 1. {==Déchaine and Wiltschko (2002) distinguish pro-DP, pro-φP and pro-NP==}{>>this is just the usual confused generativist garbage.<<}{id="c6" by="user" at="2026-09-10T15:44:39.737Z"}, connecting different pronominal projections with distribution and binding. Their proposal adds differences in pronominal projection to the comparison.

Rejecting a separate primary D needn’t preserve a unified determinative subcategory. Spinillo (2004) proposes redistribution among existing categories, retaining _the_, _a_ and _every_ as an expanded {==article category==}{>>basically D with a different name<<}{id="c7" by="user" at="2026-09-10T15:45:21.622Z"}. That proposal makes the restricted members a separate category; the D-noun analysis retains them inside the wider determinative subcategory.

For demonstratives and forms such as _some_ and _all_, Spinillo (2004, 140–44) rejects switching between determiner and pronoun categories according to whether a noun follows. She {==compares the alternation with verbs and prepositions used with or without a complement==}{>>a simplistic analogy that fails to account for much of the data<<}{id="c8" by="user" at="2026-09-10T15:46:29.862Z"}. The D-noun analysis agrees that the two uses needn’t involve different lexical categories. It differs in retaining determinative as the subcategory across those uses.

Van Eynde (2003) likewise rejects a separate determiner category, but assigns determining expressions to adjective or noun on morphological and agreement evidence, {==chiefly from Italian and Dutch==}{>>this paper is about English and rejects the idea of universal categories<<}{id="c9" by="user" at="2026-09-10T15:47:02.538Z"}. His analysis separates lexical category from the features governing determination. A noun-headed NP account therefore needn’t unify every determining expression as nominal.

Independent nominal use may support inclusion within Noun without selecting the pronoun subcategory. The demonstratives’ deictic properties make a pronominal grouping plausible; the question is how far that grouping captures the wider inventory’s {~~syntax~>syntactic, semantic, and morphological properties~~}{id="s8" by="user" at="2026-09-10T15:49:46.122Z"}. {==The comparisons below address modifier profiles (§3.3), the determinative–pronoun boundary (§5), and the positive connections linking restricted _every_ to other quantifiers (§6). Redistribution must be assessed against those connections as well as independence. The starting point is _CGEL_’s existing grounds for including distinct subcategories within Noun.==}{>>this seems too limited<<}{id="c10" by="user" at="2026-09-10T15:50:47.110Z"}
# 3 The D-noun analysis
## 3.1 The existing standard of nounhood
The starting category is Noun as _CGEL_ already constitutes it. Its discussion of pronouns makes the reasoning explicit: they differ from prototypical nouns in inflection and permitted dependents, but qualify because the phrases they head {~~have~>have almost complete overlap with~~}{id="s9" by="user" at="2026-09-10T15:52:05.978Z"} the {++syntactic++}{id="s10" by="user" at="2026-09-10T15:52:38.188Z"} functions {++(e.g., subject, object, determiner, etc.)++}{id="s11" by="user" at="2026-09-10T15:52:54.302Z"} of common- and proper-noun-headed phrases (Huddleston and Pullum 2002, 327). Table 2 compares the variation already accepted within that category with the proposed determinative extension.

Table 2: Typical profiles of _CGEL_’s three noun subcategories and the proposed fourth. Each has further lexical and constructional restrictions (Huddleston and Pullum 2002, 327–28, 373, 415–24, 425–30, 517–20). The text develops the genitive comparison.

| Dimension | Common noun | Proper noun | Pronoun | Determinative |
| :--- | :--- | :--- | :--- | :--- |
| Inventory | Open | Open to new names | Closed | Closed |
| Morphology | Number and genitive | Genitive; {++number (++}{id="s13" by="user" at="2026-09-10T15:54:17.649Z"}restricted{++)++}{id="s15" by="user" at="2026-09-10T15:54:23.309Z"} {--plurals--}{id="s14" by="user" at="2026-09-10T15:54:21.179Z"} | {--Personal-pronoun--}{id="s18" by="user" at="2026-09-10T15:56:58.382Z"} case {--paradigms--}{id="s19" by="user" at="2026-09-10T15:56:59.997Z"} | {--Demonstrative--}{id="s16" by="user" at="2026-09-10T15:55:11.488Z"} number; {++grade;++}{id="s17" by="user" at="2026-09-10T15:56:05.503Z"} genitive{~~-marked personal compounds~>(e.g., _something's_)~~}{id="s31" by="user" at="2026-09-10T16:28:43.733Z"} |
| Determination | Broad contrasts; singular count arguments normally require it | Restricted in primary naming uses | Normally excluded | Lexically restricted; _the few_, _these three_ |
| Internal modification | Productive {--AdjP and nominal modification--}{id="s20" by="user" at="2026-09-10T15:58:57.138Z"} | Restricted embellishments | Restricted: _poor old me_ | Restricted adverb premodifiers and {==nominal postmodifiers==}{>><<}{id="c12" by="user" at="2026-09-10T15:59:39.021Z"} |
| {++Complementation++}{id="s21" by="user" at="2026-09-10T15:59:56.162Z"} |     |     |     |     |

Common nouns supply the most familiar profile, but they don’t supply an entry test that every noun subcategory has to pass unchanged. Pronouns remain nouns despite their closed inventory and restricted modification; proper nouns remain nouns despite their distinct naming uses {++and resistance to dependents++}{id="s22" by="user" at="2026-09-10T16:00:28.399Z"}. An argument that excludes determinatives on these grounds therefore needs to explain why comparable differences warrant a primary-category boundary in this case.

Meaning and reference also vary within Noun. _Apple_ conveys a descriptive classification; _Kim_, in its primary naming use, identifies through a name; _she_ supplies limited descriptive content and depends on context. The quantificational or deictic contribution of a determinative therefore needs to be assessed alongside its grammar, rather than measured against common-noun semantics alone.

The distributional comparison follows _CGEL_’s pronoun argument: a range of determinatives occurs in subject, object and complement-of-preposition positions without another overt nominal head. The pattern recurs across lexemes and appropriate contexts, establishing systematic nominal use. The examples in §4.1 compare all four proposed subcategories in the same positions.

External distribution alone is insufficient: adjectival constructions such as _the rich_ also fill those positions. The further comparison concerns the breadth of independent use, number, determination, partitives and internal modification. Together these properties support a nominal subcategory profile. Restrictions on particular lexemes or readings remain part of the description, just as they do within the existing Noun category; §4.6 examines the predicative restrictions.

Extending the analysis to restricted members carries a separate burden. Pronoun forms themselves don’t all pass the argument-position test: dependent genitives such as _my_ have positive support from their paradigms. For determinatives, the argument likewise needs to establish both a broadly nominal constructional profile and the restricted members’ integration into that category. Section 6 supplies the latter argument.

The distinction at issue is thus one of taxonomic level. A closed inventory, reduced descriptive content or unusual modifier selection can establish a distinctive subcategory without establishing exclusion from Noun. The decisive comparison is whether the shared nominal behaviour and local differences are better captured by extending existing nominal structure or by preserving a separate primary D. Section 7.2 holds the lexical restrictions fixed to make that comparison explicit.

The D-noun analysis captures shared properties through inheritance: a property stated for a superordinate category is available to its subcategories, subject to stated restrictions. Determinatives therefore inherit nominal projection from Noun. Subcategory rules constrain combinatorics, and lexical entries distinguish such forms as independent _some_ and dependent-only _every_.
## 3.2 Noun phrases in determiner and argument functions
Determiner function already cuts across the existing noun subcategories. Compare _my_ {~~_book_~>preferences~~}{id="s23" by="user" at="2026-09-10T16:25:52.475Z"}, _Kim’s_ {~~_book_~>preferences~~}{id="s24" by="user" at="2026-09-10T16:25:55.404Z"} and {~~_the king’s book_~>_people's preferences_~~}{id="s25" by="user" at="2026-09-10T16:26:03.193Z"}. The determiner is an NP ultimately headed by a pronoun, a proper noun and a common noun respectively (Huddleston and Pullum 2002, 354–55, 470–71). {--In the last example, _the_ determines _king_ inside the genitive NP, while that whole NP determines _book_.--}{id="s26" by="user" at="2026-09-10T16:26:32.230Z"} Figure 2 illustrates the proper-noun case: _Kim’s_ fills Det, while {~~_book_~>_preferences_~~}{id="s27" by="user" at="2026-09-10T16:26:52.818Z"} ultimately heads the larger NP.

> Note 2. _CGEL_ assigns these genitives the combined function Subject–Det (Huddleston and Pullum 2002, 472–73). I treat them as Det here, without the additional subject function.

```text
NP ├── Det: NP[gen] │ └── Head: Nom │ └── Head: N_proper │ └── Kim's └── Head: Nom └── Head: N_common └── {~~book~>preferences~~}{id="s28" by="user" at="2026-09-10T16:27:02.716Z"}
```

Figure 2: The genitive NP _Kim’s_ functions as determiner within _Kim’s_ {~~_book_~>_preferences_~~}{id="s29" by="user" at="2026-09-10T16:27:10.627Z"}, ultimately headed by {~~_book_~>preferences~~}{id="s30" by="user" at="2026-09-10T16:27:22.271Z"}. The representation abstracts from the internal realization of genitive marking.

The compound determinative {++(cite Payne et al for this analysis)++}{id="s32" by="user" at="2026-09-10T16:30:07.268Z"} joins this pattern in _someone’s book_: its genitive NP fills the same determiner function. The nominal base in _someone_ may contribute to that permission{--;--}{id="s34" by="user" at="2026-09-10T16:30:55.234Z"}{++,++}{id="s35" by="user" at="2026-09-10T16:30:56.799Z"} {~~it doesn’t establish genitive marking throughout determinative~>and most determinatives resist case marking~~}{id="s36" by="user" at="2026-09-10T16:31:50.674Z"}.

The inherited projection gives the two D-noun structures in Figure 1. In _take some apples_, the NP headed by _some_ fills Det, as _Kim’s_ does in _Kim’s book_; _apples_ heads the larger NP. In _take some_, _some_ heads the whole object NP. The lexeme retains its subcategory and nominal projection across these uses, while the NP it heads changes function.

Shared projection doesn’t imply unrestricted interchangeability. The determiner construction selects a determinative-headed phrase, a suitable genitive NP, or another licensed expression. Number, countability and other selectional conditions further distinguish the determining expressions. Section 7.2 includes these restrictions in the comparison of grammars.
## 3.3 Modifier selection and taxonomic level
Shared nominal projection doesn’t make modifier permissions uniform. In _almost every experienced teacher_ (Figure 3), the AdvP _almost_ modifies the determinative noun _every_; the AdjP _experienced_ modifies the common noun _teacher_, which ultimately heads the outer NP.

```text
NP
├── Det: NP_D
│   └── Head: Nom
│       ├── Mod: AdvP
│       │   └── almost
│       └── Head: N_D
│           └── every
└── Head: Nom
    ├── Mod: AdjP
    │   └── experienced
    └── Head: N_common
        └── teacher
```

Figure 3: Two modifier relations in _almost every experienced teacher_: _almost_ modifies _every_, and _experienced_ modifies _teacher_. The outer NP has _teacher_ as its ultimate head. Internal structure within the one-word modifier phrases is suppressed.

Payne et al. (2010, 40–42) defend keeping _few_, _any_ and related forms in one lexical category across dependent and independent uses. In _hardly any money_ and independent _hardly any_, _hardly_ remains an adverb and _any_ retains its category. The D-noun analysis preserves that continuity. It also preserves their contrast between adverbial premodification, as in _almost anybody_, and adjectival postmodification, as in _nothing absolute_.

Payne et al. (2010, 60–61) also argue that distribution alone can’t decide whether adjectives and adverbs are inflectional variants of one category or derivationally related members of different categories. The D-noun analysis preserves distinct lexical subcategories and makes no inflectional-variant claim. Their methodological constraint still applies: shared positions alone don’t settle category status.

Modifier selection supports distinguishing determinatives from pronouns and common nouns. {++But it's also, perhaps, the strongest evidence against the whole D-noun analysis: Pre-head AdvP modifiers simply do not occur in the other three subcategories of Noun.++}{id="s37" by="user" at="2026-09-10T17:01:33.285Z"}{>>this probably needs adjustment for cohesion and coherence<<}{id="c13" by="user" at="2026-09-10T17:02:38.044Z" re="s37"} {++Consider, though, that post-head relative-clause modifiers are restricted to common nouns, though relative clause adjuncts appear elsewhere++}{id="s37" by="user" at="2026-09-10T17:01:33.285Z"} The further question is the taxonomic level of that distinction. Within the proposed Noun, the determinative subcategory licenses _hardly any_ and _almost every_; the common-noun subcategory licenses _experienced teacher_. Neither *_experienced every_ nor *_almost teacher_ follows. The existing modifier profiles remain, while their relation to the broader category changes; §7.3 considers the cost explicitly. Section 4 assesses the fuller constructional profile against the grounds on which _CGEL_ already includes distinct subcategories within Noun.
# 4 Evidence for nominal structure
Independent uses, partitives and modification show a recurring nominal pattern. These observations overlap: _Some left_ illustrates both external distribution and syntactic completeness. Fusion and ordinary headedness can cover this pattern. The comparisons below distinguish the shared observations from the analyses of their internal structure; §7.2 assesses the resulting organization of the grammar.
## 4.1 Breadth of independent use
Independent use is widespread within the determinative inventory. _CGEL_ discusses such uses for demonstratives and quantifiers including _some_, _all_, _both_, _many_, _few_, _several_, _each_, _either_, _neither_, _much_ and _enough_, while recording lexical restrictions and the separate forms _no_/_none_ (Huddleston and Pullum 2002, 371–72, 410–24). The generalization concerns the availability of independent constructions across a lexical category, not unrestricted acceptability in every sentence frame.

> Note 3. Material before a determiner falls outside the independent-use comparison. _CGEL_ treats _all_/_both_ in _all/both the books_ as predeterminer modifiers, _quite_/_rather_ before _a good idea_ as peripheral modifiers, and _such_/exclamative _what_ before _a disaster_ as adjectives (Huddleston and Pullum 2002, 433–37). The fixed _many a_ is a complex determinative restricted to Det function (Huddleston and Pullum 2002, 394). The _half_ in _half a cake_ is a common noun used as a predeterminer modifier (Huddleston and Pullum 2002, 434). These constructions don’t add evidence for independent determinative heads.

The pattern extends beyond a few compounds or a single lexicalized expression. For this closed category, productivity concerns the availability of independent use among established members under appropriate conditions, rather than the licensing of new lexical items.

In the constructed examples in (1), compare the positions occupied by the bracketed NPs: subject, object and complement of a preposition. Assume that a woman named Kim and a group of people are already under discussion. These positions admit NPs containing words from each proposed noun subcategory; the competing analyses assign different internal structures to independent _some_.

(1a) _[People] left._ — _I see [people]._ — _with [people]_

(1b) _[Kim] left._ — _I see [Kim]._ — _with [Kim]_

(1c) _[She] left._ — _I see [her]._ — _with [her]_

(1d) _[Some] left._ — _I see [some]._ — _with [some]_

Adjectival independent uses prevent a simple inference from these positions to nounhood. _The rich_ and _the poor_ can fill nominal argument positions. Comparative and superlative adjectives also head expressions without a human-class interpretation: _CGEL_’s _the most important of her criticisms_ is an NP containing a partitive _of_-phrase (Huddleston and Pullum 2002, 332–33, 416–23).

Independent _some_ can form a one-word NP, whereas an NP with _rich_ as fused head normally requires a determiner on the human-class reading. That is a local contrast: argument NPs headed by singular count common nouns also need determination. Section 4.4 returns to the fuller adjectival comparison.
## 4.2 Structural saturation and interpretation
With a group of people under discussion, _Some left_, _Many came_ and _All agree_ illustrate structural saturation: an argument expression can be syntactically complete without another overt head or determiner. Syntactic completeness differs from contextual interpretation. In _I’ll take some_, the relevant substance or set may be supplied by discourse or the situation. That dependence doesn’t establish a deleted common noun: ordinary pronouns also depend on context.

In the following attestation from the CGELBank treebank, _two different Honda models_ supplies the domain for the independent object _both_:

> Note 4. CGELBank (Reynolds et al. 2023), sentence `reviews-083459-0002`.

(2) _Went there yesterday: we are trying to decide between two different Honda models, so we wanted to test-drive both back to back._

Generalizing expressions such as _Many are called, few are chosen_ and _Enough is enough_ need no previously uttered common-noun phrase. They rule out a mandatory overt-antecedent requirement, but a silent-noun account could supply a generic restriction. Such examples don’t decide whether the restriction belongs in semantics or syntax.

The comparison with ordinary pronouns and proper nouns is structural as well as interpretive. In _She left_ and _Kim left_, _CGEL_ permits an NP headed by a nominal with no determiner. Applying that structure to _Some left_ preserves the same division between a complete NP and its context-dependent reference. The dependent use of _some_ doesn’t by itself require a Det function inside every independent occurrence.

Fusion supplies the competing analysis. In Payne et al. (2007), one constituent jointly realizes Head and a dependent function, subject to structural and adjacency conditions. In _CGEL_’s analysis of independent _some_, the DP headed by _some_ fills Det of NP and Head of Nom. The word retains the determinative category it has in _some apples_, while the independent expression is an NP. Ordinary headedness replaces this relation with nominal projection; lexical restrictions on independence and form selection remain.

_CGEL_ also uses fusion in noun-headed structures. It analyses _mine_ as fused Det–Head when it stands for a possessed entity in an anaphoric context, but as pure Head in the predicative possessive use _it’s mine_ (Huddleston and Pullum 2002, 410–11).

Saturation therefore clarifies the distributional comparison without independently selecting either internal structure.
## 4.3 Partitives locate the quantificational head
In _some of the wine_, _some_ specifies a quantity drawn from an identifiable amount of wine. The NP _the wine_ denotes the partitive domain: the whole from which that quantity is drawn. This NP is complement of _of_. A pronoun-headed NP or independent genitive NP can express the domain too: _many of them_, referring to previously mentioned people, or _some of Kim’s_, referring to Kim’s apples.

Compare where the common noun occurs in _some apples_ and _some of the wine_. In the partitive, _wine_ is embedded inside the _of_-phrase, so it can’t be the lexical head of the whole NP. The comparison instead concerns the head-like role of _some_ in that larger expression.

Figure 4 gives the D-noun analysis, with the _of_-phrase functioning as complement within Nom, as in _CGEL_’s partitive tree (Huddleston and Pullum 2002, 411–12). _CGEL_ represents the head-like role of _some_ through Det–Head fusion. Partitives support that role while leaving the choice between fusion and ordinary headedness open.

```text
NP
└── Head: Nom
    ├── Head: N_D
    │   └── some
    └── Comp: PP
        ├── Head: P
        │   └── of
        └── Comp: NP
            └── the wine
```

Figure 4: _Some of the wine_ under the D-noun analysis. The Head relations lead from the outer NP to _some_. The common noun _wine_ is inside the complement PP and doesn’t head the whole expression. The inner NP is abbreviated.

The overt quantifier and domain already supply a compositional interpretation of _some of the wine_. A silent common noun would need to explain something further, such as a restriction on interpretation or modification that the overt-head account misses. The construction itself supplies no such requirement. I therefore prefer an overt-head analysis over an otherwise equivalent null-head analysis; fusion remains compatible with that preference.

The D-noun analysis treats _some_ and _some of the wine_ as sharing nominal projection, with an added domain phrase in the partitive. Modification provides a further comparison of internal structure.
## 4.4 Modification tests the internal analysis
The pair _the lucky survivors_/_the lucky few_ supplies a comparison involving both external determination and adjectival modification. _CGEL_ explicitly permits determinatives used as internal modifiers to fuse with Head, as in _the other two_ and _these few here_ (Huddleston and Pullum 2002, 415–16). Its analysis of _the few mistakes_ assigns _the_ to Det and _few_ to Mod (Huddleston and Pullum 2002, 392). That dependent use supplies the counterpart for a Mod–Head analysis of independent _few_ after an external determiner.

Figure 5 compares the resulting analyses of _the lucky few_. Both have an overt Det and a Nom modified by _lucky_. In the D-noun analysis, _few_ fills Head. In the fusion analysis, its DP fills Mod–Head. The competing structure thus uses machinery already needed for adjectival fusion; it requires neither a silent noun nor conversion.

```text
NP
├── Det: NP_D
│   └── the
└── Head: Nom
    ├── Mod: AdjP
    │   └── lucky
    └── Head: N_D
        └── few
```

```text
NP
├── Det: DP
│   └── the
└── Head: Nom ───────────────┐
    ├── Mod: AdjP            │
    │   └── lucky            │
    └── Head: Nom            │
        └── Mod–Head: DP ◄───┘
            └── Head: D
                └── few
```

Figure 5: _The lucky few_ with ordinary Head (first tree) and Mod–Head fusion (second tree). The determiner is separately realized in both. Internal structure within the article phrase and AdjP is suppressed.

Table 3 compares the Head relations across four constructions; §7.2 supplies the rules under both taxonomies.

Table 3: Head and dependent functions under matched analyses. Each independent expression is an NP; _the_ fills Det wherever it appears. The ordinary-Head column applies to both taxonomies permitting ordinary determinative heads.

| Expression | Separate D with fusion | Ordinary determinative Head |
| :--- | :--- | :--- |
| _few survivors_ | _few_: Det; _survivors_: Head | Same functions |
| Independent _few_ | _few_: Det–Head | _few_: Head |
| _the lucky few_ | _few_: Mod–Head; _lucky_: Mod | _few_: Head; _lucky_: Mod |
| _the idle rich_ | _rich_: Mod–Head; _idle_: Mod | Same fusion and modifier functions |

Fusion groups _the lucky few_ with _the idle rich_, whereas ordinary headedness groups it with _the lucky survivors_. Ordinary headedness unifies _few_ across its bare and externally determined uses, without alternating Det–Head and Mod–Head. Neither account gains coverage from this example alone. The comparison is between sharing a fusion construction across D and adjective, and sharing ordinary nominal headedness across determinative constructions.

Reducing fusion’s applications can simplify this description even when fusion remains available for adjectives. The advantage is the uniform treatment of _few_; its value depends on any additional conditions or lost generalizations elsewhere. Section 7.2 compares those costs while holding the lexical restrictions fixed.

> Note 5. Compare the theory of second best in Lipsey and Lancaster (1956, 11–12): under a constraint preventing an optimum, satisfying more optimality conditions needn’t improve the outcome. The analogy concerns interactions among grammatical choices, not a formal optimum for the grammar.

The constructed _the remaining three_ extends the modifier pattern to cardinals. It doesn’t independently decide whether _three_ is determinative or has a common-noun use: Reynolds (2026) argues for both uses of cardinals. Section 7.3 treats their unification as a consequence conditional on that analysis.

Relative-clause postmodification adds another nominal construction: _those who came_, _anyone who asks_, _everything that matters_, and, with books under discussion, _some that I saw_. _CGEL_ describes relatives with demonstratives and compounds (Huddleston and Pullum 2002, 414, 422–23). These clauses modify the nominal expression containing the determinative, as they do in _people who came_; their availability isn’t limited to compounds.

Number supplies a further distinction between determinatives and adjectives. Independent _this_/_these_ and _that_/_those_ retain overt singular–plural contrasts. The human-class _the rich_, by contrast, is a plural NP whose adjective lacks nominal number inflection and still takes adverb modifiers: _the very rich_ (Huddleston and Pullum 2002, 418). The strongest morphological evidence comes from the demonstrative paradigms. The singular and plural specifications of _each_ and _several_ concern lexical restrictions; NP number alone doesn’t distinguish the categories. Other determinatives, such as plural or non-count _some_, remain number-neutral.

Bare colour expressions and evaluative comparative subjects complicate a simple distributional boundary. _CGEL_’s _Henrietta likes red shirts, and I like blue_ permits colour-noun ambiguity as well as possible reduction licensed by coordination; the attested _Bluer is better_ establishes a bare comparative subject without settling its phrase category. These cases leave the wider comparison of argument distribution and head properties necessary.

> Note 6. The _blue_, _old_ and _small_ examples on _CGEL_ p. 417 all occur in coordinated contrasts. _Bluer is better_ accompanies a results colour scale in Stanford CS329X, [“Codeswitching LLMs”](https://web.stanford.edu/class/cs329x/slides/Lecture12_B_Codeswitching%20LLMs.pdf), slide 8 (accessed 10 September 2026). I interpret it as evaluating a degree of blueness. Subject function alone doesn’t establish NP status (Huddleston and Pullum 2002, 236).

The positive comparison therefore combines independent argument use with nominal number properties, partitives and modification. Adjectival constructions provide overlapping external functions while preserving distinct properties of their heads. This favours retaining adjectival fusion alongside ordinary determinative headedness.
## 4.5 Compounds and modifier domains
A more demanding modifier comparison is _hardly anyone present_. Payne et al. (2007, 581–83) assign _hardly_ to DP structure and _present_ to nominal structure. The compound _anyone_ takes the premodifiers of its determinative base _any_: compare _hardly any writer present_. The adjective realizes a specialized restrictor function, restricted to post-head position and non-recursive. Figure 6 contrasts this account with an ordinary-Head analysis.

```text
NP
└── Head: Nom
    ├── Mod: AdvP
    │   └── hardly
    ├── Head: N_D
    │   └── anyone
    └── Mod: AdjP
        └── present
```

```text
NP ──────────────────────┐
└── Head: Nom            │
    ├── Det–Head: DP ◄───┘
    │   ├── Mod: AdvP
    │   │   └── hardly
    │   └── Head: D
    │       └── anyone
    └── Mod: AdjP
        └── present
```

Figure 6: _Hardly anyone present_ with ordinary Head (first tree) and fusion (second tree). Both post-head Mod positions realize the specialized restrictor. In the fusion tree, DP fills Det of NP and Head of Nom, following Payne et al. (2007, 582, (13d)). Modifier-phrase interiors are suppressed.

In the D-noun analysis, _anyone_ inherits nominal projection from Noun and its premodifier permissions from its determinative base. The compound construction supplies the post-head restrictor permission, with the same position and non-recursion conditions as the fusion account. It doesn’t license a corresponding pre-head adjective. The compound’s ordinary argument use and exclusion of external determination are further lexical conditions; the premodifier and restrictor slots aren’t unrestricted Nom dependents.

The relative clauses illustrated above are ordinary postmodifiers, distinct from the specialized restrictor. When both occur, the relative follows it: _something useful that I found_. _CGEL_ explicitly gives compounds the common noun’s range of ordinary postmodifiers while preserving this ordering condition (Huddleston and Pullum 2002, 423).

This division extends to _someone_ and _everybody_: the compound family licenses nominal argument use and post-head restrictors, while each base supplies its own premodifier permissions. It doesn’t follow that _hardly_ modifies every compound. CGELBank attests the post-head pattern in _I need something reliable and good looking_.

> Note 7. Sentence `answers-20111024111513AAAQhAO_ans-0003` in `ewt-test_iaa50.cgel`.

Fusion reuses the DP–Nom boundary to separate the two modifier domains. Ordinary headedness reuses nominal projection, locating both domains within Nom and assigning their restrictions to the determinative base and compound construction. Both accounts need the specialized restrictor condition. The trade-off concerns where the restrictions are stated, not whether they can be removed.
## 4.6 Predicative uses and their restrictions
The argument-use patterns above don’t extend uniformly to predicative complementation. _CGEL_ records _Its advantages are several_ and _Their enemies were many_, describing the latter pattern as uncommon and formal (Huddleston and Pullum 2002, 392, 395–96). Predicative use is available to only part of the determinative inventory; _every_ and the articles remain excluded from these frames.

The comparison also depends on what the predication expresses. _She is a doctor_ ascribes a property, whereas _That is Kim_ identifies a person. _CGEL_ excludes specifying _be_ clauses from its noun–adjective diagnostic because phrases from other categories occur in them too (Huddleston and Pullum 2002, 536). Merely placing an expression after _be_ therefore provides no uniform nounhood test.

Nominal grammar already licenses some expressions predicatively while restricting their argument uses. A bare-role NP such as _president_ is licensed in _I’d like to be president_, but requires determination in the corresponding object use _I’d like to meet the president_ (Huddleston and Pullum 2002, 328). Predicative and argument uses thus need separate conditions within Noun itself. The determinative asymmetries belong in that comparison; they don’t establish exclusion merely by departing from a common-noun substitution frame.
## 4.7 What the combined pattern supports
Independent uses, number, genitives, partitives and modification establish a systematic nominal profile. The properties are distributed across determinative families, just as the existing noun subcategories differ in inflection and dependents. This is the positive basis for extending _CGEL_’s membership rationale beyond pronouns.

Under the D-noun analysis, bare, partitive and externally determined uses inherit the ordinary Head relation of nominal projection. _CGEL_ instead relates independent determinatives to dependent counterparts and distinguishes Det–Head from Mod–Head. Its compound analysis also uses the DP–Nom boundary to separate modifier domains. The D-noun analysis states those restrictions within nominal structure (§4.5).

The next two sections consider the hierarchy within Noun and the membership of its restricted forms. Section 7.2 then compares the grammatical organization under the three accounts.
# 5 Coordinate subcategories and inheritance
Should determinatives and pronouns be coordinate subcategories within Noun, or should determinatives belong inside pronoun? Reynolds (2021) compares determinative and pronoun profiles; its matrix contains no common or proper nouns. Distributional separation between the supplied groups doesn’t determine their taxonomic rank or test the proposed superordinate category. Even perfect recovery of the distinction would be compatible with shared nounhood. The original discussion likewise leaves a nested nominal analysis open.

The accompanying audit reproduces the published DISCO decomposition, but the clustering outcome varies with initialization and feature selection.

> Note 8. The accompanying [_Replication audit of the English determinative–pronoun feature matrix_](../matrix-audit.pdf) documents the discrepancy between the reported 232 features and the public 155-feature file, an extra feature dropped by the published clustering code, and the sensitivity results. The archived public file is retained unchanged.

The pronoun inventory in that study follows _CGEL_’s classification, whereas Hudson’s pronoun category includes the words he calls determiners. Comparing these hierarchies requires aligning their lexical inventories and asking which generalizations can be stated for each superordinate category.

An intermediate pronoun-plus-determinative category would be useful if it collected generalizations otherwise repeated. Within the proposed grammar, nominal projection rules apply to all four subcategories, so they can be stated for Noun as a whole. The intermediate category would need additional generalizations. Different property profiles alone don’t favour coordination: a subtype can differ sharply from the rest of its superordinate category. Core personal pronouns’ case, reflexive and person contrasts, and determinatives’ quantificational and modifier patterns, support local distinctions under either hierarchy.

Reduced descriptive content and contextual interpretation are shared by many pronouns and determinatives. The coordinate analysis can record these interpretive properties through features or cross-classification; they don’t by themselves require an intermediate lexical category.

Pro-form gender supplies a more specific interpretive comparison. Reynolds (2025) proposes a personhood-based system spanning pronouns and determinatives. Personal reference links pronouns such as _she_ with compound determinatives such as _somebody_; non-personal reference links _it_ with _something_. These constraints concern how the referent is construed. They provide a shared generalization for nominal pro-forms, but don’t decide between coordinate and nested noun subcategories. The broader pro-form system also includes non-nominal expressions, so gender alone doesn’t delimit Noun.

Restrictions on determination and attributive modification provide syntactic candidates, but they also occur outside the proposed grouping. In their primary use, proper names don’t select freely from the determiner system, and their adjectival embellishments are restricted (Huddleston and Pullum 2002, 517, 519–20). These properties distinguish more than pronouns and determinatives from common nouns.

Determination also differs within the proposed intermediate category. Determinatives permit external determination in a range of independent quantificational constructions: _the few_, _the many_, _the two_, _these three_. The permissions vary by item and often require further modification; _CGEL_ gives _these few here_ and _the many who did_ (Huddleston and Pullum 2002, 415–16). Pronouns admit external determination only marginally, and internal premodification is restricted, as in _poor old me_ (Huddleston and Pullum 2002, 429–30). These restrictions thus cross-cut the proposed grouping and vary within it.

I place determinative alongside pronoun because the shared projection can be stated at Noun, while the contrasts in inflection, modification and determination are described within the two subcategories. The broader pronoun category doesn’t capture an additional syntactic generalization in these comparisons. Further syntactic generalizations over that category could favour nesting. Section 6 turns to the membership of the articles and other restricted forms.
# 6 The articles and other restricted members
Why classify the articles _the_ and _a_ as nouns if they can’t stand independently? Independent uses motivate the D-noun analysis of _some_, _this_ and _many_, but the articles require a different argument. _Every_ is restricted too, while _no_ has the distinct independent form _none_ (Huddleston and Pullum 2002, 371–72, 410–11).

> Note 9. The restriction concerns ordinary argument use. In _the bigger the better_, _CGEL_ analyses _the_ as a modifier within a comparative phrase (Huddleston and Pullum 2002, 1131–32, 1135–36). This dependent use outside Det leaves the restriction on ordinary argument use intact.

_CGEL_’s treatment of _my_ supplies a precedent for restricted membership within Noun (Huddleston and Pullum 2002, 470–71). The pronoun’s paradigm supports its membership despite its lack of _mine_’s independent distribution. For articles, the corresponding positive evidence is integration into determinative; their nounhood depends on the category-level argument.

Retaining a restricted member requires three kinds of support. First, it should be paradigmatically integrated with independently identified members. Second, it should participate in the category’s characteristic semantic and grammatical contrasts. Third, its missing uses should form a local restriction while the positive connections remain. Calling an item defective summarizes that pattern; it doesn’t supply an argument for membership by itself.

The articles meet these conditions within determinative. First, they contrast with demonstratives and quantifiers before common-noun nominals: _the/a/this/every book_. Second, they participate in the same system of definiteness, number and count restrictions: _the_ permits singular, plural and non-count targets, while _a_ selects a singular count target. Third, their lack of ordinary independent uses leaves that determining pattern intact. These connections support determinative membership, rather than establishing nounhood independently.

_Every_ has further connections beyond the restricted article set proposed by Spinillo (2004). Like _each_, it expresses universal quantification and selects singular count nominals: _every teacher_, _each teacher_. Unlike _each_, it lacks ordinary independent use. It also permits modification by _almost_ and _nearly_. These connections support retaining _every_ with the quantifiers.

The argument for retaining the articles is synchronic. Grammaticalization supplies background: Lyons (1999, 331–36) discusses the development of definite articles from demonstratives and of articles expressing cardinality from numerals. These histories can explain changes in content and use, but don’t establish the synchronic classification.

A separate article category would gain support from a cluster of synchronic restrictions shared by _the_, _a_ and _every_, absent elsewhere in Noun, and otherwise requiring repeated exceptions. Lack of independent argument use alone doesn’t supply that cluster. The comparison concerns the allocation of generalizations; an additional restriction needn’t by itself overturn the membership analysis. All the grammars compared in §7.2 retain the articles’ restriction on ordinary argument use.
# 7 Shared projection and grammatical economy
## 7.1 A shared phrase type in determiner function
In _some apples_ and _Kim’s apples_, the determining phrases share the NP category under both ordinary-Head accounts: D-noun and separate D. _CGEL_ instead distinguishes DP from genitive NP. It also admits a restricted range of plain-case NPs and PPs as determiners, as in _what size hat_ and _over thirty ties_ (Huddleston and Pullum 2002, Ch. 5, §4). The phrase types are:

```text
CGEL:  Det:{DP,NP,PP}
Both ordinary-Head accounts:  Det:{NP,PP}
```

This shares a phrase type without shortening the selectional disjunction: determinative-headed, genitive and other licensed NPs still require separate identification. _CGEL_ already states definiteness and the single-Det restriction functionally, so reclassification doesn’t derive them. The substantive comparison concerns whether determining phrases reuse nominal projection once their different restrictions are held fixed. Fewer phrase labels alone don’t establish grammatical economy; §7.2 displays the rules that must be compared.
## 7.2 A matched descriptive fragment
A grammatical fragment is a set of rules for a specified range of constructions. Here it covers determination, ordinary subject and object uses, partitives, and the modifier and compound comparisons in §4. It compares the D-noun analysis with two separate-D alternatives: ordinary headedness and fusion. All receive the same lexical restrictions and constructed judgments. The predicative constructions in §4.6 fall outside the fragment.

Table 4 records use permissions: whether a form, on a given reading, can head a phrase in determiner, subject or object function. Argument use covers the subject and object NPs in examples such as _Some left_ and _I saw some_. Quotation, metalinguistic naming and subordinate-clause uses of dependent genitives fall outside the fragment. Noun membership doesn’t itself grant a use permission.

Table 4: Shared permissions in the fragment. For _some_, the target column concerns its unstressed use before a noun. The inventory is deliberately limited to the displayed constructions.

| Form | Det use | Argument use | Target in the Det construction |
| :--- | :---: | :---: | :--- |
| _the_ | yes | no  | Singular or plural; count or non-count |
| _a_, _every_ | yes | no  | Singular count nominal |
| _some_ | yes | yes | Plural count or non-count nominal |
| _few_ | yes | yes | Plural count nominal |
| _my_ | yes | no  | No number/count restriction in this fragment |
| _she_ | no  | yes | None |

Further constructional restrictions apply: _she_ is a subject form, whereas the corresponding ordinary object form is _her_. The target restrictions concern the common-noun nominal being determined: _a_ requires a singular count target such as _book_ in _a book_.

Table 5 locates the three accounts. Comparing the ordinary-Head accounts holds projection fixed while varying taxonomy. Comparing the separate-D accounts holds taxonomy fixed while varying headedness.

Table 5: Three accounts retaining the permissions in Table 4, the modifier restrictions and the compound conditions.

| Account | Primary taxonomy | Simple independent determinative |
| :--- | :--- | :--- |
| D-noun analysis | D inside Noun | N–Nom–NP projection with Head function |
| Separate D, ordinary Head | D outside Noun | D–Nom–NP through cross-category projection |
| _CGEL_: separate D, fusion | D outside Noun | NP distribution through Det–Head |

The D-noun analysis applies nominal projection to determinatives through their membership in Noun. A separate condition checks use permissions. In the schemata below, `h` identifies the lexical head throughout its projection; parentheses mark optional dependents. The subscripts on Mod distinguish pre-head and post-head positions of the same modifier function. The head’s entry and construction restrict every dependent.

```text
Nom_h → (Mod_pre)  Head:N_h  (Comp)  (Mod_post)
NP_h → (Det)  Head:Nom_h
licensed(NP_h,f,c)  ⇔  f∈ U_h\ ∧\ C_h(f,c)
```

Here `U_h` is the head’s set of use permissions, `f` is the NP’s function, and `C_h` checks the lexical and constructional conditions in context `c`. For Det use, these include compatibility with the target nominal; for an argument headed by a singular count common noun, they include required determination. Optionality in the second rule doesn’t override those conditions.

In _some apples_, _some_ heads an NP whose Det permission and plural-count target requirement are satisfied. _Apples_ heads the outer Nom, which heads the NP. In _Some left_, _some_ heads an NP whose argument permission is satisfied. _Every apple_ passes the Det and singular-count checks; ordinary independent *_Every arrived_ fails the argument-permission check. _The apple_ and *_The arrived_ differ in the same way.

Each NP’s use permissions follow its own head. In _the apple_, the article’s Det permission licenses the dependent NP headed by _the_. The outer NP takes its argument permission from _apple_, whose requirement for determination is satisfied by the article.

A singular count common noun such as _book_ faces a different restriction from an article. In _a book_, its requirement for determination is satisfied; bare *_Book arrived_ leaves that requirement unsatisfied. _Books arrived_ has no such requirement. Requiring determination for a common noun doesn’t itself block an article-headed NP from argument use. An article’s exclusion from argument use must still be stated separately.

Partitives and modifiers require further lexical conditions. _Some_ and _few_ permit a partitive _of_-phrase within their nominal projection. _Almost_ can modify _every_ in _almost every teacher_; that permission doesn’t license _experienced_ as a modifier of _every_. The construction _the lucky few_ permits the external determiner and adjectival modifier shown in Figure 5. None of these permissions transfers automatically to every determinative noun.

Keeping ordinary headedness while retaining primary D gives the strongest separate-D alternative. It retains the NP and use-permission rules, but replaces the lexical-head restriction in Nom with:

```text
Nom_h→(Mod_pre)  Head:{N_h,D_h}  (Comp)  (Mod_post)
```

This projection applies to dependent as well as independent determinatives, eliminating DP from the fragment while retaining primary D. Determiner selection still identifies D-headed NPs and suitable genitives. In _the lucky few_, _few_ is D in ordinary Head function. In _hardly anyone present_, the determinative base and compound construction supply the same modifier restrictions as the D-noun account. Adjectival Mod–Head fusion remains available in both.

The separate-D fusion account relates independent determinatives to their dependent counterparts. In addition to nominal projection for nouns, it uses DP projection and permits a DP to realize a fused function in nominal structure. The partitive complement and compound restrictor belong to Nom, following the trees in _CGEL_ and Payne et al. (2007, 582):

```text
DP_h → (Mod_pre)  Head:D_h  (Comp)
Nom_h → (Mod_pre)  F:DP_h  (Comp)  (Mod_post)
F∈{Det–Head,Mod–Head}
```

The ordinary NP rule embeds this Nom. Det–Head jointly realizes Det of NP and Head of Nom, excluding a second Det; Mod–Head fills an internal modifier’s function and Head of Nom, allowing external determination. Lexical and constructional conditions select the fused function and permitted dependents. These schemata cover independent _few_, _few of them_, _the lucky few_ and _hardly anyone present_.

The ordinary-Head accounts thus share nominal projection and Head relations; these benefits don’t uniquely favour inclusion within Noun. Dependent determinatives acquire a Nom layer in both. The taxonomic difference lies in whether the lexical head enters this structure by inheritance from Noun or by a rule admitting both N and D.

A grammar with Hudson’s nested classification can use the same permissions and projection rules. Holding those rules fixed, placing the broader pronoun category on determinative’s inheritance path from Noun leaves the fragment’s judgments unchanged. Agreement on these judgments leaves the broader pronoun category open.
## 7.3 Existing restrictions, additional costs and consequences
The remaining taxonomic choice is between inheritance through Noun and a projection rule spanning N and D. Separate D preserves the modifier contrast as a primary-category distinction while licensing nominal projection across that boundary. D-noun makes projection an inherited property and states the modifier contrast within Noun.

The cost of this change needs separating from restrictions already present in the grammar. Common nouns, proper nouns and pronouns already differ in determination and permitted modifiers (Table 2). Preserving those conditions is no additional cost of including determinatives. Likewise, the separate-D grammar already restricts adverbial modification and independent use within D. Moving those restrictions inside Noun doesn’t create them.

Payne et al. (2010, 75, n. 3) analyse _almost_ as a modifier of the attributive noun _textbook_ in _an almost textbook case_. The D-noun analysis extends such premodification to a systematic noun subcategory, including _hardly any_ and _almost every_. Its cost is stating the usual modifier contrast at that subcategory boundary. In compounds, the inherited premodifier permissions must also be distinguished from the post-head restrictor construction (§4.5).

Why should systematic nominal projection warrant inclusion for pronouns but require cross-category licensing for determinatives? I favour placing the recurring external and structural profile at Noun, with modifier and use restrictions at the subcategories and constructions that distinguish them. This applies the existing membership rationale consistently.

The comparison can be extended by fixing the same inventory, constructions and readings for both grammars, then asking which additional rules each needs after common restrictions have been factored out. Inheritance gains support if further constructions reuse nominal rules that an independently motivated D-specific analysis has to state separately. Separate D gains support if its boundary captures recurring structural restrictions that inclusion in Noun has to restate across constructions. Counting independent uses alone doesn’t settle this: either grammar can state the same permissions positively or as exceptions.

Cardinals illustrate the reduction in overlap between primary categories. Reynolds (2026) distinguishes determinative uses such as _ten men_, proper-noun uses such as _Room 101_, and common-noun uses such as _tens of pens_. Under the D-noun analysis, these uses fall within Noun: cardinals no longer span separate primary determinative and noun categories. Their differences remain at the subcategory and construction levels. The argument doesn’t extend to ordinals, which that study analyses as adjectives, or turn complex numeral phrases into single lexemes.

Complex cardinals also separate category from function. In _two hundred books_, the whole _two hundred_ fills Det; internally, _two_ modifies the magnitude head _hundred_ (Reynolds 2026, sec. 4). In _these two hundred books_, _these_ fills Det and _two hundred_ is an internal modifier. Including determinatives within Noun preserves these relations. One Det function doesn’t entail a limit of one determinative lexeme per NP.

If determinative-headed and genitive expressions require different projection rules after their independently motivated restrictions are held fixed, the shared-projection proposal in §7.1 loses its advantage. That would favour separate phrase types. Retaining a separate primary D requires the further case that the category boundary captures the recurring differences better than a determinative subcategory within Noun.
# 8 Conclusion
I propose four coordinate subcategories of Noun in English: common noun, proper noun, pronoun and determinative. Across independent uses, partitives and modification, the analysis gives determinatives shared nominal structure while retaining their lexical and constructional restrictions, including those of the articles. _CGEL_ already admits pronouns on comparable grounds despite differences in inflection and dependents. The D-noun analysis extends that membership rationale.

Coordination locates the shared projection at Noun and the contrasting permissions within its subcategories. The broader pronoun category doesn’t add a syntactic generalization in the comparisons examined here, though further evidence could favour it.

Through membership in Noun, determinatives inherit the Head relations that unify their bare, partitive and externally determined uses. A separate-D grammar can also license that projection. The taxonomic choice concerns inheritance through Noun versus cross-category licensing. I favour inheritance because it extends _CGEL_’s rationale for pronoun membership, with the modifier contrast stated within Noun. Shared nominal structure belongs at the superordinate category; differing permissions remain at subcategory and construction levels.
# Data and analysis materials
The accompanying supplements are [_Replication audit of the English determinative–pronoun feature matrix_](../matrix-audit.pdf) and [_CGELBank concordance and extraction notes_](../corpus-documentation.pdf). The `analysis/` directory preserves their input files, provenance records, scripts, numerical outputs and sentence concordance. Its README identifies the files and reproduction procedures.

Acknowledgements. For the September 2026 revision, GPT-6 (Astra), Claude Opus 5, Claude Haiku 4.5 and GLM-5.3-Flash assisted drafting, source retrieval, script development or critical review; GPT-5.6 (Sol) checked numerical outputs. The accompanying materials record the tools and their uses. Responsibility for the analysis is mine.
# References
Abney, Steven P. 1987. “The English Noun Phrase in Its Sentential Aspect.” PhD thesis, Massachusetts Institute of Technology.

Anderson, John M. 1997. _A Notional Theory of Syntactic Categories_. Cambridge Studies in Linguistics 82. Cambridge University Press. <https://doi.org/10.1017/CBO9780511519734>.

Bruening, Benjamin. 2020. “The Head of the Nominal Is N, Not D: N-to-D Movement, Hybrid Agreement, and Conventionalized Expressions.” _Glossa: A Journal of General Linguistics_ 5 (1). <https://doi.org/10.5334/gjgl.1031>.

Déchaine, Rose-Marie, and Martina Wiltschko. 2002. “Decomposing Pronouns.” _Linguistic Inquiry_ 33 (3): 409–42. <https://doi.org/10.1162/002438902760168554>.

Huddleston, Rodney, and Geoffrey K. Pullum. 2002. _The Cambridge Grammar of the English Language_. Cambridge University Press. <https://doi.org/10.1017/9781316423530>.

Huddleston, Rodney, Geoffrey K. Pullum, and Brett Reynolds. 2022. _A Student’s Introduction to English Grammar_. 2nd ed. Cambridge University Press. <https://doi.org/10.1017/9781009085748>.

Hudson, Richard. 2004. “Are Determiners Heads?” _Functions of Language_ 11 (1): 7–42. <https://doi.org/10.1075/fol.11.1.03hud>.

Hudson, Richard. 2010. _An Introduction to Word Grammar_. Cambridge University Press.

Lipsey, R. G., and Kelvin Lancaster. 1956. “The General Theory of Second Best.” _The Review of Economic Studies_ 24 (1): 11–32. <https://doi.org/10.2307/2296233>.

Lyons, Christopher. 1999. _Definiteness_. Cambridge University Press. <https://doi.org/10.1017/cbo9780511605789>.

Lyons, John. 1968. _Introduction to Theoretical Linguistics_. Cambridge University Press. <https://doi.org/10.1017/CBO9781139165570>.

Palmer, Harold E. 1924. _A Grammar of Spoken English on a Strictly Phonetic Basis_. W. Heffer & Sons Ltd.

Payne, John, Rodney Huddleston, and Geoffrey K. Pullum. 2007. “Fusion of Functions: The Syntax of _Once_, _Twice_ and _Thrice_.” _Journal of Linguistics_ 43 (3): 565–603. <https://doi.org/10.1017/S002222670700477X>.

Payne, John, Rodney Huddleston, and Geoffrey K. Pullum. 2010. “The distribution and category status of adjectives and adverbs.” _Word Structure_ 3 (1): 31–81. <https://doi.org/10.3366/E1750124510000486>.

Postal, Paul M. 1966. “On so-Called “Pronouns” in English.” In _Report of the Seventeenth Annual Round Table Meeting on Linguistics and Language Studies_, edited by Francis P. Dinneen. Monograph Series on Languages and Linguistics 19. Georgetown University Press.

Pullum, Geoffrey K., and Philip Miller. 2022. _NPs Versus DPs: Why Chomsky Was Right_. LingBuzz 006845. <https://lingbuzz.net/lingbuzz/006845>.

Pullum, Geoffrey K., and Deirdre Wilson. 1977. “Autonomous Syntax and the Analysis of Auxiliaries.” _Language_ 53 (4): 741–88. <https://doi.org/10.2307/412911>.

Reynolds, Brett. 2021. “Quantifying the Differences Between Lexical Categories: The Case of Pronouns and Determinatives in English.” _Cadernos de Linguística_ 2 (3). <https://doi.org/10.25189/2675-4916.2021.V2.N3.ID399>.

Reynolds, Brett. 2025. “Personhood and Pro-Forms: A Hierarchical Analysis of Gender in Modern English.” Unpublished manuscript.

Reynolds, Brett. 2026. “The Lexicon–Syntax Boundary in English Numerals: Cardinals, Ordinals, and Fractionals.” _English Language and Linguistics_, 1–19. <https://doi.org/10.1017/S1360674325100518>.

Reynolds, Brett, Aryaman Arora, and Nathan Schneider. 2023. “Unified Syntactic Annotation of English in the CGEL Framework.” In _Proceedings of the 17th Linguistic Annotation Workshop (LAW-XVII)_, edited by Jakob Prange and Annemarie Friedrich. Association for Computational Linguistics. <https://doi.org/10.18653/v1/2023.law-1.22>.

Sommerstein, Alan H. 1972. “On the so-Called Definite Article in English.” _Linguistic Inquiry_ 3 (2): 197–209. <https://www.jstor.org/stable/4177701>.

Spinillo, Mariangela Galvão. 2004. “Reconceptualising the English Determiner Class.” {PhD} thesis, University College London. <https://discovery.ucl.ac.uk/id/eprint/10101595/>.

Van Eynde, Frank. 2003. “On the Notion ‘Determiner’.” In _Proceedings of the 10th International Conference on Head-Driven Phrase Structure Grammar_, edited by Stefan Müller. CSLI Publications. <https://doi.org/10.21248/hpsg.2003.22>.
