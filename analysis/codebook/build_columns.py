#!/usr/bin/env python3
"""Build analysis/codebook/columns.csv: one row per matrix column (the 105
syntactic and semantic columns of matrix-2026-10 plus the 10 added from CGEL's
lists, 24 Oct 2026) with its super-column, type of claim, action under the
codebook (planning/codebook.md), absence partner, and frame treatment.

All assignments are Claude's proposals for Brett's approval (24 Oct 2026).

Types: possibility (a "may" claim); universal (worded as "must"/"never", to be
reversed); derived (definable from other columns); form (a fact about the
form's shape, no modality); lexeme (a fact about the form's lexeme, the same
for every form of it); base (a fact about a base of a compound form); label (an
analysis label, excluded from the tests); superseded (a 2021 column replaced
by better-defined ones, kept as the record and excluded from the tests);
unclear (sense not recoverable from
the coded forms; Brett to define).

Morphology has three levels (Brett, 24 Oct: columns "for each of the words and
their roots"; "I meant the bases, but both apply"): the word (the row's form),
its lexeme, and the words a form contains (the 2021 matrix's word-part columns:
anybody contains any and body; CGEL p. 423 calls these the compound's
determinative and nominal bases).
"""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
MATRIX = ROOT / "analysis" / "matrix-2026-10" / "matrix-2026-10.csv"
ADDED = ROOT / "analysis" / "noun-coding-2026-10-24" / "features-added.csv"

_HEADER = next(csv.reader(MATRIX.open()))
WORD_PART = _HEADER[1:_HEADER.index("genitive_case")]

