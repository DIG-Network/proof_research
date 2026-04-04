# Results — `adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-three-n7-pair-r3-random-sample-biconditional-check`

**Outcome:** **FAIL**

**Setup:** **n=7**, shell **{2,3}**, language **coord + full r=2 menu + two chosen r=3 XOR splits** (same shape as **n=6** pair experiments). **C(7,3)=35**, **C(35,2)=595** unordered pairs. **Random sample:** **200** pairs, **`random.Random(0).sample`**, **LRU** cap **4M** (parent driver).

**Hypothesis tested:** **`min_d = 2`** **if and only if** the two triples are **disjoint** (direct lift of the **n=6** exact biconditional).

**Observed:**

- Baseline: **`coord_only min_d=7`**, **`coord_plus_full_7xor min_d=1`** (sanity OK).
- **Sample:** **200** pairs in **~0.58 s** wall.
- **Violations:** **23 / 200** — in every case **`disjoint=True`** but **`min_d=3`** (not **2**). So the **“only if”** direction fails: **disjoint** does **not** imply **`min_d=2`** at **n=7** in this language.

**Conclusion:** The **n=6** classification (**`min_d=2` iff complementary / disjoint triples**) is **not** a dimension-free invariant; **n=7** breaks the naive extension. Deeper structure (e.g. **complementary** **3+3** vs **disjoint-but-not-covering**) or additional splits may be needed to characterize **`min_d=2`** witnesses at **n=7**.

**Scope note:** This is **random-sample** evidence (**not** exhaustive **595** pairs). A full scan could still find edge cases in the converse direction; the **23** counterexamples already falsify the **stated biconditional** as a universal claim.
