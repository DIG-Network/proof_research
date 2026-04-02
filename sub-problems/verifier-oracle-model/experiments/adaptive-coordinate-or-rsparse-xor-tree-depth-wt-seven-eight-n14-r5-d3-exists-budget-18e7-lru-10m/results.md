# Results

**Outcome:** INCONCLUSIVE (parent exit **2**, PARTIAL).

**Configuration:** `n=14`, shells `{7,8}`, `coord + r=5` XOR (**2002** splits), `d=3`-only, `--max-exists-calls 180000000`, `--lru-maxsize 10000000`, `--skip-baseline`.

**Measured:** `exists_tree` budget exhausted after **1492.2222 s** DP (**build ~2.737 s**); LRU at cap **10000000**. Parent printed `d=3 feasible=False` in the depth log alongside **PARTIAL** — **budget-truncated** probe, **not** a certified full-menu **`min_d>3`** proof.

**Comparison vs `r=9` 18e7/10M (~1644.56 s):** same **180M** cap and **10M** LRU; **`r=5`** finished **~152.3 s** faster (**~9.3%** wall reduction). Both lanes **PARTIAL** — **no** complete **`d=3`** verdict for the **full** **2002** menu.

**Implication:** Complement-size symmetry (**`C(14,5)=C(14,9)`**) does **not** equalize DP wall at **18e7/10M`; **`r=5`** is modestly **easier** here. Dual **2002** band remains **open**; next large step per session guidance: **`r=9` `24e7/10M`** (~45 min extrapolated) or **DP/memo** structure change.
