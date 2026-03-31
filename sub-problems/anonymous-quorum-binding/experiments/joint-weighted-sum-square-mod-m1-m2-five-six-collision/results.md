# Results — `joint-weighted-sum-square-mod-m1-m2-five-six-collision`

**Outcome:** **PASS** (cross-cardinality collision at minimal moduli in lex order)

## Search rule

Lexicographic \((M_1,M_2)\) with \(M_1,M_2 \ge 2\), cap default 60. First pair where some **5-subset** and some **6-subset** of \(\{0,\ldots,9\}\) share
\[
\Bigl(\sum_{i\in S}(i+1) \bmod M_1,\ \sum_{i\in S}(i+1)^2 \bmod M_2\Bigr).
\]

## First collision

| Field | Value |
|-------|--------|
| \(M_1\) | **2** |
| \(M_2\) | **2** |
| Key | **(1, 1)** |
| 5-set (indices 0-based) | (4, 6, 7, 8, 9) |
| Integer \(\sum w_i\) | 39 |
| Integer \(\sum w_i^2\) | 319 |
| 6-set (indices 0-based) | (0, 1, 2, 3, 4, 5) |
| Integer \(\sum w_i\) | 21 |
| Integer \(\sum w_i^2\) | 91 |

All four integers are odd, hence both residues are 1 mod 2.

## Reasoning

**H1:** **Confirmed.** The **first** \((M_1,M_2)\) in lex order is **(2, 2)**.

At **\(M_1=M_2=2\)**, the tag is **(\(\sum w_i \bmod 2\), \(\sum w_i^2 \bmod 2\))**. For integer \(w\), \(w^2 \equiv w \pmod 2\), so **both** coordinates equal **the parity of \(\sum w_i\)** over \(\mathbb{Z}\). The pair is **redundant** — the “2D” summary **collapses** to **one** bit of information, consistent with **034** and **052** at **\(M=2\)**.

## Artifact

`script.py` — exhaustive subset enumeration + double loop on \((M_1,M_2)\).
