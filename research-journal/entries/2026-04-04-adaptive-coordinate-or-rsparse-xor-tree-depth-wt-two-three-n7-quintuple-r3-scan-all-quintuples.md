# Journal entry — 2026-04-04 — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-quintuple-r3-scan-all-quintuples`

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-quintuple-r3-scan-all-quintuples`

**Context:** verifier-oracle-model (`n=7`, shell `{2,3}`), exhaustive closure after random quint sample (`200/324632`, all `min_d=3`) and prior exhaustive quadruple scan (`52360/52360`).

**Hypothesis tested:** **Some** unordered **5-tuple** of **`r=3`** XOR indices yields **`min_d=2`** with **coord + full `r=2`**.

**Outcome:** **FAIL** — `witness_min_d2_count=0`, `quints_checked=324632`, `wall_sec≈765.946`, `lru_cap=4_000_000`.

**Key finding:** **Complete** enumeration of **`C(35,5)`** confirms **no** depth-**2** certificate from **five** triple-XOR parities plus **full `r=2`** at this **`n=7`** slice — strengthening the random-sample evidence into a **finite proof** for arity **5** in this language family.

**Implications:**

- **`min_d=3`** persists for **coord + full `r=2` + {1,2,3,4,5}** triple-parities (**exhaustive** at each arity **1..5** along this ladder).
- Next combinatorial jump is **`C(35,6)`** sextuples (**~1.62M** cases) or a **different** augmentation (**`r=4`**, unions, etc.).

**Analogy pass summary:** See `hypothesis.md` — GF(2) parity certificates; exhaustive search after random probe.
