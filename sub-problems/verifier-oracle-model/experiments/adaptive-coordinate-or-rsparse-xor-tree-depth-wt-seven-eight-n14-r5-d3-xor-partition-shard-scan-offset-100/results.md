# Results

**Outcome:** PASS (all five subprocess shards exited 0).

**Setup:** Same as `…-xor-partition-shard-scan-400`: parent `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py`, `--skip-baseline`, `--r-single 5`, `--d-min 3 --d-max 3`, `--lru-maxsize 8000000`, `--max-exists-calls 55000000`.

**Shard slices (phase shift +100):**

| Range       | XOR splits | `d=3 feasible` | LRU misses @ d=3 | DP wall (s) |
|-------------|------------|----------------|------------------|-------------|
| 100:500     | 400        | False          | 8_000_000        | ~144.35     |
| 500:900     | 400        | False          | 8_000_000        | ~116.29     |
| 900:1300    | 400        | False          | 8_000_000        | ~119.30     |
| 1300:1700   | 400        | False          | 8_000_000        | ~126.04     |
| 1700:2002   | 302        | False          | 3_916_876        | ~36.20      |

**Interpretation:** No shard found `feasible=True` at depth 3. As with the 0-origin shard scan, **these negatives do not prove** the full 2002-split `r=5` menu is infeasible at `d=3`; they only bound this **family** of contiguous sub-menus (here omitting indices `0..99`). **Positive** witness in any shard would certify `d≤3` for that sub-menu only.

**Total wall time (wrapper):** ~625 s (~10.4 min).
