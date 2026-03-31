# 2026-03-31 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n13-resolved

**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n13`  
**Context:** verifier-oracle-model  
**Outcome:** PASS (supersedes partial INCONCLUSIVE journal row for the same folder)

## What was completed

Full **`min_d(r)`** for **`r=2..12`** on **`n=13`**, **`|S|∈{6,7}`** (3432 masks), via **`python -u script.py --skip-baseline --r-single r`**, plus unions **`{2,3,4}`**, **`{2..5}`**, **`{2..12}`**.

## Key numbers

- **Row:** `7,5,4,3,3,3,4,3,4,3,2`.
- **Unions:** `r∈{2,3,4}→min_d=4`, `r∈{2..5}→3`, `r∈{2..12}→2`.
- **Baseline (prior):** coord `13`, full 13-XOR `1`.

## Implications

- Same broad picture as n=12: mixing many XOR arities collapses depth to **2**; single-arity depth is **non-monotone** in **`r`**.
- **Difference vs n=12:** triple-only union **`{2,3,4}`** gives **`4`** here vs **`3`** on n=12; **`{2..5}`** still **`3`**; full union still **`2`**.

## Pointer

Canonical tables and timings: experiment **`results.md`**.
