# Research journal — compact trustless threshold verification

## Entry 000 — Scan (2026-03-30)

**Context:** Project bootstrap. Workspace previously contained only `persona.md` (problem brief). No `main-problem/`, `sub-problems/`, or prior experiments.

**Actions:**
- Declared formal main problem statement under `main-problem/problem-statement.md`.
- Opened two **independent** blocking sub-problems (both `OPEN`):
  1. `sub-problems/verifier-oracle-model/` — verifier computational model + tension between O(1) commitment, o(n) proof, and soundness.
  2. `sub-problems/anonymous-quorum-binding/` — cryptographic binding of a threshold signing event to a static set commitment without per-key material at verify time.

**Rule applied:** No `main-problem/experiments/*` until all blocking sub-problems are `SOLVED` or `ABANDONED`.

**Next:** Run `verifier-oracle-model` experiment `info-theoretic-barrier`; integrate parallel subagent output for `anonymous-quorum-binding` / `accumulator-threshold-sanity` when available.

---

## Entry 001 — Sub-problem experiments (2026-03-30)

### Branch A — `verifier-oracle-model` / `experiments/info-theoretic-barrier/`

- **Hypothesis:** Merkle commitment to keys + `o(n)` proof cannot align with undisclosed-subset linear multisignature verification without extra binding (structural claim; see `hypothesis.md`).
- **Outcome:** **INCONCLUSIVE** for formal impossibility; **partial evidence** that (i) injective encoding of which strict-majority subset signed needs `Ω(n)` bits at scale, and (ii) toy additive “aggregate pk” depends on the chosen subset.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/info-theoretic-barrier/script.py` (exit 0).

### Branch B — *subagent* — `anonymous-quorum-binding` / `experiments/natural-primitives-failures/`

- **Source:** Subagent deliverable (integrated by main agent). Agent ID: `54cf20d9-3c07-47ab-9ad8-0d81ca888cea`.
- **Hypotheses H1/H2:** Per-signer Merkle material at `t = Θ(n)` is **Ω(n log n)** bits in naive model; BLS linear aggregate + verifier with only `C` yields **aggregate-key ambiguity** without `PK_S` or linear linking info.
- **Outcome:** **PASS** as *negative evidence* for naive stacks (Merkle-per-signer, hidden-`S` BLS black box, naive `t`-witness accumulator OR pattern fails sublinearity or soundness interface).
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/natural-primitives-failures/script.py`.

### Implications

- Main construction still **blocked**: no candidate primitive yet; both sub-problems remain **IN PROGRESS** (not SOLVED).
- Next iterations: UC/ideal-functionality game for exact verifier input; or hunt for **non-naive** assumption that breaks H1/H2 without SNARK verifier.

---

## Entry 002 — `verifier-oracle-model` / `experiments/aggregated-key-link-game/` (2026-03-30)

- **Hypothesis:** Any verifier that only checks a multisignature equation against a single claimed aggregate key `K` in `π`, without an explicit **`Link(C, K)`** (“`K` is the aggregation of ≥ `t` keys committed in `C`”), admits **strict under-quorum** acceptance by a full-key adversary.
- **Outcome:** **PASS** (interface / game level). Toy script: naive `Verify(C,m,(K,σ))` accepts `(t−1)`-subset aggregate; brute-force reference `Link` rejects under-quorum and accepts honest quorum (not a candidate scheme — specification oracle).
- **Key finding:** The **missing object** for the main problem is an **efficient** `Link` (or equivalent) compatible with sublinear `π` and no per-key verification material — consistent with `anonymous-quorum-binding` negative evidence.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/aggregated-key-link-game/script.py`.

---

## Entry 003 — `anonymous-quorum-binding` / `experiments/vc-opening-budget/` (2026-03-30)

- **Hypothesis:** Black-box `Link(C, K)` via **t** independent Merkle paths or **t**-fold naive OR of constant-size proofs scales **Ω(n)** or **Ω(n log n)** in proof bits when `t = ⌊n/2⌋ + 1`; single-path Merkle is sublinear but **does not** implement sound threshold `Link`.
- **Outcome:** **PASS** as idealized **verifier/proof-bit accounting** (not a reduction). Script tabulates models M1/M2/M3; asserts large `proof_bits/n` for M1 at `n=2048`.
- **Key finding:** Reinforces Entry **002**: necessary `Link` cannot be the “one cheap Merkle proof” pattern; standard multi-opening / disjunctive patterns clash with **sublinear** `π` at majority `t`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/vc-opening-budget/script.py`.

---

## Entry 004 — `verifier-oracle-model` / `experiments/f-link-ideal-spec/` (2026-03-30)

- **Hypothesis:** A coherent **ideal** `F_Link` exists for “`K` is aggregate of ≥ `t` keys under commitment `C`”; a **naive** real verifier that only checks `SigVerify(K,m,σ)` **separates** from this ideal (accepts under-quorum), while **compose**(`F_Link`, sig-check) rejects under-quorum.
- **Outcome:** **PASS** (spec + regression). Scripted `FLinkIdeal` with witness = index set `S`; toy `H(m‖K)` signature; composed verifier matches intended sound interface.
- **Key finding:** Makes explicit that **anonymous** realizations must implement the **same predicate** as `F_Link` **without** sending `|S| = Ω(t)` index witness in the clear — the remaining gap for sublinear `π`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/f-link-ideal-spec/script.py`.

---

## Entry 005 — `anonymous-quorum-binding` / `experiments/proof-system-verifier-rubric/` (2026-03-30)

- **Hypothesis:** A finite **verifier rubric** can partition proof families into `EXCLUDED_SNARK`, `GREY_TRANSPARENT` (IPA/Bulletproofs-style on **n-dependent** statements), and `ALLOWED_ATOMIC` (fixed BLS / single Merkle path) consistently with the main problem’s exclusion **intent**.
- **Outcome:** **PASS** (consistency / policy documentation only). Scripted table + assertions (Groth16 → excluded, BLS → atomic, ≥1 grey row).
- **Key finding:** Transparent **short proofs** can still sit in **GREY** when arithmetization of `F_Link`-style predicates is **Ω(n)** — clarifies that “no SNARK” is not synonymous with “no logarithmic proof size.”
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/proof-system-verifier-rubric/script.py`.

---

## Entry 006 — `verifier-oracle-model` / `experiments/simulator-bandwidth-toy/` (2026-03-30)

- **Hypothesis:** **H1** — anonymity does not need injective `S ↦ π`; **H2** — specifying `Agg(S)` among `U` distinct values needs `⌈log₂ U⌉` bits only if one insists on **lossless** labeling of aggregates; **H3** — simulator/`K`-marginal metaphor still points to **`Link(C, K)`** as the hard part.
- **Outcome:** **PASS** on **H1/H3** (conceptual); **INCONCLUSIVE** for cryptographic `|π|` lower bounds; **H2** illustrated with **integer subset-sum** enumeration (`U < W` for affine `pk_i` at small `n`).
- **Key finding:** **Do not** infer `|π| ≥ log₂ W` from “many majority subsets” alone; many subsets can share the same **additive** aggregate in a toy model — real security still requires **`Link`** to cryptographic keys, not just matching an integer sum.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/simulator-bandwidth-toy/script.py`.

---

## Entry 007 — `anonymous-quorum-binding` / `experiments/random-aggregate-injectivity-mc/` (2026-03-30)

- **Hypothesis:** For i.i.d. **large-range** integer `pk_i` (proxy for random scalars), strict-majority subset-sum map is **injective** (`U = W`) with probability **≈ 1** at `n = 10` (Monte Carlo); contrasts Entry **006** where **small affine** keys had **`U ≪ W`**.
- **Outcome:** **PASS.** `T = 400`, `M = 2^50`, seed `42`: **fraction `U = W` = 1.0**; baseline affine `pk_i = 1000 + 13 i` gives **`U = 75`**, **`W = 386`**.
- **Key finding:** Do not over-read Entry **006** as “aggregates are ambiguous in practice”; **structured small integers** exaggerate subset-sum collisions. **`Link(C, K)`** is still required for soundness; this experiment only calibrates the **toy model**.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/random-aggregate-injectivity-mc/script.py`.

---

## Entry 008 — `anonymous-quorum-binding` / `experiments/rogue-key-aggregate-collision/` (2026-03-30)

- **Hypothesis:** An adversary choosing `pk_i` can force **two distinct strict-majority subsets** to have the **same** additive aggregate (integer toy), so “`K` alone identifies the quorum” fails under **malicious registration** without **`Link`** / policy.
- **Outcome:** **PASS.** Explicit `n = 6`, `pk = [1,1,5,5,5,5]`, `S₁ = (0,1,2,3)`, `S₂ = (0,1,4,5)`, both majority, **`Agg = 12`**, **`U < W`** over all majority subsets.
- **Key finding:** **Bridges 006–007:** honest random keys can look injective; **rogue** keys restore **aggregate ambiguity** — sound real protocols need **`Link(C, K)`** and explicit **registration** assumptions (PoP etc. in real groups).
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/rogue-key-aggregate-collision/script.py`.

---

## Entry 009 — `anonymous-quorum-binding` / `experiments/threat-model-registration-assumptions/` + problem-statement patches (2026-03-30)

- **Hypothesis:** Journal entries **002–008** partition cleanly into **verifier-input**, **honest vs malicious registration**, **VC budgets**, and **proof-system rubric** axes without contradiction.
- **Outcome:** **PASS.** Scripted summary table; **main** `main-problem/problem-statement.md` and both sub-problem `problem-statement.md` files extended with **Threat model** / **Threat model hook** paragraphs (verifier input; honest vs adversarial `pk_i`; pointers to **006–008**).
- **Key finding:** Soundness write-ups must **name** the registration model; **`Link(C, K)`** remains orthogonal to IID injectivity (**007**) vs rogue collisions (**008**).
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/threat-model-registration-assumptions/script.py`.

---

## Entry 010 — `verifier-oracle-model` / `experiments/relaxation-ladder/` (2026-03-30)

- **Hypothesis:** Each **standard** repair to the documented barriers maps to a **relaxation** **R1–R6** of the main constraints; only slot **R7** (“novel primitive”) is marked **main-compliant** in the taxonomy script.
- **Outcome:** **PASS** (taxonomy); **INCONCLUSIVE** on realizability of **R7**. Ladder ties **002–005** to typical escape hatches (linear `π`, revealed `S`, extra verifier data, SNARK, trusted setup, TEE).
- **Key finding:** Clarifies **search space**: a full solution is **R7** or an unstated loophole; **ABANDON** / revised problem should name which **R_i** is adopted.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/relaxation-ladder/script.py`.

---

## Entry 011 — `anonymous-quorum-binding` / `experiments/r1-baseline-linear-proof-sound/` (2026-03-30)

- **Hypothesis:** Under **R1** (linear-size `π`: Merkle path per signer + aggregate `K` + toy signature), a **toy** `Verify(C, m, π)` using only `(C, m, π)` is **sound** against strict under-quorum in this model.
- **Outcome:** **PASS.** `n = 8`, `t = 5`, power-of-2 Merkle; honest majority **accepts**; `|S| = t − 1` **rejects**; mismatched `K` **rejects**.
- **Key finding:** **Compactness** is the missing axis — a **fully linear** witness **does** supply **`Link`-grade** binding; aligns with **003** and **010** (**R1** escape hatch).
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/r1-baseline-linear-proof-sound/script.py`.

---

## Entry 012 — `verifier-oracle-model` / `experiments/sublinear-pi-merkle-clash/` (2026-03-30)