FAMILY = {
    "case_form": ["genitive_case", "accusative_case", "nominative_case"],
    "shape": ["in_word_formation_e_g_a_many_sided_shape", "has_derivationtionally_related_words",
              "has_corresponding_word", "compound_word", "Monmorphemic", "Start_with_th", "Start_with_hw"],
    "inflection": ["takes_plural_es", "is_plural_in_es", "is_independent_form", "paradigm_has_dependent_independent_pair",
                   "inflects_for_case", "accepts_genitive_apstrophe_s", "inflects_for_dependent_independent_use", "paradigm_has_distinct_acc_form", "paradigm_has_genitive_form",
                   "paradigm_has_distinct_independent_genitive_form", "paradigm_has_distinct_self_form",
                   "paradigm_has_distinct_plural_form", "does_not_inflect"],
    "grade": ["is_comparative_or_superlative_form", "paradigm_has_comparative_and_superlative_forms", "degree", "has_analytic_comparative",
              "can_be_modified_by_adverb_very"],
    "particle_object": ["Must_be_stressed_as_object_after_particle"],
    "reference": ["anaphoric_marker", "deictic_marker", "person_deixis", "pro_form", "dummy"],
    "gender": ["personal_gender_as_head_or_fused_head", "non_personal_gender", "epicene_personal_gender",
               "masculine_gender", "feminine_gender"],
    "definiteness": ["definite", "indefinite", "definite_reference_possible"],
    "quantification": ["existential", "universal", "free_choice", "dual",
                       "paucal", "multal", "proportional", "cardinal", "disjunctive", "sufficiency",
                       "distributive", "joint"],
    "interrogative": ["interrogative"],
    "binding": ["reflexive", "reciprocal", "must_be_outranked_by_a_coindexed_element"],
    "number_meaning": ["semantically_singular", "semantically_plural",
                       "refers_to_or_ranges_over_single", "refers_to_or_ranges_over_plurality"],
    "agreement": ["heads_np_with_singular_agreement", "heads_np_with_plural_agreement"],
    "polarity": ["negative", "non_affirmative", "polarity_item", "positively_oriented", "sanctions_polarity_items"],
    "countability": ["semantically_countable", "semantically_uncountable"],
    "time_place": ["temporal", "locative"],
    "peripheral_modifiers": ["can_be_followed_by_adjective_such", "can_be_modified_by_almost",
                             "can_be_modified_by_approximately", "can_be_modified_by_at_least",
                             "can_be_modified_by_hardly", "can_be_modified_by_not", "at_least_focus",
                             "takes_adverb_quite_as_a_modifier", "takes_post_head_modifier_the_hell"],
    "coordination": ["Coordinates_with_independent_genitives", "Coordinates_with_dependent_genitives",
                     "Coordinates_with_NPs", "May_coordinate_with_non_fused_determiners",
                     "functions_as_marker_of_coordination"],
    "repetition": ["intensifying_reduplication", "ironic_use_of_repetition"],
    "head_selection": ["selects_singular_heads", "selects_count_singular_heads", "selects_non_count_heads",
                       "selects_plural_heads", "det_takes_count_singular_head", "det_takes_plural_head",
                       "det_takes_non_count_head"],
    "compatibility": ["compatible_count_sing_NP", "compatible_count_plur_NP", "compatible_non_count_NP"],
    "predeterminer": ["Forms_universal_pronouns_before_all", "functions_as_a_predeterminer_modifier",
                      "takes_predeterminer_modifiers_all_or_both", "occurs_after_predeterminer_modifiers_fractions",
                      "occurs_after_predeterminer_modifiers_multipliers"],
    "modifier_functions": ["functions_as_prehead_modifier_in_nominal", "functions_as_attrib_modifier_in_nominal",
                           "functions_as_degree_modifier_in_AdjP", "functions_as_post_head_modifier_of_it_or_them",
                           "functions_as_post_head_modifier_of_N", "NP_functions_as_modifier_in_AdvP",
                           "NP_functions_as_modifier_in_PP", "functions_as_adjunct_in_clause_structure"],
    "argument_functions": ["imperative_subject", "heads_subject_np", "heads_object_np", "appears_in_subject", "appears_in_object", "NP_functions_as_complement_in_PP",
                           "appears_in_existentials_there_s_on_the_table",
                           "functions_as_subject_of_present_participal_of_joining_you",
                           "Functions_as_subject_of_interrogative_tag", "functions_in_vocative"],
    "predicative": ["functions_as_predicative_complement", "functions_as_predicative_complement_to_seem"],
    "determiner_function": ["functions_as_subject_determiner", "functions_as_determiner_in_day_s_time_ago"],
    "determiner_taken": ["heads_nominal_after_separate_determiner"],
    "partitive": ["functions_as_head_of_partitive_construction", "partitive_takes_count_singular_oblique",
                  "partitive_takes_plural_oblique", "partitive_takes_non_count_oblique"],
    "dependents": ["takes_prehead_AdjP_modifier", "takes_relative_clause_modifier", "takes_post_head_AdjP",
                   "takes_nonpartitive_complement", "takes_ly_adverb_modifier",
                   "take_poor_lucky_silly_as_attrib_modifiers", "takes_else_or_more_as_a_post_head_dependent", "takes_more_as_a_post_head_dependent"],
    "analysis_label": ["functions_as_fused_determiner_head"],
    # Reynolds (2021): "a column for each word appearing as part of another word";
    # the 50 that survive in matrix-2026-10, read from its header (restored 24 Oct,
    # replacing 18 coarser base_ columns Claude had re-invented the same day).
    "base": WORD_PART,
}
# Added 24 Oct after Brett's answers on the y-to-m sheet ("what I meant is mostly
# irrelevant. The question is ... how should these columns be set up to cover the
# relevant syntactic, semantic, phonological and morphological facts").
REDESIGN_NEW = ["imperative_subject", "heads_subject_np", "heads_object_np", "det_takes_count_singular_head", "det_takes_plural_head", "det_takes_non_count_head",
                "partitive_takes_count_singular_oblique", "partitive_takes_plural_oblique",
                "partitive_takes_non_count_oblique", "polarity_item", "positively_oriented",
                "sanctions_polarity_items", "heads_np_with_singular_agreement", "heads_np_with_plural_agreement",
                "refers_to_or_ranges_over_single", "refers_to_or_ranges_over_plurality"]
