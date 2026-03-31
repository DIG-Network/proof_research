# Hypothesis: every ≤4-bit partial view allows both wt=5 and wt=6 completions (n=10)

## Analogy pass

1. **Abstract structure.** The verifier learns a **prefix** of a hidden binary participation vector (answers to membership queries). Sound quorum-vs-sub-quorum separation requires that **no** such prefix be compatible with **both** a below-threshold and an at-threshold global pattern. Equivalently: the **fiber** of the observation map intersects both threshold classes.

2. **Where else this appears.**
   - **Decision trees / PAC:** a depth-bounded tree partitions input space; **shattering** asks whether both labels remain possible in a cell — same “ambiguous leaf” obstruction.
   - **Compressed sensing / restricted views:** many full signals share the same low-dimensional measurement; **non-uniqueness** of reconstruction from too few probes.
   - **Partial assignments in CSP/SAT:** a partial assignment may extend to both a satisfying and a “just failing” global assignment — **consistency** vs **global constraint** gap.

3. **Machinery in those domains.** VC dimension bounds, **Natarajan** dimensions, **RIP** vs **non-RIP** regimes, and **look-ahead** consistency checks all formalize when a **small** observation **underdetermines** a **global** discrete property.

4. **Transfer seed.** **036** showed that for **each fixed** coordinate set **Q** of size 4, some **pair** of wt=5 and wt=6 vectors **agree on all zeros** on **Q**. Here we ask the **stronger** statement: for **every** **partial assignment** on **any** **Q** with **|Q| ≤ 4**, **both** classes remain **non-empty** — which would imply **adaptive** depth-4 **bit** probes still **cannot** separate wt=5 from wt=6 (any leaf sees only ≤4 bits along a path).

## Falsifiable claim

Let **n = 10**. Fix **Q ⊆ {0,…,9}** with **|Q| ≤ 4** and any **p ∈ {0,1}^Q** (identify **p** with values on **Q**). Let **z** = number of indices **i ∈ Q** with **p(i) = 1**.

**Claim:** There exist **u, v ∈ {0,1}^10** such that **u|_Q = v|_Q = p**, **wt(u) = 5**, and **wt(v) = 6**.

Equivalently, the following feasibility conditions hold for **R = n − |Q|** outside coordinates:

- **0 ≤ 5 − z ≤ R** (extend to total weight 5),
- **0 ≤ 6 − z ≤ R** (extend to total weight 6).

**Expected outcome:** **PASS** (pure counting for **|Q| ≤ 4**, **R ≥ 6**).

**If FAIL:** would mean some **(Q, p)** breaks the inequalities — tighten constants or find a bug.

## Link to adaptive queries

Any deterministic adaptive strategy that asks at most **4** **distinct** indices along a path ends at a leaf labeled by some **(Q, p)** with **|Q| ≤ 4**. If the claim holds, **every** such leaf is **ambiguous** between **wt = 5** and **wt = 6**, so **no** leaf can be labeled **ACCEPT** for quorum and **REJECT** for sub-quorum **without** error.
