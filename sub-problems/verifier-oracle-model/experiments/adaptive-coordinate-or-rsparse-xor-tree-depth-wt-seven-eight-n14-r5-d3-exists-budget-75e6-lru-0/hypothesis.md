# Hypothesis

**Falsifiable claim:** On `n=14`, shells `{7,8}`, `coord + r=5`, `d=3`-only: **same** **`max_exists_calls = 7.5×10⁷`** as the **75e6/12M LRU** shard but with **`--lru-maxsize 0`** (unbounded memo) completes on a host with sufficient RAM: either **`d=3 feasible=True/False`** (PASS) or **`PARTIAL: exceeded max_exists_calls`** (exit 2), without **SIGKILL** from LRU footprint.

**Context:** **75e6/12M** died **~8 min** with **SIGKILL** (OOM class). **5e7/8M** completed **PARTIAL** in **~421 s**. Unbounded memo avoids **12M-entry** cap but may grow until budget or wall limit.

## Analogy pass (abbrev.)

1. **Abstract structure:** Same DP graph as capped-LRU run; memory model switches from **bounded transposition table** to **full memo** — trades RAM for no false evictions mid-search.
2. **Analogous domains:** (i) BFS with visited set vs LRU revisit; (ii) dynamic programming tabulation vs sliding window.
3. **Machinery:** If unique `(bits, depth)` states **≤** RAM, unbounded finishes like ideal TT; if not, OOM still possible (mitigate with **timeout** + **exists** cap).
4. **Transfer seed:** **Isolate eviction** as failure mode — keep **visit budget** fixed from **75e6** bracket.

**Parent experiments:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-75e6-lru-12m` (INCONCLUSIVE SIGKILL); `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-5e7-lru-8m` (INCONCLUSIVE PARTIAL).
