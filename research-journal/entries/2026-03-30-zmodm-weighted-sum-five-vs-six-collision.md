# 2026-03-30 — zmodm-weighted-sum-five-vs-six-collision

**Experiment path:** `sub-problems/anonymous-quorum-binding/experiments/zmodm-weighted-sum-five-vs-six-collision/`

**Context:** `anonymous-quorum-binding`

**Hypothesis (summary):** For **n=10** **with** **public** **weights** **w_i=i+1**, **some** **modulus** **M∈[2,50]** **yields** **equal** **Σ w_i (mod M)** **for** **some** **5**-**subset** **and** **some** **6**-**subset.**

**Outcome:** **PASS**

**Key finding:** **Smallest** **hit** **M=2:** **5**-**set** **(4,6,7,8,9)** **sum** **39≡1,** **6**-**set** **(0,1,2,3,4,5)** **sum** **21≡1.** **One** **modular** **linear** **aggregate** **does** **not** **separate** **|S|=5** **from** **|S|=6** **—** **parity**-**class** **overlap** **(kin** **to** **023** **on** **count** **parity).**

**Implications:**

- **Homomorphic-style** **“sum** **of** **public** **weights”** **π** **needs** **more** **than** **one** **small-mod** **fingerprint** **without** **extra** **binding.**
- **Digest:** **add** **modular** **aggregate** **thread** **alongside** **polynomial** **openings.**

**Analogy pass summary:** **Subset-sum** **mod** **M,** **homomorphic** **fingerprints,** **universal** **hashing** **limits** **—** **seed:** **exhaust** **5**- **vs** **6**-**subset** **residues.**
