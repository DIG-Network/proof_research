# Analogy pass

## 1. Abstract structure

**Scale** **the** **same** **adaptive** **tree** **+** **r-sparse** **XOR** **library** **scan** **to** **the** **next** **majority** **slice:** **`n=12`**, **`t=7`**, **Hamming** **shells** **`|S|∈{6,7}`** **(** **sub-quorum** **vs** **quorum** **)** **.**

## 2. Analogues (≥3)

1. **098–100** **`{5,6}`** **sweeps** **on** **`n∈{9,10,11}`** **—** **fixed** **pattern** **:** **coord** **`min_d=n`**, **full** **`n`****-XOR** **`min_d=1`**, **interior** **`min_d(r)`** **plateaus** **/** **bumps** **vary** **with** **`n`** **.**

2. **094** **/** **092** **—** **global** **parity** **splits** **adjacent** **shells** **`k`** **vs** **`k+1`** **on** **`{0,1}^n`**, **so** **full** **12-XOR** **should** **still** **give** **`min_d=1`** **here** **.**

3. **Rate** **/** **capacity** **—** **larger** **`n`** **and** **`|domain|=C(12,6)+C(12,7)=1716`** **stress** **the** **same** **DP** **as** **924-mask** **`n=11`** **case** **(** **complexity** **probe** **)** **.**

## 3. Machinery

Identical DP to **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-five-six-n11/script.py`**, **with** **`N=12`**, **`SHELLS=(6,7)`**, **`r=2..11`**, **unions** **`r∈{2,3,4}`**, **`r∈{2..5}`**, **`r∈{2..11}`** **when** **compute** **finishes** **.**

## 4. Transfer seed

**See** **whether** **`n=11`** **`{5,6}`** **phenomenology** **(** **loss** **of** **099-style** **`min_d(6),min_d(7)>min_d(5)`** **)** **has** **an** **analog** **for** **`{6,7}`** **at** **`n=12`**, **and** **where** **prefix** **`min_d(r)`** **plateaus** **.**

---

# Formal hypothesis

**H1:** **Coord-only** **`min_d=12`** **;** **coord** **+** **full** **12-XOR** **`min_d=1`** **.**

**H2:** **Prefix** **`min_d(r)`** **for** **`r=2..5`** **is** **non-increasing** **(** **≥** **previous** **`n`** **rows** **in** **spirit** **)** **or** **we** **record** **the** **actual** **finite** **sequence** **.**

**H3:** **Union** **`r≤5`** **depth** **is** **≥** **that** **for** **`n=11`** **`r≤5`** **(** **which** **was** **3** **)** **unless** **a** **shallower** **mixed** **language** **appears** **.**

**Falsification:** **Implementation** **bug** **;** **or** **timeout** **→** **INCONCLUSIVE** **with** **partial** **`r`** **range** **documented** **.**

---

# Outcome (post-run)

*(Filled after `script.py`.)*
