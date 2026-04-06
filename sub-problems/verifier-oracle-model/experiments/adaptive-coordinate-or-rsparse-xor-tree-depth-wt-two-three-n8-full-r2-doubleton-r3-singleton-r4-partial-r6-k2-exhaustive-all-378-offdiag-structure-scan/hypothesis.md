# Hypothesis

**Falsifiable claim:** Among all **`C(28,2)=378`** choices of **two** distinct `r=6` XOR splits appended to  
`coord + full r=2 + doubleton r=3 + singleton r=4`, at least one menu yields  
**`0 < stratum_min_d2 < 107800`** on the off-diagonal stratum **`s ∈ {0,1,2}`** (same aggregation as prior `n=8` scans; **`STRATUM_TOTAL=107800`**).

**Null / contrast:** Every such menu yields **`stratum_min_d2 ∈ {0, 107800}`**, matching **`K=1`** partial `r=6` exhaustive and the **`K=2`** random probe (**16/16** trials at **`107800`**).

## Analogy pass

1. **Abstract structure:** Fix a “language” (menu of XOR splits). For each triple of structural indices `(i,j,k)` in a large finite grid, compute a monotone complexity statistic **`min_depth`**; aggregate counts over a definable **stratum** (here: off-diagonal triple intersections of cardinality **`s∈{0,1,2}`**). Ask whether **intermediate** aggregate counts appear when **two** high-arity splits are added vs **one**.

2. **Where else:** (i) **Phase transitions / percolation** — order parameter often **0** or **saturated** except in a critical window; (ii) **coding theory** — minimum distance jumps when parity checks are added; (iii) **combinatorial optimization** — solution depth of adaptive decision trees under enriched move sets.

3. **Machinery in those domains:** Critical exponents and scaling windows; **GMR** bounds; **branching-factor** / **AND–OR tree** analyses.

4. **Transfer seed:** **Coding / parity**: a second independent `r=6` parity constraint might **not** change the **saturated** closure if both constraints lie in the same “error subspace” for this stratum — exhaustive enumeration tests that structural story.

## Memory / lineage (brief)

- **Parents:**  
  - `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-partial-r6-k1-exhaustive-all-28-offdiag-structure-scan` (**FAIL**, all **`107800`**) — **`extends`**.  
  - `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-partial-r6-k2-random-trials-16-offdiag-structure-scan` (**FAIL**, random **`K=2`**) — **`refines`** (closure of random probe).

**Exit:** **0** if any menu has **`0 < d2 < 107800`**; **1** if none.
