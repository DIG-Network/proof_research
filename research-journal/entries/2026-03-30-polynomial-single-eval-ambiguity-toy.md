# 2026-03-30 — polynomial-single-eval-ambiguity-toy

**Experiment path:** `sub-problems/anonymous-quorum-binding/experiments/polynomial-single-eval-ambiguity-toy/`

**Context:** `anonymous-quorum-binding`

**Hypothesis (summary):** For **n = 8** nodes **0,…,7** and query **r ∉ nodes** over **𝔽_p**, two **different** assignment vectors **v ≠ w** can yield the **same** Lagrange-interpolated value **Σ v_i L_i(r) = Σ w_i L_i(r)**.

**Outcome:** **PASS**

**Key finding:** **One** field evaluation imposes **one** linear constraint on **n** free values — **huge** ambiguity class (here an explicit **w** at **Hamming distance 8** from **v**). Supports the **encoding-change** view: polynomial **evaluation** alone does not certify **which** committed multiset / quorum story holds without **binding** machinery and **threshold-specific** checks.

**Implications:**

- Any sketch that tries to compress the validator story to **“publish P(r)”** without **Merkle/PCS + multiple openings** or a novel **Link** must confront this **identifiability** gap.
- Add **AG-code / polynomial** thread to `anonymous-quorum-binding` digest (negative datum).

**Analogy pass summary:** **RS/AG codes**, **PCS**, **finite-field sketching**, **experimental design** — seed: **single-symbol** non-uniqueness.
