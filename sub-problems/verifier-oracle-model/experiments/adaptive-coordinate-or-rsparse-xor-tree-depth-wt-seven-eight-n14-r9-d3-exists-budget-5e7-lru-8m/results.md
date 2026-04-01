# Results

**Outcome:** INCONCLUSIVE

**Environment:** Cursor automation host; parent `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` with  
`--skip-baseline --r-single 9 --d-min 3 --d-max 3 --lru-maxsize 8000000 --max-exists-calls 50000000`.

**Command (repo root):**

```bash
python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-exists-budget-5e7-lru-8m/script.py
```

**Observed:** Parent **exit 2** (PARTIAL). Stdout:

```text
skip_baseline=1 (coord-only and full parity not run)
  probing d=3 ...
  PARTIAL: exceeded max_exists_calls=50000000 (exists_tree invocations; LRU currsize=8000000) after 542.0639s
coord_plus_9xor count=2002 min_d=None build_sec=4.229 dp_sec=542.064
  d=3 feasible=False sec=542.0639
PARTIAL: r_single probe hit max_exists_calls
```

**Metrics**

| Quantity | Value |
|----------|-------|
| `max_exists_calls` cap | 50,000,000 |
| `lru-maxsize` | 8,000,000 |
| `coord_plus_9xor` split count | 2002 (= C(14,9) = C(14,5)) |
| Certified `min_d` | none (PARTIAL before root decision) |
| Time to budget exhaust | ~542.06 s |
| LRU at stop | 8,000,000 (at cap) |
| Partition build time | ~4.23 s |

**Conclusion:** Under the **same** **(5×10⁷, LRU 8M)** envelope where **`r=6` `d=3`** **PASS**es (~435 s) and **`r=5` `d=3`** **PARTIAL**s (~421 s), **`r=9` `d=3`** also **PARTIAL**s — budget exhausted with LRU at cap in ~**542 s**. So **`r=9`** is **not** in the “easy” **`r=6`** class at this scale; it **resembles `r=5`** (hard for a definite `d=3` bit at 50M/8M). **Equal XOR split count** (**2002**) for **`r=5` vs `r=9`** does **not** align their difficulty here — the **parity pattern** matters.

**Comparison (same parent flags except `--r-single`, 5e7 + LRU 8M):**

| Shard | Outcome |
|-------|---------|
| `r=5` | INCONCLUSIVE (PARTIAL, ~421 s) |
| `r=6` | PASS (`min_d=3`, ~435 s) |
| `r=9` | INCONCLUSIVE (PARTIAL, ~542 s) |

**Note:** Prior **unbounded**-memo **`r=9` `d=3`** runs (e.g. 90 min) also failed to print **`feasible=`**; this bounded run is **consistent** with **`r=9` staying hard**, but still **does not** certify full-menu infeasibility at `d=3`.
