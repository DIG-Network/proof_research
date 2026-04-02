# Results

**Outcome:** INCONCLUSIVE (wrapper exit **2**).

**Setup:** `n=14`, shells `{7,8}`, parent `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py`, `--skip-baseline`, `--r-single 9`, `d=3`-only, contiguous XOR halves `[0:1001)` and `[1001:2002)` (1001 splits each), **`15×10⁷`** `exists_tree` per half, **`10M`** LRU, **sequential** runs.

| Half | xor range | build (s) | DP until PARTIAL (s) | LRU currsize |
|------|-----------|-----------|----------------------|--------------|
| shard_0_1001 | 0:1001 | ~4.19 | ~1167.36 | 10M |
| shard_1001_2002 | 1001:2002 | ~4.08 | ~1117.52 | 10M |

Both subprocesses exited **2** (PARTIAL). Parsed `d=3 feasible=False` lines are **post-budget** states, not completed decisions. **No** `d=3 feasible=True` witness.

**Total wall (sequential):** ~**2289 s** (~**38.1 min**).

**vs prior `r=9` half-shards:** **`12e7/8M`** **~974 + ~912** s DP (**~1886** s); **`12e7/10M`** **~1034 + ~992** s (**~2026** s). This run **+25%** visit cap (**15e7**) with **10M** LRU yields **~1167 + ~1118** s (**~2285** s)—**longer** wall time but **still** dual PARTIAL; the extra budget does **not** cross a completion threshold on either half.

**Conclusion:** Joint uplift **15e7 / 10M** on **`r=9`** contiguous half-shards does **not** resolve **`d=3`**; next steps remain **larger host**, **structural DP change**, or **different** menu geometry—not another fixed **1001**-coset sweep at similar envelopes.
