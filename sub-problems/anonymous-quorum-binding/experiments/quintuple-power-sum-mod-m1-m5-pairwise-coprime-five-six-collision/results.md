# Results — quintuple power sums mod five pairwise-coprime moduli

**Outcome:** PASS

**Setup:** `w_i = i+1`, `n=10`, `|S| ∈ {5,6}`. Lex-first **(M₁,…,M₅)** with `M_i ∈ [2,18]` and **pairwise gcd = 1**. Tag **K(S) = (p₁ mod M₁, …, p₅ mod M₅)**. First **5-set vs 6-set** key collision.

**Finding:**

- **FIRST_COLLISION** at **(M₁,…,M₅) = (2, 3, 5, 7, 13)** with **mod key (1, 1, 4, 4, 5)**.
- **5-set** indices **(0,1,2,6,9)** → weights **(1,2,3,7,10)**, **penta** **(23, 163, 1379, 12499, 117083)**.
- **6-set** indices **(0,1,2,4,5,7)** → weights **(1,2,3,5,6,8)**, **penta** **(25, 139, 889, 6115, 43945)**.

**Contrast with naive expectation:** **(2,3,5,7,11)** is pairwise coprime and **lex** **before** **(2,3,5,7,13)** — script’s first hit at **M₅=13** means **no** cross-shell collision at **(2,3,5,7,11)** in this scan (the **fifth** residue mod **11** still **separated** these shells at that tuple).

**vs Entry 059:** Triple lex-first was **(2,3,5)**. Adding **M₄=7** and scanning **M₅** delays first collision to **M₅=13** (still small, not a large “safe” modulus).
