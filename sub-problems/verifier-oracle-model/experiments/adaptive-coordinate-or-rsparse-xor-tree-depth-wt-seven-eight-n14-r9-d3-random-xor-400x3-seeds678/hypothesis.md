# Hypothesis — random non-contiguous XOR split ensembles (`n=14`, `r=9`, `d=3`, seeds 6–8)

## Analogy pass

1. **Abstract structure:** Same as `…-r9-d3-random-xor-400x3-seeds012`: coordinate splits plus a **sampled** 400-split `r=9` XOR submenu from `C(14,9)=2002`. If `d=3` witnesses cluster in measure-zero regions of index space, additional seeds improve coverage.

2. **Where else:** (i) Monte Carlo replication with independent RNG streams; (ii) sensitivity of combinatorial search to tie-breaking / sampling; (iii) rare-event estimation — need multiple seeds to see positives.

3. **Machinery:** `random.Random(seed).sample(range(2002), 400)` for `seed ∈ {6,7,8}`; same LRU/budget as prior `r=9` and `r=5` random probes.

4. **Transfer candidate:** Extend the `r=9` random 400×3 line symmetrically to seeds `{6,7,8}` after `{0,1,2}` and `{3,4,5}` (`r=5`).

## Falsifiable claim

**H1:** At least one of seeds `{6,7,8}` yields `d=3 feasible=True` for coord + that 400-split `r=9` submenu.

**H2 (null):** All three runs finish within budget with `feasible=False`.

Parent: `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` (`--xor-index-indices`).
