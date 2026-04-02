# Results

**Outcome:** PASS

**Environment:** Cursor automation host; parent `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` with  
`--skip-baseline --r-single 3 --d-min 3 --d-max 3 --lru-maxsize 8000000 --max-exists-calls 50000000`.

**Command (repo root):**

```bash
python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r3-d3-exists-budget-5e7-lru-8m/script.py
```

**Observed:** Parent **exit 0**. Stdout:

```text
skip_baseline=1 (coord-only and full parity not run)
  probing d=3 ...
  exists_tree_cache_misses_after_d=3: 8000000
coord_plus_3xor count=364 min_d=None build_sec=0.353 dp_sec=81.958
  d=3 feasible=False sec=81.9578
PASS
```

**Metrics**

| Quantity | Value |
|----------|-------|
| `max_exists_calls` cap | 50,000,000 |
| `lru-maxsize` | 8,000,000 |
| `coord_plus_3xor` split count | 364 (= C(14,3)) |
| Certified `d=3 feasible` | **False** |
| `exists_tree` LRU misses at end of `d=3` probe | 8,000,000 (saturated) |
| Partition build time | ~0.35 s |
| DP wall time | ~82 s |
| Total wall ~ | ~94 s |

**Conclusion:** At **`n=14`**, **`{7,8}`**, **`r=3`**, the **full** **364**-split XOR menu yields a **definite** verdict: **`d=3` is infeasible** for **`coord + 3xor`** under this DP (**not** a budget **PARTIAL** like **`r=5`/`r=9`** at the same **5e7/8M** envelope). Together with prior **`r=2`** **`d=2`** infeasibility shards and the **`r=4`** **PARTIAL** at **5e7/8M**, this pins the low-**`r`** side: **small** **`C(14,r)`** does **not** imply **easy** **`d=3`** — **`r=3`** needs **depth ≥ 4** here, while **`r=5`/`r=9`** remain **open** at **`d=3`** (PARTIAL). LRU saturation (**8M** misses) shows the **82 s** probe is still **memo-bound**, but the search **completed** with **`feasible=False`**.

**Comparison (same envelope 5e7/8M, `n=14`, `{7,8}`):**

| `r` | `C(14,r)` | `d=3` at 5e7/8M |
|-----|-----------|------------------|
| 3 | 364 | **False** (this run) |
| 4 | 1001 | PARTIAL (cap) |
| 5 | 2002 | PARTIAL (cap) |
| … | … | … |
| 9 | 2002 | PARTIAL (cap) |
