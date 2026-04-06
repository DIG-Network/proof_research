# Hypothesis

**Claim (falsifiable):** On the `n=8`, shell `{2,3,4}`, off-diagonal stratum `s=|T_i∩T_j|∈{0,1,2}` grid (same cell geometry as the n=8 wedge ports), there exists a **strict** nonempty subset of the **full** XOR menus at arities `r∈{5,6,7}` such that the induced language yields a **nonempty proper** subset of stratum cells with `min_d=2` — i.e. `0 < stratum_min_d2 < 107800`.

**Rationale:** The sparse baseline has `stratum_min_d2=0` (vacuous PASS for the wedge biconditional). Appending **all** of `r=5,6,7` makes `stratum_min_d2=107800` (universal depth-2, wedge FAIL). If the transition is **monotone** in menu strength, some **minimal** enrichment might land in the intermediate regime where a nontrivial certificate family could still be sought.

## Analogy pass

1. **Abstract structure:** A family of decision problems (depth of a fixed DP search tree) parameterized by a nested set of available “measurement” operations (XOR split menus). Adding operations can only **shrink** the minimal depth certificate set in this model; the question is whether the **first** crossing from “no depth-2 witnesses” to “all witnesses” happens in one jump or through a **partial** witness set.

2. **Analogous domains:**
   - **Percolation / phase transitions:** As bond probability increases, an infinite cluster may appear abruptly (first-order) or grow continuously — the **window** of coexistence of two phases matters for intermediate statistics.
   - **Constraint satisfaction:** Adding clauses moves the satisfiable region; **minimal unsatisfiable cores** capture the first obstruction — here, “which arity menu first forces depth-2 everywhere?”
   - **Matroid rank / span:** Adding generators can increase rank stepwise; the **rank gap** between “span is empty of a property” and “span is everything” can be nontrivial unless one generator already spans.

3. **Machinery in those domains:** Critical exponents and scaling windows; MUS extraction; matroid circuit/cocircuit duality.

4. **Seed for this experiment:** Treat `{r5,r6,r7}` as three independent **switches** and **exhaust** strict subsets (6 masks). This is the discrete analogue of “scan the boundary between sparse and saturated menus” without assuming continuity.

## Memory / prior context (brief)

- n=8 sparse wedge port: `stratum_min_d2=0`, vacuous PASS.
- n=8 + full `r5,r6,r7`: `stratum_min_d2=107800`, wedge biconditional FAIL.

This experiment does **not** presuppose the wedge law; it only tests the **cardinality** of the `min_d=2` stratum under partial high-arity menus.
