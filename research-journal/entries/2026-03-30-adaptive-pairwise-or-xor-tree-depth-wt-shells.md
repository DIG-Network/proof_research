# Entry 049 — adaptive-pairwise-or-xor-tree-depth-wt-shells

**Date:** 2026-03-30  
**Context:** `sub-problems/verifier-oracle-model`  
**Experiment:** `experiments/adaptive-pairwise-or-xor-tree-depth-wt-shells/`

## Hypothesis tested

Extend **048** (pairwise **AND**) to **OR** and **XOR** pair gates on the same **wt ∈ {T−1, T}** domains `(5,3)` and `(6,4)`.

## Outcome: **PASS**

## Key finding

- **OR:** `(5,3)` min depth **6** (same as AND); **`(6,4)` min depth 9** — **worse** than AND’s **6** and **> n**.
- **XOR:** **`(5,3)` impossible** when **`n = 2T − 1`** (here 5 = 2·3−1): **global complement** swaps shells; **pair XOR invariant** under complement ⇒ **no** perfect tree (**proof** in experiment **`results.md`**).
- **XOR `(6,4)`:** min depth **3** **≪** **n** — **strong** **positive** **contrast** **to** **coordinate** **/ ** **AND** **barriers** **on** **this** **instance.**

## Implications

- Non-coordinate **does** **not** **mean** **uniformly** **stronger** **or** **weaker:** **gate** **choice** **and** **(n,T)** **symmetry** **matter** **more** **than** **“nonlinear** **vs** **coordinate”** **alone.**
- Logged **impossibility** **lemma** **in** **`BREAKTHROUGHS.md`** **(low** **novelty** **confidence).**

## Analogy pass summary

Boolean **basis** **{∨,⊕}** **vs** **∧;** **reliability** **OR** **gates;** **pooled** **parity** **tests.** **Seed:** **De** **Morgan** **/ ** **complement** **—** **delivered** **via** **explicit** **XOR** **invariance** **obstruction.**
