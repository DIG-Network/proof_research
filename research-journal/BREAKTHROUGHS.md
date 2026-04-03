# Breakthrough log

Append-only record of novel constructions, impossibility results, assumptions, or structural analogies that qualify under `persona.md`.

**Status:** One small formal impossibility in the verifier-oracle toy line (**049**). Prior work (**Entries 000–020** in `research-journal.md`) is mostly **negative / interface** evidence and accounting; review before logging here.

When adding an entry, use the template in `persona.md` (title, type, discovered-in, description, novelty, implications, open questions).

---

## [2026-03-30] Pairwise-XOR decision trees cannot separate adjacent shells when n = 2T − 1

**Type:** Impossibility

**Discovered in:** `sub-problems/verifier-oracle-model/experiments/adaptive-pairwise-or-xor-tree-depth-wt-shells/`

**Description:**
Consider adaptive binary decision trees whose internal nodes query `x_i ⊕ x_j` for some `i < j`, and leaves must be pure with respect to the predicate `popcount(x) ∈ {T−1, T}` on `{0,1}^n`. If `n = 2T − 1`, then global complement `x ↦ x ⊕ (1,…,1)` swaps the two Hamming shells (`T−1` and `T`), but every pairwise XOR answer is invariant under this complement. Hence any two complementary feasible vectors follow the same root-to-leaf path, yet lie in different shells — no perfect separating tree exists.

**Why this is novel:**
Closest known material is generic “linear masks miss odd parity” folklore in F₂; packaging it as a **clean symmetry obstruction for a natural non-coordinate oracle** in the threshold-shell decision-tree toy is project-specific. May appear implicitly in coding/property-testing notes.

**Novelty confidence:** Low (elementary parity / symmetry).

**Implications:**
Any verifier model that only admits **even-parity** linear probes (e.g. 2-bit XOR pools) cannot break a `T−1` vs `T` gap when `n = 2T−1` and complement exchanges the two cases. Contrasts with `(n,T)=(6,4)` where XOR trees succeed in depth `3 ≪ n`.

**Open questions it raises:**
Classify which **pair-local** Boolean gates admit complement (or other) **equivariance** killing **which** `(n,T)` **shell** **pairs.**

---

## [2026-03-31] Triple-XOR internal nodes lower adaptive shell-separation depth on (10,{5,6})

**Type:** Constraint

**Discovered in:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-triple-xor-tree-depth-wt-five-vs-six/`

**Description:**
On the **462** masks with **n=10** and **popcount ∈ {5,6}**, consider adaptive binary decision trees whose internal nodes are either a **coordinate** probe **x_i** or a **triple parity** probe **x_i ⊕ x_j ⊕ x_k** (all **120** lexicographic triples allowed). Exhaustive memoized `exists_tree` on the full bitmask state finds **`exists_tree(full,4)=True`** and **`exists_tree(full,3)=False`**, hence **`min_d = 4`**. The same DP under the **066** gate set (coordinates plus **pair** XOR only) has **`min_d = 5`**; **074** recorded **`exists_tree(full,4)=False`** in that narrower language.

**Why this is novel:**
Within this **project’s** verifier-oracle toy, the result is a **sharp** refinement: **weight-3** **F₂** linear splits are **not** implied by **depth-4** compositions of **pair** XORs in the **one-node-one-gate** model—adding them as **primitive** splits **strictly** reduces **worst-case** **separator** **depth**. Elementary for coding theorists; the **packaged** **certificate** **on** **the** **fixed** **(10,{5,6})** **instance** **updates** **the** **internal** **“d=5** **is** **first** **feasible”** **narrative** **from** **066**/**074**.

**Novelty confidence:** Medium (exhaustive small instance; structural pattern may be folklore in property testing).

**Implications:**
Any **resource** **model** **that** **charges** **only** **pair** **parity** **queries** **may** **overstate** **minimal** **adaptive** **depth** **if** **higher-weight** **affine** **F₂** **splits** **are** **cheap** **in** **the** **real** **verifier** **—** **toy** **only,** **but** **it** **reopens** **the** ** arity** **axis** **after** **066**/**084**/**085**/**086**.

**Open questions it raises:**
For **general** **(n,** **T−1** **vs** **T)**, **how** **does** **min** **depth** **scale** **when** **internal** **nodes** **allow** **all** **r**-**sparse** **F₂** **parities** **for** **r** **≤** **R** **?** **Where** **does** **the** **first** **feasible** **d** **stabilize** **as** **R** **grows** **?**

---

## [2026-03-30] Quadruple-XOR nodes further lower adaptive depth on (10,{5,6}) to 3

**Type:** Constraint

**Discovered in:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-quadruple-xor-tree-depth-wt-five-vs-six/`

