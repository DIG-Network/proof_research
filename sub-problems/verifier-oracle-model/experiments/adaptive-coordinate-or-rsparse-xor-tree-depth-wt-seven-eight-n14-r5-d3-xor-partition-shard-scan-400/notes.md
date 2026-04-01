# Notes — XOR partition shard scan

- **One-way soundness:** If shard `S` finds `d=3 feasible=True`, the full `r=5` menu (all 2002 XOR splits) also admits some depth-3 tree, because shard languages are **subsets** of the full split menu.
- **Not the converse:** `feasible=False` on every shard does **not** prove full-menu `min_d > 3`; a depth-3 tree might need XOR splits from **multiple** shards simultaneously.
- **Why run it anyway:** (i) infrastructure to avoid OOM on mega-runs; (ii) hunt for a **cheap positive certificate** if one split block alone suffices; (iii) all five shards hit `LRU currsize=8e6` cap at `d=3`, same qualitative profile as the full-menu partial run.
- **Extra datapoint:** Shard `0:200` finished in ~10.6s with ~1.48M cache entries (not LRU-capped), still `feasible=False` — small menus are decisively infeasible at `d=3` here.
