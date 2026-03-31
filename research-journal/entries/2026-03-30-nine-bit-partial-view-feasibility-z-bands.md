# Entry — 2026-03-30 — nine-bit-partial-view-feasibility-z-bands

- **Date:** 2026-03-30
- **Experiment:** `sub-problems/verifier-oracle-model/experiments/nine-bit-partial-view-feasibility-z-bands/`
- **Context:** `verifier-oracle-model`

## Hypothesis tested

**n = 10**, **|Q| = 9**, **R = 1:** **z**-**bands** **neither** **on** **{0..3,7..9},** **only_wt5** **at** **z=4,** **both** **only** **at** **z=5,** **only_wt6** **at** **z=6;** **5120** **exhaustive** **pairs.**

## Outcome

**PASS** — **1260** **/** **1260** **/** **840** **/** **1760.**

## Key finding

**R = 1** **collapses** **“both”** **to** **a** **single** **Hamming** **layer** **z = 5** **(126** **masks** **per** **Q).** **Ambiguous** **fraction** **126/512** **≈** **24.6%,** **down** **from** **~49%** **at** **k=8.**

## Implications

- **Coordinate** **probe** **series** **for** **(10,6)** **is** **complete** **up** **to** **k=9;** **k=10** **is** **degenerate** **(full** **wt** **known).**
- **Digest** **can** **reference** **closed** **z-interval** **lemma** **from** **experiment** **notes.**

## Analogy pass summary

**Single-bit** **slack** **between** **adjacent** **thresholds** **—** **overlap** **at** **exactly** **one** **discrete** **z.**
