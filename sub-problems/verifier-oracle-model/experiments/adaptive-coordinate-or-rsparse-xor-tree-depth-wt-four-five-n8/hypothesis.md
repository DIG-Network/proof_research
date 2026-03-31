# Analogy pass

## 1. Abstract structure

Same **verifier-oracle** template as **095:** adaptive **perfect** **classification** **trees** over **two** **Hamming** **shells** **in** **`{0,1}^n`**, **internal** **nodes** **=** **coordinate** **or** **fixed** **`r`**-**sparse** **F₂** **XOR** **pools** **;** **`min_d`** **=** **worst-case** **depth**.

## 2. Analogues (≥3)

1. **095** **`(7,{3,4})`** **—** **majority** **`t=4`**, **`n=2t−1`**, **triple/quad** **`min_d`** **tie** **at** **3**.
2. **`(10,{5,6})`** **row** **(** **066/091/093** **)** **—** **strict** **arity** **ladder** **until** **pentuple** **;** **`n`** **even** **there** **too** **(** **10** **)** **but** **shells** **mid-range**.
3. **Coding** **/ ** **syndrome** **trees** **—** **which** **low-weight** **parity** **checks** **refine** **the** **constant-weight** **slice** **?**

## 3. Machinery

Exhaustive **DP** **`exists_tree`** **on** **bitmask** **over** **domain** **indices** **(** **126** **masks** **for** **`C(8,4)∪C(8,5)`** **).**

## 4. Transfer seed

Take **`n=8`**, **shells** **`{4,5}`** **(** **strict** **majority** **`t=5`** **for** **8** **validators** **;** **`n ≠ 2t−1`** **since** **`2t−1=9`** **)** **.** **Hypothesis:** **the** **pair→triple→quad→pentuple** **`min_d`** **vector** **either** **matches** **a** **strict** **stepwise** **ladder** **(** **like** **`(10,{5,6})`** **)** **or** **shows** **another** **tie** **/ ** **plateau** **as** **in** **095** **.** **Global** **`n`****-bit** **parity** **still** **splits** **even** **`|x|=4`** **vs** **odd** **`|x|=5`** **in** **one** **node** **(** **`min_d=1`** **).**

---

# Formal hypothesis

**H1:** **`coord + full`** **8****-bit** **XOR** **has** **`min_d=1`** **on** **this** **domain** **.**

**H2:** **For** **`r`** **in** **`{2,3,4,5}`** **,** **`min_d(r)`** **is** **non-increasing** **in** **`r`** **and** **strictly** **drops** **at** **each** **`r→r+1`** **step** **unless** **a** **documented** **plateau** **(** **as** **in** **095** **triple=quad** **)** **.**

**H3:** **`coord +`** **union** **of** **all** **`r`****-sparse** **XORs** **for** **`r∈{2,3,4,5}`** **achieves** **`min_d≤2`** **(** **analogue** **of** **093** **/** **095** **union** **)** **.**

**Falsification:** **DP** **contradicts** **any** **claim** **above** **(** **e.g.** **`min_d(full)>1`** **,** **unexpected** **non-monotone** **`min_d(r)`** **)** **.**

---

# Outcome (post-run)

**H1** **OK.** **H2** **refuted:** **`min_d(2)=min_d(3)=min_d(5)=4`**, **`min_d(4)=2`** **—** **not** **monotone** **in** **`r`**,** **and** **`r=5`** **is** **worse** **than** **`r=4`**. **H3** **OK** **(** **`min_d≤2`** **for** **union** **`r∈{2,3,4,5}`** **).**
