# Hypothesis

## Analogy pass (structural)

1. **Abstract structure:** At `n=14`, `{7,8}`, the `coord + r-sparse XOR` DP for `d=3` is hardest in the **2002-split** band (`r=5` and `r=9`). **`r=5`** at **6×10⁷ / 8M LRU** remained **PARTIAL** (~569 s), falsifying “+20% budget finishes.” **`r=9`** at **5×10⁷ / 8M** was **PARTIAL** (~542 s). The menu size is identical; empirical DP cost may differ by parity/XOR geometry.

2. **Analogous domains:** (a) Symmetry in search — dual formulations of the same combinatorial object. (b) Numerical PDEs — two coordinate charts for the same stiff region. (c) SAT — same clause count, different variable order / branching heuristic cost.

3. **Machinery:** Apply the **same** compute envelope (**6×10⁷**, **8M LRU**) to **`r=9`** as was applied to **`r=5`**; compare wall time and termination (PARTIAL vs definite `feasible=`).

4. **Transfer seed:** If **`r=9`** also **PARTIAL** at **6e7/8M**, the **2002** band’s **`d=3`** open class is **stable** under +20% scaling for **both** dual `r` values. If **`r=9`** **finishes** while **`r=5`** does not, **r↔n−r** duality does **not** preserve hardness at this envelope (new structural fact).

## Falsifiable claim

**H0:** Under `--max-exists-calls 60000000`, `--lru-maxsize 8000000`, `r=9`, `d=3`-only, the parent still exits **2** (PARTIAL).

**H1:** The run completes with exit **0** and a definite **`d=3 feasible=`** line without a trailing `PARTIAL: r_single` budget message.

## Memory / lineage

- **Parents:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-5e7-lru-8m` (PARTIAL ~542 s), `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-6e7-lru-8m` (PARTIAL ~569 s — same budget envelope).
