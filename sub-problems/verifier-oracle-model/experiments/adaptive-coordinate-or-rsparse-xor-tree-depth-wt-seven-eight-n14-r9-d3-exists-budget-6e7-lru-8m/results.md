# Results

**Outcome:** INCONCLUSIVE (PARTIAL — budget exhausted before root decision)

**Environment:** Cursor automation host; parent `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` with  
`--skip-baseline --r-single 9 --d-min 3 --d-max 3 --lru-maxsize 8000000 --max-exists-calls 60000000`.

**Command (repo root):**

```bash
python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-6e7-lru-8m/script.py
```

**Observed:** Parent **exit 2** (PARTIAL). Stdout:

```text
skip_baseline=1 (coord-only and full parity not run)
  probing d=3 ...
  PARTIAL: exceeded max_exists_calls=60000000 (exists_tree invocations; LRU currsize=8000000) after 562.3164s
coord_plus_9xor count=2002 min_d=None build_sec=4.272 dp_sec=562.318
  d=3 feasible=False sec=562.3164
PARTIAL: r_single probe hit max_exists_calls
```

**Metrics**

| Quantity | Value |
|----------|-------|
| `max_exists_calls` cap | 60,000,000 |
| `lru-maxsize` | 8,000,000 |
| Wall DP time | ~562.32 s |
| Build time | ~4.27 s |
| LRU `currsize` at cutoff | 8,000,000 |
| Approx. invocations/s | ~1.07×10⁵ |

**Conclusion:** **H0** supported — **+20%** over **5×10⁷** still **PARTIAL** for **`r=9` `d=3`** at **8M** LRU; **H1** falsified. Mirrors **`r=5`** **6e7** outcome: the **2002-split** **`d=3`** class does **not** resolve at this modest budget bump for **either** **`r∈{5,9}`**.

**Comparison (same flags except `--max-exists-calls`, LRU 8M, `r=9`, `d=3`-only):**

| Budget | Outcome | DP wall |
|--------|---------|---------|
| 5×10⁷ | PARTIAL | ~542 s (see journal entry) |
| 6×10⁷ | PARTIAL | ~562.3 s |

**Cross-`r` at 6×10⁷ / 8M:**

| `r` | Outcome | DP wall |
|-----|---------|---------|
| 5 | PARTIAL | ~568.8 s |
| 9 | PARTIAL | ~562.3 s |
