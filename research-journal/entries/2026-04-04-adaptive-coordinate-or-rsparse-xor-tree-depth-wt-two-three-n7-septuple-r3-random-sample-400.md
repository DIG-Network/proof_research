# Journal entry — 2026-04-04 — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-septuple-r3-random-sample-400`

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-septuple-r3-random-sample-400`

**Context:** verifier-oracle-model (`n=7`, shell `{2,3}`), follow-up after exhaustive sextuple scan (**`C(35,6)=1623160`**, **all** **`min_d=3`**, **zero** depth-**2** witnesses).

**Hypothesis tested:** Among **400** random unordered **7-tuples** of **`r=3`** XOR indices, **some** achieve **`min_d=2`** with **coord + full `r=2`**.

**Outcome:** **FAIL** — `witness_min_d2_count=0`, `wall_sec≈1.086`, `lru_cap=4_000_000`, `seed=0`, universe **`C(35,7)=6724520`**.

**Key finding:** Random sampling found **no** depth-**2** certificate at arity **7** in this draw; does **not** replace exhaustive **`C(35,7)`** enumeration.

**Implications:**

- If a **`min_d=2`** witness exists at **seven** triples, it may be **rare** enough to miss in **`400/6724520`** **or** absent until a larger / exhaustive search.
- Extrapolated wall for full **`6724520`** sept checks is **plausible** at **many hours** on this hardware (linear scaling from sextuple **~3661 s** suggests **~15k s** order-of-magnitude if per-call cost were identical — here per-call is faster in this sample, so empirical timing needed).

**Analogy pass summary:** See `hypothesis.md` — sample-before-exhaustion over **`C(35,7)`** after **`C(35,6)`** closure.
