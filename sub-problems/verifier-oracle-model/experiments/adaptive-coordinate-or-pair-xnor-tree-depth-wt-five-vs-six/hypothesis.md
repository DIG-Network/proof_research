# Analogy pass

## 1. Abstract structure

**053** classified **2-input** **binary** **gates** **invariant** **under** **bit** **complement** **(a,b)↦(1−a,1−b):** **XOR** **and** **XNOR** **(** **equivalently** **≠** **/** **=** **on** **pairs** **of** **bits** **).** **066** **computed** **minimum** **adaptive** **tree** **depth** **with** **coordinate** **+** **pair-XOR** **nodes** **on** **the** **(10,{5,6})** **shell** **pair** **(** **min_d** **=** **5** **).** **Question:** **does** **swapping** **XOR** **→** **XNOR** **at** **internal** **nodes** **change** **reachable** **leaf** **purity** **(** **existence** **of** **a** **perfect** **separator** **at** **given** **depth** **)?**

## 2. Analogues

1. **Graph** **isomorphism** **—** **same** **cut** **with** **edge** **orientation** **reversed.**
2. **Boolean** **circuits** **—** **De** **Morgan** **/ ** **output** **negation** **often** **preserves** **computability** **up** **to** **relabelling** **outputs.**
3. **Decision** **trees** **—** **left** **/** **right** **child** **order** **is** **a** **presentation** **choice** **when** **both** **subtrees** **must** **succeed** **(** **AND** **composition** **).**

## 3. Machinery

**Partition** **of** **the** **domain** **induced** **by** **“** **x_i** **XOR** **x_j** **”** **:** **{** **equal** **bits,** **unequal** **bits** **}.** **XNOR** **is** **¬(XOR)** **on** **{0,1},** **so** **the** **same** **two** **blocks** **appear;** **only** **which** **block** **is** **labelled** **0** **vs** **1** **may** **swap.**

## 4. Transfer seed

**Conjecture:** **Mixed** **coord** **+** **pair-XNOR** **has** **the** **same** **minimum** **depth** **as** **066** **(** **5** **)** **because** **each** **allowed** **split** **is** **the** **same** **set** **partition** **as** **some** **XOR** **split** **(** **child** **order** **irrelevant** **under** **symmetric** **AND** **recursion** **).**

---

# Formal hypothesis

Let **D** **=** **{** **x** **∈** **{0,1}^10** **:** **wt(x)** **∈** **{5,6}** **}.** **Allow** **internal** **nodes** **x_k** **or** **XNOR(x_i,x_j)** **with** **i<j** **(** **branch** **0** **when** **XNOR=0** **i.e.** **bits** **differ,** **1** **when** **equal** **—** **any** **fixed** **convention** **is** **fine** **if** **consistent** **).**

**H:** **The** **minimum** **d** **such** **that** **a** **perfect** **separator** **tree** **exists** **equals** **5** **(** **same** **as** **066** **).**

**Falsification:** **Computed** **min_d** **≠** **5.**

**Outcome (after run):** **PASS** — see `results.md`.
