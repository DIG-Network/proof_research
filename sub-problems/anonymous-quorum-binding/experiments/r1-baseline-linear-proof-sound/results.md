# Results — r1-baseline-linear-proof-sound

**Outcome:** **PASS**

## What was built

- `n = 8` validators, `t = 5`, **power-of-2** Merkle tree over `H_leaf(pk_i)`.
- **`π` (conceptual):** sorted signer indices `S`, **one inclusion path per** `i ∈ S`, claimed aggregate `K = ∑_{i∈S} pk_i`, toy `σ = H(m‖K)`.
- **`Verify`:** checks `|S| ≥ t`, each path against `C`, `K` matches `pks` on `S`, and `σ`.

## Findings

- **Completeness:** honest strict-majority transcript **accepts**.
- **Soundness (toy):** `|S| = t − 1` **rejects**; wrong `K` with otherwise consistent paths **rejects**.

## Relation to main goal

- This is **relaxation R1** (Entry **010**): proof size **Θ(|S| · log n)** hash outputs — **not** sublinear when `t = Θ(n)`.
- Confirms: the **difficulty** isolated in **002–004** is **compact** `Link`, not **existence** of **any** sound interface with **linear** witness.

## Script

`python script.py` — assertions; exit code 0.
