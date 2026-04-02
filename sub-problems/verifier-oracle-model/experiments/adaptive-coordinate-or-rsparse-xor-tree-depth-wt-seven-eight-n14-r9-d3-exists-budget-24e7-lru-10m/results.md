# Results

**Outcome:** INCONCLUSIVE (parent exit **2**, PARTIAL).

**Configuration:** `n=14`, shells `{7,8}`, `coord + r=9` XOR (**2002** splits), `d=3`-only, `--max-exists-calls 240000000`, `--lru-maxsize 10000000`, `--skip-baseline`.

**Measured:** `exists_tree` budget exhausted after **2118.2000 s** DP (**build ~4.325 s**, **total dp_sec ~2118.214**); LRU at cap **10000000**. Parent printed `d=3 feasible=False` alongside **PARTIAL** — **budget-truncated** probe, **not** a certified full-menu **`min_d>3`** proof.

**Comparison vs `r=9` 18e7/10M (~1644.56 s):** **+6×10⁷** calls (**+33%** budget) added **~473.6 s** wall (**~28.8%** longer); marginal **~7.9 µs**/extra call (similar order to **12e7→18e7** regime at LRU cap). Full **2002** menu still **unfinished** at **24e7**.

**Implication:** **`r=9`** **`d=3`** full-menu completion at **10M** LRU likely needs **>24e7** budget, **>10M** LRU (if memory allows), or **DP/memo** structure change.
