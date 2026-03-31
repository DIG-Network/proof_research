# Analogy pass

## 1. Abstract structure

Adaptive **`exists_tree`**: two constant Hamming shells in **`{0,1}^n`**, internal nodes coordinate or one **r-sparse** **F₂** XOR from a library.

## 2. Analogues (≥3)

1. **`(10,{5,6})`** **(** **066** **/** **091** **/** **093** **)** **—** **canonical** **462** **-mask** **row** **.**
2. **`(9,{4,5})`** **(** **097** **)** **—** **full** **`r=2..8`** **`min_d(r)`** **scan** **on** **252** **masks** **.**
3. **096** **`(8,{4,5})`** **—** **non-monotone** **`r`** **profile** **.**

## 3. Machinery

Same **DP** as `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-four-five-n9/script.py`, domain **`C(9,5) ∪ C(9,6)`** (210 masks).

## 4. Transfer seed

Fix shells **`{5,6}`** as in **`(10,{5,6})`** but **`n=9`**, for a full **`r`** sweep with the same parity pattern (wt 5 odd vs wt 6 even ⇒ full **n**-XOR still **`min_d=1`**). **Note:** for **`n=9`**, **`t=5`**, both shells are quorum-sized; the toy is “separate wt 5 vs 6”, not the **`t−1` vs `t`** slice for that **`n`**.

---

# Formal hypothesis

**H1:** Coord + full 9-bit XOR has **`min_d=1`** (odd vs even).

**H2:** Exhaustive **`min_d(r)`** for **`r=2..8`** is computed and compared qualitatively to **`(10,{5,6})`** (pair 5, triple 4, quad 3, pentuple 2, etc.).

**Falsification:** DP failure or timeout.

---

# Outcome (post-run)

**PASS.** Coord-only **`min_d=9`**; coord + full 9-XOR **`min_d=1`**. **`min_d(r)`:** `2→5`, `{3,4,5,7}→3`, `6→4`, `8→2`. Unions: `r∈{2,3,4}→3`, `r≤5` and `r≤8` both `→2`. Triple/quad/pentuple plateau at depth 3 (no strict 066→093 ladder on 210 masks). See `results.md`.
