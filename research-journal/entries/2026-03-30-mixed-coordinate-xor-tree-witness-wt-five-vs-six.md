# 2026-03-30 — mixed-coordinate-xor-tree-witness-wt-five-vs-six

- **Experiment:** `sub-problems/verifier-oracle-model/experiments/mixed-coordinate-xor-tree-witness-wt-five-vs-six/`
- **Context:** verifier-oracle-model (constructive follow-up to **066**).

## Hypothesis tested

A depth-≤5 mixed tree (internal nodes **x_i** or **x_i ⊕ x_j**) separating **wt ∈ {5,6}** on **n=10** exists (**066**); the script should emit one nested JSON witness using the **same split priority** as the existential DP.

## Outcome: **PASS**

**`witness_tree_depth = 5`.** **`exists_tree(full,5)`** recomputed **True**; printed tree passes **Σ leaf counts = 462** check.

## Key finding

**Two-phase** construction (**`exists_tree` then gated `witness`**) runs in ~**24 s** vs **timeout** on naive cached DFS. The **first** witness under **066** order is **all pair-XOR internals** (root **(0,1)**, then **(2,3), (4,5), (6,7), (8,9)** pattern in the emitted tree): **no** coordinate node appears because **no** coordinate split admits **two** depth-4 feasible children on the full **462**-set under this order.

## Implications

- **066** is backed by an **auditable** decision plan, not only a **YES** from memoized search.
- **Proof / query mix** may be **highly tie-break dependent**; comparing **witnesses** under alternate **first-success** rules is a sensible next stress test.

## Analogy pass summary

**SAT model extraction,** **principal variation** **in** **game** **trees,** **compiler** **lowering** **witness** **vs** **feasibility** **bit** **—** **implemented** **as** **existential** **DP** **+** **principal-variation** **replay** **with** **feasibility** **gates.**
