# Hypothesis

## Analogy pass

1. **Abstract structure:** We probe whether the adaptive-coordinate + r-sparse XOR decision-tree DP’s difficulty for `d=3` on half-sized XOR submenus depends on *which* half of the canonical `C(N,r)` XOR index order is scanned, not only on budget/LRU.

2. **Where else:** (i) Complementary strata in survey sampling (paired designs). (ii) Cosets of an index subgroup in experimental design. (iii) Chessboard / parity bipartition of an ordered list.

3. **Machinery there:** Complementary designs often have symmetric variance structure; here we test symmetry of *computational* hitting time, not statistical estimators.

4. **Transfer seed:** The sibling run used indices `0,2,…,2000` (1001 XOR gates). The **complementary** 1001-set is `1,3,…,2001`. If the DP’s partial completion is an artifact of early vs late indices in the fixed `combinations` order, this coset might differ.

## Falsifiable claim

Under `n=14`, shells `{7,8}`, `r∈{5,9}`, `d=3`-only, `12e7` `exists_tree` calls and `8M` LRU per run, at least one run will report `d=3 feasible=True`, **or** wall time / PARTIAL behavior will differ materially from the even-interleave sibling.

If both runs are PARTIAL with no witness (as for `0,2,…,2000`), the hypothesis that coset choice unlocks `d=3` at this budget is **falsified** for this pair.
