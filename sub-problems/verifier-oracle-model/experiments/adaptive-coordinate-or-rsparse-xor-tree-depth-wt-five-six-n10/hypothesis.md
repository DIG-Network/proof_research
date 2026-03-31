# Analogy pass

## 1. Abstract structure

Adaptive **`exists_tree`** on a bitmask over a fixed union of two Hamming shells in **`{0,1}^n`**, with internal nodes that are coordinate splits or one **r-sparse F₂ XOR** test drawn from a library (all r-subsets of coordinate indices).

## 2. Analogues (≥3)

1. **`(10,{5,6})` piecewise experiments** — **066 / 090 / 091 / 093 / 092** gave **pair → … → pentuple → total** depths **5,4,3,2,1** but never one script’s **`min_d(r)`** table for every **`r`**.

2. **`(9,{5,6})` sweep** — **098** showed **triple/quad/pentuple** can **plateau** when **`n`** shrinks; need the **canonical** **`n=10`** profile to compare.

3. **Coding / group testing** — **syndrome arity** vs **number of parity checks**; here **arity** **`r`** is the **local** **F₂** **linear** **functional** **degree** **on** **bits**.

## 3. Machinery

Same DP as **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-five-six-n9/script.py`**: **`N=10`**, **`SHELLS=(5,6)`**, **`|domain|=462`**, sweep **`r=2..9`**, unions **`{2,3,4}`**, **`2..5`**, **`2..9`**.

## 4. Transfer seed

**Unify** prior **spot** **depths** **into** **one** **reproducible** **`min_d(r)`** **curve** **and** **union** **rows** **—** **checks** **monotonicity** **and** **flags** **any** **mismatch** **with** **066/090/091/093**.

---

# Formal hypothesis

**H1:** Coord-only **`min_d=10`**; coord + full 10-XOR **`min_d=1`**.

**H2:** For each **`r∈{2,…,9}`**, **`min_d(r)`** matches the known ladder **5→4→3→2** at **r=2,3,4,5**; beyond that, **monotone** **non-increase** **was** **an** **implicit** **expectation** **(** **falsified** **)** **.**

**H3:** Union **`r∈{2,3,4,5}`** yields **`min_d=2`**; union **`r∈{2,…,9}`** does not exceed **`2`**.

**Falsification:** DP error, or **`min_d(r)`** **contradicts** **066/090/091/093** **for** **`r∈{2,3,4,5}`**.

---

# Outcome (post-run)

**PASS.** **`r∈{2,3,4,5}`:** **5,4,3,2** **(** **matches** **066** **/** **090** **/** **091** **/** **093** **)** **.** **`min_d(r)`** **not** **monotone:** **`r=6→3`**, **`r=7→4`**, **`r=8→3`**, **`r=9→2`**. **Unions:** **`r∈{2,3,4}→3`**, **`r≤5`** **and** **`r≤9`** **both** **`→2`**. See **`results.md`** **(** **099** **)** **.**
