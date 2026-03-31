# 2026-03-30 — linear-weights-integer-sum-five-six-collision

**Experiment path:** `sub-problems/anonymous-quorum-binding/experiments/linear-weights-integer-sum-five-six-collision/`

**Context:** `anonymous-quorum-binding`

**Hypothesis (summary):** For **w_i = i+1** **on** **n=10**, **some** **5**-**subset** **and** **6**-**subset** **have** **equal** **integer** **Σ w_i.**

**Outcome:** **PASS**

**Key finding:** **Sum** **21:** **5**-**set** **indices** **(1,2,3,4,6)** **(weights** **2+3+4+5+7)** **and** **6**-**set** **(0,1,2,3,4,5)** **(1+…+6).** **Single** **ℤ** **linear** **aggregate** **does** **not** **encode** **|S|≥6** **vs** **|S|=5** **—** **strictly** **stronger** **than** **034’s** **mod-2** **witness.**

**Implications:**

- **Homomorphic** **sum-only** **π** **without** **cardinality** **/ ** **membership** **proof** **remains** **ambiguous** **even** **without** **modular** **wrap.
- **Pairs** **with** **polynomial** **and** **spectral** **negative** **toys** **as** **“lossy** **summary”** **evidence.**

**Analogy pass summary:** **Subset-sum** **coincidences,** **knapsack** **multiplicity,** **anonymous** **sum** **aggregation** **—** **seed:** **exhaust** **5**- **vs** **6**-**subset** **integer** **totals.**
