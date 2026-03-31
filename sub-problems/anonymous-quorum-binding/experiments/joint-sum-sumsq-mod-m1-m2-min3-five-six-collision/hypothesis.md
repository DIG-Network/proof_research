# Hypothesis — joint sum + sum-of-squares mod (M₁,M₂), both moduli ≥ 3

## Analogy pass

1. **Abstract structure:** We want a **2D modular fingerprint** of a hidden 5- or 6-subset of weighted indices that might **separate** the two quorum shells without listing the set. Experiment **054** showed the lex-first pair **(2,2)** collapses because **w² ≡ w (mod 2)**, so both coordinates repeat parity.

2. **Where else this appears:**
   - **Redundant observables** in statistics: two “different” summary statistics that are functions of each other on the restricted support (e.g. Bernoulli: mean determines variance).
   - **Gauge / constraint redundancy** in physics: two measured channels that carry the same information along a submanifold of state space.
   - **Hash composition:** concatenating two 1-bit outputs that are both parity of the same bit vector.

3. **Machinery in those domains:** Identify **rank** of the map from hidden state to observed tuple; restrict parameters so the Jacobian (or discrete difference) has full rank.

4. **Transfer candidate:** **Raise the minimum modulus** so the second coordinate is not determined by the first on the support of interest — here, require **M₁ ≥ 3** and **M₂ ≥ 3**, then scan lexicographic **(M₁,M₂)** for the **first** 5-set vs 6-set collision on **(Σw mod M₁, Σw² mod M₂)** with **n = 10**, **w_i = i+1**.

## Falsifiable claim

For **n = 10**, **|S| ∈ {5,6}**, weights **w_i = i+1**, there exists a collision for some **(M₁,M₂)** with **3 ≤ M₁, M₂ ≤ scan_max** in lex order; we record the **first** such pair and witness sets. If none up to `scan_max`, outcome **INCONCLUSIVE** (bounded search only).

## Relation to 054

054’s first hit **(2,2)** is an **artifact of mod 2**. This experiment asks whether **excluding M₁,M₂ < 3** delays collision enough to matter in a fixed scan window, or whether a small **≥3** pair still collides quickly.
