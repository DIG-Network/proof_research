# Results — global stratified `|∩|` predicate vs `min_d=2` (off-diagonal)

**Outcome:** FAIL

**Setup:** `n=7`, shell `{2,3}`, language `coord + full r=2 + doubleton r=3 (i<j) + singleton r=4`, LRU `4_000_000`, full grid `22050` cells. Analysis: all **`i < j`** cells (**`20825`** off-diagonal triple pairs).

**Hypothesis:** Global biconditional: **`min_d = 2`** iff stratified predicate **`P`**:
- **`s = |T_i ∩ T_j| ∈ {0,1}`:** **`Q ∈ {W(i,j), W(j,i)}`** with **`W(a,b) = (T_a \ T_b) ∪ ([7] \ (T_a ∪ T_b))`**
- **`s = 2`:** **`Q ∈ {W(i,j), C(i,j)}`** with **`C = [7] \ (T_i △ T_j)`**

**Measured:**

| Metric | Value |
|--------|-------|
| `wall_sec` | ≈ 31.06 |
| Off-diagonal cells | **20825** (**`s01=13475`**, **`s2=7350`**) |
| Off-diagonal `min_d=2` | **1190** |
| Off-diagonal predicate hits | **980** |
| `viol d2 ∧ ¬pred` | **210** |
| `viol pred ∧ (md≠2)` | **0** |

**Failure mode:** Every violation lies in the **`s=2`** stratum with **`Q`** equal to the **complement of the overlap edge** (e.g. recurring **`Q=(3,4,5,6)`** / **`k=34`** when **`T_i=(0,1,2)`** and **`T_j`** shares **`{0,1}`**). Here **`Q = W_ji`** (reverse wedge), but the **`s=2`** branch of **`P`** only tests **`W_ij` ∪ `C_ij`**, so **`W_ji`** is a **false negative**.

**Conclusion:** A naive three-chart **stratified** rule that reuses the **`s∈{0,1}`** symmetric wedge disjunction on **`s=2`** **without** **`W_ji`** is **globally incomplete**. The global obstruction is **exactly** the known **`210`**-cell **`s=2`** mismatch from the **`{W,C}`** chart (experiment **159**), now seen as **missing the second wedge orientation** on **`s=2`**.
