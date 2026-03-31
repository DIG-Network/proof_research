# Results

| Field | Value |
|-------|--------|
| **Outcome** | **PASS** |
| **Nature** | Combinatorial / information-theoretic comparison only (not a cryptographic theorem for anonymous proofs). |

## Measured relationship

- \(t = \lfloor n/2 \rfloor + 1\), \(\log_2 \binom{n}{t}\) computed via \(\sum_{i=1}^{t} \log_2\frac{n-t+i}{i}\).
- Stylized cap: \(B(n) = 256 \cdot (\log_2 n)^2\) (same family as Entry **012**).

**Crossover in the scripted table:** first \(n\) with \(\log_2 \binom{n}{t} > B(n)\) is **\(n = 131072\)** (at \(n = 65536\), ratio \(\approx 0.9999\), still slightly below).

## Interpretation

- Any verifier model that **requires lossless identification** of which minimal majority coalition signed needs \(\Omega(n)\) bits in this counting sense at scale; that budget **dominates** the polylog \(B(n)\) toy cap for large enough \(n\).
- The **main** anonymous threshold goal does **not** assert such injective identification (**journal 006**); this experiment only sharpens **when** a naive “index the coalition” story collides with sublinear \(|\pi|\) aspirations.
