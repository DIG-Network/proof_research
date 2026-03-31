# Outcome: **PASS**

## Claim

On **n = 10**, **wt ∈ {5,6}**, mixed adaptive trees with internal nodes **x_k** or **NOR(x_i, x_j)** with branch **0** iff **NOR = 0** have the **same** minimum separating depth as mixed **coord + pair-OR** (**082**): **min_d = 10**.

## Proof sketch (reduction to **082**)

1. **OR** **pair** **split** **(** **branch** **0** **=** **OR** **=** **0** **):** **A** **=** **{masks** **with** **x_i** **=** **x_j** **=** **0},** **B** **=** **complement** **in** **the** **current** **leaf** **set.**

2. **NOR** **=** **¬(x_i** **∨** **x_j).** **Branch** **0** **when** **NOR** **=** **0** **⇔** **x_i** **∨** **x_j** **=** **1** **⇔** **mask** **∈** **B.** **Branch** **1** **when** **NOR** **=** **1** **⇔** **both** **0** **⇔** **mask** **∈** **A.** **So** **ordered** **pair** **(child0,** **child1)_NOR** **=** **(B,** **A)** **=** **swap** **of** **(A,** **B)_OR.**

3. **`recurse_children_bits`** **is** **symmetric:** **for** **nonempty** **both** **sides** **it** **requires** **`exists(b0)`** **∧** **`exists(b1)`** **(** **commutative** **);** **if** **one** **side** **is** **empty** **it** **recurses** **only** **on** **the** **other.** **Hence** **the** **memoized** **`exists_tree`** **predicate** **is** **identical** **for** **OR-mixed** **and** **NOR-mixed** **languages** **on** **every** **`(bits,** **d)`.**

4. **082** **certified** **min_d** **=** **10** **for** **OR-mixed** **(** **d** **≤** **9** **impossible** **+** **coordinate** **⊂** **mixed** **⇒** **d=10** **feasible** **).** **Therefore** **min_d** **=** **10** **for** **NOR-mixed.**

## Script checks

- **All** **45** **pairs:** **`nor_parts[π]`** **=** **`(or_b1,` `or_b0)`.**
- **Empirical** **regression:** **for** **d** **=** **1..5,** **`feasible_at_depth(...,` `or_parts,` `d)`** **=** **`feasible_at_depth(...,` `nor_parts,` `d)`** **(** **all** **`False`**, **matching** **082** **for** **d** **≤** **5** **).**

**Run** **(** **default** **):** **~22** **s** **total** **on** **this** **machine.**

## Relation to **084**

**Same** **logical** **pattern** **as** **XNOR** **vs** **XOR:** **complementary** **output** **labeling** **per** **pair** **gate** **with** **fixed** **unordered** **bipartition** **—** **here** **NOR** **/** **OR** **are** **De** **Morgan** **duals** **on** **the** **pair** **variables.**
