# Experiment entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r11-r12-r13-d3-exists-budget-5e6

**Date:** 2026-04-01  
**Path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r11-r12-r13-d3-exists-budget-5e6/`

## Context

verifier-oracle-model — `n=14`, shells `{7,8}`, **5×10⁶** `exists_tree` budget, `d=3`-only, **`r∈{11,12,13}`** (optional spot check after **`r=8..10`** all **PARTIAL**).

## Hypothesis tested

**Initial:** all three legs **PARTIAL** like **`r=8..10`**. **Falsified:** **`r=12,r=13`** certify **`d=3`** quickly; **`r=11`** **PARTIAL**.

## Outcome

**PASS** (on **revised** script checks: **`r=11`→exit 2**, **`r=12,r=13`→exit 0**).

## Key finding

**Second easy band** at **very high** **`r`**: **`r=12`** (91 splits) and **`r=13`** (14 splits) finish **`d=3`** in **~10⁻² s** DP, while **`r=11`** (364 splits) still **saturates** **5×10⁶** **`exists_tree`** calls (**~35–44 s**). **`r=7`** is **not** the only tractable **`r`** at this budget; cost is **not** monotone in **split count** (**`r=10`** with 1001 splits is **PARTIAL**, **`r=12`** with 91 is **easy**).

## Implications

- **`min_d(r)`** tractability under **fixed** memo budget has **multiple** isolated **easy** regions and **hard** pockets (**`r=11`** between **`r=10`** and **`r=12`**).
- Any narrative “interior **`r`** hard, boundary **`r`** easy” needs **refinement** — **`r=13`** is **easier** than **`r=11`**.

## Analogy pass summary

Parameterized search: **non-monotone** **barrier heights** — **multiple** **phases** along **`r`**.

## Space-definition

None.
