# Results — mixed-coordinate-xor-tree-witness-wt-five-vs-six

## Outcome: **PASS**

## Measured

- **`exists_tree(full, 5)`:** **True** (same DP as entry **066**).
- **`witness_tree_depth`:** **5** (longest root-to-leaf path in the printed nested tree).
- **Leaf coverage:** `json_leaf_count_sum(root) == 462` (all masks with **wt ∈ {5,6}** accounted for as multiset sizes at leaves).
- **Runtime (this machine):** ~**22–24 s** (dominated by warming **`exists_tree`** on reachable **(S, d)** states).

## Witness shape (066 split order)

Under the same probe order as **066** (coordinates **0..9**, then pair XORs **(i,j)** lex), the **first** depth-5 solution found by **`witness(full,5)`** uses **only pair-XOR internal nodes** (root **x₀ ⊕ x₁**; deeper nodes use **(2,3), (4,5), (6,7), (8,9)** in the printed tree). No coordinate split **x_i** appears, because **for this depth budget** every coordinate bisection fails **`exists_tree` on one side at depth 4** before any XOR split succeeds—consistent with **066** trying XOR only after all coordinates fail at each DP state.

## Verdict

Constructive certificate for **066**: not only **∃** depth-5 mixed tree, but one explicit nested JSON plan matching the existential DP’s split priority.