- **Hypothesis:** **M1** majority Merkle-per-signer bit count **`Θ(n · λ · log n)`** eventually dominates a stylized **`o(n)`-ish** cap **`B(n) = λ · (log₂ n)²`**; numerical clash at moderate **`n`**.
- **Outcome:** **PASS.** Table for **`n ∈ {128,…,8192}`**; at **`n = 2048`**, **`M1_total / B(n) ≈ 94`** (asserted **`> 85`**).
- **Key finding:** Pairs with **011**: **R1** soundness **vs** **main** compactness — naive **M1** is not a sublinear witness; reinforces **003**.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/sublinear-pi-merkle-clash/script.py`.

---

## Entry 013 — `anonymous-quorum-binding` / `experiments/unbound-quorum-field-attack/` (2026-03-30)

- **Hypothesis:** A **constant-size** extension `π = (K, σ, \hat{k})` with **unauthenticated** claimed quorum size `\hat{k} ≥ t` plus **only** `SigVerify` does **not** prevent **strict under-quorum** acceptance (adversary sets `\hat{k} = t` while `K` comes from **`t − 1`** keys).
- **Outcome:** **PASS** (attack **succeeds** — the extension is **unsound**). Toy demo: `n = 8`, `t = 5`, `|S| = 4`, lied `\hat{k} = 5`, verify **accepts**.
- **Key finding:** **R7** cannot be “add a few bits of **unbound** count”; threshold evidence must be **algebraically / cryptographically linked** to `C` and signing — same **`Link`** bottleneck as **002** / **004**.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/unbound-quorum-field-attack/script.py`.

---

## Entry 014 — `anonymous-quorum-binding` / `experiments/commitment-root-mismatch-attack/` (2026-03-30)

- **Hypothesis:** If path verification uses a root **supplied inside** `π` (or otherwise ignores the verifier’s on-chain commitment `C`), an adversary can present proofs internally consistent for **`C' ≠ C`**, with a valid majority signature on the **`C'`** key set, while the chain holds **`C`**.
- **Outcome:** **PASS** (attack **succeeds** on flawed interface). Two disjoint 8-leaf Merkle worlds; sound verifier rejects; flawed verifier accepts.
- **Key finding:** **`Link`-grade binding for Merkle witnesses includes `root(recomputed from π) == C`** from verifier state — not only binding of aggregate `K` (**002**); pairs with **013** as another “easy break” if threshold/set binding is mishandled.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/commitment-root-mismatch-attack/script.py`.

---

## Entry 015 — `verifier-oracle-model` / `experiments/coalition-index-entropy-vs-sublinear-cap/` (2026-03-30)

- **Hypothesis:** In an **injective minimal-coalition indexing** model, a proof must carry **≥ ⌈log₂ C(n, t)⌉** bits for \(t = \lfloor n/2\rfloor+1\); numerically **log₂ C(n,t)** (via log-sum) eventually exceeds the same stylized polylog cap **B(n) = 256·(log₂ n)²** used in Entry **012**.
- **Outcome:** **PASS** (combinatorics only). Table through **`n = 262144`**; first crossover in table at **`n = 131072`** (**65536** ratio **≈ 0.9999**, still below).
- **Key finding:** **Lossless “which majority coalition”** witnesses are **Ω(n)** bits at scale and **outgrow** the toy **B(n)** — consistent with **006** that **anonymity** is exactly what blocks applying this as a direct **|π|** lower bound for the main goal; still sharpens **verifier-oracle** / witness-model hygiene.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/coalition-index-entropy-vs-sublinear-cap/script.py`.

---

## Entry 016 — `anonymous-quorum-binding` / `experiments/claimed-k-not-equal-opened-sum-attack/` (2026-03-30)

- **Hypothesis:** With valid **majority** Merkle paths into `C`, if `Verify` checks `SigVerify(K,m,σ)` but **omits** **`K = \sum_{i\in S} pk_i`** over the opened keys, an adversary can get **accept** while **`K` mismatches** the keys attested by the paths.
- **Outcome:** **PASS** (attack **succeeds** on flawed interface). `K_adv = K_sum + 999_999`, same `|S| = t`, valid paths; **sound** (sum check) **rejects**; **flawed** **accepts**.
- **Key finding:** **Membership paths ≠ aggregate binding** for the signing key field; complements **011** by isolating the **algebraic consistency** line item (still within **R1**-scale witnesses, not a compact solution).
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/claimed-k-not-equal-opened-sum-attack/script.py`.

---

## Entry 017 — `verifier-oracle-model` / `experiments/strict-majority-subset-count-closed-form/` (2026-03-30)

- **Hypothesis:** Let \(N(n)=\sum_{k=\lfloor n/2\rfloor+1}^{n}\binom{n}{k}\). Then **odd** \(n\Rightarrow N(n)=2^{n-1}\); **even** \(n\Rightarrow N(n)=(2^n-\binom{n}{n/2})/2\); brute matches for small \(n\).
- **Outcome:** **PASS.** Verified **\(n=1..25\)** by brute; table for sample **\(n\) up to 128**; odd rows satisfy **\(N=2^{n-1}\)**.
- **Key finding:** Uniform “which strict-majority coalition” has **\(\log_2 N(n)=n-1\)** for odd **\(n\)** — a clean **full-family** counting complement to **015**’s **minimal-\(t\)** \(\log_2\binom{n}{t}\) track; still **not** a cryptographic \(|\pi|\) bound when anonymity collapses many witnesses (**006**).
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/strict-majority-subset-count-closed-form/script.py`.

---

## Entry 018 — `anonymous-quorum-binding` / `experiments/duplicate-signer-index-attack/` (2026-03-30)

- **Hypothesis:** If `Verify` demands `len(S) ≥ t` and valid Merkle paths for each coordinate of `S` plus multiplicity-correct `K = \sum_{i\in S} pk_i`, but **does not** require **distinct** signer indices, then **one** key (index repeated **`t`** times) suffices for **accept** — not **`t`** distinct validators.
- **Outcome:** **PASS** (attack **succeeds**). `S = (0,0,0,0,0)`, `t = 5`, valid paths; **sound** verifier **rejects**; **flawed** **accepts**.
- **Key finding:** **`t` list slots ≠ t-person quorum**; **011**’s injectivity check is a **necessary** part of the R1-style interface, not redundant with path count alone.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/duplicate-signer-index-attack/script.py`.

---

## Entry 019 — `verifier-oracle-model` / `experiments/r1-style-verify-hash-ops-scaling/` (2026-03-30)

- **Hypothesis:** Sound **R1-style** Merkle re-verification for **`t = \lfloor n/2\rfloor+1`** signers uses **`t \cdot (1 + \lceil\log_2 n\rceil)`** toy hash units (leaf + path) per signer, hence **Θ(n log n)** for **`t = Θ(n)`**, not **O(1)**.
- **Outcome:** **PASS** (accounting). Table **n = 8 .. 8192** (powers of two); e.g. **n = 2048** gives **12300** Merkle-hash units; **t·(1+depth)/(n log₂ n) ≈ 0.546** at **n = 2048**.
- **Key finding:** **Standard compute** for the **known-sound** linear witness is **heavy** at scale — complements **012** (**|π|**) and **011** (soundness) along the **verifier-oracle** axis.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/r1-style-verify-hash-ops-scaling/script.py`.

---

## Entry 020 — `anonymous-quorum-binding` / `experiments/toy-signature-omits-message-attack/` (2026-03-30)

