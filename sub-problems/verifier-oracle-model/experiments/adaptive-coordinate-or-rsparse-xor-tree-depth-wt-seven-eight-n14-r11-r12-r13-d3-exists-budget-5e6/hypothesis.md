# Hypothesis

**Initial claim (falsified):** All three **`r∈{11,12,13}`** would be **PARTIAL** like **`r=8..10`**.

**Observed (authoritative):** **`r=11`** **PARTIAL** (**5e6** budget); **`r=12`** and **`r=13`** **certify** **`d=3`** in **under 0.01 s** DP (**parent exit 0**). So **easy windows** exist at **both** mid-**r** (**`r=7`**) and **very high** **`r`** (**12,13**), with **`r=11`** a **hard** pocket.

**Rationale (post-run):** **Split count** **C(14,r)** drops **364 → 91 → 14**; **`r=12,13`** admit **small** enough XOR libraries that **`exists_tree`** completes under the same budget that **saturates** at **`r=11`**.

## Analogy pass

1. **Abstract structure:** Cost of exhaustive memoized search vs a discrete arity parameter can have **isolated** easy pockets surrounded by **hard** bands.

2. **Analogous domains:**
   - **Phase transitions:** Critical points are **narrow** in parameter space.
   - **Parameterized algorithms:** Some **k** admit **FPT** kernels; adjacent **k** do not.
   - **SAT / CSP:** **Clause density** vs **solvability** is often **non-monotone**.

3. **Machinery:** Barrier analysis; state-space growth; empirical classification under fixed budgets.

4. **Transfer seed:** Extend the **`n=14`**, **`5e6`** **`d=3`** **r-sweep** to **`r=11..13`** to see whether **any** high-**r** leg escapes **PARTIAL** like **`r=7`**.

## Parents

- `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r8-r9-r10-d3-exists-budget-5e6` (**`r=8..10`** **PARTIAL** at **5e6**).
- `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r6-r7-d3-exists-budget-5e6` (**`r=7`** easy vs **`r=6`** hard).
