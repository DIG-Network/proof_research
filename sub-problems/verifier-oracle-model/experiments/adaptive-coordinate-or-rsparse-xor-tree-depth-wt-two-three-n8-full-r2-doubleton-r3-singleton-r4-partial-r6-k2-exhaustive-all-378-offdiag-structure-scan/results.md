# Results

**Outcome:** **FAIL**

**Hypothesis:** Some unordered pair of distinct `r=6` XOR splits (**`K=2`**, **`C(28,2)=378`** menus) appended to `coord + full r=2 + doubleton r=3 + singleton r=4` yields **`0 < stratum_min_d2 < 107800`** on the off-diagonal **`s ∈ {0,1,2}`** stratum (**`STRATUM_TOTAL=107800`**).

**Measured:**

| Quantity | Value |
|----------|--------|
| Menus enumerated | 378 |
| Worker processes | 4 (`WORKERS=4`) |
| Wall clock (full run) | **6018.678 s** (~**1.67 h**) |
| Sum of per-menu CPU walls | **24028.831 s** (~**6.67 h** aggregate) |
| `min_stratum_d2_across_menus` | **107800** |
| `max_stratum_d2_across_menus` | **107800** |
| `stratum_pred` (every menu) | **0** |
| `viol_d2_not_pred` (every menu) | **107800** |
| `viol_pred_but_not_d2` (every menu) | **0** |

**Conclusion:** **Every** **`K=2`** partial **`r=6`** menu matches **`K=1`** exhaustive partial **`r=6`** and the prior random **`K=2`** probe on this statistic: universal **`stratum_min_d2=107800`**, no intermediate plateau, wedge predicate never fires on-stratum.

**Script:** `script.py` (exit code **1**).
