# Analogy pass

## 1. Abstract structure

Scale the adaptive tree + r-sparse XOR library scan to the next majority slice: **n=13**, **t=8**, Hamming shells **|S| ∈ {7,8}** (sub-quorum vs quorum). Domain size **C(13,7)+C(13,8)=3003** masks.

## 2. Analogues (≥3)

1. **n=12 {6,7}** — coord **min_d=12**, full **12-XOR** **min_d=1**, interior **min_d(r)** with non-monotone bumps; unions **r≤5 → 3**, full union **→ 2**.

2. **n=11 {5,6}** — same pattern class; **924** masks; prefix **min_d(r)** not strictly monotone.

3. **Global parity lemma (094)** — full **n-XOR** splits adjacent shells **k** vs **k+1** on **{0,1}^n**, so **coord + full 13-XOR** should still give **min_d=1** here.

## 3. Machinery

Identical DP to `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n12/script.py`, with **N=13**, **SHELLS=(7,8)**, **r=2..12**, unions when compute allows. Expect **process sharding** (`--r-single`) for heavy **r** (as for n=12 **r=5,7**).

## 4. Transfer seed

Compare **min_d(r)** row to **n=12 {6,7}** and test whether **union r≤5** depth tracks the previous **3** or shifts.

---

# Formal hypothesis

**H1:** Coord-only **min_d = 13**; coord + full **13-XOR** **min_d = 1**.

**H2:** Prefix **min_d(r)** for **r = 2..5** is documented; we do not assume monotonicity (falsified on n=12).

**H3:** Union **r ∈ {2,3,4,5}** has **min_d** in **{2,3}** unless a shallower mixed language appears (n=12 gave **3**).

**Falsification:** Implementation bug; or timeout → **INCONCLUSIVE** with partial **r** range documented.

---

# Outcome (post-run)

**PASS** **(** **full** **row** **+** **unions** **)** **—** **2026-03-31** **.**

- **H1:** Confirmed (`min_d_coord=13`, `min_d_full_13xor=1`).
- **H2:** Full **`min_d(r)`** for **`r=2..12`:** **`7,5,4,3,3,3,4,3,4,3,2`** (non-monotone in **`r`**).
- **H3:** **`{2,3,4,5}→3`**, full **`{2..12}→2`**; triple **`{2,3,4}→4`**. Same union depths as **`(n=13,{6,7})`**; entire **`min_d(r)`** vector **matches** that experiment despite **`|domain|=3003`** vs **3432**.
