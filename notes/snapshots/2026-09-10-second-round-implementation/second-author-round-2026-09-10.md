# Parsimony and the fourfold proposal
Second author round — 10 September 2026

The fourfold classification should be the stated proposal, with parsimony introduced early as its motivation. The present wording makes coordinate placement sound incidental. Centrality and strength of evidence are separate: we can argue for this arrangement directly while allowing that the fragment's judgments also fit a nested hierarchy.
## Proposed opening claim
> What is the categorial relationship among words such as _some_, _me_, _apple_ and _Brett_? I argue that all four are nouns, and that determinatives form a coordinate subcategory alongside common nouns, proper nouns and pronouns. I call this fourfold proposal the determinative-noun or D-noun analysis.

This puts the point raised in your comment c2 at the beginning. The later standalone sentence calling coordinate placement “a further proposal” can go. The historical paragraph can then explain how this proposal differs from Palmer and Hudson.
## Making inheritance explicit
I agree with the emphasis intended by “It's worth stating explicitly”. The causal relationship can do that work directly:

> Classifying determinatives as nouns gives them the nominal projection rules of Noun. A determinative therefore heads a nominal (Nom), which heads an NP. Nom contains the head and its internal dependents, excluding an external determiner. Lexical restrictions govern which uses are available.

The following paragraph and Figure 1 already show the contrast with CGEL's fused functions.
## Completing the parsimony argument
The defensible {==reductions==}{>>Also significantly reduces overlap in numeratives. It seems to me that other parsimonies are gained, though I haven't looked through the paper for all of them.<<}{id="c1" by="user" at="2026-09-10T14:59:05.629Z"} relative to CGEL fall into three groups:

| Level | Reduction | What remains |
| :--- | :--- | :--- |
| Primary lexical categories | Determinative ceases to be a separate primary category, reducing that inventory by one. | Determinative remains a noun subcategory. This is relocation within the taxonomy, not deletion of every determinative distinction. |
| Phrase structure | DP is replaced by NP, and determinatives use the nominal projection already available to nouns. Their determining phrases share NP status with genitive determiners. | Dependent determinatives acquire a Nom layer. Determiner selection still distinguishes the permitted expressions. |
| Head relations | Ordinary Head covers bare, partitive and externally determined determinatives, replacing their Det–Head/Mod–Head alternation. | Fusion remains for adjectival constructions; lexical and modifier restrictions remain necessary. |

These are connected consequences, rather than independent quantities to add into a numerical score. In particular, fewer primary categories does not by itself establish fewer total stipulations.
### Proposed motivation paragraph
> The motivation is parsimony. First, including determinative within Noun removes a separate primary lexical category {++and its phrasal projection, replacing++}{id="s3" by="user" at="2026-09-10T15:02:20.145Z"}{--.--}{id="s2" by="user" at="2026-09-10T15:02:18.227Z"} {--Second, it replaces--}{id="s1" by="user" at="2026-09-10T15:02:16.638Z"} DP with NP {--and reuses nominal projection--}{id="s4" by="user" at="2026-09-10T15:02:46.144Z"}. Third, it gives independent determinatives ordinary Head structure {++in the NP++}{id="s5" by="user" at="2026-09-10T15:03:01.324Z"}, unifying the bare, partitive and externally determined uses that CGEL divides between Det–Head and Mod–Head fusion. Section 7 compares these reductions with the changes required in stating modifier and use restrictions.

This gives the paper an explicit economy argument without making its introduction a catalogue of qualifications. The strongest separate-D grammar with ordinary projection remains in §7 because it can obtain the structural reductions too.
## Giving coordination an argument in §5
Parsimony relative to CGEL doesn't automatically favour coordination over Hudson's nesting. Nesting can broaden the existing pronoun node rather than add a new node to the taxonomy. We should not claim a smaller total category inventory than Hudson's on that basis.

The positive argument is about where the generalizations belong. The shared projection applies at Noun; the comparisons in §5 do not establish a further syntactic generalization requiring determinative inside pronoun. That supports the coordinate proposal, with a clear condition under which nesting would improve it.
### Proposed closing paragraph for §5
> I place determinative alongside pronoun because the shared projection can be stated at Noun, while the contrasts in {++, grade++}{id="s6" by="user" at="2026-09-10T15:05:09.491Z"}{>>not sure what all to include here. This is a low-confidence edit.<<}{id="c2" by="user" at="2026-09-10T15:08:20.765Z"}{++, gender, deixis++}{id="s6" by="user" at="2026-09-10T15:05:09.491Z"}{==, modification==}{>>not sure what all to include here. This is a low-confidence edit.<<}{id="c2" by="user" at="2026-09-10T15:08:20.765Z"} and determination are described within the two subcategories. The broader pronoun category does not capture an additional syntactic generalization in these comparisons. Further syntactic generalizations over the broader pronoun category could favour nesting. Section 6 turns to the membership of the articles and other restricted forms.

The abstract and conclusion should accordingly state the fourfold proposal without “provisionally” or “organizational preference”. The limits of the matched fragment remain where they are demonstrated in §§5 and 7. The phrase “an added pronoun category” in §7.2 should describe the extra level on determinative's inheritance path, avoiding a claim that nesting increases the total number of category nodes.
## The claim about fusion's adoption
I recommend omitting {==“at best niche, selective, and contested, with low theoretical adoption”==}{>>This strikes me as broadly true, and I think Geoff would agree. It just hasn't received any uptake oustide of CGEL authors and me.<<}{id="c4" by="user" at="2026-09-10T15:11:23.047Z"} from the introduction. The supplied report distinguishes adoption of a constructional label from adoption of the representation, which is useful. But its ratings are judgments from a search, not measured adoption rates, and absence from UD is not a test of grammatical adequacy.

The report also omits {==CGELBank==}{>>correctly, I would say<<}{id="c3" by="user" at="2026-09-10T15:10:51.821Z"} while asserting that fusion has not crossed an infrastructural threshold. CGELBank explicitly implements dual functions, describes the corresponding graph edges, and supplies annotations. That is a material omission, even though CGELBank belongs to the CGEL tradition rather than demonstrating broad independent adoption. See [Reynolds, Arora and Schneider (2023), pp. 222–223](https://aclanthology.org/2023.law-1.22.pdf).

The report's more cautious distinction about the NLP literature is supported: [Elazar and Goldberg (2019)](https://aclanthology.org/Q19-1030/) formulate their task around recovering implicit nominal information. That isn't automatically endorsement of CGEL's full syntactic representation. Neither point establishes a field-wide adoption rate.

The paper can make the stronger relevant claim directly: ordinary noun projection supplies the determinative structures without requiring those applications of fused functions. The comparative argument should establish its economy.
## DP wording
Your compact disambiguation works. I would replace the literal “[see below]” with a section reference:

> Here DP abbreviates determinative phrase, as in CGEL, not to be confused with the DP of the DP hypothesis, where D heads the whole expression _some apples_ (Abney 1987; §2.1). The D-noun analysis keeps _apples_ as that expression's ultimate head.

These proposals affect the opening, the framing of §5, and the matching abstract and conclusion statements. The source and earlier annotations are preserved for this review.
