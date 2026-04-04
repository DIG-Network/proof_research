# Hypothesis — singleton `r=3` scan (all 20 triples), n=6 shell `{2,3}`

**Parent driver:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6/script.py` (fixed 35-mask shell).

**Context:** At `n=5`, the scan `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-singleton-r3-scan-all-triples` **failed** the “only index 0” claim: **every** singleton triple with full `r=2` achieved `min_d=2`.

**Falsifiable claim:** At `n=6`, for **every** lex-ordered triple index `i ∈ {0..19}` (`C(6,3)=20`), the mixed language **full `r=2` XOR menu + exactly one `r=3` split** (index `i`) still yields **`min_d=2`** under the default `4M` LRU cap (same regime as `n=5`).

- If **any** `i` yields `min_d≠2` (typically `3`) while baselines hold → hypothesis **falsified** (counterexample index is data).
- If **all** `i` yield `2` → **PASS** (universal singleton sufficiency at `n=6`).

## Analogy pass (mandatory)

1. **Abstract structure:** Threshold of **one** extra parity generator atop a fixed rich menu; **finite sensitivity** of a `min_d` functional over a catalog of generators (`C(n,3)` triple parities).

2. **Analogous domains:** (i) **Minimal sufficient statistics** — when does one extra statistic collapse a complexity measure; (ii) **Matroid circuit** / **single-element extensions**; (iii) **Feature ablation** in ensemble splits — one coordinate flip changes ensemble depth.

3. **Machinery:** Exhaustive enumeration over `C(6,3)`; witness set as certificate.

4. **Transfer seed:** Extend the `n=5` “all singletons work” phenomenon to `n=6` or locate the first structural breakage.
