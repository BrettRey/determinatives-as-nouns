# Determinatives as nouns in English

Brett Reynolds — 10 September 2026 working draft

Revised after the latest author comments. The combined semantic, syntactic and morphological profile supplies the main argument; structural consequences and grammatical economy follow from it. The earlier annotations remain in the sections 1–3 review copy. Trees and schemata are shown as text; footnotes appear beside their paragraphs. The LaTeX source remains the manuscript master. [Typeset PDF](../determinatives-as-nouns.pdf).

# Abstract

I argue that English determinatives belong within Noun as a fourth coordinate subcategory alongside common nouns, proper nouns and pronouns. Their overlapping profiles across semantics, syntax and morphology support this broader category, while systematic differences support its internal divisions. Shared argument and determiner uses, referential distinctions, number and genitive marking, and nominal dependents contribute to the comparison. Adverbial premodification and grade give determinatives a distinctive profile with adjectival affinities. Including them within Noun makes nominal projection an inherited property and permits a more uniform analysis of their independent uses. A matched grammatical fragment examines these structural consequences and their costs against separate-D alternatives.

**Keywords:** determinatives, nouns, lexical categories, noun phrases, English

# 1 The question

What is the categorial relationship among words such as *some*, *me*, *apple* and *Brett*? I argue that all four are nouns, and that determinatives form a coordinate subcategory alongside common nouns, proper nouns and pronouns. I call this fourfold proposal the determinative-noun or D-noun analysis.

I adopt the general framework of *The Cambridge grammar of the English language* (*CGEL*; Huddleston and Pullum 2002). Unlike *CGEL*, though, I include determinatives within Noun. The claims concern synchronic English lexical categories.

> Note 1. I treat these categories as language-specific: a classification supported by another language’s grammar doesn’t determine the English classification.

I use determinative for the category containing articles, demonstratives and quantifiers such as *the*, *this*, *some*, *every* and *many*. I reserve determiner for the syntactic function within the noun phrase characteristically performed by phrases headed by these words. This distinction separates what kind of word *some* is from what syntactic relationships its phrase participates in.

