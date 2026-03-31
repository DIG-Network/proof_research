# Hypothesis — exact integer quintuple power sums (5-shell vs 6-shell)

## Analogy pass

1. **Abstract structure:** **064** showed the **exact integer** triple **(Σw, Σw², Σw³)** is **injective** on **C(10,5) ∪ C(10,6)** for **w_i=i+1**, while **059–065** showed **modular** projections of the same statistics collapse shells at tiny **M**. We add **p₄, p₅** and ask whether **exact** **5-tuples** still separate **|S|=5** from **|S|=6**.

2. **Analogues (≥3):**
   - **Lossless vs lossy compression:** More **integer** coordinates increase the embedding dimension before any quotient — may restore injectivity if the third coordinate already separated shells.
   - **Moment problem:** Finer truncated moment vector can distinguish measures supported on **5** vs **6** points in toy finite settings.
   - **Hashing vs raw data:** Same as **064** — Merkle-friendly **mod** folding destroys information **064** preserves.

3. **Machinery:** Exact enumeration over **252 + 210** subsets; dictionary keyed by **(p₁,…,p₅)**.

4. **Transfer seed:** If **triple** is injective on the union, **quintuple** **superset** of coordinates is at least as fine — expect **still** **no** cross-shell collision (**hypothesis** **A** **fails**). **Hypothesis** **B** (collision exists) would be surprising.

## Falsifiable claims

**H1 (hypothesis A):** Some **5-set** and **6-set** share **(Σw^k)_{k=1..5}** as **ℤ⁵** (cross-shell collision).

**H2:** **No** such collision; **K** injective on **C(10,5) ∪ C(10,6)** (and likely within each shell).

Script prints **PASS** if **H1** holds, **FAIL** if **H2** holds (same convention as **064**).
