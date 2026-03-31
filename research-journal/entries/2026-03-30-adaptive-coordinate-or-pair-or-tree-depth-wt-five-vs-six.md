# 2026-03-30 — adaptive-coordinate-or-pair-or-tree-depth-wt-five-vs-six

- **Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-pair-or-tree-depth-wt-five-vs-six/`
- **Context:** verifier-oracle-model (**digest** **“** **mixed** **pair-OR** **+** **coordinate** **”** **after** **066** **/** **067** **).

## Hypothesis tested

**Mixed** **internal** **nodes** **x_i** **or** **(x_i ∨ x_j)** **on** **n=10,** **wt∈{5,6}:** **quantify** **minimum** **perfect-tree** **depth** **vs** **066** **(** **XOR** **mix,** **d=5** **)** **and** **045** **(** **coordinates,** **d=10** **).**

## Outcome: **INCONCLUSIVE** (exact **min_d**); **partial** **certificate** **d≤6** **impossible**

**Memoized** **DP** **(** **462-bit** **subsets** **)** **shows** **no** **separator** **for** **d=1..6** **(** **d=6** **≈90–105** **s** **per** **run** **).** **d≥7** **did** **not** **finish** **in** **multi-minute** **windows** **—** **pair-OR** **state** **explosion** **vs** **066.** **Theory:** **min_d≤10** **(** **coordinates** **alone** **).**

## Key finding

**Pair-OR** **is** **not** **“** **free** **”** **like** **XOR** **in** **this** **toy:** **same** **shell** **pair,** **same** **n,** **but** **existence** **search** **cost** **and** **trailing** **feasible** **depth** **band** **(** **7–10** **)** **left** **open** **here.**

## Implications

- **Verifier** **oracle** **taxonomies** **should** **treat** **2-bit** **monotone** **(** **OR** **)** **and** **parity-linear** **(** **XOR** **)** **probes** **as** **different** **for** **adaptive** **depth** **and** **for** **search** **complexity** **off** **line.**
- **Finish** **min_d** **with** **a** **faster** **engine** **if** **needed** **for** **tight** **vs** **045** **/** **066.**

## Analogy pass summary

**Monotone** **vs** **linear** **Boolean** **gates** **(** **circuit** **complexity** **);** **sensor** **“** **any** **alarm** **”** **vs** **parity** **—** **OR** **mix** **does** **not** **inherit** **XOR’s** **066** **shortcut** **on** **this** **evidence.**
