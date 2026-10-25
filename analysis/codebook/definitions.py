#!/usr/bin/env python3
"""Plain-language definitions, with anchor examples, for every matrix column,
for blind coders and for Brett's approval of the codebook (24 Oct 2026).

Senses of the 2021 columns are inferred from the forms Brett coded y in the
2021 matrix (listed in analysis/codebook/feature-senses.txt); "INFERRED" marks
a definition that goes beyond what the column name and those forms show, and
"UNCLEAR" one whose sense couldn't be recovered. Each anchor is constructed
unless marked. All Claude's proposals.

Writes analysis/codebook/definitions.csv (column, definition, anchor_y, anchor_n, confidence).
"""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent

D = {
 # form facts
 "genitive_case": ("The form itself is a genitive case form.", "my, whose", "me, who", "sure"),
 "accusative_case": ("The form itself is an accusative case form.", "him, whom", "he, who", "sure"),
 "nominative_case": ("The form itself is a nominative case form.", "he, who", "him, whom", "sure"),
 "in_word_formation_e_g_a_many_sided_shape": ("The form occurs as an element of a compound or derived word (a many-sided shape).", "many (many-sided)", "the", "INFERRED"),
 "has_derivationtionally_related_words": ("The lexeme has derivationally related words (anybody/any; everyone/every).", "every (everyone)", "the", "INFERRED"),
 "has_corresponding_word": ("The form has a homonym in another category (adjective little, adverb much, conjunction that).", "that (I know that ...)", "every", "INFERRED"),
 "compound_word": ("The form is a compound (some+one).", "someone", "some", "sure"),
 "Monmorphemic": ("The form is a single morpheme.", "some", "someone", "sure"),
 "Start_with_th": ("The form begins with the sound /ð/.", "this", "which", "sure"),
 "Start_with_hw": ("The form begins with wh- spelling.", "which", "this", "sure"),
 # inflection
 "inflects_for_case": ("DERIVED: its lexeme has a case form other than its plain form: a distinct accusative, a genitive other than plain + 's, or distinct dependent and independent forms. A genitive formed by adding 's isn't counted (Brett, 24 Oct); it is accepts_genitive_apstrophe_s.", "he (him, his)", "anybody (anybody's is plain + 's)", "sure"),
 "accepts_genitive_apstrophe_s": ("A genitive in 's can be formed on it, or on the NP it heads (either's, the dog's).", "either's", "*many's", "sure"),
 "paradigm_has_distinct_acc_form": ("Its paradigm has a distinct accusative form.", "he/him", "you/you", "sure"),
 "paradigm_has_genitive_form": ("Its paradigm has a genitive form other than the plain form plus 's (I/my, he/his, who/whose). Taking 's is a separate column (accepts_genitive_apstrophe_s); 's is not counted morphologically (Brett, 24 Oct).", 'I/my', "anybody (anybody's is plain + 's)", 'sure'),
 "paradigm_has_distinct_independent_genitive_form": ("Its paradigm has an independent genitive distinct from the dependent one (my/mine).", "I (my, mine)", "he (his, his)", "sure"),
 "paradigm_has_distinct_self_form": ("Its paradigm has a reflexive -self form.", "I (myself)", "who", "sure"),
 "paradigm_has_distinct_plural_form": ("Its paradigm has a form differing in number from this one (this/these; dog/dogs).", "this (these)", "each", "sure"),
 "does_not_inflect": ("DERIVED: none of the inflection columns is y.", "", "", "sure"),
 # grade
 "paradigm_has_comparative_and_superlative_forms": ("It has inflected comparative and superlative forms.", "few (fewer, fewest)", "several", "sure"),
 "degree": ("Its meaning is gradable: it names a degree or amount on a scale that can be compared or intensified (much, many, few). Its use as a degree modifier of another word (a little tired) is a separate column.", "much", "every", "sure"),
 "has_analytic_comparative": ("It is graded by analytic more and most.", "numerous (more numerous)", "few", "sure"),
 "can_be_modified_by_adverb_very": ("Degree very can modify it directly.", "very few", "*very every", "sure"),
 # particle object
 "Must_be_stressed_as_object_after_particle": ("RECODE as may_follow_particle_unstressed_as_object: as an object, it can follow a verb's particle unstressed (pick up the dog). x if it can't be an object.", "pick up the dog", "*pick up it", "sure"),
 # reference
 "anaphoric_marker": ("It can take its interpretation from an antecedent in context (A lot were arrested; I'll take some).", "some", "the", "INFERRED"),
 "deictic_marker": ("Its meaning is anchored to the speech situation: speaker, addressee, or the time or place of speaking (I, you, this, next week). Third-person pronouns used with pointing don't count; relative which is anaphoric and definite, not deictic.", 'this', 'which', 'sure'),
 "person_deixis": ("Its own meaning is anchored to the speaker or addressee: it refers to them, or to a group that includes them (I, you, we). Reference that takes in the speaker or addressee only through something else, a partitive (all of us), an antecedent (We love each other), or an imperative (Everybody sit down!), doesn't count.", "we", "they", "sure"),
 "pro_form": ('RECODE (Brett, 24 Oct: the 2021 column was wrong): it can stand for a phrase recoverable from context, as an anaphoric pro-form. Interrogative who is no pro-form (CGEL p. 1462); dummies stand for nothing.', 'she (anaphoric)', 'who (interrogative); it (dummy)', 'sure'),
 "dummy": ("It can be a dummy, with no reference (It is raining; there is).", "it", "this", "sure"),
 # gender
 "personal_gender_as_head_or_fused_head": ("FORK (gender): it carries personal gender (selects who, he, she). CGEL's terms: what a referring use selects; Reynolds 2025: a contrast carried in the word. The 2021 coding follows the second (few, plural they: n).", "someone", "something", "FORK"),
 "non_personal_gender": ("FORK (gender): it carries non-personal gender (selects it, which). As above.", "something", "someone", "FORK"),
 "epicene_personal_gender": ("FORK (gender): personal gender not specified as masculine or feminine.", "someone", "she", "FORK"),
 "masculine_gender": ("It carries masculine gender.", "he", "she", "sure"),
 "feminine_gender": ("It carries feminine gender.", "she", "he", "sure"),
 "definite": ("It makes the NP it determines or heads definite: a classification (the, this, all, both, the personal pronouns; relative which, 'definite as relatives', CGEL p. 357).", 'the', 'a, each, few', 'sure'),
 "indefinite": ("It can mark or have indefinite reference.", "a, some", "the", "sure"),
 # quantification
 "existential": ("It expresses existential quantification, positive or negative: it asserts or denies that there is something meeting a description (CGEL p. 423 names some, any, and no as the existential quantifiers). A form with no quantificational meaning, such as a dummy, is x.", "several", "every", "sure"),
 "universal": ("Its meaning is universal quantification.", "every", "some", "sure"),
 "free_choice": ("It can have a free-choice reading (any you like).", "any", "some", "sure"),
 "negative": ("Its meaning is negative: it denies existence or quantity outright (no, nobody, neither), not merely a small quantity (few is n here; see the polarity columns).", "nobody", "few", "sure"),
 "non_affirmative": ("It is a non-affirmative polarity item, or has such a use (any, much, either).", "any", "some", "sure"),
 "dual": ("Its meaning involves two (both, either, twice).", "both", "all", "sure"),
 "paucal": ("Its meaning is a small quantity (few, a little, several).", "few", "many", "sure"),
 "multal": ("Its meaning is a large quantity (many, much).", "many", "few", "sure"),
 "proportional": ("UNCLEAR: 2021 y for a, a few, many, cardinals, some, the compounds with some-, the demonstratives; n for all, each, every, any, no, the, pronouns.", "", "", "UNCLEAR"),
 "semantically_countable": ('It itself quantifies over or denotes countable individuals (few, many, two). Combining with a count noun without quantifying (the) is the separate compatibility column.', 'few', 'the', 'sure'),
 "semantically_uncountable": ('It itself quantifies or measures a non-count amount (much, a little). Combining with a non-count noun without quantifying (the, which) is the separate compatibility column.', 'much', 'the', 'sure'),
 "semantically_singular": ("It can denote a single individual or a single amount.", "this", "these", "sure"),
 "semantically_plural": ("It can denote more than one individual.", "these", "this", "sure"),
 "distributive": ("With a predicate, it allows a distributive reading, each individual separately (All the students lifted a box: one box each; They each left).", "each", "", "sure"),
 "joint": ("With a predicate, it allows a collective reading, the individuals jointly (All the students lifted the piano together).", "all", "each", "sure"),
 "cardinal": ("It is a cardinal numeral or has a cardinal meaning.", "two", "few", "sure"),
 "disjunctive": ("Its meaning is disjunctive (one or the other).", "either", "both", "sure"),
 "sufficiency": ("Its meaning is sufficiency.", "enough", "many", "sure"),
 # binding, interrogative, time, place
 "interrogative": ("It can be interrogative.", "which", "this", "sure"),
 "reflexive": ("It is a reflexive form (-self). CHECK: oneself is n in 2021.", "myself", "me", "sure"),
 "reciprocal": ("It is a reciprocal.", "each other", "each", "sure"),
 "must_be_outranked_by_a_coindexed_element": ("RECODE as may_occur_without_a_binder: it can occur with no coindexed element outranking it. Pair with may_occur_with_a_binder.", "she (She left)", "herself (*Herself left)", "sure"),
 "temporal": ("Its meaning is temporal (once, today, next).", "today", "here", "sure"),
 "locative": ("Its meaning is locative (somewhere, anywhere).", "somewhere", "something", "sure"),
 # peripheral modifiers
 "can_be_followed_by_adjective_such": ("Such can follow it (some such, no such, all such).", "some such", "*the such", "sure"),
 "can_be_modified_by_almost": ('Almost modifies a phrase the form heads (almost every, almost all). Count it only where the modifier attaches to a phrase the form heads: in quite the scholar, quite is the sibling of an NP headed by scholar, not by the (Brett, 24 Oct).', 'almost every', '*almost some', 'sure'),
 "can_be_modified_by_approximately": ('Approximately modifies a phrase the form heads (approximately two). Count it only where the modifier attaches to a phrase the form heads: in quite the scholar, quite is the sibling of an NP headed by scholar, not by the (Brett, 24 Oct).', 'approximately two', '*approximately few', 'sure'),
 "can_be_modified_by_at_least": ('SPLIT: at least as a lower bound on a quantity (CGEL p. 432: mainly numerals, some, a few, a little, enough, sufficient; several takes at least). Count it only where the modifier attaches to a phrase the form heads: in quite the scholar, quite is the sibling of an NP headed by scholar, not by the (Brett, 24 Oct).', 'at least two', '*at least each', 'sure'),
 "can_be_modified_by_hardly": ('Hardly modifies a phrase the form heads (hardly any, hardly anyone). Count it only where the modifier attaches to a phrase the form heads: in quite the scholar, quite is the sibling of an NP headed by scholar, not by the (Brett, 24 Oct).', 'hardly any', '*hardly some', 'sure'),
 "can_be_modified_by_not": ("Not modifies the phrase the form heads, as a modifier at the level of the determinative's phrase (CGEL p. 431: most readily many, much, all, every, enough; also sufficient, a few, a little; not both, each, few, little, some). Count it only where the modifier attaches to a phrase the form heads: in quite the scholar, quite is the sibling of an NP headed by scholar, not by the (Brett, 24 Oct).", 'not many', '*not few', 'sure'),
 "takes_adverb_quite_as_a_modifier": ('Quite modifies a phrase the form heads (quite a few, quite enough, quite everything). Count it only where the modifier attaches to a phrase the form heads: in quite the scholar, quite is the sibling of an NP headed by scholar, not by the (Brett, 24 Oct).', 'quite a few', 'the (quite the scholar)', 'sure'),
 "takes_post_head_modifier_the_hell": ("The hell, on earth and the like can follow it.", "who the hell", "*someone the hell", "sure"),
 # coordination, repetition
 "Coordinates_with_independent_genitives": ("It can be coordinated with an independent genitive (this and mine).", "this and mine", "", "INFERRED"),
 "Coordinates_with_dependent_genitives": ('Before a shared noun, it can be coordinated with a dependent genitive (my and your friends; whose and which books).', 'my and your', 'each (*each and my friends)', 'sure'),
 "Coordinates_with_NPs": ("The phrase it heads can be coordinated with an NP.", "some and the rest", "", "sure"),
 "May_coordinate_with_non_fused_determiners": ('Before a shared noun, it can be coordinated with another determiner (few or no friends, one or two days, this and every day).', 'few or no', '', 'sure'),
 "functions_as_marker_of_coordination": ("It can mark coordination (both ... and, either ... or).", "both", "all", "sure"),
 "intensifying_reduplication": ("It can be repeated for intensity (more and more).", "more and more", "", "sure"),
 "ironic_use_of_repetition": ("UNCLEAR in part: 2021 y only for genitive pronouns (my, my!; yours, yours?).", "", "", "INFERRED"),
 # head selection and compatibility (Det function)
 "selects_singular_heads": ("As a determiner, it requires a singular head.", "each (each book)", "both", "sure"),
 "selects_count_singular_heads": ("As a determiner, it requires a count singular head.", "a", "much", "sure"),
 "selects_non_count_heads": ("As a determiner, it requires (or allows only) a non-count head.", "much", "many", "sure"),
 "selects_plural_heads": ("As a determiner, it requires a plural head.", "several", "each", "sure"),
 "compatible_count_sing_NP": ("It can combine with a count singular NP or nominal (as determiner or in a partitive).", "every book", "", "INFERRED"),
 "compatible_count_plur_NP": ("It can combine with a count plural NP or nominal.", "some books", "", "INFERRED"),
 "compatible_non_count_NP": ("It can combine with a non-count NP or nominal.", "some water", "", "INFERRED"),
 # predeterminer
 "Forms_universal_pronouns_before_all": ("It can precede all to form a universal phrase (us all, you all).", "us all", "", "sure"),
 "functions_as_a_predeterminer_modifier": ("It can function as a predeterminer modifier, before a determiner (all the, twice the, such a).", "all the books", "", "sure"),
 "takes_predeterminer_modifiers_all_or_both": ("It can follow predeterminer all or both (all the, both these, all my).", "all the", "*all some", "sure"),
 "occurs_after_predeterminer_modifiers_fractions": ("It can follow a fraction such as half directly, with no of and no genitive between them (half the cake, half a loaf). Half of the cake and half its size don't count.", "half the cake", "", "sure"),
 "occurs_after_predeterminer_modifiers_multipliers": ("It can follow a multiplier such as twice or double directly, with no of and no genitive between them (twice the size, double that). Twice its size doesn't count. (Brett, 24 Oct, from COCA: you are twice him.)", "twice the size", "", "sure"),
 # modifier functions
 "functions_as_prehead_modifier_in_nominal": ('It can be a pre-head modifier of any kind inside a nominal, attributive or not; non-attributive pre-head modifiers include degree modifiers like very in the very few (Brett, 24 Oct).', 'the few people', '', 'sure'),
 "functions_as_attrib_modifier_in_nominal": ('It can be an attributive modifier: an adjective-like pre-head modifier of a noun inside a nominal (the two books, his every move, the me generation, the once king).', 'the two books', '', 'sure'),
 "functions_as_degree_modifier_in_AdjP": ('It (or its phrase) can modify an adjective or adverb phrase as a degree modifier (much bigger, that big, a lot bigger, the sooner the better, all the better).', 'much bigger', '', 'sure'),
 "functions_as_post_head_modifier_of_it_or_them": ("It can follow it or them as a modifier (them all, them both).", "them all", "", "sure"),
 "functions_as_post_head_modifier_of_N": ("It can follow a noun as a modifier (money enough, two more).", "money enough", "", "sure"),
 "NP_functions_as_modifier_in_AdvP": ("Its NP can modify an adverb phrase (much later, a whole day late).", "much later", "", "sure"),
 "NP_functions_as_modifier_in_PP": ("Its NP can modify a preposition phrase (much before noon, a mile under the sea).", "much before noon", "", "sure"),
 "functions_as_adjunct_in_clause_structure": ("It (or its NP) can be an adjunct in a clause (I walk a lot; We came today).", "today", "", "sure"),
 # argument and other NP functions
 "appears_in_subject": ("It can appear in a subject NP (Some left; Any child knows; The king himself came). Count it where the form, or a phrase it heads, is the NP's head, its determiner, or a modifier next to its noun or nominal; something embedded more deeply, as in a relative clause inside the NP, doesn't count.", "Some left", "", "sure"),
 "appears_in_object": ("It can appear in an object NP (I saw some; I need every penny). Count it where the form, or a phrase it heads, is the NP's head, its determiner, or a modifier next to its noun or nominal; something embedded more deeply, as in a relative clause inside the NP, doesn't count.", "I saw some", "", "sure"),
 "NP_functions_as_complement_in_PP": ("An NP it heads can be the complement of a preposition. Dependent-only forms and nominatives n.", "with some", "*with he", "sure"),
 "appears_in_existentials_there_s_on_the_table": ("It can appear in the displaced subject of an existential (There's some on the table). Count it where the form, or a phrase it heads, is the NP's head, its determiner, or a modifier next to its noun or nominal; something embedded more deeply, as in a relative clause inside the NP, doesn't count.", "some", "the", "sure"),
 "functions_as_subject_of_present_participal_of_joining_you": ("It (or its NP) can be the subject of a gerund-participial clause in complement function (I don't mind him joining you). Absolutes (She being ill, we left) don't count.", 'him joining you', 'she (absolute only)', 'sure'),
 "Functions_as_subject_of_interrogative_tag": ("It can be the subject of a tag question (..., isn't she?).", "she", "someone", "sure"),
 "functions_in_vocative": ("It can be a vocative (Someone, help!; You, come here).", "you", "", "sure"),
 "functions_as_predicative_complement": ("It (or its phrase) can be a predicative complement.", "It's something", "", "sure"),
 "functions_as_predicative_complement_to_seem": ("It can be a bare predicative complement of seem (It seems nothing; He seemed himself).", "seemed nothing", "", "sure"),
 "functions_as_subject_determiner": ("It, or an NP it heads, can be a genitive in determiner function, whether the genitive is a form of its own (my book) or made with 's (anybody's guess). A syntactic property, so 's counts; whether the form is itself a genitive is the genitive_case column.", "my", "", "sure"),
 "functions_as_determiner_in_day_s_time_ago": ("It can determine the plural measure noun of a duration genitive, in __ days' time (in a few days' time, in two weeks' time). Definite genitives (the day's events) don't count.", "a few days' time", "the (the day's events)", 'sure'),
 "heads_nominal_after_separate_determiner": ("It can head a nominal with a determiner before it, keeping its own meaning (the few, the two, a dog). Split by frame.", "the few", "*the some", "sure"),
 "functions_as_head_of_partitive_construction": ("It can head a partitive, X of the Ns.", "some of the books", "*every of the books", "sure"),
 # dependents
 "takes_prehead_AdjP_modifier": ("A restrictive adjective can precede and modify it (good news, the lucky few).", "the lucky few", "*interesting them", "sure"),
 "takes_relative_clause_modifier": ("An integrated relative clause can modify it.", "those who came", "", "sure"),
 "takes_post_head_AdjP": ("An adjective phrase can follow and modify it.", "someone nice", "", "sure"),
 "takes_nonpartitive_complement": ("It takes a complement other than a partitive of-phrase (a lot of people; more than ten; proud of).", "more than ten", "", "sure"),
 "takes_ly_adverb_modifier": ("A degree or evaluative -ly adverb can modify it directly (remarkably few); approximators excluded.", "remarkably few", "*remarkably some", "sure"),
 "take_poor_lucky_silly_as_attrib_modifiers": ("It takes the exclamative non-restrictive lucky, poor, silly (Lucky you!, Poor everybody!).", "lucky you", "", "sure"),
 "takes_else_or_more_as_a_post_head_dependent": ('SPLIT: else can follow it (someone else, who else, nothing else).', 'someone else', '*some else', 'sure'),
 "functions_as_fused_determiner_head": ("LABEL: CGEL's analysis of an independent use as fused determiner-head; not a property of form.", "", "", "sure"),
 # columns added on Brett's 24 Oct review ("In many cases, I think the answer is to add columns")
 "definite_reference_possible": ("It can head or appear in an NP with definite reference, whatever marks the definiteness (the few, these three).", "few (the few)", "a", "sure"),
 "at_least_focus": ("At least as a focusing modifier of an NP the form heads, ranking it against alternatives (At least him; At least Kim came)." + " Count it only where the NP is headed by the form.", "at least him", "", "sure"),
 "takes_more_as_a_post_head_dependent": ("More can follow it as a dependent (some more, a few more, nothing more, little more).", "some more", "*the more (as a dependent)", "sure"),
 "inflects_for_dependent_independent_use": ("It is one of a pair of distinct inflectional forms for dependent and independent use (CGEL p. 410: my/mine, your/yours, her/hers, our/ours, their/theirs, no/none).", "no", "his (one form for both)", "sure"),
 # Redesigned after Brett's answers on the y-to-m sheet (24 Oct): columns set up to
 # cover the facts, not to recover the 2021 senses.
 "det_takes_count_singular_head": ("As a determiner, it can take a count singular noun as the head of the NP (a book, every book).", "every (every book)", "", "sure"),
 "det_takes_plural_head": ("As a determiner, it can take a plural noun as the head of the NP (several books, the books).", "several (several books)", "", "sure"),
 "det_takes_non_count_head": ("As a determiner, it can take a non-count noun as the head of the NP (much water, the water).", "much (much water)", "", "sure"),
 "partitive_takes_count_singular_oblique": ("As head of a partitive (X of the ...), it can take a count singular NP after of (some of the cake, all of the book).", "all (all of the book)", "", "sure"),
 "partitive_takes_plural_oblique": ("As head of a partitive (X of the ...), it can take a plural NP after of (many of the books).", "many (many of the books)", "", "sure"),
 "partitive_takes_non_count_oblique": ("As head of a partitive (X of the ...), it can take a non-count NP after of (much of the water).", "much (much of the water)", "", "sure"),
 "heads_subject_np": ("It can be the head of a subject NP, alone or with dependents (She left; Few came). Being the NP's determiner or a modifier in it (The king himself came) doesn't count; that is the appears_in_subject column.", "few (Few came)", "", "sure"),
 "heads_object_np": ("It can be the head of an object NP, alone or with dependents (I saw her; I took few). Being the NP's determiner or a modifier in it doesn't count; that is the appears_in_object column.", "few (I took few)", "", "sure"),
 "imperative_subject": ("It, or an NP it heads, can be the subject of an imperative (Everybody sit down!; Somebody help me!).", "everybody", "", "sure"),
 "polarity_item": ("It is a polarity item: in some use it needs a non-affirmative context such as negation or a question (I didn't see any; *I saw any, in the use that isn't free choice; ever, yet).", "ever", "", "sure"),
 "positively_oriented": ("It is positively oriented: in its ordinary use it resists falling inside the scope of a negator (in I didn't see some of them, some isn't negated) (CGEL ch. 9 §4.2, p. 829).", "already", "", "sure"),
 "sanctions_polarity_items": ("It sanctions polarity items in its scope, creating a non-affirmative context (No one saw anything; Few saw anything; Who saw anything?) (CGEL ch. 9 §4.4, p. 834).", "never (Never did anyone ...)", "", "sure"),
 "heads_np_with_singular_agreement": ("An NP it heads, alone or with dependents, can take a singular verb (Neither is here; This is mine). A form that never heads an NP is x.", "this (This is mine)", "", "sure"),
 "heads_np_with_plural_agreement": ("An NP it heads, alone or with dependents, can take a plural verb (These are mine; Neither of them are coming, informally). A form that never heads an NP is x.", "these (These are mine)", "", "sure"),
 "refers_to_or_ranges_over_single": ("It refers to, or quantifies over, single individuals or a single amount, one at a time (she; each; no one).", "each", "all", "sure"),
 "refers_to_or_ranges_over_plurality": ("It refers to, or quantifies over, more than one individual taken together (they; all; many).", "all", "each", "sure"),
 # Morphology at three levels (Brett, 24 Oct). Word level:
 "takes_plural_es": ("The form can take the plural suffix -(e)s (cat/cats, box/boxes). A form that is already plural is x.", "cat (cats)", "", "sure"),
 "is_plural_in_es": ("The form itself is a plural made with -(e)s (cats, boxes).", "cats", "mice", "sure"),
 "is_independent_form": ("The form itself is the independent member of a pair of forms for dependent and independent use (mine beside my).", "mine", "my", "sure"),
 "is_comparative_or_superlative_form": ("The form itself is an inflected comparative or superlative (bigger, biggest).", "bigger", "big", "sure"),
 # Lexeme level:
 "paradigm_has_dependent_independent_pair": ("Its lexeme has distinct forms for dependent and independent use (my/mine), whichever of them this form is.", "me (my/mine)", "him (his/his)", "sure"),
}


def main():
    cols = [r["column"] for r in csv.DictReader((HERE / "columns.csv").open())]
    header = next(csv.reader((HERE.parents[1] / "analysis" / "matrix-2026-10" / "matrix-2026-10.csv").open()))
    for w in header[1:header.index("genitive_case")]:   # the 2021 word-part columns
        D.setdefault(w, (f"The form contains the word {w.replace('_', ' ')} as one of its parts, or is that word (anybody contains any and body; another contains a, another, and other). Reynolds (2021): a column for each word appearing as part of another word.", "", "", "sure"))
    missing = [c for c in cols if c not in D]
    assert not missing, missing
    with (HERE / "definitions.csv").open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["column", "definition", "anchor_y", "anchor_n", "confidence"])
        for c in cols:
            w.writerow([c, *D[c]])
    from collections import Counter
    print(len(cols), "definitions;", dict(Counter(D[c][3] for c in cols)))


if __name__ == "__main__":
    main()
