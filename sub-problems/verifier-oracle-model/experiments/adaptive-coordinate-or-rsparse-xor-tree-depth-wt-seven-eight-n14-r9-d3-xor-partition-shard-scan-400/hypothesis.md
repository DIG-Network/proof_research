# Hypothesis — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-partition-shard-scan-400`

## Analogy pass (abbreviated)

1. **Abstract structure:** The `r=9` language uses the same 2002 XOR-derived bipartitions as `r=5` (complement symmetry on `n=14`). Full-menu DP at `5e7`/`8M` hit PARTIAL; sharding tests whether **any contiguous block** of splits admits `d=3` feasibility (positive witness) or consistently reports `feasible=False`.

2. **Analogous domains:** Same divide-and-conquer on generator menus as the `r=5` shard scan; matroid / hypergraph slice search.

3. **Machinery elsewhere:** Partition indices; per-shard DP with fixed LRU and exists cap.

4. **Transfer candidate:** Reuse `--xor-index-range` with `--r-single 9` and identical shard boundaries as `…-n14-r5-d3-xor-partition-shard-scan-400`.

## Falsifiable claim

**H1 (engineering):** With `--lru-maxsize 8000000` and `--max-exists-calls 55000000`, each contiguous slice (~400 splits) completes `d=3` probing without OOM or PARTIAL on this host.

**H2 (search):** Across the five shards partitioning `[0,2002)`, **no** shard reports `d=3 feasible=True`.

If H1 fails, falsified. If any shard prints `feasible=True`, the full `r=9` menu has `min_d ≤ 3` (certificate).
