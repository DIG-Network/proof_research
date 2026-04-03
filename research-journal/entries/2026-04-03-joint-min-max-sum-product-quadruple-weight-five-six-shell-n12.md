# Experiment entry — 2026-04-03 — joint-min-max-sum-product-quadruple-weight-five-six-shell-n12

**Path:** `sub-problems/anonymous-quorum-binding/experiments/joint-min-max-sum-product-quadruple-weight-five-six-shell-n12`

**Context:** anonymous-quorum-binding (toy shell-separation / aggregate-tag track)

**Hypothesis tested:** With `n=12`, `w_i=i+1`, shells `|S|∈{5,6}`, does the exact quadruple `K=(min,max,Σ,Π)` admit a **5-vs-6** key collision?

**Outcome:** **PASS** (hypothesis **confirmed** — collisions exist)

**Key finding:** `cross_shell_exact=2`. Witnesses share the pattern **5-set** `{1,5,6,8,m}` vs **6-set** `{1,2,3,4,10,m}` for **`m∈{11,12}`**, giving **`Π=240m`** and matching **`(min,max,Σ)`** on both sides. At **`n=10`** (**093**), this family cannot occur; injectivity of **`K`** on **`C(10,5)∪C(10,6)`** does **not** extend to **`n=12`**.

**Implications:**

- Exact **093**-style quadruples are **not** a monotone-in-**`n`** separator for adjacent shells with fixed **`w_i=i+1`**.
- **095** (modular fold at **`n=12`**) sits in the same **`n`** regime where **exact** cross-shell merges already exist (here, without any modulus).

**Analogy pass summary:** Same as parent **093**: sufficient-statistic injectivity on growing sample spaces; here the larger universe enables a **closed-form** two-shell identity.

**Space definition:** none
