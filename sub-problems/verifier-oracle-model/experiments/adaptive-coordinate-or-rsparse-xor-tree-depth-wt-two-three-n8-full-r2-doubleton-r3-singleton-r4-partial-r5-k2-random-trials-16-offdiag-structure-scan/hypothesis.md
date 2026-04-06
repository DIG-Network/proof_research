# Hypothesis

**Claim (falsifiable):** On `n=8`, shell `{2,3,4}`, off-diagonal stratum `s=|T_i∩T_j|∈{0,1,2}`, there exists **some** **random** draw of **two** distinct XOR splits from the full `r=5` menu (`C(8,5)=56` splits) (**`NUM_TRIALS=16`**, **`SEED=0`**) such that, when appended to `coord + full r=2 + doubleton r=3 + singleton r=4`, the stratum satisfies **`0 < stratum_min_d2 < 107800`**.

**Rationale:** Exhaustive **`K=1`** partial **`r=5`** yields uniform **`stratum_min_d2=3850`**. Adding a second split may move toward full-menu saturation (**`107800`**) or land at an intermediate value; random sampling is a cheap probe before exhaustive **`C(56,2)=1540`**.

## Analogy pass

1. **Abstract structure:** Two-generator closure in a monotone family of XOR constraints; test whether the second generator pushes **`stratum_min_d2`** off the **`K=1`** plateau.

2. **Analogous domains:**
   - **Matroid rank:** one independent set vs. span after adding a second element.
   - **Percolation:** second bond may or may not connect to the giant component.
   - **Phase transitions:** sampled pairs along an interpolation between sparse and saturated statistics.

3. **Machinery:** Same per-trial aggregation as partial **`r=6`** **`K=2`** random probe; enumerate triple–quad grid with **`partial_p5`**.

4. **Seed:** Port **`…-partial-r6-k2-random-trials-16-offdiag-structure-scan`** with **`p5`**, **`len=56`**, **`K=2`**, **`sample(range(56), 2)`**.

## Memory / prior context (brief)

- **`…-partial-r5-k1-exhaustive-all-56-offdiag-structure-scan`**: every **`K=1`** menu ⇒ **`stratum_min_d2=3850`**.
- **`…-partial-r6-k2-exhaustive-all-378-offdiag-structure-scan`**: every **`K=2`** partial **`r=6`** menu ⇒ **`107800`**.

This experiment tests whether **`K=2`** partial **`r=5`** already saturates like **`r=6`** in a small random sample.
