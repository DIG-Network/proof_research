# Results

**Outcome:** **FAIL**

**Script:** `script.py` (exit code 1)

**Summary:** Exhaustive enumeration of all **8** singleton partial-**`r=7`** menus (**`K=1`**) on **`n=8`**, base language `coord + full r=2 + doubleton r=3 + singleton r=4`, restricted to off-diagonal stratum **`s=|T_i∩T_j|∈{0,1,2}`** (**107800** cells). **Every** menu yields **`stratum_min_d2=107800`**, **`stratum_pred=0`**, **`107800`** instances of **`d2 ∧ ¬pred`**, **`0`** false positives. No menu achieves **`0 < stratum_min_d2 < 107800`**.

**Measured:**

| Quantity | Value |
|----------|-------|
| `menus` | 8 |
| `k_p7` | 1 |
| `STRATUM_TOTAL` | 107800 |
| `min_stratum_d2_across_menus` | 107800 |
| `max_stratum_d2_across_menus` | 107800 |
| `total_wall_sec` | ≈204.938 |
| Per-menu `wall_sec` | 38.822, 34.289, 30.732, 27.397, 23.787, 19.978, 16.891, 13.042 |

**Conclusion:** Partial-**`r=7`** at **`n=8`** on this stratum is **saturated at `K=1`** for the **`stratum_min_d2`** statistic — same plateau as **`K∈{2,3,4}`** and full **`r=7`**. Next structural pivot: partial **`r=5`/`r=6`** submenus or a new certificate family.
