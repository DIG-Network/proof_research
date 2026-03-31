# 2026-03-30 — adaptive-coordinate-or-rsparse-xor-tree-depth-wt-five-six-n10

**Context:** `sub-problems/verifier-oracle-model`  
**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-five-six-n10/`

## Hypothesis tested

Full **`min_d(r)`** sweep **`r=2..9`** on canonical **`(10,{5,6})`** (462 masks), same DP as **097**/**098**, to unify **066/090/091/093** and test monotonicity beyond **`r=5`**.

## Outcome

**PASS**

## Key finding

- **`r=2..5`:** **5,4,3,2** — matches prior spot experiments.
- **`min_d(r)`** **not** **monotone:** **`r=6→3`**, **`r=7→4`** **>** **`min_d(5)=2`**. **`r=8→3`**, **`r=9→2`**.
- **Unions:** **`r∈{2,3,4}→3`**, **`r≤5`** **and** **`r≤9`** **`→2`**.

## Implications

- **099** **/** **BREAKTHROUGHS:** **096**’s contrast with “strict ladder on (10,{5,6})” was **incomplete** — full sweep shows **interior** **arity** **regression** **on** **that** **row** **too** **.**
- **Unions** **including** **`r=5`** **still** **achieve** **`min_d=2`** **—** **bad** **`r=6,7`** **menus** **matter** **only** **for** **single-arity** **restrictions** **.**

## Analogy pass summary

Unified **coding-theoretic** **“syndrome** **arity”** **axis** **with** **prior** **066→093** **ladder** **;** **cross-linked** **098** **`(9,{5,6})`** **and** **096** **`(8,{4,5})`** **non-monotonicity** **.**

## Invented space

None.
