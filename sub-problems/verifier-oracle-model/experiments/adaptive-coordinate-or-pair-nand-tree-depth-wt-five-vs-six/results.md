# Outcome: **PASS**

## Claim

On **n = 10**, domain **wt ∈ {5,6}** (**462** masks), adaptive trees whose internal nodes are **coordinate** **x_k** or **pair-NAND** **NAND(x_i, x_j)** with branch **0** iff **both** bits are **1** have **minimum** separating depth **min_d = 10**.

## Evidence

### 1. Negative certificate: **d = 1 … 9** infeasible

Single run (no `--d-min`; budget **900** s):

| d | feasible | elapsed_sec |
|---|----------|-------------|
| 1 | False | 0.000 |
| 2 | False | 0.002 |
| 3 | False | 0.022 |
| 4 | False | 0.225 |
| 5 | False | 1.438 |
| 6 | False | 7.450 |
| 7 | False | 25.546 |
| 8 | False | 114.768 |
| 9 | False | 1145.066 |

Run ended **INCONCLUSIVE** (exit **2**) only because the wall clock expired **before** starting **d = 10**; all listed depths completed with **`feasible=False`**.

### 2. Positive certificate: **d = 10** feasible

`python -u script.py --budget-seconds 400 --d-min 10`:

- **d = 10** **feasible = True**, **elapsed_sec ≈ 227.5**
- **`min_depth_found = 10`**, **PASS** (exit **0**)

### 3. Min depth

With **d ≤ 9** ruled out and **d = 10** ruled in: **min_d = 10**.

Same as **coordinate-only** **045** and **mixed** **pair-OR** **082**. **Unlike** **066** **/** **084** **(XOR/XNOR,** **min_d** **=** **5** **).**

## Relation to **053**

**053** **classifies** **2-bit** **gates** **by** **(a,b) ↦ (1−a,1−b)** **invariance:** **only** **XOR/XNOR** **among** **nontrivial** **AND/OR/XOR/XNOR.** **NAND** **is** **asymmetric** **like** **OR** **under** **that** **map;** **here** **NAND** **behaves** **like** **OR** **for** **min** **depth** **(** **10** **),** **not** **like** **XOR** **(** **5** **).**