**Description:**
On the same **462** masks (**n=10**, **wt ∈ {5,6}**), allow internal nodes that are either a coordinate **x_i** or a **quadruple parity** **x_i ⊕ x_j ⊕ x_k ⊕ x_l** for every lexicographic **4**-tuple (**210** splits). Exhaustive memoized `exists_tree` gives **`exists_tree(full,3)=True`** and **`exists_tree(full,2)=False`**, so **`min_d = 3`**. This **strictly extends** the **090** language (**090 ⊂ 091**), which had **`min_d = 4`** and **`exists_tree(full,3)=False`**.

**Why this is novel:**
Same **project-local** **packaging** **as** **090:** **each** **increment** **pair → triple → quadruple** **as** **primitive** **parity** **splits** **has** **dropped** **`min_d`** **by** **exactly** **one** **on** **this** **fixed** **instance** **(** **5 → 4 → 3** **)** **so** **far.** **Shows** **090** **was** **not** **the** **arity** **saturation** **point.**

**Novelty confidence:** Medium (small exhaustive instance; general **R**-sparse parity classification open).

**Implications:**
**Resource** **models** **for** **adaptive** **F₂** **linear** **queries** **should** **treat** **maximum** **parity** **weight** **per** **node** **as** **a** **first-class** **parameter** **—** **depth** **can** **track** **it** **down** **faster** **than** **only** **adding** **pair** **XORs.**

**Open questions it raises:**
Does **allowing** **all** **5**-**sparse** **parities** **(** **C(10,5)=252** **)** **force** **`min_d=2`** **or** **stay** **at** **3** **?** **Does** **full** **Hamming** **weight** **parity** **(** **10** **bits** **)** **alone** **(** **plus** **coords** **)** **already** **separate** **wt=5** **vs** **6** **in** **one** **node** **on** **this** **domain** **?**

---

## [2026-03-30] One global parity XOR separates wt=5 vs wt=6 on the (10,{5,6}) toy domain

**Type:** Constraint

**Discovered in:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-total-parity-xor-tree-depth-wt-five-vs-six/`

**Description:**
Restrict to **n=10** bit vectors of Hamming weight **5** or **6** only (**462** masks). Allow adaptive binary decision trees whose internal nodes are either a coordinate **x_i** or a **single** additional gate: the **total XOR** **x_0 ⊕ ⋯ ⊕ x_9**, i.e. **global Hamming parity** (equivalently **popcount(x) mod 2**). The partition induced on the **462** indices puts **all** **252** weight-**5** vectors on one side (odd parity) and **all** **210** weight-**6** vectors on the other (even parity). Each side is leaf-pure for the shell predicate, so **`exists_tree(full,1)=True`** and **`min_d = 1`**. This **full** parity functional is **not** expressible as any **one** of the **210** **quadruple-XOR** nodes in **091** (those XOR **4** coordinates only).

**Why this is novel:**
Closes the **explicit** **open** **question** **in** **the** **091** **breakthrough** **entry** **for** **this** **fixed** **domain.** **Qualitatively** **different** **from** **the** **066→091** **“bounded** **arity** **per** **node”** **ladder:** **allowing** **weight-n** **parity** **once** **collapses** **depth** **3→1** **here.**

**Novelty confidence:** Low–Medium (elementary **parity** **vs** **weight** **on** **adjacent** **shells** **when** **n** **is** **odd** **;** **packaging** **in** **the** **project’s** **`exists_tree`** **framework** **is** **new** **for** **the** **log** **).**

**Implications:**
**Verifier-oracle** **budgets** **must** **distinguish** **“max** **r** **coordinates** **per** **XOR** **pool”** **from** **“full** **vector** **parity”** **—** **the** **latter** **can** **be** **O(n)** **wire** **XOR** **but** **O(1)** **query** **in** **an** **idealized** **probe** **model.**

**Open questions it raises:**
With **only** **5**-**sparse** **XOR** **primitives** **(** **no** **total** **parity** **),** **what** **is** **`min_d`** **on** **the** **same** **462-set** **?** **(** **Still** **open** **after** **091** **.)**

---

## [2026-03-30] 5-sparse XOR primitives (+ coords) reach depth 2 on (10,{5,6}), beating 4-sparse-only depth 3

**Type:** Constraint

**Discovered in:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-pentuple-xor-tree-depth-wt-five-vs-six/`

