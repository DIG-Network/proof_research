# Hypothesis: joint (min, max, product) on public weights

## Analogy pass

1. **Abstract structure:** Map each subset \(S\) of validators (indices) to a small tuple of summaries of public scalars \(w_i\). Ask whether the tuple’s value classifies \(|S|=t-1\) vs \(|S|=t\) (here \(t=6\), \(n=10\)).

2. **Where else:** (i) Moment fingerprints in statistics — low-order summaries often collide across sample sizes. (ii) Order statistics \((\min,\max)\) plus a third statistic — sufficient statistics for some families but not for arbitrary finite sets. (iii) Multiplicative invariants in number theory — products carry prime factorization information but mod \(M\) folds like additive moments (see 050, 063).

3. **Machinery in those domains:** Method of moments / cumulants; order-statistic theory; Chinese remainder and modular projection.

4. **Transfer seed:** Entry **091** showed \((\min,\max,\sum)\) has many exact cross-shell collisions on \(w_i=i+1\). Replacing **sum** by **product** is a non-additive encoding change (parallel **050** product-mod theme) while keeping the same **min/max** anchors — test whether **multiplicative mass** restores separation on \(C(10,5)\cup C(10,6)\) or still admits cross-shell keys, and how small **\(M\)** is for \((\min,\max,\prod\bmod M)\).

## Falsifiable claim

- **H1:** There exists at least one key in \(\mathbb{Z}^3\) shared by some 5-set and some 6-set for \(K(S)=(\min_{i\in S} w_i,\max_{i\in S} w_i,\prod_{i\in S} w_i)\) with \(w_i=i+1\).

- **H2:** If **H1** holds, the smallest **\(M\ge 2\)** with a cross-shell collision for \((\min,\max,\prod\bmod M)\) is **strictly larger** than for the sum triple (091 gave **\(M=2\)** for \((\min,\max,\sum\bmod M)\)).

## Outcome interpretation

- Many exact cross-shell keys ⇒ **PASS** on **H1**; compare **first_mod_collision** to 091.
- No exact cross-shell ⇒ **FAIL** on **H1** (injective joint on the two shells for this toy).
