# Notes

- **069** showed **XOR-first** tie-break still landed on the **same** tree as **067** (first feasible root **(0,1)** dominates). This experiment shows **root choice** is **not** unique: **45** pair-XOR roots admit depth-≤5 completions here, so **audited** **`π_tree`** can differ if the prover is allowed to pick among feasible roots (or if tie-break is specified differently).
- **Second** root **(0,2)** vs **first** **(0,1)**: subtree **`witness`** logic unchanged from **067**; only the **committed** root split changes. The emitted JSON differs globally (structure under the root is not a simple local patch).
- **068** (pair-OR mix) remains expensive / incomplete for **min_d**; this line stays orthogonal (XOR-only root enumeration + **067** completion).
- **Next:** If we need **canonical** **`π_tree`**, the spec must **pin** a rule (e.g. **minimal** **(i,j)** lex, or **minimal** **SHA256(JSON)`**, or **unique** feasibility). Otherwise **multiplicity** of valid witnesses is explicit on this instance.
