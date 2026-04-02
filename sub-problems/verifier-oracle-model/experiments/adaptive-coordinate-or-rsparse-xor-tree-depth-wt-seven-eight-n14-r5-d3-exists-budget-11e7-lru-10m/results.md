# Results

**Outcome:** INCONCLUSIVE (parent exit **2**, PARTIAL).

**Configuration:** `n=14`, shells `{7,8}`, `coord + r=5` XOR (2002 splits), `d=3`-only, `--max-exists-calls 110000000`, `--lru-maxsize 10000000`, `--skip-baseline`.

**Measured:** `exists_tree` budget exhausted after **992.4888 s** DP (build **~2.87 s**); LRU at cap **10000000**; parent reported `d=3 feasible=False` inside the partial probe.

**Comparison vs 10e7/10M:** **+10⁷** visits (**+10%**) added **~154 s** DP (**992.5** vs **~838** s) — linear-ish marginal **~15.4 µs** per extra call at LRU cap. Still **no** root **`d=3`** decision.
