# Results — info-theoretic-barrier

**Outcome:** INCONCLUSIVE (with partial supporting evidence)

## Reasoning

1. **Combinatorial scale:** For `n = 64`, strict-majority subsets number ≈ `2^62.9`. A **naive injective** encoding of *which* majority subset signed would need ~63 bits — below a toy “256-bit constant `π`” budget, so **no asymptotic separation at this `n`**. Scaling `n` makes `log2(#majority subsets)` grow as `Θ(n)` (e.g. central binomial coefficient), so for large `n` injective subset indices exceed any `O(λ)`-sized `π`.

2. **Non-injectivity caveat:** Sound threshold verification might not require uniquely identifying `S`. The counting bound therefore does **not** prove impossibility of sound **anonymous** quorum proofs.

3. **Structural check (toy mod-`p` model):** Two disjoint strict-majority index sets yield different “aggregate keys” under additive aggregation, illustrating that **standard linear aggregation ties verification to a specific cosigner set** unless extra binding ties the signature object to the correct set-derived key.

## Scripted output summary

- Merkle root over `n` toy keys: 32-byte digest (`O(λ)` commitment).
- Majority subset count and `log2` reported by `script.py` (run locally).
- Verdict line from script: INCONCLUSIVE for full impossibility.
