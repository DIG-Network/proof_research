# Results

**Outcome:** INCONCLUSIVE (parent exit **2**, PARTIAL).

**Configuration:** `n=14`, shells `{7,8}`, `coord + r=9` XOR (**2002** splits), `d=3`-only, `--max-exists-calls 180000000`, `--lru-maxsize 10000000`, `--skip-baseline`.

**Measured:** `exists_tree` budget exhausted after **1644.5624 s** DP (**build ~4.217 s**); LRU at cap **10000000**. Parent printed `d=3 feasible=False` in the depth log alongside **PARTIAL** — this reflects **budget-truncated** probe, **not** a certified **`d=3`** infeasibility proof for the full language.

**Comparison vs 12e7/10M (~965.26 s):** **+6×10⁷** calls added **~679.3 s** wall (**~11.3 min** extra for **60M** visits), i.e. **~11.3 µs** per extra `exists_tree` unit at **10M** LRU saturation — steeper marginal than **12e7→15e7** half-shard per-half pace would suggest for the same **+3×10⁷** step, consistent with **full 2002** menu staying **harder** than a single half-shard.

**Implication:** **1.8×10⁸** at **10M** LRU still does **not** resolve **`r=9`**, **`d=3`** for the **full** XOR menu; dual **2002** band remains **open** for a **complete** verdict without **DP**/**memo** structure change, larger LRU (if memory allows), or larger host.
