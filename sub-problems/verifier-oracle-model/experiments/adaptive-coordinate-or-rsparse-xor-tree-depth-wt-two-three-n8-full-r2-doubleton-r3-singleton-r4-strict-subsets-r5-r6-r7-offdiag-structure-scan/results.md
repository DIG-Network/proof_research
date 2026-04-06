# Results

**Outcome:** FAIL (hypothesis falsified — in the sense of the pre-registered claim below)

**Pre-registered success criterion (script exit 0):** There exists a strict nonempty subset of the full `{r5,r6,r7}` XOR menus such that on the off-diagonal `s∈{0,1,2}` stratum, `0 < stratum_min_d2 < 107800`.

**Observed:** For **each** of the six strict nonempty masks over `{r5,r6,r7}`:

| high_mask (bits r5,r6,r7) | label   | stratum_min_d2 | stratum_pred | viol_d2_not_pred | viol_pred_not_d2 | wall_sec |
|---------------------------|---------|----------------:|-------------:|-----------------:|-----------------:|---------:|
| `0b001`                   | r5      | 107800          | 0            | 107800           | 0                | 266.471  |
| `0b010`                   | r6      | 107800          | 0            | 107800           | 0                | 70.752   |
| `0b011`                   | r5+r6   | 107800          | 0            | 107800           | 0                | 116.132  |
| `0b100`                   | r7      | 107800          | 0            | 107800           | 0                | 16.275   |
| `0b101`                   | r5+r7   | 107800          | 0            | 107800           | 0                | 30.721   |
| `0b110`                   | r6+r7   | 107800          | 0            | 107800           | 0                | 23.762   |

**Total wall (sequential):** ≈ **524.3 s** (~8.7 min) for all six passes.

**Interpretation:** On this fixed `{2,3,4}` shell grid, **appending the full XOR menu at any single arity in `{5,6,7}`** already forces `min_d=2` on **every** stratum cell (`107800/107800`). There is **no** “partial witness” window between the sparse baseline (`stratum_min_d2=0`, prior PASS experiment) and the saturated high-menu regime: the transition is a **cliff** at the first inclusion of any full `r∈{5,6,7}` menu.

**Note:** The full triple `{r5,r6,r7}` mask (`0b111`) was not re-scanned here; the prior experiment `…-plus-full-r5-r6-r7-…` already recorded `107800` with the same diagnostics.
