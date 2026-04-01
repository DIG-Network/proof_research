# Hypothesis — random non-contiguous XOR split ensembles (`n=14`, `r=9`, `d=3`)

## Analogy pass

1. **Abstract structure:** Same as the `r=5` random-submenu probe: the DP menu is coordinate splits plus a **sampled** XOR bipartition submenu. Contiguous index blocks are arbitrary; spread indices may hit different geometry than five contiguous 400-index shards (which all gave `feasible=False`).

2. **Where else:** (i) stratified vs simple random sampling in Monte Carlo; (ii) design of experiments — factor coverage; (iii) coding — structured random ensembles.

3. **Machinery:** Fixed seeds + uniform `sample` without replacement from `{0,…,2001}`; monotonicity: if **any** 400-split menu admits `d=3`, full `C(14,9)` menu has `min_d ≤ 3`.

4. **Transfer candidate:** Mirror `r=5` seeds `{0,1,2}` and `k=400` on `C(14,9)=2002` canonical XOR list, same LRU/budget as `r=5` random probe.

## Falsifiable claim

**H1:** At least one seed yields `d=3 feasible=True` for coord + that 400-split `r=9` submenu.

**H2 (null):** All three runs finish within budget with `feasible=False`.

Parent: `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` (`--xor-index-indices`).
