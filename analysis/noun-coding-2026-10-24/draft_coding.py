#!/usr/bin/env python3
"""Draft coding of a reference set of nouns and adjectives, plus ten features
from CGEL's own lists, for the ledger's noun-reference-set row (24 Oct 2026).

Everything here is a PROPOSAL by Claude Opus 5.5 for Brett to accept or correct.
Coding follows Reynolds (2021): y = "may exhibit the feature", n = "never does";
m = marginal; blank = not coded (sense unclear, or a judgment left to Brett).

Two parts:
1. Fifteen new rows on the matrix's 105 syntactic and semantic columns and on
   the ten added columns: twelve lexemes and three category-level rows. A
   category row records whether ANY member of the category may show the
   feature, in its primary use; the lexemes are a reference set, not a sample
   (Reynolds 2021: comparing with open categories needs "a defensible sampling
   procedure"), so absence claims for a category rest on the category rows.
2. The ten added columns for the 139 existing pronoun and determinative forms.

Why the added columns: the 105 features were chosen in 2021 to compare pronouns
with determinatives, so nouns score n on many by construction, which would
favour nesting artificially (side agent's note, relayed by Brett, 24 Oct). The
added features come from CGEL's lists of the defining properties of nouns
(ch. 5 §1, [2] and [6], pp. 326-327) and the criterial properties of
adjectives (ch. 6 §2, [1], p. 527).

Conventions: primary uses only. The secondary set-denoting use (the real me,
the Kim I knew) is excluded, or every pronoun and name would take determiners
and adjectives. Form-level case features are coded for the plain form.

Run: python3 analysis/noun-coding-2026-10-24/draft_coding.py
"""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
MATRIX = ROOT / "analysis" / "matrix-2026-10" / "matrix-2026-10.csv"
NEWVALS = ROOT / "analysis" / "matrix-2026-10" / "new_feature_values.csv"

ROWS = {
    "lot": "quantificational lot in a lot (of); CGEL pp. 349-350",
    "number": "quantificational number in a number of; CGEL p. 350",
    "plenty": "quantificational plenty; CGEL p. 350",
    "dozen": "dozen, dozens of; CGEL p. 349 [53iii]",
    "majority": "majority in the majority (of)",
    "dog": "count common noun",
    "water": "non-count common noun",
    "Kim": "proper noun, primary naming use (a personal name)",
    "Toronto": "proper noun, primary naming use (a place name)",
    "numerous": "quantity adjective; CGEL pp. 539-540",
    "rich": "adjective with a fused-head use (the rich); CGEL pp. 417-418",
    "tall": "ordinary gradable adjective",
    "CN": "CATEGORY: any common noun may",
    "PN": "CATEGORY: any proper noun may, in its primary naming use",
    "ADJ": "CATEGORY: any adjective may",
}
R = list(ROWS)

