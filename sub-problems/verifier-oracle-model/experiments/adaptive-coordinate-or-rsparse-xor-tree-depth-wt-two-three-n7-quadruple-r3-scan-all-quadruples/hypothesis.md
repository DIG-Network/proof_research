# Hypothesis — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-quadruple-r3-scan-all-quadruples`

## Analogy pass

1. **Abstract structure:** We seek a *depth-2* decision tree in a fixed “language” (coordinate splits + sparse XOR parities) that separates the `{2,3}` shell on `[7]`; adding independent parity constraints is analogous to adding *linear* measurements in group testing or *parity checks* in coding—each new split may or may not reduce minimal depth.

2. **Where else this structure appears:**
   - **Decision tree / query complexity:** each split is a Boolean query; minimal depth is certificate size.
   - **Linear codes / parity checks:** XOR splits are linear functionals on the mask domain; threshold-like separation may need a minimum rank of constraints.
   - **Committee voting / threshold functions:** majority is a high-degree symmetric function; low-depth certificates often need many independent “views.”

3. **Machinery in those domains:** Fourier/sparse parity lower bounds; covering arguments; rank arguments for affine subspace structure.

4. **Transfer seed:** If **three** independent `r=3` XOR parities still leave **`min_d=3`**, **four** might be the first arity where a **depth-2** certificate exists—or the obstruction may persist (uniform **`min_d=3`**). Exhaustive **`C(35,4)`** enumeration decides this finite slice.

## Falsifiable claim

At **n=7**, **shell `{2,3}`**, language **coord + full `r=2` XOR menu + four `r=3` XOR splits** (unordered quadruple of triple indices), **some** quadruple achieves **`min_d=2`**.

**Opposite outcome:** **every** quadruple yields **`min_d=3`** (**`witness_min_d2_count=0`**).
