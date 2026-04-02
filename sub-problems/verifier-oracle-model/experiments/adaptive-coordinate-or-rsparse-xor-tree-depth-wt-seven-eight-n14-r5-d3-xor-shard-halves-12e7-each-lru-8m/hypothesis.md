# Hypothesis

**Claim:** On `n=14`, shells `{7,8}`, `coord + r=5` XOR (2002 splits), `d=3`-only probe: splitting the XOR partition list into contiguous halves `[0:1001)` and `[1001:2002)` and running the bounded DP **sequentially** on each half with **12×10⁷** `exists_tree` budget and **8M** LRU (higher per-half budget than **7×10⁷**, still **half** the XOR menu per process) may yield **`d=3 feasible=True`** on at least one half—a **witness** that the full language admits depth ≤3 (superset monotonicity in parent `script.py`).

## Analogy pass (mandatory)

1. **Abstract structure:** Large split menu defines a decision-tree language; full enumeration is expensive; a **sufficient sub-menu** that already admits a depth-3 tree implies the full menu does (more splits only help the prover).

2. **Analogous domains:** (i) *Feature sufficiency* in ML—a subset of features may already separate classes; (ii) *Branch-and-bound*—prove feasibility on a restriction then lift; (iii) *SAT sharding*—positive shard implies satisfiability under a superset of clauses.

3. **Machinery:** Restrict structure, complete search within budget, lift by inclusion.

4. **Transfer candidate:** Reuse **`--xor-index-range`** on parent; **8M LRU** avoids 10M OOM on memory-bounded hosts; **12e7** extends the **7e7** half-shard run (both halves PARTIAL) to test whether extra budget clears PARTIAL on a contiguous half.

**Falsifiable:** If both halves PARTIAL or finish with `d=3 feasible=False`, no witness at this budget; does not decide global `d=3` for full 2002.

**Parent:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py`

**Builds on:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-shard-halves-7e7-each-lru-8m` (both halves PARTIAL at 7e7/8M); `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-12e7-lru-10m` (full menu INCONCLUSIVE at 12e7/10M).
