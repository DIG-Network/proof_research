# Notes: adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n12

- **Host limit:** Standalone **`exists_tree`** for **`r=5`** and **`r=7`** hits **C(12,5)=C(12,7)=792** XOR splits on **1716** leaves; memoized recursion **RSS** exceeded cgroup and the kernel **SIGKILL**’d the process. **r=6** (**924** splits) completed in **<1 s** — non-monotonicity of memory vs split count likely comes from **partition geometry** (balance / branch factor), not just **menu size**.

- **Sharding:** Added **`--r-single`**, **`--union-rs`**, **`--baseline-only`**, **`--skip-baseline`** so each heavy DP runs in a **fresh process** and unions can be checked **without** first materializing **all** **`parts_by_r`**.

- **Union vs single-arity:** **`coord_plus_union_rs=[2,…,11]`** **`min_d=2`** is much cheaper than chaining **11** standalone DPs — the **rich** menu finds a **shallow** witness immediately.

- **Compare `n=11` `{5,6}` (100):** There **`r=5,6,7`** **plateaued** at **`min_d=3`** with **`r=8`** bump to **4**. Here **`r=6`** already **`2`**; **`r=11`** also **`2`**. **Pattern:** **threshold-adjacent** shells **`{t−1,t}`** **with** **`n=2t−2`** **(**here **12,7** **)** **may** **favor** **mid-high** **`r`** **(** **6** **)** **for** **cheap** **parity** **splits** **—** **speculative** **.**

- **Next:** If **standalone** **`min_d(5)`**/**`min_d(7)`** **matter** **for** **the** **BREAKTHROUGHS** **narrative** **,** **rerun** **on** **a** **machine** **with** **≥** **32 GiB** **RAM** **or** **port** **the** **DP** **to** **a** **bounded** **cache** **/** **disk-backed** **memo** **(** **not** **done** **here** **).**
