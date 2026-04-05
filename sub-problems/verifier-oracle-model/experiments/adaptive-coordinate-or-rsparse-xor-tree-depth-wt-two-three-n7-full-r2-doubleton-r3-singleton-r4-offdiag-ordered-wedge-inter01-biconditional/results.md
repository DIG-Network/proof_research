# Results — ordered wedge on `|∩|∈{0,1}`

**Outcome:** **FAIL**

**Setup:** Same `22050`-cell grid as structure-scan: `n=7`, shell `{2,3}`, coord + full `r=2` + doubleton `r=3` + singleton `r=4`, `LRU_CAP=4_000_000`.

**Stratum:** `i<j`, `s=|T_i∩T_j|∈{0,1}` → **13475** cells (`s0=2450`, `s1=11025`).

**Hypothesis:** `min_d=2` ⇔ `Q = W_{i,j}` with `W = (T_i\T_j) ∪ ([7]\(T_i∪T_j))`.

**Measured:**

| Metric | Value |
|--------|-------|
| `wall_sec` | ~30.5 |
| `stratum_min_d2` | 770 |
| `stratum_pred` (Q=W) | 385 |
| `viol d2_not_wedge` | 385 |
| `viol wedge_not_d2` | 0 |

**Interpretation:** Exactly half of the stratum’s `min_d=2` cells have `Q` equal to the ordered wedge; the other **385** have `min_d=2` with a different quartic `Q` (many printed witnesses share `k=34` → `Q=(3,4,5,6)`). There are **no** “wedge but not depth-2” false positives on this stratum (`wedge_not_d2=0`), so ordered wedge is a **sound but incomplete** certificate, not a biconditional.
