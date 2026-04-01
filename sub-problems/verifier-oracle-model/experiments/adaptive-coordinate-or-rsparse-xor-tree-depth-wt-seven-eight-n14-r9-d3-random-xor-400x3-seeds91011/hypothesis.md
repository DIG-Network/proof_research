# Hypothesis — random non-contiguous XOR split ensembles (`n=14`, `r=9`, `d=3`, seeds 9–11)

## Analogy pass

1. **Abstract structure:** Coordinate splits plus a sampled 400-split `r=9` XOR submenu from `C(14,9)=2002`. Prior work used seeds `{0,1,2}`, `{6,7,8}`; `r=5` used `{0,1,2}` and `{3,4,5}`. Independent RNG streams widen empirical coverage of index space.

2. **Where else:** (i) Monte Carlo replication; (ii) combinatorial search sensitivity to tie-breaking; (iii) rare-event estimation — positives may require many seeds.

3. **Machinery:** `random.Random(seed).sample(range(2002), 400)` for `seed ∈ {9,10,11}`; same LRU 8M and `5.5×10⁷` exists_tree budget as prior `r=9` random probes.

4. **Transfer candidate:** Continue the `r=9` random 400×3 line after seeds `{0..8}` to test whether any sampled menu admits `d=3`.

## Falsifiable claim

**H1:** At least one of seeds `{9,10,11}` yields `d=3 feasible=True` for coord + that 400-split `r=9` submenu.

**H2 (null):** All three runs finish within budget with `feasible=False`.

Parent: `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` (`--xor-index-indices`).

Lineage: extends `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-random-xor-400x3-seeds678` (additional RNG seeds).
