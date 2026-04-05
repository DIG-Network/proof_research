# Notes — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-full-r2-r3-plus-each-r4-split-once`

## observation

The prior `union {2,3}` vs `{2,4}`-only comparison showed both **56-split** unions have `min_d=3`, while **`{2,3,4}`** with **91** splits has `min_d=2`. That suggested **overlap** of **arity menus** might be essential. Here, **57** splits (**full `r=2`+`r=3` + one `r=4`**) universally hits **`min_d=2`**, so **arity-4 content** can be **extremely** **sparse** if **all** **`r=3`** **XOR** **splits** are already present.

## dead_end

The **specific** **primary** claim in the first draft hypothesis (“no single `r=4` direction lowers `min_d`”) is a **dead end** as stated — it is **false** for **every** quartic index.

## insight

**Quartic vs triple ladder:** **Seven** extra **`r=3`** parities on **`r=2`** never reached `min_d=2` (exhaustive septuple scan). **One** extra **`r=4`** parity on **`r=2`+`r=3`** **always** reaches `min_d=2`. So at this slice, **moving from triple-XOR to quartic-XOR** is a **sharp** **phase change** for **`min_d`**, not a smooth “add more of the same arity” story.

## question

Is there a **clean combinatorial certificate** explaining why **any** `r=4` XOR split completes depth-2 **given** the full **`r=3`** menu (e.g. relation to **majority** **threshold** **`t=4`** on **`n=7`**)?

## next steps

- Optional: **minimal** **`r=3`** **submenu** **+** **one** **`r=4`** (combinatorial search) to see how small **`|r=3|`** can be before **`r=4`** **stops** **forcing** **`min_d=2`**.
- Keep **`r=3`** **ladder** **results** **as** **negative** **evidence** **for** **“triple-only”** **sparse** **extensions** **;** **use** **this** **experiment** **as** **positive** **evidence** **for** **`r=4`** **as** **the** **right** **arity** **knob** **post-** **`r=3`** **saturation**.
