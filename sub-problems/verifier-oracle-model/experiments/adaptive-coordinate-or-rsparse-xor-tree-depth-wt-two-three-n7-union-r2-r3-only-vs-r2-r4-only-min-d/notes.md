# Notes — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-union-r2-r3-only-vs-r2-r4-only-min-d`

- **observation:** **Symmetric** **`min_d=3`** **for** **`{2,3}`** **and** **`{2,4}`** **only** **—** **same** **split** **count** **`56`** **,** **different** **parity** **families** **,** **same** **depth** **.**

- **insight:** **The** **`{2,3,4}`** **depth-** **`2`** **witness** **is** **genuinely** **multi-arity** **:** **it** **is** **not** **“** **add** **`r=4`** **to** **fix** **triple-ladder** **failure** **”** **alone** **(** **`r=2+r=4`** **still** **`min_d=3`** **)** **,** **nor** **“** **full** **`r=3`** **already** **enough** **”** **(** **`r=2+r=3`** **is** **`min_d=3`** **here** **at** **`n=7`** **)** **.**

- **question:** **Is** **there** **a** **smaller** **than** **full** **cross-product** **subset** **of** **`r=3`** **and** **`r=4`** **splits** **that** **still** **achieves** **`min_d=2`** **(** **beyond** **the** **negative** **sparse-triple** **ladder** **)** **?**

- **dead_end** **(** **for** **this** **exact** **pair** **of** **menus** **)** **:** **Neither** **`union-rs=2,3`** **nor** **`union-rs=2,4`** **alone** **is** **a** **depth-** **`2`** **language** **on** **this** **shell** **.**
