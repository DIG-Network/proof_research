# Results — n=6 unified off-diagonal wedge pair biconditional

**Outcome:** **FAIL**

**Command:**

```bash
python3 sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n6-full-r2-doubleton-r3-singleton-r4-offdiag-unified-wedge-pair-all-strata-biconditional/script.py
```

**Measured:**

| Metric | Value |
|--------|-------|
| Full grid cells (i≤j, all k) | **3150** |
| Off-diagonal stratum cells (`i<j`, `s=\|T_i∩T_j\|∈{0,1,2}`) | **2850** |
| Stratum `s0` / `s1` / `s2` counts | **150** / **1350** / **1350** |
| Stratum with `min_d=2` | **2850** (all) |
| Predicate hits `Q∈{W_ij,W_ji}` | **0** |
| Violations `d2 ∧ ¬pred` | **2850** |
| Violations `pred ∧ md≠2` | **0** |
| Wall time | **≈0.77 s** |
| LRU cap | **4_000_000** |

**Reasoning:** The n=7 certificate (**`…-offdiag-unified-wedge-pair-all-strata-biconditional`**) does **not** port to **`n=6`** on the same language shape. Here **`min_d=2` holds for every** off-diagonal **`(T_i,T_j,Q)`** triple in the scan, while **`W_ij` and `W_ji` are always 3-bit masks** (for `s∈{0,1,2}` the exterior **`[6]\(T_i∪T_j)`** has size **`6-5=1`** when **`s=2`**, and similarly for other strata the wedge is never a 4-set). **Quartics `Q` are 4-bit masks**, so **`Q=W_ij` is impossible** — the biconditional fails uniformly (false negatives only).

**Implication:** Any verifier-facing predicate for this **`n=6`** menu must use **different** certificates than the n=7 **ordered-wedge-on-quartic** characterization; **`n`** is not a benign parameter for this closed form.
