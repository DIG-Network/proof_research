# Results

**Outcome:** INCONCLUSIVE (parent exit **2** — PARTIAL: budget exhausted during `d=3` probe).

**Configuration:** `n=14`, shells `{7,8}`, `coord + r=9` XOR (2002 splits), `--d-min 3 --d-max 3`, `--max-exists-calls 90000000`, `--lru-maxsize 8000000`, `--skip-baseline`.

**Measured:**
- `exists_tree` budget hit at **9×10⁷** invocations; LRU saturated at **8×10⁶** entries.
- Parent-reported `dp_sec` for `d=3` segment: **~815.26 s** (~13.59 min); partition build **~4.20 s**.
- Wall clock for wrapper run: **~856 s**.
- Parent printed `d=3 feasible=False` after PARTIAL line (not certified completion).

**Comparison:** +10M calls over **8e7** added **~121.5 s** DP time (**~815.3** vs **~693.8** s), steeper than **r=5**'s **8e7→9e7** marginal (**~110.7** s) and than **r=9**'s **7e7→8e7** step (**~98.5** s). **`r=9`** remains faster than **`r=5`** at the same **9e7** cap (**~815** s vs **~827** s).
