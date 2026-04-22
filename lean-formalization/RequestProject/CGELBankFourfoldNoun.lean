import Mathlib

/-!
# CGELBank Fourfold Noun

This file is a narrow formalization target for CGEL's category-function architecture.
The intended scope is:

- the fourfold-Noun superordinate
- purpose-relative projectibility for the four sub-clusters
- noun-headed determiner uniformity
- category/function overlap without collapse
-/

namespace CGELBank

inductive LexCat where
  | commonNoun
  | properNoun
  | pronoun
  | determinative
deriving DecidableEq, Repr, Fintype

inductive SuperCat where
  | noun
deriving DecidableEq, Repr, Fintype

inductive SyntacticFunction where
  | det
  | head
  | mod
  | subj
  | obj
  | compOfPrep
deriving DecidableEq, Repr, Fintype

inductive PhraseCat where
  | np
  | pp
deriving DecidableEq, Repr, Fintype

inductive Purpose where
  | distributional
  | naming
  | anaphoric
  | modificational
  | detFunction
  | nominalProjection
deriving DecidableEq, Repr, Fintype

inductive Feature where
  | descriptive
  | nameLike
  | anaphoric
  | caseInflected
  | fillsDet
  | takesAdvPModifier
  | takesAdjPModifier
  | headsNP
  | referenceManaging
deriving DecidableEq, Repr, Fintype

inductive Item where
  | dog
  | water
  | kim
  | toronto
  | she
  | who
  | some
  | every
  | the
  | my
  | kimGen
deriving DecidableEq, Repr, Fintype

structure Grammar where
  member : Item → LexCat → Prop
  fills : Item → SyntacticFunction → Prop
  projectsTo : Item → PhraseCat → Prop
  hasFeature : Item → Feature → Prop
  subcatOf : LexCat → SuperCat → Prop

def nounSubcategory : LexCat → Prop
  | .commonNoun => True
  | .properNoun => True
  | .pronoun => True
  | .determinative => True

def itemIsNoun (G : Grammar) (x : Item) : Prop :=
  ∃ C, G.member x C ∧ nounSubcategory C

def projectibleForCategory
    (G : Grammar) (C : LexCat) (_P : Purpose) (fs : Set Feature) : Prop :=
  ∀ f ∈ fs, ∀ x, G.member x C → G.hasFeature x f

def projectibleForFunction
    (G : Grammar) (F : SyntacticFunction) (_P : Purpose) (fs : Set Feature) : Prop :=
  ∀ f ∈ fs, ∀ x, G.fills x F → G.hasFeature x f

def nounHeadedDetFiller (G : Grammar) (x : Item) : Prop :=
  G.fills x .det ∧ G.projectsTo x .np

def HPCConsistent (G : Grammar) (C : LexCat) (F : SyntacticFunction) : Prop :=
  ∃ catFs funFs : Finset Feature,
    projectibleForCategory G C .nominalProjection (catFs : Set Feature) ∧
    projectibleForFunction G F .detFunction (funFs : Set Feature) ∧
    (∃ x, G.member x C ∧ G.fills x F) ∧
    catFs ≠ funFs

namespace Witness

def member : Item → LexCat → Prop
  | .dog, .commonNoun => True
  | .water, .commonNoun => True
  | .kim, .properNoun => True
  | .toronto, .properNoun => True
  | .kimGen, .properNoun => True
  | .she, .pronoun => True
  | .who, .pronoun => True
  | .some, .determinative => True
  | _, _ => False

def fills : Item → SyntacticFunction → Prop
  | .dog, .head => True
  | .water, .head => True
  | .kim, .head => True
  | .toronto, .head => True
  | .she, .head => True
  | .who, .head => True
  | .some, .det => True
  | .kimGen, .det => True
  | _, _ => False

def projectsTo : Item → PhraseCat → Prop
  | .dog, .np => True
  | .water, .np => True
  | .kim, .np => True
  | .toronto, .np => True
  | .she, .np => True
  | .who, .np => True
  | .some, .np => True
  | .kimGen, .np => True
  | _, _ => False

def hasFeature : Item → Feature → Prop
  | .dog, .descriptive => True
  | .dog, .takesAdjPModifier => True
  | .dog, .headsNP => True
  | .water, .descriptive => True
  | .water, .takesAdjPModifier => True
  | .water, .headsNP => True
  | .kim, .nameLike => True
  | .kim, .headsNP => True
  | .toronto, .nameLike => True
  | .toronto, .headsNP => True
  | .kimGen, .nameLike => True
  | .kimGen, .headsNP => True
  | .kimGen, .fillsDet => True
  | .she, .anaphoric => True
  | .she, .caseInflected => True
  | .she, .headsNP => True
  | .who, .anaphoric => True
  | .who, .caseInflected => True
  | .who, .headsNP => True
  | .some, .fillsDet => True
  | .some, .takesAdvPModifier => True
  | .some, .referenceManaging => True
  | _, _ => False

