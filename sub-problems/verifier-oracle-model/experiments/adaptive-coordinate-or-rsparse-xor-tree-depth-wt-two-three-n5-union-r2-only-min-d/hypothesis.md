# Hypothesis — n=5, {2,3} shell, XOR union r=2 only

## Analogy pass

1. **Abstract structure:** Adaptive decision trees over bitmasks partition the mask domain; `min_d` is the shallowest depth that separates two threshold-induced label classes. Adding XOR splits at arity `r` enlarges the menu; we ask which menu items are **load-bearing** for a observed depth bump.

2. **Analogous domains:**
   - **Circuit complexity / gate basis:** A function’s depth may depend on which fan-in gates are available; dropping a gate type can collapse or preserve depth.
   - **Experimental design / factorial models:** A response may depend only on main effects (order-2 interactions) while higher-order terms are statistically redundant.
   - **Graph pebbling / split trees:** Some edge types in a splitting strategy may be removable without changing the optimal pebbling depth.

3. **Machinery in those domains:** Basis reduction (minimal generating sets), ANOVA-style variance decomposition, critical-path analysis on decision trees.

4. **Transfer seed:** Treat XOR arities as **generators** of the split menu; test **minimality** of the generator set that produced `min_d=2` in the `r=2..3` union experiment.

## Falsifiable claim

For `n=5`, masks with popcount in `{2,3}` (20 masks), **coord + XOR union with only `r=2`** (10 pair splits) still has **`min_d=2`** (same as `r=2..3` union with 20 splits). If true, the **`r=3` XOR splits are not necessary** for the depth-2 certificate in that shell slice.

**Opposite outcome:** If `min_d≠2` with `r=2` only, then **`r=3` XOR splits were load-bearing** for `min_d=2` in the prior experiment. **Observed:** `min_d=3` (strictly worse than `2`).

## Parent / lineage

Builds on `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-union-r2-r3-only-min-d` (PASS: `min_d=2` with 20 splits).
