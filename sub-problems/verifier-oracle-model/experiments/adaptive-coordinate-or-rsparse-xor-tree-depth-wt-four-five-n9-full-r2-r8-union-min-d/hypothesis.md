# Hypothesis

## Analogy pass

1. **Abstract structure:** Extend the certified **`min_d=2`** ladder one step below **`n=10`**: if **`n∈{10,…,14}`** all have **`min_d=2`** on the full XOR union menu, **`n=9`**, **`{4,5}`** should behave the same.

2. **Analogous domains:** Induction down the **`n`** ladder; closure of a uniform depth certificate across shell geometry.

3. **Machinery:** Wrapper delegates to **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-four-five-n9/script.py`** with **`--union-rs 2..8`**.

4. **Transfer candidate:** **`total_splits=501`**, **`min_d=2`**, baselines **`coord_only min_d=9`**, **`coord_plus_full_9xor min_d=1`**.

## Falsifiable claim

**`coord + ⋃_{r=2}^{8} XOR_r`** on **`252`** masks has **`min_d = 2`** (4M LRU).
