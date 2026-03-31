# Analogy pass (mandatory)

## 1. Abstract structure

The validator set can be **encoded** as **n** values **(v₀,…,v_{n−1})** sitting on **n** distinct domain points, with a unique interpolating polynomial **P** of degree **< n** over a field. A natural “**compact**” handle is **one** field element **P(r)** at a **public** query point **r** (the algebraic analogue of a **single** codeword symbol / **one** evaluation opening).

The question is whether **that single number** **determines** (or even **soundly certifies**) **global** combinatorial facts about **which** positions participate in a threshold event — analogous to asking whether **one** RS symbol fixes the entire message.

## 2. Where else this structure appears

1. **Reed–Solomon / algebraic geometry codes** — a codeword is evaluations of a **low-degree** polynomial; **one** coordinate is consistent with **many** messages until **distance** / **redundancy** is spent.
2. **Polynomial commitment (Merkle of evaluations)** — opening **one** point proves **consistency** with **some** committed polynomial, not **which** of many possible witness polynomials if the commitment is **underdetermined** by one opening.
3. **Oversampled compressed sensing (finite field flavour)** — **one** linear measurement **Σ c_i v_i** leaves a **large** affine solution space for **v** unless further structure is imposed.
4. **Design of experiments** — **one** response measurement cannot identify a **high-dimensional** parameter vector without **identifiability** conditions.

## 3. Machinery in those domains

- **RS decoding:** need **≥ t** evaluations (or **syndromes**) for unique recovery depending on degree and errors; **one** evaluation is **never** injective on messages of dimension **> 1**.
- **PCS:** multi-openings + **binding** commitment tie the prover to **one** polynomial; **without** binding, **many** polynomials share a point value.
- **Linear algebra:** fixing **P(r) = c** imposes **one** linear constraint on the **n** coefficients / **n** point values — **nullity** typically **n−1**.

## 4. Transfer seed

**One** evaluation constraint **P(r) = c** has a **huge** affine family of assignment vectors **w** that match **c** but differ from a reference **v**. This is the finite-field analogue of “**single-symbol ambiguity**” and cautions against expecting **threshold** or **set** knowledge from **one** algebraic probe alone.

---

# Formal hypothesis

**H:** Fix prime **p**, **n = 8**, domain points **x_i = i** for **i = 0,…,n−1**, and a query **r ∈ 𝔽_p** not equal to any **x_i**. Let **L_i(r)** be Lagrange basis values at **r**. For a concrete **v ∈ 𝔽_p^n**, let **c = Σ_i v_i L_i(r)**. Then there exists **w ∈ 𝔽_p^n** with **w ≠ v** such that **Σ_i w_i L_i(r) = c** (same single evaluation).

**Falsification:** No such **w** found for the constructed instance, or the evaluation identity fails.

**Outcome (after run):** **PASS** — see `results.md`.
