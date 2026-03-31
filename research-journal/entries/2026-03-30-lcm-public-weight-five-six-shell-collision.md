# Entry — 2026-03-30 — `lcm-public-weight-five-six-shell-collision`

**Experiment path:** `sub-problems/anonymous-quorum-binding/experiments/lcm-public-weight-five-six-shell-collision/`

**Context:** `anonymous-quorum-binding` (public summary / `Link` toy)

**Hypothesis tested:** On `n=10`, `w_i=i+1`, shells `|S|∈{5,6}`, the join-side summary `h_lcm(S)=lcm_{i∈S} w_i` and joint `(h_lcm, Σw)` admit cross-shell collisions (same key on a 5-set and a 6-set).

**Outcome:** PASS

**Key finding:** `h_lcm` has **23** distinct values on the 6-shell and **all 23** appear on the 5-shell (**30** distinct values there). Joint `(lcm, sum)` has **80** cross-shell colliding keys (sample `(60,25)`). Dualizing **089** gcd/meet to lcm/join does not recover threshold separation; joint ambiguity is **worse** than `(gcd,Σw)`’s **20** collisions.

**Implications:**

- Permutation-invariant **divisibility-lattice** meet/join statistics on fixed public weights are not promising standalone quorum certificates on this toy.
- Next work should shift away from scalar symmetric summaries unless combined with a new binding path to `C` or a non-anonymous ordered structure.

**Analogy pass summary:** Divisibility lattice (join vs meet), order-theoretic duality, prior **089** gcd branch — **lcm** chosen as the dual encoding test.

**Invented space:** none (`space-definition.md` not used).
