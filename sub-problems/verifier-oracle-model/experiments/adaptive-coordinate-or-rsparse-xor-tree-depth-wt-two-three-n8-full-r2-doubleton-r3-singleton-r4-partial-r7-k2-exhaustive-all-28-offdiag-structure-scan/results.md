# Results

**Outcome:** **FAIL**

**Setup:** `n=8`, shell `{2,3,4}`, off-diagonal stratum `s=|T_i∩T_j|∈{0,1,2}` (`STRATUM_TOTAL=107800` cells). Base language: `coord + full r=2 + doubleton r=3 + singleton r=4`. Append **exactly two** distinct XOR splits from the full `r=7` menu (`len(p7)=8`), i.e. all `C(8,2)=28` menus.

**Measured:**

| Quantity | Value |
|----------|-------|
| Menus scanned | 28 |
| `stratum_min_d2` every menu | `107800` |
| `stratum_pred` every menu | `0` |
| `viol_d2_not_pred` every menu | `107800` |
| `viol_pred_but_not_d2` every menu | `0` |
| `min_stratum_d2_across_menus` | `107800` |
| `max_stratum_d2_across_menus` | `107800` |
| `total_wall_sec` | `≈596.99` |
| LRU cap | `4_000_000` |

**Conclusion:** No menu achieves `0 < stratum_min_d2 < 107800`. **`K=2`** partial `r=7` is already on the same universal saturation plateau as **`K=3`**, **`K=4`**, and the probed random **`K=4`** sample on this statistic.

**Script exit code:** `1` (hypothesis falsified).
