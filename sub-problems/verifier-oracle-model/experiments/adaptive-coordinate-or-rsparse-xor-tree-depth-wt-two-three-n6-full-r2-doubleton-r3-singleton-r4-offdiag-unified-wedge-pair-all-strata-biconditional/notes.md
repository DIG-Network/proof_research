# Notes — n=6 unified wedge pair (FAIL)

- **Structural obstruction:** For **`N=6`**, triples are **3-subsets**. For **`i<j`**, **`|T_i∪T_j| ≥ 4`** with equality iff **`|T_i∩T_j|=2`**. Then **`|[N]\(T_i∪T_j)| = 2`** when **`s=0`**, **`1`** when **`s=1`**, and **`1`** when **`s=2`** — in all cases **`W_ij=(T_i\T_j)∪exterior`** has **`|W_ij|≤3`**, never **4**. So no quartic **`Q`** can equal **`W_ij`** or **`W_ji`**; the predicate is **unsatisfiable** on the datatype.

- **Why n=7 differed:** For **`N=7`**, when **`s=2`**, **`|union|=5`** and **`|exterior|=2`**, so **`|W_ij|=|T_i\T_j|+|exterior|=1+2=4`**, and quartic equality is **possible**. The **`n=6`** scan shows a stronger phenomenon: **`min_d=2`** is **universal** on the **`2850`** stratum cells (language is so coarse that depth **2** is always feasible), decoupling depth from **4-set** geometry.

- **Next:** If we want an **`n=6`** analogue of the **n=7** wedge story, we need either a **different mask weight** in the predicate (e.g. characterize **`min_d=2`** via **3-sets** or **mixed** certificates) or a **richer XOR menu** where depth-**2** witnesses are **not** ubiquitous.
