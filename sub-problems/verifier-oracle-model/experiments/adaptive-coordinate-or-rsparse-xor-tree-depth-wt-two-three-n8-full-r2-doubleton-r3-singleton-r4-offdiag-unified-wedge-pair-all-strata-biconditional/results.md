# Results: n=8 unified wedge pair (off-diagonal s∈{0,1,2})

**Outcome:** PASS (logically; see vacuity note below)

**Measured counts (from script stdout):**

- Full grid cells: `111720` (= C(8,3)×C(8,3)×C(8,4) with ordered pair loop).
- Off-diagonal stratum `s=|T_i∩T_j|∈{0,1,2}`: **`107800`** cells (`s0=19600`, `s1=58800`, `s2=29400`).
- On that stratum: **`stratum_min_d2=0`**, **`stratum_pred=0`** (no `Q` equals `W_ij` or `W_ji`).
- Violations: **`0`** / **`0`**.
- Wall time: **`≈755.7s`** (~12.6 min), LRU cap `4M`.

**Interpretation:** The biconditional `min_d=2 ⇔ (Q∈{W_ij,W_ji})` holds because **both sides are false for every cell** in the scanned stratum: the fixed language never achieves depth 2 on these cells at n=8, and quartic `Q` never coincides with either wedge. This is **not** the same phenomenon as n=7, where there were **`1190`** positive depth-2 cells matching the wedge predicate exactly.

**Comparison:**

| n | stratum cells | min_d=2 count | pred hits | note |
|---|---------------|---------------|-----------|------|
| 7 | 20825 | 1190 | 1190 | genuine certificate |
| 6 | (n=6 port) | many | 0 | FAIL: d2 without pred |
| 8 | 107800 | 0 | 0 | PASS vacuous |
