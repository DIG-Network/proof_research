# Hypothesis

**H:** In a Merkle-per-signer witness, if `Verify` enforces `len(S) ≥ t` and valid paths for each entry of `S`, plus consistency `K = \sum_{i \in S} pk_i` **with multiplicity**, but **does not** require **pairwise distinct** signer indices (`|S| = |\mathrm{set}(S)|`), then a **single** validator index can be repeated `t` times so that verification **accepts** despite only **one** committed key participating — violating the intended “**≥ t** distinct validators” semantics.

**Falsification:** The flawed API still rejects the duplicate transcript, or the sound API incorrectly accepts.

**Expected outcome:** **PASS** (attack succeeds on flawed interface); complements **011**/`r1-baseline`, which already includes a distinctness check.
