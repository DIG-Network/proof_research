# Journal entry

**Date:** 2026-04-06  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-partial-r6-k1-exhaustive-all-28-offdiag-structure-scan`

**Context:** verifier-oracle-model (`n=8`, shell `{2,3,4}`, off-diagonal `s∈{0,1,2}` stratum)

**Hypothesis tested:** Some **`K=1`** partial `r=6` submenu (**one of 28**) yields **`0 < stratum_min_d2 < 107800`** when appended to `coord + full r=2 + doubleton r=3 + singleton r=4`.

**Outcome:** **FAIL**

**Key finding:** **All 28** menus give **`stratum_min_d2=107800`**, **`stratum_pred=0`**, **`107800`** `d2∧¬pred`; **`total_wall_sec≈2025.0`**. A **single** `r=6` split matches **full** `r=6` saturation on this statistic (consistent with partial **`r=7`** singleton closure).

**Implications:**

- Next: **`K≥2`** partial **`r=6`** scans or **`K=1`** exhaustive partial **`r=5`** (**56** menus), or a new certificate predicate / stratum if these also cliff-saturate.

**Analogy pass summary:** One generator can already lie in the **saturated** matroid-style closure — same picture as **`r=7`**, **`K=1`**.

**Space definition:** none
