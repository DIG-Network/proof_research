# Hypothesis: off-diagonal depth-2 ⇔ quartic = symmetric difference of the two triples

## Analogy pass

1. **Abstract structure:** We fix a verifier-oracle-style split menu: coordinate splits plus full pair-XOR menu, plus **two** triple-XOR parities (possibly the same split twice), plus one quartic-XOR parity. The DP asks for the minimum decision-tree depth to separate all masks in the `{2,3}` shell. For `n=7`, singleton `r=3` + `r=4` has a clean **set-complement** characterization: `min_d=2` iff the quartic subset equals the complement of the triple. Adding a **second distinct** triple breaks that biconditional globally, but **1190** off-diagonal `(i<j,k)` cells still hit `min_d=2`.

2. **Where else does this appear?**
   - **Error-correcting codes:** two parity checks on overlapping supports define a **syndrome** that pinpoints errors on the **symmetric difference** of support sets.
   - **Graph theory:** two triangles in `K_7` that share one vertex have edge-symmetric-difference forming a 4-cycle / 4-edge witness set.
   - **Boolean analysis:** XOR of two 3-juntas on overlapping variables activates exactly on coordinates in the symmetric difference of their minimal supports (here, 3-sets).

3. **Machinery in those domains:** syndromes aggregate to **sum (XOR)** of incident constraints; **support** of combined parity is **symmetric difference** when constraints are linear over `F_2`.

4. **Transfer candidate:** Identify the quartic subset `Q` with the **4-element set** `T_i △ T_j` (symmetric difference of the two triples). This is well-defined as a 4-set **iff** `|T_i ∩ T_j| = 1` (then `|T_i △ T_j| = 4`). When `i=j` (duplicate triple menu), revert to the known **complement** law `Q = [7] \ T_i`.

## Falsifiable claim

On the full `630×35` grid (`i≤j`, `k`) for `coord + full r=2 + [p3[i],p3[j]] + p4[k]`:

- If `i=j` and `min_d=2`, then `Q_k` is the complement of `T_i`.
- If `i<j` and `min_d=2`, then `|T_i ∩ T_j| = 1` and `Q_k` equals `T_i △ T_j` as sets.

Conversely, every cell satisfying the corresponding predicate should have `min_d=2`.

If any violation occurs, the symmetric-difference story is false or incomplete.
