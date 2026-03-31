# Hypothesis

Let \(t = \lfloor n/2 \rfloor + 1\) and \(N(n) = \sum_{k=t}^{n} \binom{n}{k}\), the number of **strict-majority** subsets of \([n]\).

**H1:** For **odd** \(n\), \(N(n) = 2^{n-1}\).

**H2:** For **even** \(n\), \(N(n) = \bigl(2^n - \binom{n}{n/2}\bigr) / 2\).

**H3 (witness-size corollary, counting only):** Under a uniform “which strict-majority coalition” model, lossless identification needs \(\lceil \log_2 N(n) \rceil\) bits; for odd \(n\) this is exactly **\(n-1\)** — **linear** in \(n\), same asymptotic order as **Entry 015**’s \(\log_2 \binom{n}{t}\) story but a **cleaner** closed form for the **full** majority family.

**Non-claim:** Not a cryptographic lower bound on \(|\pi|\) for anonymous proofs (**006**).

**Falsification:** Brute counts disagree with the closed forms for any tested \(n\).
