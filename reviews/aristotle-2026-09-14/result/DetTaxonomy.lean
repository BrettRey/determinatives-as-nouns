/-
  A bounded audit of the recategorization claim in `fragment.tex`.

  Two ordinary-Head implementations are compared:

    * D-noun:     the word occurrence filling Head in Nom must have `Cat h = N`,
                  determinatives being a *subcategory* of Noun;
    * Separate D: that occurrence must have `Cat h ∈ {N, D}`,
                  determinatives forming a separate primary category.

  Everything else the fragment states (lexeme-level use permissions, form
  selection, target/dependent conditions, the at-most-one-Det restriction, the
  internal/peripheral modifier boundary) is held fixed across the two accounts,
  and is therefore represented once, as shared data/parameters whose invariance
  under recategorization is exactly the named hypothesis.  The two grammars are
  *not* defined by one predicate: each has its own `Cat` function and its own
  head-category condition, and the equality of those conditions is the thing
  that is proved.

  Self-contained: core Lean 4 only, no Mathlib, no `sorry`, no new axioms.
-/

namespace DetTaxonomy

/-! ## Primary categories, lexemes, forms, functions -/

inductive Prim | N | D
  deriving DecidableEq, Repr

/-- Lexemes of the fragment.  `noL` is the lexeme with forms *no*/*none*;
`myL` the lexeme with forms *my*/*mine*; `sheL` the lexeme *she*/*her*. -/
inductive Lexeme
  | theL | aL | everyL | someL | fewL | noL | myL | sheL | appleL | bookL
  deriving DecidableEq, Repr

/-- Surface forms, kept distinct from lexemes (the *no*/*none*, *my*/*mine*,
*she*/*her* contrasts are form selection, not use permission). -/
inductive Form
  | the | a | every | some | few | no | none | my | mine | she | her
  | apple | apples | book | books
  deriving DecidableEq, Repr

/-- External functions covered by the fragment.  `Obj` covers object and
complement-of-preposition; `Mod` is internal modification before a target. -/
inductive Func | Det | Mod | Subj | Obj
  deriving DecidableEq, Repr

def Form.lexeme : Form → Lexeme
  | .the => .theL | .a => .aL | .every => .everyL | .some => .someL
  | .few => .fewL | .no => .noL | .none => .noL | .my => .myL | .mine => .myL
  | .she => .sheL | .her => .sheL
  | .apple => .appleL | .apples => .appleL | .book => .bookL | .books => .bookL

/-- Determinative lexemes of the fragment.  This is the *only* classification
that the two taxonomies treat differently. -/
def Lexeme.isDeterminative : Lexeme → Bool
  | .theL | .aL | .everyL | .someL | .fewL | .noL | .myL => true
  | .sheL | .appleL | .bookL => false

/-! ## The two taxonomies -/

/-- D-noun: every lexical head of a Nom is a Noun (determinatives included, as
a Noun subcategory). -/
def cat1 (_ : Lexeme) : Prim := Prim.N

/-- Separate D: determinatives are a distinct primary category. -/
def cat2 (l : Lexeme) : Prim := if l.isDeterminative then Prim.D else Prim.N

/-- D-noun head condition: `Cat h = N`. -/
def headOK1 (l : Lexeme) : Bool := cat1 l == Prim.N

/-- Separate-D head condition: `Cat h ∈ {N, D}`. -/
def headOK2 (l : Lexeme) : Bool := cat2 l == Prim.N || cat2 l == Prim.D

/-! ## Shared, explicitly stated lexical restrictions

Use permissions are lexeme-level; form selection is separate. -/

/-- `U ℓ` of the fragment's Table 1, read off the rows lexeme-wise. -/
def uses : Lexeme → Func → Bool
  | .theL,  f => f == .Det
  | .aL,    f => f == .Det
  | .everyL, f => f == .Det || f == .Mod
  | .someL, f => f == .Det || f == .Subj || f == .Obj
  | .fewL,  f => f == .Det || f == .Mod || f == .Subj || f == .Obj
  | .noL,   f => f == .Det || f == .Subj || f == .Obj   -- *no* / *none*
  | .myL,   f => f == .Det || f == .Subj || f == .Obj   -- *my* / *mine*
  | .sheL,  f => f == .Subj || f == .Obj                -- *she* / plain *her*
  | .appleL, f => f == .Subj || f == .Obj
  | .bookL,  f => f == .Subj || f == .Obj