# Added 24 Oct on Brett's morphology point.
MORPH_NEW = ["takes_plural_es", "is_plural_in_es", "is_independent_form",
                              "paradigm_has_dependent_independent_pair", "is_comparative_or_superlative_form"]

TYPE = {}
for f in FAMILY["case_form"] + FAMILY["shape"]:
    TYPE[f] = "form"
TYPE.update({
    "does_not_inflect": "derived",
    "Must_be_stressed_as_object_after_particle": "universal",
    "must_be_outranked_by_a_coindexed_element": "universal",
    # "As a determiner, it requires a ... head": necessity claims, first typed as
    # possibilities; the y-to-m pass (24 Oct) showed the slip.
    # Paradigm facts hold of the lexeme and are copied to each of its forms: no m,
    # and pooled by lexeme in the model so one fact isn't counted once per form.
    "has_derivationtionally_related_words": "lexeme", "paradigm_has_distinct_acc_form": "lexeme",
    "paradigm_has_genitive_form": "lexeme", "paradigm_has_distinct_independent_genitive_form": "lexeme",
    "paradigm_has_distinct_self_form": "lexeme", "paradigm_has_comparative_and_superlative_forms": "lexeme",
    "paradigm_has_distinct_plural_form": "lexeme", "paradigm_has_dependent_independent_pair": "lexeme",
    # With 's not counted (Brett, 24 Oct), "a case form other than the plain form" is
    # the disjunction of the accusative, genitive and dependent/independent columns.
    "inflects_for_case": "derived",
    "is_plural_in_es": "form", "is_independent_form": "form", "is_comparative_or_superlative_form": "form",
    "inflects_for_dependent_independent_use": "form",
    **{c: "base" for c in FAMILY["base"]},
    "functions_as_fused_determiner_head": "label",
    "proportional": "unclear",
    # Replaced after Brett's answers (24 Oct); kept as the 2021 record.
    **{c: "superseded" for c in ("selects_singular_heads", "selects_count_singular_heads", "selects_non_count_heads",
                                 "selects_plural_heads", "compatible_count_sing_NP", "compatible_count_plur_NP",
                                 "compatible_non_count_NP", "non_affirmative", "semantically_singular",
                                 "semantically_plural")},
    "functions_as_head_of_partitive_construction": "derived",
})

