# Analogy pass (mandatory)

## 1. Abstract structure

We want a verifier that observes only **low-dimensional summaries** (outputs of a **fixed** family of “probes”) of a hidden **n-bit** participation pattern, and from those summaries must separate the predicate “**at least a strict majority** participated” from patterns **below** threshold.

Stripped of cryptography: **distinguish** two hidden binary vectors using only **linear** measurements over **F₂** (parity / XOR pooling), where the measurement family is chosen **independently** of the hidden vectors (non-adaptive).

## 2. Where else this structure appears

1. **Combinatorial group testing / syndrome pooling** — each test returns a **Boolean function** of many items’ states; threshold “**≥ k** defectives” vs “**< k**” is a global **Hamming-weight** property.
2. **Linear error-correcting codes** — parity checks **annihilate** certain error vectors; syndromes coincide for **different** error patterns lying in the same coset of the dual.
3. **Compressed sensing / sketching (linear, but usually ℝ)** — distinct sparse signals can share the same **measurement** vector unless the sketch is **injective** on the signal class; here the “signals” are participation patterns and the class is **discrete** `{0,1}ⁿ`.
4. **Two-sample tests in statistics** — deciding a property of a **high-dimensional** latent state from **few** summary statistics; insufficient summaries yield **non-identifiability**.

## 3. Machinery in those domains

- **Group testing:** adaptive / non-adaptive test matrices; disjunct / separable designs for **definite** subsets — **not** automatically tuned for **majority** vs **minority** separation with **o(n)** tests.
- **Coding:** choose parity-check rows **orthogonal** to a fixed difference vector **d** so two codewords + **d** share the same syndrome.
- **Sketching:** need **restricted isometry** / uniqueness on the family of interest; without it, **collisions** are generic in linear maps when **rank < n**.

## 4. Transfer seed

If participation patterns **x** (majority) and **y** (minority) differ by **d = x ⊕ y**, then **every** linear probe **r** with **r·d = 0** (F₂ dot product) returns the same bit on **x** and **y**. The space of such **r** has dimension **n−1** for **d ≠ 0**, so one can pack **n−1** **independent** linear measurements that are **identical** on **both** patterns — a concrete **ambiguity** for “**parity-pool only**” verifiers.

---

# Formal hypothesis

**H:** For **n = 8**, **t = 5**, there exist binary patterns **x, y ∈ {0,1}ⁿ** with **wt(x) ≥ t** and **wt(y) < t** and **x ≠ y** such that **d = x ⊕ y** is nonzero, and there exists a family of **m = n − 1** linear functionals **r₁,…,r_m** (each **r_j ∈ {0,1}ⁿ**) that are **linearly independent** over **F₂** and satisfy **r_j·x = r_j·y** for every **j**.

**Interpretation (toy):** A verifier whose entire view is **only** these **m** parity pools cannot distinguish this **honest-majority** world from the **under-threshold** world, even though **m** is large — because the measurement family was **aligned to annihilate** the **difference** between the two worlds.

**Falsification:** No such **(x, y, {r_j})** exists for the searched instance, or independence check fails.

---

# Outcome (filled after run)

**PASS** — see `results.md`.
