# Hypothesis

**H (relaxation ladder):** Every **natural** way to repair the gaps identified in the journal corresponds to at least one **explicit relaxation** of the original main-problem constraints:

| Id | Relaxation | Barrier addressed (journal) |
|----|-------------|----------------------------|
| R1 | Allow **`|π| = Θ(n)`** or **`Θ(n log n)`** (e.g. Merkle path per signer) | **003**, **004** (`Link` + binding) |
| R2 | **Reveal** the cosigner set `S` or a **bitmask** of length `n` / `O(t log n)` in `π` | **002**, **004** (under-quorum without `Link`) |
| R3 | Verifier holds **more** than `(C, m, π)` — e.g. **individual `pk_i`**, or a **precomputed** table of aggregates | Violates “no individual public keys at verification time” |
| R4 | **SNARK/STARK** or **GREY** IPA-style circuit verifier | **005**; excluded by main problem |
| R5 | **Trusted setup** (e.g. KZG) for sublinear openings | Excluded by main problem |
| R6 | **TEE / trusted third party** | Excluded by main problem |
| R7 | **Novel primitive** — efficient `Link(C, K)` + threshold sig without R1–R6 | Open; not exhibited |

**Falsification:** Exhibit a fully compliant construction (main `problem-statement.md`) that uses **none** of R1–R6 and is not R7.

**Outcome expectation:** **INCONCLUSIVE** on logical necessity of R7 vs impossibility; **PASS** as a **structured** map from experiments to relaxations.
