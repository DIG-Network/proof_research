# Results — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-shard-quarters-6e7-each-lru-8m

**Outcome (journal):** **PASS** — experiment completed cleanly: all four quarter-shards finished **`d=3`** without **`max_exists_calls` PARTIAL**; each **`d=3 feasible=False`**. **Wrapper process exit code:** **1** (same convention as half-shard wrappers: no **`feasible=True`** witness ⇒ exit **1**).

**Aggregate budget:** **4 × 6×10⁷ = 2.4×10⁸** `exists_tree` invocations — matches **two × 12×10⁷** half-shard runs that were **both PARTIAL**.

| Quarter | `xor-index-range` | splits | DP sec | `exists_tree_cache_misses_after_d=3` |
|---------|-------------------|--------|--------|----------------------------------------|
| q0 | `0:501` | 501 | ~400.57 | 8_000_000 (saturated) |
| q1 | `501:1002` | 501 | ~343.06 | 8_000_000 |
| q2 | `1002:1503` | 501 | ~332.03 | 8_000_000 |
| q3 | `1503:2002` | 499 | ~286.74 | 8_000_000 |

**Total sequential wall:** ~**1491 s** (~**24.9 min**) for the wrapper (four subprocesses).

**Key comparison:** **Half-shards** **`[0:1001)`** / **`[1001:2002)`** at **12×10⁷** each **did not** finish (`PARTIAL`). **Quarter-shards** (~501 splits) at **6×10⁷** each **do** finish with a definite **`feasible=False`** at **`d=3`**. So **finer contiguous XOR blocking** + **same per-shard budget class** crosses from **budget truncation** to **complete negative** at **`d=3`** for this **`r=5`** menu.

**Implication for full-menu `d=3`:** These negatives are **not** a sound proof that the **full** **2002**-split language has **`min_d > 3`** (sub-menu ⇒ only **lower** bounds on **min depth**). They **do** show **quarter** sub-menus are **not** deep-3 witnesses.

**Repro:** `python3 -u sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-shard-quarters-6e7-each-lru-8m/script.py`
