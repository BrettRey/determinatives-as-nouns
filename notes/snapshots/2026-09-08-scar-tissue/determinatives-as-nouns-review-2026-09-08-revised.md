# Determinatives as nouns in English

Brett Reynolds — September 2026 working draft

Revised after the opening comments and April comparison. Trees and schemata are shown as text, and footnotes appear beside their paragraphs. The LaTeX source remains the manuscript master. [Previous comments and replies](determinatives-as-nouns-review-2026-09-08.md) · [Updated April comparison](april-current-argument-comparison-2026-09-08.md).

# Abstract

I argue that English determinatives belong within Noun, preferably as a fourth coordinate subcategory alongside common nouns, proper nouns and pronouns. The argument extends the grounds on which *The Cambridge grammar of the English language* already includes pronouns despite their distinctive inflection and restricted dependents. A matched comparison of independent uses, partitives, modification and a compound construction supports shared nominal organization while preserving lexical restrictions, including those of articles. Ordinary headedness is a further proposal: a separate-D grammar can also permit it. The choice concerns which generalizations belong to the lexical hierarchy and which require constructional rules. Corpus attestations document the constructions; a feature-matrix reanalysis qualifies earlier evidence for the category boundary. Distributional differences warrant retaining determinative and pronoun as distinct subcategories; they don’t by themselves establish a primary-category boundary or decide between coordinate and nested membership within Noun.

**Keywords:** determinatives, nouns, lexical categories, noun phrases, English

# 1 The question

What is the categorial relationship among words such as *some*, *me*, *apple* and *Brett*? I argue that all four are nouns. I call this the determinative-noun or D-noun analysis.

Following *The Cambridge grammar of the English language* (*CGEL*; Huddleston and Pullum (2002)), I use determinative for the category containing articles, demonstratives and quantifiers such as *the*, *this*, *some*, *every* and *many*. I reserve determiner for a syntactic function within the noun phrase. Capitalized Noun names the proposed superordinate category containing common nouns, proper nouns, pronouns and determinative nouns. The distinction separates what kind of word *some* is from what its phrase does.

