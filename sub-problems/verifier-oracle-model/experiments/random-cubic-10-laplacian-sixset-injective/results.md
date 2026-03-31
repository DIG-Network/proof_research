# Results — random-cubic-10-laplacian-sixset-injective

## Outcome: **FAIL** (hypothesis “∃ injective random cubic” refuted in search range)

## Procedure

- **Host:** `networkx.random_regular_graph(3, 10, seed=s)` for each integer **s ∈ [0, 99 999]**.
- **Check:** For each graph, enumerate all **C(10,6) = 210** subsets **S** of size **6**, compute **L(G[S])**, sort eigenvalues, round to **8** decimals (same as **032**). **Injective** iff **210** keys are **pairwise** distinct.

## Observation

**No** seed in **0..99 999** produced an injective map **S ↦ spec(L(G[S]))** on **6**-subsets.

Collisions typically appear **very** **early** (often the **second** **6**-subset checked); a common pattern is **two** **6**-sets differing by **one** **vertex** **(e.g.** **{0,1,2,3,4,5}** **vs** **{0,1,2,3,4,6})** **with** **isomorphic** **induced** **structure** **—** **analogous** **to** **032** **on** **Petersen** **but** **without** **relying** **on** **global** **graph** **symmetry.**

## Conclusion

In this **large** **reproducible** **sample** **of** **labeled** **3-regular** **graphs** **on** **10** **vertices**, **full** **sorted** **induced** **Laplacian** **spectrum** **on** **quorum** **6**-**sets** **does** **not** **act** **as** **an** **injective** **fingerprint** **of** **S**. **Supports** **digest** **follow-up** **to** **032:** **collisions** **are** **not** **only** **a** **Petersen** **automorphism** **artifact.**

## Repro

Requires **Python** **+** **numpy** **+** **networkx** (see `script.py`). Runtime ~**20** **s** **on** **a** **typical** **laptop** **for** **100 k** **seeds.**

```bash
python script.py
```
