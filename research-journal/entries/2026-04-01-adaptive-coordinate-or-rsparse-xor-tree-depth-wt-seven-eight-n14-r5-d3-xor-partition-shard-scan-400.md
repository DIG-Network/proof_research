# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-partition-shard-scan-400

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-partition-shard-scan-400/`

## Context

verifier-oracle-model — `n=14`, shells `{7,8}`, `r=5`, `d=3`-only. Parent script extended with `--xor-index-range` to slice the 2002 XOR-derived bipartitions.

## Hypothesis tested

Contiguous XOR-menu shards (~400 splits each, five shards partitioning `[0,2002)`) finish under **LRU 8M** and **5.5×10⁷** `exists_tree` budget without OOM; search for any shard with `d=3 feasible=True` (would certify **≤3** for the full `r=5` menu).

## Outcome

**PASS** — all five shards completed; **no** shard reported `feasible=True` at `d=3`.

## Key finding

Each ~400-split shard saturated **LRU 8M** at `d=3` (same cap behavior as the full-menu partial run) but returned **`feasible=False`** within budget. **Negative shard results do not imply** full 2002-split menu is infeasible at depth 3; only a positive shard would be a one-way certificate.

## Implications

- Tooling: reproducible **XOR-menu sharding** on the canonical `n=14` parent for memory-bounded exploration.
- **`r=5` full-menu `d=3`** remains **open**; next steps remain larger RAM, different shard families, or algorithmic DP improvements—not logical inference from these negatives alone.

## Analogy pass summary

Divide large generator menus; one-way soundness for **positive** witnesses from sub-menus.

## Space-definition

None.
