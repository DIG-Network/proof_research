# Results

**Outcome:** INCONCLUSIVE (parent exit **2** — PARTIAL: budget exhausted during `d=3` probe).

**Configuration:** `n=14`, shells `{7,8}`, `coord + r=5` XOR (2002 splits), `--d-min 3 --d-max 3`, `--max-exists-calls 70000000`, `--lru-maxsize 8000000`, `--skip-baseline`.

**Measured:**
- `exists_tree` budget hit at **7×10⁷** invocations; LRU saturated at **8×10⁶** entries.
- Wall time for `d=3` probe segment: **~643.74 s** (~10.73 min); build **~2.67 s**.
- Parent printed `d=3 feasible=False` after PARTIAL line (same wrapper semantics as prior 6e7 run — not treated as certified completion).

**Comparison:** +10M calls over **6e7** added **~74 s** (~643.7 vs ~568.8 s) and **did not** yield a non-PARTIAL termination.
