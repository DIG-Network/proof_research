# Hypothesis: |Q|=5 partial views — when do wt=5 and wt=6 both extend? (n=10, t=6)

## Analogy pass

1. **Abstract structure.** After **k** **coordinate** **probes**, the verifier holds **(Q, p)** with **z** ones on **Q** and **R = n − k** free coordinates. Global Hamming weight equals **z + w_out** where **w_out ≤ R**. Threshold **t** is reachable iff **z + w_out ≥ t** for some **0 ≤ w_out ≤ R** — i.e. iff **z + R ≥ t**. The **sub-threshold** class **wt = t−1** is reachable iff **z ≤ t−1** and we can place exactly **t−1−z** ones outside (**0 ≤ t−1−z ≤ R**). **Ambiguity** at a leaf means **both** feasibility regions are non-empty.

2. **Where else this appears.**
   - **Integer knapsack / capacity constraints:** total “weight” is sum of fixed part **z** and variable part on **R** slots, each slot 0 or 1 — feasible intervals for targets **t** and **t−1**.
   - **Partial observability in MDPs:** belief state summarizes which world states remain; **threshold** events are **reachable** from belief iff some completion exists.
   - **Coding:** erasures on **k** positions leave **syndrome** compatible with multiple **Hamming** **weights** unless **R** is too small to flip the count across **t**.

3. **Machinery.** Interval arithmetic on **w_out**; **critical** boundary when **t** exceeds **z + R** (cannot reach quorum) or when **t−1−z > R** (cannot stay at **t−1**).

4. **Transfer seed.** **037** fixed **k ≤ 4** ⇒ **R ≥ 6** ⇒ always both **5−z** and **6−z** fit in **R** for **z ≤ 4**. At **k = 5**, **R = 5**: **6 − z > R** when **z = 0** (**6** ones needed outside, only **5** slots). **Predict:** **only** the **all-zero** pattern on **Q** **(z = 0)** **rules** **out** **wt = 6**; **all** **z ≥ 1** **patterns** **still** **admit** **both** **wt = 5** **and** **wt = 6**.

## Falsifiable claim

Let **n = 10**, **|Q| = 5**, **R = 5**, **z** = ones of **p** on **Q**.

- **A)** **wt = 6** extension exists iff **0 ≤ 6 − z ≤ R** iff **z ≥ 1**.
- **B)** **wt = 5** extension exists for **all** **z ∈ {0,…,5}** (iff **0 ≤ 5 − z ≤ R**).

**Expected:** **PASS** (exhaustive over **C(10,5) × 2^5 = 252 × 32 = 8064** cases).

## Interpretation

Five **distinct** **coordinate** **queries** **can** **information-theoretically** **exclude** **quorum** **only** **if** **the** **revealed** **5**-**tuple** **is** **all** **zeros** **(no** **1** **on** **Q)** — **still** **31/32** **of** **patterns** **per** **Q** **remain** **ambiguous** **between** **wt = 5** **and** **wt = 6**.
