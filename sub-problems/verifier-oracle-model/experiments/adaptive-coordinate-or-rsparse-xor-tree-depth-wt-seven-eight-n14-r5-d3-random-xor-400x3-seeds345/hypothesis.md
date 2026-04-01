# Hypothesis — random non-contiguous XOR split ensembles (`n=14`, `r=5`, `d=3`, seeds 3–5)

## Analogy pass

1. **Abstract structure:** Same as `…-r5-d3-random-xor-400x3-seeds012`: the DP menu is a subset of the canonical `C(14,5)=2002` XOR bipartitions; random index samples test whether a depth-3 witness might live in **spread** index sets rather than contiguous shards.

2. **Where else:** Stratified / Monte Carlo coverage of a large discrete menu; spread-spectrum style sampling vs contiguous blocks.

3. **Machinery elsewhere:** If any 400-split submenu admits `feasible=True` at `d=3`, the full menu has `min_d ≤ 3` (monotone superset).

4. **Transfer candidate:** Independent seeds **3,4,5** (400 samples each) extend the negative-evidence sample from seeds 0–2 without re-running identical menus.

## Falsifiable claim

**H1:** At least one of seeds `{3,4,5}` yields `d=3 feasible=True` for coord + that 400-split submenu.

**H2 (null for this probe):** All three runs complete within budget with `feasible=False`.

**Parent:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` (`--xor-index-indices`).

**Lineage:** `extends` `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-random-xor-400x3-seeds012` — same protocol, new PRNG seeds.
