# Journal entry — 2026-04-04 — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-quintuple-r3-random-sample-200`

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-quintuple-r3-random-sample-200`

**Context:** verifier-oracle-model (`n=7`, shell `{2,3}`), follow-up after exhaustive quadruple scan (`52360/52360`, all `min_d=3`).

**Hypothesis tested:** Among **200** random unordered **5-tuples** of **`r=3`** XOR indices, **some** achieve **`min_d=2`** with **coord + full `r=2`**.

**Outcome:** **FAIL** — `witness_min_d2_count=0`, `wall_sec≈0.486`, `lru_cap=4_000_000`.

**Key finding:** Random sampling found **no** depth-**2** certificate at arity **5** in this draw; does **not** replace exhaustive **`C(35,5)`** enumeration.

**Implications:**

- If a **`min_d=2`** witness exists at **5** triples, it is **rare** enough to miss in **`200/324632`** **or** absent (full scan needed).
- Extrapolated wall for full **`324632`** quint checks is **plausible** at **tens of minutes** on this hardware — next step can be exhaustive scan.

**Analogy pass summary:** See `hypothesis.md` — parity-splits as linear tests; random probe before full **`C(35,5)`** combinatorial closure.
