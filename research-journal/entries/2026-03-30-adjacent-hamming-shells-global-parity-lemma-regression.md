# 2026-03-30 — adjacent-hamming-shells-global-parity-lemma-regression

**Experiment:** `sub-problems/verifier-oracle-model/experiments/adjacent-hamming-shells-global-parity-lemma-regression/`

**Context:** `verifier-oracle-model` — **092** used one global XOR to separate **wt ∈ {5,6}** on **n = 10**; this run generalizes the underlying **adjacent-shell** pattern.

**Hypothesis tested:** On **{0,1}ⁿ**, **π(x) = ⊕ᵢ xᵢ** splits the union of Hamming shells **|x| = k** and **|x| = k+1** for every **0 ≤ k < n** (equivalently **π** matches **|x| mod 2** on those shells).

**Outcome:** **PASS** — exhaustive for **n = 1..18**, all **k**; sample **k** parity tautology for **n ∈ {19, 200}**.

**Key finding:** **Global parity** is a **perfect classifier** for **wt = k** vs **wt = k+1** because **k** and **k+1** have opposite parity; **092**’s **`min_d = 1`** is an instance, not an artifact of **(10, {5,6})**.

**Implications:**
- Digest and later work can cite **094** instead of re-explaining the lemma when discussing **total XOR** in adaptive trees.
- No change to **exists_tree** depth numbers; this is **supporting** regression only.

**Analogy pass summary:** Binary code **even/odd** syndromes, RAID parity, graph handshaking (parity flavour) — seed: **single-bit syndrome** for **adjacent** **integer** **weights**.
