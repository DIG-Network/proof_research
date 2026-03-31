# Analogy pass

## 1. Abstract structure

Same **adaptive** **`exists_tree`** **toy** **as** **095**/**096** **:** **two** **Hamming** **shells** **,** **internal** **nodes** **coordinate** **or** **one** **fixed** **r-sparse** **F₂** **XOR** **from** **a** **library** **.**

## 2. Analogues (≥3)

1. **096** **`(8,{4,5})`** **—** **`min_d(r)`** **non-monotone** **(** **`r=4`** **best** **)** **.**
2. **095** **`(7,{3,4})`** **—** **`n=2t−1`**, **triple=quad** **plateau** **.**
3. **Breakthrough** **093** **`(10,{5,6})`** **—** **strict** **arity** **ladder** **5→4→3→2** **.**

## 3. Machinery

Exhaustive **memoized** **DP** **on** **subsets** **of** **the** **domain** **index** **set** **(** **252** **masks** **for** **`C(9,4)∪C(9,5)`** **).**

## 4. Transfer seed

Take **`n=9`**, **shells** **`{4,5}`** **,** **majority** **`t=5`** **so** **`n=2t−1`** **(** **complement** **swaps** **the** **two** **shells** **,** **cf.** **049** **)** **.** **Hypothesis:** **`min_d(r)`** **profile** **differs** **from** **`n=8`** **same** **shell** **pair** **(** **096** **)** **—** **e.g.** **possible** **return** **to** **strict** **drops** **or** **different** **plateau** **structure** **;** **full** **9-XOR** **still** **`min_d=1`** **(** **even/odd** **)** **.**

---

# Formal hypothesis

**H1:** **Coord** **+** **full** **9-bit** **XOR** **has** **`min_d=1`** **.**

**H2:** **For** **each** **`r∈{2,3,4,5,6,7,8}`** **,** **single-arity** **`coord+r-XOR`** **`min_d`** **is** **computed** **and** **recorded** **;** **we** **compare** **to** **`(8,{4,5})`** **and** **`(10,{5,6})`** **rows** **.**

**H3:** **`coord`** **+** **union** **`r∈{2,3,4,5}`** **(** **and** **optionally** **through** **`8`** **)** **has** **`min_d≤3`** **(** **heuristic** **: ** **between** **096** **`2`** **and** **093** **`2`** **)** **.**

**Falsification:** **Timeout** **/ ** **OOM** **on** **DP** **(** **report** **INCONCLUSIVE** **with** **partial** **rows** **)** **.**

---

# Outcome (post-run)

**H1** **OK.** **H2** **:** **`min_d`** **by** **`r`:** **2→5,** **3→3,** **4→3,** **5→3,** **6→4,** **7→3,** **8→2** **(** **interior** **peak** **at** **`r=6`** **)** **.** **H3** **:** **union** **2–5** **`min_d=2`**, **union** **2–8** **`2`** **. ** **PASS** **.**
