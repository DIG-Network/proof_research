# Hypothesis: n=14 r=9 d=3 — 10e7 budget, 12M LRU

## Analogy pass (mandatory)

1. **Abstract structure:** Same DP family as **r=5** but XOR menu **C(14,9)=2002** splits; **r=9** DP has been systematically **faster** than **r=5** at equal **exists_tree** budget in prior runs (asymmetric state graph).

2. **Analogous domains:** (a) Same search / TT story as **r=5**; (b) spin glasses — different interaction graphs change relaxation time; (c) SAT — clause density shifts hardness while formula size is similar.

3. **Machinery:** Graph-dependent mixing times; density-parametrized hardness.

4. **Transfer seed:** If **12M** LRU helps **r=9** more than **r=5**, we learn whether cache pressure is **r**-dependent in this envelope; compare wall times to **10e7/10M** ~957 s.

## Falsifiable claim

**r=9**, **d=3** completes within **10⁸** invocations and **12M** LRU with a definite **feasible**/**infeasible** line, or **PARTIAL** / OOM.

## Parent

`../adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py`
