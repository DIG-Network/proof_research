# Analogy pass

## 1. Abstract structure

The **`exists_tree(S, d)`** recursion is a **memoized decision procedure** on a large state space **`(bitmask over domain, depth)`**. Peak **RSS** is driven by **distinct visited states** retained in the memo table. **Disk-backed** memo (**disk-memo-microbench-exists-tree-n12**) failed because **per-operation latency** dominates; the structural alternative is **in-RAM eviction** with **recomputation** on miss.

## 2. Analogues

1. **CPU caches / TLBs** — fixed capacity, evict cold lines, **correctness** via **reload** (miss penalty).
2. **Graph algorithms with limited tabu** — revisit vertices after forgetting; **complete** if the underlying search is sound on recomputation.
3. **Dynamic programming with sliding window** — when dependency graph allows, bounded memory at **time** cost.

## 3. Machinery

**LRU** (or FIFO) **cap** on **`(bits, depth_remaining) → bool`**: on eviction, **drop** the entry; a later **miss** **re-explores** that subtree. **Semantics** match **unbounded** memo because **no false positives**: cached **`True`**/**`False`** are still valid when present; absent entries are **unknown**, not **wrong**.

## 4. Transfer seed

If **working set** of **`r=5`/`r=7`** is **heavy-tailed** but **below** a **practical** cap **in footprint** if evictions are allowed, **LRU** may **finish** with **bounded RSS** at **higher** **wall time**. If the **reuse distance** exceeds any feasible cap, **time** **explodes** (**INCONCLUSIVE** or **FAIL** as engineering hypothesis).

---

# Formal hypothesis

**H1:** For **`r=6`** on **`(12,{6,7})`**, **LRU-capped** memo with **cap ≪** **|full memo|** yields the **same** **`min_d`** as **unbounded** memo (**cross-check**).

**H2:** For **`r∈{5,7}`**, **some** **LRU cap** in **{256k, 1M, 4M, …}** completes on this host within **bounded wall** and reports a **`min_d`** **consistent** with the **union** language evidence (**standalone** **`min_d` ≤ 2** if a depth-2 tree exists in that language — we only **certify** **feasibility** at reported **`d`**, not **globally** **minimal** without exhaustive proof).

**Falsification:** **H1** mismatch → **bug**; **H2** timeout or **RSS** kill → **FAIL** for bounded-LRU as drop-in.