ACTION = {
    "form": "keep (fact of form)",
    "derived": "derive from the columns it is defined by; don't code",
    "lexeme": "keep as a fact of the lexeme (no m); pool by lexeme",
    "superseded": "keep as the 2021 record; replaced by the columns in recoded_as; excluded from the tests",
    "base": "keep as a fact of the compound's base (no m); pool by base; run the tests with and without",
    "universal": "reverse into possibility form",
    "label": "keep as a record of CGEL's analysis; exclude from the tests",
    "unclear": "Brett to define, or drop",
    "possibility": "keep",
}
ACTION_COL = {
    "functions_as_head_of_partitive_construction": "derive from the three partitive_takes_ columns; don't code",
    **{c: "keep; recode blind on the new definition (the 2021 cells answer an earlier sense)"
       for c in ("existential", "negative", "distributive", "joint", "free_choice",
                 # redefined or frame-split after Brett's n-to-m answers (24 Oct)
                 "appears_in_existentials_there_s_on_the_table", "person_deixis", "degree",
                 "can_be_modified_by_adverb_very", "universal", "functions_as_post_head_modifier_of_N",
                 "occurs_after_predeterminer_modifiers_multipliers", "occurs_after_predeterminer_modifiers_fractions",
                 "anaphoric_marker", "appears_in_subject", "appears_in_object")},
    "does_not_inflect": "derive from the inflection columns; don't code (contradicted them for 17 forms)",
    "inflects_for_case": "derive from paradigm_has_distinct_acc_form, paradigm_has_genitive_form, and paradigm_has_dependent_independent_pair; don't code",
}
REVERSED_AS = {
    "Must_be_stressed_as_object_after_particle": "may_follow_particle_unstressed_as_object",
    "must_be_outranked_by_a_coindexed_element": "may_occur_without_a_binder",
    **{c: "det_takes_count_singular_head, det_takes_plural_head, det_takes_non_count_head ('requires' is derived)"
       for c in ("selects_singular_heads", "selects_count_singular_heads", "selects_non_count_heads", "selects_plural_heads")},
    **{c: "det_takes_ and partitive_takes_ columns (combining is derived)"
       for c in ("compatible_count_sing_NP", "compatible_count_plur_NP", "compatible_non_count_NP")},
    "non_affirmative": "polarity_item, sanctions_polarity_items",
    "semantically_singular": "heads_np_with_singular_agreement, refers_to_or_ranges_over_single",
    "semantically_plural": "heads_np_with_plural_agreement, refers_to_or_ranges_over_plurality",
}
# Absence partners (◇¬P) where P can be necessary.
PARTNER = {
    "heads_nominal_after_separate_determiner": "heads_NP_with_no_determiner (new; frame-split)",
    "personal_gender_as_head_or_fused_head": "non_personal_gender (existing; contrary with gaps: x where gender can't arise)",
    "non_personal_gender": "personal_gender_as_head_or_fused_head (existing)",
    "semantically_singular": "semantically_plural (existing)",
    "semantically_plural": "semantically_singular (existing)",
    "semantically_countable": "semantically_uncountable (existing)",
    "semantically_uncountable": "semantically_countable (existing)",
    "definite": "indefinite (existing)",
    "indefinite": "definite (existing)",
    "must_be_outranked_by_a_coindexed_element": "may_occur_with_a_binder (check: pronouns resist local binders)",
}
FRAMES = {
    # Frames from Brett's answers on the n-to-m sheet (24 Oct).
    "appears_in_existentials_there_s_on_the_table": "split: ordinary existential; presentational or list existential (There's only me; There's always tomorrow)",
    "appears_in_subject": "split (Brett, 24 Oct: 'split into subject of main clause, subject of non-finite, etc.'): subject of a main clause; subject of a non-tensed clause (For them to quit would be odd); subject of an embedded tensed clause (the man whom I think is guilty); emphatic reflexive modifier in the subject (The queen herself came; Brett: 'Doesn't count or it's a frame'); fused relative (Whoever said that was wrong: CGEL ch. 12 §6.1, p. 1069)",
    "appears_in_object": "split (Brett, 24 Oct: '2 yes', the same split as the subject): object of a main clause; object in a non-tensed clause; object of an embedded tensed clause (the book which I read); fused relative (Take what you want; Marry who you want: CGEL ch. 12 §6.1, p. 1069, analyses the fused relative as an NP headed by the relative word, so it heads the main clause's object)",
    "can_be_modified_by_adverb_very": "split: ordinary use; superlative or sequence intensifier (the very last, the very least); characterizing use (That's very him)",
    "universal": "split: ordinary use; free-choice reading (Any child could do that): Brett, 'why wouldn't it?'; CGEL p. 423 calls any existential, so the analysis runs the frame in and out",
    "functions_as_post_head_modifier_of_N": "split: ordinary use; post-head numeral (page one, room three)",
    "occurs_after_predeterminer_modifiers_multipliers": "split: ordinary use; arithmetic (twice two is four)",
    "occurs_after_predeterminer_modifiers_fractions": "split: ordinary use; arithmetic (half three is one and a half); clock time, chiefly British (half three)",
    "anaphoric_marker": "split: ordinary use; free indirect discourse (Tomorrow was Christmas)",
    "free_choice": "split: ordinary use; fused relative (invite who you like): Brett, 24 Oct, on what the 2021 y's for plain who, which, whose recorded",
    "takes_plural_es": "split: ordinary use; set-denoting secondary use (the Smiths, ten mes, somethings, in threes: evidence ledger rows secondary-use-schema and cardinal-secondary-use)",
    "heads_nominal_after_separate_determiner": "split: argument, predicative (bare role), fixed PP, set-denoting use; nominal in Mod as a check",
    "semantically_singular": "open: kinds reading (thousands of fishes) proposed by Brett",
    "semantically_plural": "open: kinds reading",
    "personal_gender_as_head_or_fused_head": "open: set-denoting use",
    "non_personal_gender": "open: set-denoting use",
    "takes_prehead_AdjP_modifier": "open: set-denoting use (the real me)",
    "functions_as_predicative_complement": "open: bare-role predicative",
}
# CGEL's stated diagnostic polarity (ch. 5 §1 [2]; ch. 6 §2 [1] and negative properties).
CGEL_POLARITY = {
    "takes_prehead_AdjP_modifier": "y characteristic of nouns (ch. 5 §1 [2iii]); n characteristic of adjectives (ch. 6 §2: not modified by adjectives)",
    "takes_relative_clause_modifier": "y characteristic of nouns (ch. 5 §1 [2iii])",
    "heads_nominal_after_separate_determiner": "y characteristic of nouns (ch. 5 §1 [2iii], 'certain determinatives'); n defining of pronouns (p. 429)",
    "takes_ly_adverb_modifier": "y characteristic of adjectives (ch. 6 §2 [1iii]); n characteristic of nouns (p. 538)",
    "paradigm_has_distinct_plural_form": "y characteristic of nouns (ch. 5 §1 [2i]); n characteristic of adjectives (ch. 6 §2)",
    "inflects_for_case": "y characteristic of nouns (ch. 5 §1 [2i], 'plain vs genitive'); with 's not counted, that diagnostic moves to accepts_genitive_apstrophe_s",
    "takes_plural_es": "y characteristic of nouns (ch. 5 §1 [2i]: 'Nouns prototypically inflect for number')",
    "paradigm_has_comparative_and_superlative_forms": "y characteristic of adjectives (ch. 6 §2 [1ii])",
    "has_analytic_comparative": "y characteristic of adjectives (ch. 6 §2 [1ii])",
    "can_be_modified_by_adverb_very": "y characteristic of adjectives (ch. 6 §2 [1ii])",
    "functions_as_attrib_modifier_in_nominal": "y characteristic of adjectives (ch. 6 §2 [1i])",
    "functions_as_predicative_complement": "y characteristic of adjectives (ch. 6 §2 [1i]) and of NPs (ch. 5 §1 [1i])",
    "takes_nonpartitive_complement": "adjectives 'do not take NPs as complement' (ch. 6 §2); nouns 'do not take objects' (ch. 5 §1 [2iii])",
    "appears_in_subject": "y defining of NPs (ch. 5 §1 [1i])",
    "appears_in_object": "y defining of NPs (ch. 5 §1 [1i])",
}


