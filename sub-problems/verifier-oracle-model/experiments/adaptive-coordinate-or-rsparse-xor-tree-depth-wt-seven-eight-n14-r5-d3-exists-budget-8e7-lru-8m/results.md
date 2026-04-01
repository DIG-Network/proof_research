# Results

**Outcome:** INCONCLUSIVE (parent exit **2** — PARTIAL: budget exhausted during `d=3` probe).

**Configuration:** `n=14`, shells `{7,8}`, `coord + r=5` XOR (2002 splits), `--d-min 3 --d-max 3`, `--max-exists-calls 80000000`, `--lru-maxsize 8000000`, `--skip-baseline`.

**Measured:**
- `exists_tree` budget hit at **8×10⁷** invocations; LRU saturated at **8×10⁶** entries.
- Parent-reported `dp_sec` for `d=3` segment: **~716.08 s** (~11.93 min); partition build **~2.71 s**.
- Wall clock for wrapper run (including startup): **~749 s**.
- Parent printed `d=3 feasible=False` after PARTIAL line (same wrapper semantics as 7e7 — not treated as certified completion).

**Comparison:** +10M calls over **7e7** added **~72.3 s** DP time (**~716.1** vs **~643.7** s), similar marginal cost to **6e7→7e7** (~74 s). Still **no** non-PARTIAL termination.
