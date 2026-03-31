# Notes

- Counting is **idealized** (each `H_leaf` / `H_node` = one unit); real code may batch or use different trees.
- **Main problem** demands **sublinear `|π|`**; even if a future primitive shrinks **`π`**, **standard compute** may still bottleneck if verification must touch **Ω(n)** or **Ω(n log n)** objects unless a novel **`Link`** avoids per-signer path checks entirely.
- Aligns with **`verifier-oracle-model`** deliverable: separate **communication** (**012**) from **local work** (this script).
