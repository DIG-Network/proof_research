# Hypothesis

**Falsifiable claim:** On `n=14`, shells `{7,8}`, **`coord + r=9`** XOR, **`d=3`-only** probe with **`5×10⁷`** `exists_tree` budget and **`8×10⁶`** LRU cap: the run either (a) completes with a definite `d=3` feasibility bit, or (b) exits **PARTIAL** at the budget (like **`r=5`** at this scale), or (c) runs long enough that the host kills the process without a verdict (inconclusive on feasibility).

**Context:** **`r=9`** has **`C(14,9)=2002`** XOR partitions — **same split count as `r=5`**, but a different parity functional on masks. Prior **`r=9` `d=3`** probes with **unbounded** memo hit **multi-hour** wall times without **`feasible=`** (**index:** `…-n14-r9-d3-ninety-min`, INCONCLUSIVE). **`r=6`** at **`5e7`+8M** **PASS**es **`min_d=3`** in ~**435 s**; **`r=5`** at the same envelope **PARTIAL**s. This experiment **holds (budget, LRU, d-window) fixed** and swaps **`r=9`** to locate **`r=9`** in the same resource bracket as **`r=5` vs `r=6`**.

## Analogy pass (abbrev.)

1. **Abstract structure:** Same AND–OR adaptive tree DP over the 6435-mask domain; only the **r-sparse XOR split menu** (which coordinates are XORed before partitioning) changes the reachable state set at fixed depth cap.
2. **Analogous domains:** (i) **Perturbing edge sets** in a graph reachability game while fixing step budget; (ii) **Different clause pools** in CDCL with identical restart cap; (iii) **Isomorphic combinatorial objects** (`C(n,k)=C(n,n−k)`) inducing **different** maps on the same mask alphabet.
3. **Machinery:** Memo footprint vs LRU cap; whether **`r=9`**’s splits induce **more or fewer** distinct subproblems than **`r=5`** despite **equal** menu cardinality.
4. **Transfer seed:** **Dual binomial symmetry** — **2002** splits for **`r=5` and `r=9`** — paired control for **count** while varying the **parity pattern**; compare outcomes to **`r=5`** shard scans and **`r=6`** PASS.