- **Hypothesis:** A toy verify step **`σ == H(BAD|K)`** that **omits** **`m`** admits the **same** **`(K, σ)`** for **two** different messages; **`H(SIG|m|K)`** does **not**.
- **Outcome:** **PASS.** **`σ_bad`** verifies under the flawed rule for both **`finalize-epoch-9`** and **`rollback-epoch-9`**; sound rule **rejects** **`m₂`** given **`σ_good`** for **`m₁`**.
- **Key finding:** **Message binding** is orthogonal to **quorum / Merkle / `Link`** checks — another **easy-break** interface dimension alongside **013–018**.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/toy-signature-omits-message-attack/script.py`.

---

## Entry 021 — `verifier-oracle-model` / `experiments/f2-linear-measurements-threshold-ambiguity/` (2026-03-30)

- **Hypothesis:** For **n = 8**, **t = 5**, exist **x** (majority) and **y** (one below threshold) and **n−1** **independent** **F₂** linear pools **r_j** with **r_j·x = r_j·y** for all **j** (parity measurements identical on both patterns).
- **Outcome:** **PASS.** Explicit **x** on **5** bits, **y** on **4** bits, **d = x⊕y** weight **1**; greedy **7** independent **r_j ⊥ d**; all pool bits match.
- **Key finding:** **Fixed linear parity pooling** alone cannot **intrinsically** encode strict-majority vs sub-threshold separation — same syndrome class trick as **coding**; complements **019** (**compute**) and **`Link`** narrative (**002–004**). **Analogy pass** recorded in `hypothesis.md`.
- **Structured journal:** `research-journal/entries/2026-03-30-f2-linear-measurements-threshold-ambiguity.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/f2-linear-measurements-threshold-ambiguity/script.py`.

---

## Entry 022 — `anonymous-quorum-binding` / `experiments/polynomial-single-eval-ambiguity-toy/` (2026-03-30)

- **Hypothesis:** Over **𝔽_p** with nodes **0..n−1** and **r ∉ nodes**, **two** **different** leaf vectors **v ≠ w** can satisfy **Σ v_i L_i(r) = Σ w_i L_i(r)** (same **single** interpolant evaluation).
- **Outcome:** **PASS.** **p = 1009**, **n = 8**, **r = 900**; constructed **w** with **Hamming(v,w)=8**, shared **P(r)=901**.
- **Key finding:** **Encoding-change** (polynomial / **RS-style** values) still hits **identifiability**: **one** evaluation is **one** linear constraint on **n** unknowns — not a quorum certificate. **Analogy pass** in `hypothesis.md`.
- **Structured journal:** `research-journal/entries/2026-03-30-polynomial-single-eval-ambiguity-toy.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/polynomial-single-eval-ambiguity-toy/script.py`.

---

## Entry 023 — `verifier-oracle-model` / `experiments/parity-count-summary-quorum-collision/` (2026-03-30)

- **Hypothesis:** For **n = 10**, **t = 6**, **h(k) = k mod 2** satisfies **h(4) = h(6)** while **4 < t** and **6 ≥ t** — no verifier seeing **only** **h(k)** can implement **k ≥ t** exactly.
- **Outcome:** **PASS.** Explicit collision on **parity** of signer count across the threshold boundary.
- **Key finding:** **Lossy** **1-bit** count summaries **alias** across **quorum** vs **under-quorum**; complements **021** (**F₂** mask alignment) and **022** (**𝔽_p** eval) as another “**insufficient observable**” template. **Analogy pass** in `hypothesis.md`.
- **Structured journal:** `research-journal/entries/2026-03-30-parity-count-summary-quorum-collision.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/parity-count-summary-quorum-collision/script.py`.

---

## Entry 024 — `anonymous-quorum-binding` / `experiments/polynomial-two-eval-binary-collision/` (2026-03-30)

- **Hypothesis:** For **Lagrange** nodes **0..n−1** and two queries **r₁,r₂ ∉ nodes** over **𝔽_p**, when **2ⁿ > p²** there exist **distinct** **v ≠ w ∈ {0,1}ⁿ** with **(P_v(r₁), P_v(r₂)) = (P_w(r₁), P_w(r₂))**.
- **Outcome:** **PASS.** **p = 97**, **n = 16**, **r₁ = 90**, **r₂ = 91**; brute-force bucket finds collision at **(18, 41)**, **Hamming(v,w) = 6**.
- **Key finding:** **Binary** participation vectors are **not** injectively fingerprinted by **two** polynomial evaluations alone — extends **022** with **{0,1}** restriction and **pigeonhole** barrier (**k** probes → **≤ pᵏ** buckets vs **2ⁿ** patterns).
- **Structured journal:** `research-journal/entries/2026-03-30-polynomial-two-eval-binary-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/polynomial-two-eval-binary-collision/script.py`.

---

## Entry 025 — `verifier-oracle-model` / `experiments/star-independent-minmax-eigenvalue-quorum-collision/` (2026-03-30)

- **Hypothesis:** On **K_{1,9}** (**n = 10**, **t = 6**), **leaf-only** **S_a** (**5** leaves) and **S_b** (**6** leaves) induce **edgeless** **G[S]**; **(λ_max, λ_min)** of **adjacency** both **(0, 0)**.
- **Outcome:** **PASS.** `numpy.linalg.eigvalsh` on **zero** induced blocks.
- **Key finding:** **Two-float** extremal **adjacency** spectrum does **not** separate **under-quorum** vs **quorum** when active sets sit in a **large independent** set — first in-repo **spectral** straw (digest thread); complements **023**/**024** **lossy-summary** pattern.
- **Structured journal:** `research-journal/entries/2026-03-30-star-independent-minmax-eigenvalue-quorum-collision.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/star-independent-minmax-eigenvalue-quorum-collision/script.py`.

---

## Entry 026 — `verifier-oracle-model` / `experiments/clique-induced-adjacency-max-eigenvalue-recovers-size/` (2026-03-30)

- **Hypothesis:** Host **G = K_n** ⇒ **G[S] ≅ K_{|S|}** ⇒ **λ_max(A(G[S])) = |S| − 1**; **n = 10**, **t = 6**, **|S| = 5** vs **6** ⇒ **λ_max** **4** vs **5**.
- **Outcome:** **PASS.** Numeric check with **numpy.linalg.eigvalsh** (float tolerance).
- **Key finding:** **Positive** **control** to **025**: **spectral** **extrema** **can** **encode** **|S|** when **induced** subgraphs are **full** **cliques**; **failures** track **large** **independent** **sets**, not **spectra** **tout** **court**.
- **Structured journal:** `research-journal/entries/2026-03-30-clique-induced-adjacency-max-eigenvalue-recovers-size.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/clique-induced-adjacency-max-eigenvalue-recovers-size/script.py`.

---

## Entry 027 — `verifier-oracle-model` / `experiments/biclique-large-part-minmax-eigenvalue-quorum-collision/` (2026-03-30)

- **Hypothesis:** **G = K_{3,7}** on **10** vertices; **S_a**, **S_b** subsets of the **7**-vertex part with **|S_a|=5**, **|S_b|=6** (**t=6**) induce **edgeless** graphs ⇒ **(λ_max,λ_min)=(0,0)** for **both**.
- **Outcome:** **PASS.** **21** cross edges; **numpy** eigen check.
- **Key finding:** **Dense** **bipartite** **host** still **collapses** **min/max** **adjacency** **spectrum** **across** **quorum** if **α(G)≥t** — **intermediate** **density** **between** **025** and **026**; **moral:** need **α(G)<t** (or **similar**) to **force** **internal** **edges** **on** **quorums**.
- **Structured journal:** `research-journal/entries/2026-03-30-biclique-large-part-minmax-eigenvalue-quorum-collision.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/biclique-large-part-minmax-eigenvalue-quorum-collision/script.py`.

---

## Entry 028 — `verifier-oracle-model` / `experiments/k6-plus-isolates-alpha-lt-t-lambda-max-separates/` (2026-03-30)

- **Hypothesis:** **G = K_6 ∪ 4K_1** (**n=10**), **t=6**, **α(G)=5**; **S_a={0,1,2,3,4}** **independent** **⇒** **λ_max=0**; **S_b={0,1,2,3,4,5}** **induces** **K_2** **⇒** **λ_max=1**.
- **Outcome:** **PASS.**
- **Key finding:** **α(G)<t** **positive** **toy** — **quorum** **witness** **can** **force** **λ_max>0** **while** **exhibited** **sub-quorum** **stays** **at** **0**; **pairs** **with** **027** **moral** **without** **claiming** **full** **injectivity** **of** **λ_max** **on** **all** **6**-**sets**.
- **Structured journal:** `research-journal/entries/2026-03-30-k6-plus-isolates-alpha-lt-t-lambda-max-separates.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/k6-plus-isolates-alpha-lt-t-lambda-max-separates/script.py`.

---

## Entry 029 — `verifier-oracle-model` / `experiments/k6-plus-isolates-two-sixsets-same-minmax-diff-edges/` (2026-03-30)

- **Hypothesis:** **Two** **6**-**subsets** **with** **different** **induced** **|E|** **share** **(λ_max,λ_min)** **on** **a** **fixed** **host** **(4** **isolates** **+** **3** **disjoint** **edges;** **not** **K_6** **—** **see** **hypothesis)**.
- **Outcome:** **PASS.**
- **Key finding:** **K_2+isolates** **vs** **2K_2+isolates** **both** **(1,−1)** **at** **t=6** **—** **two-float** **adjacency** **extrema** **underdetermine** **pattern** **even** **when** **|S|** **fixed** **at** **quorum**.
- **Structured journal:** `research-journal/entries/2026-03-30-k6-plus-isolates-two-sixsets-same-minmax-diff-edges.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/k6-plus-isolates-two-sixsets-same-minmax-diff-edges/script.py`.

---

## Entry 030 — `verifier-oracle-model` / `experiments/tropical-min-pool-summary-quorum-collision/` (2026-03-30)

- **Hypothesis:** **h(S) = min_{i∈S} c_i** **with** **c_i = i**; **S_a** **(5** **verts)** **and** **S_b** **(6** **verts)** **both** **contain** **0** **⇒** **h = 0** **each** **across** **t = 6**.
- **Outcome:** **PASS.**
- **Key finding:** **Min-plus** **/** **bottleneck** **one-number** **summary** **parallel** **to** **021** **(F₂)** **and** **023** **(parity)** **—** **shared** **argmin** **hides** **|S|** **vs** **t**.
- **Structured journal:** `research-journal/entries/2026-03-30-tropical-min-pool-summary-quorum-collision.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/tropical-min-pool-summary-quorum-collision/script.py`.

---

## Entry 031 — `anonymous-quorum-binding` / `experiments/polynomial-three-eval-binary-collision/` (2026-03-30)

- **Hypothesis:** For **Lagrange** nodes **0..n−1** and three queries **r₁,r₂,r₃ ∉ nodes** over **𝔽_p**, when **2ⁿ > p³** there exist **distinct** **v ≠ w ∈ {0,1}ⁿ** with identical **(P_v(r₁), P_v(r₂), P_v(r₃))**.
- **Outcome:** **PASS.** **p = 97**, **n = 20**, **r₁ = 90**, **r₂ = 91**, **r₃ = 92**; brute-force bucket finds collision at triple **(47, 73, 95)**, **Hamming(v, w) = 8**.
- **Key finding:** **Three** polynomial evaluations still **do not** injectively fingerprint arbitrary **binary** participation — extends **022**/**024**; **k** probes → **≤ pᵏ** buckets vs **2ⁿ** patterns.
- **Structured journal:** `research-journal/entries/2026-03-30-polynomial-three-eval-binary-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/polynomial-three-eval-binary-collision/script.py`.

---

## Entry 032 — `verifier-oracle-model` / `experiments/petersen-sixset-laplacian-spectrum-collision/` (2026-03-30)

- **Hypothesis:** On **Petersen** (**n = 10**, **3-regular**), **distinct** **6**-subsets **S ≠ T** exist with **identical** **sorted** **Laplacian** eigenvalues of **G[S]** and **G[T]**.
- **Outcome:** **PASS.** **S₁ = {0,1,2,3,4,5}**, **S₂ = {0,1,2,3,4,6}**; shared **6**-tuple **(0, 0.697…, 1.382…, 2, 3.618…, 4.302…)** (numerical **eigvalsh**).
- **Key finding:** **Full** induced **Laplacian** spectrum — **richer** than **(λ_max, λ_min)** — still **aliases** between **quorum-sized** patterns on a **standard** **expander** **toy** (**automorphism** / **isospectral** induced subgraphs).
- **Structured journal:** `research-journal/entries/2026-03-30-petersen-sixset-laplacian-spectrum-collision.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/petersen-sixset-laplacian-spectrum-collision/script.py`.

---

## Entry 033 — `verifier-oracle-model` / `experiments/random-cubic-10-laplacian-sixset-injective/` (2026-03-30)

- **Hypothesis:** **Some** **`networkx.random_regular_graph(3, 10, seed)`** **has** **pairwise** **distinct** **sorted** **induced** **Laplacian** **spectra** **on** **all** **C(10,6)=210** **6**-**subsets** **(8**-**decimal** **keys,** **as** **032).**
- **Outcome:** **FAIL.** **Seeds** **0..99 999** **—** **no** **injective** **instance;** **collisions** **typically** **very** **early** **(often** **single-vertex** **swap** **between** **6**-**sets).**
- **Key finding:** **Full** **induced** **L**-**spectrum** **does** **not** **fingerprint** **S** **even** **for** **generic** **labeled** **cubics** **in** **this** **scan** **—** **extends** **032** **beyond** **global** **automorphism** **story.**
- **Structured journal:** `research-journal/entries/2026-03-30-random-cubic-10-laplacian-sixset-injective.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/random-cubic-10-laplacian-sixset-injective/script.py` **(requires** **networkx).**

---

## Entry 034 — `anonymous-quorum-binding` / `experiments/zmodm-weighted-sum-five-vs-six-collision/` (2026-03-30)

- **Hypothesis:** **Public** **weights** **w_i = i+1** **on** **n=10;** **∃M∈[2,50]** **with** **some** **5**-**subset** **and** **6**-**subset** **having** **equal** **Σ w_i (mod M).**
- **Outcome:** **PASS.** **First** **hit** **M=2:** **5**-**set** **(4,6,7,8,9)** **sum** **39≡1,** **6**-**set** **(0,1,2,3,4,5)** **sum** **21≡1.**
- **Key finding:** **Single** **modular** **linear** **aggregate** **does** **not** **certify** **threshold** **(parity** **overlap);** **parallel** **to** **023** **but** **with** **nontrivial** **weights.**
- **Structured journal:** `research-journal/entries/2026-03-30-zmodm-weighted-sum-five-vs-six-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/zmodm-weighted-sum-five-vs-six-collision/script.py`.

---

## Entry 035 — `anonymous-quorum-binding` / `experiments/linear-weights-integer-sum-five-six-collision/` (2026-03-30)

- **Hypothesis:** **For** **w_i = i+1** **(n=10),** **some** **5**-**subset** **and** **6**-**subset** **have** **equal** **integer** **Σ w_i.**
- **Outcome:** **PASS.** **Sum** **21:** **5**-**set** **(1,2,3,4,6)** **→** **2+3+4+5+7;** **6**-**set** **(0,1,2,3,4,5)** **→** **1+…+6.**
- **Key finding:** **Even** **without** **modular** **reduction,** **one** **additive** **scalar** **does** **not** **separate** **sub-quorum** **from** **quorum** **—** **strengthens** **034.**
- **Structured journal:** `research-journal/entries/2026-03-30-linear-weights-integer-sum-five-six-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/linear-weights-integer-sum-five-six-collision/script.py`.

---

## Entry 036 — `verifier-oracle-model` / `experiments/nonadaptive-four-query-participation-indistinguishable/` (2026-03-30)

- **Hypothesis:** **For** **n=10,** **t=6,** **every** **Q** **with** **|Q|=4** **admits** **a,** **b** **with** **wt(a)=5,** **wt(b)=6** **and** **a|_Q=b|_Q.**
- **Outcome:** **PASS.** **Explicit** **construction** **(zeros** **on** **Q,** **5** **vs** **6** **ones** **on** **six** **outside** **indices);** **all** **C(10,4)=210** **Q** **checked.**
- **Key finding:** **Non-adaptive** **four** **membership** **queries** **do** **not** **information-theoretically** **separate** **sub-quorum** **from** **quorum** **in** **this** **bit-probe** **toy** **—** **query-budget** **template** **alongside** **|π|** **/ ** **019** **hash** **scaling.**
- **Structured journal:** `research-journal/entries/2026-03-30-nonadaptive-four-query-participation-indistinguishable.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/nonadaptive-four-query-participation-indistinguishable/script.py`.

---

## Entry 037 — `verifier-oracle-model` / `experiments/four-bit-partial-view-both-threshold-classes/` (2026-03-30)

- **Hypothesis:** **For** **n=10,** **every** **Q** **with** **|Q|≤4** **and** **every** **pattern** **p** **on** **Q** **admits** **both** **a** **wt=5** **and** **a** **wt=6** **global** **extension** **matching** **p** **on** **Q.**
- **Outcome:** **PASS.** **4521** **(Q,p)** **pairs** **—** **feasibility** **0≤5−z≤R** **and** **0≤6−z≤R** **for** **R=n−|Q|,** **z=** **ones** **of** **p** **on** **Q.**
- **Key finding:** **Stronger** **than** **036:** **not** **only** **a** **collision** **per** **fixed** **Q,** **but** **every** **≤4**-**bit** **partial** **view** **is** **ambiguous** **between** **sub-quorum** **and** **quorum** **⇒** **adaptive** **depth-4** **distinct** **coordinate** **queries** **cannot** **separate** **in** **this** **toy.**
- **Structured journal:** `research-journal/entries/2026-03-30-four-bit-partial-view-both-threshold-classes.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/four-bit-partial-view-both-threshold-classes/script.py`.

---

## Entry 038 — `verifier-oracle-model` / `experiments/five-bit-partial-view-feasibility-z0/` (2026-03-30)

- **Hypothesis:** **For** **n=10,** **|Q|=5,** **R=5,** **wt=6** **extension** **exists** **iff** **z≥1** **on** **Q;** **wt=5** **always** **for** **z≤5.**
- **Outcome:** **PASS.** **8064** **(Q,p)** **—** **7812** **both** **classes,** **252** **(z=0)** **only** **wt=5** **(no** **quorum** **completion).**
- **Key finding:** **Five** **coordinate** **probes** **exclude** **quorum** **only** **on** **the** **all-zero** **5**-**bit** **pattern;** **~96.9%** **of** **partial** **views** **still** **ambiguous** **5** **vs** **6.**
- **Structured journal:** `research-journal/entries/2026-03-30-five-bit-partial-view-feasibility-z0.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/five-bit-partial-view-feasibility-z0/script.py`.

---

## Entry 039 — `verifier-oracle-model` / `experiments/six-bit-partial-view-feasibility-z-bands/` (2026-03-30)

- **Hypothesis:** **For** **n=10,** **|Q|=6,** **R=4,** **(z=0)** **neither** **wt=5/6;** **z=1** **only** **wt=5;** **z=2..5** **both;** **z=6** **only** **wt=6.**
- **Outcome:** **PASS.** **13440** **(Q,p)** **—** **both** **11760,** **only_wt5** **1260,** **only_wt6** **210,** **neither** **210.**
- **Key finding:** **Six** **probes** **—** **87.5%** **of** **6**-**bit** **patterns** **per** **Q** **still** **ambiguous** **5** **vs** **6;** **all-zero** **prefix** **→** **neither** **class** **(wt≤4);** **all-one** **→** **only** **quorum** **completion.**
- **Structured journal:** `research-journal/entries/2026-03-30-six-bit-partial-view-feasibility-z-bands.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/six-bit-partial-view-feasibility-z-bands/script.py`.

---

## Entry 040 — `verifier-oracle-model` / `experiments/seven-bit-partial-view-feasibility-z-bands/` (2026-03-30)

- **Hypothesis:** **n=10,** **|Q|=7,** **R=3:** **z∈{0,1,7}** **neither;** **z=2** **only_wt5;** **z=3..5** **both;** **z=6** **only_wt6.**
- **Outcome:** **PASS.** **15360** **(Q,p)** **—** **both** **10920,** **only_wt5** **2520,** **only_wt6** **840,** **neither** **1080.**
- **Key finding:** **71%** **of** **7**-**bit** **patterns** **per** **Q** **still** **ambiguous** **5** **vs** **6;** **neither** **region** **grows** **(z=1** **added).**
- **Structured journal:** `research-journal/entries/2026-03-30-seven-bit-partial-view-feasibility-z-bands.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/seven-bit-partial-view-feasibility-z-bands/script.py`.

---

## Entry 041 — `verifier-oracle-model` / `experiments/eight-bit-partial-view-feasibility-z-bands/` (2026-03-30)

- **Hypothesis:** **n=10,** **|Q|=8,** **R=2:** **z∈{0,1,2,7,8}** **neither;** **z=3** **only_wt5;** **z=4,5** **both;** **z=6** **only_wt6.**
- **Outcome:** **PASS.** **11520** **(Q,p)** **—** **both** **5670,** **only_wt5** **2520,** **only_wt6** **1260,** **neither** **2070.**
- **Key finding:** **126/256** **≈** **49%** **per** **Q** **still** **ambiguous** **5** **vs** **6** **—** **first** **k** **with** **“both”** **<** **50%;** **neither** **46/256** **≈** **18%.**
- **Structured journal:** `research-journal/entries/2026-03-30-eight-bit-partial-view-feasibility-z-bands.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/eight-bit-partial-view-feasibility-z-bands/script.py`.

---

## Entry 042 — `verifier-oracle-model` / `experiments/nine-bit-partial-view-feasibility-z-bands/` (2026-03-30)

- **Hypothesis:** **n=10,** **|Q|=9,** **R=1:** **z∈{0..3,7..9}** **neither;** **z=4** **only_wt5;** **z=5** **both;** **z=6** **only_wt6.**
- **Outcome:** **PASS.** **5120** **(Q,p)** **—** **both** **1260,** **only_wt5** **1260,** **only_wt6** **840,** **neither** **1760.**
- **Key finding:** **R=1** **⇒** **“both”** **only** **at** **z=5** **(126/512** **≈** **24.6%** **per** **Q);** **coordinate** **probe** **series** **for** **(10,6)** **complete** **through** **k=9** **(k=10** **degenerate).**
- **Structured journal:** `research-journal/entries/2026-03-30-nine-bit-partial-view-feasibility-z-bands.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/nine-bit-partial-view-feasibility-z-bands/script.py`.

---

## Entry 043 — `verifier-oracle-model` / `experiments/partial-view-z-interval-formula-regression/` (2026-03-30)

- **Hypothesis:** **Per**-**Q** **cell** **weights** **for** **wt** **t−1** **vs** **t** **=** **Σ_z** **binom(k,z)** **over** **z**-**interval** **intersections;** **global** **=** **C(n,k)** **×** **per**-**Q** **—** **matches** **brute** **enumeration.**
- **Outcome:** **PASS** **(n=10,t=6,k=4..9** **regression** **+** **spot** **cases).**
- **Key finding:** **037–042** **counts** **are** **a** **pure** **closed** **form;** **see** **`results.md`** **for** **I(w)** **=** **[max(0,w−R),** **min(k,w)].**
- **Structured journal:** `research-journal/entries/2026-03-30-partial-view-z-interval-formula-regression.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/partial-view-z-interval-formula-regression/script.py`.

---

## Entry 044 — `anonymous-quorum-binding` / `experiments/polynomial-two-eval-small-n-injective-witness/` (2026-03-30)

- **Hypothesis:** **n=10,** **p=97,** **2^n** **<** **p²:** **some** **(r1,r2)** **gives** **injective** **v** **↦** **(P(r1),P(r2))** **on** **{0,1}^n.**
- **Outcome:** **PASS.** **First** **witness** **(10,26);** **95** **injective** **pairs** **/ ** **3741** **tested;** **(90,91)** **still** **collides** **(contrast** **024).**
- **Key finding:** **024** **collisions** **are** **driven** **by** **2^n** **>** **p²** **(n=16);** **small** **n** **allows** **two**-**probe** **Lagrange** **labeling** **of** **all** **binary** **leaves** **for** **chosen** **r.**
- **Structured journal:** `research-journal/entries/2026-03-30-polynomial-two-eval-small-n-injective-witness.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/polynomial-two-eval-small-n-injective-witness/script.py`.

---

## Entry 045 — `verifier-oracle-model` / `experiments/adaptive-coordinate-tree-depth-wt-five-vs-six/` (2026-03-30)

- **Hypothesis:** **Adaptive** **coordinate-only** **decision** **trees** **on** **n=10** **masks** **with** **wt∈{5,6}** **need** **worst-case** **depth** **10** **to** **purely** **split** **weights** **(not** **4).**
- **Outcome:** **PASS** **—** **memoized** **backtracking:** **no** **tree** **depth** **≤** **9;** **depth** **10** **works.**
- **Key finding:** **wt=5** **and** **wt=6** **vectors** **differing** **only** **at** **j** **agree** **on** **all** **other** **coordinate** **queries** **⇒** **must** **eventually** **query** **every** **index** **in** **the** **worst** **case.**
- **Structured journal:** `research-journal/entries/2026-03-30-adaptive-coordinate-tree-depth-wt-five-vs-six.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-tree-depth-wt-five-vs-six/script.py`.

---

## Entry 046 — `anonymous-quorum-binding` / `experiments/pair-count-mod-m-threshold-collision/` (2026-03-30)

- **Hypothesis:** **Unweighted** **pair** **count** **C(|S|,2)** **mod** **M** **collides** **for** **|S|=t−1** **vs** **t** **when** **M** **|** **(t−1);** **t=6** **⇒** **M=5** **gives** **10≡15≡0** **(mod** **5).**
- **Outcome:** **PASS** **(identity** **C(t,2)−C(t−1,2)=t−1** **+** **regression** **loop).**
- **Key finding:** **Degree-2** **symmetric** **statistic** **on** **binary** **indicators** **depends** **only** **on** **|S|;** **modular** **reduction** **kills** **t−1** **vs** **t** **separation** **iff** **M** **divides** **t−1.**
- **Structured journal:** `research-journal/entries/2026-03-30-pair-count-mod-m-threshold-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/pair-count-mod-m-threshold-collision/script.py`.

---

## Entry 047 — `anonymous-quorum-binding` / `experiments/elementary-symmetric-adjacent-mod-collision/` (2026-03-30)

- **Hypothesis:** **C(t,d)−C(t−1,d)=C(t−1,d−1)** **(Pascal);** **mod** **M** **collision** **for** **C(|S|,d)** **at** **|S|∈{t−1,t}** **iff** **M** **|** **C(t−1,d−1).**
- **Outcome:** **PASS** **(t<40,** **d≤min(t,15)** **regression;** **046** **=** **d=2).**
- **Key finding:** **All** **unweighted** **degree-d** **subset-count** **summaries** **mod** **M** **for** **the** **adjacent-threshold** **gap** **collapse** **to** **one** **divisibility** **condition.**
- **Structured journal:** `research-journal/entries/2026-03-30-elementary-symmetric-adjacent-mod-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/elementary-symmetric-adjacent-mod-collision/script.py`.

---

## Entry 048 — `verifier-oracle-model` / `experiments/adaptive-pairwise-and-tree-depth-wt-five-vs-six/` (2026-03-30)

- **Hypothesis:** **Adaptive** **trees** **branching** **on** **pairwise** **AND** **(x_i∧x_j)** **might** **beat** **coordinate-only** **worst-case** **depth** **n** **for** **wt** **T−1** **vs** **T** **(cf.** **045).**
- **Outcome:** **PASS** **(small-n** **exhaustive** **min-depth).**
- **Key finding:** **(5,3):** **min** **depth** **6** **>** **n;** **(6,4):** **min** **depth** **6** **=** **n** **—** **no** **improvement** **over** **coordinates** **on** **(6,4);** **AND-only** **can** **be** **strictly** **worse** **than** **n** **coordinate** **reads.** **(10,6)** **not** **computed.**
- **Structured journal:** `research-journal/entries/2026-03-30-adaptive-pairwise-and-tree-depth-wt-five-vs-six.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/adaptive-pairwise-and-tree-depth-wt-five-vs-six/script.py`.

---

## Entry 049 — `verifier-oracle-model` / `experiments/adaptive-pairwise-or-xor-tree-depth-wt-shells/` (2026-03-30)

- **Hypothesis:** **Pair** **OR** **/ ** **XOR** **adaptive** **trees** **on** **wt** **{T−1,T}** **vs** **048** **AND.**
- **Outcome:** **PASS.**
- **Key finding:** **OR** **(6,4)** **min** **depth** **9** **>** **AND** **6;** **XOR** **impossible** **when** **n=2T−1** **(complement** **invariance);** **XOR** **(6,4)** **min** **depth** **3** **≪** **n.**
- **Structured journal:** `research-journal/entries/2026-03-30-adaptive-pairwise-or-xor-tree-depth-wt-shells.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`, `research-journal/BREAKTHROUGHS.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/adaptive-pairwise-or-xor-tree-depth-wt-shells/script.py`.

---

## Entry 050 — `anonymous-quorum-binding` / `experiments/weighted-product-mod-m-five-six-collision/` (2026-03-30)

- **Hypothesis:** **∏(i+1)** **over** **S,** **mod** **M** **—** **multiplicative** **analog** **of** **034** **additive** **Σ** **w_i** **mod** **M.**
- **Outcome:** **PASS.**
- **Key finding:** **Smallest** **collision** **M** **=** **2:** **all** **|S|=6** **products** **≡0** **(mod** **2);** **some** **5-sets** **also** **0** **—** **witness** **F=(0..4),** **G=(0..5),** **120** **and** **720** **both** **even.**
- **Structured journal:** `research-journal/entries/2026-03-30-weighted-product-mod-m-five-six-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/weighted-product-mod-m-five-six-collision/script.py`.

---

## Entry 051 — `verifier-oracle-model` / `experiments/xor-pair-shell-complement-swap-regression/` (2026-03-30)

- **Hypothesis:** **n=2T−1** **iff** **complement** **swaps** **shells** **T−1↔T;** **regress** **XOR-pair** **tree** **impossibility** **flag** **vs** **backtracking.**
- **Outcome:** **PASS.**
- **Key finding:** **Lemma** **checked** **on** **grids;** **for** **n≤6** **XOR** **tree** **exists** **iff** **not** **`n=2T−1`;** **(5,3)** **no** **tree** **to** **depth** **100.**
- **Structured journal:** `research-journal/entries/2026-03-30-xor-pair-shell-complement-swap-regression.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/xor-pair-shell-complement-swap-regression/script.py`.

---

## Entry 052 — `anonymous-quorum-binding` / `experiments/weighted-square-sum-mod-m-five-six-collision/` (2026-03-30)

- **Hypothesis:** **Σ(i+1)²** **mod** **M** **as** **threshold** **summary** **(quadratic** **vs** **034** **linear).**
- **Outcome:** **PASS.**
- **Key finding:** **Smallest** **collision** **M=2** **(55** **and** **91** **both** **≡1);** **M=2** **residues** **for** **5-** **and** **6-sets** **both** **{0,1}** **(contrast** **050** **product** **geometry).**
- **Structured journal:** `research-journal/entries/2026-03-30-weighted-square-sum-mod-m-five-six-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/weighted-square-sum-mod-m-five-six-collision/script.py`.

---

## Entry 053 — `verifier-oracle-model` / `experiments/pair-binary-gate-complement-two-bit-invariance/` (2026-03-30)

- **Hypothesis:** Among standard 2-bit gates, only XOR and XNOR satisfy \(f(a,b)=f(1-a,1-b)\) for all inputs; NAND/NOR fail; this explains global-complement invariance of XOR/XNOR pair trees (049/051).
- **Outcome:** **PASS** (exhaustive 4-cell check + assertions).
- **Key finding:** **AND/OR/NAND/NOR** break two-bit complement symmetry; **XOR/XNOR** preserve it — finite taxonomy for the **\(Z_2\)** **pair-oracle** obstruction.
- **Structured journal:** `research-journal/entries/2026-03-30-pair-binary-gate-complement-two-bit-invariance.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/pair-binary-gate-complement-two-bit-invariance/script.py`.

---

## Entry 054 — `anonymous-quorum-binding` / `experiments/joint-weighted-sum-square-mod-m1-m2-five-six-collision/` (2026-03-30)

- **Hypothesis:** Joint tag \((\sum (i+1) \bmod M_1,\ \sum (i+1)^2 \bmod M_2)\) for \(|S|\in\{5,6\}\), \(n=10\); lex-first \((M_1,M_2)\) collision.
- **Outcome:** **PASS.**
- **Key finding:** **(2, 2)** first; key **(1,1)**; witness 5-set (4,6,7,8,9) vs 6-set (0..5) — mod 2, \(w^2\equiv w\), so both coordinates duplicate parity.
- **Structured journal:** `research-journal/entries/2026-03-30-joint-weighted-sum-square-mod-m1-m2-five-six-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/joint-weighted-sum-square-mod-m1-m2-five-six-collision/script.py`.

---

## Entry 055 — `anonymous-quorum-binding` / `experiments/joint-sum-sumsq-mod-m1-m2-min3-five-six-collision/` (2026-03-30)

- **Hypothesis:** Same joint tag as 054 but only **M₁, M₂ ≥ 3**; lex-first collision in bounded scan.
- **Outcome:** **PASS.**
- **Key finding:** First hit **(3, 3)**, key **(0, 1)** — same witnesses as 054; **Σw** and **Σw²** both align mod 3 (not parity redundancy).
- **Structured journal:** `research-journal/entries/2026-03-30-joint-sum-sumsq-mod-m1-m2-min3-five-six-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/joint-sum-sumsq-mod-m1-m2-min3-five-six-collision/script.py`.

---

## Entry 056 — `anonymous-quorum-binding` / `experiments/joint-sum-sumsq-mod-m1-m2-coprime-five-six-collision/` (2026-03-30)

- **Hypothesis:** Joint **(Σw mod M₁, Σw² mod M₂)** with **gcd(M₁,M₂)=1** only; lex-first 5-vs-6 collision.
- **Outcome:** **PASS.**
- **Key finding:** **(2, 3)**, key **(1, 1)** — same witnesses as 054/055 (parity + mod 3 on **Σw²**).
- **Structured journal:** `research-journal/entries/2026-03-30-joint-sum-sumsq-mod-m1-m2-coprime-five-six-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/joint-sum-sumsq-mod-m1-m2-coprime-five-six-collision/script.py`.

---

## Entry 057 — `anonymous-quorum-binding` / `experiments/joint-sum-sumsq-mod-m1-m2-min4-coprime-five-six-collision/` (2026-03-30)

- **Hypothesis:** Same joint tag, **M₁,M₂ ≥ 4**, **gcd(M₁,M₂)=1**; lex-first collision.
- **Outcome:** **PASS.**
- **Key finding:** **(4, 5)**, key **(1, 1)** — 5-set **(4,5,6,8,9)** vs 6-set **(0..5)** (new 5-witness vs 054–056).
- **Structured journal:** `research-journal/entries/2026-03-30-joint-sum-sumsq-mod-m1-m2-min4-coprime-five-six-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/joint-sum-sumsq-mod-m1-m2-min4-coprime-five-six-collision/script.py`.

---

## Entry 058 — `anonymous-quorum-binding` / `experiments/joint-sum-sumsq-mod-m1-m2-min5-coprime-five-six-collision/` (2026-03-30)

- **Hypothesis:** Same joint tag, **M₁,M₂ ≥ 5**, **gcd(M₁,M₂)=1**; lex-first collision.
- **Outcome:** **PASS.**
- **Key finding:** **(5, 6)**, key **(1, 1)** — 5-set **(1,4,6,7,8)** vs 6-set **(0..5)**; pattern **(m,m+1)** with **057**’s **(4,5)**.
- **Structured journal:** `research-journal/entries/2026-03-30-joint-sum-sumsq-mod-m1-m2-min5-coprime-five-six-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/joint-sum-sumsq-mod-m1-m2-min5-coprime-five-six-collision/script.py`.

---

## Entry 059 — `anonymous-quorum-binding` / `experiments/triple-power-sum-mod-m1-m2-m3-pairwise-coprime-five-six-collision/` (2026-03-30)

- **Hypothesis:** **(Σw, Σw², Σw³)** mod **(M₁,M₂,M₃)** with **pairwise coprime** moduli; lex-first **5 vs 6** collision.
- **Outcome:** **PASS.**
- **Key finding:** **(2, 3, 5)**, key **(1, 1, 1)** — 5-set **(3,4,6,8,9)** vs 6-set **(0..5)**.
- **Structured journal:** `research-journal/entries/2026-03-30-triple-power-sum-mod-m1-m2-m3-pairwise-coprime-five-six-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/triple-power-sum-mod-m1-m2-m3-pairwise-coprime-five-six-collision/script.py`.

---

## Entry 060 — `anonymous-quorum-binding` / `experiments/triple-power-sum-mod-m1-m2-m3-pairwise-coprime-min4-five-six-collision/` (2026-03-30)

- **Hypothesis:** Same triple tag, **Mᵢ ≥ 4**, **pairwise coprime**; lex-first collision.
- **Outcome:** **PASS.**
- **Key finding:** **(4, 5, 7)**, key **(1, 1, 0)** — 5-set **(2,3,5,6,8)** vs 6-set **(0..5)**.
- **Structured journal:** `research-journal/entries/2026-03-30-triple-power-sum-mod-m1-m2-m3-pairwise-coprime-min4-five-six-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/triple-power-sum-mod-m1-m2-m3-pairwise-coprime-min4-five-six-collision/script.py`.

---

## Entry 061 — `anonymous-quorum-binding` / `experiments/xor-public-weight-five-six-collision/` (2026-03-30)

- **Hypothesis:** **H(S) = XOR of (i+1)** over **i ∈ S**; collision between some **5-set** and **6-set** (**n=10**).
- **Outcome:** **PASS.**
- **Key finding:** **H = 7** — 5-set **(4,5,6,8,9)** vs 6-set **(0..5)** (same shell pair as **057**).
- **Structured journal:** `research-journal/entries/2026-03-30-xor-public-weight-five-six-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/xor-public-weight-five-six-collision/script.py`.

---

## Entry 062 — `anonymous-quorum-binding` / `experiments/joint-sum-mod-xor-five-six-separator-scan/` (2026-03-30)

- **Hypothesis:** **T_M(S) = (Σ(i+1) mod M, XOR of (i+1))** might separate **|S|=5** vs **6** for some **M** (**n=10**).
- **Outcome:** **PASS** (structural refutation).
- **Key finding:** **57** exact **(integer sum, XOR)** keys lie in both shells ⇒ **no** **M** separates; witness **(31, 5):** 5-set **(1,2,6,8,9)** vs 6-set **(0,1,2,5,8,9)**.
- **Structured journal:** `research-journal/entries/2026-03-30-joint-sum-mod-xor-five-six-separator-scan.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/joint-sum-mod-xor-five-six-separator-scan/script.py`.

---

## Entry 063 — `anonymous-quorum-binding` / `experiments/integer-sum-product-joint-five-six-collision/` (2026-03-30)

- **Hypothesis:** Some **5-set** and **6-set** share exact integer **(Σ(i+1), Π(i+1))** (**n=10**).
- **Outcome:** **PASS.**
- **Key finding:** **37** collisions; sample **sum=27, prod=1680** — 5-set **(1,5,6,7,8)** vs 6-set **(1,2,3,4,7,10)** ⇒ **(Σ mod M, Π mod M)** fails for all **M** on those pairs (same pattern as **062**).
- **Structured journal:** `research-journal/entries/2026-03-30-integer-sum-product-joint-five-six-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/integer-sum-product-joint-five-six-collision/script.py`.

---

## Entry 064 — `anonymous-quorum-binding` / `experiments/integer-triple-power-sum-five-six-shell/` (2026-03-30)

- **Hypothesis:** Some **5-set** and **6-set** share exact integer **(Σw, Σw², Σw³)** with **w_i=i+1** (**n=10**).
- **Outcome:** **FAIL** (no such collision).
- **Key finding:** **462** **/ ** **462** distinct keys on **C(10,5) ∪ C(10,6)** — injective triple moment map; contrasts **059–060** where **modular** triples collide immediately.
- **Structured journal:** `research-journal/entries/2026-03-30-integer-triple-power-sum-five-six-shell.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/integer-triple-power-sum-five-six-shell/script.py`.

---

## Entry 065 — `anonymous-quorum-binding` / `experiments/triple-power-sum-single-modulus-five-six-first-collision/` (2026-03-30)

- **Hypothesis:** Smallest **M ≥ 2** such that **(p₁,p₂,p₃) mod M** (single **M**) collides across **|S|=5** vs **6** (**w_i=i+1**, **n=10**).
- **Outcome:** **PASS.**
- **Key finding:** **M = 2**, modular key **(1,1,1)** — 5-set **(5,7,8,9,10)** vs 6-set **(1,2,3,4,5,6)**; **064**’s exact injectivity is destroyed by **1 bit** per coordinate.
- **Structured journal:** `research-journal/entries/2026-03-30-triple-power-sum-single-modulus-five-six-first-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/triple-power-sum-single-modulus-five-six-first-collision/script.py`.

---

## Entry 066 — `verifier-oracle-model` / `experiments/adaptive-coordinate-or-pair-xor-tree-depth-wt-five-vs-six/` (2026-03-30)

- **Hypothesis:** Adaptive trees separating **wt ∈ {5,6}** on **n=10** can beat coordinate-only depth **n** if internal nodes may be **x_i** or **x_i ⊕ x_j**.
- **Outcome:** **PASS** (hypothesis **D_mix ≤ 9**; observed **D_mix = 5**).
- **Key finding:** Minimum perfect-tree depth **= 5** with mixed gates vs **10** for coordinate-only (**045**); depths **1–4** impossible.
- **Structured journal:** `research-journal/entries/2026-03-30-adaptive-coordinate-or-pair-xor-tree-depth-wt-five-vs-six.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-pair-xor-tree-depth-wt-five-vs-six/script.py`.

---

## Entry 067 — `verifier-oracle-model` / `experiments/mixed-coordinate-xor-tree-witness-wt-five-vs-six/` (2026-03-30)

- **Hypothesis:** Emit one explicit nested JSON witness tree for the **066** mixed-gate model at depth **5**, using the same split priority as the existential DP.
- **Outcome:** **PASS.**
- **Key finding:** **Two-phase** **`exists_tree` + feasibility-gated `witness`** prints a depth-**5** tree in ~**24 s**; naive memoized witness DFS **times out**. First-success witness uses **only pair-XOR** internal nodes (root **x₀ ⊕ x₁**, nested disjoint-pair XORs); leaf multiset sums to **462**.
- **Structured journal:** `research-journal/entries/2026-03-30-mixed-coordinate-xor-tree-witness-wt-five-vs-six.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/mixed-coordinate-xor-tree-witness-wt-five-vs-six/script.py`.

---

## Entry 068 — `verifier-oracle-model` / `experiments/adaptive-coordinate-or-pair-or-tree-depth-wt-five-vs-six/` (2026-03-30)

- **Hypothesis:** On **n=10**, **wt ∈ {5,6}**, measure minimum depth of perfect separator trees whose internal nodes are **x_i** or **(x_i ∨ x_j)** (mixed like **066** but with pair-OR).
- **Outcome:** **INCONCLUSIVE** on exact **min_d**; **partial:** **no** tree for **d ≤ 6** (exhaustive memoized DP on **462-bit** subsets); **min_d ≤ 10** by theory (coordinates only).
- **Key finding:** **d = 6** alone takes **~90–105 s**; **d ≥ 7** did not complete in long wall-clock trials — **pair-OR** mixes explode the DP relative to **066** (XOR mix, **d = 5**, ~**30 s**). Initial script had a **`depth_remaining`** recursion bug (fixed).
- **Structured journal:** `research-journal/entries/2026-03-30-adaptive-coordinate-or-pair-or-tree-depth-wt-five-vs-six.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-pair-or-tree-depth-wt-five-vs-six/script.py` (`--budget-seconds`, `--d-min`).

---

## Entry 069 — `verifier-oracle-model` / `experiments/mixed-coordinate-xor-tree-witness-xor-first-wt-five-vs-six/` (2026-03-30)

- **Hypothesis:** Same **066** feasibility, but build a depth-**5** witness by trying **pair-XOR** splits **before** coordinates at each node (alternate tie-break vs **067**).
- **Outcome:** **PASS.**
- **Key finding:** Exported JSON tree is **byte-identical** to **067** on this instance; **internal** **counts** **coord=0, xor=31**. **067** **`exists_tree`** erratum: pass **`depth_remaining`** into **`recurse_children`**, not **`depth_remaining - 1`** (matches **066**).
- **Structured journal:** `research-journal/entries/2026-03-30-mixed-coordinate-xor-tree-witness-xor-first-wt-five-vs-six.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/mixed-coordinate-xor-tree-witness-xor-first-wt-five-vs-six/script.py`.

---

## Entry 070 — `verifier-oracle-model` / `experiments/mixed-coordinate-xor-tree-second-xor-root-witness-wt-five-vs-six/` (2026-03-30)

- **Hypothesis:** On the full **wt ∈ {5,6}** domain (**n=10**), **≥2** lex-feasible **pair-XOR** roots admit depth-**≤5** completions; the **second** such root plus **067**’s coord-first **`witness(S, d−1)`** on children yields JSON **≠** **067**.
- **Outcome:** **PASS.**
- **Key finding:** **45** feasible root XOR pairs; second lex **(0,2)**; **`sha256(JSON)`** differs from **067** default witness. **069**’s collapse was **search-order**-driven, not uniqueness of **`π_tree`**.
- **Structured journal:** `research-journal/entries/2026-03-30-mixed-coordinate-xor-tree-second-xor-root-witness-wt-five-vs-six.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/mixed-coordinate-xor-tree-second-xor-root-witness-wt-five-vs-six/script.py`.

---

## Entry 071 — `verifier-oracle-model` / `experiments/min-sha256-xor-root-complete-witness-wt-five-vs-six/` (2026-03-30)

- **Hypothesis:** Among **45** XOR-root + **067**-subtree witnesses at depth **5**, exactly **one** root pair **(i,j)** minimizes **`sha256`** of canonical JSON.
- **Outcome:** **PASS.**
- **Key finding:** Unique minimizer **(6,7)**; **`min_sha256` ≠ `sha256_067_default`** — min-hash canonical tie-break disagrees with **067** first-success construction.
- **Structured journal:** `research-journal/entries/2026-03-30-min-sha256-xor-root-complete-witness-wt-five-vs-six.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/min-sha256-xor-root-complete-witness-wt-five-vs-six/script.py`.

---

## Entry 072 — `verifier-oracle-model` / `experiments/min-sha256-coord-root-complete-witness-wt-five-vs-six/` (2026-03-30)

- **Hypothesis:** At least one coordinate **`x_i`** at the root of the full **462**-set admits **`exists_tree`** on both children with remaining depth **4** (overall depth **≤5**), enabling a parallel to **071**’s min-hash scan.
- **Outcome:** **FAIL** on that existence claim (**C1**).
- **Key finding:** **`feasible_coord_root_count = 0`** for all **i**; coordinate-root + **067** subtree family is **empty** at **d = 5** here, while **45** XOR roots work (**071**).
- **Structured journal:** `research-journal/entries/2026-03-30-min-sha256-coord-root-complete-witness-wt-five-vs-six.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/min-sha256-coord-root-complete-witness-wt-five-vs-six/script.py`.

---

## Entry 073 — `verifier-oracle-model` / `experiments/distinct-sha256-xor-root-complete-witness-wt-five-vs-six/` (2026-03-30)

- **Hypothesis:** The **45** feasible XOR-root + **067**-subtree witnesses have pairwise distinct **`sha256`** of canonical JSON (injective on the family).
- **Outcome:** **PASS.**
- **Key finding:** **`distinct_canonical_json_bytes_count = distinct_sha256_count = 45`** — no two roots yield the same JSON bytes; fingerprints fully separate choices in this slice.
- **Structured journal:** `research-journal/entries/2026-03-30-distinct-sha256-xor-root-complete-witness-wt-five-vs-six.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/distinct-sha256-xor-root-complete-witness-wt-five-vs-six/script.py`.

---

## Entry 074 — `verifier-oracle-model` / `experiments/exists-tree-depth-four-infeasible-wt-five-vs-six/` (2026-03-30)

- **Hypothesis:** For the full **wt ∈ {5,6}** subset of **`{0,1}^{10}`**, **`exists_tree(full, 4) = False`** and **`exists_tree(full, 5) = True`** using the same **`exists_tree`** as **067** (mixed coordinate + pair-XOR).
- **Outcome:** **PASS.**
- **Key finding:** Direct DP certificate that **depth 4** is **globally infeasible** on the **462**-set while **depth 5** works — aligns **066**’s minimum depth **5** with the **`exists_tree`** predicate on **`full`**.
- **Structured journal:** `research-journal/entries/2026-03-30-exists-tree-depth-four-infeasible-wt-five-vs-six.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/exists-tree-depth-four-infeasible-wt-five-vs-six/script.py`.

---

## Entry 075 — `anonymous-quorum-binding` / `experiments/uniform-quadruple-power-sum-mod-m-five-six-first-collision/` (2026-03-30)

- **Hypothesis:** Smallest **M≥2** with a **5-vs-6** collision on **(Σw^k mod M)_{k=1..4}** for **w_i=i+1**, **n=10** might exceed **2** if the fourth moment breaks parity-only merges.
- **Outcome:** **PASS** (hypothesis about **M\*>2** refuted). **FIRST_COLLISION_M = 2**, **mod_key (1,1,1,1)**; witness **5-set (5,7,8,9,10)** vs **6-set (1..6)**.
- **Key finding:** **Four** uniform modular power sums still collapse across shells at **M=2** — same scale as **065** / **034**; extra moment did not postpone the first collision in this toy.
- **Structured journal:** `research-journal/entries/2026-03-30-uniform-quadruple-power-sum-mod-m-five-six-first-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/uniform-quadruple-power-sum-mod-m-five-six-first-collision/script.py`.

---

## Entry 076 — `anonymous-quorum-binding` / `experiments/uniform-quintuple-power-sum-mod-m-five-six-first-collision/` (2026-03-30)

- **Hypothesis:** Smallest **M** with **5-vs-6** collision on **(Σw^k mod M)_{k=1..5}** might exceed **2** if the fifth moment breaks parity; structural alternative: **w^k ≡ w (mod 2)** for **k≥1** makes all five coordinates redundant mod **2**.
- **Outcome:** **PASS** (structural prediction confirmed). **FIRST_COLLISION_M = 2**, **mod_key (1,1,1,1,1)**; same witness as **075**.
- **Key finding:** At **M=2**, **no** number of raw power sums adds independent information beyond **Σw mod 2** (odd-weight-count parity). Stacking moments does not postpone the first uniform-modulus collision in this toy.
- **Structured journal:** `research-journal/entries/2026-03-30-uniform-quintuple-power-sum-mod-m-five-six-first-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/uniform-quintuple-power-sum-mod-m-five-six-first-collision/script.py`.

---

## Entry 077 — `anonymous-quorum-binding` / `experiments/uniform-quintuple-power-sum-odd-m-five-six-first-collision/` (2026-03-30)

- **Hypothesis:** Smallest **odd** **M≥3** with **5-vs-6** collision on **(Σw^k mod M)_{k=1..5}** might be **large** once **M=2** is excluded; alternative: still **small** (**3** or **5**).
- **Outcome:** **PASS**. **FIRST_ODD_COLLISION_M = 3**, **mod_key (0,1,0,1,0)**; **same** witness **5-set (5,7,8,9,10)** vs **6-set (1..6)** as **075–076**.
- **Key finding:** Restricting to **odd** moduli does **not** create headroom — **M=3** is the first hit; the recurring witness merges shells on **all five** moments mod **3** as well.
- **Structured journal:** `research-journal/entries/2026-03-30-uniform-quintuple-power-sum-odd-m-five-six-first-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/uniform-quintuple-power-sum-odd-m-five-six-first-collision/script.py`.

---

## Entry 078 — `anonymous-quorum-binding` / `experiments/integer-quintuple-power-sum-five-six-shell/` (2026-03-30)

- **Hypothesis H1:** Some **5-set** and **6-set** share exact **(Σw^k)_{k=1..5}** for **w_i=i+1**, **n=10**.
- **Outcome:** **FAIL** for **H1** — **462** distinct keys on **462** subsets; **K** injective on **C(10,5) ∪ C(10,6)** (within-shell injective too).
- **Key finding:** Same pattern as **064**: **exact** moments separate shells; **075–077** show **modular** uniform tags do not. **p₄, p₅** add no new separation information versus **064** on this finite universe.
- **Structured journal:** `research-journal/entries/2026-03-30-integer-quintuple-power-sum-five-six-shell.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/integer-quintuple-power-sum-five-six-shell/script.py`.

---

## Entry 079 — `anonymous-quorum-binding` / `experiments/quintuple-power-sum-mod-m1-m5-pairwise-coprime-five-six-collision/` (2026-03-30)

- **Hypothesis:** Lex-first **pairwise-coprime** **(M₁,…,M₅)** (**min_m=2**, **scan_max=18**) yields a **5-vs-6** collision on **(p_k mod M_k)_{k=1..5}** — **059** extended to five moments.
- **Outcome:** **PASS**. **First** **(2,3,5,7,13)**, **key (1,1,4,4,5)**; **5-set** **(1,2,3,7,10)** vs **6-set** **(1,2,3,5,6,8)**.
- **Key finding:** **Coprime** **per-coordinate** **moduli** still collapse at **small** **primes** **(≤13)**. **(2,3,5,7,11)** **is** **lex** **earlier** **and** **coprime** **but** **does** **not** **collide** **—** **M₅** **matters** **for** **lex-first** **merge** **unlike** **uniform** **M=2** **redundancy** **in** **076**.
- **Structured journal:** `research-journal/entries/2026-03-30-quintuple-power-sum-mod-m1-m5-pairwise-coprime-five-six-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/quintuple-power-sum-mod-m1-m5-pairwise-coprime-five-six-collision/script.py`.

---

## Entry 080 — `anonymous-quorum-binding` / `experiments/quintuple-power-sum-mod-m1-m5-pairwise-coprime-min4-five-six-collision/` (2026-03-30)

- **Hypothesis:** Lex-first **coprime** **(M₁,…,M₅)** with **M_i≥4** (**060**-style floor on **079**) still yields a **small-modulus** **5-vs-6** collision.
- **Outcome:** **PASS**. **First** **(4,5,7,9,17)**, **key (0,4,1,8,10)**; **5-set** **(2,3,6,8,9)** vs **6-set** **(1,3,4,5,7,8)** — **both** **p₁ = 28**.
- **Key finding:** **Raising** **min** **modulus** **to** **4** **does** **not** **buy** **a** **large** **safe** **tuple** **(max** **17** **).** **Shared** **integer** **sum** **across** **shells** **(** **035** **)** **aligns** **p₁ mod M₁** **while** **other** **moments** **can** **still** **match** **mod** **M₂…M₅**.
- **Structured journal:** `research-journal/entries/2026-03-30-quintuple-power-sum-mod-m1-m5-pairwise-coprime-min4-five-six-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/quintuple-power-sum-mod-m1-m5-pairwise-coprime-min4-five-six-collision/script.py`.

---

## Entry 081 — `verifier-oracle-model` / `experiments/mod-m-count-summary-threshold-aliasing-scan/` (2026-03-30)

- **Hypothesis:** For **n = 10**, **t = 6**, **h(k) = k mod m** threshold-aliases iff **m ≤ n**; smallest **m** with no **(k₁ < t ≤ k₂)** and **k₁ ≡ k₂ (mod m)** is **n + 1 = 11**.
- **Outcome:** **PASS.** Crossing gaps **k₂ − k₁** are **{1,…,10}**; **m ∈ {2,…,10}** has explicit witness (lex-first often **(0, m)** for **m ≥ 6**); **m ≥ 11** has **none**; loop **m < 200** matches **alias ⇔ m ≤ n**.
- **Key finding:** Systematizes **parity-count-summary** / **023**: **any** **mod m** summary with **m ≤ n** collapses **under-** vs **at/above-threshold** counts in this **full-range** participation model — **Ω(log n)** bits needed for injective **h** on **k ∈ [0,n]**.
- **Structured journal:** `research-journal/entries/2026-03-30-mod-m-count-summary-threshold-aliasing-scan.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/mod-m-count-summary-threshold-aliasing-scan/script.py`.

---

## Entry 082 — `verifier-oracle-model` / `experiments/adaptive-coordinate-or-pair-or-tree-depth-wt-five-vs-six/` (2026-03-30)

- **Hypothesis:** Mixed adaptive trees (**coordinate** or **pair OR**) on **n=10**, **wt ∈ {5,6}** have minimum depth **d**; prior **95s** budget run was **INCONCLUSIVE** past **d=6**.
- **Outcome:** **PASS.** **Partition-mask** **optimization** **in** **`script.py`;** **DP** **certifies** **d=1..9** **infeasible** **(** **d=9** **≈864** **s** **).** **045** **+** **language** **monotonicity** **(** **coord** **⊂** **mixed** **)** **⇒** **∃** **tree** **at** **d=10** **⇒** **min_d=10** **—** **pair** **OR** **does** **not** **improve** **045** **(** **066** **XOR** **still** **at** **5** **).**
- **Key finding:** **OR** **vs** **XOR** **on** **this** **toy:** **OR** **is** **adaptive-noise** **(** **huge** **DP** **)** **and** **no** **depth** **gain** **over** **coordinates;** **XOR** **shrinks** **depth** **dramatically**.
- **Structured journal:** `research-journal/entries/2026-03-30-pair-or-coord-mixed-min-depth-ten-certified.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-pair-or-tree-depth-wt-five-vs-six/script.py`.

---

## Entry 083 — `verifier-oracle-model` / `experiments/mod-m-threshold-alias-gap-set-scan/` (2026-03-30)

- **Hypothesis:** Crossing-gap set **D(n,t)** for modular count summaries generalizes **081**; relate **D** to **mod-m** **threshold** **aliasing.**
- **Outcome:** **PASS.** **Proof** **D(n,t)={1,…,n}** **for** **all** **1≤t≤n** **(** **two-case** **construction** **);** **hence** **k mod m** **aliases** **across** **k≥t** **vs** **k<t** **iff** **2≤m≤n,** **first** **clean** **m=n+1.** **Computed** **n=2..30** **at** **majority** **t** **and** **all** **t** **for** **n≤20.**
- **Key finding:** **Constant-modulus** **participation** **bucket** **cannot** **alone** **encode** **threshold** **when** **m≤n** **—** **not** **an** **artifact** **of** **(10,6).**
- **Structured journal:** `research-journal/entries/2026-03-30-mod-m-threshold-alias-gap-set-scan.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/mod-m-threshold-alias-gap-set-scan/script.py`.

---

## Entry 084 — `verifier-oracle-model` / `experiments/adaptive-coordinate-or-pair-xnor-tree-depth-wt-five-vs-six/` (2026-03-30)

- **Hypothesis:** Mixed **coord** **+** **pair-XNOR** **trees** **on** **(10,{5,6})** **have** **the** **same** **minimum** **depth** **as** **066** **(XOR).**
- **Outcome:** **PASS.** **Each** **XNOR(i,j)** **partition** **equals** **XOR(i,j)** **with** **0/1** **children** **swapped;** **symmetric** **recursion** **⇒** **same** **`exists_tree`** **answers;** **min_d** **=** **5** **(** **d<5** **fail** **).**
- **Key finding:** **Linear** **pair** **parity** **gates** **XOR/XNOR** **are** **redundant** **as** **split** **primitives** **here;** **OR** **(** **082** **)** **is** **the** **distinct** **nonlinear** **family** **tested** **so** **far** **(** **worse** **depth** **).**
- **Structured journal:** `research-journal/entries/2026-03-30-pair-xnor-mixed-tree-depth-five-vs-six.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-pair-xnor-tree-depth-wt-five-vs-six/script.py`.

---

## Entry 085 — `verifier-oracle-model` / `experiments/adaptive-coordinate-or-pair-nand-tree-depth-wt-five-vs-six/` (2026-03-31)

- **Hypothesis:** Mixed **coord** **+** **pair-NAND** **on** **(10,{5,6})** **might** **match** **XOR** **(** **5** **),** **OR** **(** **10** **),** **or** **sit** **between.**
- **Outcome:** **PASS.** **DP** **certifies** **d=1..9** **infeasible** **(** **d=9** **≈1145** **s** **);** **d=10** **feasible** **(** **≈228** **s** **)** **⇒** **min_d=10** **—** **same** **as** **045** **/** **082** **,** **not** **066** **/** **084.**
- **Key finding:** **NAND** **(** **053** **:** **not** **complement-invariant** **on** **the** **2-bit** **cell** **)** **still** **gives** **no** **depth** **gain** **over** **coordinates** **here;** **only** **XOR/XNOR** **shrink** **depth** **to** **5** **on** **this** **toy.**
- **Structured journal:** `research-journal/entries/2026-03-31-pair-nand-mixed-tree-depth-ten-certified.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-pair-nand-tree-depth-wt-five-vs-six/script.py`.

---

## Entry 086 — `verifier-oracle-model` / `experiments/adaptive-coordinate-or-pair-nor-or-partition-equivalence/` (2026-03-31)

- **Hypothesis:** **Mixed** **coord** **+** **pair-NOR** **matches** **mixed** **OR** **on** **`exists_tree`** **(** **same** **`min_d`** **).**
- **Outcome:** **PASS.** **Proof:** **NOR=0** **iff** **OR=1** **on** **each** **pair** **⇒** **same** **unordered** **bipartition** **as** **OR** **with** **0/1** **children** **swapped;** **symmetric** **recursion** **⇒** **identical** **DP.** **Hence** **`min_d=10`** **by** **082** **without** **re-running** **d=9** **DP.** **Script** **verifies** **mask** **swap** **and** **d≤5** **OR/NOR** **agreement.**
- **Key finding:** **OR/NOR** **are** **one** **equivalence** **class** **for** **this** **adaptive** **separator** **problem** **(** **like** **XOR/XNOR** **in** **084** **).**
- **Structured journal:** `research-journal/entries/2026-03-31-pair-nor-or-partition-equivalence-min-depth-ten.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-pair-nor-or-partition-equivalence/script.py`.

---

## Entry 087 — `anonymous-quorum-binding` / `experiments/bitwise-and-or-weight-five-six-shell-collision/` (2026-03-31)

- **Hypothesis:** **Bitwise** **AND/OR** **of** **w_i=i+1** **over** **S** **admits** **|S|=5** **vs** **6** **collisions** **(** **n=10** **).**
- **Outcome:** **PASS.** **h_and:** **all** **210** **six-sets** **map** **to** **one** **value** **(** **0** **);** **cross-shell** **collision** **with** **five-sets** **(** **e.g.** **weights** **1..5** **).** **h_or:** **three** **shared** **values** **across** **shells** **(** **sample** **OR=7** **for** **{1..5}** **vs** **{1..6}** **).**
- **Key finding:** **Idempotent** **bit** **summaries** **are** **too** **coarse** **for** **shell** **separation** **—** **same** **“toy** **`Link`** **fails”** **theme** **as** **034/050/061,** **different** **operation.**
- **Structured journal:** `research-journal/entries/2026-03-31-bitwise-and-or-weight-five-six-shell-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/bitwise-and-or-weight-five-six-shell-collision/script.py`.

---

## Entry 088 — `anonymous-quorum-binding` / `experiments/joint-bitwise-and-or-integer-sum-five-six-collision/` (2026-03-31)

- **Hypothesis:** **Joint** **(h_and,** **Σw)** **and** **(h_or,** **Σw)** **(** **exact** **)** **still** **collide** **across** **|S|=5** **vs** **6.**
- **Outcome:** **PASS.** **20** **shared** **K_and** **keys,** **23** **shared** **K_or** **keys** **(** **e.g.** **(0,21),** **(7,21)** **with** **6-set** **1..6** **).** **Same** **integer** **sum** **⇒** **same** **mod** **M** **for** **all** **M** **—** **extends** **087** **/** **parallels** **062.**
- **Key finding:** **Bit-op** **+** **linear** **sum** **does** **not** **restore** **shell** **separation** **on** **this** **public-weight** **toy.**
- **Structured journal:** `research-journal/entries/2026-03-31-joint-bitwise-and-or-integer-sum-five-six-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/joint-bitwise-and-or-integer-sum-five-six-collision/script.py`.

---

## Entry 089 — `anonymous-quorum-binding` / `experiments/gcd-public-weight-five-six-shell-collision/` (2026-03-31)

- **Hypothesis:** **Subset** **gcd** **of** **w_i=i+1** **and** **joint** **(gcd,** **Σw)** **collide** **across** **|S|=5** **vs** **6.**
- **Outcome:** **PASS.** **h_gcd** **takes** **only** **one** **value** **on** **all** **210** **six-sets** **(** **1** **);** **two** **values** **on** **five-sets** **⇒** **cross-shell** **collision.** **Joint** **J** **has** **20** **shared** **keys** **across** **shells** **(** **088** **parallel** **).**
- **Key finding:** **Divisibility** **gcd** **is** **another** **coarse** **symmetric** **summary** **on** **{1,…,10}** **—** **not** **a** **standalone** **`Link`** **axis** **here.**
- **Structured journal:** `research-journal/entries/2026-03-31-gcd-public-weight-five-six-shell-collision.md`, `research-journal/index.md`, digest `research-journal/digests/anonymous-quorum-binding.md`.
- **Artifact:** `sub-problems/anonymous-quorum-binding/experiments/gcd-public-weight-five-six-shell-collision/script.py`.

---

## Entry 090 — `verifier-oracle-model` / `experiments/adaptive-coordinate-or-triple-xor-tree-depth-wt-five-vs-six/` (2026-03-31)

- **Hypothesis:** Mixed **coord** **+** **triple-XOR** **x_i⊕x_j⊕x_k** **on** **(10,{5,6})** **has** **minimum** **depth** **≤** **5** **(** **066** **subset** **)** **and** **either** **<** **5** **or** **=** **5.**
- **Outcome:** **PASS.** **Bitset** **DP** **(** **120** **triple** **partitions** **+** **10** **coords** **):** **d=1..3** **False,** **d=4** **True** **(** **total** **~8.6** **s** **)** **⇒** **`min_d=4`.** **Strict** **improvement** **over** **066**/**084** **(** **5** **).** **074** **’s** **`exists_tree(full,4)=False`** **is** **for** **pair-XOR-only** **internal** **nodes.**
- **Key finding:** **Weight-3** **F₂** **parity** **splits** **as** **first-class** **tree** **nodes** **shave** **one** **depth** **level** **on** **this** **toy** **—** **not** **deducible** **from** **the** **2-bit** **XOR** **gate** **taxonomy** **alone** **(** **053** **).**
- **Structured journal:** `research-journal/entries/2026-03-31-adaptive-coordinate-or-triple-xor-tree-depth-wt-five-vs-six.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`, `research-journal/BREAKTHROUGHS.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-triple-xor-tree-depth-wt-five-vs-six/script.py`.

---

## Entry 091 — `verifier-oracle-model` / `experiments/adaptive-coordinate-or-quadruple-xor-tree-depth-wt-five-vs-six/` (2026-03-30)

- **Hypothesis:** **Coord + quad-XOR** **on** **(10,{5,6})** **has** **`min_d ∈ {3,4}`** **(** **090** **⊂** **this** **language** **)** **.**
- **Outcome:** **PASS.** **`min_d=3`** **(** **d=1,2** **false** **;** **d=3** **true** **~0.39** **s** **).** **Strict** **improvement** **over** **090** **(** **4** **).**
- **Key finding:** **Arity** **ladder** **066→090→091:** **pair/triple/quad** **primitive** **XOR** **splits** **give** **`min_d`** **5→4→3** **on** **this** **toy.**
- **Structured journal:** `research-journal/entries/2026-03-30-adaptive-coordinate-or-quadruple-xor-tree-depth-wt-five-vs-six.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`, `research-journal/BREAKTHROUGHS.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-quadruple-xor-tree-depth-wt-five-vs-six/script.py`.

---

## Entry 092 — `verifier-oracle-model` / `experiments/adaptive-coordinate-or-total-parity-xor-tree-depth-wt-five-vs-six/` (2026-03-30)

- **Hypothesis:** **Coord + total XOR** **⊕_{i=0}^9 x_i** **(** **global** **parity** **)** **yields** **`min_d=1`** **on** **(10,{5,6}).**
- **Outcome:** **PASS.** **`d=1` feasible** **;** **partition** **210** **wt6** **/** **252** **wt5** **.** **Full** **parity** **is** **not** **a** **single** **091** **quad** **gate.**
- **Key finding:** **Bounded-arity** **(** **≤4** **)** **F₂** **pools** **(** **091** **`min_d=3`**) vs **one** **n-wide** **XOR** **(** **`min_d=1`**) **—** **oracle** **class** **must** **be** **specified** **explicitly.**
- **Structured journal:** `research-journal/entries/2026-03-30-adaptive-coordinate-or-total-parity-xor-tree-depth-wt-five-vs-six.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`, `research-journal/BREAKTHROUGHS.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-total-parity-xor-tree-depth-wt-five-vs-six/script.py`.

---

## Entry 093 — `verifier-oracle-model` / `experiments/adaptive-coordinate-or-pentuple-xor-tree-depth-wt-five-vs-six/` (2026-03-30)

- **Hypothesis:** **Coord + 252** **pentuple** **XORs** **only** **(** **no** **total** **parity** **)** **yields** **`min_d∈{2,3}`** **;** **answers** **091** **open** **Q** **vs** **quad-only** **`min_d=3`.**
- **Outcome:** **PASS.** **`min_d=2`** **(** **d=1** **false** **,** **d=2** **true** **~0.005** **s** **).** **Strict** **improvement** **over** **091** **despite** **incomparable** **primitive** **lists.**
- **Key finding:** **Depth** **ladder** **on** **this** **toy** **(** **+** **coords** **):** **pair** **5** **→** **triple** **4** **→** **quad** **3** **→** **pentuple** **2** **→** **total** **parity** **1** **(** **066/090/091/093/092** **).**
- **Structured journal:** `research-journal/entries/2026-03-30-adaptive-coordinate-or-pentuple-xor-tree-depth-wt-five-vs-six.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`, `research-journal/BREAKTHROUGHS.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/adaptive-coordinate-or-pentuple-xor-tree-depth-wt-five-vs-six/script.py`.

---

## Entry 094 — `verifier-oracle-model` / `experiments/adjacent-hamming-shells-global-parity-lemma-regression/` (2026-03-30)

- **Hypothesis:** **Global** **XOR** **π(x)=⊕ᵢxᵢ** **partitions** **{x:|x|∈{k,k+1}}** **into** **the** **two** **Hamming** **shells** **for** **every** **n,k** **(** **equivalently** **π(x)=|x|** **mod** **2** **on** **that** **union** **).**
- **Outcome:** **PASS.** **Exhaustive** **enumeration** **n=1..18,** **all** **k** **;** **sample** **consecutive-k** **opposite-parity** **for** **n∈{19,200}.**
- **Key finding:** **092** **`min_d=1`** **via** **total** **parity** **is** **the** **generic** **adjacent-shell** **separator** **(** **not** **(10,{5,6})** **-** **specific** **magic** **).**
- **Structured journal:** `research-journal/entries/2026-03-30-adjacent-hamming-shells-global-parity-lemma-regression.md`, `research-journal/index.md`, digest `research-journal/digests/verifier-oracle-model.md`.
- **Artifact:** `sub-problems/verifier-oracle-model/experiments/adjacent-hamming-shells-global-parity-lemma-regression/script.py`.
