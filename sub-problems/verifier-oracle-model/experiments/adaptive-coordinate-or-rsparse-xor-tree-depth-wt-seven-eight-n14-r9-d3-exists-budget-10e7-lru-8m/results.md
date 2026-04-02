# Results

**Outcome:** INCONCLUSIVE (parent exit **2**, PARTIAL).

**Configuration:** `n=14`, shells `{7,8}`, `coord + r=9` XOR (2002 splits), `d=3`-only, `--max-exists-calls 100000000`, `--lru-maxsize 8000000`, `--skip-baseline`.

**Measured:** `exists_tree` budget exhausted after **850.2305 s** DP (build **~4.08 s**); LRU at cap **8000000**; parent reported `d=3 feasible=False` inside the partial probe.

**Comparison:** **+10M** over **9e7** cost **~35 s** DP marginal (vs **~815 s** at **9e7** — **much less steep** than **`r=5`** **9e7→10e7** **~90 s**). **`r=9`** still **faster** than **`r=5`** at **10e7** (~850 s vs ~917 s).
