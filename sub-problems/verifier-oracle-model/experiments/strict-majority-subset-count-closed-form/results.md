# Results

| Field | Value |
|-------|--------|
| **Outcome** | **PASS** |
| **Nature** | Combinatorial identities + witness-size **counting** commentary (not cryptography). |

## Verified identities

For \(t = \lfloor n/2 \rfloor + 1\) and \(N(n) = \sum_{k=t}^{n} \binom{n}{k}\):

| Parity | Closed form |
|--------|-------------|
| **Odd** \(n\) | \(N(n) = 2^{n-1}\) |
| **Even** \(n\) | \(N(n) = \bigl(2^n - \binom{n}{n/2}\bigr) / 2\) |

Brute force for **\(n = 1..25\)** matches the closed form for every **\(n\)**.

## Witness-size corollary (uniform model)

- For **odd** \(n\), \(\log_2 N(n) = n - 1\) **exactly** — lossless labeling of **which** strict-majority subset (among **all** such subsets) needs **\(n-1\)** bits in the uniform counting model.
- Compared to **Entry 015**, which tracked \(\log_2 \binom{n}{t}\) for **minimal** size \(|S| = t\), here \(N(n)\) counts **every** majority cardinality \(k \ge t\), giving a **canonical** odd-\(n\) closed form.

## Relation to stylized \(B(n) = 256 (\log_2 n)^2\)

At **\(n = 128\)**, \(\log_2 N(n) \approx 126.9\) is still **below** \(B(128) = 12544\) — crossover to \(\log_2 N > B(n)\) occurs at much larger **\(n\)** (same asymptotic story as **015**: \(\Theta(n)\) vs polylog).
