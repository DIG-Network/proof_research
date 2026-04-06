# Journal entry

**Date:** 2026-04-06  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-partial-r7-k2-exhaustive-all-28-offdiag-structure-scan`

**Context:** verifier-oracle-model (`n=8`, shell `{2,3,4}`, off-diagonal `s∈{0,1,2}` stratum)

**Hypothesis tested:** Some **`K=2`** partial `r=7` submenu (**one of 28**) yields **`0 < stratum_min_d2 < 107800`** when appended to `coord + full r=2 + doubleton r=3 + singleton r=4`.

**Outcome:** **FAIL**

**Key finding:** **All 28** menus give **`stratum_min_d2=107800`**, **`stratum_pred=0`**, **`107800`** `d2∧¬pred`; **`total_wall_sec≈597.0`**. So **`K=2`** already matches the universal saturation seen at **`K∈{3,4}`** on this stratum statistic.

**Implications:**

- Run exhaustive **`K=1`** (**8** menus) next on the same base + partial **`r=7`** slice.
- If **`K=1`** still saturates, treat **partial `r=7`** as essentially **all-or-nothing** for **`min_d=2`** coverage on this stratum and move to **partial `r=5`/`r=6`** or new **`n=8`** certificate structure.

**Analogy pass summary:** Same **phase-transition / sufficient-statistic** framing as **`K=3`/`K=4`** — reducing **`K`** one more step does not uncover a middle **`d2`** mass.

**Space definition:** none
