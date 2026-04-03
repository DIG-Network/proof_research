# Hypothesis

## Analogy pass

1. **Abstract structure:** Extend the certified **`min_d=2`** ladder one step below **`n=8`**: if **`n∈{8,…,14}`** all have **`min_d=2`** on the full XOR union menu, **`n=7`**, **`{2,3}`** should behave the same.

2. **Analogous domains:** Induction down the **`n`** ladder; closure of a uniform depth certificate across shell geometry.

3. **Machinery:** Wrapper delegates to **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7/script.py`** with **`--union-rs 2..5`**.

4. **Transfer candidate:** **`total_splits=112`**, **`min_d=2`**, baselines **`coord_only min_d=7`**, **`coord_plus_full_7xor min_d=1`**.

## Falsifiable claim

**`coord + ⋃_{r=2}^{5} XOR_r`** on **`56`** masks has **`min_d = 2`** (4M LRU).
