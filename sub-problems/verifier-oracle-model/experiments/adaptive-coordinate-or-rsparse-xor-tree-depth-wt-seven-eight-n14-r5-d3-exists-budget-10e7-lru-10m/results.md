# Results

**Outcome:** INCONCLUSIVE (parent exit **2**, PARTIAL).

**Configuration:** `n=14`, shells `{7,8}`, `coord + r=5` XOR (2002 splits), `d=3`-only, `--max-exists-calls 100000000`, `--lru-maxsize 10000000`, `--skip-baseline`.

**Measured:** `exists_tree` budget exhausted after **837.5132 s** DP (build **~2.73 s**); LRU at cap **10000000**; parent reported `d=3 feasible=False` inside the partial probe.

**Comparison:** **10M** LRU vs **8M** at same **10⁸** budget: **~79 s** **faster** DP (**837.5** vs **~916.6** s) — larger working set **reduced** wall time but **did not** terminate the **d=3** decision within **10⁸** calls.
