# Results — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-union-r2-r3-only-vs-r2-r4-only-min-d`

**Outcome:** **PASS** (primary hypothesis confirmed).

**Measured:**

| Case | `union_rs` | `total_splits` | `min_d` | `dp_sec` |
|------|------------|----------------|---------|----------|
| A | `2,3` | `56` | `3` | `0.003611` |
| B | `2,4` | `56` | `3` | `0.002447` |

**Baseline:** `coord_only min_d=7`, `coord_plus_full_xor min_d=1` (sanity).

**LRU:** `4_000_000`.

**Reasoning:**

- **Primary:** **coord + full `r∈{2,3}`** only (**`56`** splits **)** has **`min_d=3`**, so **omitting the full **`r=4`** XOR menu** **restores** the **depth-** **`3`** **barrier** **relative** **to** **`coord + {2,3,4}`** **(** **`min_d=2`**, **`91`** **splits** **)** **.** **Full** **four-point** **parities** **are** **necessary** **for** **this** **union-style** **`min_d=2`** **certificate** **at** **`n=7`**, **`{2,3}`** **.**

- **Secondary** **(** **unexpected** **symmetry** **)** **:** **coord + full `r∈{2,4}`** **only** **also** **`min_d=3`**. **So** **full** **`r=3`** **is** **likewise** **necessary** **:** **neither** **arity** **alone** **(** **with** **`r=2`** **)** **suffices** **for** **depth** **`2`** **;** **the** **`{2,3,4}`** **union** **uses** **redundant** **overlap** **(** **56+56 > 91** **)** **but** **both** **`r=3`** **and** **`r=4`** **menus** **are** **load-bearing** **in** **the** **sense** **that** **dropping** **either** **breaks** **`min_d=2`** **.**
