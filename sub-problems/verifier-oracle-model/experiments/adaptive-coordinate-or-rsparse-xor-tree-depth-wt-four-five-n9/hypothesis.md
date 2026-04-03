# Hypothesis

## Analogy pass

1. **Abstract structure:** Finite-size ladder for the majority-shell adaptive decision-tree model: at each **`n`**, take Hamming shells **`{⌊n/2⌋, ⌈n/2⌉}`** (here **`n=9`**, **`{4,5}`**) and measure **`min_d`** for **`coord + ⋃_{r=2}^{n-1} XOR_r`**.

2. **Analogous domains:** Parameter continuation; expressiveness of pooled parity tests; same DP template as **`n=10..14`**.

3. **Machinery:** Identical **`exists_tree`** DP; **`--union-rs`** mixes arities; LRU-capped memo for stability.

4. **Transfer candidate:** Expect **`min_d=2`** for **`coord + ⋃_{r=2}^{8} XOR_r`** on **`252`** masks, with baselines **`coord_only min_d=9`**, **`coord_plus_full_9xor min_d=1`**.

## Falsifiable claim

For **`n=9`**, popcount in **`{4,5}`**, the language **`coord + ⋃_{r=2}^{8} XOR_r`** has **`min_d = 2`** (4M LRU memo).
