# Hypothesis

**Claim:** For **`n=14`**, **`|S| ∈ {7,8}`**, **coord + r-sparse XOR** with **`r ∈ {2,3,4}`** only, **`min_d > 2`** — i.e. depth **`d=2`** is **infeasible** for each single-arity menu, matching the **`n=13`** resolved row where low-**`r`** values still require **`d ≥ 3`**.

**Falsification:** Any run with **`--d-min 2 --d-max 2`** returns **`d=2 feasible=True`** for **`r=2`**, **`r=3`**, or **`r=4`**.

## Analogy pass

1. **Abstract structure:** Adaptive decision trees over a finite mask alphabet; each internal node applies a binary split from a fixed gate library; **`min_d`** is the shallowest depth separating two Hamming-shell classes. Low-**`r`** XOR splits are **coarse** on the shell pair — they leave **mixed** weight on both sides longer than high-**`r`** refinements.

2. **Analogous domains:** (a) **Property testing** — few random parity checks rarely separate a high-threshold set from its complement; (b) **Group testing** — tests that XOR many items have low **separating power** until arity matches structure; (c) **Decision tree lower bounds** — shallow trees need **informative** splits; uninformative splits force depth to grow.

3. **Machinery in those domains:** Fourier concentration of Boolean functions; test design matrices; **block sensitivity** / **certificate complexity** style arguments (here empirical **`exists_tree`** DP).

4. **Transfer seed:** Treat **low-**`r`** sparse XOR** as **weak measurements** on **`{7,8}`** masks; expect **`d=2`** to fail (as on **`n=13`**) before attempting heavy **`d=3`** probes for **`r=5,9`**.

## Memory / prior context (lightweight)

Parent track: **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n14`** — **`r=5`**, **`d=2`** already **ruled out**; **`r∈{2,3,4}`** previously **timed out** on full **`min_d`** sweeps, not on a **d=2-only** shard with **unbounded** memo.
