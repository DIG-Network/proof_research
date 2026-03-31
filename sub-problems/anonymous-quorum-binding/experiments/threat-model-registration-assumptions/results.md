# Results — threat-model-registration-assumptions

**Outcome:** **PASS** (documentation / consistency)

## Summary

The scripted table partitions prior experiments by **verifier interface**, **key distribution / registration**, and **proof-system policy**, without contradiction:

- **Interface:** Entries **002**, **004** — need **`Link(C, K)`** (or equivalent), not signature check on naked `K` alone.
- **Honest random keys (toy):** Entry **007** — majority subset sums often **injective** (`U = W`).
- **Structured small integers:** Entry **006** — **`U < W`** common; not a stand-in for random keys.
- **Malicious registration:** Entry **008** — **forced aggregate collision** between two majorities.
- **Communication:** Entry **003** — naive Merkle/OR patterns fail sublinearity at majority `t`.
- **Excluded machinery:** Entry **005** — rubric for SNARK/STARK vs grey vs atomic checks.

## Interpretation

Future experiments and any **solution** or **ABANDONED** write-up should **name** the **registration** model (honest keygen vs malicious choice) alongside **`Verify`** inputs.

## Script

`python script.py` — prints table; exit code 0.
