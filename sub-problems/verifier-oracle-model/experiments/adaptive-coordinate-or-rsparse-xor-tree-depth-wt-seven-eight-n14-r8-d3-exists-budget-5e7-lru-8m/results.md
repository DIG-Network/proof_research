# Results

**Outcome:** PASS

**Environment:** Cursor automation host; parent `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` with  
`--skip-baseline --r-single 8 --d-min 3 --d-max 3 --lru-maxsize 8000000 --max-exists-calls 50000000`.

**Command (repo root):**

```bash
python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r8-d3-exists-budget-5e7-lru-8m/script.py
```

**Observed:** Parent **exit 0**. Stdout:

```text
skip_baseline=1 (coord-only and full parity not run)
  probing d=3 ...
coord_plus_8xor count=3003 min_d=3 build_sec=5.783 dp_sec=510.101
  d=3 feasible=True sec=510.1006
PASS
```

**Metrics**

| Quantity | Value |
|----------|-------|
| `max_exists_calls` cap | 50,000,000 |
| `lru-maxsize` | 8,000,000 |
| `coord_plus_8xor` split count | 3003 (= C(14,8) = C(14,6)) |
| Certified `min_d` | 3 |
| `d=3 feasible` | True |
| Partition build time | ~5.78 s |
| DP wall time | ~510.10 s |
| Total wall ~ | ~516 s |

**Conclusion:** Under the **same** **(5×10⁷, LRU 8M)** envelope, **`r=8` `d=3`** **PASS**es with **`min_d=3`**, like **`r=6`** (**3003** XOR splits), **not** like **`r=5`/`r=9`** (**2002** splits, **PARTIAL**). So at this scale **menu cardinality** (**3003 vs 2002**) aligns with **easy vs hard** more cleanly than the **`(5,9)`** dual pair alone — **`r=8`** and **`r=6`** share **count** and **both** complete; **`r=5`** and **`r=9`** share **count** and **both** hit budget at **PARTIAL**.

**Comparison (same parent flags except `--r-single`, 5e7 + LRU 8M):**

| Shard | Split count | Outcome |
|-------|-------------|---------|
| `r=5` | 2002 | INCONCLUSIVE (PARTIAL) |
| `r=6` | 3003 | PASS (`min_d=3`, ~435 s) |
| `r=8` | 3003 | PASS (`min_d=3`, ~510 s) |
| `r=9` | 2002 | INCONCLUSIVE (PARTIAL, ~542 s) |
