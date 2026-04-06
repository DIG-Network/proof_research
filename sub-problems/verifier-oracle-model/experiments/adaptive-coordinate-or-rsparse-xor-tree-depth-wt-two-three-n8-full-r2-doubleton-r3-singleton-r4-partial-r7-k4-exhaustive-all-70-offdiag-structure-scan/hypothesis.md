# Hypothesis

**Claim (falsifiable):** On the same `n=8`, shell `{2,3,4}`, off-diagonal stratum `s=|T_i∩T_j|∈{0,1,2}` grid, there exists **some** choice of **exactly four** distinct XOR splits from the full `r=7` menu (`K(8,7)=8` splits) such that, when appended to `coord + full r=2 + doubleton r=3 + singleton r=4`, the stratum satisfies **`0 < stratum_min_d2 < 107800`**.

**Rationale:** The prior experiment drew **16 random** `K=4` subsets (`SEED=0`) and saw **`stratum_min_d2=107800`** every time—consistent with universal saturation but **not** a proof over all **`C(8,4)=70`** menus. Exhaustion closes that finite envelope.

## Analogy pass

1. **Abstract structure:** Finite configuration space (`70` menus); monotone “resource” is inclusion of `r=7` splits; ask whether **any** interior point of the `K=4` slice escapes the two endpoints (`0` vs full saturation `107800`) seen at `K=0` and `K=8`.

2. **Analogous domains:**
   - **Finite-state reachability:** random walk may miss rare states; **BFS / enumeration** certifies existence.
   - **Coding theory:** minimum distance of a punctured code—**all** puncturing patterns vs one random pattern.
   - **Combinatorial thresholds:** `K`-uniform hypergraph properties—**first moment** vs **exhaustive** small universe.

3. **Machinery:** exhaustive search; inclusion–exclusion on support; design theory (covering all `4`-subsets).

4. **Seed:** Enumerate **`combinations(range(8), 4)`** (70 cases), reuse the same per-menu stratum scan as the random-trial script.

## Memory / prior context (brief)

- Parent random probe: **`…-partial-r7-k4-random-trials-16-offdiag-structure-scan`** — **FAIL**, all 16 trials **`stratum_min_d2=107800`**.
- Full `r∈{5,6,7}` menus: immediate **`107800`** saturation (**strict-subset scan**).

This experiment is the **finite completion** of the **`K=4`** partial-`r=7` story at `n=8` for this grid.
