# Hypothesis — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-partition-shard-scan-400`

## Analogy pass (abbreviated)

1. **Abstract structure:** The `r=5` language is coord splits plus a menu of 2002 XOR-derived bipartitions. Full DP blows memory or budgets; we want **decomposition** of the menu into shards that each fit an LRU cap while still allowing **positive** certificates (if any shard admits depth-3 decision trees, the full language does too).

2. **Analogous domains:** Graph sparsification; divide-and-conquer on hyperedge lists; partial basis scans in matroid intersection.

3. **Machinery elsewhere:** Slice large generator sets; prove feasibility from subsets (sound one-way only).

4. **Transfer candidate:** Add `--xor-index-range START:END` on the parent `n=14` script so each run uses a contiguous slice of the `r=5` XOR partition list; run shards that **partition** `[0,2002)` and search for `d=3 feasible=True`. Negative `feasible=False` on a shard **does not** imply infeasibility of the full menu (strict subset of splits); only `True` would certify `min_d ≤ 3` for the full language.

## Falsifiable claim

**H1 (engineering):** With `--lru-maxsize 8000000` and `--max-exists-calls 55000000`, every half-open slice of length ~400 completes `d=3` probing without OOM on this host.

**H2 (search):** Across a partition of all 2002 XOR indices into five contiguous shards, **no** shard reports `d=3 feasible=True` (so we obtain **no** positive witness for full-menu depth-3 feasibility from this sharding strategy).

If H1 fails (SIGKILL / PARTIAL), the hypothesis is falsified. If H2 is false (any shard prints `feasible=True`), the full-menu `min_d` for `r=5` is **at most** 3 (certificate).
