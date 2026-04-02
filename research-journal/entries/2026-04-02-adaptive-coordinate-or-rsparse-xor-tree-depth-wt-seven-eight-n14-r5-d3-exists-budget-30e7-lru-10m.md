# Experiment entry

**Date:** 2026-04-02  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-30e7-lru-10m`

**Context:** verifier-oracle-model (`n=14`, `{7,8}`, `r=5`, full **2002** XOR menu, `d=3`-only)

**Hypothesis tested:** Extending **`exists_tree`** budget from **24e7** to **30e7** at **10M** LRU completes the **`d=3`** probe or remains **PARTIAL**.

**Outcome:** INCONCLUSIVE (exit **2**, **PARTIAL** after **300M** calls, **~2615.7 s** DP).

**Key finding:** **+60M** calls beyond **24e7** cost **~645 s** (**~10.8 µs**/call), **worse** than **+60M** over **18e7** (**~8.0 µs**/call) — marginal **LRU** cost **increases** deeper in the search. Still no complete **`d=3`** verdict.

**Implications:**

- Pure budget scaling at **10M** LRU shows **diminishing returns**; algorithm change likely needed for **`r=5`** **`d=3`** closure.
- Truncated **`feasible=False`** remains **not** sound for **`min_d>3`**.

**Analogy pass summary:** Fixed-capacity cache under growing working set — later segments pay **higher** marginal miss cost than earlier **18e7→24e7** step.
