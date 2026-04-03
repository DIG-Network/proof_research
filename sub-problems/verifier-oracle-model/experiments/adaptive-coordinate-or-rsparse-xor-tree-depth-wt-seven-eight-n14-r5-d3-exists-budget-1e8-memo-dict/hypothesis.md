# Hypothesis

## Analogy pass (structural)

1. **Abstract structure:** Same **`r=5`**, **`d=3`-only** full **2002** XOR menu probe as the **3×10⁷** **`--memo-dict`** run, but with **~3.3×** larger **`exists_tree`** budget (**10⁸** invocations) to see whether the **`d=3`** feasibility check can **complete** (PASS/FAIL) or remains **PARTIAL** with a larger distinct-state footprint.

2. **Analogous domains:** (a) Fixed-capacity vs unbounded memo: dict grows with explored **`(bits, depth)`** frontier — scaling budget tests whether the frontier saturates before completion. (b) Prior **300M/10M LRU** **PARTIAL** vs **30M dict** **PARTIAL** bracket “effort” in different memo regimes. (c) Session-state next action: monitor **RSS** as **`memo_dict_size`** grows.

3. **Machinery:** Parent **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py`**: **`--skip-baseline`**, **`--r-single 5`**, **`--d-min 3 --d-max 3`**, **`--max-exists-calls 100000000`**, **`--memo-dict`**.

4. **Transfer seed:** If **10⁸** completes **`d=3`** with **`feasible=True/False`**, we get a **sound** menu verdict for this envelope; if still **PARTIAL**, record **`memo_dict_size`** and wall time to extrapolate toward **3×10⁸** dict path vs LRU.

## Falsifiable claim

**H0:** Budget **10⁸** still exhausts before a definitive **`d=3`** line (**PARTIAL**), with **`memo_dict_size`** strictly larger than **~12.26M** at **3×10⁷**.

**H1:** Run reaches a complete **`feasible=`** outcome for **`d=3`** within **10⁸** invocations under **`--memo-dict`**.

## Memory / lineage

- **Parent experiment (wrapper chain):** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-3e7-memo-dict` (INCONCLUSIVE **PARTIAL** at **3×10⁷**).
- **Code parent:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py`.
