# Results

**Outcome:** FAIL (hypothesis falsified on stated budget/time)

**Environment:** Cursor automation host; parent `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` with  
`--skip-baseline --r-single 5 --d-min 3 --d-max 3 --lru-maxsize 0 --max-exists-calls 5000000`.

**Command (repo root):**

```bash
python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-5e6/script.py
```

**Observed:** Parent **exit 2**. Stdout (abridged):

```text
skip_baseline=1 (coord-only and full parity not run)
  probing d=3 ...
  PARTIAL: exceeded max_exists_calls=5000000 (exists_tree invocations; LRU currsize=4999997) after 38.6330s
coord_plus_5xor count=2002 min_d=None build_sec=2.738 dp_sec=38.633
  d=3 feasible=False sec=38.6330
PARTIAL: r_single probe hit max_exists_calls
```

**Metrics (from log):**

- `exists_tree` **invocation budget:** 5,000,000 (counter increments on every call through `lru_cache`, i.e. hits + misses).
- **Wall time** for the partial `d=3` probe: **~38.6 s**.
- **LRU table size** at cutoff: **4,999,997** distinct `(bits, depth_remaining)` states memoized.

**Conclusion:** The **5×10⁶** invocation cap is **far below** what is needed to finish the **unbounded-memo** `d=3` decision for **`r=5`** in this shard (consistent with **multi-hour** timeouts that never printed `feasible=`). The run **does** give a **reproducible scale**: ~**7.7×10⁴** invocations/s and ~**1.3×10⁻⁵** s per invocation on this host for this phase.

**Parent change:** `script.py` now accepts `--max-exists-calls K` for bounded / partial probes (exit **2** = partial).
