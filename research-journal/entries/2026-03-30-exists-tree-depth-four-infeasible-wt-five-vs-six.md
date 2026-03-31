# 2026-03-30 — exists-tree-depth-four-infeasible-wt-five-vs-six

- **Experiment:** `sub-problems/verifier-oracle-model/experiments/exists-tree-depth-four-infeasible-wt-five-vs-six/`
- **Context:** verifier-oracle-model (**depth** **lower** **bound** **vs** **066** **/** **067** **).

## Hypothesis tested

**`exists_tree(full,4)=False`** **and** **`exists_tree(full,5)=True`** **for** **full** **wt∈{5,6}** **domain,** **`exists_tree`** **as** **in** **067.**

## Outcome: **PASS**

**Observed** **`False`** **then** **`True`.**

## Key finding

**Depth** **4** **is** **globally** **infeasible** **on** **the** **entire** **462-set** **under** **the** **mixed** **coord+XOR** **feasibility** **predicate;** **depth** **5** **is** **feasible** **—** **tight** **next** **step** **above** **failure.**

## Implications

- **Any** **witness** **construction** **tied** **to** **this** **`exists_tree`** **cannot** **claim** **shallower** **than** **5** **on** **this** **instance** **without** **changing** **the** **model.**

## Analogy pass summary

**Decision-tree** **depth** **lower** **bounds** **/** **phase** **transition** **in** **solvability** **—** **exhaustive** **DP** **pins** **d=4** **vs** **5.**
