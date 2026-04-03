# Hypothesis

## Analogy pass (mandatory)

1. **Abstract structure:** For **`n=14`**, **`{7,8}`**, the combined split language **`coord + ⋃_{r=2}^{13} XOR_r`** has **`min_d=2`** (full union, memo-dict scan **`d=1..3`**). The next structural question is whether this **`min_d`** is an artifact of **`n=14`** or stable when the majority threshold slice is the same (**`t=8`**, shells **`{7,8}`**) at smaller **`n`**.

2. **Analogous domains:** (i) **Finite-size scaling** in statistical mechanics — critical exponents often stabilize before the thermodynamic limit; here **`min_d`** plays the role of a discrete “order parameter” for refutation-tree depth. (ii) **Ramsey-type thresholds** — combinatorial parameters can jump at specific **`n`**. (iii) **Parameter continuation** in optimization — track a quantity along a family to see if a phenomenon is robust.

3. **Machinery elsewhere:** Hold the slice fixed, decrease **`n`** (here **`n=13`**), recompute the same **union-of-all-r** language and read **`min_d`** from the same DP.

4. **Transfer seed:** Run **`n=13`** parent with **`--union-rs`** listing **`r=2..12`** (equivalent to full **`r=2..n-1`** XOR union), with default **`d=1..13`** scan and **`4M`** LRU, matching the spirit of the **`n=14`** full-union **`min_d`** experiment.

## Falsifiable claim

For **`n=13`**, **`{7,8}`**, **`coord + ⋃_{r=2}^{12} XOR_r`** (**`8177`** splits total), **`min_d=2`** (i.e. **`d=1`** infeasible, **`d=2`** feasible). If instead **`min_d≥3`** or **`min_d=1`**, the **`n=14`** **`min_d=2`** result would not extend unchanged down one **`n`**.
