# Experiment entry

**Date:** 2026-04-06  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-strict-subsets-r5-r6-r7-offdiag-structure-scan`

**Context:** verifier-oracle-model (`n=8`, shell `{2,3,4}`, off-diagonal `s∈{0,1,2}`)

**Hypothesis tested:** Some **strict** nonempty subset of the full XOR menus at `r∈{5,6,7}` (appended to the sparse `r2+doubleton r3+singleton r4` language) yields a **nonempty proper** `min_d=2` stratum on this grid (`0 < stratum_min_d2 < 107800`).

**Outcome:** FAIL

**Key finding:** All **six** strict nonempty masks give **`stratum_min_d2=107800`** (universal depth-2 on the stratum), with **`stratum_pred=0`** and **`107800`** wedge violations — same as full `r5–r7`. Fastest pass: full **`r=7`** only (~16.3 s); slowest: full **`r=5`** only (~266.5 s). Sequential total ~**524 s**. There is **no** partial-witness window between sparse (`0`, prior experiment) and saturated high menus: **any** full high-arity menu in `{5,6,7}` already saturates the stratum.

**Implications:**

- The “biphasic” n=8 picture is sharper: the jump to universal `min_d=2` happens at **first inclusion** of a full `r∈{5,6,7}` menu, not only when all three are present.
- Searching **partial submenus** inside a fixed arity (not the full `C(8,r)` list) is the next combinatorial scale if we still want a “minimal sufficiency” certificate in this model.

**Analogy pass summary:** See `hypothesis.md` (percolation / matroid-span style boundary scan).
