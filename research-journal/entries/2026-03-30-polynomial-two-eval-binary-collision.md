# 2026-03-30 — polynomial-two-eval-binary-collision

**Experiment path:** `sub-problems/anonymous-quorum-binding/experiments/polynomial-two-eval-binary-collision/`

**Context:** `anonymous-quorum-binding`

**Hypothesis (summary):** For nodes `0..n-1` and two query points `r1,r2` in `𝔽_p`, when `2^n > p^2` there exist **distinct** binary leaf vectors `v ≠ w` with identical `(P(r1), P(r2))` for their degree-`(n-1)` Lagrange interpolants.

**Outcome:** **PASS**

**Key finding:** Brute force at `p=97`, `n=16`, `r1=90`, `r2=91` finds a collision `(P(r1),P(r2))=(18,41)` at Hamming distance `6`. **Two** polynomial openings still fail to **injectively** encode an arbitrary `0/1` participation vector — a **hypercube**-restricted extension of **022**.

**Implications:**

- Any “two evaluation openings bind the quorum pattern” story must add hypotheses (e.g. **many** points, **PCS**, **Merkle** on coefficients, or a **non-linear** predicate), not just **two** RS-style probes.
- Digest: add row + thread note on **k-point** vs **p^k** pigeonhole for binary patterns.

**Analogy pass summary:** **Linear sketching / compressed sensing**, **ECC syndromes**, **birthday/pigeonhole** — seed: **codomain** `p^k` vs **2^n** binary inputs.