**Description:**
On the **462** masks with **n=10** and **wt ∈ {5,6}**, allow adaptive binary decision trees whose internal nodes are either a coordinate **x_i** or a **5-sparse XOR** **x_{i₁} ⊕ ⋯ ⊕ x_{i₅}** for every lexicographic **5**-tuple (**252** primitive splits). **Exclude** **total** **10-bit** **parity** and **exclude** **3/4-sparse** **XOR** **as** **primitives** **(** **incomparable** **with** **091’s** **coord+quad** **library** **).** Exhaustive memoized `exists_tree` gives **`exists_tree(full,2)=True`**, **`exists_tree(full,1)=False`**, hence **`min_d = 2`**. By contrast, **091** (coord + **only** **4**-sparse XOR primitives, **210** splits) has **`min_d = 3`** on the same domain.

**Why this is novel:**
Resolves the **first** **091** **breakthrough** **open** **question** **(** **2** **vs** **3** **)** **and** **shows** **a** **strict** **depth** **improvement** **from** **raising** **sparse** **parity** **weight** **from** **4** **to** **5** **per** **node** **—** **even** **though** **neither** **gate** **set** **contains** **the** **other.**

**Novelty confidence:** Medium (small exhaustive instance).

**Implications:**
For **this** **toy** **,** **R=5** **local** **parity** **pools** **are** **a** **better** **“sweet** **spot”** **than** **R=4** **before** **resorting** **to** **full** **n**-**bit** **parity** **(** **092** **).**

**Open questions it raises:**
**Unified** **picture** **for** **general** **(n,** **T−1** **vs** **T)** **:** **which** **R** **matches** **majority** **threshold** **t** **for** **similar** **shell** **separation** **depth** **scalings** **?**

---

## [2026-03-30] Non-monotone arity depth: on (8,{4,5}), 5-sparse XOR-only library is worse than 4-sparse-only

**Type:** Constraint

**Discovered in:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-four-five-n8/`

**Description:**
On the **126** masks with **n=8** and **popcount ∈ {4,5}**, consider the same adaptive **`exists_tree`** model as **095** (`coord` **or** one **r**-sparse XOR primitive per internal node). Exhaustive DP gives **`min_d`** for **coord + all r-XORs** as follows: **`r=2` → 4**, **`r=3` → 4**, **`r=4` → 2**, **`r=5` → 4**. Thus **`min_d(r)`** is **not** monotone in **`r`**: **5-sparse-only** is **strictly worse** than **4-sparse-only** (**4** vs **2**). **Coord-only** **`min_d=8`**, **coord + full 8-bit XOR** **`min_d=1`**. Unions **`r∈{2,3,4}`** and **`r∈{2,3,4,5}`** both achieve **`min_d=2`**.

**Why this is novel:**
**095** showed a **plateau** (**triple = quad** on **`(7,{3,4})`**). **`(10,{5,6})`** showed a **strict** **increasing** **arity** **ladder** **pair→…→pentuple** **with** **decreasing** **`min_d`**. This is the first packaged **reversion**: **higher** **allowed** **parity** **weight** **`r`** **can** **increase** **worst-case** **separator** **depth** **when** **that** **is** **the** **only** **non-coordinate** **primitive** **arity** **in** **the** **language**.

**Novelty confidence:** Medium (single small instance; pattern may appear in coding/property-testing folklore under different wording).

**Implications:**
**Verifier-oracle** **/ ** **resource** **chargers** **must** **not** **assume** **“larger** **R-sparse** **XOR** **menu** **⊃** **smaller”** **implies** **`min_d`** **non-increasing** **under** **single-arity** **gate** **sets** **.** **Sweet-spot** **`r`** **can** **be** **below** **`t−1`** **(** **here** **`r=4`** **for** **shells** **4** **vs** **5** **).**

**Open questions it raises:**
**Characterize** **`(n,`** **`{t−1,t})`** **for** **which** **`min_d(r+1)≤min_d(r)`** **fails** **;** **relate** **to** **`n`**, **`t`**, **and** **dual** **Hamming** **symmetry** **.**

---

## [2026-03-30] Full r-sweep on (10,{5,6}): min_d(r) non-monotone — r=5 beats r=6 and r=7

**Type:** Constraint

**Discovered in:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-five-six-n10/`

