# Hypothesis

## Analogy pass

1. **Abstract structure:** For the majority slice on hypercube shells, we ask whether the minimal adaptive decision-tree depth for the full multi-arity XOR union menu stays at 2 as we step `n` down to the smallest odd size where the `{⌊n/2⌋, ⌈n/2⌉}` shell pair is nontrivial.

2. **Analogous domains:** Finite-size scaling (plateau of an order parameter); sensitivity of search depth to the expressiveness of a fixed split library; separating families in combinatorial group testing.

3. **Machinery:** Parameter continuation in `n`; DP certification of `min_d` for a fixed split language; union of parity menus as a single “rich” language.

4. **Transfer candidate:** If `min_d=2` held for `n∈{12,13,14}` with full XOR unions on the corresponding shells, expect the same for **`n=11`**, **`{5,6}`**, with **`r=2..10`**.

## Falsifiable claim

For **`n=11`**, popcount in **`{5,6}`**, the language **`coord + ⋃_{r=2}^{10} XOR_r`** (**2035** splits) has **`min_d = 2`** (with baselines **`coord_only min_d=11`**, **`coord_plus_full_11xor min_d=1`**).
