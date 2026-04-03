# Notes — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-eighths-6e7-each-lru-8m

- **Observation:** **r=9** total **DP** sum slightly **lower** than **r=5** (**~145 s** vs **~152 s**) on the same eighth partition — consistent with occasional **r=9** speed advantages seen in other **n=14** probes.
- **Insight:** **Eighth** geometry remains **safe** for **8M** LRU at **6e7** cap for **both** dual arities — the **quarter**-scale **~500**-split **saturation** is not replicated here.
- **Next:** Full-menu **`d=3`** still open; prefer **algorithmic / memory** changes over further eighth budget scaling.
