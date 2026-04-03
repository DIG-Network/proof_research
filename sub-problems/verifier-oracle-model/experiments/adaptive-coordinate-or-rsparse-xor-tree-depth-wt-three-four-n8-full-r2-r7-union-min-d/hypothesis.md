# Hypothesis

## Analogy pass

1. **Abstract structure:** Extend the certified **`min_d=2`** ladder one step below **`n=9`**: if **`n∈{9,…,14}`** all have **`min_d=2`** on the full XOR union menu, **`n=8`**, **`{3,4}`** should behave the same.

2. **Analogous domains:** Induction down the **`n`** ladder; closure of a uniform depth certificate across shell geometry.

3. **Machinery:** Wrapper delegates to **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-three-four-n8/script.py`** with **`--union-rs 2..7`**.

4. **Transfer candidate:** **`total_splits=246`**, **`min_d=2`**, baselines **`coord_only min_d=8`**, **`coord_plus_full_8xor min_d=1`**.

## Falsifiable claim

**`coord + ⋃_{r=2}^{7} XOR_r`** on **`126`** masks has **`min_d = 2`** (4M LRU).
