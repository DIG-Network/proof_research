# Analogy pass

## 1. Abstract structure

Fix **n** and threshold **t.** Participation count **k** lies in **[0, n].** A modular summary **h(k) = k mod m** threshold-aliases if **∃ k₁ < t ≤ k₂** with **k₁ ≡ k₂ (mod m)** ⇔ **m | (k₂ − k₁)** for some **crossing gap** in **D(n, t) = {k₂ − k₁ : 0 ≤ k₁ < t ≤ k₂ ≤ n}.**

## 2. Analogues

1. **Frobenius / coin problem** — which integers are representable as nonnegative combinations of a fixed set; here we care about **divisibility** by **m** hitting **D.**
2. **Nyquist** — alias frequencies determined by which **spacings** occur in the signal support.
3. **CRT / modulus choice** — recovering **k** from **k mod m** needs **m** larger than the **spread** of ambiguous differences.

## 3. Machinery

Enumerate **D** explicitly for small **n, t** (O(t(n−t+1)) gaps). **Alias at m** iff **∃ d ∈ D** with **m | d.** **No alias** iff **gcd(m, d) < m** for all **d ∈ D** (equivalently **m ∤ d** for all **d ∈ D**).

## 4. Transfer seed

**081** fixed **(n, t) = (10, 6)** and showed **D = {1, …, 10}.** **Hypothesis:** for **t = ⌊n/2⌋ + 1** (strict majority), **D = {1, …, n}** for all **n ≥ 2** **(or** **characterize** **exceptions** **).** If **D = {1, …, n},** then **m ≤ n** **⇒** **m ∈ D** **⇒** **alias** **at** **m,** and **first** **clean** **m** **=** **n + 1** **(same** **as** **081** **).**

---

# Formal hypothesis

**H1:** For every **n** in **{2, …, 30},** with **t = ⌊n/2⌋ + 1,** the gap set **D(n, t)** equals **{1, 2, …, n}.**

**H2:** Under **H1,** for each such **(n, t),** **k mod m** threshold-aliases iff **2 ≤ m ≤ n,** and the smallest **m** with no alias is **n + 1.**

**H3** **(** **bonus** **regression** **):** Same **D** **and** **mod-m** **alias** **law** **hold** **for** **all** **t ∈ {1,…,n}** **when** **n ≤ 20** **(** **full** **threshold** **range** **).**

**Falsification:** Any **n** with **D ≠ {1,…,n},** or any **m ≤ n** with no divisor relation to any gap, or **m = n+1** still aliasing.

**Outcome (after run):** **PASS** — see `results.md`.
