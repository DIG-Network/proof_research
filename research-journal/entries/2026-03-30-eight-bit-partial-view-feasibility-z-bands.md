# Entry — 2026-03-30 — eight-bit-partial-view-feasibility-z-bands

- **Date:** 2026-03-30
- **Experiment:** `sub-problems/verifier-oracle-model/experiments/eight-bit-partial-view-feasibility-z-bands/`
- **Context:** `verifier-oracle-model`

## Hypothesis tested

**n = 10**, **|Q| = 8**, **R = 2:** **z ∈ {0,1,2,7,8}** **neither;** **z=3** **only_wt5;** **z ∈ {4,5}** **both;** **z=6** **only_wt6;** **11520** **exhaustive** **pairs.**

## Outcome

**PASS** — **5670** **/** **2520** **/** **1260** **/** **2070.**

## Key finding

**“Both”** **share** **of** **patterns** **per** **Q** **drops** **below** **50%** **(126/256** **≈** **49.2%)** **for** **the** **first** **time** **in** **the** **series;** **neither** **grows** **to** **46/256** **≈** **18%.**

## Implications

- **Optional** **042:** **k=9,** **R=1** **(both** **only** **at** **z=5).**
- **Series** **ready** **to** **summarize** **in** **a** **single** **(n,t,k)** **lemma** **for** **digest** **or** **sub-problem** **note.**

## Analogy pass summary

**Interval** **intersection** **/** **slack** **capacity** **—** **same** **as** **038–040,** **compressed** **R.**