> Note 1. For a fuller inventory, see the online [“List of determinatives in English”](https://www.cambridge.org/highereducation/api/resources/2AC8DF5CA558F8A6FCDFACD0EAF8EA08) accompanying Huddleston et al. (2022).

Figure 1 shows the proposed structures for *take some apples* and *take some*. In each tree, *some* heads a nominal (Nom), which heads a noun phrase (NP). A nominal contains a head noun and its internal dependents, excluding an external determiner. Function labels appear above category labels: Det marks determiner and Obj object. `N_D` and `N_common` distinguish noun subcategories; V and VP mark verb and verb phrase.

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

```text
VP
├── Head: V
│   └── take
└── Obj: NP
    └── Head: Nom
        └── Head: N_D
            └── some
```

Figure 1: The proposed analyses of *take some apples* (first tree) and *take some* (second tree). The `N_D`–Nom–NP sequence above *some* is shared across uses. Its NP functions as Det within the object in the first tree and as the whole object in the second tree.

Inclusion of determinatives such as *some* within Noun is the principal thesis. The two structures add the proposal that *some* heads its own NP in both uses. I provisionally favour coordinate subcategories, pending evidence that an intermediate category captures further generalizations.

*CGEL* already places common nouns, proper nouns and pronouns within Noun. It expressly justifies pronoun membership by the functions of pronoun-headed phrases, despite differences in inflection and dependents (Huddleston and Pullum 2002, 327–28). The question is whether determinatives meet comparable grounds for inclusion. Differences from common nouns alone cannot settle that question: the accepted noun subcategories already differ from one another.

Palmer (1924, 24) proposed placing determinatives with pronouns. He cited disagreement about their classification and most members’ ability to serve either as pronouns or as modifiers of nouns. The passage is reproduced in Reynolds (2013, 3). The D-noun analysis retains the distinction between those categories within a common superordinate category.

The proposed extension gives independent *some* the phrase structure already needed for other nouns. In determiner function, determinative phrases and genitive NPs share the phrase type NP, while retaining their distinct licensing conditions. The inclusion of auxiliaries within Verb supplies a precedent for this kind of extension: a closed category can retain its distinctive syntax within a broader lexical category (Pullum and Wilson 1977).

Two comparisons are central: with *CGEL*, which places determinatives outside Noun, and with Hudson’s analysis, which places the words he calls determiners within pronoun and pronoun within noun (Hudson 2004, 2010). Evidence for nounhood alone doesn’t decide between coordinate subcategories and Hudson’s nesting. Table 1 isolates the structural comparison; Table 2 locates the proposals taxonomically.

To head off a likely misunderstanding: under the D-noun analysis, *apples* still ultimately heads the whole noun phrase *some apples*. Assigning *some* to Noun doesn’t adopt the DP hypothesis, in which functional D heads the whole expression (Abney 1987). The claims concern synchronic English lexical categories.

I first distinguish the competing analyses, then establish what the existing noun subcategories share and how determinatives compare. Independent uses, partitives and modification establish the constructions to be explained. The corpus documents these uses; the matrix reanalysis limits an earlier argument about the boundary. The final grammatical fragment carries the comparative argument by showing how each account allocates the shared generalizations and lexical restrictions.

# 2 Classification, headedness and function

## 2.1 Three decisions a grammar must make

Start with *some apples* and independent *some*. In *CGEL*, *some* is a determinative in both. Before *apples*, its phrase functions as determiner. Independently, *some* jointly fills the determiner and head functions: *CGEL* calls this fusion of functions (Huddleston and Pullum 2002, 410–12).

The D-noun analysis retains determinative alongside common noun, proper noun and pronoun within Noun, allowing independent *some* to function as an ordinary head. Table 1 isolates the comparison. Here DP abbreviates determinative phrase, and `N_D` marks a determinative noun.

Table 1: The same expressions under *CGEL* and the D-noun analysis. Both accounts retain the lexical identity of *some*; they differ in its superordinate category and in the structure assigned to its independent use.

| Expression | *CGEL* | D-noun analysis |
|:---|:---|:---|
| *some apples* | A DP headed by *some* functions as determiner in the larger NP ultimately headed by *apples*. | An NP headed by the determinative noun (`N_D`) *some* functions as determiner in the larger NP ultimately headed by *apples*. |
| *some* in *I’ll take some* | A DP headed by *some* functions as fused determiner–head within an NP. | The `N_D` *some* fills ordinary head function in a Nom, which heads the NP. |

The proposal lets independent *some* use ordinary noun-phrase structure. Lexical restrictions remain: *every apple* is grammatical, but \**I’ll take every* isn’t an ordinary way to accept apples. Making *every* a noun doesn’t give it every use available to *some*. Section 8.2 states the structural rules and lexical restrictions separately so that their contributions can be assessed.

Category, headedness and function therefore require separate decisions. A category assignment says which lexical generalizations apply to a word. A headedness analysis identifies a phrase’s organizing head. A function label identifies a constituent’s relation to its containing construction. An NP can function as determiner, as in *Kim’s book*, and a determinative-headed phrase can have another function, as in *the many people* (Payne et al. 2010; Pullum and Miller 2022).

The N–Nom–NP sequence illustrated in Figure 1 is nominal projection, and the noun is the NP’s ultimate head. Within *almost every experienced teacher*, *almost every* functions as determiner and *experienced teacher* as head nominal. Within the determiner phrase, *almost* modifies *every*.

I abbreviate noun and determinative as N and D, and determiner and modifier functions as Det and Mod. Det–Head marks fusion. In the proposed trees, `NP_D` is an NP headed by a determinative noun; the subscript identifies a subcategory. *CGEL*’s DP is a dependent phrase in *some apples*, distinct from the whole expression called DP under the DP hypothesis.

Some earlier proposals concern underlying representation. Postal (1966) unifies personal pronouns and articles through an underlying article analysis. Sommerstein (1972, 197–203) reverses the direction, assigning underlying NP structure to the definite article and personal pronouns, with relative-clause structures contributing further descriptive material. These underlying structures don’t by themselves place the surface lexical categories in the hierarchy in Table 2. Déchaine and Wiltschko (2002) further distinguish pro-DP, pro-φP and pro-NP, connecting different pronominal projections with distribution and binding. Their proposal makes the structure associated with a pronoun an additional question for comparison.

Lyons (1968, 232–35) supplies a useful methodological distinction: distribution can be compared at different levels of categorization. Two expressions may belong together at one level and differ at a more specific level. His discussion of articles, demonstratives and personal pronouns also emphasizes shared definiteness and deictic contrasts (Lyons 1968, 279).

Bruening (2020) supplies a generative defence of N-headed nominals, drawing on selection and conventionalized expressions. Such arguments support N-headed phrase structure without by themselves assigning determinatives to the noun category.

## 2.2 The nearest alternatives

Keeping a word in one category across dependent and independent uses leaves its taxonomic position open. Table 2 sets out selected arrangements, from three separate primary categories to successive inclusion. Common and proper nouns remain within noun throughout the comparison. The D-noun analysis differs from *CGEL* by including determinative within Noun, and from Hudson by placing it alongside pronoun.

Table 2: Selected taxonomic arrangements. Noun contains common and proper nouns in every row; its other members vary. Logical comparisons locate the cited proposals. The Hudson row abstracts from differences in lexical inventory explained in the text.

| Relation among Noun, pronoun and determinative | Account or status |
|:---|:---|
| Noun, pronoun and determinative are separate primary categories. | Logical comparison |
| Pronoun is within Noun; determinative is a separate primary category. | *CGEL* |
| Determinative is within Noun; pronoun is a separate primary category. | Logical comparison |
| Pronoun and determinative are coordinate subcategories of Noun. | D-noun analysis |
| Determinatives belong within pronoun, which is within Noun. | Hudson |
| Pronoun is within determinative, which is within Noun. | Reverse nesting for comparison |

Anderson (1997) groups names, pronouns and determining words as a notional {N} category, with common nouns represented separately. His {N} differs from the inclusive Noun proposed here and isn’t one of the arrangements in Table 2.

Hudson’s nominal analysis makes a different choice. In Hudson (2010, 253–54), noun has the subcategories common noun, proper noun and pronoun. Hudson identifies the words he calls determiners by valency: the kinds of dependent an item permits. In Hudson’s terminology, a determiner is a pronoun that permits the relevant common-noun dependent (Hudson 2004, 9–10). Identifying these words doesn’t require another category node.

*CGEL* and Hudson classify different inventories. Hudson’s criteria in the 2004 paper centre on licensing a singular count common noun and on mutual exclusion in that use. He sets aside *all*, cardinal numerals and quantifiers restricted to plural or non-count nouns. *CGEL*’s determinative category is broader. Comparing the classifications therefore requires checking which words and constructions each covers.

Hudson also separates dependency from phrase headedness. His 2004 account permits mutual dependency between determiner and common noun, with different constructions selecting different external heads (Hudson 2004, 7–9). Temporal adjuncts provide an illustration: *We met that day* depends on the temporal meaning of *day*. Such restrictions support a common-noun head for temporal adjuncts (Hudson 2004, 10–12).

The alternative to a separate primary D needn’t preserve a unified determinative subcategory. Spinillo (2004) proposes redistribution among existing categories, retaining *the*, *a* and *every* as an expanded article category. That proposal makes the restricted members a separate category; the D-noun analysis retains them inside the wider determinative subcategory.

For demonstratives and forms such as *some* and *all*, Spinillo (2004, 140–44) rejects switching between determiner and pronoun categories according to whether a noun follows. She compares the alternation with verbs and prepositions used with or without a complement. The D-noun analysis agrees that the two uses needn’t involve different lexical categories. It differs in retaining determinative as the subcategory across those uses.

Independent nominal use supports inclusion within Noun, but doesn’t itself select the pronoun subcategory. The demonstratives’ deictic properties make a pronominal grouping plausible; the question is how far that grouping captures the wider inventory’s syntax. The comparisons below address modifier profiles (§3.5), the proposed determinative–pronoun boundary (§6), and the positive connections linking restricted *every* to other quantifiers (§7). Redistribution must be assessed against those connections as well as independence.

Van Eynde (2003) likewise rejects a separate determiner category, but assigns determining expressions to adjective or noun on morphological and agreement evidence, chiefly from Italian and Dutch. His analysis separates lexical category from the features governing determination. A noun-headed NP account therefore needn’t unify every determining expression as nominal.

# 3 The D-noun analysis

## 3.1 The existing standard of nounhood

The starting category is Noun as *CGEL* already constitutes it. Its discussion of pronouns makes the reasoning explicit: they differ from prototypical nouns in inflection and permitted dependents, but qualify through heading phrases with the functions of common- and proper-noun-headed phrases (Huddleston and Pullum 2002, 327). Table 3 sets out some of the variation already accepted within that category.

Table 3: Contrasts already accommodated within *CGEL*’s Noun. These are typical profiles, with further restrictions and exceptions within each subcategory (Huddleston and Pullum 2002, 327–28, 425–30, 517–20).

| Dimension | Common noun | Proper noun | Pronoun |
|:---|:---|:---|:---|
| Inventory | Open | Open to new names | Closed |
| Inflection | Number and genitive | Genitive; restricted plural uses | Case paradigms in personal pronouns |
| Determination | Broad contrasts; singular count arguments normally require it | Restricted in primary naming uses | Normally excluded |
| Internal modification | Productive AdjP and nominal modification | Restricted embellishments | Restricted, as in *poor old me* |

Common nouns supply the most familiar profile, but they don’t supply an entry test that every noun subcategory has to pass unchanged. Pronouns remain nouns despite their closed inventory and restricted modification; proper nouns remain nouns despite their distinct naming uses. An argument that excludes determinatives on these kinds of difference therefore needs to explain why the difference warrants a primary-category boundary in this case.

Meaning and reference also vary within the existing category. *Apple* conveys a descriptive classification; *Kim*, in its primary naming use, identifies through a name; *she* supplies limited descriptive content and depends on context. Noun already accommodates those differences. The quantificational or deictic contribution of a determinative therefore needs to be assessed alongside its grammar, rather than measured against common-noun semantics alone.

The distributional comparison follows *CGEL*’s pronoun argument: a range of determinatives occurs in subject, object and complement-of-preposition positions without another overt nominal head. The pattern recurs across lexemes and appropriate contexts. This establishes systematic nominal use before choosing its internal analysis. The examples in §4 compare all four proposed subcategories in the same positions.

The category-level argument carries a separate burden for restricted members. Pronoun forms themselves don’t all pass the argument-position test: dependent genitives such as *my* have positive support from their paradigms. For determinatives, the corresponding argument needs to establish both a broadly nominal constructional profile and the restricted members’ integration into that category. Section 7 supplies the latter argument; merely listing exceptions wouldn’t.

External distribution alone is insufficient: adjectival constructions such as *the rich* also fill those positions. The further comparison concerns the breadth of independent use, determination, partitives and internal modification. Together these properties support a nominal subcategory profile. Restrictions on particular lexemes or readings remain part of the description, just as they do within the existing Noun category; §§4.6 and 7 examine them directly.

The distinction at issue is thus one of taxonomic level. A closed inventory, reduced descriptive content or unusual modifier selection can establish a distinctive subcategory without establishing its exclusion from Noun. The decisive comparison is whether the shared nominal behaviour and the local differences are better captured by extending existing nominal structure or by preserving a separate primary D. Section 8.2 holds the lexical restrictions fixed to make that comparison explicit.

By inheritance I mean that a property stated for a superordinate category is available to its subcategories, subject to stated restrictions. The D-noun analysis extends the division of labour already used within Noun: general rules supply nominal projection, subcategory rules constrain combinatorics, and lexical entries distinguish such forms as independent *some* and dependent-only *every*.

## 3.2 Nouns already function as determiners

Determiner function also cuts across the existing noun subcategories. Compare *my book*, *Kim’s book* and *the king’s book*. The determiner is an NP ultimately headed by a pronoun, a proper noun and a common noun respectively (Huddleston and Pullum 2002, 354–55, 470–71). In the last example, *the* determines *king* inside the genitive NP, while that whole NP determines *book*.

> Note 2. *CGEL* assigns these genitives the combined function Subject–Det (Huddleston and Pullum 2002, 472–73). I treat them as Det here, without the additional subject function. Their determining role supplies the relevant comparison; accepting the further subject analysis would leave the nounhood argument intact.

These expressions establish more than the possibility of a noun in Det function. All three admitted noun subcategories already contribute phrases to that function, subject to the genitive construction’s restrictions. The D-noun analysis extends this nominal pattern to determinative-headed phrases. Number, countability and other selectional conditions still distinguish the determining expressions; their shared function doesn’t imply unrestricted interchangeability.

Figure 2 illustrates the proper-noun case. Function labels appear above category labels: Det:NP identifies an NP functioning as determiner. The genitive NP *Kim’s* functions as Det, while *book* ultimately heads the larger NP. This existing configuration provides the comparison for the determinative analysis that follows.

```text
NP
├── Det: NP[gen]
│   └── Head: Nom
│       └── Head: N_proper
│           └── Kim's
└── Head: Nom
    └── Head: N_common
        └── book
```

Figure 2: The genitive NP *Kim’s* functions as determiner within *Kim’s book*, ultimately headed by *book*. The representation abstracts from the internal realization of genitive marking.

## 3.3 Dependent and independent uses

The genitive comparison clarifies the two analyses in Figure 1. In *take some apples*, the NP headed by *some* fills Det, as *Kim’s* does in *Kim’s book*; the common noun heads the larger NP. In *take some*, *some* heads the whole object NP. The lexeme retains its subcategory and nominal projection across these uses, while its containing phrase fills a different function.

The NP headed by *some* inside *some apples* isn’t interchangeable with every NP. The determiner construction selects a determinative-headed phrase, a suitable genitive NP, or another licensed expression. Section 8 includes this restriction in the comparison of grammars.

## 3.4 Two heads in one expression

Figure 3 separates the two modifier relations in *almost every experienced teacher*. The AdvP *almost* modifies the determinative noun *every*; the AdjP *experienced* modifies the common noun *teacher*, which ultimately heads the outer NP.

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

## 3.5 What the modifier contrast establishes

Payne et al. (2010, 40–42) defend keeping *few*, *any* and related forms in one lexical category across dependent and independent uses. The modifier remains an adverb in *hardly any money*/*hardly any*; changing the item’s function doesn’t require changing its category. The D-noun analysis preserves that continuity. It also preserves their contrast between adverbial premodification, as in *almost anybody*, and adjectival postmodification, as in *nothing absolute*.

These contrasts support distinguishing determinatives from pronouns and common nouns. The further question is the taxonomic level of that distinction. Within the proposed Noun, the determinative subcategory licenses *hardly any* and *almost every*; the common-noun subcategory licenses *experienced teacher*. Neither \**experienced every* nor \**almost teacher* follows. The existing modifier profiles remain, while their relation to the broader category changes. Section 8.3 considers the cost of that change explicitly.

Payne et al. (2010, 60–61) also argue that distribution alone can’t decide whether adjectives and adverbs are inflectional variants of one category or derivationally related members of different categories. The D-noun analysis preserves distinct lexical subcategories and makes no inflectional-variant claim. Their methodological constraint still applies: shared positions alone don’t settle category status. Here the fuller constructional profile is assessed against the grounds on which *CGEL* already includes divergent subclasses within Noun.

# 4 Evidence for nominal structure

The evidence establishes a recurring nominal pattern across independent uses, partitives and modification. These are overlapping observations: *Some left* illustrates both external distribution and structural saturation, not two independent tests. Fusion and ordinary headedness can cover this pattern. The comparisons below identify where their representations diverge; §8.2 assesses the resulting organization of the grammar.

## 4.1 Breadth of independent use

Independent use is widespread within the determinative inventory. *CGEL* discusses such uses for demonstratives and quantifiers including *some*, *all*, *both*, *many*, *few*, *several*, *each*, *either*, *neither*, *much* and *enough*, while recording lexical restrictions and the separate forms *no*/*none* (Huddleston and Pullum 2002, 371–72, 410–24). The generalization is about the availability of constructions across a lexical category, not the unrestricted acceptability of every member in every sentence frame.

In the constructed examples in (1), compare the positions occupied by the bracketed NPs: subject, object and complement of a preposition. Assume that a woman named Kim and a group of people are already under discussion. These positions admit NPs containing words from each proposed noun subcategory; the competing analyses assign different internal structures to independent *some*.

(1a) *\[People\] left.* — *I see \[people\].* — *with \[people\]*

(1b) *\[Kim\] left.* — *I see \[Kim\].* — *with \[Kim\]*

(1c) *\[She\] left.* — *I see \[her\].* — *with \[her\]*

(1d) *\[Some\] left.* — *I see \[some\].* — *with \[some\]*

The pattern extends beyond a few compounds or a single lexicalized expression. For this closed category, productivity concerns the availability of independent use among established members under appropriate conditions, rather than the licensing of new lexical items.

Material before a determiner requires a separate comparison. *CGEL* treats *all*/*both* in *all/both the books* as predeterminer modifiers, *quite*/*rather* before *a good idea* as peripheral modifiers, and *such*/exclamative *what* before *a disaster* as adjectives (Huddleston and Pullum 2002, 433–37). The fixed *many a* is a complex determinative restricted to Det function (Huddleston and Pullum 2002, 394). The *half* in *half a cake* is a common noun used as a predeterminer modifier (Huddleston and Pullum 2002, 434). These constructions don’t add evidence for independent determinative heads.

Adjectival independent uses prevent a simple inference from external distribution to nounhood. *The rich* and *the poor* can fill nominal argument positions. Comparative and superlative adjectives also head expressions without a human-class interpretation: *CGEL*’s *the most important of her criticisms* is an NP containing a partitive *of*-phrase (Huddleston and Pullum 2002, 332–33, 416–23).

Independent *some* can form a one-word NP, whereas an NP with *rich* as fused head normally requires a determiner on the human-class reading. That is a local contrast: argument NPs headed by singular count common nouns also need determination.

## 4.2 Structural saturation and interpretation

With a group of people under discussion, *Some left*, *Many came* and *All agree* illustrate structural saturation: an argument expression can be syntactically complete without another overt head or determiner.

Syntactic completeness differs from contextual interpretation. In *I’ll take some*, the relevant substance or set may be supplied by discourse or the situation. That dependence doesn’t establish a deleted common noun: ordinary pronouns also depend on context.

The comparison with ordinary pronouns and proper nouns is structural as well as interpretive. In *She left* and *Kim left*, *CGEL* permits an NP headed by a nominal with no determiner. Applying that structure to *Some left* preserves the same division between a complete NP and its context-dependent reference. The dependent use of *some* doesn’t by itself require a Det function inside every independent occurrence.

Nounhood also remains compatible with fusion. *CGEL* analyses *mine* as fused Det–Head when it stands for a possessed entity in an anaphoric context, but as pure Head in the predicative possessive use *it’s mine* (Huddleston and Pullum 2002, 410–11). That comparison blocks an objection from fusion to nounhood. The positive case for ordinary headedness instead extends the structure available to *she* and *Kim*.

Generalizing expressions such as *Many are called, few are chosen* and *Enough is enough* need no previously uttered common-noun phrase. They rule out a mandatory overt-antecedent requirement, but a silent-noun account could supply a generic restriction. Such examples don’t decide whether the restriction belongs in semantics or syntax.

Saturation establishes a fact that both fusion and ordinary headedness accommodate. It adds an interpretive clarification to the distributional comparison, rather than independently selecting one structure.

## 4.3 Partitives locate the quantificational head

In *some of the wine*, *some* specifies a quantity drawn from an identifiable amount of wine. The NP *the wine* denotes the partitive domain: the whole from which that quantity is drawn. This NP is complement of *of*. A pronoun-headed NP or independent genitive NP can express the domain too: *many of them*, referring to previously mentioned people, or *some of Kim’s*, referring to Kim’s apples.

Compare where the common noun occurs in *some apples* and *some of the wine*. In the partitive, *wine* is embedded inside the *of*-phrase, so it can’t be the lexical head of the whole NP. The determinative *some* has an organizing role in that larger expression.

Figure 4 gives the D-noun analysis, with the *of*-phrase functioning as complement within Nom. I follow *CGEL*’s explicit partitive analysis and tree (Huddleston and Pullum 2002, 411–12); its introductory description on p. 411 also calls this PP a modifier. The inner NP *the wine* is abbreviated.

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

Figure 4: The proposed structure of *some of the wine*. Follow the Head relations from the outer NP to *some*. The common noun *wine* is inside the complement PP and doesn’t head the whole expression.

*CGEL* accounts for these facts through Det–Head fusion. Partitives support the determinative’s head-like role, while leaving the choice between fusion and ordinary headedness open.

The overt quantifier and domain already supply a compositional interpretation of *some of the wine*. A silent common noun would need to explain something further, such as a restriction on interpretation or modification that the overt-head account misses. The construction itself supplies no such requirement. I therefore prefer an overt-head analysis over an otherwise equivalent null-head analysis; fusion remains compatible with that preference.

The D-noun analysis treats *some* and *some of the wine* as sharing nominal projection, with an added domain phrase in the partitive. Modification provides a further comparison of internal structure.

## 4.4 Modification tests the internal analysis

The pair *the lucky survivors*/*the lucky few* makes ordinary nominal structure attractive, but doesn’t exclude fusion. *CGEL* explicitly permits determinatives used as internal modifiers to fuse with Head, as in *the other two* and *these few here* (Huddleston and Pullum 2002, 415–16). Its analysis of *the few mistakes* assigns *the* to Det and *few* to Mod (Huddleston and Pullum 2002, 392). That dependent use supplies the counterpart for a Mod–Head analysis of independent *few* after an external determiner.

Figure 5 compares the resulting analyses of *the lucky few*. Both have an overt Det and a Nom modified by *lucky*. In the D-noun analysis, *few* fills ordinary Head. In the fusion analysis, its DP fills Mod–Head. The competing structure thus uses machinery already needed for adjectival fusion; it requires neither a silent noun nor conversion.

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
└── Head: Nom
    ├── Mod: AdjP
    │   └── lucky
    └── Mod–Head: DP
        └── Head: D
            └── few
```

Figure 5: *The lucky few* with ordinary Head (first tree) and Mod–Head fusion (second tree). The determiner is separately realized in both. Internal structure within the article phrase and AdjP is suppressed.

Table 4 compares four constructions. Separate D with ordinary headedness can assign *few* the same Head relations as the D-noun analysis while retaining D as its lexical category; §8.2 supplies that alternative’s rules.

Table 4: Head and dependent functions under matched analyses. Each independent expression is an NP; *the* fills Det wherever it appears. The ordinary-Head column applies to both taxonomies permitting ordinary determinative heads.

| Expression | Separate D with fusion | Ordinary determinative Head |
|:---|:---|:---|
| *few survivors* | *few*: Det; *survivors*: Head | Same functions |
| Independent *few* | *few*: Det–Head | *few*: Head |
| *the lucky few* | *few*: Mod–Head; *lucky*: Mod | *few*: Head; *lucky*: Mod |
| *the idle rich* | *rich*: Mod–Head; *idle*: Mod | Same fusion and modifier functions |

The local economy favours fusion: the rule for *the idle rich* can also accommodate *the lucky few*. Ordinary headedness instead unifies *few* across its bare and externally determined uses, without alternating Det–Head and Mod–Head. Neither account gains coverage from this example alone. The comparison is between sharing a fusion construction across D and adjective, and sharing ordinary nominal headedness across determinative constructions.

Why retain adjective outside Noun? The adjectival construction is restricted to particular lexical and interpretive groups, with additional determiner restrictions: compare the human-class *the rich* with \**these very poor* (Huddleston and Pullum 2002, 416–17). Determinative independent use extends across demonstratives and quantifiers with varied domains and determining contrasts. This difference favours organizing nominal projection at the determinative-subcategory level while retaining constructional licensing for adjectival fusion. It supplies a comparative reason, not a necessary-and-sufficient membership test.

The constructed *the remaining three* extends the modifier pattern to cardinals. It doesn’t independently decide whether *three* is determinative or has a common-noun use: Reynolds (2026) argues for both uses of cardinals. Section 8.3 treats their unification as a consequence conditional on that analysis. Likewise, the adjectival modification of *few* doesn’t transfer to *every*; the lexical restrictions remain.

## 4.5 Fusion and a compound comparison

In Payne et al. (2007), a fused constituent fills two adjacent functions: Head and a dependent function of the same phrase or an immediate dependent. Its category matches the dependent in a non-fused counterpart; its containing phrase projects from that counterpart’s head category. Thus independent *some* retains the D category of dependent *some* in *some apples*, within an NP. Ordinary headedness replaces this relation with nominal projection; lexical restrictions on independence and form selection remain.

The harder case is *hardly anyone present*. Payne et al. (2007, 581–83) assign the adverb to DP structure and the adjective to nominal structure. The compound takes the premodifiers of its determinative base: compare *hardly any writer present*. The adjective realizes a specialized restrictor function, restricted to post-head position and non-recursive. Figure 6 contrasts this account with an ordinary-Head analysis.

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
NP
└── Head: Nom
    ├── Det–Head: DP
    │   ├── Mod: AdvP
    │   │   └── hardly
    │   └── Head: D
    │       └── anyone
    └── Mod: AdjP
        └── present
```

Figure 6: *Hardly anyone present* with ordinary Head (first tree) and fusion (second tree). Both post-head Mod positions realize the specialized restrictor. In the fusion tree, DP fills Det of NP and Head of Nom, following Payne et al. (2007, 582, (13d)). Modifier-phrase interiors are suppressed.

In the ordinary-Head analysis, *anyone* inherits nominal projection from Noun and its premodifier permissions from its determinative base. The compound construction supplies the post-head restrictor permission, with the same position and non-recursion conditions as the fusion account. It doesn’t license a corresponding pre-head adjective. The compound’s ordinary argument use and exclusion of external determination are further lexical conditions; the premodifier and restrictor slots aren’t unrestricted Nom dependents.

This division extends to *someone* and *everybody*: the compound family licenses nominal argument use and post-head restrictors, while each base supplies its own premodifier permissions. It doesn’t follow that *hardly* modifies every compound. Fusion expresses the two modifier domains through DP and Nom; ordinary headedness locates both within Nom and distinguishes them through inherited and constructional conditions. That is a reformulation of the contrast, not its automatic derivation from nounhood.

The compound thus exposes a real trade-off. Fusion reuses a structural boundary to separate modifier domains; ordinary headedness reuses nominal projection while assigning the domain restrictions to the determinative base and compound construction. Both need the specialized restrictor condition. This worked case establishes coverage without claiming that all compound properties favour abandoning fusion.

## 4.6 Predicative uses and their restrictions

Predicative complementation provides a less uniform comparison. *CGEL* records *Its advantages are several* and *Their enemies were many*, describing the latter pattern as uncommon and formal (Huddleston and Pullum 2002, 392, 395–96). Such uses are available to only part of the determinative inventory. The ordinary independent uses of *some* therefore cannot license every determinative in every predicative frame; *every* and the articles retain their restrictions.

The comparison also depends on what the predication expresses. *She is a doctor* ascribes a property, whereas *That is Kim* identifies a person. *CGEL* excludes specifying *be* clauses from its noun–adjective diagnostic because phrases from other categories occur in them too (Huddleston and Pullum 2002, 536). Merely placing an expression after *be* therefore provides no uniform nounhood test.

Restrictions in the opposite direction already occur within nominal grammar. A bare-role NP such as *president* is licensed in *I’d like to be president*, but requires determination in the corresponding object use *I’d like to meet the president* (Huddleston and Pullum 2002, 328). Predicative and argument uses thus need separate conditions within Noun itself. The determinative asymmetries belong in that comparison; they don’t establish exclusion merely by departing from a common-noun substitution frame.

## 4.7 What the combined pattern supports

Independent uses, partitives and modification establish a systematic range of nominal constructions. They support extending the comparison with existing noun subcategories beyond *Some left*. Their coverage is shared by the fusion and ordinary-Head accounts; the examples don’t become discriminating evidence simply by being accumulated.

I favour ordinary headedness because it gives bare, partitive and externally determined uses the Head relation already available to nouns. Fusion instead relates them to dependent counterparts and distinguishes Det–Head from Mod–Head. That machinery is already needed for adjectives and genitives, and the compound comparison shows a benefit of retaining its structural domains.

The decision therefore turns on grammatical organization. The pronoun precedent favours inheritance through Noun; the competing structures retain other generalizations. Section 8.2 compares both headedness choices under both taxonomies. It makes explicit what the distributional pattern leaves undecided.

# 5 What the empirical record establishes

## 5.1 A reproducible corpus inventory

CGELBank is a corpus of English sentences annotated using categories and functions developed from *CGEL* (Reynolds et al. 2023). It supplies inspectable examples with stable sentence identifiers. Its category and fusion labels already encode analytical decisions, so label counts can’t independently establish that *CGEL* or the proposed replacement is correct.

I inventory four CGELBank datasets containing 220 sentence trees and 3,390 lexical nodes with overt text. Of those nodes, 387 are annotated D. Table 5 compares selected forms by their local function. These are counts of annotated uses, not estimates of a lexeme’s capacity for independent use. Appendix A gives the source revision, selection criteria and extraction procedure; an accompanying concordance preserves the sentences and their identifiers.

The sample has no determinative tokens of bare *few*, *either* or *neither*. For these forms, the breadth claim in §4 rests on *CGEL*’s grammatical descriptions and judgments; this corpus sample supplies no confirming attestations.

Table 5: Selected forms by local function in CGELBank. Compare forms attested in both Det and Det–Head uses with forms restricted to Det in this sample. Other includes all remaining functions. Counts group forms by corpus lemma, including singular and plural demonstratives.

| Form     | Total | Det | Det–Head | Other |
|:---------|------:|----:|---------:|------:|
| *the*    |   129 | 129 |        0 |     0 |
| *a*      |    90 |  89 |        0 |     1 |
| *every*  |     3 |   3 |        0 |     0 |
| *this*   |    28 |  21 |        7 |     0 |
| *that*   |    12 |   5 |        7 |     0 |
| *some*   |     5 |   3 |        2 |     0 |
| *all*    |    11 |   3 |        5 |     3 |
| *both*   |     4 |   2 |        1 |     1 |
| *many*   |     3 |   0 |        1 |     2 |
| *a few*  |     2 |   1 |        1 |     0 |
| *each*   |     2 |   0 |        1 |     1 |
| *enough* |     6 |   2 |        1 |     3 |

All 65 Det–Head occurrences were inspected in their source sentences. They include ordinary arguments, partitives, compounds such as *something*, floating quantifiers, degree and frequency expressions, numerical fragments and age supplements. Within *about 30 seconds*, for example, the numeral’s nominal projection is embedded in the determiner *about 30*. Reporting all 65 occurrences as independent argument uses would conflate different constructions.

Two attestations illustrate independent quantifiers with a recoverable domain:

(2a) *Went there yesterday: we are trying to decide between two different Honda models, so we wanted to test-drive both back to back.*

(2b) *I rarely listen to the news or to what politicians or lawyers say because so many tell lies that none have credibility so what’s the point?*

In (a), *both* refers to the two Honda models. In (b), *politicians or lawyers* supplies a domain for *many* and *none*. These attestations illustrate independent quantifiers whose interpretation is supplied by preceding discourse. Appendix A identifies the source sentences.

CGELBank also attests *I need something reliable and good looking*; the concordance gives the sentence identifier. The adjectives follow the compound determinative *something*, contrasting with the premodification in *the lucky few*.

The inventory attests independent and internally expanded determinatives, but provides no representative productivity estimate or controlled test of the modifier contrasts. The constructed examples in §4 remain grammatical judgments.

## 5.2 What distributional differences establish

Do determinatives and pronouns differ too much to belong to the same broader category? Reynolds (2021b) compared 73 determinative forms and 65 pronoun forms using a binary feature matrix: each row is a form, and each column records a morphological, phonological, semantic or syntactic property. The matrix contains no common or proper nouns, so it can establish differences between the two supplied categories but can’t test nounhood directly.

The reanalysis qualifies that evidence. DISCO compares the supplied partition with shuffled partitions; k-groups searches for clusters without using category labels. The coded profiles are separated, but agreement between clustering and *CGEL*’s labels depends on initialization and feature selection. Removing explicit analytical labels substantially reduces agreement. Appendix A gives the numerical results, the public-file discrepancy and the permutation interpretation. The results correct an earlier boundary argument; they don’t positively support D-noun classification.

Differences between coded profiles don’t determine taxonomic rank: subcategories of one category can differ sharply. The reanalysis supports distributional separation between the determinative and pronoun forms in this inventory, while leaving their classification within Noun open. Reynolds’s original discussion likewise recognized significant divisions within categories and left a nested nominal analysis open (Reynolds 2021b).

# 6 Coordinate subcategories and inheritance

Should determinatives and pronouns be coordinate subcategories, or should determinatives belong inside pronoun? The matrix reanalysis leaves that choice open. Its pronoun rows follow *CGEL*’s classification, whereas Hudson’s pronoun category includes the words he calls determiners. Comparing these hierarchies requires aligning their lexical inventories and asking which generalizations can be stated for each superordinate category.

An intermediate pronoun-plus-determinative category would be useful if it collected generalizations otherwise repeated. Different property profiles alone don’t favour coordination: a subtype can differ sharply from the rest of its superordinate category. Core personal pronouns’ case, reflexive and person contrasts, and determinatives’ quantificational and modifier patterns, support local distinctions under either hierarchy.

Within the proposed grammar, nominal projection rules apply to all four subcategories, so they can be stated for Noun as a whole. An intermediate pronoun-plus-determinative category would need to capture additional generalizations. Reduced descriptive content and contextual interpretation are properties shared by many pronouns and determinatives. The coordinate analysis can record these interpretive properties through features or cross-classification; Hudson’s nested classification may be preferable if it collects several otherwise repeated generalizations.

Restricted determination and attributive modification provide a candidate, but proper names immediately show that the restriction cross-cuts the proposed intermediate category. In their primary use, proper names don’t select freely from the determiner system, and their adjectival embellishments are restricted (Huddleston and Pullum 2002, 517, 519–20). These properties distinguish more than pronouns and determinatives from common nouns.

Within the proposed grouping, external determination also differs systematically. Determinatives permit it in a range of independent quantificational constructions: *the few*, *the many*, *the two*, *these three*. The permissions vary by item and often require further modification; *CGEL* gives *these few here* and *the many who did* (Huddleston and Pullum 2002, 415–16). Pronouns admit external determination only marginally, and internal premodification is restricted, as in *poor old me* (Huddleston and Pullum 2002, 429–30). The candidate restriction thus doesn’t delimit the nested category.

Pro-form gender supplies a further comparison. Reynolds (2025) proposes a personhood-based system spanning pronouns and determinatives. Personal reference links pronouns such as *she* with compound determinatives such as *somebody*; non-personal reference links *it* with *something*. These constraints concern how the referent is construed. They provide a shared generalization for nominal pro-forms, but don’t decide between coordinate and nested noun subcategories. The broader pro-form system also includes non-nominal expressions, so gender alone doesn’t delimit Noun.

The coordinate classification preserves *CGEL*’s determinative/pronoun distinction while extending nominal structure across its inventory. This is a provisional organizational preference. The fragment in §8.2 doesn’t distinguish coordination from nesting by its judgments. Hudson’s intermediate category would be preferable if further syntactic generalizations over the aligned inventory reduced otherwise repeated restrictions; the present comparisons resist a default nesting without establishing its overall inferiority.

# 7 The articles and other restricted members

Why classify the articles *the* and *a* as nouns if they can’t stand independently? Independent uses motivate the D-noun analysis of *some*, *this* and *many*, but the articles require a different argument. *Every* is restricted too, while *no* has the distinct independent form *none* (Huddleston and Pullum 2002, 371–72, 410–11).

> Note 3. The restriction concerns ordinary argument use. In *the bigger the better*, *CGEL* assigns *the* modifier function within a comparative phrase (Huddleston and Pullum 2002, 1131–32, 1135–36). Its analysis distinguishes this use from Det without licensing an article-headed argument NP. The construction therefore qualifies any claim that *the* is confined to Det.

Retaining a restricted member requires three kinds of support. First, it should be paradigmatically integrated with independently identified members. Second, it should participate in the category’s characteristic semantic and grammatical contrasts. Third, its missing uses should form a local restriction while the positive connections remain. Calling an item defective summarizes that pattern; it doesn’t supply an argument for membership by itself.

The articles meet these conditions within determinative. First, they contrast with demonstratives and quantifiers before common-noun nominals: *the/a/this/every book*. Second, they participate in the same system of definiteness, number and count restrictions: *the* permits singular, plural and non-count targets, while *a* selects a singular count target. Third, their lack of ordinary independent uses leaves that determining pattern intact. These considerations support determinative membership; inclusion within Noun depends on the category-level argument.

The most frequent members in Det use needn’t be those with the widest constructional distribution. Frequency in that function alone can’t establish which members define the category profile.

Restricted members already occur within Noun. *CGEL* classifies *my* as a pronoun despite its lack of the independent distribution of *mine* (Huddleston and Pullum 2002, 470–71). Its paradigm supplies positive membership evidence. The analogy blocks an exclusion argument; it doesn’t establish article nounhood. That conclusion depends on the articles’ determinative membership and the category-level case for including determinative within Noun. Their argument-use restriction remains explicit in §8.2.

*Every* also has positive connections beyond the restricted article set proposed by Spinillo (2004). Like *each*, it expresses universal quantification and selects singular count nominals: *every teacher*, *each teacher*. Unlike *each*, it lacks ordinary independent use. It also permits *almost* and *nearly*. These facts support retaining *every* with the quantifiers without making its full distribution identical to that of *each*.

A separate article category would gain support from a cluster of synchronic restrictions shared by *the*, *a* and *every*, absent elsewhere in Noun, and otherwise requiring repeated exceptions. Lack of independent argument use alone doesn’t supply that cluster. This tests the proposed allocation of generalizations; an additional restriction needn’t by itself falsify membership.

Grammaticalization supplies background: Lyons (1999, 331–36) discusses the development of definite articles from demonstratives and of articles expressing cardinality from numerals. These histories can explain changes in content and use, but don’t establish the synchronic classification.

# 8 What the analysis simplifies

## 8.1 A shared phrase type in determiner function

In *some apples* and *Kim’s apples*, the phrases headed by *some* and *Kim* fill the same determiner function. *CGEL* assigns them different phrase types, DP and genitive NP. It also admits a restricted range of plain-case NPs and PPs as determiners, as in *what size hat* and *over thirty ties* (Huddleston and Pullum 2002, Ch. 5, §4). The D-noun analysis reduces this phrase-type inventory:

```text
CGEL:             Det: {DP, NP, PP}
D-noun analysis:  Det: {NP, PP}
```

The gain is one shared nominal projection for the determinative and genitive cases. Selection still distinguishes determinative-headed, genitive and other licensed NPs; PP determiners remain. Nor does reclassification derive definiteness or the single-Det restriction: *CGEL* already states their common determining behaviour functionally. Independent *some* and *Kim’s* are already NPs in both accounts. Giving *some* ordinary headedness is a further change, assessed separately below; genitive fusion remains available.

## 8.2 A matched descriptive fragment

A grammatical fragment is a set of rules for a specified range of constructions. Here it covers determination, ordinary subject and object uses, partitives, and the modifier and compound comparisons in §4. Four accounts cross separate versus nominal D with fusion versus ordinary Head. All receive the same lexical restrictions and constructed judgments. The predicative constructions in §4.6 fall outside the fragment.

Table 6 records use permissions: whether a form, on a given reading, can head a phrase in determiner, subject or object function. Argument use covers the subject and object NPs in examples such as *Some left* and *I saw some*. Quotation, metalinguistic naming and subordinate-clause uses of dependent genitives fall outside the fragment. Noun membership doesn’t itself grant a use permission.

Further constructional restrictions apply: *she* is a subject form, whereas the corresponding ordinary object form is *her*. The target restrictions in Table 6 concern the common-noun nominal being determined. For example, *a* requires a singular count target such as *book* in *a book*.

Table 6: Shared permissions in the fragment. For *some*, the target column concerns its unstressed use before a noun. The inventory is deliberately limited to the displayed constructions.

| Form | Det use | Argument use | Target in the Det construction |
|:---|:--:|:--:|:---|
| *the* | yes | no | Singular or plural; count or non-count |
| *a*, *every* | yes | no | Singular count nominal |
| *some* | yes | yes | Plural count or non-count nominal |
| *few* | yes | yes | Plural count nominal |
| *my* | yes | no | No number/count restriction in this fragment |
| *she* | no | yes | None |

The ordinary-Head variant has three rules. In the schema below, `h` identifies the lexical head throughout its projection; parentheses mark optional dependents within this fragment. The subscripts on Mod distinguish pre-head and post-head positions of the same modifier function. The head’s entry and construction restrict every dependent.

```text
Nom_h → (Mod_pre)  Head:N_h  (Comp)  (Mod_post)
NP_h  → (Det)  Head:Nom_h
licensed(NP_h, f, c) ⇔ f ∈ U_h and C_h(f, c)
```

Here `U_h` is the head’s set of use permissions, `f` is the NP’s function, and `C_h` checks the lexical and constructional conditions in context `c`. For Det use, these include compatibility with the target nominal; for an argument headed by a singular count common noun, they include required determination. Optionality in the second rule doesn’t override those conditions.

Each NP’s use permissions follow its own head. In *the apple*, the article’s Det permission licenses the dependent NP headed by *the*. The outer NP takes its argument permission from *apple*, whose requirement for determination is satisfied by the article.

In *some apples*, *some* heads an NP whose Det permission and plural-count target requirement are satisfied. *Apples* heads the outer Nom, which heads the NP. In *Some left*, *some* heads an NP whose argument permission is satisfied. *Every apple* passes the Det and singular-count checks; ordinary independent \**Every left* fails the argument-permission check. *The apple* and \**The left*, with *left* as a verb, differ in the same way.

A singular count common noun such as *book* faces a different restriction. In *a book*, its requirement for determination is satisfied; bare \**Book arrived* leaves that requirement unsatisfied. *Books arrived* has no such requirement. Requiring determination for a common noun doesn’t itself block an article-headed NP from argument use. An article’s exclusion from argument use must still be stated separately.

Partitives and modifiers require further lexical conditions. *Some* and *few* permit a partitive *of*-phrase within their nominal projection. *Almost* can modify *every* in *almost every teacher*; that permission doesn’t license *experienced* as a modifier of *every*. The construction *the lucky few* permits the external determiner and adjectival modifier shown in Figure 5. None of these permissions transfers automatically to every determinative noun.

The separate-D fusion grammar already needs nominal projection for other nouns. It adds DP projection and permits a DP to realize a fused function in nominal structure. The partitive complement and compound restrictor belong to Nom, following the trees in *CGEL* and Payne et al. (2007, 582):

```text
DP_h  → (Mod_pre)  Head:D_h  (Comp)
Nom_h → (Mod_pre)  F:DP_h  (Comp)  (Mod_post)
F ∈ {Det–Head, Mod–Head}
```

The ordinary NP rule embeds this Nom. Det–Head jointly realizes Det of NP and Head of Nom, excluding a second Det; Mod–Head fills an internal modifier’s function and Head of Nom, allowing external determination. Lexical and constructional conditions select the fused function and permitted dependents. These schemata cover independent *few*, *few of them*, *the lucky few* and *hardly anyone present*. The nominal-D fusion variant replaces DP here with `NP_D`, retaining the fused relations.

The strongest separate-D alternative licenses ordinary Head across categories. Keeping the NP and use-permission rules above, it replaces the lexical-head restriction in Nom with:

```text
Nom_h → (Mod_pre)  Head:{N_h, D_h}  (Comp)  (Mod_post)
```

It can use this projection for dependent as well as independent determinatives, eliminating DP from the fragment while retaining primary D. Determiner selection still identifies D-headed NPs and suitable genitives. In *the lucky few*, *few* is D in ordinary Head function; in the compound, its base and construction supply the same modifier restrictions as the D-noun account. Adjectival Mod–Head fusion remains available in both.

Table 7: Taxonomy and headedness varied separately. All four accounts retain the permissions in Table 6, the modifier restrictions and the compound conditions.

| Account | Primary taxonomy | Simple independent determinative |
|:---|:---|:---|
| Separate D, fusion | D outside Noun | NP distribution through Det–Head |
| Separate D, ordinary Head | D outside Noun | D–Nom–NP through cross-category projection |
| Nominal D, fusion | D inside Noun | NP distribution through Det–Head |
| Nominal D, ordinary Head | D inside Noun | N–Nom–NP projection with Head function |

This fourth account shares the D-noun analysis’s ordinary headedness and reduced phrase-type inventory in Det function. Those benefits therefore don’t uniquely favour inclusion within Noun. Neither account removes the selectional alternatives, and dependent determinatives acquire a Nom layer. Their economy concerns reuse of grammatical organization, not uniformly smaller trees or fewer conditions.

The remaining choice is between inheritance through Noun and a projection rule spanning N and D. Why should systematic nominal projection warrant inclusion for pronouns but require cross-category licensing for determinatives? I favour placing the recurring external and structural profile at Noun, with modifier and use restrictions at the subcategories and constructions that distinguish them. This applies the existing membership rationale consistently; it doesn’t claim a new judgment beyond the shared permissions.

Separate D preserves the modifier contrast as a primary-category distinction while licensing nominal projection across that boundary. D-noun makes projection an inherited property and states the modifier contrast within Noun. The preference depends on giving shared nominal organization more weight than primary rank for the modifier boundary. The compound and adjectival comparisons expose the costs of that choice; the present fragment demonstrates the allocation, rather than proving a unique minimum description length.

A grammar with Hudson’s nested classification can use the same permissions and projection rules. Holding those rules fixed, an added pronoun category between Noun and determinative leaves the fragment’s judgments unchanged. Agreement on these judgments leaves the broader pronoun category open; it doesn’t establish equivalence between the full analyses.

## 8.3 Existing restrictions, additional costs and consequences

The comparison starts with the restrictions already present in the grammar. Common nouns, proper nouns and pronouns already differ in determination and permitted modifiers (Table 3). Preserving those conditions is no additional cost of including determinatives. Likewise, the separate-D grammar already restricts adverbial modification and independent use within D. Moving those restrictions inside Noun doesn’t create them.

The adverbial contrast needs a qualified baseline. Payne et al. (2010, 75, n. 3) already analyse *almost* as modifying the noun *textbook* in *an almost textbook case*. Since *textbook* is attributive, this doesn’t erase the contrast with ordinary noun-headed argument expressions. It does exclude an exceptionless Noun-wide ban on internal adverbial premodification.

The proposal extends such premodification to a systematic noun subcategory, including *hardly any* and *almost every*. Its cost is restating the usual modifier contrast at that subcategory boundary, rather than introducing the first nominal exception. In compounds, the inherited premodifier permissions must also be distinguished from the post-head restrictor construction (§4.5). These are explicit qualifications on shared projection.

The proposal trades that primary-category formulation for shared nominal projection and a reduced phrase-type inventory in Det function. It preserves the determinative modifier profile explicitly, as the fragment shows. I favour this division because the nominal constructions recur across the subcategory, while the different dependent inventories remain describable where the lexical distinctions already lie. The auxiliary-as-verb precedent illustrates the same kind of separation between a shared category and specialized syntax; the nominal evidence supplies the justification here.

Cardinals illustrate a consequence of broadening Noun. Reynolds (2026) distinguishes determinative uses such as *ten men*, proper-noun uses such as *Room 101*, and common-noun uses such as *tens of pens*. Under the D-noun analysis, these uses fall within one superordinate category, with their differences retained at the subcategory and construction levels. This recasts the cardinal alternation without eliminating it. The argument doesn’t extend to ordinals, which that study analyses as adjectives, or turn complex numeral phrases into single lexemes.

Complex cardinals also separate category from function. In *two hundred books*, the whole *two hundred* fills Det; internally, *two* modifies the magnitude head *hundred* (Reynolds 2026, sec. 4). In *these two hundred books*, *these* fills Det and *two hundred* is an internal modifier. Including determinatives within Noun preserves these relations. One Det function doesn’t entail a limit of one determinative lexeme per NP.

The shared-Det analysis would lose its claimed economy if determinative-headed and genitive NPs required different projection rules after their independently motivated feature restrictions were held fixed. Such a result would favour retaining the separate phrase types. The present fragment demonstrates a shared analysis; lower overall description length and advantages for learning or processing require further comparison.

# 9 Conclusion

I argue for including determinative within Noun in English. *CGEL* admits pronouns on the basis of their phrase functions despite differences in inflection and dependents. Determinatives show a comparable relation between systematic nominal constructions and a distinctive internal profile. The proposal extends that membership rationale, locating shared nominal organization in the lexical hierarchy and retaining the restrictions of determinatives, including articles.

Ordinary headedness is a further proposal. It unifies bare, partitive and externally determined uses under Head, while fusion captures correspondences with dependent uses and supplies structural modifier domains in compounds. A separate-D grammar can also share nominal projection. The argument for D-noun over that alternative therefore concerns inheritance through an existing category, weighed against the reformulation of modifier restrictions within it.

The corpus documents the constructions; the matrix reanalysis qualifies earlier evidence for a primary boundary. Coordinate subcategories remain the preferred arrangement, with a more provisional status than inclusion within Noun: the fragment’s judgments don’t distinguish them from Hudson’s nesting.

Distributional differences warrant retaining determinative and pronoun as distinct subcategories; they don’t by themselves establish a primary-category boundary or decide between coordinate and nested membership within Noun.

# Data and analysis materials

The accompanying `analysis/` directory contains the feature matrices, provenance records, scripts, generated tables and CGELBank concordance. The corpus inventory records the full source commit and file checksums. Analyses used R 4.6.1 and `energy` 1.7-12; environment details and the seed schedule accompany the outputs.

Acknowledgements. For the September 2026 revision, GPT-6 (Astra), Claude Opus 5, Claude Haiku 4.5 and GLM-5.3-Flash assisted drafting, source retrieval, script development or critical review; GPT-5.6 (Sol) checked numerical outputs. The accompanying materials record the tools and their uses. Responsibility for the analysis is mine.

# A Replication details

## A.1 Corpus inventory

The four gold datasets come from revision `d0a2c2d8c522` of the [CGELBank repository](https://github.com/nert-nlp/cgel). The accompanying data record the full commit identifier and file checksums. Trial material, one-off examples and duplicate versions from the annotation study are excluded. Multiword lexical nodes count once. Overt source errors remain, with the corpus’s correction information retained.

For each D node, extraction follows Head relations upwards to the first non-Head relation, identifying the local function of its projection. The resulting counts are Det (297), Mod (18), Det–Head (65), Marker (1), Flat (4) and Coordinate (2). The concordance records each local phrase, its nearest containing NP and that NP’s function, and the source sentence.

The quantifier attestations in (2) have the sentence identifiers `reviews-083459-0002` (a) and `newsgroup-groups.google.com_INTPunderground_b2c62e87877e4a22_ENG_20050906_165900-0074` (b). Both resolve in the accompanying concordance.

## A.2 Feature matrix and sensitivity checks

The article by Reynolds (2021b) and the LingBuzz description of its matrix report 232 features, but the public file contains 155 (Reynolds 2021a). The reanalysis preserves that file with its checksum and compares it with a recovered local 232-feature working matrix. The working matrix isn’t authenticated as the published input. The public file reproduces the published DISCO decomposition: between-group component 30.58286, within-group component 356.41607 and total 386.99893, giving `F=11.670` to the reported precision.

DISCO and k-groups use Euclidean distances between unscaled binary rows: the square root of the number of feature mismatches. Columns receive equal weight, so correlated diagnostics affect the geometry. DISCO uses *CGEL*’s determinative/pronoun partition. Runs with 999 permutations and seed 20260907 give `p=.001` across the representations in Table 8, the minimum attainable value. The observations are coded word forms; the tests concern separation within this inventory.

Here the permutation results describe comparison with shuffled partitions of these rows. They aren’t population-level inference under a defended exchangeability assumption. Paradigmatic relations and repeated compound material connect word forms; removing word-component columns doesn’t remove those relations among rows. The reported values show how the supplied partition compares with the shuffled partitions under this representation, without treating the forms as independent samples from a linguistic population.

The published k-groups code records a single random start and no seed. After removing the name column, it drops the first feature again during clustering. The reanalysis therefore tests both the public 155-feature input and that 154-feature implementation. For each representation, 100 single-start fits use seeds 1–100 and the published limit of ten iterations. A separate fit uses 100 starts and a limit of 100 iterations, selecting the best objective – the clustering criterion being minimized – among those starts.

Table 8: Exploratory sensitivity of the matrix analysis. The range is agreement out of 138 across 100 single-start fits. The last column is agreement for the best-objective fit among a separate set of 100 starts, not the maximum agreement observed. All displayed DISCO runs give `p=.001` with 999 permutations.

| Representation                 | Features | DISCO `F` |  Range | Best objective |
|:-------------------------------|---------:|----------:|-------:|---------------:|
| Public matrix                  |      155 |    11.670 | 75–132 |        125/138 |
| Without word-component columns |      105 |    12.654 | 75–131 |        131/138 |
| Syntactic columns              |       50 |     9.682 | 69–133 |        120/138 |
| Syntactic, four labels removed |       46 |     7.192 | 69–117 |         97/138 |

Cluster labels are oriented after fitting to maximize agreement with *CGEL*’s classification. Eight public-matrix single-start fits reproduce the published count of 129 matches; the 100-start fit yields 125. The 154-feature implementation also varies across starts. Selecting the best clustering objective doesn’t select the closest match to *CGEL*’s labels. Reducing the feature set can increase agreement in the fit selected by that objective, but the increase doesn’t independently support the taxonomy: the feature representation has changed.

Removing 50 word-component columns changes best-objective agreement to 131/138. The 50 syntactic columns yield 120/138; removing four explicit analysis labels yields 97/138. Those labels concern fused determiner-head function, partitive head function, subject-determiner function and coordination with non-fused determiners. This is a limited sensitivity check: the remaining judgments still reflect the descriptive framework. Complete scripts, feature changes, seed schedules and outputs accompany the paper.

# References

Abney, Steven P. 1987. “The English Noun Phrase in Its Sentential Aspect.” PhD thesis, Massachusetts Institute of Technology.

Anderson, John M. 1997. *A Notional Theory of Syntactic Categories*. Cambridge Studies in Linguistics 82. Cambridge University Press. <https://doi.org/10.1017/CBO9780511519734>.

Bruening, Benjamin. 2020. “The Head of the Nominal Is N, Not D: N-to-D Movement, Hybrid Agreement, and Conventionalized Expressions.” *Glossa: A Journal of General Linguistics* 5 (1). <https://doi.org/10.5334/gjgl.1031>.

Déchaine, Rose-Marie, and Martina Wiltschko. 2002. “Decomposing Pronouns.” *Linguistic Inquiry* 33 (3): 409–42. <https://doi.org/10.1162/002438902760168554>.

Huddleston, Rodney, and Geoffrey K. Pullum. 2002. *The Cambridge Grammar of the English Language*. Cambridge University Press. <https://doi.org/10.1017/9781316423530>.

Huddleston, Rodney, Geoffrey K. Pullum, and Brett Reynolds. 2022. *A Student’s Introduction to English Grammar*. 2nd ed. Cambridge University Press. <https://doi.org/10.1017/9781009085748>.

Hudson, Richard. 2004. “Are Determiners Heads?” *Functions of Language* 11 (1): 7–42. <https://doi.org/10.1075/fol.11.1.03hud>.

Hudson, Richard. 2010. *An Introduction to Word Grammar*. Cambridge University Press.

Lyons, Christopher. 1999. *Definiteness*. Cambridge University Press. <https://doi.org/10.1017/cbo9780511605789>.

Lyons, John. 1968. *Introduction to Theoretical Linguistics*. Cambridge University Press. <https://doi.org/10.1017/CBO9781139165570>.

Palmer, Harold E. 1924. *A Grammar of Spoken English on a Strictly Phonetic Basis*. W. Heffer & Sons Ltd.

Payne, John, Rodney Huddleston, and Geoffrey K. Pullum. 2007. “Fusion of Functions: The Syntax of *Once*, *Twice* and *Thrice*.” *Journal of Linguistics* 43 (3): 565–603. <https://doi.org/10.1017/S002222670700477X>.

Payne, John, Rodney Huddleston, and Geoffrey K. Pullum. 2010. “<span class="nocase">The distribution and category status of adjectives and adverbs</span>.” *Word Structure* 3 (1): 31–81. <https://doi.org/10.3366/E1750124510000486>.

Postal, Paul M. 1966. “On so-Called “Pronouns” in English.” In *Report of the Seventeenth Annual Round Table Meeting on Linguistics and Language Studies*, edited by Francis P. Dinneen. Monograph Series on Languages and Linguistics 19. Georgetown University Press.

Pullum, Geoffrey K., and Philip Miller. 2022. *NPs Versus DPs: Why Chomsky Was Right*. LingBuzz 006845. <https://lingbuzz.net/lingbuzz/006845>.

Pullum, Geoffrey K., and Deirdre Wilson. 1977. “Autonomous Syntax and the Analysis of Auxiliaries.” *Language* 53 (4): 741–88. <https://doi.org/10.2307/412911>.

Reynolds, Brett. 2013. “Determiners, Feline Marsupials, and the Category-Function Distinction: A Critique of ELT Grammars.” *TESL Canada Journal* 30 (2): 1–17. <https://doi.org/10.18806/tesl.v30i2.1138>.

Reynolds, Brett. 2021a. *Full Matrix of English Determinative and Pronoun Features*. LingBuzz 005747. <https://ling.auf.net/lingbuzz/005747>.

Reynolds, Brett. 2021b. “Quantifying the Differences Between Lexical Categories: The Case of Pronouns and Determinatives in English.” *Cadernos de Linguística* 2 (3). <https://doi.org/10.25189/2675-4916.2021.V2.N3.ID399>.

Reynolds, Brett. 2025. “Personhood and Pro-Forms: A Hierarchical Analysis of Gender in Modern English.” Unpublished manuscript.

Reynolds, Brett. 2026. “The Lexicon–Syntax Boundary in English Numerals: Cardinals, Ordinals, and Fractionals.” *English Language and Linguistics*, 1–19. <https://doi.org/10.1017/S1360674325100518>.

Reynolds, Brett, Aryaman Arora, and Nathan Schneider. 2023. “Unified Syntactic Annotation of English in the CGEL Framework.” In *Proceedings of the 17th Linguistic Annotation Workshop (LAW-XVII)*, edited by Jakob Prange and Annemarie Friedrich. Association for Computational Linguistics. <https://doi.org/10.18653/v1/2023.law-1.22>.

Sommerstein, Alan H. 1972. “On the so-Called Definite Article in English.” *Linguistic Inquiry* 3 (2): 197–209. <https://www.jstor.org/stable/4177701>.

Spinillo, Mariangela Galvão. 2004. “Reconceptualising the English Determiner Class.” {PhD} thesis, University College London. <https://discovery.ucl.ac.uk/id/eprint/10101595/>.

Van Eynde, Frank. 2003. “On the Notion ‘Determiner’.” In *Proceedings of the 10th International Conference on Head-Driven Phrase Structure Grammar*, edited by Stefan Müller. CSLI Publications. <https://doi.org/10.21248/hpsg.2003.22>.

