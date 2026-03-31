# 2026-03-31 — pair-nand-mixed-tree-depth-ten-certified

- **Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-pair-nand-tree-depth-wt-five-vs-six/`
- **Context:** verifier-oracle-model (adaptive decision trees on wt 5 vs 6)

## Hypothesis (short)

Mixed **coord** **+** **pair-NAND** **nodes** **on** **(10,{5,6})** **either** **match** **XOR** **(** **min_d=5** **),** **OR** **(** **min_d=10** **),** **or** **sit** **strictly** **between.**

## Outcome: **PASS**

- **d = 1 … 9:** **`exists_tree(full, d) = False`** **(** **exhaustive** **memoized** **DP** **with** **precomputed** **462-bit** **partition** **masks** **).** **d=9** **≈1145** **s** **on** **one** **run** **(** **900** **s** **budget** **hit** **after** **d=9** **completed** **—** **before** **d=10** **).**
- **d = 10:** **`exists_tree(full, 10) = True`** **(** **≈228** **s** **)** **⇒** **min_d = 10.**

## Key finding

**NAND** **does** **not** **yield** **the** **XOR** **depth** **collapse** **(** **5** **);** **it** **aligns** **with** **pair-OR** **/** **coordinates** **(** **10** **).** **Together** **with** **053** **(** **only** **XOR/XNOR** **are** **2-bit** **complement-invariant** **):** **non-invariant** **gates** **tested** **so** **far** **(** **OR,** **NAND** **)** **give** **min_d** **=** **n** **on** **this** **domain.**

## Implications

- **Treat** **“parity-like”** **(** **XOR/XNOR** **)** **vs** **“corner”** **(** **OR** **/** **NAND** **)** **as** **the** **main** **split** **for** **mixed** **pair** **gates** **on** **this** **toy** **—** **not** **just** **“linear** **vs** **nonlinear”.**
- **Further** **gates** **(** **e.g.** **NOR** **)** **or** **a** **proof** **that** **all** **non-parity** **binary** **splits** **force** **min_d** **≥** **10** **would** **compress** **the** **taxonomy.**

## Analogy pass summary

**Abstract:** **threshold** **separation** **via** **adaptive** **binary** **splits** **on** **a** **finite** **mask** **set.** **Analogues:** **monotone** **Boolean** **circuits;** **hyperplane** **vs** **orthant-corner** **cuts;** **decision** **tree** **complexity.** **Seed:** **NAND** **isolates** **the** **(1,1)** **corner** **—** **different** **geometry** **from** **OR’s** **(0,0)** **corner,** **but** **same** **min** **depth** **here.**
