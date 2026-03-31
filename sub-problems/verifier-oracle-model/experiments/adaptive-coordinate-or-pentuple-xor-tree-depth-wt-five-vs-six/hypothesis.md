# Analogy pass

## 1. Abstract structure

**092** showed **global** **n-bit** **parity** **gives** **`min_d=1`.** **091** **used** **only** **≤4-sparse** **parities** **per** **node** **`min_d=3`.** **This** **experiment** **closes** **the** **091**/**092** **breakthrough** **gap:** **what** **if** **internal** **nodes** **are** **coordinates** **or** **exactly** **5-sparse** **XORs** **(** **all** **C(10,5)=252** **)** **but** **not** **full** **10-bit** **parity** **and** **not** **4-XOR** **or** **3-XOR** **as** **primitives** **?**

## 2. Analogues

1. **LDPC** **rows** **of** **weight** **5** **vs** **weight** **4** **—** **different** **local** **checks** **cover** **different** **error** **patterns.**
2. **Property** **testing** **—** **which** **k**-**juntas** **/** **k**-**sparse** **linear** **tests** **suffice** **to** **separate** **a** **concept** **?**
3. **Basis** **vs** **generating** **set** **in** **F₂ⁿ** **—** **5**-**weight** **vectors** **do** **not** **include** **the** **all**-**ones** **vector** **as** **a** **single** **generator.**

## 3. Machinery

Same **462-bit** **`exists_tree`** **DP** **as** **091,** **with** **252** **precomputed** **5**-**tuple** **XOR** **partitions.**

## 4. Transfer seed

**H:** **`min_d`** **is** **in** **{2,3}** **(** **d=1** **false** **if** **no** **single** **5**-**XOR** **bipartitions** **wt5** **/** **wt6** **)** **;** **compare** **to** **091** **`min_d=3`** **(** **incomparable** **gate** **sets** **—** **091** **has** **quads,** **this** **has** **quints** **).**

---

# Formal hypothesis

Exhaustive **`exists_tree`** **determines** **`min_d`** **for** **coord** **+** **all** **5**-**sparse** **XOR** **nodes** **only** **(** **no** **total** **parity** **,** **no** **r<5** **XOR** **primitives** **).**
