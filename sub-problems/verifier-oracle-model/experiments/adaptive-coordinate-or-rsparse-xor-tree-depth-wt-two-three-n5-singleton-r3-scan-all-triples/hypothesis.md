# Hypothesis — singleton `r=3` scan (all 10 triples)

**Parent:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-min-r3-splits-for-min-d2` (witness `r3_indices=[0]` → `min_d=2`).

**Falsifiable claim:** Among the **10** lex-ordered `C(5,3)` triple-XOR splits, **only** index **`0`** (triple `(0,1,2)`) achieves **`min_d=2`** when adjoined to the **full** `r=2` XOR menu on shell `{2,3}` (with `4M` LRU). Equivalently: the witness set of singleton indices with `min_d=2` is **`{0}`** exactly.

- If **any** `i≠0` also yields `min_d=2` → hypothesis **falsified**.
- If **all** `i≠0` yield `min_d≠2` (typically `3`) and `i=0` yields `2` → **confirmed**.

## Analogy pass (mandatory)

1. **Abstract structure:** Fix a large “generator” menu (all pair parities); ask which **single** extra parity generator is **sufficient** to lower a depth certificate from `3` to `2`. This is a **critical generator** / **matroid circuit** style question on a discrete split lattice.

2. **Analogous domains:** (i) **Minimal hitting sets** in hypergraphs — which one edge resolves a property; (ii) **Greedy basis** in linear codes — which one parity check reduces distance to a target; (iii) **Single-feature sufficiency** in decision trees — one split that separates a class when coordinate splits alone cannot.

3. **Machinery there:** Certificates via **witness** indices; **enumeration** over a small finite catalog (`C(5,3)=10`).

4. **Transfer seed:** Treat each triple-XOR split as a candidate **parity generator**; exhaustive singleton scan is the finite **sensitivity** map of the `min_d` functional under `r=2` fixation.
