# Results: off-diagonal `min_d=2` vs symmetric-difference predicate

**Outcome:** FAIL (hypothesis falsified; biconditional does not hold)

## What was tested

Full **`22050`**-cell grid: `coord` + **full** `r=2` + **two** `r=3` XOR splits `(i,j)` with `i≤j` + **one** `r=4` split `k`.

**Hypothesis**

- **Diagonal** `i=j`: `min_d=2` iff `Q` is the complement of `T_i` (singleton `3+4` law — expected true).
- **Off-diagonal** `i<j`: `min_d=2` iff `|T_i∩T_j|=1` and `Q = T_i △ T_j`.

## Findings

- **Counts reproduced:** `min_d=2` on **`1225`** cells (**`35`** diagonal, **`1190`** off-diagonal); **`wall_sec≈31.3`**, **`4M`** LRU.
- **Diagonal:** no violations of the complement law in this run (consistent with prior singleton iff check).
- **Off-diagonal:** the symmetric-difference story is **false** in multiple independent ways:
  1. **Many** `min_d=2` witnesses have **`|T_i∩T_j|=2`**, not `1` (e.g. `T_i=(0,1,2)`, `T_j=(0,1,3)`, `Q=(2,4,5,6)`).
  2. **Many** `min_d=2` witnesses with **`|T_i∩T_j|=1`** have **`Q ≠ T_i△T_j`** (e.g. `T_i=(0,1,2)`, `T_j=(0,3,4)`, `Q=(1,2,5,6)` while `T_i△T_j` is a different 4-set).
  3. **Converse fails:** **`315`** off-diagonal cells** satisfy `|T_i∩T_j|=1` and `Q=T_i△T_j` but have **`min_d=3`** (first examples include `i=0,j=9,k=20`, etc.).

So **`Q=T_i△T_j`** is **neither necessary nor sufficient** for `min_d=2` in this doubleton-triple + singleton-quartic menu.

## Implication

The **`1190`** off-diagonal depth-2 cells are **not** explained by the same “linear set law” as the singleton complement case; any closed predicate must allow **`|T_i∩T_j|∈{1,2}`** regimes and **ordered** roles of the two triple indices (lex order `(i,j)` is not symmetric in the witness set).

## Follow-up (not run here)

Empirically, for **`|T_i∩T_j|=2`** the witness `Q=(2,4,5,6)` above matches **`Q = (T_i \ T_j) ∪ ([7] \ (T_i ∪ T_j))`** for the **lex-ordered** pair `(i<j)`. Worth a separate experiment if we want a refined patchwork predicate.
