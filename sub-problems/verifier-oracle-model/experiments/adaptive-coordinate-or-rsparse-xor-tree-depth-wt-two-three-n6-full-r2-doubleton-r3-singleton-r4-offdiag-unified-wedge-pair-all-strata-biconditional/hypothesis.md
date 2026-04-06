# Hypothesis — n=6 off-diagonal unified wedge pair (all strata)

## Analogy pass

1. **Abstract structure:** For a fixed XOR-split language (coord + full r=2 + two r=3 + one r=4), the minimal decision-tree depth for a quartic mask `Q` is a discrete certificate. We ask whether **depth 2** is **exactly** characterized by **`Q` matching one of two ordered “wedge” masks** derived from the two triple masks **`T_i, T_j`**, on every off-diagonal cell where **`|T_i ∩ T_j| ∈ {0,1,2}`**.

2. **Where else:** (i) **Model checking / predicate minimization** — collapse a piecewise specification when one branch is empty on the realized datatype. (ii) **Coding theory** — threshold-like properties of set differences vs unions. (iii) **Combinatorial geometry** — wedge regions as half-spaces in a Boolean lattice.

3. **Machinery there:** Dead-code elimination and **CNF/DNF simplification**; set systems and **inclusion–exclusion**; **Boolean lattice** order on subsets.

4. **Transfer seed:** The n=7 experiment **`…-n7-…-offdiag-unified-wedge-pair-all-strata-biconditional`** showed **`C_ij`** is never needed for quartics on **`s=2`**, so **`W_ij ∨ W_ji`** alone matches **`min_d=2`** on all off-diagonal strata. The same structural claim should be **portable** to **`n=6`** with the analogous **`15×20×15`** grid.

## Falsifiable claim

Let **`N=6`**, masks in **`{2,3}`**, language **coord + full r=2 XOR + two r=3 XOR splits (indices `i≤j` on `C(6,3)=20` triples) + one r=4 XOR split (`C(6,4)=15` quartics)**. For **`i<j`** with **`s = |T_i ∩ T_j| ∈ {0,1,2}`** and quartic **`Q`**:

**`min_d == 2` iff `Q ∈ {W_ij, W_ji}`** where  
**`W_ab = (T_a \ T_b) ∪ ([6] \ (T_a ∪ T_b))`**.

**Outcome recorded in `results.md` after running `script.py`.**
