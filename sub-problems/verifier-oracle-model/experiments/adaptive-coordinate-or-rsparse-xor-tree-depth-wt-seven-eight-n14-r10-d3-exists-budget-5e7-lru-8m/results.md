# Results

**Outcome:** PASS

**Environment:** Cursor automation host; parent `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` with  
`--skip-baseline --r-single 10 --d-min 3 --d-max 3 --lru-maxsize 8000000 --max-exists-calls 50000000`.

**Command (repo root):**

```bash
python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r10-d3-exists-budget-5e7-lru-8m/script.py
```

**Observed:** Parent **exit 0**. Stdout:

```text
skip_baseline=1 (coord-only and full parity not run)
  probing d=3 ...
coord_plus_10xor count=1001 min_d=3 build_sec=2.369 dp_sec=54.589
  d=3 feasible=True sec=54.5887
PASS
```

**Metrics**

| Quantity | Value |
|----------|-------|
| `max_exists_calls` cap | 50,000,000 |
| `lru-maxsize` | 8,000,000 |
| `coord_plus_10xor` split count | 1001 (= C(14,10) = C(14,4)) |
| Certified `min_d` | 3 |
| `d=3 feasible` | True |
| Partition build time | ~2.37 s |
| DP wall time | ~54.59 s |
| Total wall ~ | ~62 s |

**Conclusion:** At **5e7/8M**, **`r=10`** (**1001** XOR splits) **PASS**es with **`min_d=3`** in **~55 s** — **much faster** than **3003-split** **`r=6`/`r=8`** (**~435–510 s**) and **far below** budget saturation. **Menu cardinality alone** does not predict runtime here: **1001** is **easier** than **2002** (**`r=5`/`r=9` PARTIAL**) and **3003** (**`r=6`/`r=8` PASS**). The earlier narrative that **`r=10`** shares **2002** with **`r=5`/`r=9`** was **arithmetically wrong** for **`n=14`**: **`C(14,10)=1001`**, not **2002**.

**Comparison (same parent flags except `--r-single`, 5e7 + LRU 8M):**

| Shard | Split count | Outcome | DP time (approx.) |
|-------|-------------|---------|-------------------|
| `r=10` | 1001 | PASS | ~55 s |
| `r=5` / `r=9` | 2002 | INCONCLUSIVE (PARTIAL) | ~420–542 s |
| `r=6` / `r=8` | 3003 | PASS | ~435–510 s |