# feature: (default, {row: value}, note). "" = not coded.
E = {
 "genitive_case": ("n", {}, "Form-level: the plain form isn't genitive (dog's is a different form)."),
 "accusative_case": ("n", {}, "Form-level."),
 "nominative_case": ("n", {}, "Form-level."),
 "in_word_formation_e_g_a_many_sided_shape": ("y", {"lot": "n", "plenty": "n", "dozen": "n", "Kim": "m", "numerous": "n"},
     "Element of a compound or derived word (number-crunching, dog-eared, Toronto-based, tall-masted)."),
 "has_derivationtionally_related_words": ("y", {"lot": "n", "dozen": "m", "Kim": "n"},
     "numerous/number, plentiful, majoritarian, Torontonian, richness, tallness."),
 "has_corresponding_word": ("n", {"number": "y", "plenty": "y", "dog": "y", "water": "y", "tall": "y", "CN": "y", "ADJ": "y"},
     "Sense inferred from the coded forms (little/less, no, that, we): a homonym in another category. number (verb), plenty (adverb: plenty big), dog and water (verbs), tall (adverb: walk tall)."),
 "compound_word": ("n", {"CN": "y", "PN": "y", "ADJ": "y"}, "None of the twelve lexemes is a compound; each category has compounds."),
 "inflects_for_case": ("n", {"majority": "y", "dog": "y", "water": "y", "Kim": "y", "Toronto": "y", "rich": "m", "CN": "y", "PN": "y", "ADJ": "m"},
     "Genitive inflection (CGEL ch. 5 §1 [3]). rich and ADJ marginal: the poor's is attested in edited prose (corpus/genitive/2026-10-16-brett-supplied-anaphoric-fused-genitives.md)."),
 "paradigm_has_distinct_acc_form": ("n", {}, ""),
 "paradigm_has_genitive_form": ("n", {"majority": "y", "dog": "y", "water": "y", "Kim": "y", "Toronto": "y", "CN": "y", "PN": "y"},
     "CGEL ch. 5 §1 [3] gives dog's as a form of dog. CHECK: the matrix codes the compounds n here though inflects_for_case is y for them; nouns and compounds should be coded alike."),
 "paradigm_has_distinct_independent_genitive_form": ("n", {}, ""),
 "paradigm_has_distinct_self_form": ("n", {}, ""),
 "paradigm_has_comparative_and_superlative_forms": ("n", {"rich": "y", "tall": "y", "ADJ": "y"}, "Inflectional only; numerous has analytic forms (added column has_analytic_comparative)."),
 "paradigm_has_distinct_plural_form": ("n", {"lot": "m", "number": "y", "dozen": "y", "majority": "y", "dog": "y", "water": "y", "CN": "y", "PN": "m"},
     "lot: CGEL lists lots separately ([57ii]); PN: plural only in restricted uses (CGEL p. 521) and plural-only names; Kim n in the primary use."),
 "does_not_inflect": ("n", {"plenty": "y", "numerous": "y", "CN": "m", "ADJ": "y"}, ""),
 "Monmorphemic": ("y", {"majority": "n", "numerous": "n"}, ""),
 "Must_be_stressed_as_object_after_particle": ("n", {}, "Nouns follow a particle unstressed: pick up the dog, pick up Kim."),
 "Start_with_th": ("n", {}, ""),
 "Start_with_hw": ("n", {}, ""),
 "anaphoric_marker": ("n", {"lot": "y", "number": "m", "plenty": "y", "dozen": "y", "majority": "y", "numerous": "y", "rich": "m", "tall": "m", "CN": "y", "ADJ": "y"},
     "Can be used with its restriction understood from context: A lot were arrested (CGEL p. 349 [56]); there's plenty in the fridge; numerous were injured; adjectives as anaphoric fused heads (CGEL p. 417)."),
 "deictic_marker": ("n", {}, ""),
 "person_deixis": ("n", {}, ""),
 "pro_form": ("n", {"CN": "y"}, "CN: pronominal one is a common noun (CGEL p. 429) and a pro-form."),
 "personal_gender_as_head_or_fused_head": ("n", {"majority": "m", "Kim": "y", "rich": "y", "CN": "y", "PN": "y", "ADJ": "y"},
     "FOR BRETT: coded on CGEL's terms (the head selects who/he/she: the doctor who, Kim... she). On Reynolds (2025), descriptions and names shape referent construal while pronouns and determinatives carry the contrast lexically; on that view nouns would be n here, and this feature becomes a candidate property of pronouns and determinatives alone."),
 "non_personal_gender": ("n", {"plenty": "m", "majority": "m", "dog": "y", "water": "y", "Toronto": "y", "CN": "y", "PN": "y", "ADJ": "y"}, "Same caveat as personal gender."),
 "epicene_personal_gender": ("n", {"majority": "m", "Kim": "y", "rich": "y", "CN": "y", "PN": "y", "ADJ": "y"}, "Same caveat."),
 "masculine_gender": ("n", {"CN": "y", "PN": "y"}, "man, John. Same caveat."),
 "feminine_gender": ("n", {"CN": "y", "PN": "y"}, "woman, Mary. Same caveat."),
 "definite": ("n", {"Kim": "y", "Toronto": "y", "PN": "y"}, "Proper names in their primary use are definite; common nouns get definiteness from a determiner."),
 "indefinite": ("n", {"plenty": "y", "CN": "y"}, "plenty heads indefinite NPs with no determiner."),
 "existential": ("y", {"tall": "m"}, "Sense inferred from the coded forms (n only for wh-forms, generic one, dummy there, zero): can carry existential import. Low confidence."),
 "universal": ("n", {}, ""),
 "free_choice": ("n", {}, ""),
 "negative": ("n", {}, ""),
 "interrogative": ("n", {}, ""),
 "non_affirmative": ("n", {"CN": "m"}, "CN: idioms such as a red cent."),
 "reflexive": ("n", {}, ""),
 "reciprocal": ("n", {}, ""),
 "dual": ("n", {"CN": "y"}, "CN: couple, pair."),
 "paucal": ("n", {"CN": "y"}, "CN: couple, handful."),
 "multal": ("n", {"lot": "y", "plenty": "y", "numerous": "y", "CN": "y", "ADJ": "y"}, ""),
 "proportional": ("", {}, "Not coded: the coded forms (y for a, that, these, some, cardinals; n for all, each, the) don't show the sense."),
 "semantically_countable": ("y", {"tall": "", "ADJ": "", "water": "n"}, ""),
 "semantically_uncountable": ("n", {"tall": "", "ADJ": "", "lot": "y", "plenty": "y", "majority": "y", "water": "y", "CN": "y"}, "tall and ADJ blank here and in the three columns below: number and countability are about what a noun phrase denotes, so for adjectives they depend on the noun."),
 "semantically_singular": ("y", {"tall": "", "ADJ": "", "number": "n", "dozen": "n", "numerous": "n", "rich": "n"}, "number permits only plural obliques (CGEL p. 350); the rich is plural."),
 "semantically_plural": ("y", {"tall": "", "ADJ": "", "water": "m", "Kim": "n", "Toronto": "n", "PN": "m"}, ""),
 "distributive": ("", {}, "Not coded: the sense isn't recoverable from the coded forms (his and mine are y)."),
 "joint": ("", {}, "Not coded, as distributive."),
 "cardinal": ("n", {"dozen": "y", "CN": "y"}, "FOR BRETT: dozen as a numeral-like noun."),
 "disjunctive": ("n", {}, ""),
 "degree": ("n", {"numerous": "y", "rich": "y", "tall": "y", "ADJ": "y"}, "Gradable meaning; in the matrix only the four gradable determinatives."),
 "sufficiency": ("n", {"ADJ": "y"}, "ADJ: adequate."),
 "temporal": ("n", {"CN": "y", "PN": "m"}, "CN: day, hour. PN: days of the week, if proper nouns."),
 "locative": ("n", {"Toronto": "m", "CN": "m", "PN": "m"}, "Sense from anywhere, somewhere: locative meaning. Low confidence."),
 "dummy": ("n", {}, ""),
 "can_be_followed_by_adjective_such": ("n", {}, "some such, no such: not with nouns."),
 "can_be_modified_by_almost": ("n", {"dozen": "y", "majority": "y", "dog": "m", "rich": "y", "tall": "y", "CN": "y", "ADJ": "y"},
     "Coded at NP level, as the matrix does for pronouns (almost his entire life): almost a dozen, almost a majority."),
 "can_be_modified_by_approximately": ("n", {"dozen": "y", "CN": "y"}, "approximately a dozen."),
 "can_be_modified_by_at_least": ("y", {"lot": "m", "number": "m", "numerous": "n"}, "NP level: at least a dog, at least Kim."),
 "can_be_modified_by_hardly": ("n", {"lot": "m", "plenty": "m", "dozen": "y", "majority": "y", "dog": "m", "numerous": "y", "rich": "y", "tall": "y", "CN": "y", "ADJ": "y"}, "hardly a dozen, hardly a majority."),
 "can_be_modified_by_not": ("n", {"lot": "y", "dozen": "m", "majority": "m", "dog": "m", "numerous": "y", "rich": "y", "tall": "y", "CN": "y", "ADJ": "y"}, "not a lot; not numerous."),
 "can_be_modified_by_adverb_very": ("n", {"numerous": "y", "rich": "y", "tall": "y", "ADJ": "y"}, ""),
 "Coordinates_with_independent_genitives": ("n", {"dog": "y", "water": "m", "CN": "y", "PN": "m"}, "FOR BRETT: the sense (this and mine) is unclear for nouns; coded via the NP (the dog and mine)."),
 "Coordinates_with_dependent_genitives": ("n", {}, "Plain forms."),
 "Coordinates_with_NPs": ("y", {"numerous": "n", "tall": "m"}, "rich via its fused-head NP (the rich and the poor)."),
 "intensifying_reduplication": ("n", {"lot": "m", "dozen": "m", "CN": "y", "ADJ": "y"}, "lots and lots, dozens and dozens, miles and miles; ADJ through comparatives (taller and taller)."),
 "selects_singular_heads": ("n", {}, "Determiner selection; nouns aren't determiners."),
 "selects_count_singular_heads": ("n", {}, ""),
 "selects_non_count_heads": ("n", {}, ""),
 "selects_plural_heads": ("n", {"dozen": "m"}, "FOR BRETT: a dozen eggs, if dozen is numeral-like there."),
 "compatible_count_sing_NP": ("n", {"lot": "y", "majority": "y", "CN": "y", "ADJ": "m"},
     "FOR BRETT: for nouns coded through the of-complement (a lot of the cake), not as a determiner; ADJ through superlatives (the best of the cake)."),
 "compatible_count_plur_NP": ("n", {"lot": "y", "number": "y", "plenty": "y", "dozen": "y", "majority": "y", "CN": "y", "ADJ": "m"}, "As above."),
 "compatible_non_count_NP": ("n", {"lot": "y", "plenty": "y", "majority": "y", "CN": "y", "ADJ": "m"}, "As above."),
 "Forms_universal_pronouns_before_all": ("n", {}, ""),
 "functions_as_a_predeterminer_modifier": ("n", {"CN": "y", "ADJ": "m"}, "CN: half (CGEL p. 434). ADJ: double the cost, CGEL's category for double unchecked."),
 "functions_as_prehead_modifier_in_nominal": ("y", {"lot": "n", "number": "n", "plenty": "n"},
     "dog houses, water bottle, majority rule, the dozen roses, the Clinton years, Toronto streets; the quantificational senses don't modify. CHECK: the difference between this column and functions_as_attrib_modifier_in_nominal isn't recoverable; coded alike."),
 "functions_as_degree_modifier_in_AdjP": ("n", {"lot": "y", "plenty": "y", "CN": "y", "ADJ": "m"}, "a lot bigger; plenty big enough (CGEL p. 550); three inches long (CGEL p. 327 [6iv])."),
 "functions_as_predicative_complement": ("y", {"number": "m"}, "Three eggs is plenty (CGEL p. 349)."),
 "functions_as_predicative_complement_to_seem": ("n", {"lot": "y", "plenty": "m", "dog": "y", "numerous": "y", "rich": "y", "tall": "y", "CN": "y", "ADJ": "y"}, "seems a lot to ask; seemed a nice dog."),
 "functions_as_marker_of_coordination": ("n", {}, ""),
 "functions_as_fused_determiner_head": ("n", {}, "CGEL's analysis label; not a property of form."),
 "functions_as_head_of_partitive_construction": ("n", {"lot": "y", "number": "y", "plenty": "m", "dozen": "y", "majority": "y", "CN": "y", "ADJ": "y"},
     "a lot of the delegates (CGEL p. 349 [54i]); a number of the protesters (p. 350); ADJ: the most important of her criticisms (pp. 332-333)."),
 "functions_as_adjunct_in_clause_structure": ("n", {"lot": "y", "CN": "y", "ADJ": "m"}, "I travel a lot; the day before yesterday (CGEL p. 327 [6iii]); ADJ as predicative adjunct."),
 "functions_as_attrib_modifier_in_nominal": ("y", {"lot": "n", "number": "n", "plenty": "n"}, "Coded as functions_as_prehead_modifier_in_nominal."),
 "appears_in_subject": ("y", {"tall": "m"}, ""),
 "appears_in_object": ("y", {"tall": "m"}, ""),
 "functions_as_post_head_modifier_of_it_or_them": ("n", {}, ""),
 "functions_as_post_head_modifier_of_N": ("n", {"Kim": "y", "Toronto": "m", "rich": "y", "tall": "y", "CN": "m", "PN": "y", "ADJ": "y"},
     "my friend Kim; the opera 'Carmen' (CGEL p. 327 [6vii]); someone rich, someone tall (postpositive, CGEL p. 527)."),
 "appears_in_existentials_there_s_on_the_table": ("n", {"lot": "y", "number": "y", "plenty": "y", "dozen": "y", "majority": "y", "dog": "y", "water": "y", "CN": "y"},
     "In the displaced subject of an existential; names and pronouns are excluded on the ordinary reading."),
 "functions_as_determiner_in_day_s_time_ago": ("n", {"dozen": "m"}, ""),
 "functions_as_subject_of_present_participal_of_joining_you": ("y", {"plenty": "m", "numerous": "n", "tall": "n"}, "Kim joining us; the rich getting richer."),
 "Functions_as_subject_of_interrogative_tag": ("n", {}, "Tag subjects are pronouns."),
 "functions_as_subject_determiner": ("n", {}, "Plain forms."),
 "functions_in_vocative": ("n", {"dog": "m", "Kim": "y", "tall": "m", "CN": "y", "PN": "y", "ADJ": "y"}, "Waiter!; Kim, ...; Hey, gorgeous!"),
 "May_coordinate_with_non_fused_determiners": ("n", {}, ""),
 "must_be_outranked_by_a_coindexed_element": ("n", {}, ""),
 "takes_predeterminer_modifiers_all_or_both": ("n", {"Toronto": "y", "PN": "y"}, "all Toronto turned out. FOR BRETT: CGEL's analysis of all here unchecked."),
 "occurs_after_predeterminer_modifiers_fractions": ("n", {"dozen": "y", "water": "y", "dog": "m", "Toronto": "y", "CN": "y", "PN": "y"}, "half dozen; half water, half milk; half Toronto."),
 "occurs_after_predeterminer_modifiers_multipliers": ("n", {}, ""),
 "ironic_use_of_repetition": ("n", {}, ""),
 "take_poor_lucky_silly_as_attrib_modifiers": ("n", {"dog": "y", "Kim": "y", "Toronto": "m", "CN": "y", "PN": "y"}, "Poor dog!; poor Kim (CGEL p. 520)."),
 "takes_adverb_quite_as_a_modifier": ("n", {"lot": "y", "number": "y", "dozen": "m", "majority": "m", "dog": "y", "numerous": "y", "rich": "y", "tall": "y", "CN": "y", "ADJ": "y"}, "quite a lot; quite a number of; quite a dog; quite tall."),
 "takes_else_or_more_as_a_post_head_dependent": ("n", {"lot": "y", "plenty": "y", "dozen": "y", "CN": "y"}, "a lot more, plenty more, a dozen more: the more half of this conflated feature."),
 "accepts_genitive_apstrophe_s": ("n", {"majority": "y", "dog": "y", "water": "y", "Kim": "y", "Toronto": "y", "dozen": "m", "rich": "m", "CN": "y", "PN": "y", "ADJ": "m"}, "As inflects_for_case."),
 "takes_post_head_modifier_the_hell": ("n", {}, ""),
}

