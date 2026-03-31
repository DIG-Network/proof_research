# Results — petersen-sixset-laplacian-spectrum-collision

## Outcome: **PASS**

## Host graph

- **Petersen** on **10** vertices: **3-regular**, **15** edges (standard outer pentagon + inner pentagram + spokes).

## Quorum parameter

- Strict majority **t = ⌊10/2⌋ + 1 = 6**; both witnesses are **|S| = 6**.

## Collision

Two **distinct** **6**-subsets:

- **S₁ = {0,1,2,3,4,5}** (all outer cycle vertices plus inner **5** — spoke partner of outer **0**)
- **S₂ = {0,1,2,3,4,6}** (same outer five plus inner **6** — spoke partner of outer **1**)

share the **same** **sorted** **Laplacian** eigenvalues of the **induced** subgraph (to **8** decimal places after `numpy.linalg.eigvalsh`):

`[0, 0.69722436, 1.38196601, 2, 3.61803399, 4.30277564]` (leading **0** is numerical **−0**).

## Conclusion

Even the **full** **6**-vector Laplacian spectrum of **G[S]** (not merely **λ_max** and **λ_min**) **does not** distinguish these two **quorum-sized** coalitions on this **expander** host. Extends the spectral **alias** thread (**025**–**029**) to **complete** induced Laplacian spectrum on a **3-regular** **Petersen** toy.

## Repro

```bash
python script.py
```
