# Entry 051 — xor-pair-shell-complement-swap-regression

**Date:** 2026-03-30  
**Context:** `sub-problems/verifier-oracle-model`  
**Experiment:** `experiments/xor-pair-shell-complement-swap-regression/`

## Hypothesis tested

**Formalize** **049’s** **condition** **n = 2T − 1** **as** **equivalent** **to** **“global** **complement** **swaps** **exactly** **the** **two** **Hamming** **shells** **T−1** **and** **T”** **and** **regress** **the** **XOR-pair** **decision-tree** **shortcut** **against** **backtracking** **on** **a** **small** **(n,T)** **grid.**

## Outcome: **PASS**

## Key finding

- **Algebraic:** **For** **1 ≤ T−1 < T ≤ n,** **w ↦ n−w** **exchanges** **T−1** **and** **T** **iff** **n = 2T − 1** **(brute-verified** **consistency** **with** **a** **direct** **predicate** **`complement_swaps_two_shells`).**
- **Computational:** **`n == 2T−1`** **matches** **implemented** **`xor_pairwise_impossible`;** **for** **n ≤ 6,** **XOR** **tree** **exists** **within** **depth** **80** **iff** **not** **impossible;** **(5,3)** **spot** **—** **no** **tree** **to** **depth** **100.**

## Implications

- **049** **/ ** **BREAKTHROUGHS** **obstruction** **is** **now** **anchored** **to** **a** **precise** **shell-swap** **identity,** **not** **only** **a** **one-line** **pattern.**
- **Does** **not** **rule** **out** **other** **(n,T)** **where** **XOR-pair** **trees** **fail** **for** **different** **reasons** **—** **only** **this** **symmetry** **class** **is** **characterized** **here.**

## Analogy pass summary

**Gauge** **/ ** **involution** **quotient;** **F₂** **even-support** **characters** **vs** **all-ones** **—** **seed** **was** **making** **the** **complement** **swap** **condition** **explicit.**
