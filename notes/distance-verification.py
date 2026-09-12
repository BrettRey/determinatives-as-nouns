#!/usr/bin/env python3
"""Historical selected-distance checker, retired after the September 2026 audit.

The old script and manuscript are preserved in notes/snapshots/2026-09-07-pre-rebuild/.
It used selected comparison groups and approximate agreement, not a clustering
reproduction. Use the analysis/ scripts and README for the current evidence.
"""
from pathlib import Path

if __name__ == "__main__":
    analysis = Path(__file__).resolve().parents[1] / "analysis"
    print(f"Retired historical checker. Current reproducible analysis: {analysis / 'README.md'}")
    print(f"Exact historical-distance audit: {analysis / 'results/legacy-distance-audit.csv'}")
