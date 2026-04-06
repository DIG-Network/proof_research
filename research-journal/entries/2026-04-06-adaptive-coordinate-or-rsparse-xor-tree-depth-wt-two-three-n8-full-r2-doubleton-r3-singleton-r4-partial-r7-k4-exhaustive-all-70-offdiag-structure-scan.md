# Journal entry

**Date:** 2026-04-06  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-partial-r7-k4-exhaustive-all-70-offdiag-structure-scan`

**Context:** verifier-oracle-model (`n=8`, shell `{2,3,4}`, off-diagonal `s∈{0,1,2}` stratum)

**Hypothesis tested:** Some **`K=4`** partial `r=7` submenu (**one of 70**) yields **`0 < stratum_min_d2 < 107800`** when appended to `coord + full r=2 + doubleton r=3 + singleton r=4`.

**Outcome:** **FAIL**

**Key finding:** **All 70** menus give **`stratum_min_d2=107800`**, **`stratum_pred=0`**, **`107800`** `d2∧¬pred`; **`total_wall_sec≈1233.1`**. The earlier **16-trial random** sample was not a fluke—**exhaustion** closes the **`C(8,4)`** envelope: **`K=4`** partial `r=7` **universally saturates** the stratum like **full** `r=7`.

**Implications:**

- Next probes: **`K∈{1,2,3}`** exhaustive or targeted scans; or **partial** `r=5` / `r=6` submenus within arity.
- Strengthens the “**high-arity XOR parity is a cliff**” picture: even **half** of the **`r=7`** split list is enough for **full** stratum **`min_d=2`** here.

**Analogy pass summary:** Finite **coding / puncturing** analogy—**all** puncture patterns of weight **4** behave like the **full** `r=7` menu on this statistic, not a rare subfamily.

**Space definition:** none
