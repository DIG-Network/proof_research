# Hypothesis: first modular fold of the 093 quadruple

## Context

Experiment **093** (`joint-min-max-sum-product-quadruple-weight-five-six-shell-collision`) showed that for `n=10`, public weights `w_i=i+1`, shells `|S|∈{5,6}`, the **exact** joint statistic

`K(S) = (min w, max w, Σ w, Π w) ∈ Z^4`

is **injective** on `C(10,5) ∪ C(10,6)` (no 5-vs-6 key collision).

Earlier **091** / **092** showed that folding **only** `Σ` or **only** `Π` mod `M` while keeping exact `(min,max)` still yields first cross-shell collision already at **`M=2`** for those **triple** tags.

## Analogy pass (mandatory)

1. **Abstract structure:** A discrete labeling map from a union of two fixed-size shells into a finite key space; **exact** labels are injective; **coarse** labels (quotient by a modulus) may glue distinct exact keys. The question is the **first** modulus where gluing merges across shells.

2. **Analogous domains:** (i) **Hash length / security parameter** — when does truncation first create a birthday collision across structured domains? (ii) **Quantization** — when does rounding first merge two distinct signals? (iii) **Modular arithmetic in coding** — when does reduction mod `M` first identify distinct residue-class representatives?

3. **Machinery there:** First-collision scans over `M`, rate–distortion thresholds, Chinese remainder / modulus ladders.

4. **Transfer candidate:** **Lexicographic scan on `M≥2`** for the joint fold  
   `K_M = (min, max, Σ mod M, Π mod M)`  
   and report the **smallest** `M` with a **5-vs-6** key collision (same `K_M` for some 5-set and some 6-set).

## Falsifiable claim

**H:** The smallest integer `M≥2` for which there exist a 5-subset and a 6-subset of `{0,…,9}` with identical `K_M` is **`M=2`**.

If the scan finds first collision at `M>2`, **H** is **FAIL** (falsified). If first collision is `M=2`, **H** is **PASS** (confirmed).

## Parent

Extends **093** (exact quadruple injective); compares to **091** / **092** (single-fold triples).