# The ten added columns: id, definition, source.
NEW = [
 ("heads_nominal_after_separate_determiner", "Reused from matrix-2026-10 (its definition in new_features.csv): in its primary use the form heads a nominal with a separate determiner before it (the few, the two, a dog, the rich). This is CGEL's first noun-typical dependent, 'certain determinatives' (ch. 5 §1 [2iii]). For the 139 forms, values are copied from new_feature_values.csv, NA read as n.", "CGEL ch. 5 §1 [2iii]"),
 ("takes_prehead_AdjP_modifier", "In its primary use, a restrictive pre-head AdjP modifies the nominal the form heads (good news, the lucky few, a huge lot of time). Non-restrictive adjectives (poor me, young Isaac Newton) are excluded; the exclamative lucky/poor/silly type has its own column (take_poor_lucky_silly_as_attrib_modifiers).", "CGEL ch. 5 §1 [2iii]; ch. 6 §2 (adjectives aren't modified by adjectives)"),
 ("takes_relative_clause_modifier", "An integrated relative clause modifies the nominal the form heads (people who work, those who came, we who have read the report). Delayed relatives (Who do you know who...) don't count.", "CGEL ch. 5 §1 [2iii]; p. 430 for pronouns"),
 ("takes_nonpartitive_complement", "The form takes a complement other than a partitive of-phrase: an of-PP (a lot of people, a number of boys), another PP or clause (the fact that, proud of), or a than-phrase (more than ten).", "Added by Claude, not on CGEL's lists: motivated by the quantity nouns' of-complements (CGEL pp. 349-350) and adjectives' complements (proud of)"),
 ("NP_functions_as_complement_in_PP", "An NP headed by the form is the complement of a preposition (to the doctor, for some, to him). Dependent-only forms and nominative pronouns are n.", "CGEL ch. 5 §1 [6i]"),
 ("NP_functions_as_modifier_in_AdvP", "An NP headed by the form modifies an AdvP (a whole day late, much later, that quickly, the sooner).", "CGEL ch. 5 §1 [6v]"),
 ("NP_functions_as_modifier_in_PP", "An NP headed by the form modifies a PP (a mile under the sea, much before noon, all over the floor).", "CGEL ch. 5 §1 [6vi]"),
 ("takes_post_head_AdjP", "A post-head AdjP modifies the nominal the form heads (someone nice, the people present, those present, all present).", "CGEL ch. 6 §2 [1i] (postpositive function)"),
 ("has_analytic_comparative", "Graded by analytic more and most (more useful, more numerous).", "CGEL ch. 6 §2 [1ii]"),
 ("takes_ly_adverb_modifier", "Modified by a degree or evaluative -ly adverb (remarkably happy, surprisingly few, considerably more); the approximators (almost, nearly, hardly, approximately) have their own columns and are excluded.", "CGEL ch. 6 §2 [1iii]; p. 538 (the modifier test: nouns 'are modified by adjectives, not adverbs')"),
]

