# Results

**Outcome:** INCONCLUSIVE (parent exit **2**, PARTIAL).

**Configuration:** `n=14`, shells `{7,8}`, `coord + r=5` XOR (2002 splits), `d=3`-only, `--max-exists-calls 120000000`, `--lru-maxsize 10000000`, `--skip-baseline`.

**Measured:** `exists_tree` budget exhausted after **1076.6253 s** DP (build **~2.67 s**); LRU at cap **10000000**; parent reported `d=3 feasible=False` inside the partial probe.

**Comparison vs 11e7/10M:** **+10⁷** visits (**12e7** vs **11e7**) added **~84.6 s** wall (**992 → ~1076.6** s) — **~8.5 µs** per extra call at LRU cap, similar order to prior **10e7→11e7** step. Still **PARTIAL**; dual **2002** band **open**.
