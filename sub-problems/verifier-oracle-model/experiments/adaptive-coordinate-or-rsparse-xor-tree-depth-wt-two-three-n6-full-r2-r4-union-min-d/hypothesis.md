# Hypothesis

## Analogy pass

1. **Abstract structure:** Extend the certified **`min_d=2`** ladder one step below **`n=7`**: if **`n∈{7,…,14}`** all have **`min_d=2`** on the full XOR union menu (for the majority-adjacent shells), **`n=6`** with **`{2,3}`** should behave the same.

2. **Analogous domains:** Induction down the **`n`** ladder; closure of a uniform depth certificate across shell geometry.

3. **Machinery:** New **`n=6`** driver mirrors **`n=7`** CLI; wrapper delegates with **`--union-rs 2..4`** (**`n-2`** is the top nontrivial arity for **`n=6`**).

4. **Transfer candidate:** **`total_splits=50`** (**`C(6,2)+C(6,3)+C(6,4)=15+20+15`**), **`min_d=2`**, baselines **`coord_only min_d=6`**, **`coord_plus_full_6xor min_d=1`**.

## Falsifiable claim

**`coord + ⋃_{r=2}^{4} XOR_r`** on **`35`** masks (**`{2,3}`** only) has **`min_d = 2`** (4M LRU).
