# 2026-03-30 — polynomial-three-eval-binary-collision

**Experiment path:** `sub-problems/anonymous-quorum-binding/experiments/polynomial-three-eval-binary-collision/`

**Context:** `anonymous-quorum-binding`

**Hypothesis (summary):** For nodes `0..n-1` and three query points `r1,r2,r3` in `𝔽_p`, when `2^n > p^3` there exist **distinct** binary leaf vectors `v ≠ w` with identical `(P(r1), P(r2), P(r3))` for their degree-`(n-1)` Lagrange interpolants.

**Outcome:** **PASS**

**Key finding:** At `p=97`, `n=20`, `r1=90`, `r2=91`, `r3=92`, brute-force bucketing finds collision at triple `(47,73,95)` with **Hamming distance 8**. **Three** RS-style openings still fail to injectively encode arbitrary **0/1** participation — extends **022** and **024**.

**Implications:**

- Constant **k** evaluation openings cannot bind **all** binary patterns once **2^n > p^k**; **k** must grow with **n** (or the committed object must shrink / gain structure).
- Aligns digest thread: **image size ≤ p^k** vs hypercube **2^n**.

**Analogy pass summary:** **Linear sketches**, **RS evaluation codomain size**, **pigeonhole / hashing** — seed: **p^k** bucket count vs **2^n** domain.
