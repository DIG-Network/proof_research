# Results: n=7 — complement iff for singleton r3 + r4 on full grid

**Outcome:** PASS

**Setup:** Same as `…-n7-full-r2-singleton-r3-singleton-r4-grid-scan`: `n=7`, shell `{2,3}`, coordinate splits + full `r=2` XOR (21 splits) + one `r=3` + one `r=4`, exhaustive `35×35` grid, LRU `4_000_000`, `d_max=n`.

**Verified claims (programmatic, all 1225 cells):**

1. **A:** Every cell with `min_d = 2` has the `r=4` subset equal to the complement of the `r=3` subset in `[7]`.
2. **B:** Every complementary pair `(T, [7]\setminus T)` has `min_d = 2`.
3. **C:** No cell with `min_d ≥ 3` is complementary.

**Counts:** `complement_pairs_on_diagonal=35`, `min_d2_cells=35`, `wall_sec≈1.65`.

**Interpretation:** The narrative “sharp structure” from the prior PASS grid experiment is now a **machine-checked** characterization: with this sparse triple+quad language on top of full pair XOR, depth-2 certificates are **exactly** the global `3+4` cut of all seven indices — no other alignment of one triple parity and one quad parity suffices.

**Command:**

```bash
python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-singleton-r3-singleton-r4-complement-iff-check/script.py
```
