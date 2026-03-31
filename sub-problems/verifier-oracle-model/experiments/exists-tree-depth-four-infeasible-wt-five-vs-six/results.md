# Results — `exists_tree(full, 4)` infeasible, `exists_tree(full, 5)` feasible

## Outcome: **PASS**

## Repro

```text
python -u sub-problems/verifier-oracle-model/experiments/exists-tree-depth-four-infeasible-wt-five-vs-six/script.py
```

Exit code: **0**.

## Measured quantities

| Check | Value |
|-------|--------|
| `exists_tree_full_d4` | **False** |
| `exists_tree_full_d5` | **True** |

## Reasoning

**Same** **`exists_tree`** **recursion** **as** **067** **/** **066** **(** **coordinate** **then** **pair-XOR** **splits,** **`recurse_children`** **semantics** **unchanged** **).** **The** **full** **wt∈{5,6}** **subset** **of** **`{0,1}^{10}`** **admits** **no** **perfect** **separator** **tree** **of** **depth** **≤4** **but** **admits** **one** **at** **depth** **≤5.** **So** **the** **mixed** **oracle** **minimum** **(** **066** **)** **is** **not** **only** **a** **search** **artifact:** **budget** **4** **is** **globally** **insufficient** **on** **`full`.**

## Wall clock

~**34** **s** **on** **the** **machine** **used** **(** **memoized** **`exists_tree`** **).**
