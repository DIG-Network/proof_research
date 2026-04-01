# Notes

- **Parent footgun:** `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14/script.py` prints **`PASS`** whenever **`--skip-baseline`** and **`r_single`** return **exit 0**, even if **`d=3 feasible=False`** and **`min_d=None`** within the probed range. This wrapper treats **`feasible=False`** as **FAIL** (**exit 1**) so journal semantics stay aligned with **hypothesis** outcome.
- **Interpretation:** **`r=11`** sits **between** an **`r=7`** **`d=3`** **yes** and **`r=12` `d=3`** **yes**, but is **not** “ **`d=3`** **yes** **with** **more** **time** ” — it is ** **`d=3`** **no** **for** **this** **language** **.**
