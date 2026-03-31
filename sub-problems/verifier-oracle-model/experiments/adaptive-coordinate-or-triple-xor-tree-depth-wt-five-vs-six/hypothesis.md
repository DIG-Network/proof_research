# Analogy pass

## 1. Abstract structure

**066** **closed** **the** **pairwise** **F₂** **linear** **probe** **family** **(** **x_i** **⊕** **x_j** **)** **at** **min** **depth** **5** **on** **(10,{5,6}).** **A** **strict** **extension** **allows** **one** **node** **to** **apply** **parity** **on** **three** **coordinates** **x_i** **⊕** **x_j** **⊕** **x_k** **—** **a** **different** **affine** **hyperplane** **restriction** **than** **any** **single** **pair** **XOR** **(** **though** **composable** **at** **higher** **depth** **in** **066** **).**

## 2. Analogues

1. **Error-correcting** **codes** **—** **parity-check** **rows** **of** **weight** **3** **vs** **weight** **2.**
2. **Group** **testing** **—** **3-way** **XOR** **pools** **as** **linear** **measurements** **(** **021** **line** **).**
3. **Decision** **trees** **with** **richer** **split** **library** **—** **VC** **/** **split** **complexity** **increases.**

## 3. Machinery

**Same** **462-bit** **subset** **DP** **as** **082** **/** **085:** **precompute** **partition** **masks** **for** **each** **triple** **i<j<k** **with** **child** **0** **when** **b_i⊕b_j⊕b_k=0,** **1** **otherwise.** **Plus** **10** **coordinate** **splits.**

## 4. Transfer seed

**Hypothesis:** **min_d** **for** **mixed** **coord** **+** **triple-XOR** **is** **either** **<** **5** **(** **strict** **improvement** **over** **066** **)** **or** **=** **5** **(** **triple** **gates** **do** **not** **shrink** **depth** **further** **).** **Cannot** **exceed** **10** **(** **coordinates** **).**

---

# Formal hypothesis

**H:** **Exhaustive** **memoized** **`exists_tree`** **on** **the** **full** **462-set** **determines** **the** **minimum** **depth** **d** **(** **or** **partial** **log** **+** **INCONCLUSIVE** **if** **time** **budget** **exhausted** **before** **min** **found** **).**

**Falsification:** **Implementation** **bug** **(** **e.g.** **coordinate** **depth** **10** **fails** **).**

**Outcome:** see `results.md`.
