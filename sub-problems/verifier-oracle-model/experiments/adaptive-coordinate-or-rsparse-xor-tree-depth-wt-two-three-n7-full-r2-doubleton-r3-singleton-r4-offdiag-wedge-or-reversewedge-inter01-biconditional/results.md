# Results: `W(i,j) ∨ W(j,i)` biconditional on `|T_i∩T_j|∈{0,1}`

**Outcome:** PASS

**Setup:** `n=7`, adaptive language: coordinate splits + full `r=2` XOR + two distinct `r=3` XOR splits (`i<j`) + one `r=4` XOR split `Q`. Stratum: off-diagonal pairs with `|T_i∩T_j|∈{0,1}` (`13475` cells of the `22050` grid).

**Predicate:** For triple masks `T_i`, `T_j` (with `i<j`),
- `W_ij = (T_i \ T_j) ∪ ([7] \ (T_i ∪ T_j))`
- `W_ji = (T_j \ T_i) ∪ ([7] \ (T_i ∪ T_j))`
- `pred ⇔ (Q = W_ij ∨ Q = W_ji)` (here `W_ij ≠ W_ji` on this stratum: `pred_both=0`)

**Measured counts (LRU `4M`, `wall_sec≈30.3`):**
- `stratum_min_d2=770`
- `stratum_pred=770` (exactly matches `min_d=2` count)
- `pred_wij=385`, `pred_wji=385`, `pred_both=0`
- Violations: `d2_not_pred=0`, `pred_not_d2=0`

**Conclusion:** On the `|∩|∈{0,1}` off-diagonal stratum, **`min_d = 2` if and only if** `Q` equals one of the two ordered wedges (either orientation). This symmetrizes the sound but incomplete ordered-wedge predicate from experiment 161 and completes the biconditional.
