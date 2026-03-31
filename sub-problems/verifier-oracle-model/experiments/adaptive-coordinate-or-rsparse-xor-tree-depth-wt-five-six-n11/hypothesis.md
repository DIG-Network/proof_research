# Analogy pass

## 1. Abstract structure

Measure how **single-arity r-sparse XOR libraries** interact with **adaptive coordinate + XOR decision trees** as **`n`** grows along the **same** **Hamming** **shell** **pair** **`{5,6}`** **(** **still** **`t−1`** **vs** **`t`** **for** **majority** **`t=6`** **when** **`n≥11`** **)** **.**

## 2. Analogues (≥3)

1. **099** — full **`min_d(r)`** on **`(10,{5,6})`**, **non-monotone** **middle** **`r`** **.**
2. **098** — **`(9,{5,6})`**, **210** **masks** **,** **plateau** **/** **bumps** **.**
3. **Coding** **/** **LDPC** **—** **check** **node** **degree** **`r`** **vs** **separation** **power** **on** **a** **fixed** **length** **`n`** **.**

## 3. Machinery

Same DP as **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-five-six-n10/script.py`**: **`N=11`**, **`SHELLS=(5,6)`**, **`|domain|=C(11,5)+C(11,6)=924`**, sweep **`r=2..10`**, unions, full **11**-XOR.

## 4. Transfer seed

**Trace** **whether** **`min_d(r)`** **non-monotonicity** **(** **`r=6,7`** **regression** **vs** **`r=5`** **on** **`n=10`** **)** **persists** **or** **morphs** **when** **`n`** **increases** **to** **11** **(** **same** **shell** **labels** **,** **larger** **ambient** **)** **.**

---

# Formal hypothesis

**H1:** Coord-only **`min_d=11`**; coord + full 11-XOR **`min_d=1`** (parity of **|x|**).

**H2:** **`min_d(r)`** **for** **`r=2..5`** **continues** **the** **prefix** **pattern** **seen** **at** **`n=10`** **(** **non-increasing** **5,4,3,2** **)** **or** **document** **the** **first** **`r`** **where** **it** **breaks** **.**

**H3:** **If** **compute** **allows** **,** **record** **whether** **`min_d(6),min_d(7)>min_d(5)`** **still** **occurs** **(** **099** **-style** **)** **.**

**Falsification:** **Script** **error** **;** **or** **timeout** **before** **baseline** **(** **coord** **+** **full** **XOR** **)** **completes** **—** **then** **mark** **INCONCLUSIVE** **with** **partial** **`r`** **.**

---

# Outcome (post-run)

**PASS.** **H1** OK. **H2** **refined:** **`r=2..5` → 6,5,4,3** (**not** **099’s** **5,4,3,2**). **H3** **false** **on** **`n=11`:** **`min_d(5)=min_d(6)=min_d(7)=3`** **;** **bump** **`r=8→4`** **;** **`r=10→2`**. **Union** **`r≤5` → 3** **(** **vs** **2** **on** **`n=10`** **)** **;** **`r≤10` → 2**. See **`results.md`** **(** **100** **)** **.**
