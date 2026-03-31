# Analogy pass

## 1. Abstract structure

**053** **classified** **2-input** **gates** **on** **{0,1}²** **by** **behavior** **under** **global** **bit** **complement** **(a,b)↦(1−a,1−b).** **XOR/XNOR** **are** **invariant;** **NAND/NOR** **are** **not.** **066** **/** **084** **show** **mixed** **coord** **+** **parity** **pair** **gates** **cut** **depth** **to** **5;** **082** **shows** **pair-OR** **does** **not** **(** **min_d** **=** **10** **).** **NAND** **is** **monotone** **in** **a** **partial** **order** **(** **0** **only** **on** **(1,1)** **)** **—** **a** **different** **geometry** **than** **OR** **(** **0** **only** **on** **(0,0)** **).**

## 2. Analogues

1. **Monotone** **Boolean** **circuits** **—** **NAND** **is** **universal** **but** **asymmetric** **on** **inputs.**
2. **Hyperplane** **cuts** **vs** **corner** **cuts** **—** **NAND** **isolates** **a** **single** **orthant** **corner** **(both** **1)** **from** **the** **rest.**
3. **Decision** **tree** **literature** **—** **allowed** **split** **family** **changes** **reachable** **leaf** **complexity.**

## 3. Machinery

Same **462-bit** **subset** **DP** **as** **pair-OR** **experiment:** **precomputed** **partition** **masks** **per** **coordinate** **and** **per** **pair** **(i,j)** **for** **NAND(x_i,x_j)** **with** **branch** **0** **iff** **both** **bits** **are** **1** **(** **NAND** **output** **0** **).**

## 4. Transfer seed

**Hypothesis:** **Mixed** **coord** **+** **pair-NAND** **either** **(** **A** **)** **matches** **XOR** **(** **min_d** **=** **5** **),** **(** **B** **)** **matches** **OR** **(** **min_d** **=** **10** **),** **or** **(** **C** **)** **lands** **strictly** **between** **—** **any** **outcome** **sharpens** **the** **gate** **taxonomy** **beyond** **053’s** **symmetry** **classification.**

---

# Formal hypothesis

**n = 10,** **domain** **wt ∈ {5,6},** **462** **masks.** **Internal** **nodes:** **x_k** **or** **NAND(x_i,x_j)** **with** **i<j,** **branch** **0** **on** **(1,1),** **1** **otherwise.**

**H:** **The** **minimum** **perfect-separator** **depth** **d** **is** **determined** **by** **exhaustive** **memoized** **`exists_tree`** **(** **or** **partial** **negative** **+** **INCONCLUSIVE** **if** **budget** **exhausted** **before** **min** **found** **).**

**Falsification:** **Incorrect** **partition** **masks** **or** **logic** **bug** **(** **e.g.** **coordinate** **tree** **at** **10** **fails** **).**

**Outcome (after run):** **PASS** **—** **min_d** **=** **10** **(** **d≤9** **out,** **d=10** **in** **);** **details** **in** **`results.md`.**
