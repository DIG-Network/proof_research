# Journal entry

**Date:** 2026-04-06  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-partial-r7-k1-exhaustive-all-8-offdiag-structure-scan`

**Context:** verifier-oracle-model (`n=8`, shell `{2,3,4}`, off-diagonal `s∈{0,1,2}` stratum)

**Hypothesis tested:** Some **`K=1`** partial `r=7` submenu (**one of 8**) yields **`0 < stratum_min_d2 < 107800`** when appended to `coord + full r=2 + doubleton r=3 + singleton r=4`.

**Outcome:** **FAIL**

**Key finding:** **All 8** menus give **`stratum_min_d2=107800`**, **`stratum_pred=0`**, **`107800`** `d2∧¬pred`; **`total_wall_sec≈204.9`**. With prior **`K∈{2,3,4}`** exhaustive scans, **every** nonempty partial **`r=7`** submenu at **`n=8`** matches full **`r=7`** saturation on this statistic.

**Implications:**

- Pivot to **partial `r=5`/`r=6`** submenus (within fixed **`r`**) or invent a new **`n=8`** certificate predicate family; the **`r=7`** arity slice is structurally **all-or-nothing** for **`stratum_min_d2`** here.

**Analogy pass summary:** Minimal generator count (**`K=1`**) still lies in the saturated phase — same **matroid-closure / percolation** picture as **`K≥2`**.

**Space definition:** none
