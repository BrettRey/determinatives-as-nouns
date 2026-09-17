# Where the articles and the four gradable quantifiers sit in the 2021 matrix

<!-- SUMMARY: average-linkage clustering of the public 138 x 155 matrix; the articles sit in an 18-member dependent-only cluster with every, no, such, what, which; the four gradable quantifiers sit in a 26-member quantifier cluster with some, all, any, several and their own grade forms · status: analysis note, 2026-09-17 · updated: 2026-09-17 -->

Computed from `analysis/data/matrix155-lingbuzz.csv` (Reynolds 2021, public 155-feature file), Euclidean distance on binary rows, average linkage, cut at eight clusters. The matrix contains determinatives and pronouns only; it has no adjective or common-noun rows, so it cannot place either group relative to Adjective.

## Articles' cluster (18): a, a_certain, every, it_dum, last, many_a, next, no, somewhat, such, the, there, what_det, whatever_det, which_int_det, which_rel_det, whichever_int_det, whichever_rel_det

## Gradable quantifiers' cluster (26): a_few, a_great_many, a_little, all, any, both, certain, enough, few, fewer, fewest, least, less, little, many, more, most, much, one_det, several, some, sufficient, three_det, two_det, various_det, zero_det

## Features separating the two clusters (mean in articles' cluster minus mean in quantifiers' cluster)

- `functions_as_head_of_partitive_construction`: -0.89 (articles 0.11, quantifiers 1.00)
- `functions_as_fused_determiner_head`: -0.76 (articles 0.17, quantifiers 0.92)
- `functions_as_subject_of_present_participal_of_joining_you`: -0.75 (articles 0.06, quantifiers 0.81)
- `proportional`: -0.74 (articles 0.11, quantifiers 0.85)
- `compatible_count_sing_NP`: +0.72 (articles 0.83, quantifiers 0.12)
- `joint`: -0.68 (articles 0.06, quantifiers 0.73)
- `Coordinates_with_NPs`: -0.66 (articles 0.22, quantifiers 0.88)
- `anaphoric_marker`: -0.65 (articles 0.28, quantifiers 0.92)
- `distributive`: -0.62 (articles 0.11, quantifiers 0.73)
- `appears_in_existentials_there_s_on_the_table`: -0.59 (articles 0.33, quantifiers 0.92)
- `May_coordinate_with_non_fused_determiners`: -0.59 (articles 0.22, quantifiers 0.81)
- `semantically_plural`: -0.51 (articles 0.22, quantifiers 0.73)

## Nearest neighbours

- *the*: such (3.0), next (3.7), last (3.7), there (4.0), a_certain (4.0)
- *a*: a_certain (2.8), many_a (3.0), next (3.7), last (3.7), such (3.9)
- *every*: each (4.5), a_certain (4.6), one_det (4.7), many_a (4.7), next (4.8)
- *many*: few (3.3), fewer (3.9), a_great_many (3.9), three_det (4.0), fewest (4.1)
- *much*: little (3.0), most (3.7), least (3.9), a_little (4.2), less (4.4)
- *few*: fewest (2.4), fewer (2.8), many (3.3), several (3.5), most (3.9)
- *little*: much (3.0), least (3.2), a_little (3.6), less (3.7), most (3.9)

## Reading

The articles are not isolated in the matrix: they sit with *every*, *no*, *such*, exclamative *what* and the *which* determinatives in a cluster defined by dependent-only use, and *such* is *the*'s nearest neighbour. Two of that cluster's members (*such*, *what*) are adjectives in the paper's own analysis (CGEL p. 435), so the 2021 evidence for the articles' coherence with determinatives is partly coherence with a dependent-only profile that cuts across the paper's category line. The four gradable quantifiers sit inside the general quantifier cluster with *some*, *all*, *any*, *enough*, *several*; their adjectival profile is visible only in that their grade forms (*fewer*, *fewest*, *more*, *most*, *less*, *least*) are their own nearest neighbours. Nothing in the matrix separates them from the other quantifiers, and nothing in it could, since adjectives were not coded.
