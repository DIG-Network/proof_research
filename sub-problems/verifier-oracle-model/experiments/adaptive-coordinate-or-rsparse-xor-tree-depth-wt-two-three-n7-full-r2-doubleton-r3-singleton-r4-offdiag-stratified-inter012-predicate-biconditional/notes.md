# Notes — experiment 163

## Observation

- Totals **`1190 = 770 + 420`** match **`s01` depth-2 count** (experiment **162**) plus **`s=2` depth-2 count** (experiment **159** structure scan).
- Predicate hits **`980 = 770 + 210`**: all **`s01`** depth-2 cells are captured by **`W_ij ∨ W_ji`**; on **`s=2`**, only **`210`** of **`420`** depth-2 cells hit **`W_ij ∨ C_ij`**.
- **Zero** false positives (`pred` with `md≠2`): the stratified predicate is **sound** but **incomplete** on **`s=2`**.

## Dead end (for this exact template)

- **Patchwork:** `s∈{0,1}` → `W∨W_rev`; `s=2` → `W∨C` **only** (no **`W_ji`**) — **fails** globally (**210** **`min_d=2`** witnesses missed).

## Insight

- Printed violations show **`Qbits == Wji`** while **`strat_pred=False`**: the fix for a unified template likely requires **symmetrizing the `s=2` chart** to **`{W_ij, W_ji, C_ij}`** (or proving a smaller symmetric envelope). Expect **`|pred|`** would jump by **`210`** to **`1190`** if **`W_ji`** is added on **`s=2`**, matching **`|min_d=2|`** — **next experiment**.

## Question

- Does **`min_d=2` ⇔ Q ∈ {W_ij, W_ji, C_ij}`** hold on the full **`s=2`** stratum (**7350** cells)? If yes, the global law may be: **always** **`W_ij ∨ W_ji`**, and on **`s=2`** **also** allow **`C_ij`** (equivalently **three** charts on **`s=2`**, two redundant with wedge pair for some cells).
