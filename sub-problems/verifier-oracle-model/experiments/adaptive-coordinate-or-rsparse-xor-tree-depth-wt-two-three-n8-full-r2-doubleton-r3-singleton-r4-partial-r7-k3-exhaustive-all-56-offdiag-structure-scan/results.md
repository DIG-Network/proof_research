# Results

**Outcome:** **FAIL**

**Setup:** `n=8`, shell `{2,3,4}`, off-diagonal stratum `s=|T_i∩T_j|∈{0,1,2}` (`107800` cells). Base language: `coord + full r=2 + doubleton r=3 + singleton r=4`. Append **exactly `K=3`** XOR splits chosen from the full `r=7` menu (`len(p7)=8`). Exhaust **all** `C(8,3)=56` index triples. `LRU_CAP=4_000_000`.

**Measured:**

| Quantity | Value |
|----------|-------|
| Menus enumerated | 56 |
| `stratum_min_d2` every menu | `107800` |
| `stratum_pred` every menu | `0` |
| `viol_d2_not_pred` every menu | `107800` |
| `viol_pred_but_not_d2` every menu | `0` |
| `min_stratum_d2_across_menus` | `107800` |
| `max_stratum_d2_across_menus` | `107800` |
| `total_wall_sec` | `≈1052.0` |

**Conclusion:** No menu satisfies `0 < stratum_min_d2 < 107800`. **`K=3`** partial `r=7` behaves like **`K=4`** and full `r=7` on this statistic: universal stratum saturation at `min_d=2` on all `107800` cells.