# Values of the added columns for the fifteen new rows.
NEW_ROWS = {
 "takes_prehead_AdjP_modifier": ("n", {"lot": "y", "number": "y", "dozen": "y", "majority": "y", "dog": "y", "water": "y", "rich": "m", "CN": "y", "ADJ": "m"},
     "a whole/huge lot (CGEL p. 350); huge numbers (p. 350 [58]); plenty takes none (p. 350); the vast majority; the idle rich. Names n: in the primary use they take only non-restrictive adjectives (young Isaac Newton, CGEL pp. 520-521), a wider range than the pronouns' lucky/poor/silly, which the separate column records."),
 "takes_relative_clause_modifier": ("n", {"lot": "y", "number": "m", "plenty": "y", "dozen": "y", "majority": "y", "dog": "y", "water": "y", "rich": "y", "CN": "y", "ADJ": "y"},
     "there's a lot that I don't understand; the rich who live here; names take integrated relatives only in secondary uses."),
 "takes_nonpartitive_complement": ("n", {"lot": "y", "number": "y", "plenty": "y", "dozen": "y", "majority": "y", "rich": "y", "CN": "y", "ADJ": "y"},
     "a lot of people (CGEL p. 349 [54ii]); dozens of errors (p. 349 [53iii]); plenty of butter (p. 350); rich in minerals."),
 "NP_functions_as_complement_in_PP": ("y", {"numerous": "n", "tall": "m"}, "for the rich."),
 "NP_functions_as_modifier_in_AdvP": ("n", {"lot": "y", "plenty": "m", "CN": "y", "ADJ": "m"}, "a lot later; a whole day late."),
 "NP_functions_as_modifier_in_PP": ("n", {"lot": "m", "CN": "y"}, "a mile under the sea."),
 "takes_post_head_AdjP": ("n", {"plenty": "m", "majority": "m", "dog": "y", "water": "y", "CN": "y"}, "a dog bigger than mine; water fit to drink."),
 "has_analytic_comparative": ("n", {"numerous": "y", "rich": "m", "tall": "m", "ADJ": "y"}, ""),
 "takes_ly_adverb_modifier": ("n", {"numerous": "y", "rich": "y", "tall": "y", "ADJ": "y"}, "remarkably numerous; nouns take adjectives, not adverbs."),
}
NEW_ROWS_DET = ("n", {"lot": "y", "number": "y", "dozen": "y", "majority": "y", "dog": "y", "water": "y", "rich": "y", "tall": "m", "CN": "y", "PN": "m", "ADJ": "y"},
    "a lot, a number (CGEL p. 350: obligatory determiner); plenty takes none (p. 350); names in the primary use take none, except names that include the (the Hague); the rich; the tall only in contrasts (CGEL p. 417).")

