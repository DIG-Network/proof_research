# Results — `s=2` off-diagonal stratum: `W_ij ∨ W_ji ∨ C_ij` vs `min_d=2`

**Outcome:** PASS

**Setup:** `n=7`, shell `{2,3}`, language `coord + full r=2 + doubleton r=3 (i<j) + singleton r=4`, LRU `4_000_000`, full grid scan `22050` cells; analysis restricted to **`i < j`** with **`|T_i ∩ T_j| = 2`** (**`7350`** cells).

**Hypothesis:** On this stratum, **`min_d = 2`** iff **`Q ∈ {W(i,j), W(j,i), C(i,j)}`** with **`W`** and **`C`** as in experiment **163**.

**Measured:**

| Metric | Value |
|--------|-------|
| `wall_sec` | ≈ 30.24 |
| `s2_cells` | **7350** |
| `s2_min_d2` | **420** |
| `s2_pred` | **420** |
| `pred_wij` | **210** |
| `pred_wji` | **210** |
| `pred_c` | **0** |
| `viol d2 ∧ ¬pred` | **0** |
| `viol pred ∧ (md≠2)` | **0** |

**Key finding:** On **`|∩|=2`**, **`C(i,j) = [7] \ (T_i △ T_j)`** has **`|C| = 5`**, while every quartic **`Q`** has **`|Q| = 4`**, so **`Q = C`** never occurs. Every depth-**`2`** witness is therefore a **wedge** — split evenly between **`W_ij`** and **`W_ji`** (**`210`** each). The triple-disjunct predicate is **equivalent** on this stratum to **`W_ij ∨ W_ji`**, repairing the **210** false negatives from the **`s=2: W∨C`** chart in experiment **163**.

**Conclusion:** The **`s=2`** slice satisfies the **symmetric wedge pair** biconditional **`min_d=2 ⇔ (W_ij ∨ W_ji)`**; **`C`** is **vacuous** here but included to match the session prompt’s **`{W,W_rev,C}`** envelope.
