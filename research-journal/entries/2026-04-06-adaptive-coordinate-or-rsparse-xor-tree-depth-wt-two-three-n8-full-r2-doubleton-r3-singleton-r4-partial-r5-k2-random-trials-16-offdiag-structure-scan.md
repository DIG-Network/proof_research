# Journal entry

**Date:** 2026-04-06  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-partial-r5-k2-random-trials-16-offdiag-structure-scan`

**Context:** verifier-oracle-model (`n=8`, shell `{2,3,4}`, off-diagonal `s∈{0,1,2}` stratum)

**Hypothesis tested:** Some **random** draw of **two** distinct `r=5` XOR splits (**`K=2`**, **`NUM_TRIALS=16`**, **`SEED=0`**) yields **`0 < stratum_min_d2 < 107800`** when appended to `coord + full r=2 + doubleton r=3 + singleton r=4`.

**Outcome:** **PASS**

**Key finding:** **All 16** trials give **`stratum_min_d2=7630`** (intermediate between **`K=1`** uniform **`3850`** and **`r=6`**/**`r=7`** saturation **`107800`**), **`stratum_pred=0`**, **`7630`** `d2∧¬pred`, **`0`** false positives; **`total_wall_sec≈3867.9`**. Suggests a **second plateau** for partial **`r=5`** at **`K=2`** in this sample — **not** universal proof until **`C(56,2)=1540`** exhaustive scan.

**Implications:**

- Partial **`r=5`** **`K=2`** is structurally unlike partial **`r=6`** **`K=2`** (which universally **`107800`** exhaustive).
- Next: exhaustive **`1540`** menus, closed-form for **`7630`** (**`2×3850−70`** numerology vs **`len(p4)=70`**), or certificate pivot.

**Analogy pass summary:** Second generator in a monotone XOR family; sampled pairs probe whether closure jumps to **`107800`** — here it lands at a strict intermediate.

**Space definition:** none
