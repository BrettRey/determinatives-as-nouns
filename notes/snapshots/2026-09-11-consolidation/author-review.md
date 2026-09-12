# Determinatives as nouns in English

Brett Reynolds — 11 September 2026 working draft

Revised after your completed author review. Section 5 has been rewritten, inflection has its own subsection, and the modifier analysis distinguishes peripheral and internal attachment. Trees and schemata are shown as text; footnotes appear beside their paragraphs. [Typeset PDF](../determinatives-as-nouns.pdf) · [Response to all review points](passes/2026-09-11-final-author-review.md).

# Abstract

I argue that English determinatives belong within Noun alongside common nouns, proper nouns, and pronouns. Their combined semantic, syntactic, and morphological profile supports the grouping; quantificational common nouns provide particularly close connections. Adverbial premodification and grade distinguish determinatives within it. I examine restricted articles and determinatives’ degree-modifier uses. The proposed hierarchy makes nominal projection inherited, unifying bare, partitive, and externally determined uses under ordinary Head structure. A matched grammatical fragment compares separate-D alternatives and identifies the costs of restricting modifier generalizations to subcategories.

**Keywords:** determinatives, nouns, lexical categories, noun phrases, English

# 1 The question

What is the categorial relationship among words such as *some*, *me*, *apple*, and *Brett*? I argue that all four are nouns: determinatives form a coordinate subcategory alongside common nouns, proper nouns, and pronouns. I write the superordinate category as Noun and call the fourfold proposal the determinative-noun or D-noun analysis.

I adopt the general framework of *The Cambridge grammar of the English language* (*CGEL*; Huddleston and Pullum 2002). Unlike *CGEL*, though, I include determinatives within Noun. The claims concern synchronic English lexical categories.

> Note 1. I treat these categories as language-specific: a categorization supported by another language’s grammar doesn’t determine the English categorization.

I use determinative for the category containing articles, demonstratives, and quantifiers such as *the*, *this*, *some*, *every*, and *many*. I reserve determiner for the syntactic function within the noun phrase characteristically performed by phrases headed by these words. This distinction separates what kind of word *some* is from what syntactic relationships its phrase participates in.

