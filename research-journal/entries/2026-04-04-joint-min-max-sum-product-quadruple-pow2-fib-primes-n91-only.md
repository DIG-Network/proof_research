# Experiment entry — 2026-04-04 — joint-min-max-sum-product-quadruple-pow2-fib-primes-n91-only

**Date:** 2026-04-04  
**Experiment path:** `sub-problems/anonymous-quorum-binding/experiments/joint-min-max-sum-product-quadruple-pow2-fib-primes-n91-only`  
**Context:** anonymous-quorum-binding (entry **135**)

## Hypothesis tested

For at least one of `pow2_2^i`, Fibonacci prefix, first-`n` primes, there exists a **5-vs-6** cross-shell collision on exact `K=(min w, max w, Σ w, Π w)` at **`n=91`**.

## Outcome

**FAIL** — no schedule collides at `n=91`.

## Key finding

Exhaustive scan per schedule (~3.85 h wall, SQLite-backed 5-key table ~6.9 GiB peak): **pow2**, **Fibonacci**, **first-n primes** all **NO_COLLISION** at `n=91`. With **101–134**, **no** collision for **`n ∈ [11,91]`** on these three schedules under exact **`K`**.

## Implications

- Same structured-schedule / exact-quadruple line remains collision-free one step further; **`n=92`** is the next single-`n` probe (higher cost).
- For large `n`, **disk-backed** key stores are required; bigint **`K`** fields must not be forced into SQLite `INTEGER`.

## Analogy pass summary

Same as **134**: fingerprint / sufficient-statistic collapse; collision search as stress test of coarse public summaries for threshold binding.

## Space definition

None.
