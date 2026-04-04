# Results — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6-singleton-r3-scan-all-triples

**Outcome:** **FAIL** (hypothesis falsified)

**Setup:** `n=6`, fixed shell `{2,3}` (35 masks in parent), LRU `4_000_000`, union languages driven by `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6/script.py` with new `--union-r3-indices`.

**Baselines (from first parent invocation):**

- `coord_plus_union_rs=[2, 3]` → `total_splits=35`, **`min_d=2`**
- Pair-only `coord_plus_union_rs=[2]` → `total_splits=15`, **`min_d=3`**

**Singleton scan:** For each `r3_index ∈ {0..19}` (`C(6,3)=20`), language = full `r=2` menu (15 splits) + exactly one triple-XOR split → **`total_splits=36`** each time.

**Measured `min_d`:** **`3`** for **every** index `0..19` (uniform). No index achieves `min_d=2` with only one triple adjoined to full `r=2`.

**Conclusion:** The `n=5` phenomenon (“any single triple + full `r=2` → `min_d=2`”) **does not** extend to `n=6` on this shell. Here **one** triple parity is **insufficient**; the full `r=2..3` union (35 splits) is needed for the depth-2 certificate.
