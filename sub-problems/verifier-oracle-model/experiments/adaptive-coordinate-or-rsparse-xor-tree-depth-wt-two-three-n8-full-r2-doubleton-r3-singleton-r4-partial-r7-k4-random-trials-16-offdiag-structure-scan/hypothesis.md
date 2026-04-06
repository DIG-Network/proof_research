# Hypothesis

**Claim (falsifiable):** On the same `n=8`, shell `{2,3,4}`, off-diagonal stratum `s=|T_i∩T_j|∈{0,1,2}` grid as the strict full-menu scan, there exists a **random draw** of **`K=4`** distinct XOR splits from the **`r=7`** menu ( **`K(8,7)=8`** splits total) such that, when appended to `coord + full r=2 + doubleton r=3 + singleton r=4`, the stratum satisfies **`0 < stratum_min_d2 < 107800`**.

**Rationale:** Exhaustive scans showed **any full** `r∈{5,6,7}` menu jumps immediately to universal `min_d=2` on all **`107800`** stratum cells. A **partial** `r=7` submenu might sit strictly between the sparse baseline (`stratum_min_d2=0`) and saturation—analogous to “subcritical percolation” still leaving some non-depth-2 cells while others deepen.

## Analogy pass

1. **Abstract structure:** Fix a large structured grid of instances; strengthen a monotone resource (split menu size) from empty to full; ask whether intermediate resource levels can yield a **mixed phase** on the grid (here: a proper subset of cells at `min_d=2`).

2. **Analogous domains:**
   - **Percolation:** below \(p_c\) infinite cluster absent; above present; **near-critical** windows have fractal coexistence—discrete menus may mimic a finite “bond probability” sweep.
   - **Bootstrap percolation:** **minimal** activating sets vs **full** closure—intermediate infection sets can be nontrivial before full occupation.
   - **Sparse linear measurements:** **subset** of parity checks in LDPC leaves some error patterns undetected while catching others.

3. **Machinery:** scaling limits; activation rules; code minimum distance vs check-node degree.

4. **Seed:** Replace “all 8 `r=7` splits” by a **random `K=4`** subset and repeat **`NUM_TRIALS`** independent draws—cheap structure probe before any exhaustive `C(8,K)` enumeration.

## Memory / prior context (brief)

- `…-strict-subsets-r5-r6-r7-offdiag-structure-scan`: every **full** single-arity menu in `{5,6,7}` already gives **`107800/107800`** `min_d=2` on the stratum.
- Sparse base (no high menus): **`stratum_min_d2=0`**.

This experiment asks whether **strict subset** behavior can appear **inside** arity-7 alone, not only by omitting whole arities.
