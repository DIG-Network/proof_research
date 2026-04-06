# Notes

- **Strong saturation at K=4:** Even though full `r=7` uses **8** XOR splits, **4** randomly chosen splits (seed **0**, **16** trials) still yielded **`107800/107800`** `min_d=2` every time. This suggests the DP language is **highly redundant** at arity **7**: a **small** fraction of splits may already encode enough parity constraints to deepen **every** coarse cell on this stratum.

- **Wedge diagnostic unchanged:** **`stratum_pred=0`** throughout — quartics vs **3-set** wedges; the partial-`r7` enrichment does not revive the n=7-style wedge biconditional on this grid.

- **Next probes:** (1) **Lower** **`K`** (**1–3**) with the same random or structured sampling. (2) **Exhaust** all **`C(8,4)=70`** `r=7` submenus (bounded, ~**70×~15s** if wall scales linearly). (3) Partial menus at **`r=5`** or **`r=6`** where **full** menus already saturate—test whether **strict subsets** of splits can avoid universal `min_d=2`.
