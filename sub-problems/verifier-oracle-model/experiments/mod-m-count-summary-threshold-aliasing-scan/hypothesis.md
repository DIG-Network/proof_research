# Analogy pass (mandatory)

## 1. Abstract structure

The verifier sees **h(k) = k mod m** for an unknown participation count **k ∈ {0,…,n}**. Threshold soundness requires **k ≥ t** to be a function of **h(k)** alone. That holds iff **no** pair **(k₁, k₂)** satisfies **k₁ < t ≤ k₂** and **k₁ ≡ k₂ (mod m)**. This is **quantization** of an integer with **period m**: residue classes **fold** the line; the question is whether the fold **identifies** counts on opposite sides of **t**.

## 2. Where else this structure appears

1. **Nyquist / sampling** — aliasing when the signal bandwidth exceeds half the sampling rate; here **“bandwidth”** is the **range of crossing gaps** **{k₂−k₁}**.
2. **Modular hashing / rolling hashes** — **mod m** buckets collide on all pairs differing by a multiple of **m**.
3. **CRT / lift-uniqueness** — uniqueness of **k** from residues only when moduli exceed **spread** of admissible **k** (compare recovering **k ∈ [0,n]** from **k mod m**).

## 3. Machinery in those domains

- **Number theory:** **k₁ ≡ k₂ (mod m)** ⇔ **m | (k₂−k₁)**.
- **Discrete geometry:** admissible gaps between the lower interval **[0, t−1]** and upper **[t, n]** form a set **D ⊆ {1,…,n}**; **m** must divide **no** element of **D** for **h** to separate the threshold classes.

## 4. Transfer seed

For **n = 10**, **t = 6**, gaps **k₂−k₁** with **k₁ < t ≤ k₂** cover **every** **d ∈ {1,…,10}** (e.g. **(5,6)** gives **1**, **(0,10)** gives **10**). Hence **m | d** for some **d ≤ 10** iff **m ≤ 10** (take **d = m** with witness **(0, m)** when **m ≤ 10** and **m ≥ 6**… need **k₂ = m ≥ 6** and **k₁ = 0 < 6**: works for **m ∈ {6,…,10}**; for **m ≤ 5** use **(5, 5+m)** if **5+m ≤ 10** i.e. **m ≤ 5** gives **(5,5+m)** with **5+m ≥ 6** for **m ≥ 1**). **Conjecture:** aliasing exists iff **m ≤ n**, and **first** **m** with **no** cross-threshold collision is **n+1 = 11**.

---

# Formal hypothesis

Let **n = 10**, **t = ⌊n/2⌋ + 1 = 6**. For integer **m ≥ 2**, say **m** **threshold-aliases** if there exist integers **k₁, k₂** with **0 ≤ k₁ ≤ t−1**, **t ≤ k₂ ≤ n**, and **k₁ ≡ k₂ (mod m)**.

**H1:** **m** threshold-aliases iff **m ≤ n**.

**H2:** The smallest **m** such that **no** threshold-aliasing occurs is **n + 1 = 11**.

**Falsification:** Any **m ≤ n** with exhaustive scan showing no **(k₁, k₂)**, or any **m > n** with a witness pair.

**Outcome (after run):** **PASS** — see `results.md`.
