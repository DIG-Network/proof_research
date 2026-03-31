# Analogy pass

## 1. Abstract structure

The verifier-oracle toy fixes a **hidden** participation vector `x ∈ {0,1}^n` and asks what **adaptive binary query trees** (each internal node a **coordinate** or a **fixed family** of **F₂-linear** probes) can **perfectly separate** two **Hamming shells** `|x| ∈ {t−1, t}`. **Depth** proxies for **query budget**; **gate arity** (`r`-sparse XOR) is a **resource** knob.

## 2. Analogues (≥3 domains)

1. **Property testing / decision tree complexity** — symmetric properties of Boolean strings; **parity gates** vs **coordinate** probes; **symmetry** and **invariance** obstructions (e.g. **049** complement on `n = 2T−1` for **pure** pair-XOR trees).
2. **Error-correcting codes** — **syndrome** bits are **linear** functionals; **weight** shells relate to **distance** from **0**; **which** linear masks **refine** the **weight** partition?
3. **Combinatorial search / branch-and-bound** — **adaptive** splitting of a **finite** feasible set; **depth** = **worst-case** **decisions** to reach **pure** **leaves**.

## 3. Machinery in each domain

- **Property testing:** **Exact** **DP** on **bitmask-over-domain-indices** **`exists_tree(S, d)`** (project standard from **045**, **066**, **091–093**).
- **Coding:** **Same** **DP** **as** **“which** **affine** **hyperplane** **splits** **the** **code** **by** **weight** **shell?”** **toy.**
- **Search:** **Memoized** **recursion** **over** **subsets** **of** **the** **462/70** **active** **indices.**

## 4. Transfer seed

**Breakthrough** **049** **:** **pair-XOR-only** **trees** **impossible** **when** **`n = 2T−1`** **for** **shells** **`T−1`** **vs** **`T`.** **Breakthrough** **093** **/** **arity** **ladder** **on** **`(10,{5,6})`** **:** **pair** **`min_d=5`**, **triple** **4**, **quad** **3**, **pentuple** **2**, **full** **parity** **1**. **Test** **the** **same** **mixed** **`coord + r-sparse`** **languages** **on** **a** **smaller** **`n = 2T−1`** **instance** **`(n,t)=(7,4)`**, **shells** **`{3,4}`**, **domain** **size** **`C(7,3)+C(7,4)=70`**, **to** **see** **whether** **the** **depth** **/ ** **arity** **scaling** **rhymes** **with** **the** **`n=10`** **row** **and** **where** **`r=4`** **sits** **relative** **to** **full** **`n`** **-bit** **parity** **(** **here** **quad** **=** **full** **XOR** **on** **7** **bits** **).**

---

# Formal hypothesis

**H1:** On **`n=7`**, masks with **`popcount ∈ {3,4}`** (**70** **indices**), **adaptive** trees with internal nodes **`x_i`** **or** **`x_{i₁}⊕⋯⊕x_{i_r}`** for **all** **lexicographic** **`r`** **-tuples** admit **`exists_tree(full, d)=True`** **for** **`d`** **values** **that** **form** **a** **strict** **arity** **ladder** **(** **expect** **`r=2`** **>** **`r=3`** **>** **`r=4`** **in** **minimal** **depth** **,** **with** **`r=4`** **coinciding** **with** **global** **parity** **hence** **`min_d=1`** **for** **`r≥4`** **in** **this** **geometry** **).**

**H2 (** **sanity** **):** **`r=4`** **on** **`n=7`** **is** **exactly** **the** **full** **parity** **functional** **(** **up** **to** **relabeling** **of** **the** **all-one** **mask** **)** **—** **so** **`coord+quad`** **language** **includes** **a** **single** **split** **that** **separates** **odd** **wt=3** **from** **even** **wt=4** **(** **`min_d=1`** **).**

**Falsification:** **Computed** **`min_d`** **violates** **the** **expected** **ordering** **or** **`r=4`** **does** **not** **yield** **`d=1`**.

**Note:** **Pair-only** **(** **no** **coords** **)** **impossibility** **is** **049** **;** **this** **experiment** **is** **mixed** **`coord+pair`** **like** **066**.

---

# Outcome (post-run, `results.md`)

**H2** **refuted:** **`coord+quad`** **has** **`min_d=3`**, **not** **1** **—** **4-sparse** **primitives** **are** **not** **equivalent** **to** **full** **`n`** **-bit** **parity** **.**

**H1** **partially** **confirmed:** **pair** **`min_d=4`**, **triple** **`3`**, **but** **quad** **also** **`3`** **(** **no** **strict** **drop** **triple→quad** **on** **this** **instance** **).** **Union** **`pair∪triple∪quad`** **→** **`min_d=2`**. **Coord-only** **`min_d=7`**, **coord+full** **7-XOR** **`min_d=1`**. **PASS** **overall** **as** **enumerated** **certificate** **.**
