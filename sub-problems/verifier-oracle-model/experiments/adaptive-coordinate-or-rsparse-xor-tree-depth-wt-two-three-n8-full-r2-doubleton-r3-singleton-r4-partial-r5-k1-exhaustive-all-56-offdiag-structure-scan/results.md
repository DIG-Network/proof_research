# Results

**Outcome:** PASS (pre-registered success criterion satisfied)

**Pre-registered success criterion (script exit 0):** There exists a partial `r=5` submenu with **exactly one** XOR split (`K=1` of `C(8,5)=56`) such that on the off-diagonal `s∈{0,1,2}` stratum, `0 < stratum_min_d2 < 107800`.

**Observed:** For **every** one of the **56** singleton menus, **`stratum_min_d2=3850`** (identical across menus), **`stratum_pred=0`**, **`3850`** `d2∧¬pred`, **`0`** `viol_pred_not_d2`. **Sequential total** **`total_wall_sec≈16092.6`** (~4.5 h). **`min_stratum_d2_across_menus=max_stratum_d2_across_menus=3850`**.

**Interpretation:** On this fixed `{2,3,4}` shell grid, **a single** `r=5` XOR split does **not** force the **`r=6`/`r=7`-style saturation** to **`stratum_min_d2=107800`**. The statistic sits at a **uniform intermediate plateau** (**`3850`** **`min_d=2`** witnesses on the stratum), unlike **partial `r=6` `K=1`** where **every** menu already matched **full `r=6`**. So **partial `r=5` at minimal submenu size behaves qualitatively differently** from **`r=6`/`r=7`** on **`stratum_min_d2`**.

**Command:**  
`python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-partial-r5-k1-exhaustive-all-56-offdiag-structure-scan/script.py`
