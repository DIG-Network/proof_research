# Notes — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-quarters-6e7-each-lru-8m

- **observation:** All four quarters completed **`d=3`** with **`feasible=False`**; **8M** LRU saturated each; **no** **`PARTIAL`**; total wall **~1419 s** (**~23.6 min**).
- **insight:** **`r=9`** matches **`r=5`** quarter completion pattern (**definite** **`d=3`** negatives on **~500-split** menus) — **2002-band** arity does not change **quarter-scale** **PARTIAL** vs **complete** geometry here.
- **observation:** **`r=9`** **~5%** faster than **`r=5`** **~1491 s** at same shard sizes — consistent with prior full-menu **`r=9`** vs **`r=5`** timing in this band.