def main():
    header = next(csv.reader(MATRIX.open()))
    cols = header[1:]   # the word-part columns first, as in the 2021 matrix
    cols += [r["feature"] for r in csv.DictReader(ADDED.open()) if r["feature"] not in cols]
    cols += [c for c in ("definite_reference_possible", "at_least_focus", "takes_more_as_a_post_head_dependent",
             "inflects_for_dependent_independent_use") if c not in cols]  # added 24 Oct on Brett's review
    cols += [c for c in MORPH_NEW if c not in cols]
    cols += [c for c in REDESIGN_NEW if c not in cols]
    fam = {f: k for k, fs in FAMILY.items() for f in fs}
    missing = [c for c in cols if c not in fam]
    assert not missing, missing
    with (HERE / "columns.csv").open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["column", "super_column", "type", "action", "recoded_as", "absence_partner",
                    "frames", "cgel_polarity"])
        for c in cols:
            t = TYPE.get(c, "possibility")
            w.writerow([c, fam[c], t, ACTION_COL.get(c, ACTION[t]), REVERSED_AS.get(c, ""), PARTNER.get(c, ""),
                        FRAMES.get(c, "default (ordinary use)"), CGEL_POLARITY.get(c, "")])
    from collections import Counter
    print(len(cols), "columns;", dict(Counter(TYPE.get(c, "possibility") for c in cols)),
          "; super-columns:", len(FAMILY))


if __name__ == "__main__":
    main()
