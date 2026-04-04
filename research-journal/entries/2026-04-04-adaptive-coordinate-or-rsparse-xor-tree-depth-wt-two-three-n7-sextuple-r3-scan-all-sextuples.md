# Journal entry — 2026-04-04 — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-sextuple-r3-scan-all-sextuples`

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-sextuple-r3-scan-all-sextuples`

**Context:** verifier-oracle-model (`n=7`, shell `{2,3}`), next step after exhaustive `C(35,5)` quintuple scan (`witness_min_d2_count=0`, ~766 s).

**Hypothesis tested:** **Some** unordered **6-tuple** of **`r=3`** XOR indices yields **`min_d=2`** with **coord + full `r=2`**.

**Outcome:** **FAIL** — `witness_min_d2_count=0`, `sexts_checked=1623160`, `wall_sec≈3661.0`, `lru_cap=4_000_000`.

**Key finding:** **Complete** enumeration of **`C(35,6)`** confirms **no** depth-**2** certificate from **six** triple-XOR parities plus **full `r=2`** at this **`n=7`** slice — the sparse triple ladder remains **`min_d=3`** through arity **6**.

**Implications:**

- **`min_d=3`** persists for **coord + full `r=2` + {1,2,3,4,5,6}** triple-parities (**exhaustive** at each arity **1..6** on this ladder).
- **`C(35,7)`** (~6.7M) is the next combinatorial step if pursuing **seven** triple parities; otherwise pivot to **partial `r=4` sub-menus**, **hitting sets**, or other augmentations.

**Analogy pass summary:** See `hypothesis.md` — GF(2) parity / coding-theory ladder; exhaustive closure after quintuple proof.
