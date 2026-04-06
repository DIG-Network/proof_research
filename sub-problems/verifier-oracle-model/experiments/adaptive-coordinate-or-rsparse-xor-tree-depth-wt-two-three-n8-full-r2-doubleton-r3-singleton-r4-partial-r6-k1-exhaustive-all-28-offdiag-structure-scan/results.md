# Results

**Outcome:** FAIL (hypothesis falsified — pre-registered claim below)

**Pre-registered success criterion (script exit 0):** There exists a partial `r=6` submenu with **exactly one** XOR split (`K=1` of `C(8,6)=28`) such that on the off-diagonal `s∈{0,1,2}` stratum, `0 < stratum_min_d2 < 107800`.

**Observed:** For **each** of the **28** singleton menus, **`stratum_min_d2=107800`**, **`stratum_pred=0`**, **`107800`** `d2∧¬pred`, **`0`** `viol_pred_not_d2`. Per-menu wall times decreased monotonically from **`≈103.3s`** (menu 1) to **`≈41.6s`** (menu 28) as the LRU warmed; **sequential total** **`total_wall_sec≈2025.0`** (~33.8 min).

**Interpretation:** On this fixed `{2,3,4}` shell grid, **a single** `r=6` XOR split already forces **`min_d=2` on every** stratum cell — same saturation as the **full** `r=6` menu from the strict-subset scan. There is **no** partial-`r=6` window at **`K=1`** for the **`stratum_min_d2`** statistic; behavior matches partial **`r=7`**.

**Command:**  
`python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-partial-r6-k1-exhaustive-all-28-offdiag-structure-scan/script.py`
