# Hypothesis

**Claim:** On `n=14`, shells `{7,8}`, `coord + r=9` XOR (2002 splits), `d=3`-only probe: splitting the XOR partition list into contiguous halves `[0:1001)` and `[1001:2002)` and running the bounded DP **sequentially** on each half with **12×10⁷** `exists_tree` budget and **8M** LRU (mirror of the **`r=5`** **12e7/8M** half-shard run) may yield **`d=3 feasible=True`** on at least one half—a **witness** that the full language admits depth ≤3 (superset monotonicity in parent `script.py`).

## Analogy pass (mandatory)

1. **Abstract structure:** Same **2002**-split menu as **`r=5`**; paired A/B on **parity pattern** while holding **budget**, **LRU**, and **shard geometry** fixed.

2. **Analogous domains:** (i) *Controlled pair* in experimental design—swap one factor (`r`) with matched combinatorial cardinality; (ii) *SAT sharding*—same clause count, different literal wiring; (iii) *Symmetry breaking*—binomial duality does not preserve DP hardness here; test whether **half-shard** scaling tracks **`r=5`** or diverges.

3. **Machinery:** **`--xor-index-range`** on parent; **8M LRU** per half; **sequential** subprocesses (avoid parallel **10M** OOM on this host).

4. **Transfer candidate:** Prior **`r=9`** full-menu and **10M** LRU half-shards were **PARTIAL**; **`r=9`** is often **faster** than **`r=5`** at the same visit cap on full menu. This run asks whether **8M** half-shards at **12e7** close the gap toward a witness or stay **PARTIAL** like **`r=5`**.

**Falsifiable:** If both halves **PARTIAL** or finish with `d=3 feasible=False`, no witness at this budget; does not decide global `d=3` for full 2002.

**Parent:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py`

**Builds on:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-xor-shard-halves-12e7-each-lru-8m` (both halves PARTIAL ~927 s each at **12e7/8M**); `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-halves-12e7-each-lru-10m` (both PARTIAL ~1034+992 s at **10M** LRU).
