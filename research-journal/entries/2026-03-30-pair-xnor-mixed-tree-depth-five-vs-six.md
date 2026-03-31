# 2026-03-30 — pair-xnor-mixed-tree-depth-five-vs-six

**Experiment path:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-pair-xnor-tree-depth-wt-five-vs-six/`

**Context:** `verifier-oracle-model`

**Hypothesis (summary):** On **n = 10,** **wt ∈ {5,6},** mixed trees with **coordinate** or **pair-XNOR** nodes have the same minimum depth as **066** **(XOR)** because splits induce the same bipartitions.

**Outcome:** **PASS**

**Key finding:** **XNOR** **partitions** **=** **XOR** **partitions** **with** **child** **labels** **swapped;** **DP** **gives** **d<5** **infeasible,** **d=5** **feasible** **⇒** **min_d** **=** **5.** **Confirms** **053’s** **algebraic** **symmetry** **at** **the** **decision-tree** **existence** **level** **for** **this** **domain.**

**Implications:**

- **No** **need** **to** **track** **XOR** **vs** **XNOR** **separately** **for** **mixed** **linear** **pair** **probes** **on** **{0,1}** **coordinates.**
- **OR** **vs** **XOR/XNOR** **remains** **the** **meaningful** **split** **(** **082** **vs** **066** **/** **084** **).**

**Analogy pass summary:** **Graph** **cut** **orientation,** **De** **Morgan,** **symmetric** **AND** **recursion** **—** **seed:** **partition** **identity.**
