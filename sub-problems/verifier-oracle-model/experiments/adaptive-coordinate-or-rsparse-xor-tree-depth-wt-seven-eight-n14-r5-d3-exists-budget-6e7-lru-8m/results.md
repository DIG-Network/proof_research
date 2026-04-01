# Results

**Outcome:** INCONCLUSIVE (PARTIAL — budget exhausted before root decision)

**Environment:** Cursor automation host; parent `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` with  
`--skip-baseline --r-single 5 --d-min 3 --d-max 3 --lru-maxsize 8000000 --max-exists-calls 60000000`.

**Command (repo root):**

```bash
python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-6e7-lru-8m/script.py
```

**Observed:** Parent **exit 2** (PARTIAL). Stdout:

```text
skip_baseline=1 (coord-only and full parity not run)
  probing d=3 ...
  PARTIAL: exceeded max_exists_calls=60000000 (exists_tree invocations; LRU currsize=8000000) after 568.8427s
coord_plus_5xor count=2002 min_d=None build_sec=2.652 dp_sec=568.846
  d=3 feasible=False sec=568.8427
PARTIAL: r_single probe hit max_exists_calls
```

**Metrics**

| Quantity | Value |
|----------|-------|
| `max_exists_calls` cap | 60,000,000 |
| `lru-maxsize` | 8,000,000 |
| Wall DP time | ~568.84 s |
| LRU `currsize` at cutoff | 8,000,000 |
| Approx. invocations/s | ~1.05×10⁵ |

**Conclusion:** **+20%** invocation budget over the **5×10⁷** run **still** ends in **PARTIAL** with LRU at cap — **no** definite `min_d` / root feasibility bit for **`r=5` `d=3`**. The extra **10M** calls consumed **~148 s** additional wall time vs ~421 s at 50M (similar per-call rate once cache is warm). **H0** (still PARTIAL) is supported; **H1** (definite verdict at 6e7) is **falsified**.

**Comparison (same flags except `--max-exists-calls`, LRU 8M, `r=5`, `d=3`-only):**

| Budget | Outcome | DP wall |
|--------|---------|---------|
| 5×10⁷ | PARTIAL | ~420.6 s |
| 6×10⁷ | PARTIAL | ~568.8 s |

**Implication:** The **50M** cutoff is **not** sitting just below a completion threshold for this shard; larger budgets (or unbounded memo on a high-RAM host / sharding) remain the next levers — mirroring the **`r=9`** situation at **5e7/8M** (~542 s PARTIAL).
