# Hypothesis — uniform quintuple power sums mod M (5-set vs 6-set)

## Analogy pass

1. **Abstract structure:** We compress subset signatures into a short vector of modular symmetric power sums \( (p_1,\ldots,p_5) \bmod M \) and ask for the smallest \(M\) at which two different threshold shells (here \(|S|=5\) vs \(6\)) collide under one uniform modulus.

2. **Analogues (≥3):**
   - **Moment problems in statistics:** Higher moments add information only if they are not algebraic consequences of lower ones in the chosen quotient ring.
   - **Signal quantization:** Each extra “sensor” is useless if, modulo the coarse grid, it repeats an earlier measurement (linearly dependent in the digit space).
   - **Finite-field symmetric polynomials:** Over \(\mathbb{Z}/2\mathbb{Z}\), \(x^k \equiv x\) for \(k\ge1\), so all power sums collapse to the same parity functional on the support.

3. **Machinery in those domains:** Dependence among observables modulo \(M\); Newton/Girard relations in characteristic two collapsing \(p_k\) to \(p_1\) mod 2 for our weight set’s parity pattern.

4. **Transfer seed:** Mod 2, for any \(k\ge1\), \(w^k \equiv w \pmod 2\) for integers \(w\). Hence \(p_k(S) \equiv \sum_{i\in S} w_i \pmod 2\) for every \(k\). The 5-tuple mod 2 is **five copies of one bit**, so adding \(p_4,p_5\) cannot separate shells any better than \(p_1\) alone at \(M=2\).

## Falsifiable claim

Let \(w_i=i+1\), \(n=10\), \(p_k(S)=\sum_{i\in S} w_i^k\). Let \(M^\*\) be the least \(M\ge 2\) such that some 5-set and some 6-set have identical \((p_1,\ldots,p_5)\bmod M\).

- **H1 (structural):** \(M^\*=2\) still, with the same parity mechanism as Entries 034, 065, 075 — fifth moment adds no independent bit mod 2.
- **H2 (empirical surprise):** \(M^\*>2\) — a collision first appears at a larger modulus (would require breaking the mod-2 collapse).

We test by exhaustive scan over \(M\) (same as 075, one more power).
