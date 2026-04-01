# Results

**Outcome:** INCONCLUSIVE (PARTIAL — budget exhausted before root decision)

**Environment:** Cursor automation host; parent `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` with  
`--skip-baseline --r-single 4 --d-min 3 --d-max 3 --lru-maxsize 8000000 --max-exists-calls 50000000`.

**Command (repo root):**

```bash
python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r4-d3-exists-budget-5e7-lru-8m/script.py
```

**Observed:** Parent **exit 2**. Stdout:

```text
skip_baseline=1 (coord-only and full parity not run)
  probing d=3 ...
  PARTIAL: exceeded max_exists_calls=50000000 (exists_tree invocations; LRU currsize=8000000) after 467.2116s
coord_plus_4xor count=1001 min_d=None build_sec=1.186 dp_sec=467.212
  d=3 feasible=False sec=467.2116
PARTIAL: r_single probe hit max_exists_calls
```

**Metrics**

| Quantity | Value |
|----------|-------|
| `max_exists_calls` | 50,000,000 |
| `lru-maxsize` | 8,000,000 |
| `coord_plus_4xor` split count | 1001 (= C(14,4) = C(14,10)) |
| Certified `min_d` | None (run truncated) |
| Partition build time | ~1.19 s |
| DP wall time to cutoff | ~467.21 s |
| LRU `currsize` at cutoff | 8,000,000 |
| Approx. invocations/s | ~1.07×10⁵ |

**Conclusion:** **`r=4`** at the **same** **5e7/8M** envelope as **`r=10`** **PARTIAL**s — **identical** split count **1001**, but **~8.5×** **longer** DP to cap than **`r=10`** (**~55 s** **PASS**). **Binomial duality** **`C(14,r)=C(14,14−r)`** does **not** preserve **adaptive-tree DP** hardness: **low-**`r`** 4-sparse XOR** can be **as heavy** as the **2002** band at this budget, while **high-**`r`** 10-sparse** is **easy**.

**Comparison (same envelope, 1001 splits):**

| Shard | Split count | Outcome | DP time (approx.) |
|-------|-------------|---------|-------------------|
| `r=10` | 1001 | PASS | ~55 s |
| `r=4` | 1001 | INCONCLUSIVE (PARTIAL) | ~467 s (cap) |
