# Results

**Outcome:** INCONCLUSIVE (parent exit **2**, PARTIAL).

**Configuration:** `n=14`, shells `{7,8}`, `coord + r=9` XOR (2002 splits), `d=3`-only, `--max-exists-calls 100000000`, `--lru-maxsize 10000000`, `--skip-baseline`.

**Measured:** `exists_tree` budget exhausted after **956.6551 s** DP (build **~4.09 s**); LRU at cap **10000000**; parent reported `d=3 feasible=False` inside the partial probe.

**Comparison:** **10M** LRU vs **8M** at same **10⁸** budget: **~107 s** **slower** DP (**956.7** vs **~850.2** s) — **opposite** sign to **`r=5`** (**8M→10M** sped **`r=5`** up). **Dual 2002** band remains **PARTIAL**; **`r=9`** **no longer** faster than **`r=5`** at **10e7** when LRU is **10M**.
