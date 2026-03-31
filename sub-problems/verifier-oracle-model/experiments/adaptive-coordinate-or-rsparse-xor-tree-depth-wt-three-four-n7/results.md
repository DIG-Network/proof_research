# Results — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-three-four-n7`

**Outcome:** PASS (measurements complete; one sub-hypothesis refuted)

**Domain:** `n=7`, participation masks with `popcount(x) ∈ {3,4}` (**70** masks). Majority threshold `t=4`, so **`n = 2t − 1`** (same complement/shell-swap regime as breakthrough **049**, but **mixed coord + r-XOR** trees).

## Measured `min_d` (adaptive, perfect leaf purity)

| Language | `#` extra XOR primitives | `min_d` |
|----------|--------------------------|--------|
| Coordinate only | 0 | **7** |
| Coord + full **7**-bit XOR | 1 | **1** |
| Coord + all **pair** XORs | C(7,2)=21 | **4** |
| Coord + all **triple** XORs | 35 | **3** |
| Coord + all **quad** XORs | 35 | **3** |
| Coord + **pair ∪ triple ∪ quad** | 21+35+35 | **2** |

## Reasoning

- **Odd `n`:** global **n**-bit parity separates **wt=3** (odd) from **wt=4** (even) in **one** query — **`min_d=1`** with that single gate (**092** pattern).
- **Arity ladder (pair → triple):** **`min_d` drops 4 → 3**, matching the qualitative **066→090** step on **`(10,{5,6})`** (there **5→4**).
- **Triple vs quad:** On this instance, **`r=3` and `r=4` tie at `min_d=3`** — raising primitive arity from 3 to 4 **does not** further reduce depth **when quad XORs are restricted to **4** of **7** coordinates** (none of the **35** quad splits is shell-pure by itself; depth-**2** fails for coord+quad-only).
- **Rich library:** Allowing **pair+triple+quad** together reaches **`min_d=2`**, analogous to **093** (**pentuple-only** reached **2** on the **462**-set without using full **n**-parity).

## Sub-hypothesis H2 (from `hypothesis.md`)

**Refuted:** **4-sparse XOR primitives are not** the same object as **full 7-bit parity**; **`coord+quad` does *not* achieve `min_d=1` here** (`min_d=3`).
