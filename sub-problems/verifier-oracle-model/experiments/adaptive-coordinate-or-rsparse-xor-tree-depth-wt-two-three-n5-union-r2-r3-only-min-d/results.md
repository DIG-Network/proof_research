# Results

**Outcome:** **PASS**

**Configuration:** `n=5`, `--shells 2,3` (20 masks), `--union-rs 2,3` (20 XOR splits), `--lru-maxsize 4000000`.

**Parent output (parsed):** `coord_plus_union_rs=[2, 3] total_splits=20 min_d=2 dp_sec=0.000`.

**Conclusion:** The **`min_d=2`** phenomenon on the `{2,3}` shell **does not require** **`r=4`** XOR splits in the union. **Weight-3 masks** together with **only** binary and ternary XOR parity tests already force decision-tree depth **2**.
