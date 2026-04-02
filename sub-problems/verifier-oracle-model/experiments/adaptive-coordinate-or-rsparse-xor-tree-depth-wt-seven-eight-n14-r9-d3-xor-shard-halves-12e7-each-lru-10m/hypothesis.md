# Hypothesis

**Claim:** On `n=14`, shells `{7,8}`, `coord + r=9` XOR (2002 splits), `d=3`-only probe: the prior **6×10⁷** per-half run (`…-6e7-each-lru-10m`) hit **PARTIAL** on both contiguous halves. Doubling per-half budget to **1.2×10⁸** `exists_tree` (same **10M** LRU) matches the **full-menu** **12e7** cap **per** half in aggregate; at least one half may complete with a definitive `d=3 feasible=` line or produce **`d=3 feasible=True`** as a **witness** for the superset language (parent monotonicity).

## Analogy pass (mandatory)

1. **Abstract structure:** Two disjoint halves partition the same finite search menu; total work equals sum of halves; if each half gets the same budget as a known full-menu run, we test whether the bottleneck was **per-shard** truncation vs **global** structure.

2. **Analogous domains:** (i) *Domain decomposition in PDE solvers* — interface conditions vs bulk; here halves are independent menus (no cross-coupling). (ii) *MapReduce* — same total keyspace, more reducers with larger per-partition memory. (iii) *Portfolio risk* — sub-portfolios can each hit risk limits; doubling per-book limit tests scaling.

3. **Machinery there:** Equal budget per partition; compare completion vs partial.

4. **Transfer candidate:** Parent already supports `--xor-index-range`; only change is `--max-exists-calls` **120000000** per subprocess.

**Falsifiable:** If both halves still **PARTIAL** (exit 2) with no `d=3 feasible=True`, the **2002** `r=9` `d=3` question remains **open** at this envelope (stronger negative evidence for half-wise completion). If one half **PASS**es with witness, we get a **positive** certificate for full menu by inclusion.

**Parent experiment:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-halves-6e7-each-lru-10m`

**Parent script:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py`
