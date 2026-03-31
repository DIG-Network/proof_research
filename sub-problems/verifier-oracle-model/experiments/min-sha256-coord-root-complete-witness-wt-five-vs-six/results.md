# Results — min SHA256 among **coordinate**-root + 067-subtree witnesses

## Outcome: **FAIL** (on **C1:** feasible coordinate roots)

## Repro

```text
python -u sub-problems/verifier-oracle-model/experiments/min-sha256-coord-root-complete-witness-wt-five-vs-six/script.py
```

Exit code: **1** (`NO_FEASIBLE_COORD_ROOT`).

## Measured quantities

| Quantity | Value |
|----------|--------|
| `feasible_coord_root_count` | **0** |
| `feasible_coord_roots` | **`[]`** |

## Reasoning

For **each** **`i` ∈ {0,…,9}`**, **`split_coord(full, i)`** **on** **the** **full** **wt∈{5,6}** **set** **(462** **masks)** **yields** **two** **non-empty** **sides** **(** **both** **shells** **mixed** **in** **general** **).** **Nevertheless** **for** **every** **`i`,** **`exists_tree(S0,** **4)** **`∧`** **`exists_tree(S1,** **4)`** **is** **false** **—** **no** **coordinate** **may** **be** **the** **root** **of** **a** **depth-≤5** **perfect** **separator** **tree** **in** **the** **same** **`exists_tree`** **semantics** **as** **066** **/** **067.**

**Hypothesis** **C1** **(** **`G`** **non-empty** **)** **is** **therefore** **false.** **C2** **(** **min-hash** **uniqueness** **within** **`G`** **)** **is** **vacuous.**

## Structural interpretation (**positive** **knowledge**)

**071** **scans** **45** **feasible** **XOR** **roots;** **072** **shows** **the** **parallel** **coordinate-root** **family** **is** **empty** **at** **d=5** **on** **this** **domain.** **This** **is** **consistent** **with** **067’s** **witness** **using** **pair-XOR** **at** **the** **top** **(** **not** **a** **coordinate** **)** **—** **the** **first** **successful** **root** **split** **cannot** **be** **pure** **coordinate** **here.**
