# 2026-03-31 — pair-nor-or-partition-equivalence-min-depth-ten

- **Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-pair-nor-or-partition-equivalence/`
- **Context:** verifier-oracle-model

## Hypothesis (short)

**Mixed** **coord** **+** **pair-NOR** **has** **the** **same** **`exists_tree`** **behavior** **as** **mixed** **coord** **+** **pair-OR** **(** **hence** **same** **`min_d`** **).**

## Outcome: **PASS**

- **Proof:** **For** **each** **(i,j),** **NOR=0** **iff** **x_i∨x_j=1** **⇒** **NOR** **child-0** **/** **child-1** **subsets** **are** **exactly** **OR** **child-1** **/** **child-0** **(** **swap** **).** **`recurse_children_bits`** **symmetric** **⇒** **identical** **memoized** **DP** **on** **all** **`(bits,d)`.**
- **082** **⇒** **`min_d_OR=10`** **⇒** **`min_d_NOR=10`.**
- **Script:** **45/45** **mask** **swap** **checks** **;** **d=1..5** **OR** **vs** **NOR** **`feasible(full,d)`** **agree** **(** **regression** **).**

## Key finding

**NOR** **adds** **nothing** **over** **OR** **as** **an** **adaptive** **split** **primitive** **here** **—** **dual** **of** **084** **(** **XNOR** **redundant** **with** **XOR** **).** **Completes** **the** **AND/OR/XOR/XNOR/NAND/NOR** **picture** **on** **this** **shell** **with** **082** **/** **084** **/** **085** **.**

## Implications

- **Future** **oracle** **experiments** **can** **treat** **(OR,NOR)** **as** **one** **equivalence** **class** **for** **existence** **of** **depth-`d`** **separators** **on** **`{5,6}`** **masks.**
- **Prefer** **structural** **reductions** **before** **re-running** **heavy** **pair-gate** **DP.**

## Analogy pass summary

**De** **Morgan** **/** **labeled** **vs** **unlabeled** **splits** **/** **084** **child-label** **swap** **—** **seed:** **output** **negation** **swaps** **which** **side** **is** **called** **0** **but** **not** **the** **available** **bipartitions.**
