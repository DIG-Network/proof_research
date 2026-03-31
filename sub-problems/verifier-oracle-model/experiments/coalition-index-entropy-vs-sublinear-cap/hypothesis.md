# Hypothesis

**H1 (counting, injective witness):** If — in an idealized model — the verifier must recover **which** minimal quorum coalition \(S\) of size exactly \(t=\lfloor n/2\rfloor+1\) signed (injective encoding of one of \(\binom{n}{t}\) possibilities), then any one-shot proof must carry at least \(\lceil \log_2 \binom{n}{t} \rceil\) bits of information in the worst case.

**H2 (numerical vs stylized cap):** Using the same stylized “generous sublinear” bit cap as Entry **012**, \(B(n) = \lambda (\log_2 n)^2\) with \(\lambda=256\), the quantity \(\log_2 \binom{n}{t}\) **eventually exceeds** \(B(n)\) at feasible \(n\) (computed via \(\sum_i \log_2\frac{n-t+i}{i}\) without forming \(\binom{n}{t}\) explicitly).

**Non-claim:** This does **not** prove a lower bound for the **anonymous** main goal (journal **006**): many coalitions may map to the same aggregate or transcript. The experiment **documents tension** between “lossless coalition indexing” and polylog \(|\pi|\) caps.

**Falsification:** For all tested \(n\), \(\log_2 \binom{n}{t} \leq B(n)\), or the numeric method is inconsistent.
