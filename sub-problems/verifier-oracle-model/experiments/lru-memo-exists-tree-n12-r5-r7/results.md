# Results: lru-memo-exists-tree-n12-r5-r7

**Outcome:** FAIL (for the **engineering** hypothesis that **LRU-capped** in-RAM memo is a **practical** way to recover **standalone** **`min_d(r=5)`** / **`min_d(r=7)`** on **low-RAM** hosts)

## H1 — LRU agrees with unbounded memo on **`r=6`**

**PASS.** `python3 script.py --r-single 6 --verify-r6 --cap 500000`:

- **`min_d = 2`**, matching the published **`n=12`**, **`{6,7}`** table in **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n12/results.md`**.
- Confirms the **LRU implementation** does not introduce **false negatives** on at least one **heavy** but **RAM-safe** single-arity language.

## H2 — **`r=5`** / **`r=7`** under **cap**

**`r=7`**, **`--d-max 2`**, **`cap=4_000_000`:** **`d=1,2`** both **infeasible** in **~1 s** (**322k** memo hits, **324k** misses at **`d=2`**). **Standalone** **`min_d(7)`** is **known** **≥ 3** from the **union** **`r∈{6,7}`** run (**`min_d=2`** there includes **`r=6`** splits), so **infeasible at `d≤2`** is **not** a contradiction.

**`r=5`**, **`--d-max 2`**, **`cap=4_000_000`:** same **~1 s** profile (**infeasible** at **`d=1,2`**). Published **standalone** **`min_d(5)=4`** would first show feasibility at **`d=4`**; we did **not** reach **`d=4`** under LRU.

**`r=5`**, **`d=3`**, **`cap=4_000_000`:** **no completion** within **900 s** (**`timeout 900`**). Earlier **`cap=1_000_000`** runs showed **`d=3`** still running after **90 s**. So **eviction-driven recomputation** blows up **wall time** before **RSS** is the bottleneck.

**Automated repro:** `python3 script.py --bench-h2` — runs **`r=6`** LRU cross-check (**must** **PASS**), then **`timeout 120`** on **`r=5`**, **`d≤3`**, **`cap=4_000_000`**; **expected** **exit** **124** on the inner run → script **exits** **1** with **`OUTCOME: FAIL hypothesis H2`** (**~121 s** **wall**).

**Contrast:** **Unbounded** memo **OOM**’s on **`r=5`/`r=7`**; **LRU** **avoids** **OOM** on **`d≤2`** probes but **does not** **terminate** for **`d=3`** on **`r=5`** in **≤15 min** at **4M** entries — **not** a usable **drop-in** for **full** **`min_d`** **certificates** here.

## Reasoning

**Disk** memo failed on **latency** (**disk-memo-microbench-exists-tree-n12**). **LRU** fixes **capacity** but **destroys** **reuse locality** on this **branching** **DP**: **misses** **≈** **hits** at **`d=2`** already, and **`d=3`** **explodes**. **Tighter** caps **worsen** **time**; **looser** caps **approach** **unbounded** **RSS** again.

**Context:** The **full** **`n=12`**, **`{6,7}`** **`min_d(r)`** **table** **(** **including** **`r=5,7`** **)** **was** **completed** **separately** **(** **`adaptive-coordinate-or-rsparse-xor-tree-depth-wt-six-seven-n12-r5-r7-resolved`** **)** **using** **unbounded** **memo** **;** **this** **experiment** **does** **not** **re-open** **those** **values** **—** **it** **only** **tests** **whether** **LRU** **could** **substitute** **for** **that** **memory** **model**.

## Implications

- **Next** avenues for **`min_d(5)`** / **`min_d(7)`** remain **more RAM**, **symmetry**/**state** **compression**, or **algorithmic** **pruning** — **not** **naive** **LRU** on **`(bits, depth)`**.
