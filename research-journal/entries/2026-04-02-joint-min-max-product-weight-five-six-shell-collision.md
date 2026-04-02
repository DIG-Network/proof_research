# Experiment entry: joint-min-max-product-weight-five-six-shell-collision

**Date:** 2026-04-02  
**Path:** `sub-problems/anonymous-quorum-binding/experiments/joint-min-max-product-weight-five-six-shell-collision/`

## Context

anonymous-quorum-binding — toy shell separation on \(n=10\), \(|S|\in\{5,6\}\), public weights \(w_i=i+1\). Follow-up to **091** \((\min,\max,\sum)\).

## Hypothesis tested

\(K(S)=(\min,\max,\prod)\) over \(S\): whether exact cross-shell keys exist and the smallest \(M\) for \((\min,\max,\prod\bmod M)\) to collide across shells.

## Outcome

**PASS** — **31** exact cross-shell keys; first modular collision at **\(M=2\)** (**15** shared \(K_M\) keys). Sample exact: \((1,7,840)\) for five-set vs six-set.

## Key finding

**Product** replaces **sum** but does **not** separate the two shells: still **many** exact collisions (**31** vs **41** for sum triple). **First collision modulus** remains **2** (parity / even product class), same floor as **091**’s \((\min,\max,\sum\bmod M)\).

## Implications

- **Joint \((\min,\max,\cdot)\)** with either additive or multiplicative third coordinate is **not** a threshold witness on this toy.
- **063**-style **(sum, product)** or richer tuples remain the next binding-summary probes if staying in this track.

## Analogy pass summary

See `hypothesis.md`: order statistics + multiplicative mass vs **091** additive mass; parallel **050** product-mod collapse.

## Space-definition

None.
