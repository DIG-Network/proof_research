# Analogy pass

## 1. Abstract structure

**091** built **adaptive** trees with **bounded-weight** **F₂** **parities** **(** **≤4** **coordinates** **per** **node** **).** **Global** **Hamming** **parity** **(** **XOR** **of** **all** **n** **bits** **)** **is** **the** **same** **as** **popcount** **mod** **2** **on** **{0,1}ⁿ.** **For** **n=10,** **wt∈{5,6},** **every** **weight-5** **vector** **is** **odd** **and** **every** **weight-6** **vector** **is** **even** **—** **so** **one** **linear** **functional** **might** **bipartition** **the** **462-set** **into** **two** **pure** **leaves** **without** **a** **depth-3** **tree.**

## 2. Analogues

1. **Single** **parity-check** **bit** **of** **a** **code** **—** **detects** **odd** **/** **even** **Hamming** **weight** **on** **the** **whole** **word.**
2. **Sufficient** **statistic** **for** **“odd** **vs** **even** **count”** **in** **Bernoulli** **trials** **(** **sum** **mod** **2** **).**
3. **Hardness** **of** **coding-theory** **problems** **often** **separates** **by** **global** **syndrome** **vs** **local** **checks.**

## 3. Machinery

Same **462-bit** **`exists_tree`**, **plus** **one** **extra** **partition:** **branch** **0** **when** **⊕_{i=0}^{9} x_i = 0** **(** **equivalently** **popcount** **even** **),** **else** **1.**

## 4. Transfer seed

**H:** **`min_d = 1`** **when** **this** **total-parity** **split** **is** **allowed** **(** **with** **or** **without** **coordinates** **—** **parity** **alone** **suffices** **at** **the** **root** **).**

---

# Formal hypothesis

**`exists_tree(full, 1) = True`** **under** **internal** **nodes** **=** **coordinate** **OR** **total** **XOR** **(** **one** **non-coordinate** **gate** **).**
