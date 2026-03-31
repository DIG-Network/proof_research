# Journal entry: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n13 (baseline)

**Date:** 2026-03-31  
**Experiment:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n13`  
**Context:** verifier-oracle-model  

## Hypothesis tested

**H1:** Coord-only **min_d = 13**; coord + full **13-XOR** **min_d = 1**.  
**H2/H3:** Deferred — full **`min_d(r)`** **/** **unions** **not** **run** **this** **session** **.

## Outcome: PASS (baseline)

**Coord-only** **`min_d=13`** **(** **3003-mask** **domain** **)** **.** **Coord** **+** **full** **13-XOR** **`min_d=1`** **.** **Wall** **time** **~31** **s** **for** **`--baseline-only`** **on** **this** **host** **.

## Key finding

The **n=13**, **{7,8}** slice **inherits** **the** **same** **qualitative** **baseline** **as** **smaller** **majority** **slices** **:** **coordinates** **need** **full** **depth** **;** **global** **parity** **(** **full** **`n`****-XOR** **)** **separates** **the** **two** **shells** **in** **one** **split** **.

## Implications

- **Proceed** **with** **sharded** **`--r-single`** **runs** **for** **`r=2..12`** **when** **compute** **budget** **allows** **;** **expect** **larger** **build** **/** **DP** **cost** **than** **`n=12`** **for** **mid** **`r`** **.

## Analogy pass summary

Scaled **(12,{6,7})** **machinery** **to** **(13,{7,8})** **;** **parity** **lemma** **predicts** **`min_d_full=1`** **.
