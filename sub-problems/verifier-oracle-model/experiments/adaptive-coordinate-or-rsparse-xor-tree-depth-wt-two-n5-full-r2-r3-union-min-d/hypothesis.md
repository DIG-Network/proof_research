# Hypothesis

## Analogy pass

1. **Abstract structure:** Extend the certified full-menu ladder one step below **`n=6`**: if **`n≥6`** shows **`min_d=2`** on **`coord + ⋃_{r=2}^{n-2} XOR_r`** for the majority-adjacent shells, check whether **`n=5`** with weight-**`2`** masks only still matches.

2. **Analogous domains:** Finite-size scaling / small-**`n`** boundary where the DP language collapses; threshold geometry at **`n=5`** (majority **`t=3`**) with only **`10`** weight-**`2`** masks.

3. **Machinery:** Same DP as **`n=6`** driver; wrapper **`--union-rs 2,3`** (**`C(5,2)+C(5,3)=10+10=20`** splits).

4. **Transfer candidate:** Expect either **`min_d=2`** (continuation) or a **smaller** **`min_d`** if the domain is too small for the same obstruction.

## Falsifiable claim

**`coord + ⋃_{r=2}^{3} XOR_r`** on **`10`** masks (**`{2}`** only) has **`min_d = 2`** (4M LRU), matching the **`n≥6`** ladder.
