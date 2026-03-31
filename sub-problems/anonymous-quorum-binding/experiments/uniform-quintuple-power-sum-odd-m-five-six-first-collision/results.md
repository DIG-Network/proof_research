# Results — quintuple power sums, first collision at odd M only

**Outcome:** PASS

**Setup:** Same as **076** (`w_i=i+1`, `n=10`, `S_k` for `k=1..5`), but scan only **odd** `M ≥ 3` (skip even `M` and thus the mod-2 collapse mechanism).

**Finding:** `FIRST_ODD_COLLISION_M = 3` with `mod_key = (0, 1, 0, 1, 0)`.

**Witness:** Same index sets as **075/076**: five-set `(4,6,7,8,9)` (weights 5,7,8,9,10), six-set `(0..5)` (weights 1..6). Raw quintuples unchanged from **076**; congruences mod **3** match across shells for all five coordinates.

**Takeaway:** Escaping **M=2** does not force a large modulus: the **first odd** modulus already yields a **5-vs-6** collision on the full **5**-tuple, and the **same** pair that witnessed **M=2** works at **M=3**.
