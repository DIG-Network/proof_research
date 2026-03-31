# Hypothesis

**Claim:** Replacing `functools.lru_cache` in `exists_tree` with a disk-backed key-value store (SQLite or `dbm.ndbm`) will allow certifying standalone `min_d(5)` and `min_d(7)` on memory-capped hosts while finishing in wall-clock time comparable to in-RAM DP (within a constant factor).

**Falsifiable if:** Random read/write latency per memo entry makes total time orders of magnitude worse than in-RAM, or the DP’s access pattern (millions of small keys) saturates disk IOPS before completion.

## Analogy pass (abbreviated)

1. **Abstract structure:** Recursive decision procedure over a huge bitmask state space with overlapping subproblems → memoization reduces exponential re-computation to one visit per state per depth.
2. **Analogous domains:** Dynamic programming on graphs with external memory; database-backed memo in chess engines; out-of-core BFS layers.
3. **Machinery there:** Batching, locality-friendly layouts, or accepting RAM for hot states.
4. **Transfer candidate:** Batched SQLite transactions or `dbm` as a drop-in LRU replacement.

**Seed:** If batching hides sync cost, disk memo might be viable.
