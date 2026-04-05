# Results — off-diagonal patchwork by `|T_i∩T_j|`

**Outcome:** FAIL

**Setup:** `n=7`, shell `{2,3}`, language `coord + full r=2 + doubleton r=3 (i≤j) + singleton r=4`, LRU `4_000_000`, full grid `22050` cells.

**Hypothesis:** Biconditional `min_d=2` ⇔ patchwork: diagonal `Q = [7]\T_i`; off-diagonal if `s=|T_i∩T_j|` then `Q=T_i△T_j` for `s∈{0,1}` and `Q=(T_i\T_j)∪([7]\(T_i∪T_j))` for `s=2`.

**Measured:**

| Metric | Value |
|--------|-------|
| `wall_sec` | ≈ 30.47 |
| `min_d=2` total | 1225 (diag 35, off 1190) — matches prior scan |
| Cells matching patchwork predicate (off-diag) | **525** (not 1190) |
| Biconditional | **broken** both ways |

**Failure modes:**

1. **False positives:** Many off-diagonal cells satisfy the patchwork mask equality but have `min_d=3` (e.g. `i=0,j=9,k=20` and long family with `i=0` and varying `j,k`).
2. **False negatives:** Many `min_d=2` off-diagonal witnesses violate the patchwork template — including **`|∩|=2`** cases where observed `Q` is the **complement of the symmetric difference** `T_i△T_j` (e.g. `T_i=(0,1,2), T_j=(0,1,3)`, `Q=(3,4,5,6)` while patchwork expected a different 4-set), and **`|∩|=1`** cases where `Q` is not `T_i△T_j`.

**Conclusion:** A **three-way intersection stratification** with **symdiff + ordered wedge** does **not** classify off-diagonal depth-2 cells. The `min_d=2` region is **not** a union of a small number of **fixed set-theoretic charts** indexed only by `(T_i,T_j)` overlap type and lex order `(i,j)`.
