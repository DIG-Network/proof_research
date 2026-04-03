# Results — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-shard-eighths-3e7-each-lru-8m

**Outcome (journal):** **PASS** — all eight contiguous XOR eighth-shards finished **`d=3`** without **`max_exists_calls` PARTIAL**; each **`d=3 feasible=False`**. **Wrapper exit code:** **1** (no **`feasible=True`** witness; same convention as quarter wrappers).

**Aggregate budget:** **8 × 3×10⁷ = 2.4×10⁸** `exists_tree` cap per eighth — **same total** as **four × 6×10⁷** quarters.

| Eighth | `xor-index-range` | splits | `build_sec` | `dp_sec` | `exists_tree_cache_misses_after_d=3` |
|--------|-------------------|--------|-------------|----------|----------------------------------------|
| e0 | `0:251` | 251 | ~2.669 | ~22.429 | 2_835_863 |
| e1 | `251:502` | 251 | ~2.650 | ~19.660 | 2_647_808 |
| e2 | `502:753` | 251 | ~2.661 | ~17.490 | 2_545_208 |
| e3 | `753:1004` | 251 | ~3.389 | ~18.946 | 2_631_113 |
| e4 | `1004:1255` | 251 | ~2.711 | ~19.414 | 2_547_242 |
| e5 | `1255:1506` | 251 | ~2.637 | ~18.014 | 2_598_455 |
| e6 | `1506:1757` | 251 | ~2.645 | ~17.943 | 2_549_486 |
| e7 | `1757:2002` | 245 | ~2.940 | ~15.098 | 1_916_958 |

**Total sequential wall (wrapper):** ~**183.2 s** (~**3.05 min**).

**Key comparison to quarters:** Quarter shards (~501 splits) at **6×10⁷** each **saturated** **8M** LRU on every quarter (~**1491 s** total). Eighths (~251 splits) at **3×10⁷** each stay **well under** **8M** misses (max ~**2.84×10⁶**) and finish **~8× faster** wall-clock at the **same** **2.4×10⁸** aggregate budget cap — so the quarter completion phenomenon was **memoization / working-set** pressure at **~500**-split scale, not merely “total invocation budget.”

**Implication:** Definite **`d=3`** **`False`** on **eighth** sub-menus **agrees** with **quarter** negatives; **no** witness. Still **not** a full-menu **`min_d`** proof.

**Repro:** `python3 -u sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-shard-eighths-3e7-each-lru-8m/script.py`
