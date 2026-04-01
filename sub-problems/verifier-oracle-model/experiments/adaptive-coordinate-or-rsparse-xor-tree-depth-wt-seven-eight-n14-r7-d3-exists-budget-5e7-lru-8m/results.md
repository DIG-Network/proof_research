# Results

**Outcome:** PASS

**Environment:** Cursor automation host; parent `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` with  
`--skip-baseline --r-single 7 --d-min 3 --d-max 3 --lru-maxsize 8000000 --max-exists-calls 50000000`.

**Command (repo root):**

```bash
python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r7-d3-exists-budget-5e7-lru-8m/script.py
```

**Observed:** Parent **exit 0**. Stdout:

```text
skip_baseline=1 (coord-only and full parity not run)
  probing d=3 ...
coord_plus_7xor count=3432 min_d=3 build_sec=5.824 dp_sec=0.543
  d=3 feasible=True sec=0.5426
PASS
```

**Metrics**

| Quantity | Value |
|----------|-------|
| `max_exists_calls` cap | 50,000,000 |
| `lru-maxsize` | 8,000,000 |
| `coord_plus_7xor` split count | 3432 |
| Certified `min_d` | 3 |
| `d=3 feasible` | True |
| Partition build time | ~5.82 s |
| DP wall time | ~0.54 s |
| Total wall ~ | ~6.7 s |

**Conclusion:** At **`n=14`**, **`{7,8}`**, **`r=7`**, the **full** **`C(14,7)=3432`** XOR menu completes **`d=3`** verification **trivially** under **5e7/8M** — consistent with the prior **5e6** shard where **`r=7`** was already **fast**. **Cardinality alone** does **not** sort hardness in the **2002–3432** window: **3432** is **easy** while **2002** (**`r=5`/`r=9`**) remains **PARTIAL** at the same envelope. The **hard pocket** is **parity-pattern / split-geometry** dependent, not a simple function of **`C(14,r)`**.

**Comparison (same parent flags except `--r-single`, 5e7/8M):**

| `r` | `C(14,r)` | Outcome at 5e7/8M | DP order of magnitude |
|-----|-----------|-------------------|------------------------|
| 5 | 2002 | PARTIAL | ~420 s, cap |
| 6 | 3003 | PASS | ~435 s |
| 7 | 3432 | PASS | **~0.5 s** |
| 8 | 3003 | PASS | ~510 s |
| 9 | 2002 | PARTIAL | ~542 s, cap |
| 10 | 1001 | PASS | ~55 s |
| 4 | 1001 | PARTIAL | ~467 s, cap |
