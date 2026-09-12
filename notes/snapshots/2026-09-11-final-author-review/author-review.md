# Determinatives as nouns in English
Brett Reynolds — 11 September 2026 working draft

Complete revision following your annotations and the question about _what_. Trees and schemata are shown as text; footnotes appear beside their paragraphs. [Typeset PDF](../determinatives-as-nouns.pdf) · [Response to all review points](./passes/2026-09-11-complete-revision.md).
# Abstract
I argue that English determinatives belong within Noun alongside common nouns, proper nouns, and pronouns. Their combined semantic, syntactic, and morphological profile supports the grouping; quantificational common nouns provide particularly close connections. Adverbial premodification and grade distinguish determinatives within it. I examine restricted articles, reconsider independent _what_’s pronoun classification, and address determinatives’ degree-modifier uses. The proposed hierarchy makes nominal projection inherited, unifying bare, partitive, and externally determined uses under ordinary Head structure. A matched grammatical fragment compares separate-D alternatives and identifies the costs of restricting modifier generalizations to subcategories.

**Keywords:** determinatives, nouns, lexical categories, noun phrases, English
# 1 The question
What is the categorial relationship among words such as _some_, _me_, _apple_, and _Brett_? I argue that all four are nouns: determinatives form a coordinate subcategory alongside common nouns, proper nouns, and pronouns. I write the superordinate category as Noun and call the fourfold proposal the determinative-noun or D-noun analysis.

I adopt the general framework of _The Cambridge grammar of the English language_ (_CGEL_; Huddleston and Pullum 2002). Unlike _CGEL_, though, I include determinatives within Noun. The claims concern synchronic English lexical categories.

> Note 1. I treat these categories as language-specific: a classification supported by another language’s grammar doesn’t determine the English classification.

I use determinative for the category containing articles, demonstratives, and quantifiers such as _the_, _this_, _some_, _every_, and _many_. I reserve determiner for the syntactic function within the noun phrase characteristically performed by phrases headed by these words. This distinction separates what kind of word _some_ is from what syntactic relationships its phrase participates in.

