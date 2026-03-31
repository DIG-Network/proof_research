# Notes

- **Sharding** **lesson** **:** **`exists_tree`** **LRU** **over** **`(bits,` `depth)`** **for** **`|domain|=1716`** **makes** **standalone** **`r=5`** **/** **`r=7`** **(** **792** **splits** **)** **feasible** **in** **~400s** **each** **when** **no** **other** **huge** **single-arity** **memo** **is** **resident** **—** **matches** **`disk-memo-microbench-exists-tree-n12`** **FAIL** **(** **disk** **per-state** **not** **the** **fix** **)** **;** **process** **isolation** **is** **.**

- **vs** **`(11,{5,6})`** **:** **Union** **`r≤5`** **still** **`min_d=3`** **(** **like** **100** **)** **;** **full** **union** **`min_d=2`** **.** **099-style** **`min_d(6),min_d(7)>min_d(5)`** **does** **not** **appear** **:** **here** **`min_d(6)=2`**, **`min_d(5)=min_d(7)=4`** **.**

- **H2** **(** **“prefix** **non-increasing”** **)** **:** **false** **—** **sequence** **`r=2..5`** **is** **`6,4,3,4`** **(** **uptick** **at** **`r=5`** **)** **.**
