# Results — adaptive-coordinate-or-triple-xor-tree-depth-wt-five-vs-six

**Outcome:** **PASS**

**Domain:** `n=10`, Hamming weight in `{5,6}`, **462** masks as 462-bit DP state (same as **045** / **066** / **082**).

**Gate set:** At each internal node, either
- **coordinate** split on bit `x_i` (`i ∈ {0,…,9}`), or
- **triple-XOR** split on `x_i ⊕ x_j ⊕ x_k` for lexicographic triples `i<j<k` (**120** partitions, precomputed masks).

**Algorithm:** Memoized `exists_tree(bits, depth_remaining)` with `pure_bits` = all active masks share the same weight; child recursion as in **082**/**085** (empty side short-circuits).

**Measured feasibility (single run, `--budget-seconds 1200 --d-min 1`):**

| d | feasible | elapsed_sec |
|---|----------|-------------|
| 1 | False    | 0.000       |
| 2 | False    | 0.015       |
| 3 | False    | 0.732       |
| 4 | **True** | 0.706       |

**Conclusion:** **`min_d = 4`** for mixed coordinate + triple-XOR on this toy.

**Comparison:**
- **066** (coord + **pair**-XOR): **`min_d = 5`**.
- This language **strictly extends** **066** (every pair XOR is composable at higher depth, but **one** triple-XOR node induces partitions not equal to any **single** pair-XOR split).
- **074** certified `exists_tree(full,4)=False` under **066** semantics only; **d=4** becomes feasible when **weight-3** linear splits are allowed.

**Upper bounds:** `min_d ≤ 5` (subset of **066**), `min_d ≤ 10` (coordinates).