**Description:**
On the **462** masks with **n=10** and **popcount ∈ {5,6}**, run the same **`exists_tree`** DP as **097**/**098**: internal nodes are **coordinate** splits or one **r-sparse XOR** parity split chosen from **all** **C(10,r)** **r**-subsets of coordinates (single-arity library per run). Exhaustive **`min_d(r)`** for **r=2..9** yields:

**r=2→5, r=3→4, r=4→3, r=5→2** (agrees with **066**/**090**/**091**/**093**), then **r=6→3**, **r=7→4**, **r=8→3**, **r=9→2**. Thus **`min_d(6)>min_d(5)`** and **`min_d(7)>min_d(5)`**: **higher** **sparse** **parity** **weight** **alone** **does** **not** **improve** **worst-case** **depth** **monotonically** **even** **on** **the** **canonical** **threshold-shell** **pair** **.** **Coord-only** **`min_d=10`**, **full** **10-XOR** **`min_d=1`**. **Unions** **`r∈{2,3,4}`** **`→3`**, **`r∈{2..5}`** **and** **`r∈{2..9}`** **both** **`→2`**.

**Why this is novel:**
**096** packaged **non-monotonicity** on **`(8,{4,5})`** **and** **contrasted** **with** **a** **perceived** **strict** **decreasing** **ladder** **on** **`(10,{5,6})`** **that** **had** **only** **been** **verified** **for** **`r≤5`**. **099** **is** **the** **first** **full** **`r=2..n−1`** **table** **on** **462** **masks** **and** **shows** **the** **same** **reversion** **phenomenon** **in** **the** **middle** **range** **`r∈{6,7}`**.

**Novelty confidence:** Medium (single instance; exhaustive DP).

**Implications:**
**Resource** **models** **and** **proof** **sketches** **that** **infer** **“larger** **r** **⇒** **easier** **separation”** **from** **the** **066→093** **prefix** **are** **invalid** **without** **scanning** **all** **`r`**. **Sweet-spot** **`r=t−1=5`** **here** **is** **not** **superseded** **by** **`r=6`** **or** **`r=7`** **as** **single-arity** **libraries** **.**

