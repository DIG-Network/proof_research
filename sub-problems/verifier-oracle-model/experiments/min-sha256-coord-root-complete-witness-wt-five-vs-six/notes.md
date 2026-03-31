# Notes

- **Not** **a** **bug:** **`exists_tree`** **/** **`witness`** **match** **067** **(** **`recurse_children`** **passes** **`depth_remaining`** **into** **children** **).** **Re-ran** **with** **exit** **1** **and** **empty** **`feasible`** **list** **—** **exhaustive** **over** **10** **coordinates.**

- **Contrast** **071:** **XOR-root** **+** **067** **subtrees** **—** **45** **options;** **coord-root** **+** **same** **subtrees** **—** **0** **options** **at** **depth** **5** **for** **the** **full** **462-set.**

- **Implication** **for** **“union** **of** **root** **types”** **canonicalization:** **on** **this** **instance,** **any** **rule** **that** **only** **allows** **coordinate** **at** **the** **root** **has** **no** **valid** **witness** **at** **d≤5** **—** **the** **prover** **must** **use** **XOR** **(** **or** **deeper** **coord** **below** **a** **non-coord** **root** **).**

- **Optional** **follow-up:** **smaller** **|** **S** **|** **or** **d=6** **might** **admit** **coord** **roots;** **out** **of** **scope** **for** **this** **folder.**