/-- Form selection inside a paradigm: which form realises which function. -/
def formOK : Form → Func → Bool
  | .no,   f => f == .Det
  | .none, f => f == .Subj || f == .Obj
  | .my,   f => f == .Det
  | .mine, f => f == .Subj || f == .Obj
  | .she,  f => f == .Subj
  | .her,  f => f == .Obj
  | g,     f => uses g.lexeme f

/-! ## Occurrences -/

/-- A phrase occurrence, recording only what the audited conditions inspect. -/
structure Occ where
  form      : Form
  func      : Func
  /-- number of Det dependents in the occurrence's own core -/
  detCount  : Nat
  /-- is the occurrence itself singular count? -/
  sgCount   : Bool
  /-- is a peripheral modifier attached to an NP whose Head relation
      continues to an NP (as opposed to inside the core)? -/
  peripheralOK : Bool
  deriving Repr

def Occ.lexeme (o : Occ) : Lexeme := o.form.lexeme

/-- The structural conditions the fragment states for *both* ordinary-Head
accounts: at most one Det per NP core, and the internal/peripheral modifier
boundary. -/
def structuralOK (o : Occ) : Bool := o.detCount ≤ 1 && o.peripheralOK

/- `C` of the fragment: target and dependent conditions, left as a parameter.
   Its invariance under recategorization is the named assumption: the *same*
   `C` is used by both grammars below. -/
variable (C : Occ → Bool)

/-- Shared checks: use permission, form selection, structural conditions, `C`. -/
def shared (o : Occ) : Bool :=
  uses o.lexeme o.func && formOK o.form o.func && structuralOK o && C o

/-- Admissibility under D-noun. -/
def adm1 (o : Occ) : Bool := headOK1 o.lexeme && shared C o

/-- Admissibility under separate D. -/
def adm2 (o : Occ) : Bool := headOK2 o.lexeme && shared C o

/-! ## Result 1: the head-category conditions coincide, hence so do the grammars -/

theorem headOK_agree (l : Lexeme) : headOK1 l = headOK2 l := by
  cases l <;> rfl

/-- Equivalence under recategorization, given that all other conditions are
lexeme/subcategory-indexed (encoded by both grammars using the same `uses`,
`formOK`, `structuralOK` and the same parameter `C`).  The proof is a case
split on the lexeme: it is essentially definitional. -/
theorem adm_equiv (o : Occ) : adm1 C o = adm2 C o := by
  simp [adm1, adm2, headOK_agree]

/-! ## Result 2: the invariance assumption is load-bearing

The fragment states "A singular count noun normally requires determination".
It does not say whether that condition is indexed by the *primary* category N
or by the noun subcategory that excludes determinatives.  Under the primary-
category reading the two accounts come apart, because under D-noun a
determinative-headed phrase *is* an N. -/

/-- Determination requirement, read as indexed by the primary category. -/
def detReqPrim (c : Prim) (o : Occ) : Bool :=
  !(c == Prim.N && o.sgCount && o.detCount == 0)

def adm1' (o : Occ) : Bool :=
  headOK1 o.lexeme && detReqPrim (cat1 o.lexeme) o && shared C o

def adm2' (o : Occ) : Bool :=
  headOK2 o.lexeme && detReqPrim (cat2 o.lexeme) o && shared C o

/-- General form of the divergence: any undetermined singular-count occurrence
with a determinative head that passes the shared checks is admitted by
separate D and rejected by D-noun. -/
theorem divergence_general (o : Occ)
    (hdet : o.lexeme.isDeterminative = true)
    (hsg : o.sgCount = true) (hnodet : o.detCount = 0)
    (hsh : shared C o = true) :
    adm1' C o = false ∧ adm2' C o = true := by
  constructor
  · simp [adm1', headOK1, cat1, detReqPrim, hsg, hnodet]
  · simp [adm2', headOK2, cat2, detReqPrim, hdet, hsh]

/-- A concrete witness: independent subject *some* construed as singular
(`Some was left`), with no Det of its own. -/
def someSubj : Occ :=
  { form := .some, func := .Subj, detCount := 0, sgCount := true,
    peripheralOK := true }

theorem divergence_witness (hC : C someSubj = true) :
    adm1' C someSubj = false ∧ adm2' C someSubj = true :=
  divergence_general C someSubj rfl rfl rfl (by simp [shared, structuralOK, hC]; decide)

/-- And the two grammars really do differ on it, unlike in Result 1. -/
theorem adm'_not_equiv (hC : C someSubj = true) :
    adm1' C someSubj ≠ adm2' C someSubj := by
  have h := divergence_witness C hC
  rw [h.1, h.2]; exact Bool.noConfusion

end DetTaxonomy
