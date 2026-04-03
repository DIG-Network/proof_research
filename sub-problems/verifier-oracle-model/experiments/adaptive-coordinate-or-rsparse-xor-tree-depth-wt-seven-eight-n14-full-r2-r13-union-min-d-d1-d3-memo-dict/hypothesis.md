# Hypothesis

## Analogy pass (mandatory)

1. **Abstract structure:** The prior full-menu experiment fixed `--d-min 3 --d-max 3`, so it only certified **existence** of a depth-3 refuting tree in the combined split language, not the **true minimum depth** `min_d`. The DP driver can scan `d` upward from 1 until the first feasible depth.

2. **Analogous domains:** (i) Binary search / exponential search for a threshold — here the predicate is monotone in `d` (larger depth only adds expressivity). (ii) Model checking: finding the smallest unwinding depth that witnesses a property. (iii) Game trees: minimal plies to force a win.

3. **Machinery elsewhere:** Sequential deepening; stopping at first success gives the optimum under monotonicity.

4. **Transfer seed:** Re-run **`coord + ⋃_{r=2}^{13} XOR_r`** with **`--d-min 1 --d-max 3`** and **`--memo-dict`** to read off **`min_d`** explicitly.

## Falsifiable claim

For **`n=14`**, **`{7,8}`**, full **`r=2..13`** XOR union (**`16368`** splits), **`min_d`** is **either** `2` **or** `3` (prior run showed `d=3` feasible; we test whether `d=2` is already feasible). If `min_d=2`, the **`d=3`-only** witness run was **not** depth-tight.
