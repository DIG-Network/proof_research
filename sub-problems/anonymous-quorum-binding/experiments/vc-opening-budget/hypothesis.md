# Hypothesis

**H:** Any **black-box** instantiation of `Link(C, K)` (“`K` is the sum / group-aggregate of **at least** `t` distinct leaves of commitment `C` to vector `(pk_0,…,pk_{n−1}`)”) that follows one of these **documented** patterns requires **verifier-side** resources that scale as **Ω(t)** or **Ω(t log n)** (hash / field / group operations, or proof bits), when the prover must **not** reveal the witness subset `S` in the clear:

1. **Merkle-per-leaf:** one inclusion path (or co-path) per signed index attested.
2. **Sparse Merkle / multiset:** same asymptotic if `t` distinct positions must be authenticated independently.
3. **Single linear opening** (e.g. inner-product / IPA flavor): to bind `K = ⟨w, pk⟩` with **hidden** 0/1 vector `w` of Hamming weight ≥ `t`, standard **non-ZK** IPAs prove **one** inner product against a **known** `w` or committed `w` with structure — hiding `w` while certifying **weight** reintroduces **disjunctive** or **range** style composition (excluded SNARK-like layer).

**Falsifier:** Give operation counts + proof size for a concrete ROM/DL-secure scheme with `t = Θ(n)`, `|π| = o(n)`, verifier `poly(λ, log n)`, no SNARK verifier, that proves `Link` without revealing `S`.

**Scope:** Asymptotic **accounting** in an idealized model, not a new security reduction.