> Note 2. For a fuller inventory, see the online [“List of determinatives in English”](https://www.cambridge.org/highereducation/api/resources/2AC8DF5CA558F8A6FCDFACD0EAF8EA08) accompanying Huddleston et al. (2022).

Capitalized Noun names the proposed category above common nouns, proper nouns, pronouns and determinative nouns. I argue that the similarities across their semantic, syntactic and morphological profiles are substantial enough to support this grouping. The differences distinguish subcategories within it. The comparison includes both the properties that connect determinatives with other nouns and those that connect them with other categories.

*CGEL*’s inclusion of pronouns within Noun supplies a starting comparison. It emphasizes the functions of pronoun-headed phrases, despite differences in inflection and dependents (Huddleston and Pullum 2002, 327–28). I assess pronouns and determinatives within the broader comparison just described. The inclusion of auxiliaries within Verb supplies a precedent for preserving distinctive syntax within a more inclusive lexical category (Pullum and Wilson 1977).

Classifying determinatives as nouns gives them the nominal projection rules of Noun. A determinative therefore heads a nominal (Nom), which heads an NP, just as common nouns, proper nouns and pronouns do. Nom contains the head and its internal dependents, excluding an external determiner. Lexical restrictions govern which uses are available.

Figure 1 compares *CGEL* with the D-noun analysis for *take some apples* and *take some*. Both keep *some* in one lexical category across uses. In *CGEL*, independent *some* jointly fills determiner and head functions, a fusion of functions (Huddleston and Pullum 2002, 410–12). As a syntactic representation, fusion of functions appears to have seen little adoption outside work based on *CGEL*. In the D-noun analysis, *some* heads its own NP through a Nom in both uses.

Here DP abbreviates determinative phrase, as in *CGEL*, not to be confused with the DP of the DP hypothesis, where D heads the whole expression *some apples* (Abney 1987; §2.1). The D-noun analysis keeps *apples* as that expression’s ultimate head.

CGEL: take some apples — dependent some

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

CGEL: take some — independent some

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

D-noun analysis: take some apples — dependent some

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

D-noun analysis: take some — independent some

```text
VP
├── Head: V
│   └── take
└── Obj: NP
    └── Head: Nom
        └── Head: N_D
            └── some
```

Figure 1: *Take some apples* (first and third trees) and *take some* (second and fourth trees) under *CGEL* (first pair) and the D-noun analysis (second pair). In the second tree, DP fills Det of NP and Head of Nom. In the third and fourth trees, *some* heads an NP through the same nominal projection; that NP functions as Det in the third tree and Obj in the fourth tree. Function labels appear above category labels. Det marks determiner, Obj object, and Det–Head fusion; the two links show the combined functions. N, D and V mark noun, determinative and verb; NP, DP and VP mark their phrases. Subscripts identify noun subcategories.

The English article–pronoun boundary has long been contested. Palmer (1924) groups “determinative adjectives” with pronouns; Postal (1966) analyses personal pronouns as articles at an intermediate level of representation; Sommerstein (1972) gives the definite article and pronouns underlying NP structure. Their proposals make different kinds of unification available. Hudson places his determining words within pronoun and pronoun within noun (Hudson 2004, 2010). Section 2.2 compares the English evidence and the resulting classifications.

The grouping also offers several connected simplifications. First, determinatives inherit nominal projection, replacing a separate DP with NP. Second, ordinary Head structure unifies the bare, partitive and externally determined uses that *CGEL* divides between Det–Head and Mod–Head fusion. Third, NP becomes the phrase type shared by ordinary determinatives, genitives and the minor nominal determiners. Fourth, the determinative, common-noun and proper-noun uses of cardinals fall within one primary category.

These consequences contribute an economy argument whose force depends on the rest of the grammar. Section 7 compares the shared structures with the changes required in stating modifier and use restrictions. The primary taxonomic argument concerns the combined grammatical profile; a reduction in category labels alone wouldn’t establish it.

I first distinguish the competing analyses, then compare external and internal syntax, meaning, inflection and word formation across the proposed noun subcategories. Independent uses, partitives and modification identify the constructions to be explained. The matched fragment in §7.2 holds the judgments and lexical restrictions fixed while varying taxonomy and headedness; its economy depends on preserving the empirical distinctions established by the comparison.

# 2 Classification, headedness and function

## 2.1 Category, function and phrase structure

Lexical categories and syntactic functions cut across one another. An NP can function as determiner, as in *<u>Kim’s</u> book*, and a determinative-headed phrase can function as modifier, as in *the <u>many</u> people* (Payne et al. 2010; Pullum and Miller 2022). Including determinatives within Noun preserves this distinction: the NP headed by *some* functions as determiner in *take some apples* and as object in *take some* (Figure 1).

The question of lexical classification is distinct from the headedness question associated with the DP hypothesis of Abney (1987). Under that hypothesis, D heads expressions such as *some apples*. I retain noun-headed NPs and reject the DP analysis for English, following the arguments of Pullum and Miller (2022) and Bruening (2020).

Category membership doesn’t remove lexical restrictions. *Every apple* is grammatical, but \**I’ll take every* isn’t an ordinary way to accept apples. Making *every* a noun doesn’t give it the full range of uses available to *some*. Section 7.2 states structural rules and lexical restrictions separately so their contributions can be assessed.

## 2.2 Taxonomic and structural alternatives

Keeping a word in one category across dependent and independent uses leaves its taxonomic position open. As Lyons (1968, 232–35) observes, distribution can be compared at different levels of categorization: two expressions may belong together at one level and differ at a more specific level. Table 1 distinguishes the selected authors’ proposals, their analytical levels and several logical alternatives. The D-noun analysis differs from *CGEL* by including determinative within Noun, and from Hudson by placing it alongside pronoun.

Table 1: Selected accounts and logical alternatives. The earlier proposals differ in scope and representational level; they don’t all specify a surface taxonomy. The prose gives sources and inventory qualifications.

| Account | Proposed relationship | Level or status |
|:---|:---|:---|
| Palmer | Determinative adjectives grouped with pronouns. | Lexical grouping; inclusive Noun unspecified |
| Postal | Personal pronouns analysed as articles, with deeper noun features. | Intermediate and underlying representations |
| Sommerstein | Definite article and personal pronouns given NP structure. | Underlying representation |
| Lyons | Articles, demonstratives and personal pronouns linked by definiteness and deixis. | Semantic relationship |
| *CGEL* | Pronoun within Noun; determinative separate. | Lexical taxonomy |
| Hudson | Determiners within pronoun, which is within noun. | Lexical taxonomy |
| Spinillo | Determinatives redistributed; *the*, *a* and *every* retained as articles. | Lexical reclassification |
| D-noun analysis | Common noun, proper noun, pronoun and determinative coordinate within Noun. | Proposed taxonomy |
| Logical alternative | Noun, pronoun and determinative separate. | For comparison |
| Logical alternative | Determinative within Noun; pronoun separate. | For comparison |
| Logical alternative | Pronoun within determinative, which is within Noun. | For comparison |
| Logical alternative | Pronoun within proper noun; determinative within common noun. | For comparison |

Palmer (1924, 24) proposed placing “determinative adjectives” with pronouns. He contrasted them with qualifying adjectives, which permit predicative use, comparison and adverbial modification, and emphasized most determinatives’ ability to “be used indifferently as pronouns or as modifiers of nouns”. This supplies an early English distributional argument for unification. It doesn’t specify the inclusive Noun hierarchy proposed here. Lyons (1968, 279) adds a semantic connection: articles, demonstratives and personal pronouns share definiteness and deictic contrasts.

Postal (1966) develops the article–pronoun connection through English reflexives and combinations such as *we men*. His morphological evidence for the noun *self* includes *selfish*, *selfless* and the plural alternation *self*/*selves*; he analyses the preceding pronominal material as an article. The classification depends on representational level: article segments occur at intermediate stages, their deepest counterparts are features of nouns, and surface pronouns can receive derivative Noun status.

Sommerstein (1972, 197–203) argues in the opposite direction, giving the definite article and personal pronouns underlying NP structure. His English comparison includes the count restriction on anaphoric *one*, contrasting with *it*’s ability to refer to a quantity of a substance. He also observes that noun status for *self* doesn’t decide whether the preceding element is an article or a genitive pronoun. Their disagreement concerns which direction of analysis explains the shared behaviour.

> Note 3. For the later analysis of anaphoric *one* as a common count noun, distinct from determinative *one* and personal pronoun *one*, see Payne et al. (2013, 797–98). The count restriction remains part of that account.

These proposals are substantive predecessors of the present unification, but their underlying structures don’t supply a classification of the full English determinative inventory. The wider contrasts in grade, modification, complementation and restricted independent use still need an account. The comparison here asks how those properties are distributed among surface lexical categories, while retaining the earlier challenge to a fundamental article–pronoun separation.

Hudson makes taxonomic inclusion explicit. His noun category contains common noun, proper noun and pronoun (Hudson 2010, 253–54); a determiner is a pronoun whose valency permits the relevant common-noun dependent (Hudson 2004, 9–10). His analysis preserves one lexical category across independent and dependent uses and expresses their difference through permitted dependents. The D-noun analysis shares that continuity but proposes a coordinate determinative subcategory.

Hudson’s criteria are also limited: they centre on licensing a singular count common noun and on mutual exclusion in that use. He sets aside *all*, cardinal numerals and quantifiers restricted to plural or non-count nouns (Hudson 2004, 9–10). These exclusions leave a substantial part of *CGEL*’s inventory outside his target grouping. Extending the pronoun analysis to that inventory requires comparing its modifier selection, grade and quantitative meanings with the properties of the existing pronouns.

Hudson also permits mutual dependency between determiner and common noun, with different constructions selecting different external heads (Hudson 2004, 7–12). His English temporal adjunct *We met that day* supports a common-noun head because the adjunct’s distribution depends on *day*’s temporal meaning. Mutual dependency adds a structural commitment to his taxonomy. The D-noun analysis retains common-noun headedness in *that day* while changing the determining word’s superordinate category.

Spinillo (2004) instead proposes redistributing determinatives among existing categories, with *the*, *a* and *every* retained as an expanded article category. This isolates three members without ordinary independent use while assigning the others elsewhere. In particular, isolating *every* requires weighing that restriction against the quantitative and modifier properties it shares with other determinatives (§6).

For demonstratives and forms such as *some* and *all*, Spinillo (2004, 140–44) compares dependent and independent uses with verbs and prepositions occurring with or without a complement. The analogy supports keeping a word’s category stable across uses. It doesn’t select that category or explain the full pattern of permitted dependents. *CGEL*, Hudson and the D-noun analysis can all preserve category continuity while disagreeing about classification.

The comparison therefore concerns the same English words across external syntax, internal syntax, semantics, inflection, and word formation. Independent use and shared deixis supply part of that evidence. Grade, genitive marking, complementation, modifier selection and derivational relationships supply further comparisons, including potential evidence against unification. Section 3 sets out this broader profile before §4 develops the nominal constructions and §5 assesses the pronoun boundary.

# 3 The D-noun analysis

## 3.1 The basis for a broader Noun category

Common nouns, proper nouns and pronouns combine different ways of identifying or characterizing entities with overlapping nominal syntax. Determinatives add quantitative, definite and deictic meanings to this comparison. Table 2 sets their external and internal syntax beside their semantics and morphology. The grouping proposed here rests on the combined profile across these domains. Its breadth permits systematic differences among subcategories as well as restrictions on individual members.

Table 2: Representative profiles of the proposed noun subcategories. Entries describe ranges of behaviour, not properties of every member. External syntax concerns whole phrases; the competing analyses differ over their internal heads. Noun-forming suffixes are listed by their bases, without assuming that noun output establishes noun input. Sources and qualifications follow.

| Dimension | Common noun | Proper noun | Pronoun | Determinative |
|:---|:---|:---|:---|:---|
| Inventory | Open | Open to new names | Closed | Closed |
| External syntax | NP argument functions; genitive Det | NP argument functions; genitive Det | NP argument functions; genitive Det | NP argument functions; Det as in *some books*, *someone’s books* |
| Meaning | Descriptive properties and relations | Naming in primary uses | Mainly deixis and anaphora | Quantification, definiteness and deixis |
| Pro-form gender | Descriptions contribute to referent construal | Names identify referents construed by gender | Contrasts expressed by gender-sensitive pro-forms | Contrasts expressed by gender-sensitive pro-forms |
| Inflection | Number and genitive | Genitive; restricted number | Case, including genitive; reflexive forms | Number; grade; genitive, e.g. *something’s* |
| Noun-forming suffixes | *-ship*: *friendship* | *-er*: *Londoner* | No parallel established here | *-ness*: *nothingness* |
| Determination | Broad contrasts; singular count arguments normally require it | Restricted in primary naming uses | Normally excluded | Lexically restricted; *the few*, *these three* |
| Internal modification | Productive; usually AdjP premodifiers; relative postmodifiers | Restricted embellishments | Restricted: *poor old me*; relative postmodifiers | AdvP premodifiers; NP-internal postmodifiers; *the lucky few* |
| Complementation | Selected PPs and clauses | Not characteristic of primary naming uses | Normally absent | Partitive *of*-PPs; comparative *than*-phrases |

Common nouns supply the most familiar nominal profile. Proper nouns’ naming uses and pronouns’ deictic and anaphoric uses depart from it in both meaning and permitted dependents. Their inclusion within Noun is a classificatory judgment about those similarities and differences. I make the same kind of judgment about determinatives, assessing all four profiles together rather than treating the common noun as an entry test for the others.

Meaning and reference vary within Noun. *Apple* conveys a descriptive classification; *Kim*, in its primary naming use, identifies through a name; *she* supplies limited descriptive content and depends on context. Determinatives range from deictic *this* to quantitative *many* and universal *every* (Huddleston and Pullum 2002, 358–60, 370–405, 425–28, 515–21). Their semantic affinities cross several boundaries: deixis connects demonstratives with pronouns, while quantity connects determinatives with common nouns such as *number* and *majority*.

Pro-form gender connects these ways of referring. Descriptions such as *the woman* and names such as *Kim* identify referents whose construal bears on pro-form choice. Gender-sensitive pronouns and determinatives express the relevant contrasts: compare personal *she* and *somebody* with non-personal *it* and *something* (Reynolds 2025). The connection concerns how referents are construed, rather than noun-class gender assigned to common or proper nouns. Section 5 considers its implications for the pronoun boundary.

Semantic differences remain substantial. *Every* contributes a quantificational relation between a nominal restriction and what’s predicated of its members; *Kim* identifies an individual through a name. The proposal preserves these contributions within distinct subcategories. Their place in one category is supported by the accompanying syntactic and morphological relationships, not by a claim that quantification and naming have the same meaning.

External syntax supplies a broad overlap in the functions available to the phrases. *CGEL* makes this the stated ground for including pronouns within Noun (Huddleston and Pullum 2002, 327). A range of determinatives likewise occurs in subject, object and complement-of-preposition positions without another overt nominal head. The examples in §4.1 compare these uses across all four proposed subcategories.

Shared functions leave systematic distributional differences. In *Who did you see?*, interrogative *who* precedes the inverted auxiliary. Substituting *the vicar* doesn’t preserve the open interrogative. A common-noun-headed phrase needs an interrogative constituent, as in *which vicar*. Both expressions have object function, but the construction also requires interrogative properties (Huddleston and Pullum 2002, Ch. 10, §§7.1, 7.9). Such differences belong in the profile being compared.

I treat shared external functions as one source of evidence for nounhood. Making them a sufficient condition would give a single diagnostic more authority than the broader comparison supports: adjectival constructions such as *the rich* also fill those positions. Internal syntax supplies further evidence. Determinatives permit partitive complements, as in *some of the wine*, and comparative complements, as in *more than ten* (Huddleston and Pullum 2002, 392–94, 411–12, 432–33).

Common nouns permit PPs and clauses, while pronouns and primary naming uses of proper nouns have much more restricted dependents (Huddleston and Pullum 2002, 429–30, 439–43, 517–21). Determinatives share parts of both profiles: restricted determination and modification coexist with nominal complement and postmodifier constructions. Section 3.3 examines their distinctive premodifiers, and §4.4 compares the resulting profile with adjectives.

Inflection supplies overlapping contrasts too. Common nouns inflect for number and genitive; proper nouns permit number distinctions in restricted uses. Pronouns distinguish case, including genitive, and reflexive forms. Within determinative, *this*/*these* shows number, *few*/*fewer*/*fewest* grade, and *something’s* genitive (Huddleston and Pullum 2002, 373, 423–24, 426, 479–80, 521). Number and case connect parts of the inventory with nouns; grade connects another part with adjectives.

Number contrasts aren’t uniformly inflectional. *CGEL* treats singular and plural *you* as distinct lexemes whose difference is overt only in the reflexive forms *yourself* and *yourselves* (Huddleston and Pullum 2002, 486). The comparison therefore distinguishes the expression of number from number inflection within a lexeme. Word formation contributes a further morphological comparison (§3.4).

Extending the analysis to restricted members carries a separate burden. Pronoun forms themselves don’t all pass the argument-position test: dependent genitives such as *my* have positive support from their paradigms. For determinatives, the argument likewise needs to establish both a broadly nominal constructional profile and the restricted members’ integration into that category. Section 6 supplies the latter argument.

The similarities link determinatives to different parts of Noun. Deixis and pro-form gender connect them with pronouns; number and genitive marking connect some members with common and proper nouns; argument and determiner uses span all four groups. Partitives and nominal postmodification extend the internal-syntactic comparison. I judge this combined profile substantial enough for a superordinate category, with determinatives’ quantificational, inflectional and modifier patterns supporting their distinct place within it.

The D-noun analysis captures shared properties through inheritance: a property stated for a superordinate category is available to its subcategories, subject to stated restrictions. Determinatives therefore inherit nominal projection from Noun. Subcategory rules constrain combinatorics, and lexical entries distinguish such forms as independent *some* and dependent-only *every*.

## 3.2 Noun phrases in determiner and argument functions

Determiner function already cuts across the existing noun subcategories. Compare *my preferences*, *Kim’s preferences* and *people’s preferences*. The determiner is an NP ultimately headed by a pronoun, a proper noun and a common noun respectively (Huddleston and Pullum 2002, 354–55, 470–71). Figure 2 illustrates the proper-noun case: *Kim’s* fills Det, while *preferences* ultimately heads the larger NP.

> Note 4. *CGEL* assigns these genitives the combined function Subject–Det (Huddleston and Pullum 2002, 472–73). I treat them as Det here, without the additional subject function.

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

Figure 2: The genitive NP *Kim’s* functions as determiner within *Kim’s preferences*, ultimately headed by *preferences*. The representation abstracts from the internal realization of genitive marking.

The compound determinative *someone*, following the classification of Payne et al. (2007, sec. 1.3), joins this pattern in *someone’s preferences*: its genitive NP fills the same determiner function. The nominal base in *someone* may contribute to that permission, and most determinatives resist case marking.

The inherited projection gives the two D-noun structures in Figure 1. In *take some apples*, the NP headed by *some* fills Det, as *Kim’s* does in *Kim’s preferences*; *apples* heads the larger NP. In *take some*, *some* heads the whole object NP. The lexeme retains its subcategory and nominal projection across these uses, while the NP it heads changes function.

NP becomes the shared phrase type for the principal realizations of determiner function. Plain determinative phrases join genitives such as *Kim’s* and *my*. Minor determiners include further NPs: *what size* in *what size shoes*, *that size* in *that size shoes*, and *Sunday* in *Sunday morning* (Huddleston and Pullum 2002, 356). Determiner function is thus shared across the proposed nominal subcategories.

PPs remain a restricted alternative, as in *up to twenty minutes* and *between fifty and sixty tanks* (Huddleston and Pullum 2002, 356). By contrast, *almost ten* is an NP under the D-noun analysis, with an adverbial modifier of its numeral head. Number, countability and other selectional conditions distinguish the determining expressions. Sections 7.1–7.2 compare the resulting structures and restrictions.

## 3.3 Modifier selection and taxonomic level

Shared nominal projection doesn’t make modifier permissions uniform. In *almost every experienced teacher* (Figure 3), the AdvP *almost* modifies the determinative noun *every*; the AdjP *experienced* modifies the common noun *teacher*, which ultimately heads the outer NP.

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

Figure 3: Two modifier relations in *almost every experienced teacher*: *almost* modifies *every*, and *experienced* modifies *teacher*. The outer NP has *teacher* as its ultimate head. Internal structure within the one-word modifier phrases is suppressed.

Payne et al. (2010, 40–42) defend keeping *few*, *any* and related forms in one lexical category across dependent and independent uses. In *hardly any money* and independent *hardly any*, *hardly* remains an adverb and *any* retains its category. The D-noun analysis preserves that continuity. It also preserves their contrast between adverbial premodification, as in *almost anybody*, and adjectival postmodification, as in *nothing absolute*.

The systematic use of AdvP premodifiers is the strongest internal-syntactic objection to the D-noun analysis. In the other three noun subcategories, internal premodifiers are normally adjectival or nominal. Adverbs occurring before a whole NP, as in *only you*, don’t supply a parallel: they’re peripheral modifiers of the NP, rather than internal modifiers of its head (Huddleston and Pullum 2002, 430–31). The distinction concerns attachment as well as word order.

Payne et al. (2010, 42–47) establish that adverbs can postmodify common nouns, and they analyse *almost* as modifying the attributive noun *textbook* in *an almost textbook case* (Payne et al. 2010, 75, n. 3). Adverbial modification therefore isn’t categorically excluded from Noun. But neither postmodification nor a restricted attributive use removes the systematic contrast between *hardly any* or *almost every* and ordinary common-noun premodification.

The existing noun subcategories also differ in the range and conditions of their postmodifiers. Common nouns freely take integrated relative clauses; personal pronouns permit a restricted range, including *we who have read the report* (Huddleston and Pullum 2002, 430). Compound determinatives permit them too, as in *something that you need to know* (Huddleston and Pullum 2002, 423–24). These comparisons show that modifier permissions can vary within Noun, but they don’t neutralize the premodifier objection.

Including determinatives places this systematic premodifier contrast within Noun. The determinative subcategory licenses *hardly any* and *almost every*; common nouns license *experienced teacher*. Neither \**experienced every* nor \**almost teacher* follows. The contrast weighs against the proposed grouping, while the other nominal connections weigh in its favour. Its taxonomic level depends on that cumulative comparison; §7.3 examines the consequences for stating the rules.

## 3.4 Word formation and category boundaries

Derivational affixes contribute two kinds of evidence: the categories they select as bases and the categories they form. A suffix restricted to nominal bases would supply evidence about a determinative’s input category. A suffix forming common nouns establishes the output category, but may permit several kinds of base. The noun-forming examples in Table 2 need to be assessed in these terms.

The common-noun and proper-noun examples illustrate the distinction. *Friendship* contains *-ship*, which primarily selects nouns denoting persons, though *hardship* has an adjective base. The inhabitant suffix *-er* in *Londoner* attaches to a place name. These are specific nominal derivations, but the comparisons presented here establish no corresponding noun-selecting suffix shared by pronouns and determinatives (Huddleston and Pullum 2002, Ch. 19, §§5.6.2(b), 5.7.2(k)).

Related suffixes reinforce the need to check input restrictions. *-hood* usually selects noun bases, as in *bachelorhood*, but also forms *falsehood* and *likelihood* from adjectives. *-dom* similarly has noun bases in *kingdom* and *officialdom*, alongside adjectival bases in *freedom* and *wisdom* (Huddleston and Pullum 2002, Ch. 19, §5.7.2(e–f)). These exceptions limit the value of treating a familiar nominal suffix as a categorical input test.

Determinatives do enter derivations whose output is a common noun. *CGEL* cites *nothingness* and *oneness* among formations with *-ness* on non-adjectival bases (Huddleston and Pullum 2002, Ch. 19, §5.7.2(i)). Further established nouns include *thisness*, *fewness* and *muchness*. On a direct D-base analysis, these formations connect determinatives with common nouns through derivation. Under the proposed taxonomy, that connection is internal to Noun.

> Note 5. See *Merriam-Webster.com Dictionary*, s.vv. [*thisness*](https://www.merriam-webster.com/dictionary/thisness) and [*fewness*](https://www.merriam-webster.com/dictionary/fewness), and *Dictionary.com*, s.v. [*muchness*](https://www.dictionary.com/browse/muchness) (accessed 10 September 2026). The entries establish the words and their meanings or histories; they don’t establish a uniformly productive modern rule.

Their input classification remains open to the wider evidence. *-ness* is the default suffix for forming nouns from adjectives, but also attaches to other bases, as in *whyness*. Its occurrence in *nothingness* therefore establishes neither an exclusively nominal nor an exclusively adjectival base. Where a converted base intervenes, the derivation begins from that base; a conversion analysis needs evidence beyond protecting a preferred classification.

The adverb *mostly* provides a different output. Adverbial *-ly* primarily attaches to adjectives, but *CGEL* also gives noun-based *partly* and *purposely* (Huddleston and Pullum 2002, 566). This derivation gives *most* an adjectival affinity without supplying an adjective-only diagnostic. Its adverb output crosses a primary-category boundary under either the separate-D or D-noun classification.

> Note 6. See *Dictionary.com*, s.v. [*mostly*](https://www.dictionary.com/browse/mostly) (accessed 10 September 2026).

Compounding supplies a further connection, though it isn’t an affix-selection test. Pronouns enter gender-marking compounds such as *he-goat* and *she-ass* (Huddleston and Pullum 2002, Ch. 19, §5.3); determinatives combine with nominal material in *someone* and *anything*. Their determinative premodifier permissions recur in the compounds (§4.5), supporting continuity between a base and its compound while the nominal component contributes further properties.

Numeral morphology extends the comparison to ordinal and fractional formations, analysed respectively as adjectival and nominal by Reynolds (2026). Their formation also bears on the boundary between a numeral lexeme and a syntactic phrase. These distinctions concern different outputs and different constituent structures; the common cardinal base participates in all of them.

Morphology thus provides overlapping and divergent relationships. Number and genitive marking give the clearest inflectional connections with nouns. Noun-forming derivation adds a relationship between some determinatives and common nouns, while grade and the predominantly adjectival *-ness* and *-ly* patterns supply adjectival affinities. These contributions have different evidential force. Their place in the argument depends on the accompanying semantic and syntactic profile.

# 4 Evidence for nominal structure

Independent uses, partitives and modification show a recurring nominal pattern. These observations overlap: *Some left* illustrates both external distribution and syntactic completeness. Fusion and ordinary headedness can cover this pattern. The comparisons below distinguish the shared observations from the analyses of their internal structure; §7.2 assesses the resulting organization of the grammar.

## 4.1 Breadth of independent use

Independent use is widespread within the determinative inventory. *CGEL* discusses such uses for demonstratives and quantifiers including *some*, *all*, *both*, *many*, *few*, *several*, *each*, *either*, *neither*, *much* and *enough*, while recording lexical restrictions and the separate forms *no*/*none* (Huddleston and Pullum 2002, 371–72, 410–24). The generalization concerns the availability of independent constructions across a lexical category, not unrestricted acceptability in every sentence frame.

> Note 7. Material before a determiner falls outside the independent-use comparison. *CGEL* treats *all*/*both* in *all/both the books* as predeterminer modifiers, *quite*/*rather* before *a good idea* as peripheral modifiers, and *such*/exclamative *what* before *a disaster* as adjectives (Huddleston and Pullum 2002, 433–37). The fixed *many a* is a complex determinative restricted to Det function (Huddleston and Pullum 2002, 394). The *half* in *half a cake* is a common noun used as a predeterminer modifier (Huddleston and Pullum 2002, 434). These constructions don’t add evidence for independent determinative heads.

The pattern extends beyond a few compounds or a single lexicalized expression. For this closed category, productivity concerns the availability of independent use among established members under appropriate conditions, rather than the licensing of new lexical items.

In the constructed examples in (1), compare the positions occupied by the bracketed NPs: subject, object and complement of a preposition. Assume that a woman named Kim and a group of people are already under discussion. These positions admit NPs containing words from each proposed noun subcategory; the competing analyses assign different internal structures to independent *some*.

(1a) *\[People\] left.* — *I see \[people\].* — *with \[people\]*

(1b) *\[Kim\] left.* — *I see \[Kim\].* — *with \[Kim\]*

(1c) *\[She\] left.* — *I see \[her\].* — *with \[her\]*

(1d) *\[Some\] left.* — *I see \[some\].* — *with \[some\]*

Adjectival independent uses prevent a simple inference from these positions to nounhood. *The rich* and *the poor* can fill nominal argument positions. Comparative and superlative adjectives also head expressions without a human-class interpretation: *CGEL*’s *the most important of her criticisms* is an NP containing a partitive *of*-phrase (Huddleston and Pullum 2002, 332–33, 416–23).

Independent *some* can form a one-word NP, whereas an NP with *rich* as fused head normally requires a determiner on the human-class reading. That is a local contrast: argument NPs headed by singular count common nouns also need determination. Section 4.4 returns to the fuller adjectival comparison.

## 4.2 Structural saturation and interpretation

With a group of people under discussion, *Some left*, *Many came* and *All agree* illustrate structural saturation: an argument expression can be syntactically complete without another overt head or determiner. Syntactic completeness differs from contextual interpretation. In *I’ll take some*, the relevant substance or set may be supplied by discourse or the situation. That dependence doesn’t establish a deleted common noun: ordinary pronouns also depend on context.

In the following attestation from the CGELBank treebank, *two different Honda models* supplies the domain for the independent object *both*:

> Note 8. CGELBank (Reynolds et al. 2023), sentence [`reviews-083459-0002`](https://github.com/nert-nlp/cgel/blob/d0a2c2d8c522b23d5aa879fc9cb94948f4285b2c/datasets/ewt.cgel#L651-L654).

\(2\) *Went there yesterday: we are trying to decide between two different Honda models, so we wanted to test-drive both back to back.*

Generalizing expressions such as *Many are called, few are chosen* and *Enough is enough* need no previously uttered common-noun phrase. They rule out a mandatory overt-antecedent requirement, but a silent-noun account could supply a generic restriction. Such examples don’t decide whether the restriction belongs in semantics or syntax.

The comparison with ordinary pronouns and proper nouns is structural as well as interpretive. In *She left* and *Kim left*, *CGEL* permits an NP headed by a nominal with no determiner. Applying that structure to *Some left* preserves the same division between a complete NP and its context-dependent reference. The dependent use of *some* doesn’t by itself require a Det function inside every independent occurrence.

Fusion supplies the competing analysis. In Payne et al. (2007), one constituent jointly realizes Head and a dependent function, subject to structural and adjacency conditions. In *CGEL*’s analysis of independent *some*, the DP headed by *some* fills Det of NP and Head of Nom. The word retains the determinative category it has in *some apples*, while the independent expression is an NP. Ordinary headedness replaces this relation with nominal projection; lexical restrictions on independence and form selection remain.

*CGEL* also uses fusion in noun-headed structures. It analyses *mine* as fused Det–Head when it stands for a possessed entity in an anaphoric context, but as pure Head in the predicative possessive use *it’s mine* (Huddleston and Pullum 2002, 410–11).

Saturation therefore clarifies the distributional comparison without independently selecting either internal structure.

## 4.3 Partitives locate the quantificational head

In *some of the wine*, *some* specifies a quantity drawn from an identifiable amount of wine. The NP *the wine* denotes the partitive domain: the whole from which that quantity is drawn. This NP is complement of *of*. A pronoun-headed NP or independent genitive NP can express the domain too: *many of them*, referring to previously mentioned people, or *some of Kim’s*, referring to Kim’s apples.

Compare where the common noun occurs in *some apples* and *some of the wine*. In the partitive, *wine* is embedded inside the *of*-phrase, so it can’t be the lexical head of the whole NP. The comparison instead concerns the head-like role of *some* in that larger expression.

Figure 4 gives the D-noun analysis, with the *of*-phrase functioning as complement within Nom, as in *CGEL*’s partitive tree (Huddleston and Pullum 2002, 411–12). *CGEL* represents the head-like role of *some* through Det–Head fusion. Partitives support that role while leaving the choice between fusion and ordinary headedness open.

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

Figure 4: *Some of the wine* under the D-noun analysis. The Head relations lead from the outer NP to *some*. The common noun *wine* is inside the complement PP and doesn’t head the whole expression. The inner NP is abbreviated.

The overt quantifier and domain already supply a compositional interpretation of *some of the wine*. A silent common noun would need to explain something further, such as a restriction on interpretation or modification that the overt-head account misses. The construction itself supplies no such requirement. I therefore prefer an overt-head analysis over an otherwise equivalent null-head analysis; fusion remains compatible with that preference.

The D-noun analysis treats *some* and *some of the wine* as sharing nominal projection, with an added domain phrase in the partitive. Modification provides a further comparison of internal structure.

## 4.4 Modification tests the internal analysis

The pair *the lucky survivors*/*the lucky few* supplies a comparison involving both external determination and adjectival modification. *CGEL* explicitly permits determinatives used as internal modifiers to fuse with Head, as in *the other two* and *these few here* (Huddleston and Pullum 2002, 415–16). Its analysis of *the few mistakes* assigns *the* to Det and *few* to Mod (Huddleston and Pullum 2002, 392). That dependent use supplies the counterpart for a Mod–Head analysis of independent *few* after an external determiner.

Figure 5 compares the resulting analyses of *the lucky few*. Both have an overt Det and a Nom modified by *lucky*. In the D-noun analysis, *few* fills Head. In the fusion analysis, its DP fills Mod–Head. The competing structure thus uses machinery already needed for adjectival fusion; it requires neither a silent noun nor conversion.

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

Figure 5: *The lucky few* with ordinary Head (first tree) and Mod–Head fusion (second tree). The determiner is separately realized in both. Internal structure within the article phrase and AdjP is suppressed.

Table 3 compares the Head relations across four constructions; §7.2 supplies the rules under both taxonomies.

Table 3: Head and dependent functions under matched analyses. Each independent expression is an NP; *the* fills Det wherever it appears. The ordinary-Head column applies to both taxonomies permitting ordinary determinative heads.

| Expression | Separate D with fusion | Ordinary determinative Head |
|:---|:---|:---|
| *few survivors* | *few*: Det; *survivors*: Head | Same functions |
| Independent *few* | *few*: Det–Head | *few*: Head |
| *the lucky few* | *few*: Mod–Head; *lucky*: Mod | *few*: Head; *lucky*: Mod |
| *the idle rich* | *rich*: Mod–Head; *idle*: Mod | Same fusion and modifier functions |

Fusion groups *the lucky few* with *the idle rich*, whereas ordinary headedness groups it with *the lucky survivors*. Ordinary headedness unifies *few* across its bare and externally determined uses, without alternating Det–Head and Mod–Head. Neither account gains coverage from this example alone. The comparison is between sharing a fusion construction across D and adjective, and sharing ordinary nominal headedness across determinative constructions.

Reducing fusion’s applications can simplify this description even when fusion remains available for adjectives. The advantage is the uniform treatment of *few*; its value depends on any additional conditions or lost generalizations elsewhere. Section 7.2 compares those costs while holding the lexical restrictions fixed.

> Note 9. Compare the theory of second best in Lipsey and Lancaster (1956, 11–12): under a constraint preventing an optimum, satisfying more optimality conditions needn’t improve the outcome. The analogy concerns interactions among grammatical choices, not a formal optimum for the grammar.

The constructed *the remaining three* extends the modifier pattern to cardinals. It doesn’t independently decide whether *three* is determinative or has a common-noun use: Reynolds (2026) argues for both uses of cardinals. Section 7.3 treats their unification as a consequence conditional on that analysis.

Relative-clause postmodification adds another nominal construction: *those who came*, *anyone who asks*, *everything that matters*, and, with books under discussion, *some that I saw*. *CGEL* describes relatives with demonstratives and compounds (Huddleston and Pullum 2002, 414, 422–23). These clauses modify the nominal expression containing the determinative, as they do in *people who came*; their availability isn’t limited to compounds.

Number supplies a further distinction between determinatives and adjectives. Independent *this*/*these* and *that*/*those* retain overt singular–plural contrasts. The human-class *the rich*, by contrast, is a plural NP whose adjective lacks nominal number inflection and still takes adverb modifiers: *the very rich* (Huddleston and Pullum 2002, 418). The strongest morphological evidence comes from the demonstrative paradigms. The singular and plural specifications of *each* and *several* concern lexical restrictions; NP number alone doesn’t distinguish the categories. Other determinatives, such as plural or non-count *some*, remain number-neutral.

Bare colour expressions and evaluative comparative subjects complicate a simple distributional boundary. *CGEL*’s *Henrietta likes red shirts, and I like blue* permits colour-noun ambiguity as well as possible reduction licensed by coordination; the attested *Bluer is better* establishes a bare comparative subject without settling its phrase category. These cases leave the wider comparison of argument distribution and head properties necessary.

> Note 10. The *blue*, *old* and *small* examples on *CGEL* p. 417 all occur in coordinated contrasts. *Bluer is better* accompanies a results colour scale in Stanford CS329X, [“Codeswitching LLMs”](https://web.stanford.edu/class/cs329x/slides/Lecture12_B_Codeswitching%20LLMs.pdf), slide 8 (accessed 10 September 2026). I interpret it as evaluating a degree of blueness. Subject function alone doesn’t establish NP status (Huddleston and Pullum 2002, 236).

The positive comparison therefore combines independent argument use with nominal number properties, partitives and modification. Adjectival constructions provide overlapping external functions while preserving distinct properties of their heads. This favours retaining adjectival fusion alongside ordinary determinative headedness.

## 4.5 Compounds and modifier domains

A more demanding modifier comparison is *hardly anyone present*. Payne et al. (2007, 581–83) assign *hardly* to DP structure and *present* to nominal structure. The compound *anyone* takes the premodifiers of its determinative base *any*: compare *hardly any writer present*. The adjective realizes a specialized restrictor function, restricted to post-head position and non-recursive. Figure 6 contrasts this account with an ordinary-Head analysis.

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

Figure 6: *Hardly anyone present* with ordinary Head (first tree) and fusion (second tree). Both post-head Mod positions realize the specialized restrictor. In the fusion tree, DP fills Det of NP and Head of Nom, following Payne et al. (2007, 582, (13d)). Modifier-phrase interiors are suppressed.

In the D-noun analysis, *anyone* inherits nominal projection from Noun and its premodifier permissions from its determinative base. The compound construction supplies the post-head restrictor permission, with the same position and non-recursion conditions as the fusion account. It doesn’t license a corresponding pre-head adjective. The compound’s ordinary argument use and exclusion of external determination are further lexical conditions; the premodifier and restrictor slots aren’t unrestricted Nom dependents.

The relative clauses illustrated above are ordinary postmodifiers, distinct from the specialized restrictor. When both occur, the relative follows it: *something useful that I found*. *CGEL* explicitly gives compounds the common noun’s range of ordinary postmodifiers while preserving this ordering condition (Huddleston and Pullum 2002, 423).

This division extends to *someone* and *everybody*: the compound family licenses nominal argument use and post-head restrictors, while each base supplies its own premodifier permissions. It doesn’t follow that *hardly* modifies every compound. CGELBank attests the post-head pattern in *I need something reliable and good looking*.

> Note 11. Sentence [`answers-20111024111513AAAQhAO_ans-0003`](https://github.com/nert-nlp/cgel/blob/d0a2c2d8c522b23d5aa879fc9cb94948f4285b2c/datasets/ewt-test_iaa50.cgel#L179-L181) in `ewt-test_iaa50.cgel`.

Fusion reuses the DP–Nom boundary to separate the two modifier domains. Ordinary headedness reuses nominal projection, locating both domains within Nom and assigning their restrictions to the determinative base and compound construction. Both accounts need the specialized restrictor condition. The trade-off concerns where the restrictions are stated, not whether they can be removed.

## 4.6 Predicative uses and their restrictions

The argument-use patterns above don’t extend uniformly to predicative complementation. *CGEL* records *Its advantages are several* and *Their enemies were many*, describing the latter pattern as uncommon and formal (Huddleston and Pullum 2002, 392, 395–96). Predicative use is available to only part of the determinative inventory; *every* and the articles remain excluded from these frames.

The comparison also depends on what the predication expresses. *She is a doctor* ascribes a property, whereas *That is Kim* identifies a person. *CGEL* excludes specifying *be* clauses from its noun–adjective diagnostic because phrases from other categories occur in them too (Huddleston and Pullum 2002, 536). Merely placing an expression after *be* therefore provides no uniform nounhood test.

Nominal grammar already licenses some expressions predicatively while restricting their argument uses. A bare-role NP such as *president* is licensed in *I’d like to be president*, but requires determination in the corresponding object use *I’d like to meet the president* (Huddleston and Pullum 2002, 328). Predicative and argument uses thus need separate conditions within Noun itself. The determinative asymmetries belong in that comparison; they don’t establish exclusion merely by departing from a common-noun substitution frame.

## 4.7 What the combined pattern supports

Independent uses, number, genitives, partitives and modification establish a systematic nominal profile. Together with the semantic and derivational relationships in §3, they connect determinatives with the other proposed noun subcategories in several domains. The properties are distributed across determinative families, just as common nouns, proper nouns and pronouns differ among themselves. The case for inclusion rests on this cumulative resemblance, with the premodifier and adjectival counterpatterns retained in the comparison.

Under the D-noun analysis, bare, partitive and externally determined uses inherit the ordinary Head relation of nominal projection. *CGEL* instead relates independent determinatives to dependent counterparts and distinguishes Det–Head from Mod–Head. Its compound analysis also uses the DP–Nom boundary to separate modifier domains. The D-noun analysis states those restrictions within nominal structure (§4.5).

The next two sections consider the hierarchy within Noun and the membership of its restricted forms. Section 7.2 then compares the grammatical organization under the three accounts.

# 5 Coordinate subcategories and inheritance

Should determinatives and pronouns be coordinate subcategories within Noun, or should determinatives belong inside pronoun? Reynolds (2021) compares determinative and pronoun profiles; its matrix contains no common or proper nouns. Distributional separation between the supplied groups doesn’t determine their taxonomic rank or test the proposed superordinate category. Even perfect recovery of the distinction would be compatible with shared nounhood. The original discussion likewise leaves a nested nominal analysis open.

The accompanying audit reproduces the published DISCO decomposition, but the clustering outcome varies with initialization and feature selection.

> Note 12. The accompanying [*Replication audit of the English determinative–pronoun feature matrix*](../matrix-audit.pdf) documents the discrepancy between the reported 232 features and the public 155-feature file, an extra feature dropped by the published clustering code, and the sensitivity results. The archived public file is retained unchanged.

The pronoun inventory in that study follows *CGEL*’s classification, whereas Hudson’s pronoun category includes the words he calls determiners. Comparing these hierarchies requires aligning their lexical inventories and asking which generalizations can be stated for each superordinate category.

An intermediate category would represent pronouns and determinatives as more closely related to each other than to common and proper nouns. Assessing that relationship requires comparing their full profiles. Nominal projection already applies to all four subcategories, while personal pronouns’ case, reflexive and person contrasts and determinatives’ quantificational and modifier patterns support local distinctions under either hierarchy.

Reduced descriptive content and contextual interpretation are shared by many pronouns and determinatives. The coordinate analysis can record these interpretive properties through features or cross-classification; they don’t by themselves require an intermediate lexical category.

Pro-form gender supplies a more specific interpretive comparison. Reynolds (2025) proposes a personhood-based system spanning pronouns and determinatives. Personal reference links pronouns such as *she* with compound determinatives such as *somebody*; non-personal reference links *it* with *something*. These constraints concern how the referent is construed. They provide a shared generalization for nominal pro-forms, but don’t decide between coordinate and nested noun subcategories. The broader pro-form system also includes non-nominal expressions, so gender alone doesn’t delimit Noun.

Restrictions on determination and attributive modification provide syntactic candidates, but they also occur outside the proposed grouping. In their primary use, proper names don’t select freely from the determiner system, and their adjectival embellishments are restricted (Huddleston and Pullum 2002, 517, 519–20). These properties distinguish more than pronouns and determinatives from common nouns.

Determination also differs within the proposed intermediate category. Determinatives permit external determination in a range of independent quantificational constructions: *the few*, *the many*, *the two*, *these three*. The permissions vary by item and often require further modification; *CGEL* gives *these few here* and *the many who did* (Huddleston and Pullum 2002, 415–16). Pronouns admit external determination only marginally, and internal premodification is restricted, as in *poor old me* (Huddleston and Pullum 2002, 429–30). These restrictions thus cross-cut the proposed grouping and vary within it.

I place determinative alongside pronoun because their shared nominal properties coexist with different centres of grammatical organization. Pronouns centre on person, case, reflexivity and contextual reference; determinatives centre on quantification, determination and their associated modifier patterns. Their affinities also extend to common and proper nouns. Coordinate subcategories represent this combination, while further evidence could support a broader pronoun grouping. Section 6 turns to the membership of the articles and other restricted forms.

# 6 The articles and other restricted members

Why classify the articles *the* and *a* as nouns if they can’t stand independently? Independent uses motivate the D-noun analysis of *some*, *this* and *many*, but the articles require a different argument. *Every* is restricted too, while *no* has the distinct independent form *none* (Huddleston and Pullum 2002, 371–72, 410–11).

> Note 13. The restriction concerns ordinary argument use. In *the bigger the better*, *CGEL* analyses *the* as a modifier within a comparative phrase (Huddleston and Pullum 2002, 1131–32, 1135–36). This dependent use outside Det leaves the restriction on ordinary argument use intact.

*CGEL*’s treatment of *my* supplies a precedent for restricted membership within Noun (Huddleston and Pullum 2002, 470–71). The pronoun’s paradigm supports its membership despite its lack of *mine*’s independent distribution. For articles, the corresponding positive evidence is integration into determinative; their nounhood depends on the category-level argument.

Retaining a restricted member requires three kinds of support. First, it should be paradigmatically integrated with independently identified members. Second, it should participate in the category’s characteristic semantic and grammatical contrasts. Third, its missing uses should form a local restriction while the positive connections remain. Calling an item defective summarizes that pattern; it doesn’t supply an argument for membership by itself.

The articles meet these conditions within determinative. First, they contrast with demonstratives and quantifiers before common-noun nominals: *the/a/this/every book*. Second, they participate in the same system of definiteness, number and count restrictions: *the* permits singular, plural and non-count targets, while *a* selects a singular count target. Third, their lack of ordinary independent uses leaves that determining pattern intact. These connections support determinative membership, rather than establishing nounhood independently.

*Every* has further connections beyond the restricted article set proposed by Spinillo (2004). Like *each*, it expresses universal quantification and selects singular count nominals: *every teacher*, *each teacher*. Unlike *each*, it lacks ordinary independent use. It also permits modification by *almost* and *nearly*. These connections support retaining *every* with the quantifiers.

The argument for retaining the articles is synchronic. Grammaticalization supplies background: Lyons (1999, 331–36) discusses the development of definite articles from demonstratives and of articles expressing cardinality from numerals. These histories can explain changes in content and use, but don’t establish the synchronic classification.

A separate article category would gain support from a cluster of synchronic restrictions shared by *the*, *a* and *every*, absent elsewhere in Noun, and otherwise requiring repeated exceptions. Lack of independent argument use alone doesn’t supply that cluster. The comparison concerns the allocation of generalizations; an additional restriction needn’t by itself overturn the membership analysis. All the grammars compared in §7.2 retain the articles’ restriction on ordinary argument use.

# 7 Structural consequences and grammatical economy

## 7.1 A shared phrase type in determiner function

In *some apples* and *Kim’s apples*, the determining phrases share the NP category under both ordinary-Head accounts: D-noun and separate D. *CGEL* instead distinguishes DP from genitive NP. It also admits a restricted range of plain-case NPs and PPs as determiners, as in *what size hat* and *over thirty ties* (Huddleston and Pullum 2002, Ch. 5, §4). The phrase types are:

```text
CGEL:  Det:{DP,NP,PP}
Both ordinary-Head accounts:  Det:{NP,PP}
```

This shares a phrase type without shortening the selectional disjunction: determinative-headed, genitive and other licensed NPs still require separate identification. *CGEL* already states definiteness and the single-Det restriction functionally, so reclassification doesn’t derive them. The substantive comparison concerns whether determining phrases reuse nominal projection once their different restrictions are held fixed. Fewer phrase labels alone don’t establish grammatical economy; §7.2 displays the rules that must be compared.

## 7.2 A matched descriptive fragment

A grammatical fragment is a set of rules for a specified range of constructions. Here it covers determination, ordinary subject and object uses, partitives, and the modifier and compound comparisons in §4. It compares the D-noun analysis with two separate-D alternatives: ordinary headedness and fusion. All receive the same lexical restrictions and constructed judgments. The predicative constructions in §4.6 fall outside the fragment.

Table 4 records use permissions: whether a form, on a given reading, can head a phrase in determiner, subject or object function. Argument use covers the subject and object NPs in examples such as *Some left* and *I saw some*. Quotation, metalinguistic naming and subordinate-clause uses of dependent genitives fall outside the fragment. Noun membership doesn’t itself grant a use permission.

Table 4: Shared permissions in the fragment. For *some*, the target column concerns its unstressed use before a noun. The inventory is deliberately limited to the displayed constructions.

| Form | Det use | Argument use | Target in the Det construction |
|:---|:--:|:--:|:---|
| *the* | yes | no | Singular or plural; count or non-count |
| *a*, *every* | yes | no | Singular count nominal |
| *some* | yes | yes | Plural count or non-count nominal |
| *few* | yes | yes | Plural count nominal |
| *my* | yes | no | No number/count restriction in this fragment |
| *she* | no | yes | None |

Further constructional restrictions apply: *she* is a subject form, whereas the corresponding ordinary object form is *her*. The target restrictions concern the common-noun nominal being determined: *a* requires a singular count target such as *book* in *a book*.

Table 5 locates the three accounts. Comparing the ordinary-Head accounts holds projection fixed while varying taxonomy. Comparing the separate-D accounts holds taxonomy fixed while varying headedness.

Table 5: Three accounts retaining the permissions in Table 4, the modifier restrictions and the compound conditions.

| Account | Primary taxonomy | Simple independent determinative |
|:---|:---|:---|
| D-noun analysis | D inside Noun | N–Nom–NP projection with Head function |
| Separate D, ordinary Head | D outside Noun | D–Nom–NP through cross-category projection |
| *CGEL*: separate D, fusion | D outside Noun | NP distribution through Det–Head |

The D-noun analysis applies nominal projection to determinatives through their membership in Noun. A separate condition checks use permissions. In the schemata below, `h` identifies the lexical head throughout its projection; parentheses mark optional dependents. The subscripts on Mod distinguish pre-head and post-head positions of the same modifier function. The head’s entry and construction restrict every dependent.

```text
Nom_h → (Mod_pre)  Head:N_h  (Comp)  (Mod_post)
NP_h → (Det)  Head:Nom_h
licensed(NP_h,f,c)  ⇔  f∈ U_h\ ∧\ C_h(f,c)
```

Here `U_h` is the head’s set of use permissions, `f` is the NP’s function, and `C_h` checks the lexical and constructional conditions in context `c`. For Det use, these include compatibility with the target nominal; for an argument headed by a singular count common noun, they include required determination. Optionality in the second rule doesn’t override those conditions.

In *some apples*, *some* heads an NP whose Det permission and plural-count target requirement are satisfied. *Apples* heads the outer Nom, which heads the NP. In *Some left*, *some* heads an NP whose argument permission is satisfied. *Every apple* passes the Det and singular-count checks; ordinary independent \**Every arrived* fails the argument-permission check. *The apple* and \**The arrived* differ in the same way.

Each NP’s use permissions follow its own head. In *the apple*, the article’s Det permission licenses the dependent NP headed by *the*. The outer NP takes its argument permission from *apple*, whose requirement for determination is satisfied by the article.

A singular count common noun such as *book* faces a different restriction from an article. In *a book*, its requirement for determination is satisfied; bare \**Book arrived* leaves that requirement unsatisfied. *Books arrived* has no such requirement. Requiring determination for a common noun doesn’t itself block an article-headed NP from argument use. An article’s exclusion from argument use must still be stated separately.

Partitives and modifiers require further lexical conditions. *Some* and *few* permit a partitive *of*-phrase within their nominal projection. *Almost* can modify *every* in *almost every teacher*; that permission doesn’t license *experienced* as a modifier of *every*. The construction *the lucky few* permits the external determiner and adjectival modifier shown in Figure 5. None of these permissions transfers automatically to every determinative noun.

Keeping ordinary headedness while retaining primary D gives the strongest separate-D alternative. It retains the NP and use-permission rules, but replaces the lexical-head restriction in Nom with:

```text
Nom_h→(Mod_pre)  Head:{N_h,D_h}  (Comp)  (Mod_post)
```

This projection applies to dependent as well as independent determinatives, eliminating DP from the fragment while retaining primary D. Determiner selection still identifies D-headed NPs and suitable genitives. In *the lucky few*, *few* is D in ordinary Head function. In *hardly anyone present*, the determinative base and compound construction supply the same modifier restrictions as the D-noun account. Adjectival Mod–Head fusion remains available in both.

The separate-D fusion account relates independent determinatives to their dependent counterparts. In addition to nominal projection for nouns, it uses DP projection and permits a DP to realize a fused function in nominal structure. The partitive complement and compound restrictor belong to Nom, following the trees in *CGEL* and Payne et al. (2007, 582):

```text
DP_h → (Mod_pre)  Head:D_h  (Comp)
Nom_h → (Mod_pre)  F:DP_h  (Comp)  (Mod_post)
F∈{Det–Head,Mod–Head}
```

The ordinary NP rule embeds this Nom. Det–Head jointly realizes Det of NP and Head of Nom, excluding a second Det; Mod–Head fills an internal modifier’s function and Head of Nom, allowing external determination. Lexical and constructional conditions select the fused function and permitted dependents. These schemata cover independent *few*, *few of them*, *the lucky few* and *hardly anyone present*.

The ordinary-Head accounts thus share nominal projection and Head relations; these benefits don’t uniquely favour inclusion within Noun. Dependent determinatives acquire a Nom layer in both. The taxonomic difference lies in whether the lexical head enters this structure by inheritance from Noun or by a rule admitting both N and D.

A grammar with Hudson’s nested classification can use the same permissions and projection rules. Holding those rules fixed, placing the broader pronoun category on determinative’s inheritance path from Noun leaves the fragment’s judgments unchanged. Agreement on these judgments leaves the broader pronoun category open.

## 7.3 Existing restrictions, additional costs and consequences

The combined semantic, syntactic and morphological profile motivates the fourfold grouping. The fragment shows how that grouping can be represented while retaining the relevant judgments. Its strongest separate-D rival shares the nominal projection rules. The taxonomic judgment therefore reaches beyond the fragment: it weighs the range and organization of the shared properties against the recurring differences between the proposed subcategories.

The cost of this change needs separating from restrictions already present in the grammar. Common nouns, proper nouns and pronouns already differ in determination and permitted modifiers (Table 2). Preserving those conditions is no additional cost of including determinatives. Likewise, the separate-D grammar already restricts adverbial modification and independent use within D. Moving those restrictions inside Noun doesn’t create them.

The systematic premodifier contrast in §3.3 identifies an additional cost. A restriction normally stated for primary Noun now applies to specified noun subcategories, while determinative nouns retain their adverbial premodifiers. The attributive *almost textbook* exception limits the original generalization but doesn’t erase that change. In compounds, inherited premodifier permissions also remain distinct from the post-head restrictor construction (§4.5). Any claim of net economy has to account for these choices.

I favour inclusion because determinatives’ nominal connections extend across the domains considered here. Their argument and determiner uses, partitives and postmodification align with nominal constructions; their deictic and gender distinctions connect with pronouns; number and genitive marking connect some members with other nouns. Grade and adverbial premodification support a distinctive determinative profile. Taken together, I judge these similarities and differences better represented by subcategories of a broad Noun category.

Further comparisons can sharpen this judgment. Holding the inventory, constructions and readings fixed permits assessment of which grammar needs additional rules after shared restrictions have been factored out. Inheritance gains support where new constructions reuse nominal rules; separate D gains support where its boundary captures recurring restrictions otherwise restated within Noun. Such results would add evidence about the organization of the profile, alongside the semantic and morphological comparisons.

Cardinals illustrate the reduction in overlap between primary categories. Reynolds (2026) distinguishes determinative uses such as *ten men*, proper-noun uses such as *Room 101*, and common-noun uses such as *tens of pens*. Under the D-noun analysis, these uses fall within Noun: cardinals no longer span separate primary determinative and noun categories. Their differences remain at the subcategory and construction levels. The argument doesn’t extend to ordinals, which that study analyses as adjectives, or turn complex numeral phrases into single lexemes.

Complex cardinals also separate category from function. In *two hundred books*, the whole *two hundred* fills Det; internally, *two* modifies the magnitude head *hundred* (Reynolds 2026, sec. 4). In *these two hundred books*, *these* fills Det and *two hundred* is an internal modifier. Including determinatives within Noun preserves these relations. One Det function doesn’t entail a limit of one determinative lexeme per NP.

If determinative-headed and genitive expressions require different projection rules after their independently motivated restrictions are held fixed, the shared-projection proposal in §7.1 loses its advantage. That would favour separate phrase types. Retaining a separate primary D requires the further case that the category boundary captures the recurring differences better than a determinative subcategory within Noun.

# 8 Conclusion

I propose four coordinate subcategories of Noun in English: common noun, proper noun, pronoun and determinative. The proposal rests on their overlapping profiles across semantics, syntax and morphology. Shared argument and determiner uses, nominal dependents, referential distinctions, number and genitive marking connect the groups in different combinations. Determinatives’ quantitative meanings, grade and premodifier permissions support a distinct subcategory within this broader organization.

This is a cumulative classificatory judgment. The nominal connections have to be weighed alongside adjectival affinities and the systematic distributional differences, including those of pronouns. I judge the combined similarities substantial enough for one superordinate category, while the differences justify its internal divisions. The articles’ membership rests on their integration into the determinative paradigm and its semantic and grammatical contrasts.

Through membership in Noun, determinatives inherit nominal projection and ordinary Head relations across bare, partitive and externally determined uses. This also brings the principal realizations of determiner function within NP and places cardinal uses within one primary category. A separate-D grammar can share some of these structures, and both analyses retain lexical and constructional restrictions. Their comparative economy is a further consideration in assessing the broader grammatical grouping.

# Data and analysis materials

The accompanying supplements are [*Replication audit of the English determinative–pronoun feature matrix*](../matrix-audit.pdf) and [*CGELBank concordance and extraction notes*](../corpus-documentation.pdf). The `analysis/` directory preserves their input files, provenance records, scripts, numerical outputs and sentence concordance. Its README identifies the files and reproduction procedures.

Acknowledgements. For the September 2026 revision, GPT-6 (Astra), Claude Opus 5, Claude Haiku 4.5 and GLM-5.3-Flash assisted drafting, source retrieval, script development or critical review; GPT-5.6 (Sol) checked numerical outputs. The accompanying materials record the tools and their uses. Responsibility for the analysis is mine.

# References

Abney, Steven P. 1987. “The English Noun Phrase in Its Sentential Aspect.” PhD thesis, Massachusetts Institute of Technology.

Bruening, Benjamin. 2020. “The Head of the Nominal Is N, Not D: N-to-D Movement, Hybrid Agreement, and Conventionalized Expressions.” *Glossa: A Journal of General Linguistics* 5 (1). <https://doi.org/10.5334/gjgl.1031>.

Huddleston, Rodney, and Geoffrey K. Pullum. 2002. *The Cambridge Grammar of the English Language*. Cambridge University Press. <https://doi.org/10.1017/9781316423530>.

Huddleston, Rodney, Geoffrey K. Pullum, and Brett Reynolds. 2022. *A Student’s Introduction to English Grammar*. 2nd ed. Cambridge University Press. <https://doi.org/10.1017/9781009085748>.

Hudson, Richard. 2004. “Are Determiners Heads?” *Functions of Language* 11 (1): 7–42. <https://doi.org/10.1075/fol.11.1.03hud>.

Hudson, Richard. 2010. *An Introduction to Word Grammar*. Cambridge University Press.

Lipsey, R. G., and Kelvin Lancaster. 1956. “The General Theory of Second Best.” *The Review of Economic Studies* 24 (1): 11–32. <https://doi.org/10.2307/2296233>.

Lyons, Christopher. 1999. *Definiteness*. Cambridge University Press. <https://doi.org/10.1017/cbo9780511605789>.

Lyons, John. 1968. *Introduction to Theoretical Linguistics*. Cambridge University Press. <https://doi.org/10.1017/CBO9781139165570>.

Palmer, Harold E. 1924. *A Grammar of Spoken English on a Strictly Phonetic Basis*. W. Heffer & Sons Ltd.

Payne, John, Rodney Huddleston, and Geoffrey K. Pullum. 2007. “Fusion of Functions: The Syntax of *Once*, *Twice* and *Thrice*.” *Journal of Linguistics* 43 (3): 565–603. <https://doi.org/10.1017/S002222670700477X>.

Payne, John, Rodney Huddleston, and Geoffrey K. Pullum. 2010. “<span class="nocase">The distribution and category status of adjectives and adverbs</span>.” *Word Structure* 3 (1): 31–81. <https://doi.org/10.3366/E1750124510000486>.

Payne, John, Geoffrey K. Pullum, Barbara C. Scholz, and Eva Berlage. 2013. “Anaphoric *One* and Its Implications.” *Language* 89 (4): 794–829. <https://doi.org/10.1353/lan.2013.0071>.

Postal, Paul M. 1966. “On so-Called “Pronouns” in English.” In *Report of the Seventeenth Annual Round Table Meeting on Linguistics and Language Studies*, edited by Francis P. Dinneen. Monograph Series on Languages and Linguistics 19. Georgetown University Press.

Pullum, Geoffrey K., and Philip Miller. 2022. *NPs Versus DPs: Why Chomsky Was Right*. LingBuzz 006845. <https://lingbuzz.net/lingbuzz/006845>.

Pullum, Geoffrey K., and Deirdre Wilson. 1977. “Autonomous Syntax and the Analysis of Auxiliaries.” *Language* 53 (4): 741–88. <https://doi.org/10.2307/412911>.

Reynolds, Brett. 2021. “Quantifying the Differences Between Lexical Categories: The Case of Pronouns and Determinatives in English.” *Cadernos de Linguística* 2 (3). <https://doi.org/10.25189/2675-4916.2021.V2.N3.ID399>.

Reynolds, Brett. 2025. “Personhood and Pro-Forms: A Hierarchical Analysis of Gender in Modern English.” Unpublished manuscript.

Reynolds, Brett. 2026. “The Lexicon–Syntax Boundary in English Numerals: Cardinals, Ordinals, and Fractionals.” *English Language and Linguistics*, 1–19. <https://doi.org/10.1017/S1360674325100518>.

Reynolds, Brett, Aryaman Arora, and Nathan Schneider. 2023. “Unified Syntactic Annotation of English in the CGEL Framework.” In *Proceedings of the 17th Linguistic Annotation Workshop (LAW-XVII)*, edited by Jakob Prange and Annemarie Friedrich. Association for Computational Linguistics. <https://doi.org/10.18653/v1/2023.law-1.22>.

Sommerstein, Alan H. 1972. “On the so-Called Definite Article in English.” *Linguistic Inquiry* 3 (2): 197–209. <https://www.jstor.org/stable/4177701>.

Spinillo, Mariangela Galvão. 2004. “Reconceptualising the English Determiner Class.” {PhD} thesis, University College London. <https://discovery.ucl.ac.uk/id/eprint/10101595/>.

