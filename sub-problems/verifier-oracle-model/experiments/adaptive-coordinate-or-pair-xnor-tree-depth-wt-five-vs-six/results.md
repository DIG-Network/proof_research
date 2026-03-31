# Results: adaptive-coordinate-or-pair-xnor-tree-depth-wt-five-vs-six

**Outcome:** `PASS`

## Model

- **n = 10,** domain **D** **=** **462** **masks** **with** **wt ∈ {5,6}.**
- **Internal** **nodes:** **coordinate** **x_k** **or** **pair** **XNOR** **(** **branch** **0** **when** **bits** **differ,** **1** **when** **equal** **).**

## Verified facts

1. **Partition** **identity:** **for** **each** **pair** **(i,j),** **the** **two** **blocks** **from** **XNOR** **equal** **those** **from** **XOR** **(** **066** **)** **with** **0/1** **labels** **swapped** **(** **equal** **vs** **differ** **).**
2. **Exhaustive** **memoized** **`exists_tree`:** **no** **tree** **for** **d** **=** **1..4;** **feasible** **at** **d** **=** **5.**
3. **Hence** **min_d** **=** **5** **—** **same** **as** **mixed** **coord** **+** **pair-XOR** **(** **066** **).**

## Interpretation

**XNOR** **does** **not** **change** **the** **family** **of** **allowed** **splits** **relative** **to** **XOR** **on** **binary** **coordinates;** **it** **only** **relabels** **which** **child** **is** **“** **0** **”** **vs** **“** **1** **”.** **Under** **symmetric** **AND** **of** **subtree** **feasibility** **(** **empty-branch** **short-circuit** **),** **decision-tree** **existence** **at** **each** **depth** **is** **unchanged.**

## Contrast

**Mixed** **coord** **+** **pair-OR** **(** **082** **)** **:** **min_d** **=** **10** **(** **no** **shallow** **separator** **).**
