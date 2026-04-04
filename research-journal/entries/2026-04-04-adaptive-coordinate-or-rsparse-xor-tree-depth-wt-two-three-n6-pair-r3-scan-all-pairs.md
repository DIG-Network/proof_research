# Experiment entry — 2026-04-04

**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6-pair-r3-scan-all-pairs`  
**Slug:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6-pair-r3-scan-all-pairs`  
**Context:** verifier-oracle-model  
**Outcome:** PASS

## Hypothesis tested

Among all `C(20,2)=190` unordered pairs of `r=3` XOR splits (lex on `combinations(range(6),3)`), together with **coord + full `r=2`**, does **any** pair achieve `min_d=2` after singleton `r=3` failed for all 20 singles?

## Key finding

**10** pairs achieve `min_d=2`; they are exactly the **complementary** pairs of disjoint triples partitioning `{0,…,5}` (indices `(0,19)`, `(1,18)`, …, `(9,10)` in lex triple order). The other **180** pairs still yield `min_d=3`. Wall time ~0.12 s for the full scan.

## Implications

- Minimal number of `r=3` splits needed for `min_d=2` at `n=6` on this shell is **2**, but only for **3+3 partition** geometry — not arbitrary pairs.
- Refines the `n=6` singleton failure: two triple parities suffice when they **split the six coordinates into two halves**.

## Analogy pass summary

See `hypothesis.md` — 2-generator extension / matroid-circuit style synergy; empirical witness family = vertex 3-coloring into two triples.
