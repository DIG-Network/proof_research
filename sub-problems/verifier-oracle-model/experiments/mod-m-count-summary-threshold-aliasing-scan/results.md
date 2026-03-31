# Results: mod-m count summary threshold aliasing scan

**Outcome:** `PASS`

## Setup

- **n = 10**, **t = ⌊n/2⌋ + 1 = 6**.
- **Summary:** **h(k) = k mod m** for integer **m ≥ 2**.
- **Threshold-aliasing at m:** ∃ **k₁ ∈ [0, t−1]**, **k₂ ∈ [t, n]** with **k₁ ≡ k₂ (mod m)**.

## Computed facts

1. **Realizable gaps** **k₂ − k₁** across the threshold cut are exactly **{1, 2, …, 10}** (full interval).
2. For each **m ∈ {2,…,10}**, a witness exists; lex-first witness printed by the script (e.g. **m = 2:** **(0, 6)** residue **0** — the earlier parity note **(4, 6)** is another witness).
3. **First m with no cross-threshold alias:** **m = 11 = n + 1**. For **m ≥ 11**, **no** pair **(k₁, k₂)** with **k₁ < t ≤ k₂** shares the same residue mod **m** (equivalently **m ∤ d** for all **d ∈ {1,…,10}**).
4. Regression loop **m = 2..199:** threshold-aliasing occurs **iff** **m ≤ n** for this fixed **(n, t)**.

## Verdict

**H1** and **H2** from `hypothesis.md` are confirmed. Any modulus **m ≤ n** makes **k mod m** **insufficient** as the **only** datum for deciding **k ≥ t** when **k** is only known to lie in **[0, n]**. Avoiding aliasing requires **m ≥ n + 1**, i.e. the summary has **≥ ⌈log₂(n+2)⌉** bits for this toy — on the order of **log n**, not **O(1)**.
