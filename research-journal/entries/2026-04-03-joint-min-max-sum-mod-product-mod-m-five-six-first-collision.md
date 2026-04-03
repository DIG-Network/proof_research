# Experiment entry: joint-min-max-sum-mod-product-mod-m-five-six-first-collision

**Date:** 2026-04-03  
**Path:** `sub-problems/anonymous-quorum-binding/experiments/joint-min-max-sum-mod-product-mod-m-five-six-first-collision/`

## Context

anonymous-quorum-binding — follow-up to **093** (exact \((\min,\max,\sum,\prod)\) injective on \(|S|\in\{5,6\}\), \(n=10\), \(w_i=i+1\)). Tests the **first** modulus \(M\) for cross-shell collision under  
\(K_M=(\min,\max,\sum\bmod M,\prod\bmod M)\).

## Hypothesis tested

**H:** The smallest \(M\ge 2\) with a 5-vs-6 collision is **\(M=2\)**.

## Outcome

**PASS** (hypothesis confirmed): **first_collision_M = 2**, witness  
\(K_2=(1,6,1,0)\): 5-set indices `(0,1,2,4,5)` vs 6-set `(0,1,2,3,4,5)`.

## Key finding

Exact **093** quadruple separation is **not** preserved by folding **both** \(\sum\) and \(\prod\) mod \(M\): parity already identifies a 5-set and a 6-set at **\(M=2\)**, the same floor as **091**/**092** when only one of \(\sum\) or \(\prod\) was folded.

## Implications

- Modular **coarsening** of mass coordinates alongside exact extrema still hits **minimal** 2-adic collapse in this toy.
- Any **threshold witness** using this tuple mod small \(M\) needs extra **Link** / commitment structure.

## Analogy pass summary

See `hypothesis.md`: first-collision scan over modulus (quantization / truncation analogy).

## Space-definition

None.
