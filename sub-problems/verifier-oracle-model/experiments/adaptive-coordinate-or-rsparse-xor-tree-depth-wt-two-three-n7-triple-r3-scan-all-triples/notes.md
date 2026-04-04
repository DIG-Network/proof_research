# Notes — n=7 exhaustive three-triple scan

## Combinatorics

- **`C(35,3)=6545`** unordered triples of **`r=3`** XOR splits; each run **`min_depth_for_language`** with **`xor_lists = [p2, [p3[i], p3[j], p3[k]]]`**.

## Comparison

- **Two** triples: **595** cases, all **`min_d=3`** (**`…-n7-pair-r3-biconditional-scan-all-pairs`**).
- **Three** triples: **6545** cases, all **`min_d=3`** (this run).

## Next steps

- **Four** triples: **`C(35,4)=52,360`** — larger wall time; sample or shard if needed.
- Alternatively probe **partial** **`r=2..3`** unions (not full **`r=2`**) vs **`n=5`** minimal-split style.
- Cross-check whether **any** **`k`-subset** of **`r=3`** splits below the full **35** achieves **`min_d=2`** at **n=7** (subset lattice / minimal witness search).
