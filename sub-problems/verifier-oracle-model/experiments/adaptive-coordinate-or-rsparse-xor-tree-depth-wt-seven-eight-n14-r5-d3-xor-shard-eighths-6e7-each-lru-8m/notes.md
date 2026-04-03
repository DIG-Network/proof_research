# Notes — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-shard-eighths-6e7-each-lru-8m

- **Observation:** Per-eighth **DP** time stayed **O(20s)** scale despite **2×** `max-exists-calls` vs **3e7** eighths — the probe likely terminates well before exhausting **6e7** once **`d=3`** is decided **False** (budget headroom is slack, not extra proof work).
- **Insight:** The **stress** question “will **6e7** trigger **8M** LRU like quarters?” is answered **no** for **r=5** eighth geometry — misses remain **~2.5–2.8M** max.
- **Question:** Does **full-menu** **`d=3`** require a different strategy (**memo-dict** with more RAM, or algorithmic DP changes) rather than larger **`exists_tree`** caps on capped LRU?
