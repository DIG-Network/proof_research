# Hypothesis

**Claim (falsifiable):** On `n=8`, shell `{2,3,4}`, off-diagonal stratum `s=|T_i∩T_j|∈{0,1,2}`, there exists **some** draw of **two** distinct XOR splits from the full `r=6` menu (`C(8,6)=28` splits) such that, when both are appended to `coord + full r=2 + doubleton r=3 + singleton r=4`, the stratum satisfies **`0 < stratum_min_d2 < 107800`**.

**Probe design:** **`NUM_TRIALS=16`**, **`SEED=0`**, uniform random **unordered** pairs of distinct indices in **`{0,…,27}`** (same random-trial pattern as partial **`r=7`** **`K=4`**). Exhaustive **`C(28,2)=378`** is deferred: one menu wall time is **~107s** here, so full enumeration is **~11h** sequential.

**Rationale:** Partial **`r=6`** with **`K=1`** already saturates **`stratum_min_d2=107800`** on every singleton menu. Partial **`r=5`** with **`K=1`** yields uniform intermediate **`3850`**. **`K=2`** for **`r=6`** is the next menu size that might (or might not) leave the all-or-nothing **`{0,107800}`** regime before full **`r=6`** saturation.

## Analogy pass

1. **Abstract structure:** Enrich a fixed sparse base language with an increasing set of high-arity XOR parities; track whether the **first** nontrivial intermediate **cardinality** of depth-**2** witnesses appears at **menu cardinality 1 or 2** (per-**`r`** menu).

2. **Analogous domains:**
   - **Bootstrap percolation:** threshold for activation can jump at **one** extra edge or require **two** depending on graph geometry.
   - **Matroid rank:** one generator may already span the same flat as many; a **second** generator may be redundant or may increase rank.
   - **Coding theory:** adding **two** parity checks vs **one** can change minimum distance by a **cliff** or a **staircase**.

3. **Machinery:** Random sampling over **`C(28,2)`** before committing to exhaustive **`378`** enumeration; same per-trial aggregation as **`K=1`** partial scans.

4. **Seed:** Port **`…-partial-r7-k4-random-trials-16-offdiag-structure-scan`** with **`p6`**, **`K=2`**, **`universe=28`**.

## Memory / prior context (brief)

- **`…-partial-r6-k1-exhaustive-all-28-offdiag-structure-scan`**: every **`K=1`** partial **`r=6`** menu ⇒ **`stratum_min_d2=107800`**.
- **`…-partial-r5-k1-exhaustive-all-56-offdiag-structure-scan`**: every **`K=1`** partial **`r=5`** menu ⇒ uniform **`stratum_min_d2=3850`** (**`0<3850<107800`**).

This experiment tests whether **two** **`r=6`** splits can escape universal **`107800`** saturation the way **`r=5`** does at **`K=1`**.
