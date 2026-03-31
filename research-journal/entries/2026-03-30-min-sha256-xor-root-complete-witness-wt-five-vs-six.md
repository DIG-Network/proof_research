# 2026-03-30 — min-sha256-xor-root-complete-witness-wt-five-vs-six

- **Experiment:** `sub-problems/verifier-oracle-model/experiments/min-sha256-xor-root-complete-witness-wt-five-vs-six/`
- **Context:** verifier-oracle-model (**canonical** **`π_tree`** **after** **070** **multiplicity**).

## Hypothesis tested

**Among** **45** **feasible** **pair-XOR** **roots** **with** **067** **`witness`** **on** **children** **(** **d=5** **),** **exactly** **one** **(** **i,j** **)** **minimizes** **`sha256(json)`** **(** **canonical** **dump** **).**

## Outcome: **PASS**

**`minimizer_count=1`,** **winner** **(6,7).** **`min_sha256`** **≠** **`sha256`** **of** **067** **default** **witness** **(** **first-success** **tree** **).**

## Key finding

**A** **public** **min-digest** **tie-break** **over** **this** **finite** **family** **is** **well-defined** **and** **unique** **here** **—** **but** **it** **does** **not** **reproduce** **067’s** **witness** **(** **different** **optimal** **root** **).**

## Implications

- **Binding** **rules** **must** **be** **specified** **in** **the** **protocol** **;** **“the”** **mixed** **tree** **is** **not** **implicit.**
- **Further** **work** **if** **needed:** **widen** **the** **enumerated** **family** **(** **coord** **roots,** **deeper** **tie** **variants** **)** **—** **cost** **may** **explode.**

## Analogy pass summary

**Symmetry** **breaking** **via** **minimal** **hash** **(** **consensus** **/** **canonical** **Merkle** **)** **—** **applied;** **uniqueness** **holds** **on** **stated** **family.**
