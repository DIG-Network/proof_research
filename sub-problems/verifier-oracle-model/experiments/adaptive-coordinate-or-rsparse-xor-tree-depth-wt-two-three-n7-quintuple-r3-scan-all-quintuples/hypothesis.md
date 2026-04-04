# Hypothesis — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-quintuple-r3-scan-all-quintuples`

## Analogy pass

1. **Abstract structure:** At **n=7**, shell **`{2,3}`**, we ask whether **any** choice of **five** independent **`r=3`** XOR parity splits, together with **coordinate splits** and the **full `r=2`** XOR menu, admits a **depth-2** decision tree (**`min_d=2`**) for the majority threshold slice. Exhaustive **`C(35,4)`** found **no** witness with **four** triple-splits; arity **5** is the next finite closure step (**`C(35,5)=324632`**).

2. **Where else this structure appears:**
   - **GF(2) linear systems:** each triple-split is a halfspace; tree depth is a restricted certificate.
   - **Combinatorial search / SAT:** complete enumeration over a small witness space after random probe found nothing.
   - **Coding / covering:** asking whether five parity tests can separate a structured weight class at this ambient size.

3. **Machinery in those domains:** exhaustive enumeration; dynamic-programming **`min_depth`** as an oracle for the fixed language family.

4. **Transfer seed:** If **no** quintuple yields **`min_d=2`**, the **`min_d=3`** barrier for this **`coord + r=2 + few r=3`** family is **proven** at **n=7** for arities **≤5** triple-splits (given prior exhaustive **pair/triple/quadruple** results). If a witness exists, we record concrete indices.

## Falsifiable claim

**There exists** an unordered **5-tuple** of indices in **`0..34`** such that **`min_d=2`** for **coord + full `r=2` + those five `r=3` XOR splits**.

**Opposite outcome:** **every** one of the **`324632`** quintuples yields **`min_d=3`** (`witness_min_d2_count=0`).
