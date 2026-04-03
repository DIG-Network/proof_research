# Hypothesis — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-shard-eighths-6e7-each-lru-8m

## Analogy pass

1. **Abstract structure:** We probe whether a fixed **adaptive splitting language** (coord + one arity of r-sparse XOR) needs depth **d=3** to separate the **{7,8}** shell union on **n=14**, by exhausting a **large** `exists_tree` budget on **small contiguous XOR sub-menus** (eighths of the 2002-split list). Increasing the per-shard budget tests whether the prior **3e7** cap was **truncation-limited** vs **LRU-cap-limited**.

2. **Analogous domains:** (a) Branch-and-bound with a node budget — doubling budget may or may not change the provenance of the best certificate. (b) Paging / cache sizing — if working set fits in cache, more CPU budget does not increase misses. (c) Partial order search — if the goal state is not reachable at depth 3 in the sub-language, more search steps along the same frontier do not change feasibility.

3. **Machinery in those domains:** Budget curves, cache miss profiles, and completeness of depth-bounded search.

4. **Transfer seed:** **Cache miss scaling** — quarter shards at ~500 XOR splits saturated **8M** LRU; eighth shards at ~251 splits did not at **3e7**. **6e7** per eighth doubles aggregate work to **4.8×10⁸** while keeping the same **~250**-split geometry — if saturation appears, it would indicate **budget × menu width** interaction.

## Falsifiable claim

**Claim:** With **r=5**, **d=3**-only probes, **8** contiguous eighth-shards, **6×10⁷** `exists_tree` per eighth, **8M** LRU, sequential subprocesses: either (A) some eighth returns **PARTIAL** (budget exhaustion) or shows **LRU saturation** near **8M** misses, or (B) all eighths complete with **`d=3 feasible=False`** and misses stay **≪ 8M** (strengthening that **3e7** eighth runs were not memo-starved).
