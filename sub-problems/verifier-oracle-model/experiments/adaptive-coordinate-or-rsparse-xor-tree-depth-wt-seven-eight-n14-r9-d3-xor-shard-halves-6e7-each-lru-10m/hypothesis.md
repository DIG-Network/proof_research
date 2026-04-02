# Hypothesis

**Claim:** On `n=14`, shells `{7,8}`, `coord + r=9` XOR (2002 splits), `d=3`-only probe: splitting the XOR partition list into two contiguous halves `[0:1001)` and `[1001:2002)` and running the same bounded DP on each half (separate processes, **6×10⁷** `exists_tree` budget each, **10M** LRU) may hit **`d=3 feasible=True`** on at least one half before budget exhaustion—serving as a **witness** that the full 2002-split language admits depth ≤3 (superset argument in parent `script.py` help).

## Analogy pass (mandatory)

1. **Abstract structure:** A large discrete menu of admissible splits defines a language; exact threshold for minimum decision-tree depth is unknown; full enumeration is expensive; **any** sufficient sub-menu that already proves a shallow tree yields a **certificate** for the richer language by monotonicity (more splits ⊇ fewer splits).

2. **Analogous domains:** (i) *Branch-and-bound / divide search* — prove optimality on a restricted region first; (ii) *Sufficient statistics* — a subset of features may already determine the label; (iii) *SAT sharding* — parallel clauses sets; if one shard is UNSAT under restricted clauses, structure differs—here we seek a **positive** shard witness.

3. **Machinery there:** Restrict structure, run complete solver within budget, lift implication via inclusion.

4. **Transfer candidate:** **XOR index range sharding** (`--xor-index-range`) already implemented on the parent script; paired halves cover all 2002 partitions without overlap.

**Falsifiable:** If both halves return PARTIAL (exit 2) or finish with `d=3 feasible=False`, this run does **not** refute the global `d=3` question—it only shows these shards under this budget did not witness feasibility.

**Parent:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py`
