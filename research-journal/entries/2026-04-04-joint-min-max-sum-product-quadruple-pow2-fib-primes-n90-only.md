# Experiment entry — 2026-04-04 — joint-min-max-sum-product-quadruple-pow2-fib-primes-n90-only

**Date:** 2026-04-04  
**Experiment path:** `sub-problems/anonymous-quorum-binding/experiments/joint-min-max-sum-product-quadruple-pow2-fib-primes-n90-only`  
**Context:** anonymous-quorum-binding (entry **134**)

## Hypothesis tested

For at least one of `pow2_2^i`, Fibonacci prefix, first-`n` primes, there exists a **5-vs-6** cross-shell collision on exact `K=(min w, max w, Σ w, Π w)` at **`n=90`**.

## Outcome

**FAIL** — no schedule collides at `n=90`.

## Key finding

Exhaustive scan per schedule (~35.4 min wall): **pow2**, **Fibonacci**, **first-n primes** all **NO_COLLISION** at `n=90`. With **101–133**, **no** collision for **`n ∈ [11,90]`** on these three schedules under exact **`K`**.

## Implications

- Continues strong empirical evidence that this **exact quadruple** stays **shell-injective** on these structured weight lists farther than small-`n` scans suggested.
- Next minimal step in this thread: single-`n` probe **`n=91`** (cost scales with `C(n,6)`).

## Analogy pass summary

Same as **133**: fingerprint / sufficient-statistic collapse; collision search as stress test of coarse public summaries for threshold binding.

## Space definition

None.
