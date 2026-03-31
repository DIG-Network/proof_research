# Results — mixed-coordinate-xor-tree-witness-xor-first-wt-five-vs-six

## Outcome: **PASS**

## Measured

- **`exists_tree(full, 5)`:** **True** (same predicate as **066** / **067**).
- **`witness_tree_depth`:** **5**.
- **Internal gate counts:** **`coord=0`, `xor=31`** (full binary tree of depth 5 ⇒ **31** internals).
- **Leaf coverage:** **`json_leaf_count_sum(root) == 462`** (assert in script).

## Comparison to 067 (coord-first witness)

Byte-compared the **JSON** **tree** **(** **after** **stripping** **script** **header** **lines** **)** **to** **`mixed-coordinate-xor-tree-witness-wt-five-vs-six`:** **identical.**

So on this instance, **XOR-first** **principal-variation** **order** **does** **not** **change** **the** **emitted** **plan:** **the** **first** **lex** **pair-XOR** **(** **0,1** **)** **is** **already** **the** **first** **feasible** **split** **at** **the** **root** **under** **066’s** **feasibility** **test,** **and** **no** **coordinate** **split** **beats** **it** **in** **067’s** **loop** **either** **(** **coords** **are** **tried** **first** **there** **but** **fail** **at** **depth** **4** **on** **both** **children** **of** **the** **full** **462-set** **—** **see** **067** **notes** **).**

## Verdict

**Tie-break** **experiment** **succeeds** **(** **witness** **valid** **)** **and** **refines** **the** **story:** **for** **this** **fixed** **(** **n=10,** **wt{5,6}** **)** **instance,** **067** **vs** **069** **collapse** **to** **the** **same** **π_tree** **—** **not** **all** **tie-breaks** **matter** **when** **the** **winning** **XOR** **root** **is** **unique** **as** **first** **successful** **probe** **in** **both** **orderings.**
