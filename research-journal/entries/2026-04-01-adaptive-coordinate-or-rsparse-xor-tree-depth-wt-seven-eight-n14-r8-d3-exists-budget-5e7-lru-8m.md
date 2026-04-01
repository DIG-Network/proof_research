# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r8-d3-exists-budget-5e7-lru-8m

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r8-d3-exists-budget-5e7-lru-8m/`

## Context

verifier-oracle-model — `n=14`, Hamming shells `{7,8}`, `coord + r=8` XOR language, `d=3`-only probe with **5×10⁷** `exists_tree` budget and **8×10⁶** LRU cap. **C(14,8)=C(14,6)=3003** splits (dual pair to **`r=6`**, same count as **`r=5`/`r=9`** dual).

## Hypothesis tested

See `hypothesis.md`: whether **`r=8`** completes with a definite **`d=3`** bit at this envelope (like **`r=6`**) or **PARTIAL**s (like **`r=5`/`r=9`**).

## Outcome

**PASS** — **`d=3 feasible=True`**, **`min_d=3`**, DP ~**510.1 s** within **50M** calls and **8M** LRU.

## Key finding

**`r=8`** tracks **`r=6`** (**3003** splits, **PASS**), **not** **`r=9`** (**2002**, **PARTIAL**). Together with **`r=5`/`r=9`** both **PARTIAL** at **2002**, this supports **split-count banding** at **5e7/8M**: **~3003** menus **can** finish **`d=3`**; **~2002** menus **need** more budget or stay **PARTIAL** here.

## Implications

- **`r=10`** (**2002** splits) is the natural next **same-count-as-5/9** probe; **`r=7`** (**3432** splits) extends the **>3003** band.
- **`r=8`** does **not** refute **`r=9`** hardness; it **separates** **cardinality** from **complement-only** symmetry.

## Analogy pass summary

Binomial dual **`(6,8)`** at **3003** vs **`(5,9)`** at **2002** as paired controls on **menu size** vs **parity map**.

## Space-definition

None.
