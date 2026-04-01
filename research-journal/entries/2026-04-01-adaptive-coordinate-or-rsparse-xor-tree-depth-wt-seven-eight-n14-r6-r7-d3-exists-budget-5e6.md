# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r6-r7-d3-exists-budget-5e6

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r6-r7-d3-exists-budget-5e6/`

## Context

verifier-oracle-model — `n=14`, shells `{7,8}`, same **5×10⁶** `exists_tree` budget and `d=3`-only probes as the `r=5` shard; legs **`r=6`** then **`r=7`**.

## Hypothesis tested

Under identical bounded-memo settings, **`r=7`** reaches a definite `feasible=` line while **`r=6`** stays **PARTIAL** like **`r=5`**.

## Outcome

**PASS** — **`r=6`** exit **2** (partial at budget), **`r=7`** exit **0** with **`d=3 feasible=True`**.

## Key finding

**`d=3` tractability is not monotone in `r`:** mid-`r` values **{5,6}** exhaust the **5×10⁶** budget without deciding `d=3`, while **`r=7`** finishes the DP in **~0.4 s** despite **more** partition splits than `r=6`.

## Implications

- When interpreting **`min_d(r)`** sweeps, **easy** and **hard** `r` bands can be **interleaved**; “more XORs” ≠ uniformly harder.
- Resolving **`r=5`/`r=6`** still needs **unbounded memo**, **sharding**, or **new ideas**—this run only **maps** the phenomenon.

## Analogy pass summary

Phase-transition style: same global budget, qualitatively different reachable state spaces as `r` steps across a band.

## Space-definition

None.
