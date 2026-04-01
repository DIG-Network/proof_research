# Results

**Outcome:** PASS

**Environment:** Cursor automation host; parent `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` with  
`--skip-baseline --r-single 6 --d-min 3 --d-max 3 --lru-maxsize 8000000 --max-exists-calls 50000000`.

**Command (repo root):**

```bash
python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r6-d3-exists-budget-5e7-lru-8m/script.py
```

**Observed:** Parent **exit 0**. Stdout:

```text
skip_baseline=1 (coord-only and full parity not run)
  probing d=3 ...
coord_plus_6xor count=3003 min_d=3 build_sec=4.546 dp_sec=435.336
  d=3 feasible=True sec=435.3355
PASS
```

**Metrics**

| Quantity | Value |
|----------|-------|
| `max_exists_calls` cap | 50,000,000 |
| `lru-maxsize` | 8,000,000 |
| `coord_plus_6xor` split count | 3003 |
| Certified `min_d` | 3 |
| `d=3 feasible` | True |
| Partition build time | ~4.55 s |
| DP wall time | ~435.34 s |
| Total wall ~ | ~440 s |

**Conclusion:** Under the **same** **(5×10⁷, LRU 8M)** resource envelope that left **`r=5` `d=3`** **PARTIAL** (budget exhausted, LRU at cap), **`r=6` `d=3`** **completes** and certifies **`min_d=3`**. So the **`n=14` `{7,8}`** hard pocket is **not uniform** across **`r=5` vs `r=6`** at this scale — **`r=6`** is strictly **easier** than **`r=5`** here (consistent with the earlier **`5e6`** shard where both were PARTIAL, but **`5e7`** suffices for **`r=6`**).

**Comparison (same parent flags except `--r-single`):**

| Shard | Outcome at 5e7 + LRU 8M |
|-------|-------------------------|
| `r=5` | INCONCLUSIVE (PARTIAL, 50M calls exhausted) |
| `r=6` | PASS (`d=3` feasible, ~435 s DP) |
