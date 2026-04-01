# Results

**Outcome:** INCONCLUSIVE (PARTIAL — budget exhausted before root decision)

**Environment:** Cursor automation host; parent `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` with  
`--skip-baseline --r-single 5 --d-min 3 --d-max 3 --lru-maxsize 8000000 --max-exists-calls 50000000`.

**Command (repo root):**

```bash
python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-5e7-lru-8m/script.py
```

**Observed:** Parent **exit 2**. Stdout:

```text
skip_baseline=1 (coord-only and full parity not run)
  probing d=3 ...
  PARTIAL: exceeded max_exists_calls=50000000 (exists_tree invocations; LRU currsize=8000000) after 420.5530s
coord_plus_5xor count=2002 min_d=None build_sec=2.677 dp_sec=420.553
  d=3 feasible=False sec=420.5530
PARTIAL: r_single probe hit max_exists_calls
```

**Metrics**

| Quantity | Value |
|----------|-------|
| `max_exists_calls` | 50,000,000 |
| `lru-maxsize` | 8,000,000 |
| Wall DP time | ~420.55 s |
| LRU `currsize` at cutoff | 8,000,000 |
| Approx. invocations/s | ~1.19×10⁵ |

**Conclusion:** **10×** the prior **5×10⁶** invocation budget still does **not** decide **`r=5` `d=3`** under this memo policy. The **`r=5`/`d=3`** shard remains in the **heavy undecided** class; next comparable bracket is **r=6** at **(5e7, LRU 8M)**, or **unbounded** memo on a **large-RAM** host / process sharding.
