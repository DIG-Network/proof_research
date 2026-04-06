# Results

**Outcome:** FAIL

**Language:** coordinate partitions + full `r=2` XOR + doubleton `r=3` `{T_i,T_j}` + singleton `r=4` `Q` + **full** XOR menus for `r=5`, `r=6`, and `r=7` (same `n=8` weight-`{2,3}` mask universe as the parent driver).

**Grid:** all `111720` cells enumerated; off-diagonal stratum `i<j` and `s=|T_i∩T_j|∈{0,1,2}` has **`107800`** cells (`s0=19600`, `s1=58800`, `s2=29400`).

**Measured:**

| Metric | Value |
|--------|-------|
| `wall_sec` | `37.380` |
| LRU cap | `4_000_000` |
| `stratum_min_d2` | `107800` (every stratum cell) |
| `stratum_pred` (`Q∈{W_ij,W_ji}`) | `0` |
| Violations `d2 ∧ ¬pred` | `107800` |
| Violations `pred ∧ md≠2` | `0` |

**Reasoning:** Appending full `r=5,r=6,r=7` XOR splits makes **depth-2 feasibility universal** on this stratum for **every** quartic `Q`, while the wedge masks `W_ij,W_ji` are still **never** equal to a 4-subset `Q` in this encoding (`pred=0` throughout). Hence the biconditional `min_d=2 ⇔ Q∈{W_ij,W_ji}` is false: the left-hand side is always true on the stratum and the right-hand side is always false.

**Contrast:**

- Sparse menu only (prior n=8 experiment): `stratum_min_d2=0` — biconditional **vacuously** PASS.
- This enrichment: `stratum_min_d2=107800` — biconditional **maximally** FAIL (all `d2_not_pred`).

**Implication:** The n=7-style wedge law is not a stable certificate under “add the splits that globally lower `min_d`”; making the menu strong enough to unlock `min_d=2` on `n=8` **over-separates** and destroys the geometric selector role of `Q`.
