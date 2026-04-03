# Hypothesis: quarter-shard `r=5` XOR menu, `d=3`

## Analogy pass

1. **Abstract structure:** Search for a depth-3 decision tree over a large discrete split menu; LRU-capped memoization may saturate before the search finishes. Smaller active split sets reduce per-invocation branching factor and may allow the DP to reach a verdict within the same aggregate `exists_tree` budget as coarser sharding.

2. **Analogous domains:** (a) Branch-and-bound with smaller active constraint sets per node. (b) Domain decomposition in PDE solvers — finer partitions can change iteration counts. (c) List-decoding with shorter candidate lists — different truncation geometry changes which codewords are reachable first.

3. **Machinery in those domains:** Bounding / pruning early; local solves on subdomains; re-encoding with different segment boundaries.

4. **Transfer candidate:** Partition the canonical `C(14,5)=2002` XOR splits into **four** contiguous index blocks (~501 splits each) instead of two halves (~1001). Hold **total** budget at **2.4×10⁸** `exists_tree` (**6×10⁷** per quarter, **8M** LRU) — same aggregate cap as **two** **12×10⁷** half-shard runs — and test whether **any** quarter completes with **`d=3 feasible=True`** (witness) or a definite **`False`** without PARTIAL.

## Falsifiable claim

At least one of the four quarters finishes without exit 2 (budget PARTIAL) **or** a witness appears in some quarter. If all four PARTIAL like the 12e7 halves, the claim that quartering improves completion is falsified (for this budget envelope).
