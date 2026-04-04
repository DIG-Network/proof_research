# Hypothesis — pair of `r=3` splits (all `C(20,2)` pairs), n=6 shell `{2,3}`

**Parent driver:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6/script.py`.

**Context:** Experiment `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6-singleton-r3-scan-all-triples` **falsified** universal singleton sufficiency: **every** one of the 20 triple-XOR splits, together with the **full** `r=2` menu, still gives **`min_d=3`** (vs `n=5` where every singleton gave `min_d=2`).

**Falsifiable claim:** Among all **`C(20,2)=190`** unordered pairs of distinct triple indices `{i,j}`, **at least one** pair yields **`min_d=2`** for the mixed language **coord + full `r=2` XOR + exactly those two `r=3` splits** (default `4M` LRU, same shell).

- If **no** pair achieves `2` (all `190` give `min_d=3` while baselines hold) → **FAIL** (even two triple splits never collapse depth to 2 at `n=6` in this regime).
- If **some** pair achieves `2` → **PASS** (minimal `k` for triples is at most `2`; witness indices recorded).

## Analogy pass (mandatory)

1. **Abstract structure:** A **2-generator** extension of a fixed rich split menu; **interaction** between parity constraints — does a **pair** of triple parities ever act like a “sufficient statistic” for the `min_d` functional where each **single** triple did not?

2. **Analogous domains:** (i) **Synergy** in information — \(I(X;Y|Z)\) can exceed marginal contributions; (ii) **Matroid** circuits — minimal dependent sets of size \(>1\); (iii) **2-term DNF** over parity features — when does a conjunction of two parity tests reduce decision-tree depth?

3. **Machinery:** Exhaustive `O(n^6)` pair enumeration over `C(6,3)`; witness as certificate.

4. **Transfer seed:** After universal singleton failure at `n=6`, the next combinatorial knob is **pairwise** triple menus before accepting that **full** 20-triple menu is the minimal witness for `min_d=2`.
