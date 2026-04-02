# Hypothesis

## Analogy pass

1. **Abstract structure:** The DP probe over a fixed XOR-index menu is embarrassingly parallel across disjoint index ranges; wall-clock is dominated by sequential composition of two halves even when total work is unchanged.
2. **Analogous domains:** (a) MapReduce-style partition-aggregate where reducers are independent; (b) branch-and-bound with disjoint subspaces; (c) SIMD / multi-core numerical kernels with no cross-core state.
3. **Machinery in those domains:** Split the domain, run identical workers, join by a commutative summary (here: witness OR and PARTIAL flags).
4. **Transfer candidate:** Run both XOR half-shards concurrently so elapsed time is ~max(t₀, t₁) instead of t₀ + t₁, preserving **1.2×10⁸** `exists_tree` budget and **10M** LRU per process.

## Falsifiable claim

Concurrent execution of `[0:1001)` and `[1001:2002)` with the same parameters as the sequential **12e7-each** wrapper will finish in wall-clock approximately **half** the sequential **~35 min** (up to host contention), and will not change the feasibility verdict class versus the sequential run (still expect both PARTIAL, exit **2**, unless a race exposes a witness—which would be unexpected).
