# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-10e7-lru-12m

**Date:** 2026-04-02  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-10e7-lru-12m/`

## Context

verifier-oracle-model — `n=14`, `{7,8}`, **r=5**, **d=3**-only, **10⁸** `exists_tree` budget, **12×10⁶** LRU (test whether **10M→12M** helps at **10e7** after **10e7/10M** PARTIAL ~838 s).

## Hypothesis tested

See `hypothesis.md`: **12M** LRU might complete or improve time vs **10M** at fixed **10e7** budget.

## Outcome

**INCONCLUSIVE** — exit **247** ~**464** s; **OOM** / **SIGKILL** class; no **`PARTIAL:`** / no **`feasible=`** (same class as **7.5e7/12M**).

## Key finding

**12M** LRU is **unsafe** on this host for **r=5** **d=3** at **10e7** — worse than **10M** which at least exhausts budget with a **PARTIAL** certificate.

## Implications

- Do **not** use **12M** LRU for **n=14** **2002**-split **d=3** probes here; next steps remain **high-RAM** **unbounded** memo, **sharding**, or **algorithm** change.

## Analogy pass summary

See `hypothesis.md` — transposition-table size vs time; **12M** hits memory wall before **10⁸** invocations.

## Space-definition

None.
