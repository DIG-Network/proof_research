# Results — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-septuple-r3-scan-all-septuples`

**Outcome:** **FAIL** (hypothesis falsified: no `min_d=2` witness in the full `C(35,7)` family).

**Measured:**

| Quantity | Value |
|----------|--------|
| `septs_checked` | `6724520` (= C(35,7)) |
| `witness_min_d2_count` | `0` |
| `lru_cap` | `4_000_000` |
| `wall_sec` | `14123.178` (~3.92 h) |

**Baseline (from script):** `coord_only min_d=7`, `coord_plus_full_xor min_d=1` (sanity).

**Reasoning:** Exhaustive enumeration of every unordered 7-tuple of `r=3` XOR split indices, together with coordinate splits and the full `r=2` XOR menu, never achieves decision-tree depth 2 in this DP model at `n=7`, shell `{2,3}`. This closes the finite `C(35,7)` combinatorial envelope on this sparse triple ladder (after full `C(35,5)` and `C(35,6)`).

**Log:** `scan.log` in this folder records progress every 50k septuples and the final summary line.
