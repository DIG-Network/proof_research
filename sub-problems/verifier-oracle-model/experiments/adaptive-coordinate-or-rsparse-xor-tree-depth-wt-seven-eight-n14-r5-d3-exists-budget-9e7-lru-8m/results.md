# Results

**Outcome:** INCONCLUSIVE (parent exit **2** — PARTIAL: budget exhausted during `d=3` probe).

**Configuration:** `n=14`, shells `{7,8}`, `coord + r=5` XOR (2002 splits), `--d-min 3 --d-max 3`, `--max-exists-calls 90000000`, `--lru-maxsize 8000000`, `--skip-baseline`.

**Measured:**
- `exists_tree` budget hit at **9×10⁷** invocations; LRU saturated at **8×10⁶** entries.
- Parent-reported `dp_sec` for `d=3` segment: **~826.80 s** (~13.78 min); partition build **~2.74 s**.
- Wall clock for wrapper run: **~860 s**.
- Parent printed `d=3 feasible=False` after PARTIAL line (not certified completion).

**Comparison:** +10M calls over **8e7** added **~110.7 s** DP time (**~826.8** vs **~716.1** s), steeper than **7e7→8e7** (**~72.3** s). Dual **2002** band still **PARTIAL** at **9e7/8M**.
