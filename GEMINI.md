# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Academic paper by Brett Reynolds. Working title: "Determinatives as nouns."

### Core thesis

The paper argues for a superordinate **Noun** category with four sub-categories:

1. **Common noun** (*dog, water, idea*)
2. **Proper noun** (*Brett, Toronto*)
3. **Pronoun** (*she, who, something*)
4. **Determinative** (*the, a, this, some, every*)

That is, determinatives are a *kind of noun*, alongside the other three. This revises the standard CGEL (Huddleston & Pullum) taxonomy, which treats determinative as a distinct lexical category at the same level as noun. The move here is *not* Abney's DP hypothesis (which makes D the head of a DP); the categorial function distinction is preserved, and "the dog" remains an NP with a DP in determiner function. What changes is the superordinate classification: all four subcategories live under a broader Noun.

### Related work (Brett's own)

- *Quantifying the differences between lexical categories: The case of pronouns and determinatives in English* (2021, *Cadernos de Linguística*) — showed distributional distance between pronouns and determinatives. This paper has to explain how such distance is compatible with their both being nouns.
- *Full matrix of English determinative and pronoun features* (2021, LingBuzz 005747) — the feature-matrix the present paper should build on.
- *Determiners, feline marsupials, and the category-function distinction* (2013, TESL Canada) — early statement of the category/function distinction.
- *Determinatives again* (2014, TESL Canada) — follow-up.
- *The lexicon-syntax boundary in English numerals* (2026, *English Language and Linguistics*) — numerals sit on a lexicon-syntax spectrum; cardinals pattern nominally in several constructions. Open question for this paper: are numerals a fifth noun sub-category, a nominal use of a separate numerative category, or something else? Either outcome affects the superordinate-Noun argument.
- HPC book, Ch 11 (lexical categories) — the superordinate-category move should be consistent with the book's HPC-profile framing.
- HPC book, Ch 12 (pro-form gender) — pronoun-specific properties that distinguish the pronoun sub-cluster.

### HPC angle (probably load-bearing)

On an HPC reading: Noun is an HPC kind with a profile (clustered properties) stabilised by mechanisms (acquisition, entrenchment, interactive alignment, iterated transmission). The four sub-categories are sub-clusters of the same kind — they share the Noun-level profile but have distinct additional properties stabilised by subtype-specific mechanisms. This is consistent with Boyd's homeostasis-at-multiple-scales view.

### Status

- 2026-04-20: Project created. Empty `main.tex`. No draft yet.
- GitHub remote pending.

## Build System

## Build System

This LaTeX project requires **XeLaTeX** (not pdfLaTeX) due to the Charis SIL font requirement.

**Avoid LuaLaTeX** – it tends to run words together in the underlying PDF text layer, breaking copy-paste and accessibility.

### Compilation Commands

```bash
# Full build sequence
xelatex main.tex
biber main
xelatex main.tex
xelatex main.tex

# Or use automated build
make              # Full build
make quick        # Single pass
make clean        # Clean artifacts
```

The multiple runs are necessary to resolve all cross-references and citations.

## File Structure

```
Determinatives_as_nouns/
├── main.tex                  # Main document
├── references.bib            # Bibliography
├── .house-style/             # House style snapshot
│   ├── preamble.tex         # LaTeX preamble
│   └── style-rules.yaml     # Style conventions
├── Makefile                  # Build automation
├── CLAUDE.md                 # This file
├── AGENTS.md                 # Synced with this file
└── GEMINI.md                 # Synced with this file
```

## House Style

This project uses Brett Reynolds house style (see `.house-style/style-rules.yaml`).

### Key LaTeX Conventions

**Terms, Mentions, Quotations:**
- Use `\term{}` for terms/concepts (small caps): `\term{definiteness}`
- Use `\mention{}` for mentions/forms (italics): `\mention{the}`
- Use `\olang{}` for object language (italics): `\olang{der Hund}`
- Use `\enquote{}` for quotations: `\enquote{actual quote}`
- Never use raw quotes for mention

**Cross-linguistic Notation:**
- Cross-linguistic: `\textsc{subject}\crossmark`
- Language-specific: `\textsc{subject}\textsubscript{eng}`

**Dashes:**
- Parenthetical: `foo~-- bar~-- baz` (en dash with spaces)
- Ranges: `2001--2025` (en dash, no spaces)
- Compounds: `corpus-based` (hyphen)

**Citations:**
- Parenthetical: `\citep{key}`
- Textual: `\textcite{key}`

**Citations and BibTeX (LAW):**
- Citations and BibTeX entries must NEVER be placeholders
- Citations must NEVER be generated from training data
- LLMs MUST browse the web to find DOIs and verify bibliographic data
- Every citation must be confirmed against an authoritative source
- If you cannot verify a citation, say so. Do not guess. Do not fabricate.

### Writing Style

**Preferred:**
- Use contractions (don't, won't)
- Keep paragraphs ~60 words, max 100
- Direct verbs and short clauses
- Concrete before abstract

**Avoid:**
- Throat-clearers: "It is important to note that..."
- `\paragraph{}` headings (use topic sentences)
- Bold labels in prose
- Hackneyed adverbs: moreover, furthermore

**Document Structure:**
- Use `\section{}` and `\subsection{}` only
- Avoid bullet points for arguments (use prose)
- Use ordinal markers: "first," "second," "third"

**Examples (gb4e):**
```latex
\ea\label{ex:example}
\textit{Example sentence.}
\z
```

## Common Tasks

**Adding References:**
1. Add entry to `references.bib`
2. Protect capitals: `title = {The {Cambridge} Grammar...}`
3. Use `\textcite{key}` or `\citep{key}`

**Building:**
```bash
make              # Full build
make quick        # Fast build
make clean        # Clean up
```

**Git Workflow:**
- Pre-commit hook keeps CLAUDE.md, AGENTS.md, GEMINI.md synced
- Commit often with meaningful messages
- Build before committing to ensure no LaTeX errors

## Multi-Agent Dispatch (MANDATORY)

**Before dispatching multiple agents, ALWAYS ask Brett:**

1. **Which model(s)?** Options: Claude, Codex, Gemini, Copilot
   - Codex is often best for Brett's work
   - Claude and Gemini both have 1M token context windows
   - Different models have different strengths

2. **Redundant outputs?** Should multiple models tackle the same task?
   - Useful for judgment calls (e.g., "Should I add this figure?")
   - Not needed for factual tasks

### CLI Command Patterns

| CLI | Command | Notes |
|-----|---------|-------|
| **Codex** | `codex -p 'prompt' > output.txt &` | Include "Read [PATH] first" in prompt |
| **Gemini** | `cat file.tex \| gemini --yolo -o text 'prompt'` | Must pipe content (file reading broken in YOLO) |
| **Copilot** | `copilot -p 'prompt' > output.txt &` | Fast; add `--allow-all-tools` for file ops |

**Token limits:** Claude 1M = Gemini 1M+ > Codex

See portfolio `CLAUDE.md` or `HPC book/.agent/workflows/multi-agent-review.md` for full patterns.