> Note 2. For a fuller inventory, see the online [“List of determinatives in English”](https://www.cambridge.org/highereducation/api/resources/2AC8DF5CA558F8A6FCDFACD0EAF8EA08) accompanying Huddleston et al. (2022).

*CGEL* already includes pronouns within Noun on the basis of their phrases’ functions, despite differences from common and proper nouns in inflection and dependents (Huddleston and Pullum 2002, 327–28). The inclusion of auxiliaries within Verb supplies a further precedent for preserving distinctive properties within a broader lexical category (Pullum and Wilson 1977). The question is whether determinatives’ combined semantic, syntactic, and morphological profile warrants the corresponding extension of Noun.

In the D-noun analysis, determinatives inherit the nominal projection rules of Noun. Under these rules, a determinative heads a nominal (Nom), which heads an NP, just as common nouns, proper nouns, and pronouns do. Nom contains the head and its internal dependents, excluding an external determiner. Lexical restrictions govern which uses are available.

Figure 1 compares *CGEL* with the D-noun analysis for *take some apples* and *take some*. Both keep *some* in one lexical category. In *CGEL*, independent *some* jointly fills determiner and head functions, a fusion of functions (Huddleston and Pullum 2002, 410–12). In the D-noun analysis, *some* heads its own NP through a Nom in both uses; that NP functions as determiner before *apples* and as object in *take some*.

> Note 3. As a syntactic representation, fusion of functions appears to have seen little adoption outside work based on *CGEL*.

Here DP abbreviates determinative phrase, as in *CGEL*, not to be confused with the DP of the DP hypothesis, where D heads the whole expression *some apples* (Abney 1987; §2.1). The D-noun analysis keeps *apples* as that expression’s ultimate head.

CGEL: take some apples

```text
VP
├── Head: V
│   │
│   take
└── Obj: NP
    ├── Det: DP
    │   │
    │   Head: D
    │   │
    │   some
    └── Head: Nom
        │
        Head: N_common
        │
        apples
```

CGEL: take some

```text
VP
├── Head: V
│   │
│   take
└── Obj: NP ─────────┐
    │                │
    Head: Nom        │
    │                │
    Det–Head: DP ◄───┘
    │
    Head: D
    │
    some
```

D-noun analysis: take some apples

```text
VP
├── Head: V
│   │
│   take
└── Obj: NP
    ├── Det: NP
    │   │
    │   Head: Nom
    │   │
    │   Head: N_D
    │   │
    │   some
    └── Head: Nom
        │
        Head: N_common
        │
        apples
```

D-noun analysis: take some

```text
VP
├── Head: V
│   │
│   take
└── Obj: NP
    │
    Head: Nom
    │
    Head: N_D
    │
    some
```

Figure 1: The first pair shows *CGEL*; the second pair shows the D-noun analysis. Each pair compares *take some apples* with *take some*. In the second tree, DP fills Det of NP and Head of Nom. In the third and fourth trees, *some* heads an NP through the same `N_D`–Nom–NP sequence; that NP functions as Det in the third tree and Obj in the fourth.

The same ordinary Head structure extends to bare *few*, partitive *few of them*, and externally determined *the lucky few*. *CGEL* divides these between Det–Head and Mod–Head fusion. Their unification is one structural consequence of the D-noun proposal. Another is that replacing DP with NP consolidates the phrase types functioning as determiner: determinatives join genitives and other nominal determiners.

The argument proceeds from categorization to its consequences. Section 2.2 places the proposal among earlier accounts; §3 compares the four profiles, and §4 examines the nominal constructions. Sections 5 and 6 address subcategory rank and difficult members. The matched fragment in §7.2 then compares the resulting grammar with separate-D alternatives, holding judgments and lexical restrictions fixed.

# 2 Categorization, headedness, and function

## 2.1 Category, function, and phrase structure

Lexical categories and syntactic functions cut across one another. An NP can function as determiner, as in *<u>Kim’s</u> book*, and a determinative-headed phrase can function as modifier, as in *the <u>many</u> people* (Payne et al. 2010; Pullum and Miller 2022).

The question of lexical categorization is distinct from the headedness question associated with the DP hypothesis of Abney (1987). Under that hypothesis, D heads expressions such as *some apples*. I retain noun-headed NPs and reject the DP analysis for English, following the arguments of Pullum and Miller (2022) and Bruening (2020).

Category membership doesn’t remove lexical restrictions. *Every apple* is grammatical, but \**I’ll take every* isn’t an ordinary way to accept apples. The fragment retains that restriction (§7.2).

## 2.2 Taxonomic and structural alternatives

Keeping a word in one category across dependent and independent uses leaves its taxonomic position open. As Lyons (1968, 232–35) observes, distribution can be compared at different levels of categorization: two expressions may belong together at one level and differ at a more specific level. Table 1 distinguishes the selected authors’ proposals, their analytical levels, and several logical alternatives. The D-noun analysis differs from *CGEL* by including determinative within Noun, and from Hudson by placing it alongside pronoun.

Table 1: Selected accounts and logical alternatives. The earlier proposals differ in scope and representational level; they don’t all specify a surface taxonomy. The prose gives sources and inventory qualifications.

| Account | Proposed relationship | Level or status |
|:---|:---|:---|
| Palmer | Determinative adjectives grouped with pronouns. | Lexical grouping; inclusive Noun unspecified |
| Postal | Personal pronouns analysed as articles, with deeper noun features. | Intermediate and underlying representations |
| Sommerstein | Definite article and personal pronouns given NP structure. | Underlying representation |
| Lyons | Articles, demonstratives, and personal pronouns linked by definiteness and deixis. | Semantic relationship |
| *CGEL* | Pronoun within Noun; determinative separate. | Lexical taxonomy |
| Hudson | Determiners within pronoun, which is within noun. | Lexical taxonomy |
| Spinillo | Determinatives redistributed; *the*, *a*, and *every* retained as articles. | Lexical recategorization |
| D-noun analysis | Common noun, proper noun, pronoun, and determinative coordinate within Noun. | Proposed taxonomy |
| Logical alternative | Noun, pronoun, and determinative separate. | For comparison |
| Logical alternative | Determinative within Noun; pronoun separate. | For comparison |
| Logical alternative | Pronoun within determinative, which is within Noun. | For comparison |
| Logical alternative | Pronoun within proper noun; determinative within common noun. | For comparison |

Palmer (1924, 24) proposed placing “determinative adjectives” with pronouns. He contrasted them with qualifying adjectives, which permit predicative use, comparison, and adverbial modification. Most determinatives, he observed, can “be used indifferently as pronouns or as modifiers of nouns”. Lyons (1968, 279) adds a semantic connection: articles, demonstratives, and personal pronouns share definiteness and deictic contrasts.

Postal (1966) develops the article–pronoun connection through English reflexives and combinations such as *we men*. His morphological evidence for the noun *self* includes *selfish*, *selfless*, and the plural alternation *self*/*selves*; he analyses the preceding pronominal material as an article. The categorization depends on representational level: article segments occur at intermediate stages, their deepest counterparts are features of nouns, and surface pronouns can receive derivative Noun status.

Sommerstein (1972, 197–203) argues in the opposite direction, giving the definite article and personal pronouns underlying NP structure. His English comparison includes the count restriction on anaphoric *one*, whereas *it* can refer to a quantity of a substance. He also observes that noun status for *self* doesn’t decide whether the preceding element is an article or a genitive pronoun.

> Note 4. Payne et al. (2013, 797–98) analyse anaphoric *one* as a common count noun, distinct from determinative *one* and personal pronoun *one*.

These predecessors challenge a fundamental article–pronoun separation, but leave the full determinative inventory uncategorized. Its contrasts in grade, modification, complementation, and restricted independent use extend the comparison beyond their proposals.

Hudson makes taxonomic inclusion explicit. His noun category contains common noun, proper noun, and pronoun (Hudson 2010, 253–54); a determiner is a pronoun whose valency permits the relevant common-noun dependent (Hudson 2004, 9–10). The word’s category remains constant across independent and dependent uses, which differ in their permitted dependents.

Hudson’s criteria centre on licensing a singular count common noun and on mutual exclusion in that use. He sets aside *all*, cardinal numerals, and quantifiers restricted to plural or non-count nouns (Hudson 2004, 9–10). Their place in his taxonomy remains unsettled by those criteria. Extending the pronoun analysis to *CGEL*’s fuller inventory requires comparing its modifier selection, grade, and quantitative meanings with the existing pronouns’ properties.

Hudson also distinguishes dependency from external headedness. He argues that determiner and common noun depend on each other, although only one connects the phrase to its surroundings (Hudson 2004, 7–8). His temporal adjunct evidence supports common-noun headedness: *I saw him that day* is possible, whereas \**I saw him that point in time* isn’t, despite the similar temporal meanings (Hudson 2004, 10–12). The lexical noun matters, as well as the construction’s determiner restrictions.

The reciprocal selection facts are substantial: a singular count noun normally requires determination, while *every* requires an overt nominal and *some* doesn’t. They establish conditions in both directions. In the present phrase-structure analysis, the noun can remain Head while both constituents impose such conditions (§7.2). Including determinatives within Noun neither explains away the selection facts nor requires mutual headedness; it concerns the selecting words’ superordinate category.

Spinillo (2004, 153–58) instead retains *the*, *a*, and *every* as an expanded article category and redistributes other determinatives among adjectives and pronouns (Spinillo 2004, 194–95). Her grounds include dependence on a following nominal, lack of predicative and partitive uses, and limited descriptive content. She also recognizes differences within the article trio. Section 6 assesses this cluster against the connections each member retains with the wider inventory.

Spinillo (2004, 140–44) draws an analogy with verbs and prepositions whose complements can be omitted. For demonstratives and quantifiers such as *some* and *all*, occurrence before a nominal (*some teachers*) alternates with occurrence without one (*some left*). The analogy supports category continuity, but leaves the category to be established: *CGEL*, Hudson, and the D-noun analysis can all preserve it.

# 3 The D-noun analysis

## 3.1 The basis for a broader Noun category

Table 2 compares the four proposed subcategories. The issue is the combined profile: how broadly a property occurs within each group, where it recurs across constructions, and how specifically it connects determinatives with nouns or adjectives.

Table 2: Representative profiles, with ranges rather than universal properties. Argument and Det functions concern whole phrases; modifier examples involve Nom or NP as appropriate. Construction type is distinct from function. The determinative inventory includes independent *what* and relative *which*, as explained in §6.2.

| Dimension | Common noun | Proper noun | Pronoun | Determinative |
|:---|:---|:---|:---|:---|
| Inventory | Open | Open to new names | Closed | Closed |
| Argument / Det functions | NP arguments; genitive Det | NP arguments; genitive Det | NP arguments; genitive Det | NP arguments; plain and genitive Det |
| Modifier / adjunct functions | *dog houses*; *that day* | *Canada Day*; *Sunday* | Emphatic reflexives in both functions | *the few people*; degree adjuncts |
| Interrogative / relative constructions | Through another constituent, e.g. *which book* | Through another constituent | *who*, *whose* | *which*, *what*, and *-ever* forms |
| Meaning | Descriptive properties and relations | Naming in primary uses | Person, deixis, anaphora, and interrogation | Quantification, definiteness, deixis, and interrogation |
| Pro-form gender | Descriptions shape referent construal | Names identify referents construed by gender | Gender-sensitive forms | Gender-sensitive forms and constructions |
| Inflection | Number and genitive | Genitive; restricted number | Case, including genitive; reflexive forms | Number; grade; genitive; *no*/*none* |
| Accepts determination | Broad contrasts; singular count arguments normally require it | Restricted in primary naming uses | Normally excluded | Lexically restricted: *the few*, *these three* |
| Internal modification | Productive AdjP and nominal premodifiers; relative postmodifiers | Restricted AdjP premodifiers and embellishments | Restricted AdjP premodifiers and relative postmodifiers | AdvP and D premodifiers; nominal postmodifiers; *the lucky few* |
| Complementation | Selected PPs and clauses | Not characteristic of primary naming uses | Normally absent | Partitive *of*-PPs; comparative *than*-phrases |

Meaning and reference vary within Noun. *Apple* describes a category; *Kim*, in its primary naming use, identifies through a name; *she* depends on context. Determinatives range from deictic *this* to quantitative *many* and universal *every* (Huddleston and Pullum 2002, 358–60, 370–405, 425–28, 515–21). Deixis connects demonstratives with pronouns, while quantity connects determinatives with common nouns such as *number* and *majority*.

These meanings aren’t exclusive to nouns. Adjectives such as *singular* and *plural* also concern number; *proximate* and *distal* describe spatial relations relevant to demonstrative contrasts, though spatial meaning needn’t itself be deictic. Nor does Noun imply close semantic similarity throughout: *every* quantifies over a nominal restriction, while *Kim* identifies an individual. Semantic affinities contribute to the comparison without settling its boundaries.

Pro-form gender (Reynolds 2025) connects these ways of referring. Descriptions such as *the woman* and names such as *Kim* identify referents whose construal bears on pro-form choice. Pronouns and determinatives express contrasts between personal *she*/*somebody* and non-personal *it*/*something*. Relative *who*/*which* supplies another contrast; independent *what* raises a categorization question taken up in §6.2.

External syntax supplies a broad overlap in the functions available to the phrases. *CGEL* makes this the stated ground for including pronouns within Noun (Huddleston and Pullum 2002, 327). A range of determinatives likewise occurs in subject, object, and complement-of-preposition positions without another overt nominal head. The examples in §4.1 compare these uses across all four proposed subcategories.

Modifier and adjunct functions also cut across the groups. Compare the modifiers in *dog houses*, *Canada Day*, *the manager herself*, and *the few people*. Emphatic *herself* also functions as a clause adjunct in *The manager detected the error herself* (Huddleston and Pullum 2002, 1496–97). Temporal NPs such as *that day* and *Sunday* supply adjuncts, as does degree *enough* in *I hadn’t prepared enough* (§6.3). These are shared functions with construction-specific distributions.

Interrogative and relative properties must be distinguished from those functions. An interrogative object may be headed by a pronoun (*who*) or a common noun (*which book*); the latter obtains its interrogative property from a dependent. Neither the object function nor the interrogative construction determines the lexical head’s category.

Overlap with adjectives likewise needs phrase levels kept distinct. Both *the people* and *the rich* are NPs in *CGEL*, though only the former has a noun as lexical head. In *a soccer/round ball*, Nom and AdjP share modifier function; in *Jones became president/ill*, NP and AdjP share predicative complement function. External functions alone therefore don’t establish nounhood.

Complementation sharpens the comparison. Common nouns and determinatives take partitive complements: *a lot/some of the wine*. Comparative complements such as *more than ten* instead connect determinatives with adjectives (Huddleston and Pullum 2002, 349–50, 392–94, 411–12, 432–33). Common nouns permit PP and clausal complements more generally; pronouns and primary naming uses of proper nouns have much more restricted dependents (Huddleston and Pullum 2002, 429–30, 439–43, 517–21). Determinatives combine nominal complement and postmodifier constructions with their own selectional restrictions.

Quantificational common nouns make the connection more specific than shared quantity meanings. In *a lot of the delegates* and *many of the delegates*, both heads quantify over a partitive domain. Yet *lot* permits *a lot of delegates*, whereas \**many of delegates* is excluded. *CGEL* also categorizes *plenty* as a common noun whose quantificational use resists determination and modification (Huddleston and Pullum 2002, 349–50). Established common nouns thus approach the determinative profile as determinatives approach theirs.

Ordinary count nouns alone are consequently an inadequate comparison group. Quantificational common nouns already combine selected *of*-complements with restricted dependents. Determinatives extend this pattern within Noun, adding the broad specialization in plain-case Det and the premodifier contrast examined in §3.3.

The adjectival affinities likewise vary across the inventory. Grade connects *few*, *many*, *much*, and *little* with adjectives, and their comparative forms take *than*-complements. Predicative use extends to *several*, and AdvP premodification extends much further. Even the gradable forms have distinct syntax: *so many mistakes* contrasts with \**so numerous mistakes* (Huddleston and Pullum 2002, 392–96, 539–40).

The case for inclusion rests on this distribution of connections. Determinatives share argument and determiner functions with all three noun subcategories, referential contrasts with pronouns, and number, genitive marking, and partitive constructions with established parts of Noun. Adverbial premodification is a broad counterweight; grade and comparative complementation connect a smaller set with adjectives. I give greater weight to the recurring nominal profile, while preserving those countervailing properties in the determinative subcategory.

The D-noun analysis captures shared properties through inheritance: a property stated for a superordinate category is available to its subcategories, subject to stated restrictions. Determinatives therefore inherit nominal projection from Noun. Subcategory rules constrain combinatorics, and lexical entries distinguish such forms as independent *some* and dependent-only *every*.

## 3.2 Noun phrases in determiner and argument functions

Determinatives’ characteristic determiner use could support a separate primary category. But Det is itself specific to NP structure, where it marks definiteness and often contributes quantification (Huddleston and Pullum 2002, 354–59). These tasks connect it with the reference and number properties compared above. The question is whether this specialization warrants a primary boundary within nominal grammar.

Determiner function already cuts across the existing noun subcategories. Compare *my preferences*, *Kim’s preferences*, and *people’s preferences*. The determiner is an NP ultimately headed by a pronoun, a proper noun, and a common noun respectively (Huddleston and Pullum 2002, 354–55, 470–71). Figure 2 illustrates the proper-noun case.

> Note 5. *CGEL* assigns these genitives the combined function Subject–Det (Huddleston and Pullum 2002, 472–73). I treat them as Det here, without the additional subject function.

```text
NP
├── Det: NP[gen]
│   │
│   Head: Nom
│   │
│   Head: N_proper
│   │
│   Kim's
└── Head: Nom
    │
    Head: N_common
    │
    preferences
```

Figure 2: The genitive NP *Kim’s* functions as determiner within *Kim’s preferences*, ultimately headed by *preferences*. The representation abstracts from the internal realization of genitive marking.

The compound determinative *someone*, following the categorization of Payne et al. (2007, sec. 1.3), joins this pattern in *someone’s preferences*: its genitive NP fills the same determiner function. The nominal base in *someone* may contribute to that permission, and most determinatives resist case marking.

The NP headed by *some* likewise functions as Det in *take some apples* and as object in *take some* (Figure 1). Its subcategory and nominal projection remain constant across these uses.

NP becomes the shared phrase type for the principal realizations of determiner function. Plain determinative-headed NPs, such as *almost ten* in *almost ten apples*, join genitives such as *Kim’s* and *my*. Minor determiners include further NPs: *what size* in *what size shoes*, *that size* in *that size shoes*, and *Sunday* in *Sunday morning* (Huddleston and Pullum 2002, 356).

These existing NP determiners give the extension a functional basis. In *Kim’s preferences*, the embedded NP supplies an identifying anchor through its own referent; *Sunday* and *what size* specify a day or a dimension. Determinatives’ deictic and quantitative specifications fit this nominal pattern. I take that fit to support treating their specialization in Det as a distinction within Noun.

PPs remain a restricted alternative, as in *up to twenty minutes* and *between fifty and sixty tanks* (Huddleston and Pullum 2002, 356). Number, countability, and other selectional conditions distinguish the determining expressions.

## 3.3 Modifier selection and taxonomic level

Shared nominal projection doesn’t make modifier permissions uniform. In *almost every experienced teacher* (Figure 3), the AdvP *almost* modifies the determinative noun *every*; the AdjP *experienced* modifies the common noun *teacher*, which ultimately heads the outer NP.

```text
NP
├── Det: NP_D
│   │
│   Head: Nom
│   ├── Mod: AdvP
│   │   │
│   │   almost
│   └── Head: N_D
│       │
│       every
└── Head: Nom
    ├── Mod: AdjP
    │   │
    │   experienced
    └── Head: N_common
        │
        teacher
```

Figure 3: Two modifier relations in *almost every experienced teacher*: *almost* modifies *every*, and *experienced* modifies *teacher*. The outer NP has *teacher* as its ultimate head. Internal structure within the one-word modifier phrases is suppressed.

Payne et al. (2010, 40–42) defend keeping *few*, *any*, and related forms in one lexical category across dependent and independent uses. In *hardly any money* and independent *hardly any*, *hardly* remains an adverb and *any* retains its category. The D-noun analysis preserves that continuity. It also preserves their contrast between adverbial premodification, as in *almost anybody*, and adjectival postmodification, as in *nothing absolute*.

Adverbial premodification needs two levels distinguished. Within a common-noun Nom, premodifiers are normally adjectival or nominal. At the edge of a whole NP, adverbs are less restricted: compare *only you*, *for almost my entire life*, and *Usually a careful driver, Anne found her mind wandering*. Here *only*, *almost*, and *usually* modify NPs containing their own heads and, where present, determiners. *CGEL* calls these peripheral modifiers (Huddleston and Pullum 2002, 430–31).

Could *almost* in *almost every* likewise modify the whole determinative-headed NP? Once DP is replaced by NP, that becomes an available analysis. *CGEL* itself observes overlap between DP modifiers and peripheral NP modifiers, with some attachment decisions uncertain (Huddleston and Pullum 2002, 431). Figure 3 retains internal attachment, but the dependent use alone doesn’t establish it: either attachment can place *almost every* together in Det function.

Treating every pre-head adverb as peripheral would require more. In the constructed *the very few who objected*, *very* follows the external determiner and modifies *few* within Nom. A peripheral analysis would need an additional embedded NP or another structural change. The ordinary nominal structure therefore still needs internal AdvP modification for some determinatives, although *almost every* alone isn’t decisive evidence for it.

NP modifiers provide a further connection. Determinatives permit determinative premodifiers such as *this* in *this much* (Huddleston and Pullum 2002, 393). Under the proposed analysis, this is an NP modifier in another NP. Comparative determinatives also take established NP modifiers: *a lot* in *a lot fewer*, alongside *CGEL*’s *a lot more than fifty* (Huddleston and Pullum 2002, 432). These permissions remain specific to the head and construction.

Payne et al. (2010, 42–47) establish that adverbs can postmodify common nouns, as in the constructed *the changes globally to the climate*. They also analyse *almost* as modifying the attributive nominal *textbook* in *an almost textbook case* (Payne et al. 2010, 75, n. 3). Adverbial modification therefore isn’t categorically excluded from Noun, even internally. Its broader availability with determinatives remains a difference of distribution within the proposed category.

Postmodifier permissions also overlap. Common nouns freely take integrated relative clauses; personal pronouns permit a restricted range, including *we who have read the report* (Huddleston and Pullum 2002, 430). Determinative examples include *few who come ever leave*, *those who came*, *that which remains*, and *something that you need to know*. Section 4.4 examines this shared construction.

The resulting comparison is narrower than a contrast between nouns and adverb-modified determinatives. Peripheral modification already belongs to NP grammar; some internal adverbial modification occurs with common nouns too. Determinatives still permit internal modifier patterns that ordinary common-noun heads exclude. Section 7.3 counts the necessary subcategory restrictions in comparing the grammars.

## 3.4 Inflection

Inflection supplies several connections with established nouns, though no one contrast runs through the whole category. Common nouns typically distinguish singular and plural; proper nouns permit number inflection in restricted uses such as *the Smiths*. Demonstratives likewise distinguish *this*/*these* and *that*/*those* (Huddleston and Pullum 2002, 373, 521). These are contrasts between forms of a lexeme, unlike the fixed number restrictions of *each* and *several*.

Number needn’t be inflectional wherever it matters. *CGEL* treats singular and plural *you* as distinct lexemes, differentiated overtly only by the reflexive forms *yourself* and *yourselves* (Huddleston and Pullum 2002, 486). Number-neutral *some* has no corresponding singular–plural alternation. The demonstratives supply positive morphological evidence; the absence of that alternation elsewhere doesn’t distinguish determinatives from pronouns as whole categories.

Case gives a further partial connection. Genitives occur across the proposed subcategories: *dog’s*, *Kim’s*, *my*, and *someone’s*. Personal pronouns have fuller case paradigms. Most determinatives lack case inflection, and compounds such as *someone* and *something* may owe their genitives to the nominal component (Huddleston and Pullum 2002, 423–24, 479–80). This supports the compounds’ nominal affinity more directly than the category’s membership as a whole.

Grade instead connects determinatives with adjectives. The paradigms *few*/*fewer*/*fewest*, *many*/*more*/*most*, and their counterparts with *little* and *much* distinguish plain, comparative, and superlative forms (Huddleston and Pullum 2002, 391–95). Only a restricted quantificational group has this property. Demonstratives and articles lack grade, just as most determinatives lack case.

The *no*/*none* alternation distinguishes dependent and independent forms. Genitive *my*/*mine* supplies a parallel (§6.3). Inflection thus supports both nominal and adjectival connections. The clearest nominal comparison is demonstrative number; grade is the clearest counterweight. Neither can serve as a necessary condition for the whole superordinate category.

## 3.5 Word formation and category boundaries

Derivation connects categories through word formation, but the output category need not identify the input. Noun-forming suffixes differ in the bases they select: *-ship* in *friendship* primarily selects nouns denoting persons, though *hardship* has an adjective base; the inhabitant suffix *-er* in *Londoner* attaches to a place name (Huddleston and Pullum 2002, Ch. 19, §§5.6.2(b), 5.7.2(k)). No noun-selecting suffix shared by pronouns and determinatives is established here.

Determinatives enter derivations whose output is a common noun. *CGEL* cites *nothingness* and *oneness* among formations with *-ness* on non-adjectival bases (Huddleston and Pullum 2002, Ch. 19, §5.7.2(i)). Further established nouns include *thisness*, *fewness*, and *muchness*.

> Note 6. See *Merriam-Webster.com Dictionary*, s.vv. [*thisness*](https://www.merriam-webster.com/dictionary/thisness) and [*fewness*](https://www.merriam-webster.com/dictionary/fewness), and *Dictionary.com*, s.v. [*muchness*](https://www.dictionary.com/browse/muchness) (accessed 10 September 2026). These attestations don’t establish a uniformly productive modern rule.

*-ness* is the default suffix for forming nouns from adjectives, but also attaches to other bases, as in *whyness* (Huddleston and Pullum 2002, Ch. 19, §5.7.2(i)). It therefore doesn’t settle the input category of *nothingness*. A conversion analysis would require independent evidence for an intermediate base.

The adverb *mostly* provides a different output. Adverbial *-ly* primarily attaches to adjectives, but *CGEL* also gives noun-based *partly* and *purposely* (Huddleston and Pullum 2002, 566). This gives *most* an adjectival affinity without an adjective-only diagnostic.

> Note 7. See *Dictionary.com*, s.v. [*mostly*](https://www.dictionary.com/browse/mostly) (accessed 10 September 2026).

Pronouns enter gender-marking compounds such as *he-goat* and *she-ass* (Huddleston and Pullum 2002, Ch. 19, §5.3); determinatives combine with nominal material in *someone* and *anything*. Their determinative premodifier permissions recur in the compounds (§4.5), while the nominal component contributes further properties.

Numeral morphology requires the input categories to be kept distinct. Reynolds (2026, sec. 5.4) derives fractional nouns from cardinal nouns: *seventh*, for example, is a count noun in *three sevenths*. This isn’t independent evidence that determinative *seven* is a noun. The analysis already distinguishes a nominal cardinal base from the determinative one. Ordinal *seventh*, as in *the seventh attempt*, is adjectival.

Larger numerals also require syntax. In *two thousand and twenty-seventh*, only the final coordinate is an AdjP; the preceding cardinal phrase retains its own category (Reynolds 2026, sec. 5.5). Suffixation on the rightmost base doesn’t turn the entire coordination into an adjective lexeme. The D-noun proposal preserves these distinctions between lexemes, phrases, and coordinates.

Word formation therefore provides connections without a uniform category diagnostic. Several determinatives supply bases for common nouns, but the relevant suffixes also select other categories. The stronger morphological comparisons remain the inflectional contrasts in the preceding subsection.

# 4 Evidence for nominal structure

Independent uses, partitives, and modification show a recurring nominal pattern. The observations overlap: *Some left* illustrates both external distribution and syntactic completeness. Fusion and ordinary headedness offer different internal analyses of these constructions.

## 4.1 Breadth of independent use

Independent use is widespread within the determinative inventory. *CGEL* discusses such uses for demonstratives and quantifiers including *some*, *all*, *both*, *many*, *few*, *several*, *each*, *either*, *neither*, *much*, and *enough*, while recording lexical restrictions and the separate forms *no*/*none* (Huddleston and Pullum 2002, 371–72, 410–24). The generalization concerns the availability of independent constructions across a lexical category, not unrestricted acceptability in every sentence frame.

> Note 8. Material before a determiner falls outside the independent-use comparison. *CGEL* treats *all*/*both* in *all/both the books* as predeterminer modifiers, *quite*/*rather* before *a good idea* as peripheral modifiers, and *such*/exclamative *what* before *a disaster* as adjectives (Huddleston and Pullum 2002, 433–37). The fixed *many a* is a complex determinative restricted to Det function (Huddleston and Pullum 2002, 394). The *half* in *half a cake* is a common noun used as a predeterminer modifier (Huddleston and Pullum 2002, 434). These constructions don’t add evidence for independent determinative heads.

In the constructed examples in (1), compare the bracketed NPs as subjects, objects, and complements of prepositions. Assume that a woman named Kim and a group of people are already under discussion. The competing analyses assign different internal structures to independent *some*.

(1a) *\[People\] left.* — *I see \[people\].* — *with \[people\]*

(1b) *\[Kim\] left.* — *I see \[Kim\].* — *with \[Kim\]*

(1c) *\[She\] left.* — *I see \[her\].* — *with \[her\]*

(1d) *\[Some\] left.* — *I see \[some\].* — *with \[some\]*

Independent uses containing fused-head AdjPs prevent a simple inference from these positions to nounhood. *The rich* and *the poor* can fill nominal argument positions. Comparative and superlative adjectives also head expressions without a generic human interpretation: *CGEL*’s *the most important of her criticisms* is an NP containing a partitive *of*-phrase (Huddleston and Pullum 2002, 332–33, 416–23).

Independent *some* can form a one-word NP, whereas an NP with *rich* as fused head requires the definite article *the* on the generic human reading (Huddleston and Pullum 2002, 417–18). That is a local contrast: argument NPs headed by singular count common nouns also need determination. Section 4.4 returns to the fuller adjectival comparison.

## 4.2 Structural saturation and interpretation

With a group of people under discussion, *Some left*, *Many came*, and *All agree* illustrate structural saturation: an argument expression can be syntactically complete without another overt head or determiner. Syntactic completeness differs from contextual interpretation. In *I’ll take some*, the relevant substance or set may be supplied by discourse or the situation. That dependence doesn’t establish a deleted common noun: ordinary pronouns also depend on context.

In the following attestation from the CGELBank treebank, *two different Honda models* supplies the domain for the independent object *both*:

> Note 9. CGELBank (Reynolds et al. 2023), sentence [`reviews-083459-0002`](https://github.com/nert-nlp/cgel/blob/d0a2c2d8c522b23d5aa879fc9cb94948f4285b2c/datasets/ewt.cgel#L651-L654).

\(2\) *Went there yesterday: we are trying to decide between two different Honda models, so we wanted to test-drive both back to back.*

Generalizing expressions such as *Many are called, few are chosen* and *Enough is enough* need no previously uttered common-noun phrase. They rule out a mandatory overt-antecedent requirement, but a silent-noun account could supply a generic restriction. Generic pronoun *one*, as in *One shouldn’t judge*, provides a parallel without a required overt antecedent. Such examples don’t decide whether the restriction belongs in semantics or syntax.

The comparison with ordinary pronouns and proper nouns is structural as well as interpretive. In *She left* and *Kim left*, *CGEL* permits an NP headed by a nominal with no determiner. Applying that structure to *Some left* preserves the same division between a complete NP and its context-dependent reference. The dependent use of *some* doesn’t by itself require a Det function inside every independent occurrence.

In Payne et al. (2007), one constituent jointly realizes Head and a dependent function, subject to structural and adjacency conditions. Under *CGEL*’s analysis of independent *some*, its DP fills Det of NP and Head of Nom. The word remains determinative, while the independent expression is an NP. Ordinary headedness instead gives *some* nominal projection, with the same restrictions on independence and form selection.

*CGEL* also uses fusion with nouns. Anaphoric *mine*, understood as “my car”, combines the possessive relation with an understood nominal description and receives a fused analysis. Predicative *mine*, as in *it’s mine*, can instead mean “belongs to me”: it expresses the relation directly, without an understood nominal head (Huddleston and Pullum 2002, 410–11, 470–71). A suitable context may permit either reading.

This distinction shows why nounhood and fusion are compatible. Ordinary headedness follows here from the proposed projection rules; it doesn’t require eliminating every fused construction containing a noun. The analysis of independent genitives, including *Kim’s* and *mine*, falls outside the fragment in §7.2.

## 4.3 Partitives locate the quantificational head

In *some of the wine*, *some* specifies a quantity drawn from an identifiable amount of wine. The NP *the wine* denotes the partitive domain: the whole from which that quantity is drawn. This NP is complement of *of*. A pronoun-headed NP or independent genitive NP can express the domain too: *many of them*, referring to previously mentioned people, or *some of Kim’s*, referring to Kim’s apples.

Compare where the common noun occurs in *some apples* and *some of the wine*. In the partitive, *wine* is embedded inside the *of*-phrase, so it can’t be the lexical head of the whole NP. The comparison instead concerns the head-like role of *some* in that larger expression.

Figure 4 gives the D-noun analysis, with the *of*-phrase functioning as complement within Nom, as in *CGEL*’s partitive tree (Huddleston and Pullum 2002, 411–12). *CGEL* represents the head-like role of *some* through Det–Head fusion. Partitives support that role while leaving the choice between fusion and ordinary headedness open.

```text
NP
│
Head: Nom
├── Head: N_D
│   │
│   some
└── Comp: PP
    ├── Head: P
    │   │
    │   of
    └── Comp: NP
        │
        the wine
```

Figure 4: *Some of the wine* under the D-noun analysis. The Head relations lead from the outer NP to *some*. The common noun *wine* is inside the complement PP and doesn’t head the whole expression. The inner NP is abbreviated.

The overt quantifier and domain already supply a compositional interpretation of *some of the wine*. A silent common noun would need to explain something further, such as a restriction on interpretation or modification that the overt-head account misses. The construction itself supplies no such requirement. I therefore prefer an overt-head analysis over an otherwise equivalent null-head analysis; fusion remains compatible with that preference.

## 4.4 Modification tests the internal analysis

The pair *the lucky survivors*/*the lucky few* supplies a comparison involving both an external determiner and an attributive-modifier AdjP. *CGEL* explicitly permits determinatives used as internal modifiers to fuse with Head, as in *the other two* and *these few here* (Huddleston and Pullum 2002, 415–16). Its analysis of *the few mistakes* assigns *the* to Det and *few* to Mod (Huddleston and Pullum 2002, 392). That dependent use supplies the counterpart for a Mod–Head analysis of independent *few* after an external determiner.

Figure 5 compares the resulting analyses of *the lucky few*. Both have an overt Det and a Nom modified by *lucky*. In the D-noun analysis, *few* fills Head. In the fusion analysis, its DP fills Mod–Head. The competing structure thus uses machinery already needed for adjectival fusion; it requires neither a silent noun nor conversion.

```text
NP
├── Det: NP_D
│   │
│   the
└── Head: Nom
    ├── Mod: AdjP
    │   │
    │   lucky
    └── Head: N_D
        │
        few
```

```text
NP
├── Det: DP
│   │
│   the
└── Head: Nom ───────────┐
    ├── Mod: AdjP        │
    │   │                │
    │   lucky            │
    └── Head: Nom        │
        │                │
        Mod–Head: DP ◄───┘
        │
        Head: D
        │
        few
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

Fusion groups *the lucky few* with *the idle rich*; ordinary headedness groups it with *the lucky survivors* and unifies bare and externally determined *few*. Both cover the example. The choice is between sharing fusion across D and adjective, and sharing ordinary Head structure across determinative constructions.

Reducing fusion’s applications can simplify this description even when fusion remains available for adjectives. The advantage is the uniform treatment of *few*; its value depends on any additional conditions or lost generalizations elsewhere. Section 7.2 compares those costs while holding the lexical restrictions fixed.

> Note 10. Compare the theory of second best in Lipsey and Lancaster (1956, 11–12): under a constraint preventing an optimum, satisfying more optimality conditions needn’t improve the outcome. The analogy concerns interactions among grammatical choices, not a formal optimum for the grammar.

The constructed *the remaining three* extends the modifier pattern to cardinals. It doesn’t independently decide whether *three* is determinative or has a common-noun use: Reynolds (2026) argues for both uses of cardinals. Section 7.3 treats their unification as a consequence conditional on that analysis.

Relative-clause postmodification adds another nominal construction: *those who came*, *anyone who asks*, *everything that matters*, and, with books under discussion, *some that I saw* and *two that I have seen*. *CGEL* describes relatives with demonstratives and compounds (Huddleston and Pullum 2002, 414, 422–23). These clauses modify the nominal expression containing the determinative, as they do in *people who came*.

Number supplies a further distinction between determinatives and adjectives. Independent *this*/*these* and *that*/*those* retain overt singular–plural contrasts. The generic human *the rich*, by contrast, is a plural NP whose adjective lacks nominal number inflection and still takes adverb modifiers: *the very rich* (Huddleston and Pullum 2002, 418). The strongest morphological evidence comes from the demonstrative paradigms. The singular and plural specifications of *each* and *several* concern lexical restrictions; NP number alone doesn’t distinguish the categories. Other determinatives, such as plural or non-count *some*, remain number-neutral.

Bare colour expressions and evaluative comparative subjects complicate a simple distributional boundary. *CGEL*’s *Henrietta likes red shirts, and I like blue* permits reduction licensed by coordination. The constructed *Blue is good* raises a separate ambiguity between noun and adjective, while the attested *Bluer is better* establishes a bare comparative subject without settling its phrase category. These cases leave the wider comparison of argument distribution and head properties necessary.

> Note 11. The *blue*, *old*, and *small* examples on *CGEL* p. 417 all occur in coordinated contrasts. *Bluer is better* accompanies a results colour scale in Stanford CS329X, [“Codeswitching LLMs”](https://web.stanford.edu/class/cs329x/slides/Lecture12_B_Codeswitching%20LLMs.pdf), slide 8 (accessed 10 September 2026). I interpret it as evaluating a degree of blueness. Subject function alone doesn’t establish NP status (Huddleston and Pullum 2002, 236).

The combination of argument use, nominal number properties, partitives, and modification favours ordinary determinative headedness alongside adjectival fusion.

## 4.5 Compounds and modifier domains

A more demanding modifier comparison is *hardly anyone present*. Payne et al. (2007, 581–83) assign *hardly* to DP structure and *present* to nominal structure. The compound *anyone* takes the premodifiers of its determinative base *any*: compare *hardly any writer present*. The adjective realizes a specialized restrictor function, restricted to post-head position and non-recursive. Figure 6 contrasts this account with an ordinary-Head analysis.

```text
NP
│
Head: Nom
├── Mod: AdvP
│   │
│   hardly
├── Head: N_D
│   │
│   anyone
└── Mod: AdjP
    │
    present
```

```text
NP ──────────────────┐
│                    │
Head: Nom            │
├── Det–Head: DP ◄───┘
│   ├── Mod: AdvP
│   │   │
│   │   hardly
│   └── Head: D
│       │
│       anyone
└── Mod: AdjP
    │
    present
```

Figure 6: *Hardly anyone present* with ordinary Head (first tree) and fusion (second tree). Both post-head Mod positions realize the specialized restrictor. In the fusion tree, DP fills Det of NP and Head of Nom, following Payne et al. (2007, 582, (13d)). Modifier-phrase interiors are suppressed.

In the D-noun analysis, *anyone* inherits nominal projection from Noun and its premodifier permissions from its determinative base. The compound construction supplies the post-head restrictor permission, with the same position and non-recursion conditions as the fusion account. It doesn’t license a corresponding pre-head adjective. The compound’s ordinary argument use and exclusion of external determination are further lexical conditions; the premodifier and restrictor slots aren’t unrestricted Nom dependents.

The relative clauses illustrated above are ordinary postmodifiers, distinct from the specialized restrictor. When both occur, the relative follows it: *something useful that I found*. *CGEL* explicitly gives compounds the common noun’s range of ordinary postmodifiers while preserving this ordering condition (Huddleston and Pullum 2002, 423).

This division extends to *someone* and *everybody*: the compound family licenses nominal argument use and post-head restrictors, while each base supplies its own premodifier permissions. CGELBank attests the post-head pattern in *I need something reliable and good looking*.

> Note 12. Sentence [`answers-20111024111513AAAQhAO_ans-0003`](https://github.com/nert-nlp/cgel/blob/d0a2c2d8c522b23d5aa879fc9cb94948f4285b2c/datasets/ewt-test_iaa50.cgel#L179-L181) in `ewt-test_iaa50.cgel`.

Fusion reuses the DP–Nom boundary to separate the two modifier domains. Ordinary headedness locates both within Nom, assigning their restrictions to the determinative base and compound construction. Both accounts need the specialized restrictor condition.

## 4.6 Predicative uses and their restrictions

*CGEL* records predicative *Its advantages are several* and *Their enemies were many*, describing the latter pattern as uncommon and formal (Huddleston and Pullum 2002, 392, 395–96). This use is available to only part of the determinative inventory; *every* and the articles remain excluded.

*She is a beauty* ascribes a property, whereas *That is Kim* identifies a person. *CGEL* excludes specifying *be* clauses from its noun–adjective diagnostic because phrases from other categories occur in them too (Huddleston and Pullum 2002, 536).

Nominal grammar also distinguishes predicative and argument uses. A bare-role NP such as *president* is licensed in *I’d like to be president*, but requires determination in the corresponding object use *I’d like to meet the president* (Huddleston and Pullum 2002, 328). Determinatives’ asymmetries fit this broader variation within Noun.

## 4.7 What the combined pattern supports

The nominal constructions reinforce the semantic and morphological connections in §3. Under the D-noun analysis, bare, partitive, and externally determined uses inherit ordinary Head structure. *CGEL* distinguishes Det–Head from Mod–Head and uses the DP–Nom boundary to separate modifier domains. These are competing ways of organizing the same constructional evidence; their grammatical costs are compared in §7.2.

# 5 Coordinate subcategories and inheritance

Including determinatives within Noun leaves a second question: where within Noun do they belong? In the proposed hierarchy, common noun, proper noun, pronoun, and determinative are four coordinate subcategories. Hudson instead puts determinative inside pronoun, which is itself inside Noun. Both group determinatives with nouns. They differ in whether pronouns and determinatives form an intermediate category that excludes common and proper nouns.

The intermediate category would be useful if it supported grammatical generalizations applying to pronouns and determinatives together. The coordinate analysis can still record properties shared by those two groups; it doesn’t claim that every noun subcategory is equally similar to every other. The issue is whether their shared properties warrant another level in the lexical hierarchy.

Reynolds (2021) investigates their similarity by applying an unsupervised clustering model to a matrix of word forms and properties. Each entry records whether a form has a property, such as permitting *almost* as a modifier or having a genitive form. The study reports 232 properties for 138 word forms. Clustering groups forms by their recorded similarities without being told which forms are pronouns and which are determinatives.

The resulting groups broadly resemble the supplied pronoun and determinative inventories, although the outcome varies with the starting configuration and the properties included. This supports a distinction between the groups. It doesn’t decide where to place that distinction in a larger hierarchy.

> Note 13. The public file contains 155 properties for the same 138 forms, despite the reported 232. The accompanying [*Replication audit of the English determinative–pronoun feature matrix*](run:matrix-audit.pdf) documents this discrepancy, reproduces the published statistical decomposition, and examines sensitivity to starting configuration and feature selection. The public file is preserved unchanged.

Two subcategories can be clearly distinguishable while sharing a parent. The study therefore leaves both a broader pronoun category and the present broader Noun category open. It also contains no common or proper nouns, so it can’t test whether determinatives are closer to pronouns than to those alternatives. Its inventories follow *CGEL*; the small boundary revisions in §6.2 would require a correspondingly revised comparison.

The grammatical case for nesting needs to be assessed on its own. Many pronouns and determinatives have little descriptive content and depend on context for interpretation. Pro-form gender supplies further connections (§3.1). These properties make the grouping plausible, but they don’t uniquely identify it: primary naming uses of proper nouns also depend on context, and pro-form gender extends to non-nominal expressions (Reynolds 2025).

Restrictions on determination and modification are another candidate. Personal pronouns generally resist external determiners and permit few internal modifiers: *poor old me* illustrates the restricted adjectival pattern (Huddleston and Pullum 2002, 429–30). But proper names also resist free determination and modification in their primary uses (Huddleston and Pullum 2002, 517, 519–20). These restrictions don’t pick out pronouns and determinatives alone.

Nor are those restrictions uniform within the proposed intermediate category. Determinatives allow *the few*, *the two*, and *these three*, with item-specific conditions; *CGEL* gives *these few here* and *the many who did* (Huddleston and Pullum 2002, 415–16). Their adverbial modifier patterns differ from the restricted adjectival pattern of personal pronouns. A broader pronoun category couldn’t simply pass the personal pronouns’ rules down to determinatives.

I therefore place determinative alongside pronoun. Their shared nominal structure belongs at the Noun level, while their more specific patterns remain distinct: person, case, and reflexivity organize much of the pronoun system; quantification, determination, and degree organize much of the determinative system. Nesting remains a coherent alternative, but the comparisons here don’t establish a further shared set of grammatical rules that requires it.

# 6 Restricted members and disputed boundaries

The broader grouping must accommodate members that lack its most conspicuous properties. Articles test whether ordinary independent use is necessary; *which* and *what* test the pronoun boundary; *no*/*none* and *enough* test form selection and functions outside NP structure.

## 6.1 Articles and the limits of independent use

Why categorize the articles *the* and *a* as nouns if they can’t stand independently? *Every* is restricted too, while *no* has the distinct independent form *none* (Huddleston and Pullum 2002, 371–72, 410–11).

*CGEL*’s treatment of *my* supplies a precedent for restricted membership within Noun (Huddleston and Pullum 2002, 470–71). Dependent *my* and independent *mine* belong to one pronoun paradigm. *My* remains a noun even though, in the ordinary NP construction, it requires a following nominal. For articles, the corresponding positive evidence is integration into determinative; their nounhood depends on the category-level argument.

The articles participate in the determinative system of definiteness, quantity, and count restrictions. In *the/a/this/every book*, they occupy the same Det position and contribute to the interpretation of the NP. *The* permits singular, plural, and non-count targets; *a* selects a singular count target and contributes individuation. Their connections extend beyond shared position, although neither has the full determinative profile (Huddleston and Pullum 2002, 368–73).

*The* also participates in degree modification. In *the bigger the better*, it modifies comparative AdjPs, as other determinatives do in *much bigger* or *no better* (Huddleston and Pullum 2002, 1131–32, 1135–36). This supplies a connection outside ordinary Det function while preserving its exclusion from independent argument use.

*A* also enters the complex determinatives *a few*, *a little*, and *many a*. In the last, *many* contributes a large number and *a* an individuating, distributive effect. *CGEL* treats *many a* as syntactically fixed: it doesn’t establish that ordinary *a* freely accepts modifiers (Huddleston and Pullum 2002, 392–94). It does connect the article with quantificational constructions beyond *a book*.

*Every* connects with independent *each* through universal quantification and singular count selection. It also permits *almost*/*nearly* and occurs after genitives in *her every move*. Spinillo (2004, 156–58) recognizes these differences from *the* and *a*, as well as the articles’ greater phonological dependence. Her restricted grouping is thus a substantive alternative, not merely an omission of inconvenient properties.

The issue is how much independent support its shared restrictions provide. Absence of bare, predicative, and partitive uses all limits occurrence without a following nominal; they aren’t three independent reasons for a primary category. Little descriptive content extends well beyond the trio. Meanwhile, *a*’s quantificational constructions and *every*’s modifier permissions cross the proposed article boundary. I retain the restricted members within determinative because these connections preserve a broader system without granting unrestricted use to any member.

The argument for retaining the articles is synchronic. Grammaticalization supplies background: Lyons (1999, 331–36) discusses the development of definite articles from demonstratives and of articles expressing cardinality from numerals. These histories can explain changes in content and use, but don’t establish the synchronic categorization.

The D-noun analysis retains the shared determining profile and records the absence of independent use in lexical permissions. The articles’ nounhood depends on their membership in that broader system. They don’t individually exhibit the full evidence that supports the parent category.

## 6.2 The pronoun boundary: *who*, *which*, and *what*

The pronoun boundary matters for the inventory, but either categorization keeps the disputed forms within Noun. I retain *who* as a pronoun: its *who*/*whom*/*whose* paradigm gives positive case evidence, though no single property is definitive (Huddleston and Pullum 2002, 904–5). I treat interrogative and relative *what* as determinative across dependent and independent uses.

*CGEL* splits *what* by gender: dependent *what* allows personal and non-personal heads, while independent *what* is non-personal (Huddleston and Pullum 2002, 398). Compare *What person/object do you have in mind?* with *What’s behind the door?* I state this as a constructional restriction: an overt nominal supplies its own descriptive restriction; without one, the independent construction requires a non-personal interpretation. Independent use alone doesn’t require a pronoun analysis.

Interrogative *which* already remains determinative across both uses in *CGEL*. I extend that continuity to relative *which*, preserving its non-personal restriction when independent (Huddleston and Pullum 2002, 397–99). This leaves partitive and relative-clause permissions to be stated separately. The proposal concerns these lexical boundaries; its superordinate-Noun argument doesn’t depend on their precise placement.

> Note 14. Exclamative *what*, as in *What a nice day!*, retains the distinct adjective analysis in *CGEL* (Huddleston and Pullum 2002, 436–37).

## 6.3 Form selection and degree modification

*No*/*none* illustrates a restriction on forms within a paradigm. *CGEL* treats them as inflectional forms of one determinative: dependent *no students* contrasts with independent *none*, while both permit *almost* (Huddleston and Pullum 2002, 389–90). The D-noun analysis preserves this relation. Ordinary Head structure licenses *none of the students*; it doesn’t license \**no of the students*. Form selection remains necessary, just as with *my*/*mine*.

*Enough* tests both position and external function. It precedes a nominal in *enough money* and can follow one in *money enough*; post-head *enough* can’t itself be premodified, as shown by \**money almost enough* (Huddleston and Pullum 2002, 396–97, 445). Only the permitted construction licenses each position.

*Enough* also modifies adjectives, adverbs, verbs, and some PPs: *good enough*, *quickly enough*, *I hadn’t prepared enough*, and *enough in control* (Huddleston and Pullum 2002, 396–97). The degree determinatives *much* and *little*, and *no*/*none*, likewise have uses outside NP structure (Huddleston and Pullum 2002, 390, 395–97). These permissions must survive recategorization. Noun membership doesn’t confine every projection to argument or determiner function.

> Note 15. *Both*, *either*, and *neither* also serve as markers of coordination (Huddleston and Pullum 2002, 1305, 1308). Their noun categorization would preserve that further category–function combination; the present fragment doesn’t analyse coordination.

NPs already modify adjectives in *three years old*, *a great deal smaller*, and *plenty big enough* (Huddleston and Pullum 2002, 549–50). These include the quantificational common nouns compared in §3.1. Degree modification therefore supplies another connection with existing nouns, but also another restriction: *CGEL* contrasts predicative *a great deal better* with its exclusion before a noun in \**some a great deal better proposals*, where *much better* is permitted (Huddleston and Pullum 2002, 551–52).

The D-noun analysis must preserve that difference between two kinds of NP modifier. It expands NP’s range of degree-modifier uses while restricting their positions by head and construction. The resulting cost is that the existing ban on pre-head NP modifiers within attributive AdjPs becomes a narrower condition. Nominal projection alone doesn’t license *enough*’s full distribution.

# 7 Structural consequences and grammatical economy

## 7.1 A shared phrase type in determiner function

In *some apples* and *Kim’s apples*, the determining phrases share the NP category under both ordinary-Head accounts: D-noun and separate D. *CGEL* instead distinguishes DP from genitive NP. It also admits a restricted range of plain-case NPs and PPs as determiners, as in *what size hat* and *over thirty ties* (Huddleston and Pullum 2002, Ch. 5, §4). The phrase types are:

```text
CGEL:  Det:{DP,NP,PP}
Both ordinary-Head accounts:  Det:{NP,PP}
```

Determinative phrases and genitive NPs supply the principal realizations in the separate-D analysis; PPs are restricted. Under ordinary headedness, NP covers both principal types. This consolidation leaves the selectional conditions in place: determinative-headed, genitive, and other licensed NPs still require separate identification. *CGEL* already states definiteness and the single-Det restriction functionally, so recategorization doesn’t derive them. The following fragment compares projection once those restrictions are held fixed.

## 7.2 A matched descriptive fragment

A grammatical fragment is a set of rules for a specified range of constructions. Here it covers determination, ordinary subject and object uses, partitives, and the modifier and compound comparisons in §4. It compares the D-noun analysis with two separate-D alternatives: ordinary headedness and fusion. All receive the same lexical restrictions and constructed judgments. Predication, the disputed wh forms, and modification outside NP structure fall outside this small fragment; their implications enter the broader comparison in §7.3.

Table 4 records use permissions. Dependent means that the form heads a phrase in Det function before another nominal. Independent means that its phrase occurs without another nominal in the displayed subject or object uses, as in *Some left* and *I saw some*. These labels describe the constructions covered here, rather than every possible function. Quotation, metalinguistic naming, and subordinate-clause uses of dependent genitives fall outside the fragment. Noun membership doesn’t itself grant a use permission.

Table 4: Shared permissions in the fragment. For *some*, the target column concerns its unstressed use before a noun. The inventory is deliberately limited to the displayed constructions.

| Form         | Dependent | Independent | Target in the Det construction         |
|:-------------|:---------:|:-----------:|:---------------------------------------|
| *the*        |    yes    |     no      | Singular or plural; count or non-count |
| *a*, *every* |    yes    |     no      | Singular count nominal                 |
| *some*       |    yes    |     yes     | Plural count or non-count nominal      |
| *few*        |    yes    |     yes     | Plural count nominal                   |
| *my*         |    yes    |     no      | No count or number restriction         |
| *she*        |    no     |     yes     | Not applicable                         |

Further constructional restrictions apply: *she* is a subject form, whereas the corresponding ordinary object form is *her*. The target restrictions concern the common-noun nominal being determined: *a* requires a singular count target such as *book* in *a book*.

Table 5 locates the three accounts. Comparing the ordinary-Head accounts holds projection fixed while varying taxonomy. Comparing the separate-D accounts holds taxonomy fixed while varying headedness.

Table 5: Three accounts retaining the permissions in Table 4, the modifier restrictions, and the compound conditions.

| Account | Primary taxonomy | Simple independent determinative |
|:---|:---|:---|
| D-noun analysis | D inside Noun | N–Nom–NP projection with Head function |
| Separate D, ordinary Head | D outside Noun | D remains separate but heads Nom and NP |
| *CGEL*: separate D, fusion | D outside Noun | NP distribution through Det–Head fusion |

The D-noun analysis applies nominal projection to determinatives through their membership in Noun. A separate condition checks use permissions. In the schemata below, `h` identifies the lexical head throughout its projection; parentheses mark optional dependents. The subscripts on Mod distinguish pre-head and post-head positions of the same modifier function. The head’s entry and construction restrict every dependent. `Mod_periph` adds the peripheral premodifier discussed in §3.3; the compact rule leaves any further NP layering implicit.

```text
Nom_h → (Mod_pre)  Head:N_h  (Comp)  (Mod_post)
NP_h → (Mod_periph) (Det)  Head:Nom_h
licensed(NP_h,f,c)  ⇔  f ∈ U_h ∧ C_h(f,c)
```

Here `U_h` is the head’s set of use permissions, `f` is the NP’s function, and `C_h` checks the lexical and constructional conditions in context `c`. For Det use, these include compatibility with the target nominal; for an argument headed by a singular count common noun, they include required determination. Optionality in the second rule doesn’t override those conditions.

These checks accommodate the reciprocal selection discussed by Hudson (§2.2). The determining phrase checks the target nominal’s count and number properties; the outer noun’s projection checks whether determination is required and supplied. Both conditions have to hold even though the tree assigns only one Head to each phrase.

In *some apples*, *some* heads an NP whose Det permission and plural-count target requirement are satisfied. *Apples* heads the outer Nom, which heads the NP. In *Some left*, *some* heads an NP whose argument permission is satisfied. *Every apple* passes the Det and singular-count checks; ordinary independent \**Every arrived* fails the argument-permission check. *The apple* and \**The arrived* differ in the same way.

Each NP’s use permissions follow its own head. In *the apple*, the article’s Det permission licenses the dependent NP headed by *the*. The outer NP takes its argument permission from *apple*, whose requirement for determination is satisfied by the article.

The same distinction between phrase levels matters beyond the fragment. In *I know which apple it is*, *which* heads the determining phrase inside *which apple*. The whole *which apple* is the preposed predicative complement of *is* in the embedded interrogative clause. Its function doesn’t make *which* independent; *apple* still heads that NP.

A singular count common noun such as *book* faces a different restriction from an article. In *a book*, its requirement for determination is satisfied; bare \**Book arrived* leaves that requirement unsatisfied. *Books arrived* has no such requirement. Requiring determination for a common noun doesn’t itself block an article-headed NP from argument use. An article’s exclusion from argument use must still be stated separately.

*Some* and *few* permit a partitive *of*-phrase within their nominal projection. *Almost* can modify *every* in *almost every teacher*; that permission doesn’t license *experienced* as a modifier of *every*. The construction *the lucky few* permits the external determiner and adjectival modifier shown in Figure 5.

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

The ordinary NP rule embeds this Nom. Det–Head jointly realizes Det of NP and Head of Nom, excluding a second Det; Mod–Head fills an internal modifier’s function and Head of Nom, allowing external determination. Lexical and constructional conditions select the fused function and permitted dependents. These schemata cover independent *few*, *few of them*, *the lucky few*, and *hardly anyone present*.

The ordinary-Head accounts share nominal projection and Head relations. Once a member’s use is licensed, its nominal structure follows from the shared rules; lexical and constructional conditions still determine the available functions and dependents. Dependent determinatives acquire a Nom layer in both. One account supplies these common structural expectations through inheritance from Noun, the other through a rule admitting both N and D.

The disjunction `{N, D}` groups the same heads for nominal projection. The D-noun analysis expresses this grouping in its lexical hierarchy, giving a point of harmony between taxonomy and phrase structure. Shared projection supports considering the grouping; its taxonomic rank depends on the broader profile comparison.

A grammar with Hudson’s nested categorization can use the same permissions and projection rules. Holding those rules fixed, placing the broader pronoun category on determinative’s inheritance path from Noun leaves the fragment’s judgments unchanged.

## 7.3 Existing restrictions, additional costs, and consequences

I compare the shared structural core, the number of primary categories, the treatment of internal differences, the placement of related forms and uses, and the restrictions each account needs. I hold the inventory, constructions, and readings fixed. Shared rules receive equal credit whether they use inheritance or cross-category licensing.

Common nouns, proper nouns, and pronouns already differ in determination and permitted modifiers (Table 2). Preserving those conditions adds no cost to the D-noun analysis. Separate D likewise restricts adverbial modification and independent use within its own category; moving those restrictions inside Noun doesn’t create them.

Internal premodification still adds a cost (§3.3). Peripheral NP modification can accommodate some determinative premodifiers, so it would overstate the difference to count every pre-head AdvP against the proposal. Internal cases such as *the very few* still need a permission that ordinary common nouns lack. The attributive *almost textbook* exception further qualifies the generalization. The degree-modifier contrast in §6.3 adds a parallel cost: determinative-headed NPs are admitted in positions that exclude other NP modifiers. Compound constructions also retain the distinction between inherited premodifier permissions and post-head restrictors (§4.5).

On shared structure, the ordinary-Head accounts tie. D-noun reduces the number of primary categories by one, retaining determinative as a subcategory and preserving its internal distinctions.

Reynolds (2026) distinguishes determinative numerals such as *ten* in *ten men*, proper-noun cases such as *10* in *Room 10*, and common-noun numerals such as *tens* in *tens of pens*. Under the D-noun analysis, all fall within primary Noun, retaining their subcategory and constructional differences. Ordinals remain adjectives, and complex numeral phrases remain distinct from single lexemes.

Payne et al. (2013, 797–98) distinguish three lexemes spelled *one*: determinative, anaphoric common noun, and generic pronoun. These remain distinct under the D-noun analysis, but all belong within primary Noun.

Complex cardinals also separate category from function. In *two hundred books*, the whole *two hundred* fills Det; internally, *two* modifies the magnitude head *hundred* (Reynolds 2026, sec. 4). In *these two hundred books*, *these* fills Det and *two hundred* is an internal modifier. One Det function doesn’t entail a limit of one determinative lexeme per NP.

Cardinal uses and the lexemes spelled *one* remain within one primary category. Reassigning *what* and relative *which* likewise relocates a boundary inside Noun. These connected consequences of the hierarchy show what its alignment with nominal projection buys once the broader profile supports the grouping.

I favour the broader Noun category because it places the recurring nominal structure at the shared level and preserves the determinative distinctions where their restrictions apply. The alternative retains a primary boundary and crosses it in the projection rule. Both are coherent grammars. The choice turns on whether the shared profile warrants that parent category, with the modifier restrictions counted against it; reducing the number of primary categories alone wouldn’t suffice.

If determinative-headed and genitive expressions require different projection rules after their independently motivated restrictions are held fixed, the shared-projection proposal in §7.1 loses its advantage. That would favour separate phrase types. Retaining a separate primary D requires the further case that the category boundary captures the recurring differences better than a determinative subcategory within Noun.

# 8 Conclusion

English determinatives belong within Noun as a coordinate subcategory alongside common nouns, proper nouns, and pronouns. The combined case draws on argument and determiner functions, referential contrasts, inflection, and nominal dependents. Quantificational common nouns make the connection especially clear: their selected partitives and restricted dependents already occupy part of the grammatical territory associated with determinatives.

The resulting category retains internal differences. Articles lack ordinary independent uses; the *no*/*none* paradigm requires form selection; degree modifiers require construction-specific permissions. The proposed treatment of *what* and relative *which* relocates a boundary within Noun. These distinctions constrain the proposed subcategories within their shared parent.

Determinatives then inherit nominal projection and ordinary Head relations across bare, partitive, and externally determined uses. A separate-D grammar can reproduce that structure through cross-category licensing. I prefer the hierarchy that makes the recurring nominal grouping explicit, accepting the narrower modifier generalizations it requires. It aligns lexical categorization with the broader grammatical profile while preserving determinatives’ distinctive place within Noun.

# Data and analysis materials

The accompanying supplements are [*Replication audit of the English determinative–pronoun feature matrix*](run:matrix-audit.pdf) and [*CGELBank concordance and extraction notes*](run:corpus-documentation.pdf). The `analysis/` directory preserves their input files, provenance records, scripts, numerical outputs, and sentence concordance. Its README identifies the files and reproduction procedures.

Acknowledgements. For the September 2026 revision, GPT-6 (Astra), Claude Opus 5, Claude Haiku 4.5, and GLM-5.3-Flash assisted drafting, source retrieval, script development, or critical review; GPT-5.6 (Sol) checked numerical outputs. The accompanying materials record the tools and their uses. Responsibility for the analysis is mine.

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

