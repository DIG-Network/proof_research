# Results

**Outcome:** INCONCLUSIVE (parent exit **2**, PARTIAL).

**Configuration:** `n=14`, shells `{7,8}`, `coord + r=9` XOR (2002 splits), `d=3`-only, `--max-exists-calls 110000000`, `--lru-maxsize 10000000`, `--skip-baseline`.

**Measured:** `exists_tree` budget exhausted after **911.4665 s** DP (build **~4.37 s**); LRU at cap **10000000**; parent reported `d=3 feasible=False` inside the partial probe.

**Comparison vs 10e7/10M:** **+10⁷** visits at **10M** LRU **reduced** wall time vs **10e7** alone (**911.5** vs **~957** s) — **opposite** marginal sign to **`r=5`** (**838→992** s). Suggests **`r=9`** DP path benefited from extra budget in a way **`r=5`** did not (or run-to-run variance); still **PARTIAL**, dual **2002** band **open**.
