# Results — uniform quadruple power sums mod M (5-set vs 6-set, n=10)

**Outcome:** PASS

**Setup:** Uniform weights `w_i = i+1`, `n=10`. For each subset size 5 and 6, compute raw power sums `S_k = sum_{i in S} w_i^k` for `k=1..4`. Scan `M` from 2 upward; first `M` where some 5-set and some 6-set have identical `(S1,S2,S3,S4) mod M`.

**Finding:** `FIRST_COLLISION_M = 2` with `mod_key = (1, 1, 1, 1)`.

**Witness (one of possibly many):**
- Five-set indices `(4,6,7,8,9)` → weights `(5,7,8,9,10)`, raw `(39, 319, 2709, 23683)`.
- Six-set indices `(0,1,2,3,4,5)` → weights `(1,2,3,4,5,6)`, raw `(21, 91, 441, 2275)`.
- Mod 2: both reduce to `(1,1,1,1)` (odd first moments; odd sums of odd squares/cubes/fourth powers for these multiset sizes).

**Interpretation:** Adding the fourth power does not postpone the first collision beyond `M=2` for this toy model: parity still collapses all four coordinates simultaneously, matching the single-power-sum experiment (065) in spirit.
