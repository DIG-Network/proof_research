# Results

**Overall:** **PASS** (for the intended negative / impossibility-style evidence in the stated naive models)

## Checklist

| Check | Outcome |
|--------|---------|
| Merkle + **per-signer** inclusion material at `t = Θ(n)` | **FAIL** as sublinear: proof size scales as **Θ(t · λ · log n) = Θ(n log n)** in the counting model encoded in `script.py`. |
| BLS-style **linear aggregate** + verifier only has `C`, not `PK_S` | **FAIL** for black-box soundness: correct pairing verification requires the **aggregate public key** (or equivalent) for the **actual** signing set; hiding `S` while keeping `|π| = o(n)` does not admit the obvious Merkle-per-signer fix, and the aggregate itself is not determined by `C` alone. |
| RSA accumulator + **t** separate membership witnesses (naive OR) | **INCONCLUSIVE** as a full impossibility proof, but **FAIL** the sublinear goal under the **naive** “present `t` independent witnesses” pattern: **Ω(t · λ) = Ω(n · λ)** when `t = Θ(n)`. Tighter lower bounds would need a formal theorem. |

## Reasoning

1. **Sublinearity vs. majority quorum:** The main problem requires `|π| = o(n) · λ` with `t = ⌊n/2⌋ + 1`. Any construction that includes **one** authenticated Merkle path (or co-path) **per participating signer** to bind each `pk_i` to `C` incurs at least **t** such paths. For `t ∼ n/2`, that is **Θ(n)** hash outputs (each **Ω(λ)** bits) plus index data — already **linear** in `n`; with depth **⌈log₂ n⌉**, the bound is **Θ(n log n)** bits in the usual Merkle model. So this natural combination **does not** meet **o(n)** (indeed not **O(n)** without compressing multiple paths, which reintroduces heavy machinery).

2. **Anonymity + aggregation:** Standard BLS aggregation identifies verification with **one** pairing equation using **PK_S**. If `S` is hidden and not derivable in **O(1)** space from `C`, the verifier lacks the G₂ element (or appropriate group handle) that the pairing must use. Giving **only** `C` and `σ` does not specify `PK_S` uniquely from partial information without extra proof — and the “extra proof” is exactly where naive solutions blow up to linear or SNARK-sized objects.

3. **RSA / bilinear accumulators:** Single-element accumulators give **O(λ)** witnesses per element, but certifying **“≥ t distinct elements from committed set”** without revealing **which** `t`, using only **standard** disjunctive proof techniques, typically scales at least **linearly in t** for explicit witness OR-composition unless one allows **general ZK** (excluded).

## Script

Run: `python script.py` — exits **0** if toy arithmetic checks pass (demonstrating scaling and aggregate ambiguity in the toy group).
