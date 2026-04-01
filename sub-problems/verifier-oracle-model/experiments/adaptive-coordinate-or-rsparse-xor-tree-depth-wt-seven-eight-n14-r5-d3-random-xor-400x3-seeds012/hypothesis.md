# Hypothesis — random non-contiguous XOR split ensembles (`n=14`, `r=5`, `d=3`)

## Analogy pass

1. **Abstract structure:** The decision-tree DP searches over a *menu* of binary splits (coordinate + chosen XOR bipartitions). Feasibility at depth `d` is monotone in the menu: adding splits only helps. Contiguous index blocks in the canonical `combinations(N,r)` order are an arbitrary partition of the menu; a depth-3 witness might require splits whose indices are **spread** across that order (analogous to **spread-spectrum** coding or **stratified sampling** vs contiguous chunks in experiment design).

2. **Where else:** (i) Monte Carlo integration — random samples can hit representative geometry faster than axis-aligned slabs; (ii) group testing — random test pools vs consecutive pools; (iii) error-correcting codes — good codes often have **structured randomness** rather than contiguous coordinate blocks.

3. **Machinery elsewhere:** Random subset selection + empirical coverage; if **any** sampled sub-menu admits `feasible=True` at `d=3`, the full 2002-split language has `min_d ≤ 3` (superset monotonicity).

4. **Transfer candidate:** Sample **400** distinct XOR split indices uniformly from `{0,…,2001}` with fixed seeds **0,1,2**, run the same budgeted `d=3` probe as the contiguous shard scan. **Falsifiable:** all three runs return `feasible=False` ⇒ no random 400-submenu witness found (still not a full-menu impossibility proof).

## Falsifiable claim

**H1:** At least one of seeds `{0,1,2}` yields `d=3 feasible=True` for coord + that 400-split submenu.

**H2 (null for this probe):** All three runs complete within budget with `feasible=False`.

Parent change: `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` adds `--xor-index-indices` (mutually exclusive with `--xor-index-range`).
