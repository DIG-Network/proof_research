# Results

**Outcome:** INCONCLUSIVE (parent exit **2**, PARTIAL).

**Configuration:** `n=14`, shells `{7,8}`, `coord + r=5` XOR (**2002** splits), `d=3`-only, `--max-exists-calls 240000000`, `--lru-maxsize 10000000`, `--skip-baseline`.

**Measured:** `exists_tree` budget exhausted after **1970.2726 s** DP (**build ~2.660 s**); LRU at cap **10000000**. Parent printed `d=3 feasible=False` in the depth log alongside **PARTIAL** — **budget-truncated** probe, **not** a certified full-menu **`min_d>3`** proof.

**Comparison vs `r=5` 18e7/10M (~1492.22 s):** same **180M → 240M** step as **`r=9`**; **+478.05 s** for **+6×10⁷** calls (**~7.97 µs**/extra call at LRU cap).

**Comparison vs `r=9` 24e7/10M (~2118.20 s):** same **240M**/**10M**; **`r=5`** finished **~147.93 s** faster (**~7.0%** wall reduction vs **`r=9`** at this cap). At **18e7** the gap was **~9.3%** — complement-speed advantage **narrows slightly** at **24e7** but **`r=5`** remains **easier** in wall time.

**Implication:** Paired **dual 2002** lanes both **PARTIAL** at **24e7/10M**; marginal **18e7→24e7** cost is **~478 s** (**r=5**) vs **~474 s** (**r=9**) — nearly **identical** **µs/call** at **10M** LRU. Next: **`30e7/10M`**, **DP/memo** structure, or **smaller strategic shards** — avoid **parallel dual 10M** LRU (**OOM** risk per prior experiments).
