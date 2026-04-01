# Notes — r=9 random XOR 400×3 (seeds 0,1,2)

- Mirrors `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-random-xor-400x3-seeds012` with `--r-single 9`; same `C(14,r)=2002` count for `r∈{5,9}` so index sampling domain matches `r=5`.
- Contiguous `r=9` shard scan (five 400-width shards) already gave all `feasible=False` at `d=3` with LRU saturation; this tests whether **non-contiguous** 400-menus behave differently for `r=9`.
