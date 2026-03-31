# 2026-03-30 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-five-six-n11

**Context:** `sub-problems/verifier-oracle-model`  
**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-five-six-n11/`

## Hypothesis tested

Full **`min_d(r)`** sweep **`r=2..10`** on **`(11,{5,6})`** (924 masks); check whether **099**’s **`min_d(6),min_d(7)>min_d(5)`** pattern persists when **`n`** increases.

## Outcome

**PASS**

## Key finding

- **Prefix** **`r=2..5`:** **6,5,4,3** (**+1** vs **099** **per** **`r`** **)** **.**
- **No** **099-style** **regression** **at** **`r=6,7`:** **all** **plateau** **3** **;** **bump** **`r=8→4`**, **`r=10→2`** **.**
- **Union** **`r≤5`:** **`min_d=3`** **vs** **`2`** **on** **`n=10`** **;** **`r≤10`** **still** **`→2`** **.**

## Implications

- **`min_d(r)`** **landscape** **depends** **on** **`n`** **in** **non-uniform** **ways** **(** **not** **just** **rescaling** **099** **)** **.**
- **Resource** **claims** **tied** **to** **“pentuple** **+** **lower** **arities”** **must** **be** **re-checked** **per** **`n`** **.**

## Analogy pass summary

**099** **/** **098** **/** **LDPC** **arity** **—** **confirmed** **H3** **fails** **on** **`n=11`** **.**

## Invented space

None.
