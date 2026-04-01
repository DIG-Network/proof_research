# Hypothesis

**Claim:** On `n=14`, shells `{7,8}`, with `--max-exists-calls 5_000_000`, `d=3`-only, and `--lru-maxsize 0`, each of **`r∈{8,9,10}`** hits the **same PARTIAL** class as **`r∈{5,6}`** (budget exhausted before a definitive `min_d` decision), unlike **`r=7`** which certifies `d=3` quickly.

**Rationale:** The **`r=7`** easy band is **isolated**: more XOR splits (`r=8`) re-enters a heavy DP state space; **`r=9`** was already known as multi-hour-hard for `d=3` with unbounded memo; **`r=10`** has fewer splits but may still saturate the same budget.

## Analogy pass

1. **Abstract structure:** Parameterized family of adaptive decision problems; computational cost vs a discrete arity parameter can have **multiple easy windows** and **hard bands**, not a single unimodal curve.

2. **Analogous domains:**
   - **Spin glasses / disordered systems:** Energy barriers depend on **microstructure**, not monotonically on interaction range.
   - **Algorithm parameterized complexity:** Some parameter values admit **kernelization**; neighbors do not.
   - **Coding theory:** List-decoding radius vs performance is often **non-monotone** in auxiliary parameters.

3. **Machinery:** Barrier heights; kernel sizes; combinatorial state counts.

4. **Transfer seed:** Treat **`r`** as tuning a **split library size** vs **constraint strength**; measure **complete vs partial** under **fixed** `exists_tree` budget to map **which** `r` share the same **hardness class** as **`r=5,6`**.

## Parents

- `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r6-r7-d3-exists-budget-5e6` (**`r=7`** easy vs **`r=6`** hard under **5e6**).
- `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14-r5-d3-exists-budget-5e6` (**`r=5`** partial).
