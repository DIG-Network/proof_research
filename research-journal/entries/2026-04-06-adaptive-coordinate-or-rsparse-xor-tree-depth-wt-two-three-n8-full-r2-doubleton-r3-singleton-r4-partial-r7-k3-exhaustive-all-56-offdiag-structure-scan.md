# Journal entry

**Date:** 2026-04-06  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-partial-r7-k3-exhaustive-all-56-offdiag-structure-scan`

**Context:** verifier-oracle-model (`n=8`, shell `{2,3,4}`, off-diagonal `s∈{0,1,2}` stratum)

**Hypothesis tested:** Some **`K=3`** partial `r=7` submenu (**one of 56**) yields **`0 < stratum_min_d2 < 107800`** when appended to `coord + full r=2 + doubleton r=3 + singleton r=4`.

**Outcome:** **FAIL**

**Key finding:** **All 56** menus give **`stratum_min_d2=107800`**, **`stratum_pred=0`**, **`107800`** `d2∧¬pred`; **`total_wall_sec≈1052.0`**. So **`K=3`** is already enough for the same universal saturation as **`K=4`** and full **`r=7`** on this stratum statistic.

**Implications:**

- Continue **`K=2`** (**28**) and **`K=1`** (**8**) exhaustive scans to locate (or rule out) any smaller partial-**`r=7`** slice with intermediate **`stratum_min_d2`**.
- If low **`K`** still saturates, pivot to **partial `r=5` / `r=6`** submenus (arity-split hypothesis).

**Analogy pass summary:** Same **finite puncturing / phase transition** framing as **`K=4`** exhaustion—**`K=3`** is not a rare subfamily; it sits on the saturated side of the cliff.

**Space definition:** none