**Open questions it raises:**
**Closed** **form** **or** **symmetry** **explanation** **for** **which** **`r`** **are** **local** **minima** **of** **`min_d(r)`** **on** **`(n,{t−1,t})`** **;** **relation** **to** **dual** **codes** **/** **MacWilliams** **style** **identities** **(** **speculative** **)** **.**

---

## [2026-04-03] Full XOR union min_d=2 certificate does not extend to n=5 on the {2} shell

**Type:** Constraint

**Discovered in:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-rsparse-xor-tree-depth-wt-two-n5-full-r2-r3-union-min-d/`

**Description:**
On **`n=5`**, restrict to the **`10`** weight-**`2`** Hamming masks (**`C(5,2)`**). Run the same **`exists_tree`** DP as the **`n≥6`** ladder: coordinate splits plus the **full multi-arity XOR union** **`⋃_{r=2}^{3} XOR_r`** (**`C(5,2)+C(5,3)=20`** parity splits). With default **`4M`** LRU memo, **`coord_only`**, **`coord_plus_full_5xor`**, and the **union** language all have **`min_d=1`**. Thus the **`min_d=2`** phenomenon documented for **`coord + ⋃_{r=2}^{n-2} XOR_r`** on the majority-adjacent shells **starts at `n=6`**, not **`n=5`**.

**Why this is novel:**
Prior digest text flagged **`n=5`** as an **optional** downward extension **without** a measured verdict. This experiment **closes** that gap with a **clean negative**: the **same** menu template **fails** to produce depth-**`2`** **minimality** at **`n=5`** on the natural **`{2}`** slice for **`t=3`**.

**Novelty confidence:** Medium (small **`n`**, but definitive for this shell and menu).

**Implications:**
Oracle / narrative claims should cite **`n∈{6,…,14}`** (or **`n≥6`**) for this **`min_d=2`** **full-union** fact — **not** **`n≥5`**. Any **`n=5`** certificate needs a **different** mask family or split library.

**Open questions it raises:**
Whether **adding weight-**`3`** masks at **`n=5`** (all **`26`** nontrivial masks) restores a **`min_d=2`** **separator** for a **`t=3`** **vs** **`t=2`** **story** **orthogonal** **to** **the** **`{2}`**-only **slice**.

---

## [2026-04-03] Closed-form 5-vs-6 cross-shell collision for exact (min,max,Σ,Π) at n=12

**Type:** Constraint

**Discovered in:** `sub-problems/anonymous-quorum-binding/experiments/joint-min-max-sum-product-quadruple-weight-five-six-shell-n12`

**Description:**
Fix public weights **`w_i=i+1`** on **`n=12`** and shells **`|S|∈{5,6}`**. Let **`K(S)=(min,max,Σ,Π)`** in **ℤ**. For any **`m∈{11,12}`**, the **5-set** **`{1,5,6,8,m}`** and the **6-set** **`{1,2,3,4,10,m}`** share the same **`K`**: **`min=1`**, **`max=m`**, **`Σ=20+m`**, **`Π=240m`**. Hence **`K`** is **not** injective on **`C(12,5)∪C(12,6)`** despite **093** showing **injectivity** at **`n=10`** for the same statistic and weights.

**Why this is novel:**
**093** was summarized as a strong “joint extrema + both masses” separator in the toy; this gives an **explicit parametric** cross-shell equality that **only appears** once **`n`** is large enough to host **`m≥11`**, so **injectivity is not monotone** in **`n`**.

**Novelty confidence:** Medium (elementary arithmetic; project-specific framing).

**Implications:**
Claims that **exact** **`(min,max,Σ,Π)`** separates **`|S|=5`** vs **`|S|=6`** for **`w_i=i+1`** must be **qualified by `n`**. Modular-collapse experiments at **`n=12`** (**095**) sit in a regime where **integer** collisions already exist without any modulus.

**Open questions it raises:**
For which **`n>10`** does the first cross-shell collision appear for this **`K`**, and whether other **`w_i`** schedules avoid this **family** on **`{5,6}`** shells.

---

## [2026-04-03] Minimal universe for exact (min,max,Σ,Π) 5-vs-6 cross-shell collision is n=11 (linear weights)

**Type:** Constraint

**Discovered in:** `sub-problems/anonymous-quorum-binding/experiments/joint-min-max-sum-product-quadruple-weight-five-six-minimal-n11-scan`

**Description:**
Fix **`w_i=i+1`** and **`K(S)=(min,max,Σ,Π)`** on shells **`|S|∈{5,6}`**. Exhaustive scan: **`n=10`** (**093**) has **no** cross-shell key collision; **`n=11`** has **exactly one** shared key **`(1,11,31,2640)`** with witness **5-set** weights **`{1,5,6,8,11}`** vs **6-set** **`{1,2,3,4,10,11}`** (0-based indices **`(0,4,5,7,10)`** vs **`(0,1,2,3,9,10)`**). Hence the **smallest** **`n>10`** with a **5-vs-6** collision is **`11`**, not **`12`**. At **`n=11`**, each shell still has **`462`** distinct internal keys (full rank within shell), but the two shells are not disjoint in **`K`**-space.

**Why this is novel:**
**096** documented a **closed-form** collision family at **`n=12`**; this pins the **first** **`n`** where separation fails for this quadruple and weight schedule, and shows the **`n=12`** phenomenon is **not** the minimal threshold — a **different** witness already appears at **`n=11`**.

**Novelty confidence:** Medium (finite exhaustive check; sharp minimality statement).

**Implications:**
Narratives that “**`K`** breaks when moving from **10** to **12** validators” should read “breaks by **11**”; **096**’s family is an **additional** collision mechanism at **`n≥12`**, not the **first**.

**Open questions it raises:**
Characterize **all** minimal **`n`** witnesses for other **`w_i`** (non-linear schedules); relate **`n=11`** collision to **mod-2** / **095** floor (same **`n`** regime).