> Note 2. For a fuller inventory, see the online [“List of determinatives in English”](https://www.cambridge.org/highereducation/api/resources/2AC8DF5CA558F8A6FCDFACD0EAF8EA08) accompanying Huddleston et al. (2022).

_CGEL_ already includes pronouns within Noun on the basis of their phrases’ functions, despite differences from common and proper nouns in inflection and dependents (Huddleston and Pullum 2002, 327–28). The inclusion of auxiliaries within Verb supplies a further precedent for preserving distinctive properties within a broader lexical category (Pullum and Wilson 1977). The question is whether determinatives’ combined semantic, syntactic, and morphological profile warrants the corresponding extension of Noun.

In the D-noun analysis, determinatives inherit the nominal projection rules of Noun. Under these rules, a determinative heads a nominal (Nom), which heads an NP, just as common nouns, proper nouns, and pronouns do. Nom contains the head and its internal dependents, excluding an external determiner. Lexical restrictions govern which uses are available.

Figure 1 compares _CGEL_ with the D-noun analysis for _take some apples_ and _take some_. Both keep _some_ in one lexical category. In _CGEL_, independent _some_ jointly fills determiner and head functions, a fusion of functions (Huddleston and Pullum 2002, 410–12). In the D-noun analysis, _some_ heads its own NP through a Nom in both uses; that NP functions as determiner before _apples_ and as object in _take some_.

> Note 3. As a syntactic representation, fusion of functions appears to have seen little adoption outside work based on _CGEL_.

Here DP abbreviates determinative phrase, as in _CGEL_, not to be confused with the DP of the DP hypothesis, where D heads the whole expression _some apples_ (Abney 1987; §2.1). The D-noun analysis keeps _apples_ as that expression’s ultimate head.

CGEL: take some apples

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

CGEL: take some

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

Figure 1: The first pair shows _CGEL_; the second pair shows the D-noun analysis. Each pair compares _take some apples_ with _take some_. In the second tree, DP fills Det of NP and Head of Nom. In the third and fourth trees, _some_ heads an NP through the same `N_D`–Nom–NP sequence; that NP functions as Det in the third tree and Obj in the fourth.

The same ordinary Head structure extends to bare _few_, partitive _few of them_, and externally determined _the lucky few_. _CGEL_ divides these between Det–Head and Mod–Head fusion. Their unification is one structural consequence of the {++D-noun++}{id="s1" by="user" at="2026-09-11T21:05:33.761Z"} proposal. Another is that replacing DP with NP consolidates the phrase types functioning as determiner: determinatives join genitives and other nominal determiners.

The argument proceeds from {==classification==}{>>we don't use class, classify, or classification for this<<}{id="c1" by="user" at="2026-09-11T21:11:17.404Z"} to its consequences. Section 2.2 places the proposal among earlier accounts; §3 compares the four profiles, and §4 examines the nominal constructions. Sections 5 and 6 address subcategory rank and difficult members. The matched fragment in §7.2 then compares the resulting grammar with separate-D alternatives, holding judgments and lexical restrictions fixed.
# 2 {~~Classification~>Categorization~~}{id="s2" by="user" at="2026-09-11T21:11:06.680Z"}, headedness, and function
## 2.1 Category, function, and phrase structure
Lexical categories and syntactic functions cut across one another. An NP can function as determiner, as in _Kim’s book_, and a determinative-headed phrase can function as modifier, as in _the many people_ (Payne et al. 2010; Pullum and Miller 2022).

The question of lexical classification is distinct from the headedness question associated with the DP hypothesis of Abney (1987). Under that hypothesis, D heads expressions such as _some apples_. I retain noun-headed NPs and reject the DP analysis for English, following the arguments of Pullum and Miller (2022) and Bruening (2020).

Category membership doesn’t remove lexical restrictions. _Every apple_ is grammatical, but *_I’ll take every_ isn’t an ordinary way to accept apples. The fragment retains that restriction (§7.2).
## 2.2 Taxonomic and structural alternatives
Keeping a word in one category across dependent and independent uses leaves its taxonomic position open. As Lyons (1968, 232–35) observes, distribution can be compared at different levels of categorization: two expressions may belong together at one level and differ at a more specific level. Table 1 distinguishes the selected authors’ proposals, their analytical levels, and several logical alternatives. The D-noun analysis differs from _CGEL_ by including determinative within Noun, and from Hudson by placing it alongside pronoun.

Table 1: Selected accounts and logical alternatives. The earlier proposals differ in scope and representational level; they don’t all specify a surface taxonomy. The prose gives sources and inventory qualifications.

| Account | Proposed relationship | Level or status |
| :--- | :--- | :--- |
| Palmer | Determinative adjectives grouped with pronouns. | Lexical grouping; inclusive Noun unspecified |
| Postal | Personal pronouns analysed as articles, with deeper noun features. | Intermediate and underlying representations |
| Sommerstein | Definite article and personal pronouns given NP structure. | Underlying representation |
| Lyons | Articles, demonstratives, and personal pronouns linked by definiteness and deixis. | Semantic relationship |
| _CGEL_ | Pronoun within Noun; determinative separate. | Lexical taxonomy |
| Hudson | Determiners within pronoun, which is within noun. | Lexical taxonomy |
| Spinillo | Determinatives redistributed; _the_, _a_, and _every_ retained as articles. | Lexical reclassification |
| D-noun analysis | Common noun, proper noun, pronoun, and determinative coordinate within Noun. | Proposed taxonomy |
| Logical alternative | Noun, pronoun, and determinative separate. | For comparison |
| Logical alternative | Determinative within Noun; pronoun separate. | For comparison |
| Logical alternative | Pronoun within determinative, which is within Noun. | For comparison |
| Logical alternative | Pronoun within proper noun; determinative within common noun. | For comparison |

Palmer (1924, 24) proposed placing “determinative adjectives” with pronouns. He contrasted them with qualifying adjectives, which permit predicative use, comparison, and adverbial modification. Most determinatives, he observed, can “be used indifferently as pronouns or as modifiers of nouns”. Lyons (1968, 279) adds a semantic connection: articles, demonstratives, and personal pronouns share definiteness and deictic contrasts.

Postal (1966) develops the article–pronoun connection through English reflexives and combinations such as _we men_. His morphological evidence for the noun _self_ includes _selfish_, _selfless_, and the plural alternation _self_/_selves_; he analyses the preceding pronominal material as an article. The classification depends on representational level: article segments occur at intermediate stages, their deepest counterparts are features of nouns, and surface pronouns can receive derivative Noun status.

Sommerstein (1972, 197–203) argues in the opposite direction, giving the definite article and personal pronouns underlying NP structure. His English comparison includes the count restriction on anaphoric _one_, whereas _it_ can refer to a quantity of a substance. He also observes that noun status for _self_ doesn’t decide whether the preceding element is an article or a genitive pronoun.

> Note 4. Payne et al. (2013, 797–98) analyse anaphoric _one_ as a common count noun, distinct from determinative _one_ and personal pronoun _one_.

These predecessors challenge a fundamental article–pronoun separation, but leave the full determinative inventory unclassified. Its contrasts in grade, modification, complementation, and restricted independent use extend the comparison beyond their proposals.

Hudson makes taxonomic inclusion explicit. His noun category contains common noun, proper noun, and pronoun (Hudson 2010, 253–54); a determiner is a pronoun whose valency permits the relevant common-noun dependent (Hudson 2004, 9–10). The word’s category remains constant across independent and dependent uses, which differ in their permitted dependents.

Hudson’s criteria centre on licensing a singular count common noun and on mutual exclusion in that use. He sets aside _all_, cardinal numerals, and quantifiers restricted to plural or non-count nouns (Hudson 2004, 9–10). Their place in his taxonomy remains unsettled by those criteria. Extending the pronoun analysis to _CGEL_’s fuller inventory requires comparing its modifier selection, grade, and quantitative meanings with the existing pronouns’ properties.

Hudson also distinguishes dependency from external headedness. He argues that determiner and common noun depend on each other, although only one connects the phrase to its surroundings (Hudson 2004, 7–8). His temporal adjunct evidence supports common-noun headedness: _I saw him that day_ is possible, whereas *_I saw him that point in time_ isn’t, despite the similar temporal meanings (Hudson 2004, 10–12). The lexical noun matters, as well as the construction’s determiner restrictions.

The reciprocal selection facts are substantial: a singular count noun normally requires determination, while _every_ requires an overt nominal and _some_ doesn’t. They establish conditions in both directions. In the present phrase-structure analysis, the noun can remain Head while both constituents impose such conditions (§7.2). Including determinatives within Noun neither explains away the selection facts nor requires mutual headedness; it concerns the selecting words’ superordinate category.

Spinillo (2004, 153–58) instead retains _the_, _a_, and _every_ as an expanded article category and redistributes other determinatives {++among ...++}{id="s3" by="user" at="2026-09-11T21:16:37.932Z"}. Her grounds include dependence on a following nominal, lack of predicative and partitive uses, and limited descriptive content. She also recognizes differences within the {++article++}{id="s4" by="user" at="2026-09-11T21:16:57.489Z"} trio. Section 6 assesses this cluster against the connections each member retains with the wider inventory.

Spinillo (2004, 140–44) draws an analogy with verbs and prepositions whose complements can be omitted. For demonstratives and quantifiers such as _some_ and _all_, occurrence before a nominal (_some teachers_) alternates with occurrence without one (_some left_). The analogy supports category continuity, but leaves the category to be established: _CGEL_, Hudson, and the D-noun analysis can all preserve it.
# 3 The D-noun analysis
## 3.1 The basis for a broader Noun category
Table 2 compares the four proposed subcategories. The issue is the combined profile: how broadly a property occurs within each group, where it recurs across constructions, and how specifically it connects determinatives with nouns or adjectives.

Table 2: Representative profiles, with ranges rather than universal properties. Argument and Det functions concern whole phrases; modifier examples involve Nom or NP as appropriate. Construction type is distinct from function. The determinative inventory includes the reassignment of independent _what_ and relative _which_ argued for in §6.2.

| Dimension | Common noun | Proper noun | Pronoun | Determinative |
| :--- | :--- | :--- | :--- | :--- |
| Inventory | Open | Open to new names | Closed | Closed |
| Argument / Det functions | NP arguments; genitive Det | NP arguments; genitive Det | NP arguments; genitive Det | NP arguments; plain and genitive Det |
| Modifier / adjunct functions | _dog houses_; _that day_ | _Canada Day_; _Sunday_ | Emphatic reflexives in both functions | _the few people_; degree adjuncts |
| Interrogative / relative constructions | Through another constituent, e.g. _which book_ | Through another constituent | _who_, _whose_ | _which_, _what_, and _-ever_ forms |
| Meaning | Descriptive properties and relations | Naming in primary uses | Person, deixis, anaphora, and interrogation | Quantification, definiteness, deixis, and interrogation |
| Pro-form gender | Descriptions shape referent construal | Names identify referents construed by gender | Gender-sensitive forms | Gender-sensitive forms and constructions |
| Inflection | Number and genitive | Genitive; restricted number | Case, including genitive; reflexive forms | Number; grade; genitive; _no_/_none_ |
| Accepts determination | Broad contrasts; singular count arguments normally require it | Restricted in primary naming uses | Normally excluded | Lexically restricted: _the few_, _these three_ |
| Internal modification | Productive AdjP and nominal premodifiers; relative postmodifiers | Restricted AdjP premodifiers and embellishments | Restricted AdjP premodifiers and relative postmodifiers | AdvP and D premodifiers; nominal postmodifiers; _the lucky few_ |
| Complementation | Selected PPs and clauses | Not characteristic of primary naming uses | Normally absent | Partitive _of_-PPs; comparative _than_-phrases |

Meaning and reference vary within Noun. _Apple_ describes a class; _Kim_, in its primary naming use, identifies through a name; _she_ depends on context. Determinatives range from deictic _this_ to quantitative _many_ and universal _every_ (Huddleston and Pullum 2002, 358–60, 370–405, 425–28, 515–21). Deixis connects demonstratives with pronouns, while quantity connects determinatives with common nouns such as _number_ and _majority_.

These meanings aren’t exclusive to nouns. Adjectives such as _singular_ and _plural_ also concern number; _proximate_ and _distal_ describe spatial relations relevant to demonstrative contrasts, though spatial meaning needn’t itself be deictic. Nor does Noun imply close semantic similarity throughout: _every_ quantifies over a nominal restriction, while _Kim_ identifies an individual. Semantic affinities contribute to the comparison without settling its boundaries.

Pro-form gender (Reynolds 2025) connects these ways of referring. Descriptions such as _the woman_ and names such as _Kim_ identify referents whose construal bears on pro-form choice. Pronouns and determinatives express contrasts between personal _she_/_somebody_ and non-personal _it_/_something_. Relative _who_/_which_ supplies another contrast; independent _what_ raises a classification question taken up in §6.2.

External syntax supplies a broad overlap in the functions available to the phrases. _CGEL_ makes this the stated ground for including pronouns within Noun (Huddleston and Pullum 2002, 327). A range of determinatives likewise occurs in subject, object, and complement-of-preposition positions without another overt nominal head. The examples in §4.1 compare these uses across all four proposed subcategories.

Modifier and adjunct functions also cut across the groups. Compare the modifiers in _dog houses_, _Canada Day_, _the manager herself_, and _the few people_. Emphatic _herself_ also functions as a clause adjunct in _The manager detected the error herself_ (Huddleston and Pullum 2002, 1496–97). Temporal NPs such as _that day_ and _Sunday_ supply adjuncts, as does degree _enough_ in _I hadn’t prepared enough_ (§6.3). These are shared functions with construction-specific distributions.

Interrogative, relative, and exclamative properties must be distinguished from those functions. An interrogative object may be headed by a pronoun (_who_) or a common noun (_which book_); the latter obtains its interrogative property from a dependent. {==Similarly, _What a nice day!_ requires exclamative _what_; substituting an ordinary NP doesn’t preserve the construction. _CGEL_ classifies this _what_ as an adjective, distinct from interrogative and relative _what_ (Huddleston and Pullum 2002, 433–37; Ch. 10, §7).==}{>>yes, I'd forgotten that was an adjective. Perhaps it's not relevant here?<<}{id="c2" by="user" at="2026-09-11T22:41:19.248Z"}

Overlap with adjectives likewise needs phrase levels kept distinct. Both _the people_ and _the rich_ are NPs in _CGEL_, though only the former has a noun as lexical head. In _a soccer/round ball_, Nom and AdjP share modifier function; in _Jones became president/ill_, NP and AdjP share predicative complement function. External functions alone therefore don’t establish nounhood.

Complementation sharpens the comparison. Common nouns and determinatives take partitive complements: _a lot/some of the wine_. Comparative complements such as _more than ten_ instead connect determinatives with adjectives (Huddleston and Pullum 2002, 349–50, 392–94, 411–12, 432–33). Common nouns permit PP and clausal complements more generally; pronouns and primary naming uses of proper nouns have much more restricted dependents (Huddleston and Pullum 2002, 429–30, 439–43, 517–21). Determinatives combine nominal complement and postmodifier constructions with their own selectional restrictions.

Quantificational common nouns make the connection more specific than shared quantity meanings. In _a lot of the delegates_ and _many of the delegates_, both heads quantify over a partitive domain. Yet _lot_ permits _a lot of delegates_, whereas *_many of delegates_ is excluded. _CGEL_ also classifies _plenty_ as a common noun whose quantificational use resists determination and modification (Huddleston and Pullum 2002, 349–50). Established common nouns thus approach the determinative profile as determinatives approach theirs.

Ordinary count nouns alone are consequently an inadequate comparison class. Quantificational common nouns already combine selected _of_-complements with restricted dependents. Determinatives extend this pattern within Noun, adding the broad specialization in plain-case Det and the premodifier contrast examined in §3.3.

Inflection supplies overlapping contrasts too. Common nouns inflect for number and genitive; proper nouns permit number distinctions in restricted uses. Pronouns distinguish case, including genitive, and reflexive forms. Within determinative, _this_/_these_ shows number, _few_/_fewer_/_fewest_ grade, and _something’s_ genitive (Huddleston and Pullum 2002, 373, 423–24, 426, 479–80, 521). Number and case connect parts of the inventory with nouns; grade connects another part with adjectives.

_CGEL_ treats singular and plural _you_ as distinct lexemes whose difference is overt only in the reflexive forms _yourself_ and _yourselves_ (Huddleston and Pullum 2002, 486). Here number distinguishes lexemes rather than inflectional forms of one lexeme.

The adjectival affinities likewise vary across the inventory. Grade connects _few_, _many_, _much_, and _little_ with adjectives, and their comparative forms take _than_-complements. Predicative use extends to _several_, and AdvP premodification extends much further. Even the gradable forms have distinct syntax: _so many mistakes_ contrasts with *_so numerous mistakes_ (Huddleston and Pullum 2002, 392–96, 539–40).

The case for inclusion rests on this distribution of connections. Determinatives share argument and determiner functions with all three noun subcategories, referential contrasts with pronouns, and number, genitive marking, and partitive constructions with established parts of Noun. Adverbial premodification is a broad counterweight; grade and comparative complementation connect a smaller set with adjectives. I give greater weight to the recurring nominal profile, while preserving those countervailing properties in the determinative subcategory.

The D-noun analysis captures shared properties through inheritance: a property stated for a superordinate category is available to its subcategories, subject to stated restrictions. Determinatives therefore inherit nominal projection from Noun. Subcategory rules constrain combinatorics, and lexical entries distinguish such forms as independent _some_ and dependent-only _every_.
## 3.2 Noun phrases in determiner and argument functions
Determinatives’ characteristic determiner use could support a separate primary category. But Det is itself specific to NP structure, where it marks definiteness and often contributes quantification (Huddleston and Pullum 2002, 354–59). These tasks connect it with the reference and number properties compared above. The question is whether this specialization warrants a primary boundary within nominal grammar.

Determiner function already cuts across the existing noun subcategories. Compare _my preferences_, _Kim’s preferences_, and _people’s preferences_. The determiner is an NP ultimately headed by a pronoun, a proper noun, and a common noun respectively (Huddleston and Pullum 2002, 354–55, 470–71). Figure 2 illustrates the proper-noun case.

> Note 5. _CGEL_ assigns these genitives the combined function Subject–Det (Huddleston and Pullum 2002, 472–73). I treat them as Det here, without the additional subject function.

```text
NP
├── Det: NP[gen]
│   └── Head: Nom
│       └── Head: N_proper
│           └── Kim's
└── Head: Nom
    └── Head: N_common
        └── preferences
```

Figure 2: The genitive NP _Kim’s_ functions as determiner within _Kim’s preferences_, ultimately headed by _preferences_. The representation abstracts from the internal realization of genitive marking.

The compound determinative _someone_, following the classification of Payne et al. (2007, sec. 1.3), joins this pattern in _someone’s preferences_: its genitive NP fills the same determiner function. The nominal base in _someone_ may contribute to that permission, and most determinatives resist case marking.

The NP headed by _some_ likewise functions as Det in _take some apples_ and as object in _take some_ (Figure 1). Its subcategory and nominal projection remain constant across these uses.

NP becomes the shared phrase type for the principal realizations of determiner function. Plain determinatives, including modified forms such as _almost ten_ {++_apples_++}{id="s5" by="user" at="2026-09-11T22:50:31.195Z"}, join genitives such as _Kim’s_ and _my_{==.==}{>>this may not be the spot for it, but it just occurred to me that AdvPs won't premodify within a Nom, but they will premodify an NP as in Usually a careful driver, Anne found her mind wandering; For almost my entire life; Almost my age at nineteen, he was the only sensible male in the family<<}{id="c3" by="user" at="2026-09-11T22:51:30.355Z"}{>>Ah, looks like 3.3 is the place<<}{id="c4" by="user" at="2026-09-11T23:22:27.093Z" re="c3"} Minor determiners include further NPs: _what size_ in _what size shoes_, _that size_ in _that size shoes_, and _Sunday_ in _Sunday morning_ (Huddleston and Pullum 2002, 356).

These existing NP determiners give the extension a functional basis. In _Kim’s preferences_, the embedded NP supplies an identifying anchor through its own referent; _Sunday_ and _what size_ specify a day or a dimension. Determinatives’ deictic and quantitative specifications fit this nominal pattern. I take that fit to support treating their specialization in Det as a distinction within Noun.

PPs remain a restricted alternative, as in _up to twenty minutes_ and _between fifty and sixty tanks_ (Huddleston and Pullum 2002, 356). Number, countability, and other selectional conditions distinguish the determining expressions.
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

Payne et al. (2010, 40–42) defend keeping _few_, _any_, and related forms in one lexical category across dependent and independent uses. In _hardly any money_ and independent _hardly any_, _hardly_ remains an adverb and _any_ retains its category. The D-noun analysis preserves that continuity. It also preserves their contrast between adverbial premodification, as in _almost anybody_, and adjectival postmodification, as in _nothing absolute_{==.==}{>>hardly one to be ignored, she ...<<}{id="c5" by="user" at="2026-09-11T23:24:51.681Z"}

The systematic use of AdvP premodifiers is the strongest internal-syntactic objection to the D-noun analysis. In the other three noun subcategories, internal premodifiers are normally adjectival or nominal. Adverbs occurring before a whole NP, as in _only you_, are peripheral modifiers of the NP, rather than internal modifiers of its head (Huddleston and Pullum 2002, 430–31){==.==}{>>is there an argument for pre-head modifiers in "DP" being peripheral too under the D-noun analysis?<<}{id="c6" by="user" at="2026-09-11T23:25:48.643Z"}

Determinatives also permit determinative premodifiers, as in _this much_ (Huddleston and Pullum 2002, 393). Under the proposed analysis, this is a{++n NP++}{id="s7" by="user" at="2026-09-11T23:27:29.676Z"} {--noun--}{id="s6" by="user" at="2026-09-11T23:27:27.983Z"} modify{++er++}{id="s9" by="user" at="2026-09-11T23:27:41.963Z"}{--ing--}{id="s8" by="user" at="2026-09-11T23:27:41.064Z"} {++in++}{id="s10" by="user" at="2026-09-11T23:27:44.712Z"} another {~~noun~>NP~~}{id="s11" by="user" at="2026-09-11T23:27:47.155Z"}{==.==}{>>consider also *A day* more and I couldn't have born it; *a lot* fewer<<}{id="c7" by="user" at="2026-09-11T23:27:58.034Z"} Its licensing remains specific: the availability of one determinative modifier doesn’t license arbitrary nominal premodification.

Payne et al. (2010, 42–47) establish that adverbs can postmodify common nouns {++(the changes globally to the climate)++}{id="s12" by="user" at="2026-09-11T23:30:46.768Z"}, and they analyse _almost_ as modifying the attributive {--noun--}{id="s13" by="user" at="2026-09-11T23:31:14.796Z"}{++nominal++}{id="s14" by="user" at="2026-09-11T23:31:18.016Z"} _textbook_ in _an almost textbook case_ (Payne et al. 2010, 75, n. 3). {==Adverbial modification therefore isn’t categorically excluded from Noun==}{>>nice find! I had forgotten this.<<}{id="c8" by="user" at="2026-09-11T23:30:09.459Z"}. But neither postmodification nor a restricted attributive use removes the systematic contrast between _hardly any_ or _almost every_ and ordinary common-noun premodification.

Postmodifier permissions vary within Noun too. Common nouns freely take integrated relative clauses; personal pronouns permit a restricted range, including _we who have read the report_ (Huddleston and Pullum 2002, 430). Compound determinatives permit them too, as in _something that you need to know_ (Huddleston and Pullum 2002, 423–24). {++(also few who come ever leave; many who; those who; that which; two that I have seen, etc.)++}{id="s15" by="user" at="2026-09-11T23:36:26.391Z"}

Including determinatives places the premodifier contrast within Noun. The determinative subcategory licenses _hardly any_ and _almost every_; common nouns license _experienced teacher_. Neither *_experienced every_ nor *_almost teacher_ follows. This contrast weighs against the grouping; §7.3 examines its consequences for stating the rules.
## 3.4 Word formation and category boundaries
Derivation supplies a less uniform comparison than {==inflection==}{>>does inflection not bear a whole subsection?<<}{id="c11" by="user" at="2026-09-11T23:42:47.796Z"}. Noun-forming suffixes differ in the bases they select: _-ship_ in _friendship_ primarily selects nouns denoting persons, though _hardship_ has an adjective base; the inhabitant suffix _-er_ in _Londoner_ attaches to a place name (Huddleston and Pullum 2002, Ch. 19, §§5.6.2(b), 5.7.2(k)). No noun-selecting suffix shared by pronouns and determinatives is established here.

Determinatives enter derivations whose output is a common noun. _CGEL_ cites _nothingness_ and _oneness_ among formations with _-ness_ on non-adjectival bases (Huddleston and Pullum 2002, Ch. 19, §5.7.2(i)). Further established nouns include _thisness_, _fewness_, and _muchness_.

> Note 6. See _Merriam-Webster.com Dictionary_, s.vv. [_thisness_](https://www.merriam-webster.com/dictionary/thisness) and [_fewness_](https://www.merriam-webster.com/dictionary/fewness), and _Dictionary.com_, s.v. [_muchness_](https://www.dictionary.com/browse/muchness) (accessed 10 September 2026). These attestations don’t establish a uniformly productive modern rule.

_-ness_ is the default suffix for forming nouns from adjectives, but also attaches to other bases, as in _whyness_ (Huddleston and Pullum 2002, Ch. 19, §5.7.2(i)). It therefore doesn’t settle the input category of _nothingness_. A conversion analysis would require independent evidence for an intermediate base.

The adverb _mostly_ provides a different output. Adverbial _-ly_ primarily attaches to adjectives, but _CGEL_ also gives noun-based _partly_ and _purposely_ (Huddleston and Pullum 2002, 566). This gives _most_ an adjectival affinity without an adjective-only diagnostic.

> Note 7. See _Dictionary.com_, s.v. [_mostly_](https://www.dictionary.com/browse/mostly) (accessed 10 September 2026).

Pronouns enter gender-marking compounds such as _he-goat_ and _she-ass_ (Huddleston and Pullum 2002, Ch. 19, §5.3); determinatives combine with nominal material in _someone_ and _anything_. Their determinative premodifier permissions recur in the compounds (§4.5), while the nominal component contributes further properties.

{==Numeral morphology extends the comparison to ordinal and fractional formations, analysed respectively as adjectival and nominal by Reynolds (2026). Their formation also bears on the boundary between a numeral lexeme and a syntactic phrase.==}{>>this doesn't make sense, I think. Read that paper of mine.<<}{id="c9" by="user" at="2026-09-11T23:40:59.339Z"}

{==Morphology==}{>>but we've only talked about derivational morphology.<<}{id="c10" by="user" at="2026-09-11T23:41:51.766Z"} supplies mixed evidence: number and genitive marking give the clearest inflectional connections with nouns, while grade gives an adjectival connection. Derivation links some determinatives with common nouns through suffixes whose typical bases are adjectival.
# 4 Evidence for nominal structure
Independent uses, partitives, and modification show a recurring nominal pattern. The observations overlap: _Some left_ illustrates both external distribution and syntactic completeness. Fusion and ordinary headedness offer different internal analyses of these constructions.
## 4.1 Breadth of independent use
Independent use is widespread within the determinative inventory. _CGEL_ discusses such uses for demonstratives and quantifiers including _some_, _all_, _both_, _many_, _few_, _several_, _each_, _either_, _neither_, _much_, and _enough_, while recording lexical restrictions and the separate forms _no_/_none_ (Huddleston and Pullum 2002, 371–72, 410–24). The generalization concerns the availability of independent constructions across a lexical category, not unrestricted acceptability in every sentence frame.

> Note 8. Material before a determiner falls outside the independent-use comparison. _CGEL_ treats _all_/_both_ in _all/both the books_ as predeterminer modifiers, _quite_/_rather_ before _a good idea_ as peripheral modifiers, and _such_/exclamative _what_ before _a disaster_ as adjectives (Huddleston and Pullum 2002, 433–37). The fixed _many a_ is a complex determinative restricted to Det function (Huddleston and Pullum 2002, 394). The _half_ in _half a cake_ is a common noun used as a predeterminer modifier (Huddleston and Pullum 2002, 434). These constructions don’t add evidence for independent determinative heads.

In the constructed examples in (1), compare the {==bracketed==}{>>brackets should always be upright<<}{id="c12" by="user" at="2026-09-11T23:44:10.799Z"} NPs as subjects, objects, and complements of prepositions. Assume that a woman named Kim and a group of people are already under discussion. The competing analyses assign different internal structures to independent _some_.

(1a) _[People] left._ — _I see [people]._ — _with [people]_

(1b) _[Kim] left._ — _I see [Kim]._ — _with [Kim]_

(1c) _[She] left._ — _I see [her]._ — _with [her]_

(1d) _[Some] left._ — _I see [some]._ — _with [some]_

{--Adjectival--}{id="s16" by="user" at="2026-09-11T23:45:17.444Z"}{>><<}{id="c13" by="user" at="2026-09-11T23:45:01.091Z"} independent use {++of AdjP++}{id="s17" by="user" at="2026-09-11T23:45:21.780Z"}s prevent{++s++}{id="s18" by="user" at="2026-09-11T23:45:51.063Z"} a simple inference from these positions to nounhood. _The rich_ and _the poor_ can fill nominal argument positions. Comparative and superlative adjectives also head expressions without a human-class interpretation: _CGEL_’s _the most important of her criticisms_ is an NP containing a partitive _of_-phrase (Huddleston and Pullum 2002, 332–33, 416–23).

Independent _some_ can form a one-word NP, whereas an NP with _rich_ as fused head normally requires {==a determiner==}{>>it's gotta be "the", doesn't it?<<}{id="c14" by="user" at="2026-09-12T00:02:08.851Z"} on the human-class reading. That is a local contrast: argument NPs headed by singular count common nouns also need determination. Section 4.4 returns to the fuller adjectival comparison.
## 4.2 Structural saturation and interpretation
With a group of people under discussion, _Some left_, _Many came_, and _All agree_ illustrate structural saturation: an argument expression can be syntactically complete without another overt head or determiner. Syntactic completeness differs from contextual interpretation. In _I’ll take some_, the relevant substance or set may be supplied by discourse or the situation. That dependence doesn’t establish a deleted common noun: ordinary pronouns also depend on context.

In the following attestation from the CGELBank treebank, _two different Honda models_ supplies the domain for the independent object _both_:

> Note 9. CGELBank (Reynolds et al. 2023), sentence `reviews-083459-0002`.

(2) _Went there yesterday: we are trying to decide between two different Honda models, so we wanted to test-drive_ {==_both_==}{>>not sure that it has a place in this paper but both, neither, and either function as markers of coordination<<}{id="c15" by="user" at="2026-09-12T00:30:51.268Z"} _back to back._

Generalizing expressions such as _Many are called, few are chosen_ and _Enough is enough_ need no previously uttered common-noun phrase. They rule out a mandatory overt-antecedent requirement, but a silent-noun account could supply a generic restriction. Such examples don’t decide whether the restriction belongs in semantics or syntax. {++Among the pronouns: _one shouldn't judge_.++}{id="s19" by="user" at="2026-09-12T00:31:50.833Z"}

The comparison with ordinary pronouns and proper nouns is structural as well as interpretive. In _She left_ and _Kim left_, _CGEL_ permits an NP headed by a nominal with no determiner. Applying that structure to _Some left_ preserves the same division between a complete NP and its context-dependent reference. The dependent use of _some_ doesn’t by itself require a Det function inside every independent occurrence.

In Payne et al. (2007), one constituent jointly realizes Head and a dependent function, subject to structural and adjacency conditions. Under _CGEL_’s analysis of independent _some_, its DP fills Det of NP and Head of Nom. The word remains determinative, while the independent expression is an NP. Ordinary headedness instead gives _some_ nominal projection, with the same restrictions on independence and form selection.

_CGEL_ also uses fusion with nouns. {==It assigns anaphoric _mine_ to Det–Head, but predicative possessive _mine_, as in _it’s mine_, to pure Head==}{>>what's the motivation for this?<<}{id="c16" by="user" at="2026-09-12T00:34:26.214Z"} (Huddleston and Pullum 2002, 410–11). Nounhood is thus compatible with fusion. Here ordinary determinative headedness follows from the inherited projection rules; the analysis of independent genitives, including _Kim’s_ and _mine_, falls outside the fragment in §7.2.
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
## 4.4 Modification tests the internal analysis
The pair _the lucky survivors_/_the lucky few_ supplies a comparison involving both {++an++}{id="s21" by="user" at="2026-09-12T00:35:54.485Z"} external determin{++er++}{id="s23" by="user" at="2026-09-12T00:35:58.001Z"}{--ation--}{id="s22" by="user" at="2026-09-12T00:35:56.833Z"} and {~~adjectival modification~>an attributive-modifier AdjP~~}{id="s20" by="user" at="2026-09-12T00:35:48.846Z"}. _CGEL_ explicitly permits determinatives used as internal modifiers to fuse with Head, as in _the other two_ and _these few here_ (Huddleston and Pullum 2002, 415–16). Its analysis of _the few mistakes_ assigns _the_ to Det and _few_ to Mod (Huddleston and Pullum 2002, 392). That dependent use supplies the counterpart for a Mod–Head analysis of independent _few_ after an external determiner.

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

Fusion groups _the lucky few_ with _the idle rich_; ordinary headedness groups it with _the lucky survivors_ and unifies bare and externally determined _few_. Both cover the example. The choice is between sharing fusion across D and adjective, and sharing ordinary Head structure across determinative constructions.

Reducing fusion’s applications can simplify this description even when fusion remains available for adjectives. The advantage is the uniform treatment of _few_; its value depends on any additional conditions or lost generalizations elsewhere. Section 7.2 compares those costs while holding the lexical restrictions fixed.

> Note 10. Compare the theory of second best in Lipsey and Lancaster (1956, 11–12): under a constraint preventing an optimum, satisfying more optimality conditions needn’t improve the outcome. The analogy concerns interactions among grammatical choices, not a formal optimum for the grammar.

The constructed _the remaining three_ extends the modifier pattern to cardinals. It doesn’t independently decide whether _three_ is determinative or has a common-noun use: Reynolds (2026) argues for both uses of cardinals. Section 7.3 treats their unification as a consequence conditional on that analysis.

Relative-clause postmodification adds another nominal construction: _those who came_, _anyone who asks_, _everything that matters_, and, with books under discussion, _some that I saw_. _CGEL_ describes relatives with demonstratives and compounds (Huddleston and Pullum 2002, 414, 422–23). These clauses modify the nominal expression containing the determinative, as they do in _people who came_.

Number supplies a further distinction between determinatives and adjectives. Independent _this_/_these_ and _that_/_those_ retain overt singular–plural contrasts. The human-class _the rich_, by contrast, is a plural NP whose adjective lacks nominal number inflection and still takes adverb modifiers: _the very rich_ (Huddleston and Pullum 2002, 418). The strongest morphological evidence comes from the demonstrative paradigms. The singular and plural specifications of _each_ and _several_ concern lexical restrictions; NP number alone doesn’t distinguish the categories. Other determinatives, such as plural or non-count _some_, remain number-neutral.

Bare colour expressions and evaluative comparative subjects complicate a simple distributional boundary. _CGEL_’s _Henrietta likes red shirts, and I like blue_ permits {--colour-noun ambiguity as well as--}{id="s24" by="user" at="2026-09-12T00:44:45.524Z"} possible reduction licensed by coordination; {++blue is good is ambiguous between adjective and nouns, and++}{id="s25" by="user" at="2026-09-12T00:45:13.375Z"} the attested _Bluer is better_ establishes a bare comparative subject without settling its phrase category. These cases leave the wider comparison of argument distribution and head properties necessary.

> Note 11. The _blue_, _old_, and _small_ examples on _CGEL_ p. 417 all occur in coordinated contrasts. _Bluer is better_ accompanies a results colour scale in Stanford CS329X, [“Codeswitching LLMs”](https://web.stanford.edu/class/cs329x/slides/Lecture12_B_Codeswitching%20LLMs.pdf), slide 8 (accessed 10 September 2026). I interpret it as evaluating a degree of blueness. Subject function alone doesn’t establish NP status (Huddleston and Pullum 2002, 236).

The combination of argument use, nominal number properties, partitives, and modification favours ordinary determinative headedness alongside adjectival fusion.
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
NP ──────────────────────┐ └── Head: Nom │ ├── Det–Head: DP ◄───┘ │ ├── Mod: AdvP │ │ └── hardly │ └── Head: D │ └── anyone └── Mod: AdjP {==└──==}{>>the branching in the tree should go straight down, not to the west<<}{id="c17" by="user" at="2026-09-12T00:46:11.888Z"} present
```

Figure 6: _Hardly anyone present_ with ordinary Head (first tree) and fusion (second tree). Both post-head Mod positions realize the specialized restrictor. In the fusion tree, DP fills Det of NP and Head of Nom, following Payne et al. (2007, 582, (13d)). Modifier-phrase interiors are suppressed.

In the D-noun analysis, _anyone_ inherits nominal projection from Noun and its premodifier permissions from its determinative base. The compound construction supplies the post-head restrictor permission, with the same position and non-recursion conditions as the fusion account. It doesn’t license a corresponding pre-head adjective. The compound’s ordinary argument use and exclusion of external determination are further lexical conditions; the premodifier and restrictor slots aren’t unrestricted Nom dependents.

The relative clauses illustrated above are ordinary postmodifiers, distinct from the specialized restrictor. When both occur, the relative follows it: _something useful that I found_. _CGEL_ explicitly gives compounds the common noun’s range of ordinary postmodifiers while preserving this ordering condition (Huddleston and Pullum 2002, 423).

This division extends to _someone_ and _everybody_: the compound family licenses nominal argument use and post-head restrictors, while each base supplies its own premodifier permissions. CGELBank attests the post-head pattern in _I need something reliable and good looking_.

> Note 12. Sentence `answers-20111024111513AAAQhAO_ans-0003` in `ewt-test_iaa50.cgel`.

Fusion reuses the DP–Nom boundary to separate the two modifier domains. Ordinary headedness locates both within Nom, assigning their restrictions to the determinative base and compound construction. Both accounts need the specialized restrictor condition.
## 4.6 Predicative uses and their restrictions
_CGEL_ records predicative _Its advantages are several_ and _Their enemies were many_, describing the latter pattern as uncommon and formal (Huddleston and Pullum 2002, 392, 395–96). This use is available to only part of the determinative inventory; _every_ and the articles remain excluded.

_She is a_ {~~_doctor_~>beauty~~}{id="s26" by="user" at="2026-09-12T00:49:11.632Z"} ascribes a property, whereas _That is Kim_ identifies a person. _CGEL_ excludes specifying _be_ clauses from its noun–adjective diagnostic because phrases from other categories occur in them too (Huddleston and Pullum 2002, 536).

Nominal grammar also distinguishes predicative and argument uses. A bare-role NP such as _president_ is licensed in _I’d like to be president_, but requires determination in the corresponding object use _I’d like to meet the president_ (Huddleston and Pullum 2002, 328). Determinatives’ asymmetries fit this broader variation within Noun.
## 4.7 What the combined pattern supports
The nominal constructions reinforce the semantic and morphological connections in §3. Under the D-noun analysis, bare, partitive, and externally determined uses inherit ordinary Head structure. _CGEL_ distinguishes Det–Head from Mod–Head and uses the DP–Nom boundary to separate modifier domains. These are competing ways of organizing the same constructional evidence; their grammatical costs are compared in §7.2.
# {==5==}{>>the writing in this section is highly inaccessible, assuming, as it does, far too much background knowledge from the reader<<}{id="c18" by="user" at="2026-09-12T01:03:38.847Z"} Coordinate subcategories and inheritance
Should determinatives and pronouns be coordinate subcategories within Noun, or {~~should~>do~~}{id="s27" by="user" at="2026-09-12T00:58:24.828Z"} determinatives belong inside pronoun? Reynolds (2021) {~~compares~>applies an~~}{id="s35" by="user" at="2026-09-12T01:01:51.267Z"} {++unsupervised clustering model to++}{id="s34" by="user" at="2026-09-12T01:01:38.111Z"} determinative and pronoun {--profiles--}{id="s33" by="user" at="2026-09-12T01:01:28.273Z"} {++in an x properties by y word-types matrix++}{id="s28" by="user" at="2026-09-12T00:58:47.344Z"}{--; its matrix--}{id="s29" by="user" at="2026-09-12T01:00:22.554Z"} {++which++}{id="s30" by="user" at="2026-09-12T01:00:28.319Z"} contains no common or proper nouns. Distributional separation between the supplied groups doesn’t determine their taxonomic rank or test the proposed superordinate category. The original discussion likewise leaves a nested nominal analysis open.

The accompanying audit reproduces the published DISCO decomposition, but the clustering outcome varies with initialization and feature selection.

> Note 13. The accompanying _Replication audit of the English determinative–pronoun feature matrix_ documents the discrepancy between the reported 232 features and the public 155-feature file, an extra feature dropped by the published clustering code, and the sensitivity results. The archived public file is retained unchanged.

The pronoun inventory in that study follows _CGEL_’s classification, whereas Hudson’s pronoun category includes the words he calls determiners. The reassignment of independent _what_ and relative _which_ proposed below also changes the boundary. The archived analysis therefore isn’t a test of the revised membership proposed here. Comparing the hierarchies requires aligned lexical inventories and generalizations stated for each candidate superordinate category.

Nesting would group pronouns and determinatives more closely than either with common or proper nouns. Reduced descriptive content and contextual interpretation are shared by many pronouns and determinatives. The coordinate analysis can record these interpretive properties through features or cross-classification; they don’t by themselves require an intermediate lexical category.

Pro-form gender links pronouns and determinatives (§3.1). The personhood-based system also includes non-nominal expressions (Reynolds 2025); it doesn’t by itself decide between coordinate and nested noun subcategories.

Restrictions on determination and attributive modification provide syntactic candidates, but they also occur outside the proposed grouping. In their primary use, proper names don’t select freely from the determiner system, and their adjectival embellishments are restricted (Huddleston and Pullum 2002, 517, 519–20). These properties distinguish more than pronouns and determinatives from common nouns.

Determination also differs within the proposed intermediate category. Determinatives permit external determination in a range of independent quantificational constructions: _the few_, _the many_, _the two_, _these three_. The permissions vary by item and often require further modification; _CGEL_ gives _these few here_ and _the many who did_ (Huddleston and Pullum 2002, 415–16). Pronouns admit external determination only marginally, and internal premodification is restricted, as in _poor old me_ (Huddleston and Pullum 2002, 429–30). These restrictions thus cross-cut the proposed grouping and vary within it.

I place determinative alongside pronoun because their shared nominal properties coexist with different centres of grammatical organization. Pronouns centre on person, case, reflexivity, and contextual reference; determinatives centre on quantification, determination, and their associated modifier patterns. The wider modifier permissions of determinatives would in particular prevent the restrictions on personal pronouns from being inherited by the whole nested grouping. Coordination preserves the distinctions without adding an intermediate pronoun category whose common rules remain to be established.
# 6 Restricted members and disputed boundaries
The broader grouping must accommodate members that lack its most conspicuous properties. Articles test whether ordinary independent use is necessary; _which_ and _what_ test the pronoun boundary; _no_/_none_ and _enough_ test form selection and functions outside NP structure.
## 6.1 Articles and the limits of independent use
Why classify the articles _the_ and _a_ as nouns if they can’t stand independently? _Every_ is restricted too, while _no_ has the distinct independent form _none_ (Huddleston and Pullum 2002, 371–72, 410–11).

> Note 14. In _the bigger the better_, _CGEL_ analyses _the_ as a modifier within a comparative phrase (Huddleston and Pullum 2002, 1131–32, 1135–36). This dependent use outside Det leaves the restriction on ordinary argument use intact.

_CGEL_’s treatment of _my_ supplies a precedent for restricted membership within Noun (Huddleston and Pullum 2002, 470–71). The pronoun’s paradigm supports its membership despite its lack of _m_{++y++}{id="s37" by="user" at="2026-09-12T01:06:33.765Z"}{--_ine_--}{id="s36" by="user" at="2026-09-12T01:06:31.629Z"}’s {==independent==}{>>mine is always independent<<}{id="c19" by="user" at="2026-09-12T01:06:43.150Z"} distribution. For articles, the corresponding positive evidence is integration into determinative; their nounhood depends on the category-level argument.

The articles participate in the determinative system of definiteness, quantity, and count restrictions. In _the/a/this/every book_, they occupy the same Det position and contribute to the interpretation of the NP. _The_ permits singular, plural, and non-count targets; _a_ selects a singular count target and contributes individuation. Their connections extend beyond shared position, although neither has the full determinative profile (Huddleston and Pullum 2002, 368–73){==.==}{>>the, like other Ds also functions as mod in AdjPs like the bigger the better<<}{id="c20" by="user" at="2026-09-12T01:07:51.303Z"}

_A_ also enters the complex determinatives _a few_, _a little_, and _many a_. In the last, _many_ contributes a large number and _a_ an individuating, distributive effect. _CGEL_ treats _many a_ as syntactically fixed: it doesn’t establish that ordinary _a_ freely accepts modifiers (Huddleston and Pullum 2002, 392–94). It does connect the article with quantificational constructions beyond _a book_.

_Every_ connects with independent _each_ through universal quantification and singular count selection. It also permits _almost_/_nearly_ and occurs after genitives in _her every move_. Spinillo (2004, 156–58) recognizes these differences from _the_ and _a_, as well as the articles’ greater phonological dependence. Her restricted grouping is thus a substantive alternative, not merely an omission of inconvenient properties.

The issue is how much independent support its shared restrictions provide. Absence of bare, predicative, and partitive uses all limits occurrence without a following nominal; they aren’t three independent reasons for a primary category. Little descriptive content extends well beyond the trio. Meanwhile, _a_’s quantificational constructions and _every_’s modifier permissions cross the proposed article boundary. I retain the restricted members within determinative because these connections preserve a broader system without granting unrestricted use to any member.

The argument for retaining the articles is synchronic. Grammaticalization supplies background: Lyons (1999, 331–36) discusses the development of definite articles from demonstratives and of articles expressing cardinality from numerals. These histories can explain changes in content and use, but don’t establish the synchronic classification.

The D-noun analysis retains the shared determining profile and records the absence of independent use in lexical permissions. The articles’ nounhood depends on their membership in that broader system. They don’t individually exhibit the full evidence that supports the parent category.
## {==6.2==}{>>how important is the inclusion of this section?<<}{id="c21" by="user" at="2026-09-12T01:16:19.603Z"} The pronoun boundary: _who_, _which_, and _what_
_Who_ has positive morphological grounds for pronoun status: its paradigm includes nominative _who_, accusative _whom_, and genitive _whose_ (Huddleston and Pullum 2002, 904–5){++, though, as we've seen above, no one property is definitive++}{id="s38" by="user" at="2026-09-12T01:11:00.142Z"}. _What_ lacks a comparable case paradigm. That absence alone wouldn’t exclude it from pronoun, but independent use and a non-personal interpretation don’t establish pronounhood either. Both properties occur among determinatives, including the _-thing_ compounds.

_CGEL_ assigns interrogative _what_ to two categories. Before an overt nominal it’s determinative, as in _what book_ or _what person_; independently it’s a non-personal pronoun, as in _What arrived?_ Relative _what_/_whatever_ receives a corresponding split. The stated contrast concerns gender: the independent forms are non-personal, while the determinatives permit personal and non-personal heads (Huddleston and Pullum 2002, 398).

I treat these occurrences as determinatives throughout. With an overt nominal, that nominal supplies the restriction {++(What person/object do you have in mind?)++}{id="s40" by="user" at="2026-09-12T01:13:26.658Z"}; without one, the construction requires a non-personal interpretation {++(What's behind the door?)++}{id="s39" by="user" at="2026-09-12T01:13:08.414Z"}. This states the contrast as a use condition instead of assigning a second lexical category on its basis. The determinative analysis preserves _what_’s connection across the constructions while distinguishing its gender restrictions from those of _which_.

Interrogative _which_ is already determinative in _CGEL_ both before a nominal and independently: compare _Which candidate arrived?_ and _Which arrived?_ With candidates under discussion, the latter can be personal. It also permits _which of the candidates_, whereas *_what of the candidates_ doesn’t have the corresponding selective reading (Huddleston and Pullum 2002, 397–98). Determinative membership therefore doesn’t predict identical gender or partitive permissions.

Relative _which_ poses the same boundary question as _what_. _CGEL_ treats it as determinative in _at which stage_, but as a non-personal pronoun in _the post office, which is nearby_ (Huddleston and Pullum 2002, 399). I retain determinative here too, with the non-personal restriction attached to this relative construction. This changes lexical classification, leaving relative-clause syntax, including fused relatives, to be analysed separately. Either classification places these words within the proposed superordinate Noun.

Exclamative _what_ in _What a nice day!_ remains a separate case. Following _CGEL_, I retain its adjective analysis here (§3.1). A common spelling doesn’t require one lexeme across all constructions. Nor does being a pro-form determine lexical category: gender-sensitive interpretation must be distinguished from the grammatical evidence for pronoun membership (Reynolds 2025).
## 6.3 Form selection and degree modification
_No_/_none_ illustrates a restriction on forms within a paradigm. _CGEL_ treats them as inflectional forms of one determinative: dependent _no students_ contrasts with independent _none_, while both permit _almost_ (Huddleston and Pullum 2002, 389–90). The D-noun analysis preserves this relation. Ordinary Head structure licenses _none of the students_; it doesn’t license *_no of the students_. Form selection remains necessary, just as with _my_/_mine_.

_Enough_ tests both position and external function. It precedes a nominal in _enough money_ and can follow one in _money enough_; post-head _enough_ can’t itself be premodified, as shown by *_money almost enough_ (Huddleston and Pullum 2002, 396–97, 445). Only the permitted construction licenses each position.

_Enough_ also modifies adjectives, adverbs, verbs, and some PPs: _good enough_, _quickly enough_, _I hadn’t prepared enough_, and _enough in control_ (Huddleston and Pullum 2002, 396–97). The degree determinatives _much_ and _little_, and _no_/_none_, likewise have uses outside NP structure (Huddleston and Pullum 2002, 390, 395–97). These permissions must survive reclassification. Noun membership doesn’t confine every projection to argument or determiner function.

NPs already modify adjectives in _three years old_, _a great deal smaller_, and _plenty big enough_ (Huddleston and Pullum 2002, 549–50). These include the quantificational common nouns compared in §3.1. Degree modification therefore supplies another connection with existing nouns, but also another restriction: _CGEL_ contrasts predicative _a great deal better_ with its exclusion before a noun in *_some a great deal better proposals_, where _much better_ is permitted (Huddleston and Pullum 2002, 551–52).

The D-noun analysis must preserve that difference between two kinds of NP modifier. It expands NP’s range of degree-modifier uses while restricting their positions by head and construction. The resulting cost is that the existing ban on pre-head NP modifiers within attributive AdjPs becomes a narrower condition. Nominal projection alone doesn’t license _enough_’s full distribution.
# 7 Structural consequences and grammatical economy
## 7.1 A shared phrase type in determiner function
In _some apples_ and _Kim’s apples_, the determining phrases share the NP category under both ordinary-Head accounts: D-noun and separate D. _CGEL_ instead distinguishes DP from genitive NP. It also admits a restricted range of plain-case NPs and PPs as determiners, as in _what size hat_ and _over thirty ties_ (Huddleston and Pullum 2002, Ch. 5, §4). The phrase types are:

```text
CGEL: Det:{DP,NP,PP} {++where DP > NP >> PP++}{id="s48" by="user" at="2026-09-12T01:24:01.456Z"} Both ordinary-Head accounts: Det:{NP,PP} {++where NP >> PP++}{id="s49" by="user" at="2026-09-12T01:24:15.134Z"}
```

This shares a phrase type without shortening the selectional disjunction: determinative-headed, genitive, and other licensed NPs still require separate identification. _CGEL_ already states definiteness and the single-Det restriction functionally, so reclassification doesn’t derive them. The following fragment compares projection once those restrictions are held fixed.
## 7.2 A matched descriptive fragment
A grammatical fragment is a set of rules for a specified range of constructions. Here it covers determination, ordinary subject and object uses, partitives, and the modifier and compound comparisons in §4. It compares the D-noun analysis with two separate-D alternatives: ordinary headedness and fusion. All receive the same lexical restrictions and constructed judgments. Predication, the disputed wh forms, and modification outside NP structure fall outside this small fragment; their implications enter the broader comparison in §7.3.

Table 4 records use permissions: whether a form, on a given reading, can head a phrase in determiner, subject, or object function. Argument use covers the subject and object NPs in examples such as _Some left_ and _I saw some_. Quotation, metalinguistic naming, and subordinate-clause uses of dependent genitives fall outside the fragment. Noun membership doesn’t itself grant a use permission.

Table 4: Shared permissions in the fragment. For _some_, the target column concerns its unstressed use before a noun. The inventory is deliberately limited to the displayed constructions.

| Form | De{++pendent++}{id="s42" by="user" at="2026-09-12T01:20:57.673Z"}{--t--}{id="s41" by="user" at="2026-09-12T01:20:57.226Z"} {--use--}{id="s43" by="user" at="2026-09-12T01:21:02.515Z"} | {~~Argument use~>Independnet~~}{id="s44" by="user" at="2026-09-12T01:21:06.690Z"} | Target in the Det construction |
| :--- | :---: | :---: | :--- |
| _the_ | yes | no  | Singular or plural; count or non-count |
| _a_, _every_ | yes | no  | Singular count nominal |
| _some_ | yes | yes | Plural count or non-count nominal |
| _few_ | yes | yes | Plural count nominal |
| _my_ | yes | no  | No {~~number/count restriction in this fragment~>ne~~}{id="s45" by="user" at="2026-09-12T01:22:16.761Z"} |
| _she_ | no  | yes | None |

Further constructional restrictions apply: _she_ is a subject form, whereas the corresponding ordinary object form is _her_. The target restrictions concern the common-noun nominal being determined: _a_ requires a singular count target such as _book_ in _a book_.

Table 5 locates the three accounts. Comparing the ordinary-Head accounts holds projection fixed while varying taxonomy. Comparing the separate-D accounts holds taxonomy fixed while varying headedness.

Table 5: Three accounts retaining the permissions in Table 4, the modifier restrictions, and the compound conditions.

| Account | Primary taxonomy | Simple independent determinative |
| :--- | :--- | :--- |
| D-noun analysis | D inside Noun | N–Nom–NP projection with Head function |
| Separate D, ordinary Head | D outside Noun | {~~D–Nom–NP through cross-category projection~>unclear~~}{id="s46" by="user" at="2026-09-12T01:23:09.987Z"} |
| _CGEL_: separate D, fusion | D outside Noun | NP distribution through Det–Head {++fusion++}{id="s47" by="user" at="2026-09-12T01:23:17.969Z"} |

The D-noun analysis applies nominal projection to determinatives through their membership in Noun. A separate condition checks use permissions. In the schemata below, `h` identifies the lexical head throughout its projection; parentheses mark optional dependents. The subscripts on Mod distinguish pre-head and post-head positions of the same modifier function. The head’s entry and construction restrict every dependent.

```text
Nom_h → (Mod_pre) Head:N_h (Comp) (Mod_post) NP_h → {++(pre-mod)++}{id="s50" by="user" at="2026-09-12T01:25:26.504Z"} (Det) Head:Nom_h licensed(NP_h,f,c) ⇔ f ∈ U_h ∧ C_h(f,c)
```

Here `U_h` is the head’s set of use permissions, `f` is the NP’s function, and `C_h` checks the lexical and constructional conditions in context `c`. For Det use, these include compatibility with the target nominal; for an argument headed by a singular count common noun, they include required determination. Optionality in the second rule doesn’t override those conditions.

These checks accommodate the reciprocal selection discussed by Hudson (§2.2). The determining phrase checks the target nominal’s count and number properties; the outer noun’s projection checks whether determination is required and supplied. Both conditions have to hold even though the tree assigns only one Head to each phrase.

In _some apples_, _some_ heads an NP whose Det permission and plural-count target requirement are satisfied. _Apples_ heads the outer Nom, which heads the NP. In _Some left_, _some_ heads an NP whose argument permission is satisfied. _Every apple_ passes the Det and singular-count checks; ordinary independent *_Every arrived_ fails the argument-permission check. _The apple_ and *_The arrived_ differ in the same way. {++what about _I know_ **_which apple_** _it is_++}{id="s51" by="user" at="2026-09-12T01:28:33.621Z"}

Each NP’s use permissions follow its own head. In _the apple_, the article’s Det permission licenses the dependent NP headed by _the_. The outer NP takes its argument permission from _apple_, whose requirement for determination is satisfied by the article.

A singular count common noun such as _book_ faces a different restriction from an article. In _a book_, its requirement for determination is satisfied; bare *_Book arrived_ leaves that requirement unsatisfied. _Books arrived_ has no such requirement. Requiring determination for a common noun doesn’t itself block an article-headed NP from argument use. An article’s exclusion from argument use must still be stated separately.

_Some_ and _few_ permit a partitive _of_-phrase within their nominal projection. _Almost_ can modify _every_ in _almost every teacher_; that permission doesn’t license _experienced_ as a modifier of _every_. The construction _the lucky few_ permits the external determiner and adjectival modifier shown in Figure 5.

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

The ordinary NP rule embeds this Nom. Det–Head jointly realizes Det of NP and Head of Nom, excluding a second Det; Mod–Head fills an internal modifier’s function and Head of Nom, allowing external determination. Lexical and constructional conditions select the fused function and permitted dependents. These schemata cover independent _few_, _few of them_, _the lucky few_, and _hardly anyone present_.

The ordinary-Head accounts share nominal projection and Head relations. Once a member’s use is licensed, its nominal structure follows from the shared rules; lexical and constructional conditions still determine the available functions and dependents. Dependent determinatives acquire a Nom layer in both. One account supplies these common structural expectations through inheritance from Noun, the other through a rule admitting both N and D.

The disjunction `{N, D}` groups the same heads for nominal projection. The D-noun analysis expresses this grouping in its lexical hierarchy, giving a point of harmony between taxonomy and phrase structure. Shared projection supports considering the grouping; its taxonomic rank depends on the broader profile comparison.

A grammar with Hudson’s nested classification can use the same permissions and projection rules. Holding those rules fixed, placing the broader pronoun category on determinative’s inheritance path from Noun leaves the fragment’s judgments unchanged.
## 7.3 Existing restrictions, additional costs, and consequences
I compare the shared structural core, the number of primary categories, the treatment of internal differences, the placement of related forms and uses, and the restrictions each account needs. I hold the inventory, constructions, and readings fixed. Shared rules receive equal credit whether they use inheritance or cross-category licensing.

Common nouns, proper nouns, and pronouns already differ in determination and permitted modifiers (Table 2). Preserving those conditions adds no cost to the D-noun analysis. Separate D likewise restricts adverbial modification and independent use within its own category; moving those restrictions inside Noun doesn’t create them.

The premodifier contrast in §3.3 adds a cost. A restriction normally stated for primary Noun now applies to specified noun subcategories, while determinatives retain their adverbial premodifiers. The attributive _almost textbook_ exception qualifies the original generalization. The degree-modifier contrast in §6.3 adds a parallel cost: determinative-headed NPs are admitted in positions that exclude other NP modifiers. Compound constructions also retain the distinction between inherited premodifier permissions and post-head restrictors (§4.5).

On shared structure, the ordinary-Head accounts tie. D-noun reduces the number of primary categories by one, retaining determinative as a subcategory and preserving its internal distinctions.

Reynolds (2026) distinguishes determinative {~~uses~>numerals~~}{id="s52" by="user" at="2026-09-12T01:32:56.064Z"} such as _ten men_, proper-noun {~~uses~>cases~~}{id="s53" by="user" at="2026-09-12T01:33:08.802Z"} such as _Room 10_{--_1_--}{id="s54" by="user" at="2026-09-12T01:33:12.208Z"}, and common-noun {~~uses~>numerals~~}{id="s55" by="user" at="2026-09-12T01:33:19.748Z"} such as _tens of pens_. Under the D-noun analysis, all fall within primary Noun, retaining their subcategory and constructional differences. Ordinals remain adjectives, and complex numeral phrases remain distinct from single lexemes.

Payne et al. (2013, 797–98) distinguish three lexemes spelled _one_: determinative, anaphoric common noun, and generic pronoun. These remain distinct under the D-noun analysis, but all belong within primary Noun.

Complex cardinals also separate category from function. In _two hundred books_, the whole _two hundred_ fills Det; internally, _two_ modifies the magnitude head _hundred_ (Reynolds 2026, sec. 4). In _these two hundred books_, _these_ fills Det and _two hundred_ is an internal modifier. One Det function doesn’t entail a limit of one determinative lexeme per NP.

Cardinal uses and the lexemes spelled _one_ remain within one primary category. Reassigning _what_ and relative _which_ likewise relocates a boundary inside Noun. These connected consequences of the hierarchy show what its alignment with nominal projection buys once the broader profile supports the grouping.

I favour the broader Noun category because it places the recurring nominal structure at the shared level and preserves the determinative distinctions where their restrictions apply. The alternative retains a primary boundary and crosses it in the projection rule. Both are coherent grammars. The choice turns on whether the shared profile warrants that parent category, with the modifier restrictions counted against it; reducing the number of primary categories alone wouldn’t suffice.

If determinative-headed and genitive expressions require different projection rules after their independently motivated restrictions are held fixed, the shared-projection proposal in §7.1 loses its advantage. That would favour separate phrase types. Retaining a separate primary D requires the further case that the category boundary captures the recurring differences better than a determinative subcategory within Noun.
# 8 Conclusion
English determinatives belong within Noun as a coordinate subcategory alongside common nouns, proper nouns, and pronouns. The combined case draws on argument and determiner functions, referential contrasts, inflection, and nominal dependents. Quantificational common nouns make the connection especially clear: their selected partitives and restricted dependents already occupy part of the grammatical territory associated with determinatives.

The resulting category retains internal differences. Articles lack ordinary independent uses; the _no_/_none_ paradigm requires form selection; degree modifiers require construction-specific permissions. I retain _who_ as a pronoun and analyse interrogative and relative _what_ as determinative, with explicit interpretive restrictions. These distinctions constrain the proposed subcategories within their shared parent.

Determinatives then inherit nominal projection and ordinary Head relations across bare, partitive, and externally determined uses. A separate-D grammar can reproduce that structure through cross-category licensing. I prefer the hierarchy that makes the recurring nominal grouping explicit, accepting the narrower modifier generalizations it requires. It aligns lexical classification with the broader grammatical profile while preserving determinatives’ distinctive place within Noun.
# Data and analysis materials
The accompanying supplements are _Replication audit of the English determinative–pronoun feature matrix_ and _CGELBank concordance and extraction notes_. The `analysis/` directory preserves their input files, provenance records, scripts, numerical outputs, and sentence concordance. Its README identifies the files and reproduction procedures.

Acknowledgements. For the September 2026 revision, GPT-6 (Astra), Claude Opus 5, Claude Haiku 4.5, and GLM-5.3-Flash assisted drafting, source retrieval, script development, or critical review; GPT-5.6 (Sol) checked numerical outputs. The accompanying materials record the tools and their uses. Responsibility for the analysis is mine.
# References
Abney, Steven P. 1987. “The English Noun Phrase in Its Sentential Aspect.” PhD thesis, Massachusetts Institute of Technology.

Bruening, Benjamin. 2020. “The Head of the Nominal Is N, Not D: N-to-D Movement, Hybrid Agreement, and Conventionalized Expressions.” _Glossa: A Journal of General Linguistics_ 5 (1). <https://doi.org/10.5334/gjgl.1031>.

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

Payne, John, Geoffrey K. Pullum, Barbara C. Scholz, and Eva Berlage. 2013. “Anaphoric _One_ and Its Implications.” _Language_ 89 (4): 794–829. <https://doi.org/10.1353/lan.2013.0071>.

Postal, Paul M. 1966. “On so-Called “Pronouns” in English.” In _Report of the Seventeenth Annual Round Table Meeting on Linguistics and Language Studies_, edited by Francis P. Dinneen. Monograph Series on Languages and Linguistics 19. Georgetown University Press.

Pullum, Geoffrey K., and Philip Miller. 2022. _NPs Versus DPs: Why Chomsky Was Right_. LingBuzz 006845. <https://lingbuzz.net/lingbuzz/006845>.

Pullum, Geoffrey K., and Deirdre Wilson. 1977. “Autonomous Syntax and the Analysis of Auxiliaries.” _Language_ 53 (4): 741–88. <https://doi.org/10.2307/412911>.

Reynolds, Brett. 2021. “Quantifying the Differences Between Lexical Categories: The Case of Pronouns and Determinatives in English.” _Cadernos de Linguística_ 2 (3). <https://doi.org/10.25189/2675-4916.2021.V2.N3.ID399>.

Reynolds, Brett. 2025. “Personhood and Pro-Forms: A Hierarchical Analysis of Gender in Modern English.” Unpublished manuscript.

Reynolds, Brett. 2026. “The Lexicon–Syntax Boundary in English Numerals: Cardinals, Ordinals, and Fractionals.” _English Language and Linguistics_, 1–19. <https://doi.org/10.1017/S1360674325100518>.

Reynolds, Brett, Aryaman Arora, and Nathan Schneider. 2023. “Unified Syntactic Annotation of English in the CGEL Framework.” In _Proceedings of the 17th Linguistic Annotation Workshop (LAW-XVII)_, edited by Jakob Prange and Annemarie Friedrich. Association for Computational Linguistics. <https://doi.org/10.18653/v1/2023.law-1.22>.

Sommerstein, Alan H. 1972. “On the so-Called Definite Article in English.” _Linguistic Inquiry_ 3 (2): 197–209. <https://www.jstor.org/stable/4177701>.

Spinillo, Mariangela Galvão. 2004. “Reconceptualising the English Determiner Class.” {PhD} thesis, University College London. <https://discovery.ucl.ac.uk/id/eprint/10101595/>.
