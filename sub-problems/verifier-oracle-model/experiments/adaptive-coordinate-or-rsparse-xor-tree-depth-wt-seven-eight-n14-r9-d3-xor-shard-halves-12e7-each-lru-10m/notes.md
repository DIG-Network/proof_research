# Notes

- **Scaling:** Per-half DP time scaled ~**2×** vs **6e7** half-shards (**~509 s** → **~1034 s**, **~479 s** → **~992 s**), consistent with linear budget scaling at LRU cap.
- **feasible=False under PARTIAL:** Parent still prints `d=3 feasible=False` when budget exhausts before a completion certificate—same semantic caveat as prior XOR-shard runs.
- **Next:** Further budget increases per half risk long wall-clock; **parallel** two processes could halve wall time for the same budgets. Alternative: pivot **anonymous-quorum-binding** or other `r` bands per digest.
- **dead_end (local):** **12e7** per half with **10M** LRU is **not** enough to finish either **1001**-split contiguous shard for **`r=9` `d=3`** in this DP model.
