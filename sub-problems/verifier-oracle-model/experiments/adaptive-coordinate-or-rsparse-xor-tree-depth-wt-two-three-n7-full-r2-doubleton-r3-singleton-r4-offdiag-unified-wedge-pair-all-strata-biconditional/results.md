# Results

**Outcome:** PASS

**Setup:** `n=7`, shell `{2,3}`, language = coordinate partition + full `r=2` XOR + unordered pair of distinct `r=3` triples `(T_i,T_j)` with `i<j` + singleton `r=4` quartic `Q`. Off-diagonal cells: `20825` with `s = |T_i ∩ T_j| ∈ {0,1,2}` (`s0=2450`, `s1=11025`, `s2=7350`).

**Predicate:** `W_ij = (T_i \ T_j) ∪ ([7] \ (T_i ∪ T_j))`, `W_ji` with roles swapped. Claim: `min_d = 2` iff `Q ∈ {W_ij, W_ji}`.

**Measured:**
- `grid_done=22050`, `wall_sec≈30.389`, `LRU_CAP=4_000_000`
- `stratum_min_d2=1190`, `stratum_pred=1190`, `pred_wij=595`, `pred_wji=595`
- `viol_counts`: `d2_not_pred=0`, `pred_not_d2=0`

**Conclusion:** The **same** symmetric wedge-pair certificate characterizes `min_d=2` on the **entire** off-diagonal union `s∈{0,1,2}`; no separate `C_ij` branch is needed (consistent with experiment 164: `C` is never a quartic on `s=2`).
