# Notes — patchwork `inter012` template

- The **ordered wedge** for `|∩|=2` was suggested after the pure **symdiff** law failed; this run shows **even with case-splitting by `s`**, the **quartic label** is **not** determined by **`(T_i,T_j,s)`** alone for **`min_d=2`**.
- **Complement-of-symdiff** pattern: several **`min_d=2`** witnesses with **`|∩|=2`** have **`Q = [7] \ (T_i △ T_j)`** (e.g. `Q=(3,4,5,6)` for `T_i=(0,1,2)`, `T_j=(0,1,3)` where `T_i△T_j={2,3}`). The patchwork expected **`(T_i\T_j)∪exterior`** which is **not** that complement in general — so **two natural 4-sets** compete in the **`|∩|=2`** stratum.
- **False positives** (`pred`, `md≥3`) show the patchwork masks are **too permissive**: mask equality **does not imply** DP feasibility.
- **Next angles:** (1) try **`Q = complement(T_i △ T_j)`** as a third branch when `s=2` (or disjunction of wedge vs complement-symdiff); (2) admit **`k`** in the predicate (quartic index matters, not just **`Q`** as a set — but that trivializes classification); (3) abandon closed **set formulas** and search **short DNF** over a richer atom family (parity bits on **`Q`** vs **`T_i,T_j`**).
