# 2026-03-30 — `joint-weighted-sum-square-mod-m1-m2-five-six-collision`

**Context:** `sub-problems/anonymous-quorum-binding`  
**Experiment:** `sub-problems/anonymous-quorum-binding/experiments/joint-weighted-sum-square-mod-m1-m2-five-six-collision/`

## Hypothesis tested

For \(n=10\), \(w_i=i+1\), some 5-subset and 6-subset share \((\sum w_i \bmod M_1,\ \sum w_i^2 \bmod M_2)\) for small \((M_1,M_2)\) in lex order.

## Outcome

**PASS**

## Key finding

First collision at **(2, 2)** with key **(1, 1)**. Witness: 5-set indices (4,6,7,8,9) vs 6-set (0,1,2,3,4,5); sums 39 vs 21, sum-squares 319 vs 91 — all odd, so both residues are 1 mod 2. At mod 2, \(w^2\equiv w\), so the two coordinates are **redundant** (parity twice).

## Implications

Joint **(mod 2, mod 2)** is not a stronger fold than single mod 2 for this weight choice; **non-redundant** 2D modular tests need coprime/odd moduli or other structure (see experiment `notes.md`).

## Analogy pass summary

**Domains:** sufficient-statistic identifiability; CRT / simultaneous congruences; syndrome pairs. **Seed:** stack linear + quadratic power sums with two moduli after **034/052** single-mod collisions.
