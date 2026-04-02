# Results

**Outcome:** INCONCLUSIVE (wrapper exit **2**).

**Setup:** `n=14`, shells `{7,8}`, parent `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py`, `--skip-baseline`, `--r-single 5`, `d=3`-only, contiguous XOR halves `[0:1001)` and `[1001:2002)` (1001 splits each), **`7×10⁷`** `exists_tree` per half, **`8M`** LRU, **sequential** runs.

| Half | xor range | build (s) | DP until PARTIAL (s) | LRU currsize |
|------|-----------|-----------|----------------------|--------------|
| shard_0_1001 | 0:1001 | ~2.74 | ~540.04 | 8M |
| shard_1001_2002 | 1001:2002 | ~2.67 | ~537.30 | 8M |

Both subprocesses exited **2** (PARTIAL). Parsed `d=3 feasible=False` lines are **post-budget** states, not completed decisions. **No** `d=3 feasible=True` witness.

**Total wall (sequential):** ~**1082 s** (~**18 min**).

**Comparison:** Full-menu `r=5` at **7e7/8M** was PARTIAL ~**644 s** on all 2002 splits. Each **half** at the **same** per-run budget finished PARTIAL in ~**540 s**—**not** ~half the full-menu time, suggesting the hard part of the search is not evenly split by contiguous XOR index order (or cache/memo interaction differs).
