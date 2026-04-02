# Hypothesis

**Claim:** For `n=14`, `{7,8}`, `d=3`-only probes on the **2002**-wide `r=5` / `r=9` XOR menus, a **non-contiguous** 1001-index submenu may behave differently from the contiguous half-shards `[0:1001)` and `[1001:2002)` under the same `exists_tree` / LRU envelope—possibly closing or revealing a witness where contiguous halves stayed PARTIAL.

**Rationale:** Session state flagged “non-contiguous 1001-wide XOR sub-menus” after both contiguous half-shards at `12e7/8M` remained PARTIAL. Lexicographic halves are a special cut; taking **every other** canonical XOR index (`0,2,4,…,2000`) preserves cardinality 1001 but interleaves “early” and “late” combinations, changing the effective split family order versus a prefix or suffix block.

## Analogy pass (mandatory)

1. **Abstract structure:** We approximate a large discrete search space (full XOR partition list) by a **structured subsample** of fixed size; completeness of the full menu is unknown, but negative/positive witnesses on subsets constrain where feasibility may lie.

2. **Analogous domains:** (a) **Stratified sampling** in statistics—splitting a population by index parity to reduce bias vs contiguous chunks. (b) **Interleaved trial order** in experiment design—alternating levels to average out drift. (c) **Bit-reversal / radical-inverse** quasi-Monte Carlo—non-contiguous index maps that improve uniformity.

3. **Machinery there:** Stratification uses disjoint representative subsets; interleaving decorrelates order effects; QMC uses deterministic non-contiguous index permutations for coverage.

4. **Transfer candidate:** **Parity / interleaved index subset** on the canonical `combinations` order—same size as a half-shard but different geometry—tests whether prior PARTIAL was sensitive to contiguous half-menu bias.

**Falsification:** If both `r=5` and `r=9` runs finish without PARTIAL and `d=3 feasible=False`, the odd-index 1001 menu is another negative submenu (like random 400×3), not a witness. If PARTIAL again, inconclusive at this budget. If `feasible=True`, would suggest a witness on that submenu (implication for full menu as per parent script comments on shards).
