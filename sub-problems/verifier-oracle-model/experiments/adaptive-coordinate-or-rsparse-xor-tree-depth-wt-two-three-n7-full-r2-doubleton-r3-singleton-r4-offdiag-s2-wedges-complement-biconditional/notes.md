# Notes — `s=2` wedges ∪ complement (vacuous `C`)

## observation

Exhaustive scan: **`0`** violations both ways on **`7350`** **`s=2`** cells; runtime **`~30.2`** s with **`4M`** LRU.

## insight

**`C_ij`** is **not** a **4-subset** when **`|T_i ∩ T_j| = 2`**: symmetric difference has size **`2`**, so **`|C_ij| = 7 - 2 = 5`**. The **`pred_c=0`** counter is structural, not empirical luck.

## analogy

This is the same **orientation** phenomenon as **ordered vs symmetrized cuts**: the **`s=2`** failure mode in **163** was **missing one wedge orientation**; adding **`W_ji`** closes the **`210`** gap without changing **`s∈{0,1}`** law.

## question

Does the **global** off-diagonal biconditional hold if **`s∈{0,1}`** uses **`W∨W_rev`** (experiment **162**) and **`s=2`** uses **`W∨W_rev`** only (**`C`** redundant)? Next experiment: full **20825** off-diagonal grid with **two-stratum** predicate.
