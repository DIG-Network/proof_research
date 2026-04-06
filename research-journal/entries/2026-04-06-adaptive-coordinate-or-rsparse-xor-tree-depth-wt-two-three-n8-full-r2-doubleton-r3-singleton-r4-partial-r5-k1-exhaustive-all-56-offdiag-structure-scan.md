# Experiment entry

**Date:** 2026-04-06  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-partial-r5-k1-exhaustive-all-56-offdiag-structure-scan`  
**Context:** verifier-oracle-model  

## Hypothesis tested

On `n=8`, shell `{2,3,4}`, off-diagonal stratum `s=|T_i∩T_j|∈{0,1,2}`, some **`K=1`** choice from the full **`r=5`** XOR menu (**`C(8,5)=56`**) appended to `coord + full r=2 + doubleton r=3 + singleton r=4` yields **`0 < stratum_min_d2 < 107800`**.

## Outcome: PASS

Every one of the **56** singleton menus satisfies **`stratum_min_d2=3850`** (strictly between **0** and **107800**). **`total_wall_sec≈16092.6`**. Wedge predicate hits **0** on the stratum for every menu.

## Key finding

**Partial `r=5` at `K=1` does not saturate like partial `r=6`/`r=7`:** a single **`r=5`** split leaves **`stratum_min_d2`** on a **uniform intermediate plateau** (**3850**), whereas **partial `r=6` `K=1`** already forced **`107800`** on every menu (matching full **`r=6`**).

## Implications

- The “first high-arity XOR split alone closes the gap to full-menu saturation” phenomenon is **arity-sensitive** at **`n=8`**: **`r=5`** is below the threshold for that collapse at **`K=1`**.
- Next structural probes: **`K≥2`** partial **`r=5`**, or **`K=2`** partial **`r=6`** (**378** menus), or a closed-form explanation of **3850**.

## Analogy pass summary

Monotone closure / percolation-style: test whether **one** generator already spans the **saturated** flat. **Result:** **one `r=5`** generator lands in a **strictly intermediate** flat (**3850**), not the **107800** flat.

## Space definition

None.
