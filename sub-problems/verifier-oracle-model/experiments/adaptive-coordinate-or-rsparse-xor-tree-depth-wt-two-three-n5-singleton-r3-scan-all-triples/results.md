# Results — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-singleton-r3-scan-all-triples

**Outcome:** **FAIL** (hypothesis falsified)

**Setup:** `n=5`, shell `{2,3}`, `--union-rs 2,3` with `--union-r3-indices` a **single** index `i ∈ {0,…,9}` (lex `C(5,3)` triples), **`--lru-maxsize 4000000`**, parent `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5/script.py`.

**Baselines (sanity):**

- Full `r=2..3` union (`20` splits): **`min_d=2`**.
- `r=2` only (`10` splits): **`min_d=3`**.

**Singleton scan:** For **every** `i ∈ {0,…,9}`, **`total_splits=11`**, **`min_d=2`**.

**Witness set:** `[0,1,2,3,4,5,6,7,8,9]` (all ten).

**Conclusion:** The first witness in lexicographic subset search (`…-min-r3-splits-for-min-d2`) was **not** structurally unique — **any** one triple-XOR parity split, when added to the **full** pair-XOR menu on this shell, suffices for the depth-`2` certificate. The earlier “single triple suffices” result generalizes to **full universality** among triples at `n=5`.
