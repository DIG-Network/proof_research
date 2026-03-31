# Analogy pass

## 1. Abstract structure

Scale the adaptive tree + r-sparse XOR library scan to **n=14**, **t=8**, Hamming shells **|S| ∈ {7,8}**. Domain size **C(14,7)+C(14,8)=6435** masks (vs **3003** at n=13).

## 2. Analogues (≥3)

1. **n=13 {7,8}** — coord **min_d=13**, full **13-XOR** **min_d=1**; **min_d(r)** row **`7,5,4,3,3,3,4,3,4,3,2`**; unions **`{2,3,4}→4`**, **`{2..5}→3`**, **`{2..12}→2`**.

2. **n=12 {6,7}** — same qualitative pattern; larger domain drove sharded **`--r-single`** runs for heavy **r**.

3. **Adjacent-shell global parity lemma** — full **n-XOR** should still separate **k** vs **k+1** shells, so **coord + full 14-XOR** should yield **min_d=1**.

## 3. Machinery

Identical DP to **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-seven-eight-n13/script.py`**, with **N=14**, **SHELLS=(7,8)**, **r=2..13**, unions when compute allows. Expect **process sharding** for heavy **r** and/or **unbounded LRU** on hosts with RAM.

## 4. Transfer seed

Check whether **min_d(r)** and union minima **track n=13** or shift under the **~2.14×** domain growth.

---

# Formal hypothesis

**H1:** Coord-only **min_d = 14**; coord + full **14-XOR** **min_d = 1**.

**H2:** Prefix **min_d(r)** for small **r** is documented; monotonicity is **not** assumed (falsified at smaller **n**).

**H3:** Union **r ∈ {2,3,4,5}** has **min_d** in **{2,3,4}** unless a shallower mixed language appears.

**Falsification:** Implementation bug; or timeout / OOM → **INCONCLUSIVE** with partial **r** range documented.

---

# Outcome (post-run, 2026-03-31)

**INCONCLUSIVE** — **baseline PASS** (**H1**); **interior row** and **unions** **incomplete**.

- **H1:** **Confirmed** — `coord min_d=14`, `coord+full 14-XOR min_d=1`.
- **H2 / H3:** **Open** — completed **`r ∈ {6,7,8,10,11,12,13}`** only; **`r ∈ {2,3,4,5,9}`** and **union** probes **`{2,3,4}`**, **`{2..5}`** **timed out** (see **`results.md`**).
