# Analogy pass

## 1. Abstract structure

**Extend** **the** **`(12,{6,7})`** **adaptive** **coord** **+** **r-sparse** **XOR** **depth** **scan** **to** **`n=13`** **with** **the** **same** **majority** **semantics** **:** **t=7** **,** **shells** **`|S|∈{6,7}`** **(** **one** **below** **quorum** **vs** **quorum** **)** **.**

## 2. Analogues (≥3)

1. **101** **/** **`…-n12-r5-r7-resolved`** **—** **1716** **masks** **;** **full** **`min_d(r)`** **row** **and** **union** **`min_d=2`** **.**
2. **Complexity** **—** **`|domain|=C(13,6)+C(13,7)=3432`** **(** **2×** **n=12** **)** **tests** **whether** **sharded** **`--r-single`** **still** **suffices** **or** **baseline** **DP** **already** **bites** **.**
3. **094** **/** **092** **—** **full** **`n`****-XOR** **still** **splits** **adjacent** **Hamming** **shells** **at** **any** **`n`** **.**

## 3. Machinery

Same **`script.py`** **pattern** **as** **`wt-six-seven-n12`** **:** **`N=13`**, **`SHELLS=(6,7)`**, **sharding** **flags** **.**

## 4. Transfer seed

**See** **if** **`coord_only`** **`min_d=13`** **and** **`min_d_full=1`** **hold** **,** **and** **whether** **any** **cheap** **`r`** **(** **e.g.** **`r=2`** **)** **completes** **within** **resource** **budget** **.**

---

# Formal hypothesis

**H1:** **Coord-only** **`min_d=13`** **;** **coord** **+** **full** **13-XOR** **`min_d=1`** **.**

**H2:** **If** **compute** **allows** **,** **at** **least** **`--r-single`** **2** **returns** **a** **finite** **`min_d`** **(** **expect** **≥** **n=12’s** **6** **)** **.**

**Falsification:** **Script** **bug** **;** **or** **baseline** **timeout** **/** **OOM** **→** **INCONCLUSIVE** **with** **partial** **baseline** **timings** **only** **.**

---

# Outcome (post-run)

- **H1:** PASS (coord `min_d=13`, full 13-XOR `min_d=1`).
- **H2:** INCONCLUSIVE — only **`r=2`** completed (`min_d=7`); **`r=3..12`** deferred to follow-up shards.
