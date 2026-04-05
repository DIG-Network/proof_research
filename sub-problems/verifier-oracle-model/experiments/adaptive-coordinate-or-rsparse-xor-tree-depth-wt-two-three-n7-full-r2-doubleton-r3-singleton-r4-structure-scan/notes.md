# Notes

- **Observation:** Total depth-2 count **1225** equals singleton-grid **35×35** cell count but the **split** differs: here **1190** depth-2 cells have **distinct** triple indices `i<j`, not only diagonal duplication.
- **Contrast:** Singleton `r=3` + `r=4` grid had depth-2 **iff** quartic = complement of triple. This scan shows **two triple indices** + one quartic can still yield depth 2 for many non-diagonal pairs — the combinatorial certificate is strictly richer.
- **Next:** If we need a human-readable law, brute-force extract invariants for the **1190** off-diagonal `(i,j,k)` witnesses (e.g. bitmask relations between the two triples and the quad).