def subcatOf : LexCat → SuperCat → Prop
  | _, .noun => True

def grammar : Grammar where
  member := member
  fills := fills
  projectsTo := projectsTo
  hasFeature := hasFeature
  subcatOf := subcatOf

end Witness

theorem T0_fourfold_noun_superordinate :
    Witness.grammar.subcatOf .commonNoun .noun ∧
    Witness.grammar.subcatOf .properNoun .noun ∧
    Witness.grammar.subcatOf .pronoun .noun ∧
    Witness.grammar.subcatOf .determinative .noun := by
  simp [Witness.grammar, Witness.subcatOf]

theorem T1_distinct_field_relative_projectibility_profiles :
    projectibleForCategory Witness.grammar .commonNoun .distributional
      {Feature.descriptive, Feature.takesAdjPModifier, Feature.headsNP} ∧
    projectibleForCategory Witness.grammar .properNoun .naming
      {Feature.nameLike, Feature.headsNP} ∧
    projectibleForCategory Witness.grammar .pronoun .anaphoric
      {Feature.anaphoric, Feature.caseInflected, Feature.headsNP} ∧
    projectibleForCategory Witness.grammar .determinative .modificational
      {Feature.fillsDet, Feature.takesAdvPModifier, Feature.referenceManaging} ∧
    ¬ projectibleForCategory Witness.grammar .commonNoun .anaphoric
      {Feature.anaphoric, Feature.caseInflected, Feature.headsNP} ∧
    ¬ projectibleForCategory Witness.grammar .pronoun .modificational
      {Feature.fillsDet, Feature.takesAdvPModifier, Feature.referenceManaging} := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_⟩
  · intro f hf x hx
    cases x <;> cases f <;>
      simp [Witness.grammar, Witness.member, Witness.hasFeature] at hf hx ⊢
  · intro f hf x hx
    cases x <;> cases f <;>
      simp [Witness.grammar, Witness.member, Witness.hasFeature] at hf hx ⊢
  · intro f hf x hx
    cases x <;> cases f <;>
      simp [Witness.grammar, Witness.member, Witness.hasFeature] at hf hx ⊢
  · intro f hf x hx
    cases x <;> cases f <;>
      simp [Witness.grammar, Witness.member, Witness.hasFeature] at hf hx ⊢
  · intro h
    have hDog := h Feature.anaphoric (by simp) Item.dog (by simp [Witness.grammar, Witness.member])
    simp [Witness.grammar, Witness.hasFeature] at hDog
  · intro h
    have hShe := h Feature.fillsDet (by simp) Item.she (by simp [Witness.grammar, Witness.member])
    simp [Witness.grammar, Witness.hasFeature] at hShe

theorem T2_noun_headed_det_fillers_are_nouns :
    ∀ x, nounHeadedDetFiller Witness.grammar x → itemIsNoun Witness.grammar x := by
  intro x hx
  cases x <;>
    simp [nounHeadedDetFiller, itemIsNoun, Witness.grammar, Witness.member, Witness.fills,
      Witness.projectsTo, nounSubcategory] at hx ⊢
  case some =>
    exact ⟨.determinative, by simp⟩
  case kimGen =>
    exact ⟨.properNoun, by simp⟩

theorem T3_category_function_architecture_is_hpc_consistent :
    HPCConsistent Witness.grammar .determinative .det := by
  refine ⟨{Feature.fillsDet, Feature.takesAdvPModifier, Feature.referenceManaging},
    {Feature.fillsDet}, ?_, ?_, ?_, ?_⟩
  · intro f hf x hx
    cases x <;> cases f <;>
      simp [Witness.grammar, Witness.member, Witness.hasFeature] at hf hx ⊢
  · intro f hf x hx
    cases x <;> cases f <;>
      simp [Witness.grammar, Witness.fills, Witness.hasFeature] at hf hx ⊢
  · refine ⟨.some, ?_, ?_⟩ <;> simp [Witness.grammar, Witness.member, Witness.fills]
  · intro h
    have hmem : Feature.takesAdvPModifier ∈
        ({Feature.fillsDet, Feature.takesAdvPModifier, Feature.referenceManaging} : Finset Feature) := by
      simp
    simp [h] at hmem

end CGELBank
