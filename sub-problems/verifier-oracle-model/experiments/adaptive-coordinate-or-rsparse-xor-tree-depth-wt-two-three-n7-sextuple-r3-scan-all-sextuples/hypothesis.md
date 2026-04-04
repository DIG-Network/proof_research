# Hypothesis — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-sextuple-r3-scan-all-sextuples`

## Analogy pass

1. **Abstract structure:** Fix the `n=7`, shell `{2,3}` mask alphabet (56 masks). The verifier-oracle DP asks for the minimum decision-tree depth using coordinate splits plus a *sparse* menu of GF(2) parity splits (`r=2` full menu, plus a *subset* of `r=3` triple parities). Enumerating larger subsets of triple parities is the discrete analogue of adding more parity checks in a linear code: each new split refines the partition of mask space; we test whether **six** chosen triple parities ever yield a depth-2 certificate when the full `r=2` menu is already present.

2. **Where else this structure appears:**
   - **Coding theory:** lengthening a parity-check matrix by adding rows; threshold phenomena in whether the resulting code separates a target set in one round of “local decoding” style queries.
   - **Combinatorial group testing:** each XOR split is a test; we ask whether 6 adaptive tests (composed with coordinates) can identify a feasible leaf class in depth 2.
   - **Boolean function complexity:** parity splits are linear tests; the DP depth is a restricted decision-tree complexity measure on the indicator of “pure” mask subsets.

3. **Machinery in those domains:** codes use rank/distance; group testing uses coverage designs; Boolean complexity uses parity decision trees. Here the “cost” is *sequential* split depth under a fixed menu, not just linear independence.

4. **Transfer candidate:** Treat **six** triple parities as the next rung after exhaustive **five**-tuple enumeration (`C(35,5)`) showed **no** `min_d=2` witness. If **no** sextuple works either, the sparse `r=3` ladder is closed through arity 6 for this language family at `n=7`.

## Falsifiable claim

**Some** unordered **6-tuple** of **`r=3`** XOR split indices (among **35** triples), together with **coordinate splits** and the **full** **`r=2`** XOR menu, yields **`min_d=2`** on the `n=7`, `{2,3}` shell.

**Opposite (expected given quintuple closure):** **`witness_min_d2_count=0`** over all **`C(35,6)=1_623_160`** unordered sextuples.

## Parent / lineage

- Extends: `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-quintuple-r3-scan-all-quintuples` (exhaustive `C(35,5)`, all `min_d=3`).
