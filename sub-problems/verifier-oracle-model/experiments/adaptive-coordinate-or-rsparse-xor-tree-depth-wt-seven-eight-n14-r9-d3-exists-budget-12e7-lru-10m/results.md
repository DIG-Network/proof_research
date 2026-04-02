# Results

**Outcome:** INCONCLUSIVE (parent exit **2**, PARTIAL).

**Configuration:** `n=14`, shells `{7,8}`, `coord + r=9` XOR (2002 splits), `d=3`-only, `--max-exists-calls 120000000`, `--lru-maxsize 10000000`, `--skip-baseline`.

**Measured:** `exists_tree` budget exhausted after **965.2617 s** DP (build **~4.09 s**); LRU at cap **10000000**; parent reported `d=3 feasible=False` inside the partial probe.

**Comparison vs 11e7/10M:** **+10⁷** visits added **~53.8 s** (**911.5 → ~965.3** s) — **`r=9`** again **faster** than **`r=5`** at the same cap and **milder** marginal than **`r=5`**’s **~84.6 s** jump. Still **PARTIAL**; dual **2002** band **open**.
