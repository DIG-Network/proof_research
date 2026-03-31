# Notes

- **Relation to `parity-count-summary-quorum-collision`:** parity is the **m = 2** slice; lex-smallest witness there is **(0, 6)**, not **(4, 6)** — both are valid **even** residues straddling **t**.
- **General pattern (informal):** For fixed **n, t**, let **D = {k₂ − k₁ : 0 ≤ k₁ < t ≤ k₂ ≤ n}**. Then **m** threshold-aliases iff **∃ d ∈ D** with **m | d**. Here **D = {1,…,n}**, hence **m** aliases iff **m ≤ n**.
- **Implication for “compact π” narratives:** A **single** modular bucket of the **total signer count** cannot be **sublinear in log n** in this sense unless extra structure breaks the **{1,…,n}** gap coverage (different **n, t**, or correlated **k** not ranging freely).
- **Next:** If revisiting **068** (OR+coord depth), keep separate from this **scalar-quantization** line; optional: same **D** characterization for other **(n, t)** to see when **D** is a **proper** subset of **{1,…,n−t+1}** etc.
