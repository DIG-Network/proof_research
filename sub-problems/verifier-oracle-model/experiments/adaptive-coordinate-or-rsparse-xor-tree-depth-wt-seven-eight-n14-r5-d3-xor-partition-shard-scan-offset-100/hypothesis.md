# Hypothesis

## Analogy pass

1. **Abstract structure:** The `r=5` XOR split menu is a fixed ordered list of 2002 bipartitions. Prior work partitioned index ranges `[0,400), …` contiguously from the start. We ask whether **feasibility at depth 3** might correlate with **where** a split sits in lexicographic `combinations(14,5)` order—so a **phase shift** (skip the first 100 indices) samples a different structural family than the origin block.

2. **Where else:** (i) FFT windows use phase shifts to avoid spectral leakage at boundaries; (ii) stratified sampling shifts strata to reduce bias; (iii) rotating cache-line aligned partitions in parallel DP to spread hot spots.

3. **Machinery there:** phase / offset parameters change which samples are included without changing the global object.

4. **Transfer candidate:** **Contiguous XOR slices with `start=100`** — same budgets as shard-400 baseline; any `feasible=True` would still only certify that **sub-menu**, not full menu; all `False` remains non-conclusive for global `d=3`.

## Falsifiable claim

Under **LRU 8M** and **5.5×10⁷** `exists_tree` calls per shard, the five slices  
`100:500`, `500:900`, `900:1300`, `1300:1700`, `1700:2002`  
each complete with a definite `feasible` at `d=3` (no PARTIAL/OOM). We record whether any shard reports `feasible=True` (positive witness for that sub-menu).

## Lineage

- Extends `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-partition-shard-scan-400` (same hardware budget, different index offsets).
