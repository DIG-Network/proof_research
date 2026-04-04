# Results — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-sextuple-r3-scan-all-sextuples`

**Outcome:** **FAIL** (hypothesis falsified: no `min_d=2` witness).

**Measured:**

| Quantity | Value |
|----------|--------|
| `sexts_checked` | `1623160` (= C(35,6)) |
| `witness_min_d2_count` | `0` |
| `lru_cap` | `4_000_000` |
| `wall_sec` | `3661.037` (~61.0 min) |

**Baseline (from script):** `coord_only min_d=7`, `coord_plus_full_xor min_d=1` (sanity).

**Reasoning:** Exhaustive enumeration of every unordered 6-tuple of `r=3` XOR split indices, together with coordinate splits and the full `r=2` XOR menu (37 XOR splits total: 21 pair + 6 triple), never achieves decision-tree depth 2 in this DP model at `n=7`, shell `{2,3}`. This closes the `C(35,6)` combinatorial envelope suggested after the full `C(35,5)` quintuple scan.
