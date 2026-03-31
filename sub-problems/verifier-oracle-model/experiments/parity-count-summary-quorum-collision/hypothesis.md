# Analogy pass (mandatory)

## 1. Abstract structure

The verifier receives a **scalar summary** **h(k)** of an unknown **integer** **k** (e.g. the number of participating validators), and must decide a **threshold predicate** **k ≥ t**. This is the same abstract shape as **lossy quantization** of a sufficient statistic: **full** **k** determines any threshold rule, but **composed** summaries **h** may **collapse** values that lie on opposite sides of **t**.

## 2. Where else this structure appears

1. **Statistical hypothesis testing** — test based on **binned** counts or **rounded** statistics; **coarse** bins destroy **power** for **local** alternatives near the threshold.
2. **Digital communication / A/D conversion** — **quantization** maps many inputs to one output; **threshold crossing** information is lost unless resolution is fine enough.
3. **Database / OLAP rollups** — **histogram** buckets hide whether a count is just above or below a policy cutoff.
4. **Modular arithmetic summaries** — **k mod m** is a **homomorphism** that identifies **k** and **k+ℓm**; choosing **m** creates **aliasing** between sub-threshold and super-threshold counts.

## 3. Machinery in those domains

- **Sufficiency / Neyman–Pearson:** the **full count** is sufficient for **Bernoulli** **n**-sample size; **non-injective** **h(k)** throws away information needed at the **boundary** **k = t**.
- **Signal processing:** **Nyquist** / resolution arguments — **one** low-resolution bit can agree on unequal inputs straddling a decision boundary.
- **Number theory:** **k₁ ≡ k₂ (mod m)** defines residue classes; **threshold** cuts across classes when **m** shares structure with **t**.

## 4. Transfer seed

**Parity** **h(k) = k mod 2** collides on **k = 4** and **k = 6**, while for **n = 10**, **t = 6** we have **4 < t** (strict under-quorum for “**≥ 6** of **10**”) and **6 ≥ t** (at threshold). Same **1-bit** summary — opposite **quorum** truth values.

---

# Formal hypothesis

**H:** Let **n = 10**, **t = ⌊n/2⌋ + 1 = 6**. Define **h(k) = k mod 2**. Then **h(4) = h(6)** but **(4 ≥ t)** is false and **(6 ≥ t)** is true. Hence **no** decision rule **ψ: {0,1} → {accept, reject}** can equal **𝟙_{k ≥ t}** for all **k** when the verifier **only** observes **h(k)**.

**Falsification:** **h(4) ≠ h(6)** or **t** miscomputed.

**Outcome (after run):** **PASS** — see `results.md`.
