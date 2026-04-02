# Results

**Outcome:** INCONCLUSIVE (parent exit **2**, PARTIAL).

**Configuration:** `n=14`, shells `{7,8}`, `coord + r=5` XOR (**2002** splits), `d=3`-only, `--max-exists-calls 300000000`, `--lru-maxsize 10000000`, `--skip-baseline`.

**Measured:** `exists_tree` budget exhausted after **2615.6780 s** DP (**build ~2.652 s**); LRU at cap **10000000**. Parent printed `d=3 feasible=False` alongside **PARTIAL** — **budget-truncated** probe, **not** a certified full-menu **`min_d>3`** proof.

**Comparison vs `r=5` 24e7/10M (~1970.27 s):** **+6×10⁷** calls (**240M → 300M**) added **~645.41 s** (**~10.76 µs**/extra call) — **steeper** than the **18e7 → 24e7** marginal (**~7.97 µs**/call), consistent with **worse LRU locality** as the working set grows deeper into the **2002** menu.

**Implication:** **30e7/10M** still **PARTIAL**; wall **~43.6 min** DP. Next: **algorithmic** change (**DP/memo** / frontier structure), **smaller strategic shards**, or accept that **full-menu** **`d=3`** at **`r=5`** may need **>30e7** or different **LRU** strategy — avoid **parallel dual 10M** (**OOM**).
