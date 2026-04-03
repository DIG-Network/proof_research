# Hypothesis

## Analogy pass (structural)

1. **Abstract structure:** Same **`r=5`**, **`d=3`-only** full **2002** XOR menu as **3×10⁷** **`--memo-dict`**, but **5×10⁷** invocation budget and **Linux VmRSS** logging after each depth probe to relate **`memo_dict_size`** to resident RAM.

2. **Analogous domains:** (a) Working-set growth vs RSS in dynamic programming. (b) Empirical scaling from **12.3M** dict entries at **3×10⁷** calls — extrapolate memory at **~1.7×** more work. (c) Session-state directive: intermediate budgets + external RSS instrumentation before retrying **10⁸** dict.

3. **Machinery:** Parent adds **`--log-rss`**; wrapper passes **`--max-exists-calls 50000000`**, **`--memo-dict`**, **`--log-rss`**.

4. **Transfer seed:** If RSS scales roughly linearly with distinct memo keys, **5×10⁷** gives a second point for extrapolating whether **10⁸** is safe on typical hosts.

## Falsifiable claim

**H0:** Outcome is still **PARTIAL** at **d=3** with **`memo_dict_size`** ~ linear in budget; **VmRSS** tracks dict growth within a predictable band.

**H1:** **PASS** at **d=3** (full menu admits depth 3 within **5×10⁷** invocations).

## Memory / lineage

- **Parent experiment:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-3e7-memo-dict` (**INCONCLUSIVE**, **~12.3M** memo entries at cutoff).
- **Code parent:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` (**--log-rss** added this session).
