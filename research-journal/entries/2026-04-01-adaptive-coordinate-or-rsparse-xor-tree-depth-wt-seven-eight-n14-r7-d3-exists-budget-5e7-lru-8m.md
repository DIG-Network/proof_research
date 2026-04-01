# Journal entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r7-d3-exists-budget-5e7-lru-8m

**Date:** 2026-04-01  
**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r7-d3-exists-budget-5e7-lru-8m`  
**Context:** verifier-oracle-model (`n=14`, wt `{7,8}`, coord + **7-sparse** XOR, `d=3`-only)

## Hypothesis tested

At **5×10⁷** `exists_tree` + **8×10⁶** LRU, **`r=7`** (**`C(14,7)=3432`**) either finishes `d=3` with a definite bit or hits **PARTIAL** — probing whether **intermediate** menu size between **3003 PASS** and **2002 PARTIAL** bands is hard.

## Outcome

**PASS** — **`d=3 feasible=True`**, **`min_d=3`**, **DP ~0.54 s** (build ~5.82 s). **3432** splits are **easy** at this envelope; consistent with prior **5e6** shard where **`r=7`** was already sub-second.

## Key finding

**Menu cardinality** **`C(14,r)`** is **not** a monotone predictor of **5e7/8M** **hardness**: **3432** finishes **instantly** while **2002** (**`r=5`/`r=9`**) **PARTIAL** and **1001** is **split-dependent** (**`r=10`** ~55 s **PASS**, **`r=4`** ~467 s **PARTIAL**). **`r=7`** is a **strong easy island** between slower **`r=6`/`r=8`**.

## Implications

- Prefer **parity / geometry** explanations over **raw binomial** **count** for **`n=14` `{7,8}`** **`d=3`** **DP** cost.
- **Self-dual** **`r=7`** does **not** inherit **hardness** from **`r=6`/`r=8`** neighbors at **5e7/8M**.

## Analogy pass summary

Interpolation between **3003** and **2002** regimes; result: **3432** behaves like **trivial** phase, not **intermediate** difficulty.
