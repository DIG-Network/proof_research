# Experiment entry — 2026-04-04 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-union-r2-only-min-d

**Date:** 2026-04-04  
**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-union-r2-only-min-d`  
**Context:** verifier-oracle-model (entry **136**)

## Hypothesis tested

On `n=5` with mask shell `{2,3}` (20 masks), **coord + XOR union with only `r=2`** still has **`min_d=2`** (so `r=3` splits in the prior `r=2..3` union would be redundant for the depth-2 certificate).

## Outcome

**FAIL** — parent reports `coord_plus_union_rs=[2] total_splits=10 min_d=3` (vs `min_d=2` with `r=2..3` and 20 splits).

## Key finding

**Triple-XOR (`r=3`) splits are load-bearing** for achieving `min_d=2` on this shell: pair-XOR alone only reaches `min_d=3`. This refines the prior “`r=4` not needed” story: dropping **high arity** is not the same as dropping **middle arity** once weight-3 masks are in play.

## Implications

- When analyzing **minimal split menus**, treat each arity as a potential **generator**; falsify redundancy per arity, not only “do we need max arity.”
- Follow-up could search for **minimal subsets** of the 10 triple splits that still force `min_d=2` with all pair splits.

## Analogy pass summary

Decision-tree / circuit-basis view: XOR arities act like gate types; removing `r=3` increased required depth despite keeping `r=2`.

## Space definition

None.
