# Hypothesis — joint-min-max-sum-product-quadruple-square-weights-extended-n-scan

## Analogy pass

1. **Abstract structure:** We test whether a fixed public embedding of validator indices into weights (here squares) makes the exact aggregate fingerprint `K(S) = (min, max, sum, product)` injective enough to separate the `|S|=5` shell from the `|S|=6` shell as `n` grows. This is a discrete “phase boundary” question: at which universe size does combinatorial overlap of multiset statistics first appear?

2. **Where else does this structure appear?**
   - **Statistical mechanics / percolation:** onset scales often depend on lattice geometry, not just cardinality.
   - **Coding theory:** separating constant-weight shells by a low-dimensional summary is like asking when a non-linear map becomes many-to-one across cosets.
   - **Additive combinatorics:** collisions between different subset sizes under moment-like data are sensitive to the actual multiset of summands, not only `n`.

3. **Machinery in those domains:** critical thresholds, design distance vs dual distance, and inverse problems for subset sums — none gives a direct certificate here; we use exhaustive shell comparison as a toy falsifier.

4. **Transfer candidate:** **Geometry of the weight sequence** (square growth vs linear) changes the feasible `(min,max,Σ,Π)` tuples enough to delay shell collisions; extending `n` quantifies how far that delay lasts.

## Falsifiable claim

For **`w_i = (i+1)^2`**, **`i = 0..n-1`**, there is **no** 5-vs-6 **exact** cross-shell collision for **`K = (min, max, Σ w_i, Π w_i)`** for any integer **`n`** with **`11 ≤ n ≤ 35`**.

- **PASS** if the scan finds **no** such collision in that range.
- **FAIL** if some **`n`** in the range exhibits **`keys5 ∩ keys6 ≠ ∅`**, with the script printing the minimal such **`n`** and a witness **`K`**.

## Lineage

Extends **`joint-min-max-sum-product-quadruple-weight-schedules-minimal-n-scan` (098)**, which found no collision for squares on **`n ∈ [11,18]`** only.
