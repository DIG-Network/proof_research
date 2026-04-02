# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-10e7-lru-12m

**Date:** 2026-04-02  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-10e7-lru-12m/`

## Context

verifier-oracle-model — `n=14`, `{7,8}`, **r=9**, **d=3**-only, **10⁸** `exists_tree`, **12×10⁶** LRU (paired with **r=5** **10e7/12M**; compare **r=9** **10e7/10M** PARTIAL ~957 s).

## Hypothesis tested

See `hypothesis.md`.

## Outcome

**INCONCLUSIVE** — exit **247** ~**473** s; **OOM** class; no feasibility line.

## Key finding

**12M** LRU **OOM** at **10e7** is **not** **r-asymmetric** — **r=9** matches **r=5** (~464 s vs ~473 s to kill).

## Implications

**12M** LRU remains off-limits on this host for full-menu **d=3** **2002** probes; **r**-dependent speed comparisons require **≤10M** LRU where runs reach **PARTIAL**.

## Analogy pass summary

See `hypothesis.md`.

## Space-definition

None.
