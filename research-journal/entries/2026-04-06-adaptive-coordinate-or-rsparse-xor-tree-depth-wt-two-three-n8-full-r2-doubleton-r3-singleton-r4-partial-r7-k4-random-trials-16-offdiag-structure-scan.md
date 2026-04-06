# Journal entry

**Date:** 2026-04-06  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-partial-r7-k4-random-trials-16-offdiag-structure-scan`

**Context:** verifier-oracle-model (`n=8`, shell `{2,3,4}`, off-diagonal `s∈{0,1,2}` stratum)

**Hypothesis tested:** Some **random** draw of **`K=4`** splits from the **`r=7`** XOR menu (**8** total), appended to `coord + full r=2 + doubleton r=3 + singleton r=4`, yields **`0 < stratum_min_d2 < 107800`** (**16** trials, **`SEED=0`**).

**Outcome:** **FAIL**

**Key finding:** All **16** trials gave **`stratum_min_d2=107800`**, **`stratum_pred=0`**, **`107800`** `d2∧¬pred` violations; **≈274.4 s** total wall. **Partial** `r=7` at **half** the full split count does **not** (in this probe) produce a **mixed** stratum—saturation matches **full** `r=7`.

**Implications:**

- Try **smaller** **`K`** or **exhaustive** **`C(8,K)`** for small **`K`** before claiming “any nontrivial `r=7` submenu suffices.”
- The **strict full-menu** “cliff” may extend to **sparse** high-arity submenus at modest **`K`**.

**Analogy pass summary:** Percolation-style **mixed phase** between sparse and full menus — **not** observed in this **16×K=4** random sample; behavior looks **first-order** (all-or-nothing on the stratum).

**Space definition:** none
