# Results

**Outcome:** INCONCLUSIVE (parent exit **2**, PARTIAL).

**Configuration:** `n=14`, shells `{7,8}`, `coord + r=5` XOR (2002 splits), `d=3`-only, `--max-exists-calls 100000000`, `--lru-maxsize 8000000`, `--skip-baseline`.

**Measured:** `exists_tree` budget exhausted after **916.5780 s** DP (build **~2.85 s**); LRU at cap **8000000**; parent reported `d=3 feasible=False` inside the partial probe.

**Comparison:** **+10M** over **9e7** cost **~89–90 s** DP marginal (vs **~827 s** at **9e7** in prior run — **less steep** than **8e7→9e7** **~111 s**).
