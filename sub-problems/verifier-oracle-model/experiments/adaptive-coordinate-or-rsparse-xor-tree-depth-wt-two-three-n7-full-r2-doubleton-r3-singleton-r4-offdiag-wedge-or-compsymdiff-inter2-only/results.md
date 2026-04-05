# Results — wedge ∪ complement(symdiff) on `|∩|=2` stratum only

**Outcome:** FAIL

**Setup:** `n=7`, shell `{2,3}`, language `coord + full r=2 + doubleton r=3 (i≤j) + singleton r=4`, LRU `4_000_000`, full grid `22050` cells. Analysis restricted to off-diagonal pairs with **`s = |T_i ∩ T_j| = 2`** (**`7350`** cells).

**Hypothesis:** On that stratum, **`min_d = 2`** iff **`Q ∈ {W, C}`** where **`W = (T_i \ T_j) ∪ ([7] \ (T_i ∪ T_j))`** (ordered wedge) and **`C = [7] \ (T_i △ T_j)`** (complement of symmetric difference).

**Measured:**

| Metric | Value |
|--------|-------|
| `wall_sec` | ≈ 32.04 |
| Stratum cells (`i<j`, `s=2`) | **7350** |
| Stratum cells with `min_d=2` | **420** |
| Stratum cells with `Q ∈ {W,C}` | **210** |
| Biconditional | **broken** — **210** witnesses with **`min_d=2`** but **`Q ∉ {W,C}`** (no counterexamples observed in the converse direction in the printed sample; totals imply **`|pred ∧ (md≠2)| = 0`** on this stratum) |

**Failure mode:** **`Q=(3,4,5,6)`** with **`k=34`** recurs for many **`(T_i,T_j)`** sharing the same fixed overlap pattern (e.g. **`T_i=(0,1,2)`**, varying **`T_j`** with **`{0,1}⊂T_j`**) — **`min_d=2`** holds but **`Q`** is neither **`W`** nor **`C`** for those pairs.

**Conclusion:** Even after isolating **`|∩|=2`**, **depth-2** quartic labels are **not** classified by the **two-set** disjunction **wedge vs complement(symdiff)**. The **`min_d=2`** fiber in this stratum is **strictly larger** than **`{W,C}`**.
