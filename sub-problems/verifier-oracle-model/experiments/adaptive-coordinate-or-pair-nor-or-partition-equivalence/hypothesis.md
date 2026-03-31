# Analogy pass

## 1. Abstract structure

**Adaptive** **trees** **whose** **internal** **nodes** **are** **coordinate** **splits** **or** **2-bit** **Boolean** **gates** **on** **pairs.** **Each** **gate** **induces** **a** **bipartition** **of** **the** **current** **leaf** **set** **(** **462** **masks** **for** **wt∈{5,6}** **).** **The** **search** **problem** **depends** **only** **on** **which** **unordered** **bipartitions** **are** **available** **at** **each** **node** **type,** **not** **on** **which** **side** **is** **labeled** **0** **vs** **1** **(** **given** **symmetric** **recursion** **).**

## 2. Analogues

1. **De** **Morgan** **duality** **—** **NOR** **=** **¬∨** **on** **{0,1}²** **flips** **output** **but** **the** **level** **sets** **swap** **(** **one** **singleton** **corner** **vs** **its** **complement** **).**
2. **Labeled** **vs** **unlabeled** **splits** **in** **decision** **trees** **—** **binary** **tree** **over** **the** **same** **partition** **family** **with** **child** **labels** **permuted** **per** **node.**
3. **084** **(** **XNOR** **vs** **XOR** **)** **—** **same** **partition,** **swapped** **0/1** **children** **⇒** **identical** **`exists_tree`.**

## 3. Machinery

**Formal:** **For** **pair** **(i,j),** **OR** **split:** **A** **=** **{both** **bits** **0},** **B** **=** **{≥1** **bit** **1}.** **NOR** **with** **branch** **0** **when** **NOR=0:** **NOR=0** **iff** **¬(x_i∨x_j)=0** **iff** **x_i∨x_j=1** **⇒** **branch-0** **side** **=** **B,** **branch-1** **=** **A.** **Same** **{A,B}.** **`recurse_children_bits`** **is** **symmetric** **(** **AND** **of** **two** **recursive** **calls** **commutes;** **one-sided** **empty** **cases** **unchanged** **).**

## 4. Transfer seed

**Hypothesis:** **Mixed** **coord** **+** **pair-NOR** **has** **the** **same** **minimum** **separating** **depth** **as** **mixed** **coord** **+** **pair-OR** **(** **082** **,** **min_d=10** **)** **—** **no** **new** **DP** **past** **d=9** **required** **if** **we** **verify** **partitions** **and** **low-depth** **DP** **agreement.**

---

# Formal hypothesis

**H:** **On** **(10,{5,6}),** **`exists_tree_NOR(bits,d)`** **=`exists_tree_OR(bits,d)`** **for** **all** **`bits,d`** **(** **hence** **min_d_NOR** **=** **min_d_OR** **=** **10** **by** **082** **).**

**Falsification:** **Any** **`d`** **where** **OR** **and** **NOR** **feasibility** **differ** **on** **the** **full** **462-set,** **or** **partition** **masks** **fail** **the** **swap** **check.**

**Outcome:** **PASS** **—** **NOR-mixed** **≡** **OR-mixed** **(** **partition** **swap** **);** **min_d** **=** **10** **by** **082.** **Details** **in** **`results.md`.**
