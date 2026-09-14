/-
  Audit of the ordinary-Head fragment of `fragment.tex`:
  are the external use permissions of a whole NP kept separate from those of
  its embedded determining phrase?

  Standalone Lean 4, core/Std only.  No `sorry`, no new axioms.

  ---------------------------------------------------------------------------
  A. WHAT IS ENCODED, AND ON WHAT AUTHORITY
  ---------------------------------------------------------------------------

  (E) EXPLICIT SOURCE CONSTRAINTS (Table `tab:permissions`, §sec:fragment,
      §sec:det-uniform, and the closing paragraph of the source):

   E1. Use permissions are lexical, per form, over Det / Mod / Subj / Obj-CompP.
       They are transcribed verbatim in `permitted` / `formFor` below.
   E2. `no`/`none` and `my`/`mine` are one paradigm each with different forms
       selected for different functions; likewise plain `she`/`her`.
       Encoded by splitting `Lexeme` (identity) from `Form` (surface form)
       and making form selection part of admissibility.
   E3. "A permission applies to an occurrence in the specified construction.
       Intermediate Head relations within its projection don't require a
       further argument permission."  Encoded: `admissible` is evaluated at a
       phrase occurrence with the function it actually bears; the Det daughter
       is checked with function `Det`, never with the mother's function.
   E4. Target restrictions before another nominal: `the`, `no`, `my` none;
       `a`, `every` singular count; `some` plural count or non-count;
       `few` plural count.  Targets include determinative-headed nominals
       (`the few`).
   E5. "An NP core has a Nom as Head and at most one Det."  Encoded in the
       shape of the datatype: `NP.bare` / `NP.det`, one optional Det.
   E6. Primary-category condition on the word filling Head in Nom:
       D-noun requires Cat = N; separate D allows Cat ∈ {N, D}.
   E7. Lexical assignments held fixed across accounts: determinatives are
       Determinative (primary N under D-noun, primary D under separate D);
       `my`/`mine`, `she`/`her` are Pronoun, primary N in BOTH accounts;
       `apple(s)`, `book(s)` are common nouns, primary N in both.
   E8. "In `the apple` ... the outer NP has argument permission through
       `apple`, whose determination requirement is satisfied.  Bare `Book
       arrived` fails that requirement, while `Books arrived` passes.  The
       article's exclusion from argument use remains a separate condition."
       Encoded as `determinationOK`, restricted to the ordinary singular-count
       common-noun argument construction (see A2 below).
   E9. Quotation, metalinguistic naming and subordinate dependent-genitive
       uses are outside the fragment: no such use is in `Use`.

  (T) CONSEQUENCES OF THE TREE REPRESENTATION (not re-stated as conditions):
   T1. Acyclicity and unique parentage are supplied by the inductive datatype;
       they are not audited as possible omissions.
   T2. Every Nom in this fragment has exactly one lexical Head word
       (`Nom.lex`), modifier geometry being excluded.

  (A) ADDITIONAL MODELLING ASSUMPTIONS MADE HERE:
   A1. Modifier geometry (internal Mod, peripheral modification, degree
       modifiers, approximatives, partitives, relatives, compounds) is
       EXCLUDED to keep the fragment small.  `Mod` therefore appears in the
       permission table but no tree in this file contains a Mod relation, and
       NOTHING is claimed to be verified about peripheral-modifier geometry or
       the third structural condition of §sec:det-uniform.
   A2. The determination requirement is attached to the ordinary singular-count
       common-noun argument construction only, per the task's scope statement:
       it is not a requirement on every primary-Noun head (so `Some left` is
       unaffected under either account).
   A3. Number/count of a determinative-headed phrase: `few` is plural count
       (explicit in the source); `some` is left UNSPECIFIED ("takes its
       interpretation from the construction and domain"), and every other
       determinative- or pronoun-headed phrase is likewise Unspecified, since
       the source assigns it no value.  A restrictive target test fails on an
       Unspecified target rather than inventing a value.
   A4. Obj and complement-of-preposition are collapsed into one use `Obj`
       (the table gives them one column).
   A5. Lexical and constructional restrictions are held FIXED across the two
       accounts by stipulation of the task; the only thing that varies between
       the accounts is the primary category of determinatives and hence the
       Cat condition E6.  No further rule keys off primary category.
-/

namespace Fragment

/-! ## 1. Lexemes, forms, categories -/

/-- Lexeme identity (a paradigm), kept separate from surface form. -/
inductive Lexeme where
  | the | a | every | some | few
  | no          -- paradigm {no, none}
  | my          -- paradigm {my, mine}
  | she         -- paradigm {she, plain her}
  | apple | book
  deriving DecidableEq, Repr

/-- Surface forms. -/
inductive Form where
  | the | a | every | some | few
  | no | none
  | my | mine
  | she | her
  | apple | apples | book | books
  deriving DecidableEq, Repr

def allForms : List Form :=
  [.the, .a, .every, .some, .few, .no, .none, .my, .mine, .she, .her,
   .apple, .apples, .book, .books]

def lexOf : Form → Lexeme
  | .the => .the | .a => .a | .every => .every | .some => .some | .few => .few
  | .no => .no | .none => .no
  | .my => .my | .mine => .my
  | .she => .she | .her => .she
  | .apple => .apple | .apples => .apple
  | .book => .book | .books => .book

/-- Subcategory distinctions, invariant across accounts. -/
inductive Sub where
  | commonNoun | pronoun | determinative
  deriving DecidableEq, Repr

def subcat : Lexeme → Sub
  | .the | .a | .every | .some | .few | .no => .determinative
  | .my | .she => .pronoun
  | .apple | .book => .commonNoun

/-- Primary lexical category. -/
inductive Cat where
  | N | D
  deriving DecidableEq, Repr

/-- The two taxonomies being compared. -/
inductive Account where
  | dNoun | sepD
  deriving DecidableEq, Repr

/-- Primary category assignment.  Only determinatives differ between accounts;
    pronouns and common nouns are primary Noun in BOTH. -/
def primaryCat : Account → Lexeme → Cat
  | .dNoun, _ => .N
  | .sepD, l => match subcat l with
      | .determinative => .D
      | _ => .N

/-! ### Executable checks on the lexical assignments (Ground-truth table) -/

-- `my`/`mine` are Pronoun, primary Noun, in BOTH accounts.
#guard subcat (lexOf .my) == .pronoun
#guard subcat (lexOf .mine) == .pronoun
#guard lexOf .my == lexOf .mine                       -- one paradigm
#guard primaryCat .dNoun (lexOf .my) == .N
#guard primaryCat .sepD  (lexOf .my) == .N
#guard primaryCat .dNoun (lexOf .mine) == .N
#guard primaryCat .sepD  (lexOf .mine) == .N
-- `she`/plain `her`: Pronoun, primary Noun in both.
#guard primaryCat .sepD (lexOf .her) == .N
-- `no`/`none`: one paradigm, Determinative; primary D only under separate D.
#guard lexOf .no == lexOf .none
#guard primaryCat .dNoun (lexOf .none) == .N
#guard primaryCat .sepD  (lexOf .none) == .D
-- common nouns unchanged.
#guard primaryCat .sepD (lexOf .apples) == .N

theorem pronouns_primary_N_in_both (a : Account) (f : Form)
    (h : subcat (lexOf f) = Sub.pronoun) : primaryCat a (lexOf f) = Cat.N := by
  cases a with
  | dNoun => rfl
  | sepD => simp [primaryCat, h]

theorem commonNouns_primary_N_in_both (a : Account) (f : Form)
    (h : subcat (lexOf f) = Sub.commonNoun) : primaryCat a (lexOf f) = Cat.N := by
  cases a with
  | dNoun => rfl
  | sepD => simp [primaryCat, h]

/-- Exactly the determinatives change primary category between the accounts;
    the pronoun and common-noun assignments are untouched, and the subcategory
    (`subcat`) is a function of the lexeme alone, hence account-independent. -/
theorem primaryCat_differs_iff_determinative (l : Lexeme) :
    (primaryCat .dNoun l ≠ primaryCat .sepD l) ↔ subcat l = Sub.determinative := by
  cases l <;> decide

/-! ## 2. Number / count -/

inductive NumCount where
  | sgCount | plCount | nonCount | unspec
  deriving DecidableEq, Repr

/-- Number/count of the phrase headed by a form.  Determinative-headed phrases
    bear these properties too (`few` plural count); `some` and the remaining
    determinatives are left unspecified (A3). -/
def numCount : Form → NumCount
  | .apple | .book => .sgCount
  | .apples | .books => .plCount
  | .few => .plCount
  | _ => .unspec

/-! ## 3. Use permissions and form selection (Table `tab:permissions`) -/

inductive Use where
  | Det | Mod | Subj | Obj    -- Obj covers complement-of-preposition (A4)
  deriving DecidableEq, Repr

/-- Lexical use permissions, read off the table. -/
def permitted : Lexeme → Use → Bool
  | .the,   u => u == .Det
  | .a,     u => u == .Det
  | .every, u => u == .Det || u == .Mod
  | .some,  u => u == .Det || u == .Subj || u == .Obj
  | .few,   _ => true
  | .no,    u => u == .Det || u == .Subj || u == .Obj   -- Det: `no`; Subj/Obj: `none`
  | .my,    u => u == .Det || u == .Subj || u == .Obj   -- Det: `my`; Subj/Obj: `mine`
  | .she,   u => u == .Subj || u == .Obj                -- Subj: `she`; Obj: plain `her`
  | .apple, u => u == .Subj || u == .Obj
  | .book,  u => u == .Subj || u == .Obj

/-- Form selection: which form of the paradigm the function selects.
    (`none`, `mine` independent; `no`, `my` before another nominal.)
    Common nouns select by number, so both forms are available. -/
def formSelected : Lexeme → Use → Form → Bool
  | .the,   _, f => f == .the
  | .a,     _, f => f == .a
  | .every, _, f => f == .every
  | .some,  _, f => f == .some
  | .few,   _, f => f == .few
  | .no,    u, f => if u == .Det || u == .Mod then f == .no else f == .none
  | .my,    u, f => if u == .Det || u == .Mod then f == .my else f == .mine
  | .she,   u, f => if u == .Subj then f == .she else f == .her
  | .apple, _, f => f == .apple || f == .apples
  | .book,  _, f => f == .book || f == .books

/-- Target restriction imposed by a determining form on the nominal it
    determines (Table, last column). -/
def targetOK : Form → NumCount → Bool
  | .the, _ => true
  | .no,  _ => true
  | .my,  _ => true
  | .a,     n => n == .sgCount
  | .every, n => n == .sgCount
  | .some,  n => n == .plCount || n == .nonCount
  | .few,   n => n == .plCount
  | _, _ => false      -- forms with no Det permission never reach this test

/-! ## 4. Constituents: NP and Nom with Head and Det relations -/

/-- A Nom whose Head is filled directly by a word occurrence.
    Modifier geometry excluded (A1), so this is the only Nom shape. -/
inductive Nom where
  | lex : Form → Nom
  deriving DecidableEq, Repr

/-- An NP core: a Nom as Head, and at most one Det, which is itself an NP. -/
inductive NP where
  | bare : Nom → NP                 -- Head Nom, no Det
  | det  : NP → Nom → NP            -- Det daughter, Head Nom
  deriving DecidableEq, Repr

def Nom.head : Nom → Form | .lex f => f

/-- The lexical head of an NP is the lexical head of its Head Nom. -/
def NP.head : NP → Form
  | .bare n => n.head
  | .det _ n => n.head

def NP.hasDet : NP → Bool
  | .bare _ => false
  | .det _ _ => true

/-- Primary-category condition on the word filling Head in Nom (E6). -/
def catOK (a : Account) (n : Nom) : Bool :=
  match a with
  | .dNoun => primaryCat .dNoun (lexOf n.head) == .N
  | .sepD  => primaryCat .sepD (lexOf n.head) == .N
              || primaryCat .sepD (lexOf n.head) == .D

/-- The determination requirement of §sec:fragment: an ordinary singular-count
    common noun heading an argument NP requires a Det (A2). -/
def determinationOK (x : NP) : Bool :=
  if subcat (lexOf x.head) == .commonNoun && numCount x.head == .sgCount then
    x.hasDet
  else
    true

/-- `admissible a x f`: phrase occurrence `x` bearing external/internal
    function `f`.  Three checks, as in the source:
    permission for the use, selection of the form, and the constructional
    conditions `C` (here: well-formedness of `x`, plus the determination
    requirement at an argument occurrence).
    The target condition is checked at the attachment site, where the target
    is visible. -/
def wf (a : Account) : NP → Bool
  | .bare nm => catOK a nm
  | .det d nm =>
      catOK a nm
      -- the Det daughter is checked with function `Det` — never with the
      -- mother's function.  This is where E3 is enforced.
      && wf a d
      && permitted (lexOf d.head) .Det
      && formSelected (lexOf d.head) .Det d.head
      && targetOK d.head (numCount nm.head)

def admissible (a : Account) (x : NP) (f : Use) : Bool :=
  wf a x
  && permitted (lexOf x.head) f
  && formSelected (lexOf x.head) f x.head
  && (match f with
      | .Subj | .Obj => determinationOK x
      | _ => true)

/-! ## 5. The source-grounded cases -/

def n (f : Form) : Nom := .lex f
def lexNP (f : Form) : NP := .bare (n f)
def detNP (d : NP) (f : Form) : NP := .det d (n f)

def theP   : NP := lexNP .the        -- the smaller article phrase
def theApple : NP := detNP theP .apple
def someP  : NP := lexNP .some
def everyP : NP := lexNP .every
def bookP  : NP := lexNP .book
def booksP : NP := lexNP .books
def everyApple : NP := detNP everyP .apple
def someApples : NP := detNP (lexNP .some) .apples

-- `the apple` is admissible as an argument, under both accounts.
theorem the_apple_subj_dNoun : admissible .dNoun theApple .Subj = true := by decide
theorem the_apple_subj_sepD  : admissible .sepD  theApple .Subj = true := by decide
theorem the_apple_obj        : admissible .dNoun theApple .Obj = true := by decide

-- `Some left`: independent subject use of `some`.
theorem some_subj_dNoun : admissible .dNoun someP .Subj = true := by decide
theorem some_subj_sepD  : admissible .sepD  someP .Subj = true := by decide

-- `*Every arrived`: rejected, by use permission.
theorem every_subj_rejected_dNoun : admissible .dNoun everyP .Subj = false := by decide
theorem every_subj_rejected_sepD  : admissible .sepD  everyP .Subj = false := by decide

-- `*Book arrived`: rejected, by the determination requirement.
theorem book_subj_rejected : admissible .dNoun bookP .Subj = false := by decide
theorem book_subj_rejected_sepD : admissible .sepD bookP .Subj = false := by decide
-- and it is the determination requirement, not the use permission, that fails:
theorem book_has_subj_permission : permitted (lexOf .book) .Subj = true := by decide
theorem book_determination_fails : determinationOK bookP = false := by decide

-- `Books arrived`: accepted.
theorem books_subj : admissible .dNoun booksP .Subj = true := by decide
theorem books_subj_sepD : admissible .sepD booksP .Subj = true := by decide

-- Dependent checks on `every apple` and `some apples`; target restrictions bite.
theorem every_apple_wf : wf .dNoun everyApple = true := by decide
theorem every_apples_ill : wf .dNoun (detNP everyP .apples) = false := by decide
theorem some_apples_wf : wf .dNoun someApples = true := by decide
theorem some_apple_ill : wf .dNoun (detNP (lexNP .some) .apple) = false := by decide
theorem a_apples_ill : wf .dNoun (detNP (lexNP .a) .apples) = false := by decide
-- `the few`: a determinative-headed target, licensed because `the` is unrestricted.
theorem the_few_wf : wf .dNoun (detNP theP .few) = true := by decide

/-! ## 6. The permission-separation question -/

/-- Admitting `the apple` as an argument gives the embedded article phrase no
    independent argument use: the article phrase is rejected as Subj and Obj,
    under both accounts, for every NP it heads. -/
theorem article_phrase_never_argument (a : Account) (x : NP) (h : x.head = Form.the) :
    admissible a x .Subj = false ∧ admissible a x .Obj = false := by
  constructor <;> simp [admissible, h, lexOf, permitted]

theorem the_apple_arg_but_article_phrase_not :
    admissible .dNoun theApple .Subj = true
    ∧ admissible .dNoun theP .Subj = false
    ∧ admissible .dNoun theP .Obj = false := by decide

/-- A Det daughter has to satisfy its Det permission and its own internal
    well-formedness, and nothing else: occurring inside an argument NP imposes
    no argument permission on it. -/
theorem det_daughter_needs_only_det_permission
    (a : Account) (d : NP) (m : Form) (h : wf a (detNP d m) = true) :
    permitted (lexOf d.head) Use.Det = true
    ∧ formSelected (lexOf d.head) Use.Det d.head = true
    ∧ wf a d = true := by
  unfold wf detNP Fragment.n at h
  simp only [Bool.and_eq_true] at h
  exact ⟨h.1.1.2, h.1.2, h.1.1.1.2⟩

/-- No inheritance upwards: a mother's argument permission is not obtained
    from its Det daughter.  `the apple` is an admissible subject although its
    Det daughter has no Subj permission; and a Det daughter with a Subj
    permission does not confer one on a mother that lacks it. -/
theorem mother_permission_not_from_daughter :
    -- mother admitted, daughter not:
    admissible .dNoun theApple .Subj = true
    ∧ admissible .dNoun theP .Subj = false
    -- daughter admitted, mother not (`*some book` as subject: `some` is a
    -- fine subject on its own, but the mother fails its own conditions):
    ∧ admissible .dNoun someP .Subj = true
    ∧ admissible .dNoun (detNP someP .book) .Subj = false := by decide

/-- An intermediate Head relation creates no further argument requirement:
    whether `x` is admitted under an argument function depends only on `x`'s
    own head, form, well-formedness and determination, never on an argument
    permission for any daughter. -/
theorem no_extra_argument_requirement (a : Account) (d : NP) (m : Form) :
    admissible a (detNP d m) .Subj =
      (wf a (detNP d m)
        && permitted (lexOf m) .Subj
        && formSelected (lexOf m) .Subj m
        && determinationOK (detNP d m)) := by
  rfl

/-! ## 7. Recategorization equivalence (secondary consistency check) -/

theorem catOK_always (a : Account) (nm : Nom) : catOK a nm = true := by
  cases a
  · cases nm with | lex f => cases f <;> rfl
  · cases nm with | lex f => cases f <;> rfl

theorem wf_account_invariant (a b : Account) : ∀ x : NP, wf a x = wf b x := by
  intro x
  induction x with
  | bare nm => simp [wf, catOK_always]
  | det d nm ih => simp [wf, catOK_always, ih]

/-- With the lexical and constructional restrictions held fixed (A5), the two
    primary classifications admit exactly the same trees under exactly the same
    functions. -/
theorem admissible_account_invariant (a b : Account) (x : NP) (f : Use) :
    admissible a x f = admissible b x f := by
  simp [admissible, wf_account_invariant a b x]

/-! ## 8. Exhaustive search for unintended admissions / rejections -/

def allNoms : List Nom := allForms.map Nom.lex

def depth1 : List NP := allNoms.map NP.bare
def depth2 : List NP := depth1.flatMap (fun d => allNoms.map (fun m => NP.det d m))
def depth3 : List NP := depth2.flatMap (fun d => allNoms.map (fun m => NP.det d m))
def allTrees : List NP := depth1 ++ depth2 ++ depth3

/-- Every tree in the enumeration behaves identically under the two accounts,
    for every function. -/
theorem search_account_invariant :
    allTrees.all (fun x => [Use.Det, .Mod, .Subj, .Obj].all
      (fun f => admissible .dNoun x f == admissible .sepD x f)) = true := by
  rw [List.all_eq_true]
  intro x _
  rw [List.all_eq_true]
  intro f _
  simp only [beq_iff_eq]
  exact admissible_account_invariant _ _ _ _

/-- No tree admitted as an argument has a `the`-headed Det daughter that is
    itself admissible as an argument. -/
def noArticleLeak : Bool :=
  (depth1 ++ depth2).all fun x =>
    match x with
    | .det d _ => !(admissible .dNoun d .Subj || admissible .dNoun d .Obj)
                  || !(d.head == Form.the)
    | _ => true

theorem no_article_leak : noArticleLeak = true := by decide

/-- Trees admitted as subjects, for inspection. -/
def render : NP → String
  | .bare nm => toString (repr nm.head)
  | .det d nm => render d ++ " " ++ toString (repr nm.head)

def admittedSubjects : List String :=
  (depth1 ++ depth2).filter (fun x => admissible .dNoun x .Subj) |>.map render

#eval admittedSubjects.length
#eval admittedSubjects

/-! ### The smallest unintended admissions found

    Every condition on these witnesses is displayed below, and every feature
    value used is one the source supplies; none was chosen to obtain a witness.

    They do NOT bear on permission separation, which §6 establishes.  They
    isolate a different gap: the fragment states the condition on a Det's
    target in count/number terms only (Table, last column) and explicitly
    extends it to determinative-headed targets (`the few`), but states no
    condition on the *category* of the target's head.  So an unrestricted
    determiner (`the`, `no`, `my`: "No count or number restriction") admits a
    pronoun-headed target, and `few` (explicitly plural count as a Det target
    restriction, and explicitly plural count as a phrase head) admits itself. -/

/-- Witness 1, two words: `*few few`.  Conditions, all source-supplied:
    `few` has Det permission; its selected Det form is `few`; its target
    restriction is plural count; the target nominal is headed by `few`, which
    the source states to be plural count.  Hence admitted, under both
    accounts, in Det, Subj and Obj function. -/
theorem overgeneration_few_few :
    permitted (lexOf .few) Use.Det = true
    ∧ formSelected (lexOf .few) Use.Det Form.few = true
    ∧ targetOK Form.few (numCount Form.few) = true
    ∧ numCount Form.few = NumCount.plCount
    ∧ wf .dNoun (detNP (lexNP .few) .few) = true
    ∧ admissible .dNoun (detNP (lexNP .few) .few) .Subj = true
    ∧ admissible .sepD (detNP (lexNP .few) .few) .Subj = true := by decide

/-- Witness 2, two words: `*the she` (likewise `*my mine`, `*no none`).
    `the` has Det permission and, per the table, "No count or number
    restriction", so its target test succeeds on any target, including a
    nominal headed by a pronoun.  The number/count of the pronoun-headed
    phrase is left unspecified (A3) and is not what admits the tree: the
    admission comes from `the` imposing no restriction at all. -/
theorem overgeneration_the_she :
    targetOK Form.the (numCount Form.she) = true
    ∧ subcat (lexOf .she) = Sub.pronoun
    ∧ wf .dNoun (detNP theP .she) = true
    ∧ admissible .dNoun (detNP theP .she) .Subj = true
    ∧ admissible .sepD (detNP theP .she) .Subj = true := by decide

/-- The same gap admits the two forms of one paradigm together: `*my mine`
    and `*no none`. -/
theorem overgeneration_my_mine :
    lexOf .my = lexOf .mine
    ∧ admissible .dNoun (detNP (lexNP .my) .mine) .Subj = true
    ∧ admissible .dNoun (detNP (lexNP .no) .none) .Subj = true := by decide

/-- By contrast the source's own licensed case `the few` is admitted, and the
    ungrammatical count/number mismatches are correctly excluded, so the gap is
    specific to the missing category condition on the target. -/
theorem target_count_conditions_do_bite :
    wf .dNoun (detNP theP .few) = true
    ∧ wf .dNoun (detNP (lexNP .a) .apples) = false
    ∧ wf .dNoun (detNP (lexNP .every) .apples) = false
    ∧ wf .dNoun (detNP (lexNP .some) .apple) = false
    ∧ wf .dNoun (detNP (lexNP .few) .apple) = false := by decide

/-! ### The missing condition, and a candidate repair

    The gap is that `targetOK` (the Table's last column) is the only condition
    on a target, and it is purely count/number.  The source's prose does supply
    the missing material, but the fragment's stated conditions do not encode it:

      • "In Det or internal Mod function before a target, ordinary `some` and
        `few` exclude external determination ...  Independent `some` and `few`
        permit selected partitives and relatives; independent `few` also
        permits *definite* determination, as in `the lucky few`.  These
        permissions don't transfer to `every` or the articles."
      • Pronoun-headed nominals are never given a Det in the fragment.

    Formalised as a condition on the target's head, this is: -/

/-- `the` and the dependent genitive `my` are the definite determiners of the
    encoded fragment. -/
def definiteDeterminer : Form → Bool
  | .the | .my => true
  | _ => false

/-- Proposed extra condition on an attachment: a determinative-headed target
    must be `few`, and then only under definite determination; a pronoun-headed
    target admits no Det at all. -/
def targetAcceptsDet (d : Form) (t : Form) : Bool :=
  match subcat (lexOf t) with
  | .commonNoun => true
  | .pronoun => false
  | .determinative => (lexOf t == Lexeme.few) && definiteDeterminer d

/-- Well-formedness with the proposed condition added. -/
def wfRepaired (a : Account) : NP → Bool
  | .bare nm => catOK a nm
  | .det d nm =>
      catOK a nm
      && wfRepaired a d
      && permitted (lexOf d.head) .Det
      && formSelected (lexOf d.head) .Det d.head
      && targetOK d.head (numCount nm.head)
      && targetAcceptsDet d.head nm.head

/-- The proposed condition removes exactly the unintended admissions above and
    retains every case the source licenses. -/
theorem repair_effect :
    -- removed
    wfRepaired .dNoun (detNP (lexNP .few) .few) = false
    ∧ wfRepaired .dNoun (detNP theP .she) = false
    ∧ wfRepaired .dNoun (detNP (lexNP .my) .mine) = false
    ∧ wfRepaired .dNoun (detNP (lexNP .no) .none) = false
    ∧ wfRepaired .dNoun (detNP theP .some) = false
    -- retained
    ∧ wfRepaired .dNoun (detNP theP .few) = true
    ∧ wfRepaired .dNoun theApple = true
    ∧ wfRepaired .dNoun everyApple = true
    ∧ wfRepaired .dNoun someApples = true
    ∧ wfRepaired .dNoun (detNP (lexNP .my) .books) = true := by decide

/-- The repair is itself account-invariant, so it does not disturb §7. -/
theorem wfRepaired_account_invariant (a b : Account) : ∀ x : NP, wfRepaired a x = wfRepaired b x := by
  intro x
  induction x with
  | bare nm => simp [wfRepaired, catOK_always]
  | det d nm ih => simp [wfRepaired, catOK_always, ih]

/-- The determining forms that can head a phrase admitted as an argument are
    exactly those the table gives a Subj/Obj permission, in the selected
    independent form. -/
theorem argument_heads_are_table_heads (x : NP) (a : Account) :
    admissible a x .Subj = true → permitted (lexOf x.head) .Subj = true := by
  intro h
  unfold admissible at h
  simp only [Bool.and_eq_true] at h
  exact h.1.1.2

end Fragment

/-! ## 9. Axiom audit -/

#print axioms Fragment.admissible_account_invariant
#print axioms Fragment.article_phrase_never_argument
#print axioms Fragment.no_article_leak
#print axioms Fragment.overgeneration_few_few
#print axioms Fragment.repair_effect
