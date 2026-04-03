# Experiment entry: joint-min-max-sum-mod-product-mod-m-five-six-first-collision-n12

**Date:** 2026-04-03  
**Path:** `sub-problems/anonymous-quorum-binding/experiments/joint-min-max-sum-mod-product-mod-m-five-six-first-collision-n12/`

## Context

anonymous-quorum-binding — extension of **094** (`n=10`, same `K_M`) to **`n=12`**, **`w_i=i+1`**, shells **|S|∈{5,6}**.

## Hypothesis tested

**H:** The smallest \(M\ge 2\) with a 5-vs-6 collision for  
\(K_M=(\min,\max,\sum\bmod M,\prod\bmod M)\) is **\(M=2\)**.

## Outcome

**PASS**: **first_collision_M = 2**, witness **\(K_2=(1,6,1,0)\)** — 5-set indices `(0,1,2,4,5)` vs 6-set `(0,1,2,3,4,5)` (same witness pattern as **094** on the shared prefix).

## Key finding

Larger validator universe **`n=12`** does **not** push the first modular cross-shell collision above **2** for this joint tag; the witness lives in the first six weights.

## Implications

- **M=2** floor for this tuple appears **stable** under adding higher-index validators in this linear-weight toy.
- Separation would require a **different** statistic or **Link** structure, not merely more signers.

## Analogy pass summary

See `hypothesis.md`: first-hit modulus scan / coarse-graining.

## Space-definition

None.
