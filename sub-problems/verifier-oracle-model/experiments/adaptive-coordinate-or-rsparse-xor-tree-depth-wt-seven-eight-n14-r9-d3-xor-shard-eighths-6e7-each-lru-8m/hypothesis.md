# Hypothesis — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r9-d3-xor-shard-eighths-6e7-each-lru-8m

## Analogy pass

1. **Abstract structure:** Dual to the **r=5** eighth-shard stress run: same **2002** XOR index partition and **6×10⁷** per-eighth **`exists_tree`** cap, **8M** LRU, **d=3**-only — test whether **r=9** shows different **LRU** pressure or **PARTIAL** behavior than **r=5** when the per-shard budget doubles from **3e7**.

2. **Analogous domains:** Same as **r=5** run — cache/working-set vs budget; symmetry breaking between two equivalent-count XOR arities on **C(14,9)=C(14,5)**.

3. **Machinery:** Side-by-side miss peaks and wall time.

4. **Transfer seed:** Prior data showed **r=9** slightly slower than **r=5** on some full-menu budgets but **matched** eighth **3e7** phenomenology — **6e7** checks whether that parity persists under **2×** cap.

## Falsifiable claim

**Claim:** **r=9** eighth shards at **6e7** each complete without **PARTIAL**, all **`d=3 feasible=False`**, and **LRU** misses stay **≪ 8M** (matching **r=5** stress), **or** an arity asymmetry appears in saturation / **PARTIAL** rates.
