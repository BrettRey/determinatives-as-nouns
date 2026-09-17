# Makefile for LaTeX paper compilation
# English determinatives as nouns

# Configuration
LATEX = xelatex
BIBER = biber
MAIN = determinatives-as-nouns
SUPPLEMENTS = matrix-audit corpus-documentation quantifier-controls
OUTDIR = .

# Targets
.PHONY: all supplements clean distclean view help test check-quant-table claims check-claims census

# Default target: build the PDF
all: $(MAIN).pdf

# Standalone empirical supplements
supplements: $(SUPPLEMENTS:%=%.pdf)

$(SUPPLEMENTS:%=%.pdf): %.pdf: %.tex references.bib references-local.bib .house-style/preamble.tex
	$(LATEX) -interaction=nonstopmode -halt-on-error -output-directory=$(OUTDIR) $<
	$(BIBER) $*
	$(LATEX) -interaction=nonstopmode -halt-on-error -output-directory=$(OUTDIR) $<
	$(LATEX) -interaction=nonstopmode -halt-on-error -output-directory=$(OUTDIR) $<

matrix-audit.pdf: analysis/generated/matrix-table.tex
corpus-documentation.pdf: analysis/generated/corpus-table.tex
quantifier-controls.pdf: analysis/generated/quant-table.tex analysis/generated/exclusion-table.tex

# Table 1 of the quantifier supplement is derived from the extracted claim set
# (analysis/expanded-json-2026-09-14), so the markers cannot drift from the
# evidence.  `make check-quant-table' verifies the committed file instead.
analysis/generated/quant-table.tex: analysis/expanded-json-2026-09-14/records.json \
		analysis/expanded-json-2026-09-14/supplement-cell-map.json \
		analysis/tools/quant_table.py
	python3 analysis/tools/quant_table.py build

analysis/generated/exclusion-table.tex: analysis/exclusion-checks.json analysis/tools/exclusion_table.py
	python3 analysis/tools/exclusion_table.py

check-quant-table:
	python3 analysis/tools/quant_table.py check
	python3 analysis/tools/exclusion_table.py check

# The claim set gains evidence_type and subcategory in a derived layer; the
# source run under analysis/expanded-json-2026-09-14 is a provenance bundle
# and is never modified.
analysis/claims/claims-enriched.json: analysis/expanded-json-2026-09-14/records.json \
		analysis/expanded-json-2026-09-14/supplement-cell-map.json \
		analysis/claims/enrich.py
	python3 analysis/claims/enrich.py

claims: analysis/claims/claims-enriched.json

# Fails when a quoted passage has been edited, moved or deleted, i.e. when the
# claim set has gone stale against the manuscript.
check-claims:
	python3 analysis/claims/check_sources.py

# Normalized census layer (lexeme, subcategory, construction, basis at the locus) and
# the tables derived from it. normalize.py caches its model calls, so a rerun is free
# unless the census, the enriched claim set or the manuscript changed.
census:
	python3 analysis/manuscript-census-2026-09-14/normalize.py
	python3 analysis/tools/census_tables.py

# Full build sequence with bibliography
$(MAIN).pdf: $(MAIN).tex references.bib
	@echo "==> First LaTeX pass..."
	$(LATEX) -output-directory=$(OUTDIR) $(MAIN).tex
	@echo "==> Running Biber..."
	$(BIBER) $(MAIN)
	@echo "==> Second LaTeX pass..."
	$(LATEX) -output-directory=$(OUTDIR) $(MAIN).tex
	@echo "==> Third LaTeX pass (finalizing)..."
	$(LATEX) -output-directory=$(OUTDIR) $(MAIN).tex
	@echo "==> Build complete: $(MAIN).pdf"

# Quick build (single pass, no bibliography update)
quick: $(MAIN).tex
	@echo "==> Quick build (single pass)..."
	$(LATEX) -output-directory=$(OUTDIR) $(MAIN).tex

# Use LuaLaTeX instead of XeLaTeX (not recommended - breaks PDF text layer)
lualatex: LATEX = lualatex
lualatex: all

# Clean build artifacts (keep PDF)
clean:
	@echo "==> Cleaning build artifacts..."
	rm -f $(MAIN).aux $(MAIN).bbl $(MAIN).bcf $(MAIN).blg $(MAIN).log
	rm -f $(MAIN).out $(MAIN).run.xml $(MAIN).toc $(MAIN).fdb_latexmk
	rm -f $(MAIN).fls $(MAIN).synctex.gz
	@echo "==> Clean complete"

# Clean everything including PDF
distclean: clean
	@echo "==> Removing PDF..."
	rm -f $(MAIN).pdf
	@echo "==> Deep clean complete"

# Open PDF viewer (macOS)
view: $(MAIN).pdf
	@echo "==> Opening PDF..."
	open $(MAIN).pdf

# Test the Python specification
test:
	@echo "==> Testing theoretical specification..."
	cd src && python typology.py

# Show available targets
help:
	@echo "Available targets:"
	@echo "  make          - Build PDF with full bibliography (default)"
	@echo "  make supplements - Build the matrix audit and corpus documentation"
	@echo "  make quick    - Quick build (single pass, no bib update)"
	@echo "  make lualatex - Build using LuaLaTeX (not recommended)"
	@echo "  make clean    - Remove build artifacts (keep PDF)"
	@echo "  make distclean- Remove everything including PDF"
	@echo "  make view     - Open PDF (macOS only)"
	@echo "  make test     - Run Python specification tests"
	@echo "  make check-quant-table - Verify Table 1 against the claim set"
	@echo "  make claims   - Rebuild the enriched claim set"
	@echo "  make check-claims - Verify claim quotations still match the sources"
	@echo "  make census   - Rebuild the normalized census and its cross-tab and worklist"
	@echo "  make help     - Show this help message"
