# Results

**Outcome:** INCONCLUSIVE (parent exit **2**, **`PARTIAL`** — budget exhausted during **`d=3`** probe).

**Command:** `python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-3e7-memo-dict/script.py`

**Measured:**

| Quantity | Value |
|----------|-------|
| `max_exists_calls` | 30_000_000 |
| Memo | `--memo-dict` (unbounded dict; no LRU eviction) |
| `memo_dict_size` at cutoff | 12_256_532 |
| DP wall time (`d=3` probe only) | ~112.53 s |
| XOR partition build | ~2.67 s |
| End-to-end (subprocess wrapper) | ~120.1 s |

**Interpretation:** At **3×10⁷** invocations the dict memo holds **~12.3M** distinct **`(bits, depth)`** states before the budget trips — **no** completion of the **`d=3`** feasibility check for the full **2002**-split **`r=5`** menu. Wall time is **far below** the **~2600 s** class of the **3×10⁸ / 10M LRU** **PARTIAL**, consistent with the microbench finding that **`--memo-dict`** avoids LRU thrashing; scaling invocation budget upward remains the next lever for a definite **`d=3`** verdict.
