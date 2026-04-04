# Journal entry — 2026-04-04 — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-union-r2-r3-r4-min-d`

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-union-r2-r3-r4-min-d`

**Context:** verifier-oracle-model (`n=7`, shell `{2,3}`), after exhaustive quintuple `r=3` scan (all `min_d=3`) and known PASS for union `r∈{2,3,4,5}`.

**Hypothesis tested:** **coord + union `r∈{2,3,4}`** (omit `r=5`) still has **`min_d=2`**.

**Outcome:** **PASS** — `total_splits=91`, `min_d=2`, `dp_sec≈0.002`, `lru_maxsize=4_000_000`.

**Key finding:** **Full `r=4`** XOR menu together with full **`r=2`** and **`r=3`** suffices for a depth-**2** certificate at this slice; **`r=5`** parities are **not necessary** for the union-style witness found by the DP (they may still appear in *some* minimal split set, but the coarse union language does not require them).

**Implications:**

- Refines **`n7-full-r2-r5-union-min-d`**: drop **`r=5`** without losing **`min_d=2`**.
- Juxtaposition: **finite** “few triples” still stuck at **`min_d=3`** through arity **5**, while **full `r=4`** crosses the barrier — the qualitative jump is **arity / coverage of 4-point parities**, not **5-point** ones.

**Analogy pass summary:** See `hypothesis.md` — minimal sufficient features / parity basis redundancy.