# Values of the added columns (except the reused first) for the 139 existing forms.
DEP_ONLY = {"a", "a_certain", "every", "many_a", "no", "the", "us_det", "we_det", "you_det", "what_det",
            "which_rel_det", "whatever_det", "whichever_rel_det", "her_dep", "my", "our",
            "their_sing", "their_plur", "your_sing", "your_plur", "whose_rel", "whoever_s", "whosoever_s",
            "one_s", "its", "somewhat", "last", "next", "zero_det", "various_det", "certain", "such"}
COMPOUNDS = {"anybody", "anyone", "anything", "anywhere", "everybody", "everyone", "everything", "everywhere",
             "nobody", "no_one", "nothing", "nowhere", "somebody", "someone", "something", "somewhere"}
EXISTING = {
 "takes_prehead_AdjP_modifier": ("n", {"few": "y", "a_few": "y", "one_det": "y", "two_det": "y", "three_det": "y", "many": "m", "little": "m"},
     "the lucky few (corpus/premodification/2026-10-16-brett-supplied-adj-few.md); a lucky few; the remaining three; pronouns 'do not normally allow internal pre-head dependents' (CGEL p. 430)."),
 "takes_relative_clause_modifier": ("n", {**{c: "y" for c in COMPOUNDS},
     "a_few": "y", "a_great_many": "y", "a_little": "y", "all": "y", "any": "y", "few": "y", "little": "y", "least": "y",
     "many": "y", "more": "y", "most": "y", "much": "y", "none": "y", "two_det": "y", "three_det": "y", "several": "y",
     "some": "y", "that": "y", "those": "y", "another": "m", "both": "m", "each": "m", "enough": "m", "fewer": "m",
     "fewest": "m", "less": "m", "one_det": "m", "these": "m",
     "he": "y", "she": "y", "I": "y", "we_pron": "y", "you_pron_sing": "y", "you_pron_plur": "y", "they_plur": "m",
     "him": "m", "her_acc": "m", "me": "m", "us_pron": "m", "them_plur": "m", "one_pron": "m"},
     "few who come ever leave, those who came, that which remains, something that you need to know (combined manuscript §2.4); I/We who have read the report, He who controls, you who worked (CGEL p. 430: personal pronouns with human denotation)."),
 "takes_nonpartitive_complement": ("n", {"fewer": "y", "less": "y", "more": "y", "enough": "m", "sufficient": "m"},
     "than-phrases (more than ten); enough/sufficient with an infinitival (enough to go round)."),
 "NP_functions_as_complement_in_PP": ("y", {**{d: "n" for d in DEP_ONLY},
     "he": "n", "she": "n", "I": "n", "they_sing": "n", "they_plur": "n", "we_pron": "n", "who_int": "m", "who_rel": "m",
     "it_dum": "n", "there": "n", "whose_int": "y", "whosever": "m", "twice": "n", "thrice": "n", "fewest": "m", "sufficient": "m"},
     "Dependent-only forms and nominative pronouns n; whose_int y (whose is that?)."),
 "NP_functions_as_modifier_in_AdvP": ("n", {"much": "y", "a_little": "y", "little": "m", "any": "y", "no": "y", "all": "m", "enough": "y",
     "that": "y", "this": "y", "the": "y", "more": "y", "less": "y", "most": "m", "least": "m", "somewhat": "y"},
     "much later, any sooner, no later, quickly enough, that quickly, the sooner."),
 "NP_functions_as_modifier_in_PP": ("n", {"much": "y", "a_little": "y", "little": "m", "all": "y", "somewhat": "y"}, "much before noon; all over the floor; somewhat before."),
 "takes_post_head_AdjP": ("n", {**{c: "y" for c in COMPOUNDS}, "all": "y", "much": "y", "little": "y", "those": "y",
     "few": "m", "none": "m", "any": "m", "enough": "m", "several": "m", "many": "m"},
     "someone nice; all present; those present; Brett (19 Oct): all, much, and little take plain restrictors, few, some, and none take only comparatives (corpus/exclusion_tests/2026-10-19-brett-supplied-none-comparative.md)."),
 "has_analytic_comparative": ("n", {}, ""),
 "takes_ly_adverb_modifier": ("n", {"few": "y", "many": "y", "much": "y", "little": "y", "fewer": "y", "more": "y", "less": "y", "most": "m", "least": "m"},
     "remarkably few, surprisingly many, relatively little, considerably more."),
}


