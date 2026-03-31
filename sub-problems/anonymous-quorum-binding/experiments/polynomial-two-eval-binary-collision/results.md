# Results — polynomial-two-eval-binary-collision

**Outcome:** PASS

**Setup:** Prime `p = 97`, `n = 16`, interpolation nodes `0..15`, evaluation points `r1 = 90`, `r2 = 91` (both outside nodes). Leaf vectors `v ∈ {0,1}^16`.

**Procedure:** Enumerate all `2^16` binary patterns; bucket by `(P(r1), P(r2))` in `𝔽_p^2`. First duplicate bucket yields a collision.

**Observed:** Collision at shared pair `(18, 41)`; Hamming distance between the two patterns is `6`.

**Reasoning:** `2^16 = 65536 > 97^2 = 9409`, so pigeonhole forces some collision for this map; the script exhibits one. Hence **two** independent Lagrange evaluations still do **not** injectively label all `0/1` participation vectors — extending Entry **022** (single eval, unconstrained field values) to **binary** leaves and **two** openings.

**Command:** `python script.py` → exit 0, prints `RESULT: PASS`.
