# Notes — adaptive-coordinate-or-pair-or-tree-depth-wt-five-vs-six

## Bugs fixed en route

- **Initial** **`recurse_children`** **passed** **`depth_remaining`** **unchanged** **into** **children** **→** **infinite** **recursion** **/** **stack** **overflow.** **Must** **use** **`depth_remaining - 1`** **(** **match** **066** **).**

## Implementation

- **462-bit** **integer** **subsets** **instead** **of** **sorted** **mask** **tuples.**
- **Precomputed** **partition** **masks** **(** **per** **coordinate** **and** **per** **pair-OR** **):** **each** **split** **is** **two** **ANDs** **on** **462-bit** **ints** **—** **large** **speedup** **(** **d=6** **~8** **s** **vs** **~105** **s** **before** **).**

## Budget semantics

- **`--budget-seconds`:** **deadline** **checked** **before** **each** **new** **d.** **The** **currently** **running** **depth** **may** **run** **past** **budget** **until** **it** **finishes.**

## Resolution (2026-03-30)

- **Exhaustive** **DP:** **d** **=** **1..9** **infeasible** **(** **d=9** **~864** **s** **).**
- **Lift** **d=10:** **mixed** **⊇** **coordinate-only;** **045** **gives** **depth-10** **coord** **tree** **⇒** **min_d_mixed** **=** **10** **(** **OR** **offers** **no** **improvement** **over** **045** **here;** **contrast** **066** **XOR** **at** **5** **).**

## Next steps

- **Compare** **to** **049** **pure** **pair-OR** **on** **other** **shell** **pairs** **if** **needed.**
- **Optional:** **faster** **engine** **only** **if** **one** **wants** **a** **direct** **`exists_tree(full,10)=True`** **print** **from** **this** **binary** **(** **not** **required** **once** **045** **+** **monotonicity** **accepted** **).**
