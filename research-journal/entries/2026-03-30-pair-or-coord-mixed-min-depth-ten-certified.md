# 2026-03-30 — pair-or-coord-mixed-min-depth-ten-certified

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-pair-or-tree-depth-wt-five-vs-six/`

**Context:** `verifier-oracle-model`

**Hypothesis (summary):** On **n = 10**, **wt ∈ {5,6}**, adaptive trees with nodes **x_i** or **(x_i ∨ x_j)** have some minimum depth **d**; prior run was **INCONCLUSIVE** past **d = 6** (**068** timeline).

**Outcome:** **PASS**

**Key finding:** **Precomputed** **462-bit** **partition** **masks** **make** **splits** **O(1)** **ANDs;** **exhaustive** **DP** **shows** **no** **tree** **for** **d** **≤** **9** **(** **d=9** **≈** **864** **s** **).** **Mixed** **language** **includes** **coordinate-only;** **045** **gives** **a** **depth-10** **coordinate** **separator** **⇒** **min_d** **=** **10** **for** **mixed** **coord** **+** **pair-OR** **—** **OR** **does** **not** **beat** **045** **here** **(** **vs** **066** **XOR** **at** **5** **).**

**Implications:**

- **Pair-OR** **as** **an** **adaptive** **probe** **is** **much** **weaker** **than** **pair-XOR** **for** **this** **shell** **pair** **(** **depth** **cost** **and** **no** **strict** **improvement** **over** **coordinates** **).**
- **Exact** **min-d** **claims** **may** **need** **long** **runs** **at** **high** **d** **unless** **closed** **with** **a** **structural** **lift** **(** **subset** **⊆** **superset** **of** **gates** **).**

**Analogy pass summary:** **(** **unchanged** **in** **`hypothesis.md`** **)** **circuit** **monotonicity** **(** **OR** **vs** **linear** **),** **sensor** **fusion,** **branching** **programs.**
