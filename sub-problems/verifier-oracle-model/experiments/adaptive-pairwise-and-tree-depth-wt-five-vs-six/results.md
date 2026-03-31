# Results: adaptive pairwise-AND tree depth (wt T−1 vs T)

## Outcome: **PASS**

## Summary

Exhaustive memoized backtracking computed the **minimum worst-case depth** of a **perfect** decision tree that separates `popcount(x) = T−1` from `popcount(x) = T`, when each internal node branches on **`x_i ∧ x_j`** for some `i < j`.

| (n, T) | Domain size | Min depth (pairwise AND) | Coordinate worst-case depth (045 pattern) |
|--------|---------------|---------------------------|-------------------------------------------|
| (5, 3) | 20            | **6**                     | **5** (= n)                               |
| (6, 4) | 35            | **6**                     | **6** (= n)                               |

## Interpretation

- **(6, 4):** Pairwise-AND trees require depth **n**, matching the coordinate-only barrier on this instance (no improvement from switching to these nonlinear probes).
- **(5, 3):** Pairwise-AND trees require depth **6 > n** — strictly **worse** than reading **n** coordinates in the worst case, because a single AND does not reveal a coordinate in isolation and the adaptive strategy pays an extra round on this toy.

The optimistic hypothesis that **non-coordinate** **pairwise** **AND** **queries** **strictly** **beat** **the** **045** **coordinate** **lower** **bound** **(depth** **<** **n−1** **for** **the** **(10,6)** **toy)** is **not** **supported**; on smaller **threshold** **toys** **it** **is** **flat** **or** **worse**. Exhaustive **(10,6)** **min-depth** **was** **not** **computed** **(search** **too** **large).**

## Reproducibility

```bash
python script.py
python script.py --n 6 --t 4
```
