# Notes

## Observation

The driver-level probe `n8/script.py --union-rs 2,3,4,5,6,7` reports `min_d=2` for the **full** weight-`{2,3}` shell with **246** XOR splits. This experiment grafts only the **new** arities (`r=5,6,7` full menus) onto the **sparse** `r2 + doubleton r3 + singleton r4` cell language used in the n=7 wedge grid.

## Dead end (for this combined certificate)

**Enriching the sparse cell with full `r=5,r=6,r=7` does not restore the n=7 wedge biconditional.** It instead makes `min_d=2` hold for **all** `107800` off-diagonal stratum cells, so `Q` no longer acts as a discriminant for depth-2 — the wedge predicate stays at **0** hits.

## Analogy

This resembles **overfitting a sufficient statistic**: adding enough instruments makes a feasibility event almost surely true, wiping out a sharp **if-and-only-if** characterization that depended on a **intermediate** proof-strength window.

## Next steps

- If the goal is a **non-vacuous** n=8 certificate, search for a **strict subset** of the `r=5..7` splits (or a different augmentation) that yields **some** but not **all** `min_d=2` witnesses on the stratum, then re-fit predicates.
- Alternatively, treat **n=8** wedge laws as requiring a **different** quartic–triple relationship than n=7 (as n=6 already signaled for the *sparse* menu).
