# Notes

- **Localization:** Same **25** XOR splits as **`{2,3}+r2..4`**, but **`min_d` drops from 2 → 1** when masks are restricted to **weight 2 only** ⇒ the **mask shell expansion** is the active degree of freedom for the depth bump (not **r=4** alone).
- **Contrast:** Pair with **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5-full-r2-r3-union-min-d`** (**`{2}`**, **`r=2..3`**, **`min_d=1`**) and **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n5-full-r2-r4-union-min-d`** (**`{2,3}`**, **`r=2..4`**, **`min_d=2`**).
- **Next (optional):** **`{2,3}`** shell but union **`r=2..3` only** — check whether **`min_d` is already 2** or still **1**, to see if **weight-3 masks** require **`r=4`** in the union to trigger depth 2.
