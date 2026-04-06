# Journal entry

**Date:** 2026-04-06  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n8-full-r2-doubleton-r3-singleton-r4-partial-r6-k2-random-trials-16-offdiag-structure-scan`

**Context:** verifier-oracle-model (`n=8`, shell `{2,3,4}`, off-diagonal `s∈{0,1,2}` stratum)

**Hypothesis tested:** Some **random** draw of **two** distinct `r=6` XOR splits (**`K=2`**, **`NUM_TRIALS=16`**, **`SEED=0`**) yields **`0 < stratum_min_d2 < 107800`** when appended to `coord + full r=2 + doubleton r=3 + singleton r=4`.

**Outcome:** **FAIL**

**Key finding:** **All 16** trials give **`stratum_min_d2=107800`**, **`stratum_pred=0`**, **`107800`** `d2∧¬pred`, **`0`** false positives; **`total_wall_sec≈986.6`**. Behavior matches **`K=1`** exhaustive partial **`r=6`** on this statistic in the sampled draws. Exhaustive **`C(28,2)=378`** remains open (~**`11h`** sequential at ~**`100s`**/menu in this environment).

**Implications:**

- Treat random probe as **negative evidence** only; finite closure requires **`C(28,2)`** enumeration or a proof.
- Contrast remains: partial **`r=5`** **`K=1`** ⇒ uniform **`3850`**; partial **`r=6`** **`K∈{1,2}`** (this probe) ⇒ **`107800`**.

**Analogy pass summary:** Second high-arity parity may still lie in the same **saturated** closure as the first for **`r=6`**; **`r=5`** is the arity where **`K=1`** already shows an intermediate plateau.

**Space definition:** none
