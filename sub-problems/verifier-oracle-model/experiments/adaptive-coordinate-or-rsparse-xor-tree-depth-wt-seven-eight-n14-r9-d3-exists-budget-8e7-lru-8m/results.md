# Results

**Outcome:** INCONCLUSIVE (parent exit **2** — PARTIAL: budget exhausted during `d=3` probe).

**Configuration:** `n=14`, shells `{7,8}`, `coord + r=9` XOR (2002 splits), `--d-min 3 --d-max 3`, `--max-exists-calls 80000000`, `--lru-maxsize 8000000`, `--skip-baseline`.

**Measured:**
- `exists_tree` budget hit at **8×10⁷** invocations; LRU saturated at **8×10⁶** entries.
- Parent-reported `dp_sec` for `d=3` segment: **~693.77 s** (~11.56 min); partition build **~4.28 s**.
- Wall clock for wrapper run: **~736 s**.
- Parent printed `d=3 feasible=False` after PARTIAL line (not certified completion).

**Comparison:** +10M calls over **7e7** added **~98.5 s** DP time vs prior **~595.3** s at **7e7** (marginal cost higher than **r=5**'s **~72** s for the same +10M step). Both **2002** dual runs **PARTIAL** at **8e7/8M**.
