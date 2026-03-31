# 2026-03-30 — min-sha256-coord-root-complete-witness-wt-five-vs-six

- **Experiment:** `sub-problems/verifier-oracle-model/experiments/min-sha256-coord-root-complete-witness-wt-five-vs-six/`
- **Context:** verifier-oracle-model (**mirror** **071** **for** **coordinate** **roots** **—** **digest** **“wider** **families”** **).**

## Hypothesis tested

**C1:** **At** **least** **one** **coordinate** **`x_i`** **at** **the** **root** **of** **the** **full** **462-set** **admits** **`exists_tree`** **on** **both** **children** **with** **depth** **budget** **4** **(** **overall** **d≤5** **).** **C2** **would** **then** **study** **min** **SHA256** **over** **that** **family.**

## Outcome: **FAIL** **(** **C1** **)**

**`feasible_coord_root_count=0`** **for** **all** **`i`∈{0,…,9}.`**

## Key finding

**No** **coordinate-only** **root** **split** **is** **compatible** **with** **a** **depth-5** **066-style** **tree** **on** **(** **n=10,** **wt{5,6}** **)** **—** **whereas** **45** **XOR** **roots** **work** **(** **071** **).** **So** **the** **“coord-root** **+** **067** **subtree”** **slice** **of** **the** **design** **space** **is** **empty** **here.**

## Implications

- **Canonical** **min-hash** **over** **“XOR** **or** **coord** **root”** **collapses** **to** **the** **XOR-only** **family** **at** **this** **(** **n,d** **)** **point** **(** **coord** **branch** **vacuous** **).**
- **067** **/** **070** **/** **071** **behavior** **(** **XOR** **at** **top** **)** **is** **forced** **by** **feasibility,** **not** **only** **by** **tie-break.**

## Analogy pass summary

**Feature** **families** **in** **ML** **/** **syntax** **variants** **—** **tested** **second** **root** **type;** **family** **empty** **(** **structural** **obstruction** **).**
