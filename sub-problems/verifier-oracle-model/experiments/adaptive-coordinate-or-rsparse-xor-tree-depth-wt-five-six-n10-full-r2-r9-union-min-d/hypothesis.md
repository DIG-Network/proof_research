# Hypothesis

## Analogy pass

1. **Abstract structure:** Continue the finite-size ladder for the majority-shell adaptive decision-tree model: if full XOR unions at **`n∈{11,12,13,14}`** yield **`min_d=2`**, the same should hold one step smaller at **`n=10`**, **`{5,6}`**, with **`r=2..9`**.

2. **Analogous domains:** Parameter continuation / scaling limits; library expressiveness vs minimal depth; union of parity split families as a single language.

3. **Machinery:** Same DP as sibling drivers; **`--union-rs`** to mix all nontrivial arities; LRU-capped memo for stability.

4. **Transfer candidate:** Expect **`min_d=2`** for **`coord + ⋃_{r=2}^{9} XOR_r`** on **`462`** masks, with baselines **`coord_only min_d=10`**, **`coord_plus_full_10xor min_d=1`**.

## Falsifiable claim

For **`n=10`**, popcount in **`{5,6}`**, the language **`coord + ⋃_{r=2}^{9} XOR_r`** (**1012** splits) has **`min_d = 2`** (4M LRU memo).