def val(spec, row):
    default, over, _ = spec
    v = over.get(row, default)
    return "marginal" if v == "m" else v


def main():
    m = list(csv.reader(MATRIX.open()))
    header, forms = m[0], m[1:]
    feats = header[header.index("genitive_case"):]
    missing = [f for f in feats if f not in E]
    assert not missing, missing
    newids = [n for n, _, _ in NEW]
    names = {f[0] for f in forms}
    unknown = sorted({k for spec in EXISTING.values() for k in spec[1] if k not in names})
    unknown_rows = sorted({k for spec in list(E.values()) + list(NEW_ROWS.values()) + [NEW_ROWS_DET]
                           for k in spec[1] if k not in ROWS})
    assert not unknown_rows, unknown_rows
    if unknown:
        print("override names not in the matrix (ignored):", ", ".join(unknown))

    det_reused = {}
    for r in csv.DictReader(NEWVALS.open()):
        if r["feature_id"] == "heads_nominal_after_separate_determiner":
            v = r["proposed_value"]
            det_reused[r["form"]] = "n" if v == "NA" else v
    det_reused.setdefault("whomever", "n")

    with (HERE / "proposed-new-rows.csv").open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["names"] + feats + newids)
        for row in R:
            vals = [val(E[f], row) for f in feats]
            vals.append(val(NEW_ROWS_DET, row))
            vals += [val(NEW_ROWS[n], row) for n in newids[1:]]
            w.writerow([row] + vals)

    with (HERE / "proposed-new-columns.csv").open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["names"] + newids)
        for f in forms:
            name = f[0]
            vals = [det_reused.get(name, "")]
            vals += [val(EXISTING[n], name) for n in newids[1:]]
            w.writerow([name] + vals)

    with (HERE / "feature-notes.csv").open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["feature", "part", "note"])
        for f in feats:
            w.writerow([f, "new rows", E[f][2]])
        w.writerow(["heads_nominal_after_separate_determiner", "new rows", NEW_ROWS_DET[2]])
        for n in newids[1:]:
            w.writerow([n, "new rows", NEW_ROWS[n][2]])
            w.writerow([n, "existing forms", EXISTING[n][2]])

    with (HERE / "features-added.csv").open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["feature", "definition", "source"])
        w.writerows(NEW)

    blanks = sum(1 for f in feats for row in R if val(E[f], row) == "")
    flagged = [f for f in feats if "FOR BRETT" in E[f][2] or "CHECK" in E[f][2]]
    print(f"{len(R)} new rows x {len(feats) + len(newids)} columns; {len(forms)} forms x {len(newids)} added columns")
    print(f"blank cells in new rows: {blanks}; features flagged for Brett: {len(flagged)}")
    print("flagged:", ", ".join(flagged))


if __name__ == "__main__":
    main()
