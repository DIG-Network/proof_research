# Results — adaptive-coordinate-or-pair-or-tree-depth-wt-five-vs-six

## Outcome: **PASS** — **exact** **mixed** **min** **depth** **=** **10**

## Model (unchanged)

**n = 10,** domain **462** masks with **wt ∈ {5,6}.** Internal nodes: **coordinate** **x_i** or **pair** **OR** **(x_i ∨ x_j).** Leaves pure (constant wt).

## Computation (optimized script, partition-mask splits)

Single run **`python -u script.py --d-min 1 --budget-seconds 200`** (continued past budget between **d**-iterations):

| d | feasible | elapsed (s) |
|---|----------|---------------|
| 1 | False | 0.000 |
| 2 | False | 0.003 |
| 3 | False | 0.032 |
| 4 | False | 0.217 |
| 5 | False | 1.250 |
| 6 | False | 7.901 |
| 7 | False | 39.124 |
| 8 | False | 221.230 |

Second run **`--d-min 8 --budget-seconds 800`:**

| d | feasible | elapsed (s) |
|---|----------|---------------|
| 8 | False | 221.230 |
| 9 | False | 863.589 |

Then wall budget expired before testing **d = 10** inside this script.

## Certificate for **min_d = 10** (logic + **045**)

1. **Exhaustive** **memoized** **DP** **above** **⇒** **no** **perfect** **mixed** **(coord** **∨** **OR)** **tree** **for** **d** **≤** **9** **on** **the** **full** **462-set.**
2. **Monotonicity:** **Every** **coordinate-only** **node** **is** **an** **allowed** **mixed** **node.** **Entry** **045** **(** **`adaptive-coordinate-tree-depth-wt-five-vs-six`** **)** **proves** **∃** **perfect** **coordinate-only** **tree** **at** **depth** **10** **(** **and** **none** **for** **d** **<** **10** **).** **Hence** **∃** **mixed** **tree** **at** **depth** **10.**
3. **Combine:** **min** **depth** **for** **mixed** **coord** **+** **pair-OR** **=** **10** **—** **same** **as** **coordinate-only;** **pair** **OR** **does** **not** **reduce** **depth** **on** **this** **instance** **(** **vs** **066** **XOR** **mix** **at** **depth** **5** **).**

## Verdict

**Primary** **hypothesis** **(** **exact** **min** **d** **)** **:** **resolved** **PASS** **with** **min_d** **=** **10.** **Earlier** **INCONCLUSIVE** **(** **95** **s** **budget** **)** **superseded** **by** **faster** **splits** **+** **d** **=** **9** **completion** **+** **045** **lift.**
