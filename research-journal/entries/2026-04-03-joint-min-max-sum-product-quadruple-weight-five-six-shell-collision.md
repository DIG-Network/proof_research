# Experiment entry: joint-min-max-sum-product-quadruple-weight-five-six-shell-collision

**Date:** 2026-04-03  
**Path:** `sub-problems/anonymous-quorum-binding/experiments/joint-min-max-sum-product-quadruple-weight-five-six-shell-collision/`

## Context

anonymous-quorum-binding — toy shell separation on \(n=10\), \(|S|\in\{5,6\}\), public weights \(w_i=i+1\). Follow-up stacking **091** \((\min,\max,\sum)\), **092** \((\min,\max,\prod)\), and **063** \((\sum,\prod)\).

## Hypothesis tested

Whether the exact integer quadruple \(K(S)=(\min,\max,\sum,\prod)\) admits any **5-vs-6** key collision across shells.

## Outcome

**FAIL** (hypothesis falsified): **no** cross-shell collisions. Counts: **252** distinct keys on \(|S|=5\) (full **C(10,5)**), **210** on \(|S|=6\) (**C(10,6)**), **0** intersection — **injective** on the union of the two shells.

## Key finding

**Extrema + both masses** separate the adjacent shells in this toy, even though **063** showed \((\sum,\prod)\) alone has cross-shell collisions and **091**/**092** showed \((\min,\max,\cdot)\) with a **single** third statistic still collides. The separation is **not** monotonic in “number of coordinates” alone; the **specific** pairing matters.

## Implications

- Richer **public-weight summaries** can recover shell information **without** SNARKs in toy settings, but **compact commitment / Link(C,K)** and **large-n** behavior remain open.
- **Modular** or **fixed-width** encodings of the same tuple likely reintroduce small-\(M\) collapse (not tested here).

## Analogy pass summary

See `hypothesis.md`: sufficient-statistic injectivity vs explicit witness pairs.

## Space-definition

None.
