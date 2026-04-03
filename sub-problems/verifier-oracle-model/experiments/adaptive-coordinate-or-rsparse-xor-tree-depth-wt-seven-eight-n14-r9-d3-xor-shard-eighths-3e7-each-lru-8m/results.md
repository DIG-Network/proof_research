# Results — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-eighths-3e7-each-lru-8m

**Outcome (journal):** **PASS** — all eight XOR eighth-shards finished **`d=3`** without **`max_exists_calls` PARTIAL**; each **`d=3 feasible=False`**. **Wrapper exit code:** **1** (no **`feasible=True`** witness).

**Aggregate budget:** **8 × 3×10⁷ = 2.4×10⁸** (same partition and cap as **`r=5`** eighths).

| Eighth | `xor-index-range` | splits | `build_sec` | `dp_sec` | `exists_tree_cache_misses_after_d=3` |
|--------|-------------------|--------|-------------|----------|----------------------------------------|
| e0 | `0:251` | 251 | ~4.067 | ~17.428 | 2_174_711 |
| e1 | `251:502` | 251 | ~4.125 | ~17.703 | 2_547_284 |
| e2 | `502:753` | 251 | ~4.095 | ~17.279 | 2_607_995 |
| e3 | `753:1004` | 251 | ~4.069 | ~17.168 | 2_551_706 |
| e4 | `1004:1255` | 251 | ~4.050 | ~18.019 | 2_643_908 |
| e5 | `1255:1506` | 251 | ~4.052 | ~16.592 | 2_577_773 |
| e6 | `1506:1757` | 251 | ~4.123 | ~19.556 | 2_682_926 |
| e7 | `1757:2002` | 245 | ~4.053 | ~18.000 | 2_646_279 |

**Total sequential wall (wrapper):** ~**185.0 s** (~**3.08 min**).

**Key comparison:** Mirrors **`r=5`** eighths: **no** **8M** LRU saturation (max misses ~**2.68×10⁶**), complete **`d=3`** **`False`** on every eighth. Wall ~**1%** slower than **`r=5`** (~**185 s** vs ~**183 s**), same order as quarter **`r=9`** vs **`r=5`** gap (~**5%** at **6e7** quarters).

**Repro:** `python3 -u sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-eighths-3e7-each-lru-8m/script.py`
