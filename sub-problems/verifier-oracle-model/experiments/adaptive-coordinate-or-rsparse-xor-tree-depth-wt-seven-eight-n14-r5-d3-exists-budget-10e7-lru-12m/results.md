# Results: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-10e7-lru-12m

**Outcome:** INCONCLUSIVE

**Configuration:** `n=14`, shells `{7,8}`, coord + full **r=5** XOR menu (2002 partitions), **d=3** only, `--max-exists-calls 100000000`, `--lru-maxsize 12000000`, `--skip-baseline`.

**Run:** Process exit **247** after **~463.9 s** wall (~7.73 min). No `feasible=` line and no `PARTIAL:` line printed (killed mid `probing d=3 …`).

**Interpretation:** Same **OOM / SIGKILL** class as **2026-04-01** **7.5e7/12M** **r=5** run — **12M** LRU resident states exceed this host’s practical memory budget for this probe, independent of raising **exists_tree** budget to **10⁸**.

**Comparison:** **10e7/10M** completed with **PARTIAL** ~838 s; **10e7/12M** does **not** reach budget exhaustion here.
