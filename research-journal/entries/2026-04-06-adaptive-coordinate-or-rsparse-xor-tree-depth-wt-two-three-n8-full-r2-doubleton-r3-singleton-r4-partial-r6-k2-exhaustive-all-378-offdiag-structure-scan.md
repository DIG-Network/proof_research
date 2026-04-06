# Journal entry

**Date:** 2026-04-06  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-partial-r6-k2-exhaustive-all-378-offdiag-structure-scan`

**Context:** verifier-oracle-model (`n=8`, shell `{2,3,4}`, off-diagonal `s∈{0,1,2}` stratum)

**Hypothesis tested:** Some **unordered pair** of distinct `r=6` XOR splits (**`K=2`**, exhaustive **`C(28,2)=378`**) yields **`0 < stratum_min_d2 < 107800`** when appended to `coord + full r=2 + doubleton r=3 + singleton r=4`.

**Outcome:** **FAIL**

**Key finding:** **All 378** menus give **`stratum_min_d2=107800`**, **`stratum_pred=0`**, **`107800`** `d2∧¬pred`, **`0`** false positives. Run used **`WORKERS=4`**: **`wall_clock_sec≈6018.7`**, **`sum_menu_wall_sec≈24028.8`**. This **closes** the open item from the random **`K=2`** probe: two **`r=6`** splits never produce an intermediate off-diagonal **`d2`** count on this stratum (same saturation as **`K=1`** partial **`r=6`**).

**Implications:**

- **`n=8`**, this base + stratum: partial **`r=6`** at **`K∈{1,2}`** is **fully saturated** at **`107800`** (finite evidence).
- Next structural pressure: **`K≥2`** partial **`r=5`** (**`1540`** menus) or theory for **`3850`** vs **`107800`**.

**Analogy pass summary:** Second parity constraint in a **saturated** affine coset of constraints need not refine the **observable** statistic if both constraints are **redundant** for the stratum closure; exhaustive enumeration is the finite proof hook.

**Space definition:** none
