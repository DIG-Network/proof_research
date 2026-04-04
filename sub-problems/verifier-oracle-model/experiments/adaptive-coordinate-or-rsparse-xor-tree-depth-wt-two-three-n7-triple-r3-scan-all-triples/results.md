# Results — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-triple-r3-scan-all-triples`

**Outcome:** FAIL

**Setup:** **n=7**, shell **`{2,3}`**, language **coord + full `r=2` XOR menu + exactly three `r=3` XOR splits** (unordered triple of triple indices). **LRU** cap **`4_000_000`**. Exhaustive **`C(35,3)=6545`** triples.

**Baselines:** `coord_only` **`min_d=7`**; **`coord + full n-XOR`** **`min_d=1`** (sanity).

**Measured:**

| Quantity | Value |
|----------|-------|
| `triples_checked` | 6545 |
| `wall_sec` | ~18.08 |
| `witness_min_d2_count` | **0** |

**Interpretation:**

- **No** unordered triple of **`r=3`** parities, together with the full **`r=2`** menu and per-coordinate splits, yields a depth-**2** certificate on this shell at **n=7** — **`min_d=3`** persists uniformly for this **3-triple** sparse slice.
- This strengthens the **n=7** picture beyond the **two-triple** exhaustive scan (**595/595** pairs, **`witness_min_d2_count=0`**): adding a **third** triple-XOR split **does not** unlock **`min_d=2`** anywhere in the **`C(35,3)`** universe.

**Conclusion:** Hypothesis **falsified** — **three** fixed triple-XOR splits **do not** restore **`min_d=2`** at **n=7** on **`{2,3}`** in this DP model; next probes likely need **more** **`r=3`** splits, **higher** arity **XOR**, or a **different** language than **coord + full `r=2` + sparse `r=3`**.
